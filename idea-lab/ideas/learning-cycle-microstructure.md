---
id: idea-20260925-learning-cycle-microstructure
title: "The Microstructure of Learning — Two Steps per Cycle, and the Cycle Is the Plugin"
tags:
  - teach-method
  - learning
  - plugin-architecture
  - cycle-design
  - knowledge-map
  - curriculum-design
  - methodology
summary: "Learning’s microstructure is a sequence of cycles, each needing only two steps: absorb knowledge or skill, then verify that absorption happened. The cycle is the plugin unit, and the verification method—three-tier exam or filter-map redraw—is the plugin that fills the verify slot. Concept versus practice becomes a parameter of the absorb step rather than fixed structure, removing the self-contradictory stacking that failed the prior /teach refactor. This simplification bets the spine need not encode the two-axis c/p model, but it risks losing load-bearing sequencing rules. A pointwise three-tier exam can pass tasks while the learner’s structure is wrong, whereas holistic filter-map redraw catches structure but may verify the map rather than usable knowledge."
body_hash: "9c1288c4"
connections:
  - type: idea
    slug: "teach-method-fixes"  # auto
  - type: idea
    slug: "learning-method-v2"  # auto
  - type: idea
    slug: "hermeneutic-circle-learning"  # auto
  - type: idea
    slug: "teach-task-volume-scaling"  # auto
  - type: idea
    slug: "enumerative-as-scaffold-for-generative"  # auto
  - type: idea
    slug: "practice-necessity-willingness-tradeoff"  # auto
  - type: idea
    slug: "pass-criteria-as-curriculum-design"  # auto
  - type: idea
    slug: "learning-pipeline"  # auto
  - type: idea
    slug: "knowledge-mastery-two-axis-model"  # auto
  - type: idea
    slug: "plugin-architecture-vs-defaults"  # auto
  - type: idea
    slug: "memorization-in-pipeline"  # auto
  - type: idea
    slug: "pattern-pipeline"  # auto
  - type: idea
    slug: "teach-application-scope"  # auto
  - type: idea
    slug: "learning-dynamics"  # auto, review: 0.590
  - type: idea
    slug: "knowledge-map-format"  # auto, review: 0.585
importance: 7.17  # auto
---
# The Microstructure of Learning — Two Steps per Cycle, and the Cycle Is the Plugin

**One sentence**: Learning's microstructure is a sequence of **cycles**, and a cycle needs only **2 steps** — absorb knowledge or skill (concept *or* practice), then verify the absorption — with the cycle itself as the plugin unit and the verification method (three-tier exam, filter-map) as the plugin that fills the verify slot.

## The Cycle Is Two Steps

1. **Absorb** — knowledge or skill. Concept or practice. Either way it is one step, not two.
2. **Verify** — did the absorption actually happen? Via a three-tier exam, or by drawing a **filter-map** (the knowledge map).

That is the whole cycle. Everything else in the current `/teach` design — lesson types, sequencing rules, ratio selection — is either a *parameter of step 1* or an *implementation of step 2*, rather than additional structure.

## The Plugin Organization

The reference is the plugin form used in `~/teach-design-thinking`, where it is **phases that form the spine and tools that plug into them**:

| | Spine (not plugins) | Plugins |
|---|---|---|
| **teach-design-thinking** | The four questions — *What is? · What if? · What wows? · What works?* | Mind mapping, journey mapping, brainstorming, assumption testing, rapid prototyping, storytelling, … — each inserts at a phase |
| **`/teach`** | The two steps — *absorb · verify* | Three-tier exam, filter-map — each fills the verify slot |

The mapping is exact: **a step is the slot; the method is the plugin that fills it.** The step is not a plugin, just as *What is?* is not a plugin in teach-design-thinking — it is where plugins go.

And a **cycle is itself a plugin**, which is consistent with the nested-plugin picture already recorded in [[composition-language]]: there, design thinking is a *large* plugin, mind mapping *medium*, journey mapping *small*. A cycle sits at that scale — large enough to compose into a course, small enough to be composed of methods.

So the structure is **plugin at two levels, spine at one**: cycles compose upward, methods compose inward, and the two steps are the fixed skeleton of a cycle.

## Why This Draws the Boundary Better Than the Last Attempt

The `/teach` refactor of 2026-08-24 failed and was rolled back. Its first failure mode, per [[plugin-architecture-vs-defaults]], was **self-contradictory structure**:

> the old body still treated concept/practice and the three-tier exam as *fixed structure*, while the new files declared them *just strategies*. Two worldviews stacked in one document.

This proposal answers that contradiction directly by **saying which is which**:

- **Structure**: the two steps, and the cycle boundary.
- **Plugin**: the verification method.

Concept-vs-practice stops being a structural distinction and becomes a **parameter of the absorb step** — which is the resolution the earlier attempt lacked. Whether that resolution is right is a separate question (see below), but it removes the contradiction rather than stacking a second worldview on top of the first.

## What the Simplification Costs

This is the part to watch. `/teach` currently encodes a **two-axis model**:

- **c — horizontal interaction density**: concept lessons build the richness of the conceptual map
- **p — vertical cross-filter binding**: practice lessons attach concrete operations to concepts

The sequencing rules that serve it are load-bearing: bottom-up ordering, concept always before practice, practice introduces no new concepts, and a concept/practice ratio that varies by domain.

Collapsing absorb to a single step keeps concept/practice as a **label** but drops it as a **structural element**. That is fine *if* the axis distinction can live in the lesson's own marking — which `/teach` already does, since lessons carry their type in the visual header. It is **not** fine if the sequencing rules were doing work that the two-step cycle can no longer express, because the rules are what enforce the order the two-axis model requires.

So the simplification is a real bet: that the spine does not need to know about c and p, only the lesson does.

## Verification as a Swappable Plugin

The three-tier exam is currently the *only* verification method. Making it one plugin among several changes what verification is:

| Method | Verifies by | Shape |
|---|---|---|
| **Three-tier exam** | Task performance — can you *do* it | **Pointwise**: many independent checks |
| **Filter-map redraw** | Structure reproduction — can you *redraw the map* | **Holistic**: one check over the whole structure |

These are not interchangeable instruments. A pointwise exam can pass every task while the structure in the learner's head is wrong — the answers are right, the map is not. A redraw catches exactly that and misses nothing else. The two fail in different directions, which is an argument for *both* being in the plugin set rather than either replacing the other.

Worth noting: `/teach` already lists "draw a diagram from memory" among its passing criteria, and the concept-lesson pass bar already requires drawing the relationship map from memory. So the filter-map is **already present as a criterion**; this idea promotes it to a standalone verification method.

## Open Questions

- **Does the two-step cycle preserve the two-axis model?** This is the load-bearing question. If the sequencing rules are merely *consequences* of c/p, they can be derived at the lesson level and the simplification is free. If they are *independent structure*, the two-step cycle loses something the current design needs.
- **Is a filter-map a verification or a different act?** Redrawing a map may test the map rather than the knowledge — a learner can reproduce structure without being able to use it. Whether that counts as absorption having happened is a definitional call.
- **What is the minimum viable absorb step?** If a cycle is only two steps, cycles can be made very small. What is the shortest absorb worth verifying, and does the cycle overhead make small cycles inefficient?
- **How do cycles compose upward?** Cycles are plugins, so they should assemble into a course — but by plain concatenation, or through some larger structure with its own spine?
- **Does the plugin set need to be closed?** [[plugin-architecture-vs-defaults]]'s second failure mode was an *incomplete* pool losing to distilled defaults. A plugin architecture pays only when the pool is complete enough to beat the defaults — so a two-method verify slot may be worse than the single distilled exam it replaces.

## Related

- [[plugin-architecture-vs-defaults]] — the failed attempt and its two failure modes; this idea is a cleaner cut at the same boundary problem
- [[knowledge-map-format]] — MAP.md is the workspace's *authored* map; a filter-map is the learner *reproducing* it, which is what makes it a natural verification instrument
- [[composition-language]] — the nested-plugin picture (large/medium/small plugins) that the cycle's level fits into
- [[knowledge-mastery-two-axis-model]] — the two-axis model the sequencing rules serve
- [[learning-method-v2]] — the decay-aware maintenance cycle this microstructure would replace
- [[fundamental-model-of-learning]] — the underlying learning model the cycle operationalizes
