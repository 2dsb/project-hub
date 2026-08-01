---
id: "idea-20260719-leverage-existing-vs-build-from-scratch"
title: "Leverage Existing Solutions vs. Build from Scratch — A Decision System Axis"
tags:
  - decision-making
  - leverage
  - teach
  - skill-design
  - efficiency
summary: "The default instinct to build solutions from scratch is a tax on speed, as shown by a compressed learning sprint where a "teach" skill—a wrapper for executing externally designed curricula—enabled rapid progress across three tracks. The decision system’s weight allocation should shift toward first exhausting search for existing tutorials, libraries, or reference implementations before self-creation. This can be formalized as a Leverage Factor (L) axis: high L tasks favor composing or adapting external work, while low L tasks justify original creation when truly novel or proprietary needs arise. The theoretical framing exists but has not yet been formalized into a skill."
importance: 3
connections:
  - type: idea
    slug: precision-fuzziness-tradeoff
  - type: idea
    slug: "success-interrogation-heuristic"
  - type: idea
    slug: "efficiency-formula"  # review: 0.586
  - type: idea
    slug: "where-innovation-comes-from"  # review: 0.562
  - type: idea
    slug: "reconceptualizing-standard-engineering"  # review: 0.526
  - type: idea
    slug: "content-independent-framework"  # review: 0.525
  - type: idea
    slug: "freedom-exploration-generator"  # review: 0.520
  - type: idea
    slug: "framework-extraction-pattern"  # review: 0.518
  - type: idea
    slug: "practice-as-learning-purpose"  # review: 0.515
  - type: idea
    slug: "transfer-high-leverage"  # review: 0.508
  - type: idea
    slug: "standard-engineering"  # review: 0.503
---
# Leverage Existing Solutions vs. Build from Scratch — A Decision System Axis

## The evidence

The teach skill was used as the primary engine across three concurrent learning tracks (teach-runoob-python, teach-RAG, teach-Agent) in a compressed 3-day window before an internship deadline. All three tracks succeeded. The teach skill itself is a wrapper around "someone else already designed the curriculum, I just need to execute it" — it leverages existing structured resources (runoob.com tutorials, research papers, framework docs) rather than inventing pedagogy from scratch.

This is a data point: **other people's work is high-leverage.** The default instinct to "figure it out myself" is a tax on speed.

## Practical adjustment

In the decision system (not yet formalized as a skill), the weight allocation should shift:

- **↑ "Find existing solutions" weight** — before building anything, exhaust search: has someone already solved this? Is there a tutorial, a library, a reference implementation, a skill?
- **↓ "Build from scratch" weight** — self-creation should be the fallback, not the default. It's high-cost, high-friction, and only justified when existing solutions genuinely don't fit.

Concretely: when facing a new task, the first question should be "who has already done this and what can I steal?" — not "how would I design this?"

## Theoretical framing

In a general decision system, this should be an explicit axis/factor:

> **Leverage Factor (L)**: the degree to which a task can be accomplished by composing, adapting, or directly consuming existing external work, versus requiring original creation.
>
> High L → prefer external sourcing (faster, cheaper, benefits from others' learning curves).
> Low L → self-creation is unavoidable (truly novel problems, proprietary context, integration gaps).

The teach skill succeeded because the tasks had high L: Python tutorials exist, RAG tutorials exist, agent papers exist. The skill's job was adapting and localizing, not inventing.

## Status

Theoretical framing exists but the decision system hasn't been formalized into a skill yet. This idea should feed into that eventual design.
