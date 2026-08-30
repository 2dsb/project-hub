---
id: idea-20260811-teach-task-volume-scaling
title: "Teach Cycle Task Volume Scales with Content Complexity — Fatigue and Aversion Walls"
tags:
  - teach-method
  - learning-design
  - task-volume
  - cognitive-fatigue
  - aversion
  - spacing
  - curriculum-design
summary: "In the /teach method, practice + exam volume inflates with content complexity, causing late-stage mental fatigue and single-domain physiological aversion that force partial completion and deferral, which fragments the cycle and leaves Zeigarnik residue. This violates the method’s own prescriptions for short, spaced sessions and working-memory-friendly chunk sizes, because 5–6 hours of practice are delivered in one sitting without interleaving. The missing design parameter is a volume cap on the cycle: complexity should raise cycle count, not cycle size, constrained to a session-scale budget. The solution involves decomposing complex cycles into multiple sessions, front-loading hard material, and applying interleaving at the cycle level to prevent single-domain satiation. Aversion and deferral should be treated as design failures, not personal ones."
body_hash: "bf8115bb"
connections:
  - type: idea
    slug: "timeline-based-project-structure"
  - type: idea
    slug: "practice-necessity-willingness-tradeoff"
  - type: idea
    slug: "occupancy-pair-scheduling"
  - type: idea
    slug: "learning-method-v2"  # auto
  - type: idea
    slug: "teach-method-fixes"  # auto
  - type: idea
    slug: "attention-as-bottleneck"  # auto
  - type: idea
    slug: "pass-criteria-as-curriculum-design"  # auto, review: 0.593
  - type: idea
    slug: "enumerative-as-scaffold-for-generative"  # auto, review: 0.569
  - type: idea
    slug: "three-mental-resources"  # auto, review: 0.559
  - type: idea
    slug: "memorization-in-pipeline"  # auto, review: 0.546
  - type: idea
    slug: "learning-pipeline"  # auto, review: 0.538
  - type: idea
    slug: "practice-as-learning-purpose"  # auto, review: 0.534
  - type: idea
    slug: "low-occupancy-segment-reflection"  # auto, review: 0.532
  - type: idea
    slug: "willingness-experiment"  # auto, review: 0.520
  - type: idea
    slug: "hermeneutic-circle-learning"  # auto, review: 0.517
  - type: idea
    slug: "goal-singularity"  # auto, review: 0.514
  - type: idea
    slug: "learning-dynamics"  # auto, review: 0.508
  - type: idea
    slug: "teach-application-scope"  # auto, review: 0.537
  - type: idea
    slug: "single-advancement-method-first-pass"  # auto, review: 0.539
importance: 3.29  # auto
---
# Teach Cycle Task Volume Scales with Content Complexity — Fatigue and Aversion Walls

## Trigger

Observed across two /teach tracks: the practice + exam phase of a learning cycle inflates with content complexity. Past a certain size, the user hits two walls that force partial completion and deferral to the next day.

## Observation: cycle time is a function of content complexity

| Track | Complexity | Concept | Practice + Exam | Total cycle |
|---|---|---|---|---|
| teach-HTML | simple | ~20 min | ~40 min | ~1 h |
| teach-openclaw-companion | complex | 2–3 h | 5–6 h | 7–9 h |

The design intent is roughly one cycle per session, but the volume is a **dependent variable**: it scales "proportionally" with the knowledge complexity. A "session" silently becomes a marathon.

## Two failure walls

1. **Late-stage mental fatigue**: Sustained deep thinking on complex content drains the learner by the later stages of the cycle. The last practice tasks are attempted with a depleted cognitive tank, so quality collapses exactly where it matters most (consolidation).

2. **Single-domain physiological aversion**: Prolonged uninterrupted exposure to one type of knowledge (e.g., technical) triggers an almost physical repulsion — "I can't even look at it anymore." This is attention-level satiation, the learning equivalent of food satiety.

## Result

Practice + exam get done **partially**, then cannot continue; the remainder is pushed to tomorrow. The deferral fragments the cycle and breaks the cadence the method depends on — and carries Zeigarnik residue into the next day.

## Structural insight

The /teach method itself prescribes short lessons ("completable very quickly", working memory is very small) and **spacing** / **interleaving** as desirable difficulty. But the practice/exam volume for complex content violates both prescriptions:

- It is not decomposed into spaced sessions — 5–6 hours of practice are delivered in one sitting.
- It exceeds any working-memory-friendly chunk size.

So the missing design parameter is a **volume cap on the cycle**. Complexity should raise the *number of cycles*, not the *size of each cycle*. The cycle must be budgeted at session scale and decomposed, rather than allowed to scale unboundedly with content.

## Design directions (open)

- Cap practice volume per session (e.g., ~1.5–2 h), splitting a complex cycle across multiple sessions.
- Let complexity raise cycle *count*, not cycle *size*.
- Front-load the hardest material while cognition is fresh; leave lighter consolidation for the tail.
- Apply interleaving at cycle level, not just within a practice, to break single-domain satiation (the method already prescribes interleaving for skills practice).
- Treat "deferral to tomorrow" as a signal that the cycle exceeded its budget — a design failure, not a personal one.

## Open questions

- What is the maximum sustainable single-domain session length before aversion kicks in?
- Does aversion come from total volume, or from the lack of interleaving / task variety?
- Is the fix better placed in /teach (a hard design constraint) or in the user's session planning layer?
