# Failure Handling & Risk Mitigation — Recursive Planner

---

## Failure scenarios

| Failure | Detection | Recovery | Escalation |
|---------|-----------|----------|------------|
| A(n) rejected 5 times by B(n) | B(n) counts rejections in plan-review.md | B(n) writes root cause analysis. Parent B(n-1) intervenes — the step's goal may need redefinition | Escalate to parent B(n-1) |
| Workers rejected 3 times by E(n) | E(n) counts rejections | E(n) writes root cause analysis. Not the workers' fault — step design is flawed. Parent D(n-1) + E(n-1) re-plan this step | Escalate to parent D(n-1) and E(n-1) |
| Any role produces empty/corrupted file | Parent D checks output file exists and is non-empty | Re-spawn the role agent (max 3 retries). If all retries fail → mark step as `failed`, notify C to inform user | Notify C after 3 failed retries |
| Cron tasks lost | Heartbeat monitor detects missing cron (no state update in 2 cycles) | Re-register CronCreate tasks (idempotent — checks existing tasks first) | None (self-healing) |
| User requests cancellation | C detects user says "stop" or "cancel" | C sets `overall_status: "cancelled"` in state.json. All cron tasks check this status on next wake and exit | Notify user: "Recursive planner cancelled. State preserved at .recursive-planner/" |
| Child agent timeout (WAIT expires) | D(n) spawns child agent, WAIT expires (10 min, no output). D(n) checks output file doesn't exist after timeout | D(n) re-spawns the child agent (max 3 retries). If all retries fail → D(n) marks step as `failed`, adds error to state.json, notifies C to inform user | Notify C |
| D/E disagreement on overall completion | D(n) and E(n) disagree on whether a step meets acceptance criteria during OVERALL COMPLETION CHECK (the process that produces `overall-final-report.md`). D's checklist and E's independent verification produce conflicting verdicts | E(n)'s judgment prevails (per roles.md authority hierarchy). The disputed step is marked incomplete and returned to execution. Both D and E write their reasoning to state.json errors[] | If disagreement spans 3+ steps → escalate to parent D(n-1)+E(n-1) for mediation. Both D and E write reasoning to state.json errors[] before escalating |
| E's child-review REJECT loop exceeded | E(n)'s child-review.md REJECTs child output 3 times for the same step. E(n) counts REJECTs in child-review.md history | E(n) writes root cause analysis. Step design is likely flawed, not worker quality. Parent D(n-1)+E(n-1) receive the escalation and re-plan the step | Escalate to parent D(n-1)+E(n-1) |
| C detects stale questions_for_user[] | In cron mode, questions_for_user[] has entries >24h old with no user response. C (or heartbeat monitor) checks question timestamps vs current time | C marks heartbeat.log with "STALE: questions pending >24h". On next user interaction, C proactively reminds: "Recursive planner has [N] pending questions from [timestamp]. Continue or abandon?" | None (self-healing on next user contact) |

---

## Risk-specific mitigations

### 1. Recursive depth runaway

**Risk**: Execution tree exceeds 5 levels without reaching leaf nodes.

**Trigger**: D(n) detects that the current step is at depth 5 and still classifies as "complex."

**Mitigation**: Force-stop recursion at depth 5. D(n) flags the step as `"requires_human_intervention"`, writes a summary of what's been planned so far and why it can't be further decomposed. C presents to user: "This sub-tree exceeded the maximum recursion depth of 5 levels. Here's what we have so far. Please manually review and decide: redefine the task boundary, or approve manual execution at this level?"

### 2. C question fatigue

**Risk**: C engages user in too many clarification rounds, causing frustration.

**Trigger**: C has interacted with user >= 6 rounds.

**Mitigation**: At round 6, C proactively offers: "We've gone 6 rounds of clarification. Options: (1) Pause and rethink direction, (2) Skip remaining minor questions and proceed with current information, (3) Continue clarifying." User's choice is respected.

### 3. File pollution from previous runs

**Risk**: `.recursive-planner/` directory already exists with stale data from a previous execution.

**Trigger**: Step 0 (initialization) detects existing directory.

**Mitigation**: Before any work begins, orchestrator asks user: "Detected `.recursive-planner/` from a previous run. Archive (move to `.recursive-planner.backup.<date>/`) or delete?" User confirms before proceeding.

### 4. User unresponsive (cron mode)

**Risk**: In cron mode, `questions_for_user` is non-empty but user hasn't responded for >48 hours.

**Trigger**: Heartbeat monitor detects `questions_for_user[]` non-empty AND `heartbeat` unchanged for >48h.

**Mitigation**: Mark `heartbeat.log` with "STALE: user unresponsive >48h." On next user interaction with AI, C proactively reminds: "The recursive-planner task from [date] is waiting for your response. Continue or abandon?"

### 5. Context pollution across roles

**Risk**: A role reads more files than necessary, contaminating its independent judgment.

**Trigger**: Role output shows signs of being influenced by files it shouldn't have read (e.g., A's plan using B's review language, or C referencing plan details).

**Mitigation**: Enforce read-permission table strictly (see `communication.md`). Each role's agent prompt explicitly lists "Files you read" and "Files you do NOT read." Orchestrator (SKILL.md) passes only the allowed file paths when spawning each role.

### 6. Single point of failure in state.json

**Risk**: `state.json` gets corrupted, and the entire execution state is lost.

**Mitigation**: Git commits after every state change create a natural backup trail. If `state.json` is corrupted, read the latest git version: `git show HEAD:.recursive-planner/state.json`. The orchestrator also writes a backup copy `state.json.bak` before every write.

### 7. C cron-mode availability gap

**Risk**: In cron mode, C's "ongoing monitoring" depends on the orchestrator being able to re-invoke C when questions arise. Cron fires on a schedule, not on demand. This means C might be unavailable for hours between cron fires, defeating the "ongoing" purpose for time-sensitive status updates.

**Trigger**: Cron-mode execution detected (mode="cron" in state.json). questions_for_user[] contains entries that have not been processed within 2 cron cycles.

**Mitigation**:
- At each cron fire, the orchestrator checks questions_for_user[] FIRST (before proceeding with the next step). If non-empty, C is spawned synchronously within that cron fire to process all pending messages.
- For inline mode, this is not an issue — C is available on-demand.
- Acceptable latency: in cron mode with 15-min intervals, worst-case status update delay is 15 minutes. This is documented in the user manual.
- For truly time-sensitive blockers (child timeout, unrecoverable REJECT), C writes a heartbeat.log entry with "URGENT" flag. The orchestrator, on next fire, sees URGENT and processes it before any other work.

---

## Graceful degradation

If the orchestrator (main SKILL.md agent) itself fails or the session is lost:

1. **Inline mode**: User re-invokes the skill. Orchestrator reads `state.json`, detects which phase was in progress, resumes from the last git-committed state.
2. **Cron mode**: Cron tasks continue running independently. User can check status with `cat .recursive-planner/state.json` or `cat .recursive-planner/heartbeat.log`.
3. **Worst case**: All state is lost but `.recursive-planner/` directory exists. Manually inspect the directory tree:
   - **Completed steps** have `final-report.md` (per-step, inside `L*-exec/` directories)
   - **Completed levels** have `overall-final-report.md` (per-level, D+E co-signed, at each plan level directory)
   - **In-progress steps** have partial files
   User can decide to restart from scratch or salvage completed work.
4. **D/E wait failure**: If D spawns children but the session is lost before E reviews, the child sub-tree's output files still exist on disk. On recovery, the orchestrator detects completed child artifacts without corresponding E reviews and re-spawns E to perform the missing reviews.

---

## Log format (heartbeat.log)

Two formats are used for heartbeats:

### 1. state.json `heartbeat` field
- **Format**: ISO 8601 timestamp only (e.g., `"2026-05-30T14:45:00Z"`)
- **Updated by**: Any agent after a significant action (producing an artifact, completing a review, passing a gate)
- **Purpose**: Lightweight liveness signal for the heartbeat monitor
- **See**: `communication.md` for the full state.json schema

### 2. heartbeat.log entries
- **Format**: `[ISO 8601 timestamp] <TYPE> | <field1>=<value1> | <field2>=<value2> | ...`
- **Fields are TYPE-dependent** (see table below)
- **Written by**: The heartbeat monitor (cron Task 2) and any agent reporting exceptional conditions (STALLED, BLOCKED, STALE, URGENT)
- **Agents do NOT write routine HEARTBEAT entries to heartbeat.log** — they only update `state.json` heartbeat

#### Entry types and required fields

| Type | Required fields | Written by |
|------|----------------|------------|
| HEARTBEAT | status, phase, steps_done, questions_pending | Heartbeat monitor only |
| STALLED | status, heartbeat_age, last_action | Heartbeat monitor only |
| BLOCKED | questions_for_user, awaiting_user_since | C or heartbeat monitor |
| STALE | user_unresponsive_duration, last_user_interaction | Heartbeat monitor only |
| URGENT | reason, flagged_by | Any agent (child timeout, unrecoverable REJECT) |

#### Field definitions

| Field | Values/format | Description |
|-------|--------------|-------------|
| status | in_progress / completed / cancelled / blocked | Current overall_status |
| phase | requirements / L0_plan / L0_exec / L[N]_exec | Current active phase |
| steps_done | N/M | Completed steps / total steps at current level |
| questions_pending | integer | Current length of questions_for_user[] |
| heartbeat_age | e.g., 2.5h | Time since last state.json heartbeat update |
| last_action | filename | Last artifact produced (e.g., plan-review.md) |
| awaiting_user_since | ISO timestamp | When user was last prompted |
| user_unresponsive_duration | e.g., 48h | Time since last user interaction |
| reason | free text | Why the URGENT flag was raised |
| flagged_by | role(level) | Which agent raised the URGENT flag |

#### Examples

```
[2026-05-29T14:32:00Z] HEARTBEAT | status=in_progress | phase=L0_plan | steps_done=0/5 | questions_pending=0
[2026-05-29T14:52:00Z] HEARTBEAT | status=in_progress | phase=L0_exec | steps_done=2/5 | questions_pending=0
[2026-05-29T15:12:00Z] STALLED | status=in_progress | heartbeat_age=2.5h | last_action=plan-review.md
[2026-05-29T15:32:00Z] BLOCKED | questions_for_user=2 | awaiting_user_since=2026-05-29T14:00:00Z
[2026-05-29T16:00:00Z] STALE | user_unresponsive_duration=48h | last_user_interaction=2026-05-27T16:00:00Z
[2026-05-29T16:05:00Z] URGENT | reason=child_timeout_step03 | flagged_by=D(1)
```
