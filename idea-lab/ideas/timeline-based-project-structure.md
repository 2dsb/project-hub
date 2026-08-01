---
id: "idea-20260626-slp01"
summary: "Any project’s state can be losslessly represented by memory, artifacts, and physical capacity, where physical capacity is a global constraint that gates all work, decaying during deep work and recovering through rest and exercise. The study–slack oscillator shows that intense cognitive sessions deplete physical capacity via poor sleep, triggering recovery gaps, while rhinitis asymmetrically drains motivation during slack phases, making external social triggers the most reliable escape. The foundational strategy is a hard 20:30 cutoff for cognitive work to preserve physical capacity, enabling project rotation and exercise as physical‑capacity management."
title: "Timeline-Based Project Structure"
tags: [time-management, project-structure, meta-cognition, daily-flow, energy-management, recovery, physical-health]
importance: 6.58  # auto
connections:
  - type: idea
    slug: learning-pipeline
  - type: idea
    slug: deep-work-recovery-cycle
  - type: project
    slug: daily-exercise
  - type: idea
    slug: "willingness-experiment"  # auto
---
# Timeline-Based Project Structure

> Status: active development — original framework (2026-06-26) + Physical Capacity extension from deep-work-recovery-cycle (2026-07-05) + bidirectional oscillator model + exercise-as-P-management + strategy priority hierarchy (2026-07-07).

## 1. Core Intuition

This is NOT about learning specifically. It's a **universal structure** that any project lives within.

The structure unfolds on a **timeline**: you have several existing projects. Every day's waking hours — outside of rest, meals, and other maintenance — are spent *inside* one project or another. The timeline IS the container.

## 2. Time-Block Allocation

A single project is experienced in **time blocks** across a day — e.g., 08:00–12:00 Deep Learning, 13:00–14:00 running. The day is a sequence of project-slotted intervals.

## 3. The Project Dimension

From a single project's perspective, the key feature is **when the project gets worked on** — e.g., DL reading yesterday 10:00–17:00, today 08:00–12:00. This is the project's temporal footprint.

### 3.1 Memory (M)

"Memory" describes my **mastery of specific content** within the project — at every level, from the highest architecture to the lowest detail.

- **Time away from the project** → memory **decays**
- **Time spent on the project** → memory **deepens**

Memory is a state variable that rises and falls with engagement.

### 3.2 Related Artifacts (A)

The set of everything in "real life" connected to the project — files, books, notes, tools, data, references. Everything outside the mind that belongs to the project.

### 3.3 Physical Capacity (P)

> Added 2026-07-05 from deep-work-recovery-cycle observations. Extended 2026-07-07 with exercise pathway analysis.

A third dimension that the original `(M, A)` model missed: **physical capacity** — the body's ability to sustain cognitive work.

Key properties of P:

- **P is a constraint, not a driver** — it doesn't push toward completion; it gates whether any work can happen at all
- **P is global, not project-specific** — a single shared resource across all projects (unlike M, which is per-project)
- **P decays during deep work** (cumulative physical cost) and recovers during rest
- **P has a floor** — below a certain threshold, no project work is possible regardless of M or willingness

**The P equation:**

```
P_next_day = P_baseline(t) + exercise_short_term_boost(yesterday) - sleep_quality_penalty(cognitive_arousal_before_bed)
```

Where:

| Term | Time Scale | Mechanism |
|------|-----------|-----------|
| `P_baseline(t)` | Weeks to months | Underlying physical condition. **Not static** — drifts up with consistent exercise over time, decays with prolonged inactivity. This is the *floor* — the P value you return to after a good night's sleep with no recent exercise. |
| `exercise_short_term_boost` | 24-48 hours | Temporary P increase from yesterday's physical activity. A single workout gives a one-day bump but doesn't meaningfully change baseline. |
| `sleep_quality_penalty` | Daily | Function of cognitive arousal proximity to bedtime. The closer intense thinking is to sleep, the larger the penalty. Can be negative — bad sleep can reduce P below baseline. |

And the baseline itself evolves:

```
P_baseline(t) = P_baseline_initial + cumulative_exercise_effect(history) - cumulative_inactivity_decay(history)
```

- `cumulative_exercise_effect`: slow accumulation — consistent exercise over weeks gradually raises the baseline. 10 minutes daily for a month does more for baseline than a single 2-hour session.
- `cumulative_inactivity_decay`: slow erosion — without exercise, baseline drifts back down. The decay isn't linear; it accelerates the longer inactivity continues.

**Why the distinction matters:**

- A single workout gives you a one-day P bump (short-term boost) but the baseline hasn't moved
- Consistent workouts over weeks raise your *floor* — even on days you skip exercise, your baseline is higher than it was a month ago
- Stopping exercise doesn't just remove the short-term boost — the baseline itself gradually erodes back down
- The hard cutoff eliminates the daily penalty term. Exercise raises both the short-term boost and (slowly) the baseline. They operate on different time scales and can't substitute for each other.

**The mechanism that depletes P:**

```
Deep work burst (high intensity, long duration)
  → cognitive arousal before bed (mind won't shut off)
  → sleep disruption (late nights, poor quality)
  → exercise deficit (time displacement, physical neglect)
  → physical exhaustion
  → mandatory recovery gap (1-3 days of zero productivity)
```

The critical variable is **how close to bedtime cognitive work happens**. Games/videos at 21:00 → low arousal → good sleep. Studying until 22:00+ → high arousal → wrecked sleep. The cost isn't just one bad night — it's the 1-3 day productivity gap that follows.

**The 70/70 mask:** Daily mental/physical scores can mask accumulating physical debt because they're **point measurements, not cumulative ones**. A score of 70/70 captures "how I feel right now" but not the physical debt accruing across days.

### 3.4 Core Hypothesis: The (M, A, P) State Representation

A project's **complete state** can be represented as the tuple `(memory, artifacts, physical_capacity)` — and this representation is **lossless**.

- **Memory** carries all internal state: knowledge, intuitions, intentions, priorities, emotional associations, procedural know-how, current position
- **Artifacts** carries all external state: outputs, resources, records, tools
- **Physical Capacity** gates whether any transition can occur: a global constraint shared across all projects

There is no fourth category. Everything about "what state is the project in and can it move" is either in your head, in the world, or in your body.

## 4. State Transition Dynamics

### 4.1 Within a Session

A time block on a project is a state transition:

```
(M₁, A₁, P₁, t₁)  →  (M₂, A₂, P₂, t₂)
```

where `t₁` is start time, `t₂` end time, and `(t₂ - t₁)` is duration. P typically decreases during the session (cumulative fatigue). M typically increases (learning). A may change (new notes, outputs).

### 4.2 Between Sessions (Gap Dynamics)

When the project is **not** being worked on:

- **M always decays**
- **P recovers** (sleep, rest) — but only if sleep quality is good. If cognitive arousal before bed disrupts sleep, P recovery is partial or negative
- **A may or may not change**, depending on project type:

| Type | Artifact Behavior During Gaps | Example |
|------|------------------------------|---------|
| **Static-artifact** | A stays constant | Deep Learning (book, notes don't change) |
| **Dynamic-artifact** | A evolves autonomously | Running (body recovers, then fitness decays) |

### 4.3 Next Session

```
(M₃, A₃, P₃, t₃)  →  (M₄, A₄, P₄, t₄)
```

Static-artifact: you pick up exactly where you left off externally. Dynamic-artifact: the world moved while you were away. Both are gated by P₃ — if P is below floor, the transition doesn't happen at all.

## 5. The A⇄B Oscillator: Study ⇄ Slack Dynamics

> Added 2026-07-07 from empirical observation across ~30 days.

Over a month, each day is either A (studying/productive) or B (slacking off). The pattern forms alternating blocks: AAABBBBBBAAAAAAAABBBBAAAAAABBBBBB. Each transition has a triggering moment.

### 5.1 A→B Triggers (Study → Slack)

Three reasons the system switches from productive to slack:

| Trigger | Type | Mechanism |
|---------|------|-----------|
| **Willingness fatigue** | Internal, project-specific | N consecutive days on the same project drains willingness. Not about content difficulty — about the *pattern* of consecutive engagement. |
| **P depletion** | Internal, global | Physical capacity drops below floor. All projects stall simultaneously — the key diagnostic that distinguishes this from willingness fatigue. |
| **Capability blockage** | Internal, project-specific (rare) | Hit something you literally can't do yet (missing prerequisite, tool doesn't exist). Not unwillingness — you're *blocked*. Switching to a different project would work fine. |

In practice, willingness fatigue and P depletion often arrive together after an intense burst (the deep-work-recovery-cycle pattern). Capability blockage is rare — the first two cover ~90% of A→B transitions.

### 5.2 B→A Triggers (Slack → Study)

The reverse transition has two trigger types:

| Trigger | Type | Mechanism |
|---------|------|-----------|
| **Leisure satiation** | Internal | The inverse of continuity fatigue. After N consecutive days of slacking, games/videos become stale. B depletes itself just like A does. |
| **Social gravity** | External | Someone else applies a force the system can't generate internally — e.g., a friend invites you to study together. This bypasses the need to self-generate motivation. |

Unlike internal triggers (leisure satiation), external triggers don't depend on your current mental state to fire — they arrive from outside the system. This makes them disproportionately important when the rhinitis drain has suppressed internal motivation.

### 5.3 The Rhinitis Asymmetric Drain

> Observed 2026-07-07.

Allergic rhinitis acts as a **persistent debuff** that continuously drains mental score. But the drain is asymmetric across the two phases:

```
A (study):     rhinitis debuff ↓  vs.  study engagement ↑  →  net: roughly stable or slightly up
B (slack):     rhinitis debuff ↓  with nothing counteracting  →  net: continuous decline
```

During A, the act of studying itself boosts mental state, offsetting the rhinitis drain. During B, there's no counter-force — the drain runs unchecked. This means:

- **B is not neutral recovery time.** It's a **descending slope**.
- The longer B runs, the deeper the hole gets, and the harder it becomes to generate an internal trigger (leisure satiation) to switch back.
- By the time leisure satiation would naturally kick in, mental score may have dropped so far that the startup cost is enormous.

### 5.4 Why B Phases Overshoot

B phases consistently exceed the plan because:

1. The rhinitis drain compounds daily — each day in B makes the next day in B *more likely*
2. Self-generated motivation (leisure satiation) requires a certain mental floor to activate — and the drain may push below that floor before satiation arrives
3. This creates a trap: the only reliable escape is an **external trigger**, which is unpredictable

This explains why external triggers are disproportionately important — they don't just help; they may be the *only* reliable B→A mechanism when the rhinitis drain is active.

### 5.5 The Gap Type Diagnostics (Updated)

| Gap Type | Cause | Scope | Signal | Recovery Mechanism |
|----------|-------|-------|--------|-------------------|
| **Avoidance gap** | Low willingness, task too hard | Project-specific | Only that task is avoided | Lower the bar, change approach |
| **Continuity fatigue** | N consecutive days on same project | Project-specific | Relieved by switching domains | Work on a different project |
| **Capability blockage** | Missing prerequisite knowledge | Project-specific | Can't proceed even with high willingness | Acquire prerequisite, then return |
| **Recovery gap** | P depletion (physical cost from deep work) | Global | All projects stall simultaneously | Rest, sleep, exercise — time |
| **Rhinitis spiral** | Asymmetric drain during B phase | Global | B extends beyond plan, worsening daily | External trigger (social), or wait for leisure satiation to beat the drain |

**Key diagnostic:** If *all* projects stall simultaneously → P depletion or rhinitis spiral. If *one* project stalls → avoidance, fatigue, or blockage.

## 6. Willingness: The Transition Force

The `(M, A, P)` representation captures state, but it does not capture the **force that drives state transitions**: willingness.

### 6.1 Two Opposing Forces

| Force | Direction | Description |
|-------|-----------|-------------|
| **Continuity fatigue** | Away from the project | N consecutive days of engagement with the same project drains willingness. The fatigue is about the *pattern* of consecutive same-project engagement itself. |
| **Milestone gravity** | Toward the project | Proximity to a completion point exerts a pull. The closer to "done," the more uncomfortable it feels to walk away. |

Willingness sits in a tension field: `willingness = f(milestone_pull, continuity_fatigue, ...)`.

### 6.2 Willingness × Memory Interaction

| State | Description |
|-------|-------------|
| High M + low willingness | You *could* continue (you remember everything), but you *don't want to* |
| Low M + high willingness | You *want to* continue, but reconnection cost is high |
| Low M + low willingness | Project is effectively dead without intervention |
| High M + high willingness | Optimal state, rare and fragile |

### 6.3 Willingness × Physical Capacity

| State | Description |
|-------|-------------|
| High willingness + low P | You *want to* work, but your body won't cooperate — frustrating |
| Low willingness + high P | You *could* work, but don't want to — this is where external triggers help most |
| Low willingness + low P | Compound stuck state — the B-phase trap |
| High willingness + high P | Optimal — rare, protect it when it appears |

### 6.4 Willingness in the Oscillator

Willingness explains the A→B direction (continuity fatigue), but the B→A direction requires a different concept: **leisure satiation** — the willingness to stop slacking. Together they form a two-state depletion/recovery cycle:

```
A: willingness to study depletes → B triggered
B: willingness to slack depletes → A triggered (if rhinitis drain hasn't blocked it)
```

### 6.5 Willingness Across Project Types

Different projects have different willingness failure modes. This matters for P-management strategies like exercise, which is itself a project subject to willingness dynamics:

| Project Type | Primary Willingness Killer | Fix |
|-------------|---------------------------|-----|
| **Study (cognitive)** | Continuity fatigue — same domain drains it | Project rotation |
| **Exercise (bodyweight, indoor)** | Boredom — same movements daily, no completion point | Variety — rotate in new movements weekly |
| **Exercise (outdoor/gym)** | Activation energy — travel, setup, heat, equipment | Eliminate friction — zero-setup indoor alternatives |

Exercise doesn't solve the willingness problem — it **inherits** it. The same system that governs whether you study also governs whether you exercise. But the failure modes are different: study willingness dies from continuity fatigue (same domain); exercise willingness dies from boredom (same movements) or activation energy (friction). Different killers, different fixes.

### 6.6 Open Sub-Questions

- What resets continuity fatigue? Is it simply time away, or does working on a *different type* of project count as rest?
- Does milestone gravity scale nonlinearly with progress? (e.g., is 80%→100% more magnetic than 20%→40%?)
- Can reconnection docs also serve willingness by lowering the psychological startup cost?
- What determines the relative speed of leisure satiation vs. rhinitis drain? Can we predict which will win for a given starting state?
- Does exercise willingness fail at the same time and for the same reasons as study willingness, or can they offset each other? (If study willingness is low, can exercise willingness still be high — giving you a P boost even during a B-like period?)
- How often does boredom kill exercise willingness? What's the minimum variety needed to prevent it?

## 7. Ideal State & Value Objective

### 7.1 Ideal State

```
IdealState_i(T) = (M_ideal(T), A_ideal(T))
```

A time-varying target — where the project *should* be at time T. The actual state `(M, A, P)` is measured against this. P constrains whether you can close the gap.

### 7.2 Value: Self-Transformation Delta

For each project, **value_i** is the answer to: *Assuming I complete this project, what is the difference between me-after-completion and me-before-completion?*

From a lifetime perspective, value is the self-delta the project produces.

### 7.3 Uncertainty & Convergence

From the **current state**, value_i is a **probability distribution** — uncertain because the future is uncertain. From a **future state** (after completion), the distribution **collapses** to a fixed value.

### 7.4 The Objective

Maximize total self-transformation value across all projects:

```
max ∑ value_i(T)
```

Tension is a decision signal, not the objective:

```
tension_i(T) = E[value_i | completion] - E[value_i | current (M,A,P)]
```

The expected value gap between completing now and staying where you are. It tells you *what you'd gain by switching*, but the objective remains max ∑ value_i.

## 8. Reconnection Docs: An Optimization

Reconnection docs are a special kind of **artifact (A)** whose sole function is to **rapidly restore memory (M)** after a gap. They don't advance the project directly — they compress M into A so that decoding cost is minimal (≤30s).

In value terms: reconnection docs lower the maintenance cost of keeping a project recoverable, increasing the feasible number of concurrent projects under a fixed time budget. They partially neutralize the M-decay penalty, making the A⇄B oscillator less costly — you can re-enter A faster after a B phase.

## 9. Practical Implications

### 9.1 Hard Cutoff for Cognitive Work

The Deep Work II block (originally 19:00–22:00) is actively harmful — studying until 22:00 reliably produces bad sleep, which triggers P depletion and entry into the B phase. **Hard cutoff: 20:30.** After cutoff: recreational wind-down only.

This contradicts the "energy peak 14:00–22:00" assumption — peak cognitive output might happen in that window, but using the full window destroys the next day.

### 9.2 Weaponizing External Triggers

Since external triggers (social gravity) are often the only reliable B→A mechanism when the rhinitis drain is active, the most reliable strategy is to **pre-plant them**:

- Schedule a study session with someone for a specific future time *while still in A*
- The commitment acts as a planted trigger — when B is running and the rhinitis drain has suppressed internal motivation, the pre-existing social commitment pulls you out
- This transforms an unpredictable rescue into a scheduled one

Unlike internal triggers (leisure satiation), external triggers don't depend on your current mental state to fire — they arrive from outside the system.

### 9.3 Minimizing B-Phase Duration

Since B is a descending slope (not neutral recovery), the goal isn't to prevent B entirely — it's to:

1. **Prevent unnecessary B entry** — hard cutoff protects P, reducing A→B transitions driven by P depletion
2. **Shorten B when it happens** — pre-planted external triggers provide an escape route that doesn't depend on internal state
3. **Keep a "minimum viable A" during B** — something so trivial it doesn't feel like studying: open one page, read one paragraph, write one sentence. It doesn't advance any project — it just keeps the door to A from locking completely. This also partially offsets the rhinitis drain by providing a tiny engagement boost, slowing the descent.
4. **Accept some B as inevitable** — the oscillator is the natural rhythm; the problem is overshoot, not the rhythm itself

### 9.4 Exercise as P-Management

> Added 2026-07-07.

Exercise raises P baseline, giving more buffer against the sleep-quality penalty. But the strategy has a structural problem: **exercise is itself a project**, and therefore subject to willingness dynamics (§6.5).

**The barrier in practice:**

Every conventional exercise option has a dealbreaker that exceeds willingness:

| Option | Blocker | Willingness Killer |
|--------|---------|-------------------|
| Gym | 30min subway, none in hometown | Activation energy |
| Running | Boring, stretching overhead too high | Boredom + activation energy |
| Cycling | No bike | Access |
| Swimming | No pool | Access |
| Any outdoor | Too hot (summer in hometown) | Physical discomfort |

The common thread: every option has **startup friction** that exceeds willingness to do it. The only viable path is **zero-friction indoor bodyweight exercise** — no leaving the house, no equipment, no setup time.

**The minimum viable threshold:**

The goal isn't fitness — it's P management. So "enough" means: *you did it, and your body registered it.* The bar is low on purpose:

```
3 rounds × (push-ups + squats + plank)
```

The numbers don't matter. What matters is that there are numbers and you hit them. The real rule: **if after finishing you think "that was too easy," don't add more — save it for next time.** The willingness killer is dread before starting, not the workout itself. Keeping it too easy protects willingness. You can scale up later; you can't recover from quitting.

**Progression system:**

Track one number at a time. Each session: match the other two, push one up by 1-2 reps or 5s on plank. That's the whole system. The only metric that matters: *did you do it again?*

**Boredom prevention:**

Once the baseline routine is stable (≥1 week), the willingness failure mode shifts to boredom — same 3 movements daily. The fix: rotate in a new movement every week. 3 movements is enough for 10 minutes, but they don't have to be the *same* 3 forever. Recommended expansion source: *You Are Your Own Gym* (Mark Lauren) — 125 bodyweight-only exercises, pre-built programs, no philosophy filler.

### 9.5 Strategy Priority: Hard Cutoff as Prerequisite

> Added 2026-07-07 from Ch5→gap empirical proof.

The Ch5 reconnection doc case revealed a critical dependency:

```
Ch5 deep work (intense, 116 concepts)
  → P crashed + willingness fatigued simultaneously
  → You noticed the fatigue, correctly diagnosed it, planned project rotation for next day
  → But P was already below floor
  → Rotation plan couldn't execute — P overrides everything, including your own intentions
  → 3-day B phase
```

The rotation strategy was sound. It failed because **P overrides everything** — including your own plans to switch projects. When P is below floor, it doesn't matter what you *intend* to do the next day. You can notice willingness fatigue perfectly and still be powerless if P has already crashed.

This means the two A→B prevention strategies aren't equal peers:

| Strategy | What it prevents | What it depends on |
|----------|-----------------|-------------------|
| **Hard cutoff** | P depletion | Almost nothing — it's a *stop* action |
| **Project rotation** | Willingness fatigue | P must be adequate to execute |
| **Exercise** | Low P baseline | Willingness to exercise must be present |
| **External triggers** | Prolonged B | Someone else must be available |
| **Minimum viable A** | Rhinitis drain spiral | Barely any willingness — very low bar |

The hard cutoff is the **prerequisite** for every other strategy to function. Without it, rotation, exercise, reconnection docs — none of them can execute. It's not the highest-leverage strategy; it's the foundation the others rest on.

**The dependency chain:**

```
Hard cutoff (20:30)
  → P stays above floor
    → Project rotation can actually execute
    → Exercise willingness isn't undermined by P crash
    → External triggers have a functional system to pull you back into
```

Cut the hard cutoff, and the entire chain collapses. The answer to "fewer A→B" is simpler than a full strategy menu: **hard cutoff first, everything else second.**

## 10. Open Questions

### 10.1 Cross-Project Coupling

The (M, A, P) representation treats each project as independent, but they're not:

- **Hierarchical** (parent-child, e.g., AI ↔ DL Book): parent's M is partially composed of child's M
- **Shared substrate** (e.g., running ↔ other physical activities): A_dynamic of one project feeds into another
- **Knowledge transfer**: Learning X can raise M in project Y without Y being a formal child of X

How do you model these interactions without collapsing everything into one giant coupled system?

### 10.2 Detecting Incoming Gaps

- Can we detect an incoming recovery gap before it hits? (sleep hour tracking, exercise day count, consecutive deep-work days)
- Is there a "safe" deep-work intensity that doesn't trigger the cycle? What's the threshold?
- Does the recovery gap scale with the depth of the work? (116 concepts → 3-day gap; would a lighter session produce a shorter gap?)

### 10.3 Oscillator Tuning

- What determines the relative speed of leisure satiation vs. rhinitis drain? Can we predict B-phase duration from starting state?
- Does the *type* of B activity matter? (games vs. videos vs. social — different satiation rates?)
- Can we measure "distance to B→A trigger" the way we measure "distance to completion set"?
- What resets continuity fatigue — time away, or domain switching? Does working on a *different type* of project count as rest for willingness?

### 10.4 Rhinitis Modeling

- Is the rhinitis drain rate constant, or does it vary with season/medication/sleep?
- Can the drain be measured? If daily mental scores capture it, the A-phase scores should be systematically higher than B-phase scores at the same "true" baseline
- Does medication timing (every 4 weeks) create predictable windows of higher vulnerability?

### 10.5 Exercise Integration

- Does exercise willingness fail at the same time and for the same reasons as study willingness, or can they offset each other? If study willingness is low (during B), can exercise willingness still be high — giving a P boost even during a B-like period?
- What's the minimum exercise frequency needed to maintain P baseline? (3×/week? daily?)
- Does exercise timing matter for P? (morning vs. afternoon vs. evening — different effects on sleep quality and next-day P?)
- How fast does the exercise→P boost decay after stopping? (1 day? 3 days? a week?)

### 10.6 Plan Integration

- Should the M7 planner have a "recovery day" mode distinct from "low energy day" — not low daily energy, but accumulated physical debt?
- Can the planner incorporate the oscillator model to predict when a B phase is likely and pre-schedule external triggers?
- Should the planner treat exercise as a fixed daily slot (like meals) rather than an optional project — acknowledging that its willingness dynamics are different and its function is maintaining the system's ability to execute other plans?
