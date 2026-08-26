---
id: idea-20260826-plugin-architecture-vs-defaults
title: Plugin Architecture vs Distilled Defaults — The /teach Optimization Post-Mortem
tags:
  - teach-method
  - architecture
  - strategy
  - degrees-of-freedom
  - refactoring
summary: "The /teach optimization attempt failed because it introduced a plugin architecture as a half-refactor, bolting new files like MAP.md and STRATEGY-SPACE.md onto the old procedural SKILL.md instead of rewriting the core into a model plus strategy-selection engine. The resulting hybrid contradicted itself by treating concept/practice and the three-tier exam as both fixed structure and replaceable strategies. Its incomplete strategy pool underperformed the old defaults, which were distilled winning combinations from ten real tracks via freedom-exploration-generator. The general lesson is that a plugin or strategy architecture only pays off when the refactor is fully committed and the plugin pool is complete enough to beat the defaults; otherwise the distilled defaults win and partial migration is strictly worse than either coherent state."
body_hash: "ab8e5bd2"
connections:
  - type: idea
    slug: "success-interrogation-heuristic"  # auto, review: 0.569
  - type: idea
    slug: "teach-method-fixes"  # auto, review: 0.569
  - type: idea
    slug: "sunk-cost-tug-and-salvage"  # auto, review: 0.556
  - type: idea
    slug: "pattern-pipeline"  # auto, review: 0.544
  - type: idea
    slug: "strategy-three-component-model"  # auto, review: 0.529
  - type: idea
    slug: "freedom-exploration-generator"  # auto, review: 0.526
  - type: idea
    slug: "practice-necessity-willingness-tradeoff"  # auto, review: 0.520
  - type: idea
    slug: "knowledge-map-format"  # auto, review: 0.505
  - type: idea
    slug: "leverage-existing-vs-build-from-scratch"  # auto, review: 0.502
  - type: idea
    slug: "teach-application-scope"  # auto, review: 0.527
importance: 0.0  # auto
---
# Plugin Architecture vs Distilled Defaults — The /teach Optimization Post-Mortem

The `/teach` optimization attempt (2026-08-24) failed and was rolled back — but the post-mortem contains a transferable design lesson.

## The Potential: Everything as a Plugin Around an Immutable Core

The optimized design's real merit was architectural. It turned most of the old skill's "default settings" — a cycle = concept + practice + exam, bottom-up sequencing, the three-tier exam, domain adaptation, even the HTML presentation — into **replaceable strategy plugins**, with only the fundamental model as the immutable engine. Every dimension becomes swappable: course-content granularity, cycle design, presentation format, flip order and volume, f handling, when and how to search new sources. More degrees of freedom → more exploration → more meta-learning data (see [[freedom-exploration-generator]]).

## Why It Failed: The Half-Refactor Trap

A plugin architecture changes the **core** — from a procedural default-pipeline to a model + strategy-selection engine. That demands a **complete rewrite**, not an addition. The actual implementation added files (`MAP.md`, `STRATEGY-SPACE.md`) onto the old procedural `SKILL.md` without rewriting it — a half-refactor:

1. **Self-contradictory structure** — the old body still treated concept/practice and the three-tier exam as *fixed structure*, while the new files declared them *just strategies*. Two worldviews stacked in one document.
2. **Incomplete strategy pool** — `STRATEGY-SPACE.md` held only a few recipes, sourced from one workspace. Faced with choosing from a thin, unproven pool, the AI did worse than the old skill's built-in defaults.

## Why the Old Defaults Won

The old "default settings" were not arbitrary — they were the **distilled winning combinations** of pattern discovery from 10 real tracks (see [[freedom-exploration-generator]]). Defaults = the highest-scoring plugin combination already found. Any incomplete plugin pool — by definition missing the distilled winners — loses to them. "Defaults beat 95% of plugin combinations" is therefore not coincidence; it is structural.

## The General Lesson

A plugin/strategy architecture only pays off when:

1. You **fully commit** to the refactor — a core change requires rewriting the body, not bolting on files; and
2. The **plugin pool is complete enough** that selecting beats the defaults.

Otherwise the distilled defaults win. A partial migration produces a hybrid that is strictly worse than either coherent state.
