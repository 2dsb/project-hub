---
id: idea-20260828-single-advancement-method-first-pass
title: "Single Advancement Method for First-Pass Learning"
tags:
  - learning-method
  - teach-method
  - meta-cognition
  - learning-strategy
  - pacing
summary: "The Single Advancement Method for first-pass learning states that for the same subject, the initial pass should use exactly one advancement method, usually /teach, because a second method only re-covers knowledge nodes already flipped and creates a pacing mismatch experienced as a disorienting \"time gap\" (时间差). Mixing formats on a fragile first-pass map produces interference rather than reinforcement and wastes attention as a bottleneck. The deeper rule is one method per region of the map, so two engines can coexist only if they never overlap territory. Reading during a lecture is legitimate only when it advances content /teach has not reached; otherwise spare capacity should consolidate via reflection. A second source becomes valuable only in later passes as gap-filler or map-reconstructor."
body_hash: "9fc29789"
connections:
  - type: idea
    slug: "learning-method-v2"  # auto, review: 0.581
  - type: idea
    slug: "teach-method-fixes"  # auto, review: 0.549
  - type: idea
    slug: "teach-task-volume-scaling"  # auto, review: 0.539
  - type: idea
    slug: "teach-application-scope"  # auto, review: 0.528
  - type: idea
    slug: "learning-dynamics"  # auto, review: 0.517
  - type: idea
    slug: "pass-criteria-as-curriculum-design"  # auto, review: 0.511
  - type: idea
    slug: "knowledge-map-format"  # auto, review: 0.503
importance: 0.0  # auto
---
# Single Advancement Method for First-Pass Learning

**One sentence**: For the same subject, during the FIRST pass of learning, use exactly one advancement method (pure AI, pure textbook, lecture, …) — a second method on the same pass only re-covers what the first already flipped, and the speed mismatch between the two streams produces a "time gap" (时间差) that feels wrong.

## Trigger

Morning lecture on Linear Algebra. The plan was to read the linear algebra textbook *during* the lecture. But the day before, `/teach` had pushed through the material so fast that most of the lecture's content was already learned. Two methods were running on the same first-pass material at very different speeds, and the result was a disorienting gap: the fast engine (AI, yesterday) had outrun the slow context (lecture, today), making the planned textbook reading pointless and the whole slot uncomfortable.

## The rule

For the same subject, in the first pass, use **one** advancement method — whichever is fastest/richest, usually `/teach`. Do not run a second engine (textbook, lecture, video series) on the same pass.

### Corollary — reading during a lecture

When a lecture forces a slow second context onto the same subject, reading a book during it is fine **only if it covers content `/teach` has NOT reached**. The two contexts then own disjoint territory: the lecture covers its part of the map, and the reading advances a part the fast engine hasn't touched. Reading already-covered content is exactly the redundancy the rule forbids — it recreates the "time gap." Reading uncovered content instead converts the lecture's dead time into a second productive frontier.

This reveals the rule's deeper form: the real constraint is not "one method per subject" but **one method per region of the map** — two engines can coexist as long as they never overlap territory.

> Related to [[low-occupancy-segment-reflection]]: a lecture on already-learned content is a low-occupancy segment. Its spare capacity has two legitimate allocations — consolidate what the fast engine just built (reflection) or advance a disjoint frontier (this corollary). Both are valid; re-covering the already-flipped region is the only waste.

## Why mixing hurts in the first pass

1. **The map is single-threaded** — [[fundamental-model-of-learning]] postulates that each knowledge node flips 0→1 exactly once. A second method on the same pass re-covers already-flipped nodes: zero new flips, pure redundant exposure, wasted attention ([[attention-as-bottleneck]]).
2. **Pacing mismatch = the "time gap"** — methods advance at different speeds. Running a fast and a slow engine in parallel forces the learner into the slow lane for content already mastered. The gap between the two streams is the discomfort: the plan (read textbook during lecture) collapses because the textbook became redundant.
3. **Interference on a fragile map** — two delivery formats for the same content, presented close in time, compete as similar-but-different patterns (the interference drag force in [[learning-dynamics]]). In the first pass the map is still being built; mixing formats muddies it rather than strengthens it.

## When mixing IS the right move

The rule is scoped to the **first pass** (initial construction of the map). Later passes are exactly when a new information source becomes valuable:

- [[fundamental-model-of-learning]] lists "reconstruct the map using a new information source" as one of the only two unit operations — reconstruction *from a different source* is how a built map deepens.
- [[teach-application-scope]] prescribes pairing `/teach` with textbook self-study for exam prep as **gap-filling** — that is a second pass, where mixing is the whole point.
- [[hermeneutic-circle-learning]] — each circle iteration legitimately draws on a new source to revise the map.

Refined rule: **one method owns the first pass; a second method may enter only in a later pass, where it acts as gap-filler or map-reconstructor, not as a duplicate.**

## Design implication

When a subject is also covered by an external course/lecture, decide ownership up front: either `/teach` owns the first pass and the lecture becomes review, or the lecture owns it and `/teach` is used only for gaps. A "time gap" between two streams is the symptom that two engines are both running as first-pass — coordinate them into first-pass / later-pass instead.
