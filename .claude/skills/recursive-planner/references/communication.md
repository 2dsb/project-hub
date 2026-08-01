# Communication Protocol — Recursive Planner

All inter-agent communication is file-based. No agent directly talks to another agent. This ensures context isolation, crash safety, and user auditability.

---

## Directory structure

```
<project>/.recursive-planner/
├── state.json                    ← Global state tree
├── heartbeat.log                 ← Heartbeat log
│
├── L0-overall-plan/
│   ├── requirements.md           ← C's requirements clarification records
│   ├── plan-draft.md             ← A(0)'s plan draft
│   ├── plan-review.md            ← B(0)'s review
│   ├── plan-final.md             ← Final approved plan
│   ├── overall-final-report.md   ← NEW: per-level D+E co-signed report (L0)
│   │
│   ├── step-01-<slug>/
│   │   ├── state.json            ← Step-level state
│   │   │
│   │   ├── L1-plan/              ← If complex: sub-planning
│   │   │   ├── plan-draft.md
│   │   │   ├── plan-review.md
│   │   │   ├── plan-final.md
│   │   │   ├── child-review.md   ← E(n)'s review of child sub-tree output
│   │   │   ├── overall-final-report.md  ← NEW: per-level D+E co-signed report (L1)
│   │   │   │
│   │   │   └── step-01-<slug>/   ← If recursion continues deeper (L2)
│   │   │       ├── L2-plan/
│   │   │       │   ├── plan-draft.md
│   │   │       │   ├── plan-review.md
│   │   │       │   ├── plan-final.md
│   │   │       │   ├── child-review.md
│   │   │       │   ├── overall-final-report.md  ← NEW: per-level D+E co-signed (L2)
│   │   │       │   └── ... (further recursion follows same pattern)
│   │   │       └── L2-exec/
│   │   │           ├── team-config.md
│   │   │           ├── team-review.md
│   │   │           ├── output/
│   │   │           ├── output-review.md
│   │   │           └── final-report.md   ← per-step D(n) summary
│   │   │
│   │   ├── L1-exec/              ← If not complex: direct execution
│   │   │   ├── team-config.md    ← D(1)'s team configuration
│   │   │   ├── team-review.md    ← E(1)'s team audit
│   │   │   ├── output/           ← Worker outputs
│   │   │   ├── output-review.md  ← E(1)'s output audit
│   │   │   └── final-report.md   ← per-step D(n) summary (NOT overall)
│   │   │
│   │   └── ... (further recursion if needed)
│   │
│   └── step-02-<slug>/
│       └── ...
```

**Legend — Two types of "final" reports**:
- `final-report.md` (inside `L*-exec/` directories): **Per-step** summary written by D(n) after completing a single step. Covers what the step delivered, review results, and E(n)'s verdict.
- `overall-final-report.md` (at each plan level, e.g., `L0-overall-plan/`, `L1-plan/`, `L2-plan/`): **Per-level** report co-signed by D(n) and E(n) after ALL steps at that recursion level are verified complete. Both D and E independently verify every step against plan-final.md before co-signing.

Both files appear at EVERY recursion level. The pattern is fractal: L0 has both, L1 has both, L2 has both, and so on.

---

## state.json schema

```json
{
  "skill_version": "1.0",
  "task_summary": "<one-line task description>",
  "started": "<ISO 8601 timestamp>",
  "execution_mode": "inline",
  "max_depth": 5,
  "current_depth": 0,
  "overall_status": "in_progress",
  "phases": {
    "requirements": "in_progress",
    "L0_plan": "pending",
    "L0_execution": "pending"
  },
  "steps": [
    {
      "slug": "step-01-design-gdd",
      "title": "Write Game Design Document",
      "status": "pending",
      "depth": 0,
      "complexity": "unknown",
      "sub_steps": [
        {
          "slug": "step-01-l1-exec",
          "status": "completed",
          "review_status": "PASS"
        }
      ]
    }
  ],
  "overall_review_status": null,
  "questions_for_user": [],
  "errors": [],
  "heartbeat": "<ISO 8601 timestamp>"
}
```

### Field descriptions

| Field | Values | Description |
|-------|--------|-------------|
| `execution_mode` | `"inline"` / `"cron"` | inline: spawn in current session; cron: persistent scheduled tasks |
| `overall_status` | `"in_progress"` / `"completed"` / `"cancelled"` / `"blocked"` | Top-level task state |
| `phases.*` | `"pending"` / `"in_progress"` / `"done"` | Phase status |
| `steps[].status` | `"pending"` / `"in_progress"` / `"completed"` / `"failed"` | Step status |
| `steps[].complexity` | `"unknown"` / `"complex"` / `"leaf"` | Complexity classification by D(n) |
| `steps[].sub_steps[].review_status` | `"PASS"` / `"REJECT"` / `null` | E(n)'s review verdict for this individual sub-step |
| `overall_review_status` | `"PASS"` / `"REJECT"` / `null` | D(n)+E(n) joint verdict on ALL steps at this recursion level. Set when `overall-final-report.md` is co-signed. `null` means overall check not yet performed. |
| `questions_for_user[]` | Array of strings | Questions that C needs to present to user. Format: `STATUS|[role]([level])|[event_type]|[summary]` (see Agent Status Report Format below). |
| `errors[]` | Array of error objects `{step, code, message, timestamp}` | Errors encountered during execution |
| `heartbeat` | ISO 8601 timestamp (e.g., `"2026-05-30T14:45:00Z"`) | Lightweight liveness signal. Updated by any agent after a significant action (producing an artifact, completing a review, passing a gate). For rich structured logs, see `heartbeat.log` format in `failure-handling.md`. |

---

## Read permission table

Each role reads ONLY the minimal file set needed, preventing context pollution:

| Role | Reads | Does NOT read |
|------|-------|---------------|
| C | `requirements.md`, `state.json`, `overall-final-report.md` (from any level for completion monitoring) | Any `plan-*.md` files (must not be influenced by plans) |
| A(n) | Parent `plan-final.md`, `requirements.md`, child `final-report.md` (if exists), child `overall-final-report.md` (if exists) | Sibling step files, worker internals |
| B(n) | `plan-draft.md`, `requirements.md`, parent `plan-final.md`, parent `overall-final-report.md` (if exists) | Same as A(n) |
| D(n) | `plan-final.md`, `team-config.md`, worker outputs, child `final-report.md`, child `overall-final-report.md` (if exists), `state.json` | Parent's `plan-draft.md` or `plan-review.md` (only reads final) |
| E(n) | `plan-final.md`, `team-config.md`, worker outputs, child `final-report.md`, child `overall-final-report.md` (if exists), child output files | Same as D(n) |
| Workers | `team-config.md`, task description (written by D) | Other workers' outputs, upper-level review opinions |

**C's ongoing read patterns**: C reads `state.json` periodically (not just at startup). The orchestrator notifies C when `questions_for_user[]` changes from empty to non-empty.

---

## Communication direction table

| Direction | Medium | Format |
|-----------|--------|--------|
| A(n) → B(n) | `plan-draft.md` (write file) | Markdown |
| B(n) → A(n) | `plan-review.md` (write file) | PASS or REJECT + modification list |
| C → User | Main conversation | Natural language |
| Any role → C | `state.json` → `questions_for_user[]` | String array |
| D(n) ↔ E(n) | Same-directory file reads | Markdown |
| Child → Parent | `final-report.md` (write file) | Markdown |
| Parent → Child | `plan-final.md` (child reads) | Markdown |
| E(n) → child D(n+1)+E(n+1) | `child-review.md` (write file) | PASS or REJECT + correction list |
| D(n)+E(n) → parent level | `overall-final-report.md` (co-signed write) | Per-level completion report with independent verification |
| D(n)+E(n) → C | `state.json` → `overall_review_status` | Joint verdict on all steps at this level |
| Any agent → C (status) | `state.json` → `questions_for_user[]` | Structured status message (see format below) |
| C → User (ongoing) | Main conversation | Filtered status updates, skill discoveries, requirement refinements |
| C → `state.json` | Update `questions_for_user[]` | Mark messages as "presented" after relaying to user |

---

## Agent Reporting Protocol

**Applies to**: All roles (A/B/D/E). Every agent MUST write a brief status report to `state.json` → `questions_for_user[]` at these trigger points:

- **After producing a major artifact** (`plan-draft.md`, `plan-review.md`, `team-config.md`, etc.): "I, [role](n), completed [artifact] with verdict [PASS/summary]. [1-line status]"
- **When a step is REJECTED** (any review cycle): "I, [role](n), REJECTED [step/artifact]. Reason: [1-line summary]. [N]th rejection."
- **When child agents complete at a lower level**: "Level [n+1] subtree completed for step [slug]. Result: [PASS/REJECT]. [artifact count]"
- **When discovering a useful skill**: "SKILL DISCOVERY: [skill name] applicable to [purpose]. Recommend download? [Y/N]"

C reads these reports, filters for significance, and relays to the user.

---

## Agent Status Report Format

When any agent (A/B/D/E) writes to `state.json` → `questions_for_user[]`, use this format:

```
STATUS|[role]([level])|[event_type]|[summary]
```

| Event type | Example |
|-----------|---------|
| `ARTIFACT_PRODUCED` | `STATUS\|D(0)\|ARTIFACT_PRODUCED\|team-config.md\|3 workers configured for step-03` |
| `REVIEW_PASS` | `STATUS\|E(0)\|REVIEW_PASS\|team-review.md\|Team config approved: 3 workers, parallel mode` |
| `REVIEW_REJECT` | `STATUS\|E(0)\|REVIEW_REJECT\|output-review.md\|REJECT #2: missing energy cost specs` |
| `SUBTREE_COMPLETE` | `STATUS\|D(0)\|SUBTREE_COMPLETE\|step-02\|L1 subtree done, 4 artifacts, E review PASS` |
| `SKILL_DISCOVERY` | `STATUS\|A(0)\|SKILL_DISCOVERY\|game-ui-design\|Applicable to HUD design steps. Download?` |
| `BLOCKER` | `STATUS\|D(1)\|BLOCKER\|step-03\|Cannot proceed: manager-context.md inaccessible` |
| `REQUIREMENT_GAP` | `STATUS\|D(1)\|REQUIREMENT_GAP\|step-02\|'Backup retention period' not specified in requirements` |

C reads the `[event_type]` prefix to classify and filter messages before presenting to the user.

---

## Child-Review.md Format

When E(n) reviews a child sub-tree's output (all artifacts produced at level n+1 for a given step), `child-review.md` follows this structure:

```
# Child Review — [step-slug]
Reviewer: E(n), level [n]
Child level: [n+1]
Reviewed artifacts: [list of files]

## Verdict: PASS / REJECT

## Acceptance Criteria Verification
| # | Criterion (from parent plan-final.md) | Met? | Evidence |
|---|----------------------------------------|------|----------|
| 1 | [exact criterion text]                 | YES  | [file:line or quote] |
| 2 | [exact criterion text]                 | NO   | [what's missing] |

## REJECT items (if any)
For each failed criterion:
- What the child produced
- Why it falls short
- Specific correction: what to add/change and where
```

---

## Cron mode setup

When `execution_mode` is `"cron"`:

### Task 1 — Pipeline pusher
- Cron: every 20 minutes (`"7,27,47 * * * *"`)
- Durable: true
- Prompt: "Read `<project>/.recursive-planner/state.json`. If overall_status is 'completed' or 'cancelled' → do nothing. Otherwise find the first pending step, spawn the appropriate role agent per the recursive-planner skill, update state.json after completion, git commit."

### Task 2 — Heartbeat monitor
- Cron: every 2 hours (`"13 */2 * * *"`)
- Durable: true
- Prompt: "Read `<project>/.recursive-planner/state.json` and `heartbeat.log`. Check: 1) Stalled: heartbeat > 2h old AND status not awaiting_user → mark stalled. 2) Failed: any step status='failed' → output summary. 3) Stuck: status='in_progress' AND heartbeat > 4h → revert to 'pending', reset retry_count. 4) Progress: completed/total × 100%. 5) Timeout: CP1 waiting > 72h → append reminder. Append summary to heartbeat.log."

---

## Git commit protocol

After each significant state change:
```bash
git add .recursive-planner/
git commit -m "recursive-planner: [phase/step] — [brief status]"
```

Commit messages should follow the pattern:
- `recursive-planner: requirements completed`
- `recursive-planner: L0 plan PASSED`
- `recursive-planner: step-01-design-gdd completed — L0`
- `recursive-planner: step-01 L1 plan PASSED`
