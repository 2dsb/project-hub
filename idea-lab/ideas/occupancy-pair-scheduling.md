---
id: idea-20260811-occupancy-pair-scheduling
title: "Occupancy-Pair Scheduling — a Recursive Instance of the Optimal-Curve Problem"
tags:
  - segment-model
  - scheduling
  - optimal-curve
  - recursion
  - cognitive-occupancy
  - habit-design
  - meta-model
summary: "The design of occupancy-pair scheduling across a day—alternating high-occupancy and low-occupancy segments to enable reflection via spaced retrieval and attention-residue release—is a recursive instance of the optimal-curve problem, the same structure seen at the cycle level in the practice-necessity-willingness tradeoff. Both allocate a scarce budget (cognitive capacity per day or willingness per session) across differently-costed units to maximize consolidation or mastery, making the optimal curve a scale-invariant pattern. This recursion deepens because reflection is needed most precisely when capacity is lowest—after a draining high-occupancy block—mirroring the necessity-willingness dilemma, which forces the low-occupancy segment to be exploitatively cheap rather than effortful. The invariant suggests a single design rule might propagate upward to week and month scales."
body_hash: "288f5ad3"
connections:
  - type: idea
    slug: "low-occupancy-segment-reflection"
  - type: idea
    slug: "practice-necessity-willingness-tradeoff"
  - type: idea
    slug: "teach-task-volume-scaling"
  - type: idea
    slug: "timeline-based-project-structure"
  - type: idea
    slug: "attention-as-bottleneck"  # auto, review: 0.568
  - type: idea
    slug: "learning-method-v2"  # auto, review: 0.556
  - type: idea
    slug: "three-mental-resources"  # auto, review: 0.534
  - type: idea
    slug: "learning-dynamics"  # auto, review: 0.516
importance: 2.25  # auto
---
# Occupancy-Pair Scheduling — a Recursive Instance of the Optimal-Curve Problem

## The Design Question

How to design the **timing and duration** of low-occupancy and high-occupancy segments across a day, so the reflection habit can work (`low-occupancy-segment-reflection`).

**Core constraint**: the habit needs a *pairing* — a high-occupancy segment followed by a low-occupancy one with a short gap, so the low-occupancy window can serve as spaced retrieval practice + attention-residue release.

## The Recursive Discovery

This design question turned out to be **the same problem** as the concept/practice/exam optimal curve — just at a different scale:

| Level | Units being sized | Scarce budget | Objective |
|---|---|---|---|
| **Cycle** (`practice-necessity-willingness-tradeoff`) | concept / practice / exam | willingness per session | mastery per willingness spent |
| **Day** (this idea) | high-occupancy / low-occupancy segments | cognitive capacity per day | consolidation per effort spent |

Same structure in both: **allocate a scarce budget across a sequence of differently-costed units, to maximize output.** The "optimal curve" is not one design problem — it is a *recursive pattern* that repeats at cycle level, day level, and presumably week/month level. The essence at every scale is the same.

## Design Dimensions (day level)

- **Pair structure**: alternate high → low; avoid back-to-back deep work.
- **High cap**: ~1.5–2 h — the willingness wall from `teach-task-volume-scaling`; get depth from more cycles, not longer ones.
- **Low floor**: presence > length — even a 5–15 min walk works; exploit existing idle segments before engineering new ones.
- **Gap**: immediate reflection (residue release) + sleep (offline consolidation).
- **Positioning**: high-occupancy in fresh-cognition windows (morning); low-occupancy at natural breaks (meals, commutes).
- **Cost discipline**: exploiting an existing walk costs zero; engineering a new segment costs deep-work time.

## Why the Recursion Matters

If the optimal-curve problem is recursive, a solution at one level likely transfers to all levels. Design the cycle right → the pattern tells you how to design the day; design the day right → it propagates to the week. The meta-lever is the invariant shared across scales.

## A Second Recursive Parallel: Reflection Is Needed Most When It's Hardest

The two levels share not just the optimal-curve structure — they share the same *failure mode*:

At the exact moment reflection is most valuable, capacity for it is lowest:

- **Cycle level**: at the tail of a hard practice block, exhausted — that's when consolidation matters most (you just did the work), yet willingness to reflect is at its floor.
- **Day level**: after a draining high-occupancy segment — the transition into low-occupancy is the prime consolidation window, yet the mind is most depleted precisely then.

So the necessity-willingness dilemma recurses one layer down: it is not only practice that is "needed most when hardest" (`practice-necessity-willingness-tradeoff`) — **the reflection that consolidates it is too**. A second invariant shared across scales.

**Implication for the design**: the habit cannot rely on sustained effort at the exhausted moment. It must be *cheap* (the low-occupancy constraint) precisely because it runs at capacity-minimum. The design constraint is forced, not chosen.

## Open Questions

- Does the recursion continue upward (week / month optimal curves)?
- At the day level, what is the optimal high:low ratio?
- If the pattern is scale-invariant, can a single "optimal-curve" design rule be written once and instantiated at every level?
