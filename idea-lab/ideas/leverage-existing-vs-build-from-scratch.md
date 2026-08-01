---
id: "idea-20260719-leverage-existing-vs-build-from-scratch"
title: "Leverage Existing Solutions vs. Build from Scratch — A Decision System Axis"
status: raw
source_type: daily
source_path: null
importance: 3
permanent_note_material: true
material_since: 2026-07-19
material_expiry_days: 30
promoted_from: null
tags:
  - decision-making
  - leverage
  - teach
  - skill-design
  - efficiency
related_entities:
  - type: idea
    slug: precision-fuzziness-tradeoff
    relation: related
    strength: 0.4
    dimensions: [concept-relation]
    bidirectional: true
    source: manual
links: []
created: 2026-07-19
updated: 2026-07-19
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
