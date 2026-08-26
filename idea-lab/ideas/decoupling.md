---
id: idea-20260826-decoupling
title: "Decoupling Is a Rather Interesting Idea"
tags:
  - decoupling
  - architecture
  - modularity
  - refactoring
  - design
summary: "Decoupling—separating components that don't need to be coupled—is a powerful design move because each part can change, be replaced, or evolve independently without breaking the whole. Coupling forces big-bang rewrites, whereas decoupling converts \"rewrite everything\" into \"swap a part.\" The failed half-refactor in plugin-architecture-vs-defaults was fundamentally a coupling problem, and the /teach connection shows decoupling made concrete through an immutable engine separated from swappable strategy plugins. The project-hub system applies the same principle by keeping five subsystems independent through internal cohesion and deliberately sacrificing cross-module connections so each can evolve on its own."
body_hash: "c5acc316"
connections:
  - type: idea
    slug: "cohesion-coupling-decomposition-heuristic"  # auto, review: 0.536
  - type: idea
    slug: "content-independent-framework"  # auto, review: 0.502
importance: 0.0  # auto
---
# Decoupling Is a Rather Interesting Idea

**One sentence**: Decoupling — separating components that don't need to be coupled — is a surprisingly powerful design move: each part can change, be replaced, or evolve independently without breaking the whole.

## Why It Matters

- **Independent evolution** — a decoupled part can be swapped or improved on its own; no big-bang rewrite of everything.
- **Failure is contained** — a change to one part does not cascade into the others. (The half-refactor hybrid in [[plugin-architecture-vs-defaults]] failed precisely because the new files and the old body were *coupled* into one self-contradicting document.)
- **The `/teach` connection** — the plugin architecture is decoupling made concrete: the immutable engine decoupled from swappable strategy plugins. A properly decoupled skill would have turned the optimization into a clean *swap of a part* instead of a risky *rewrite of the whole*. At bottom, the failure was a coupling problem.

## The General Principle

Coupling forces big-bang rewrites; decoupling converts "rewrite everything" into "swap a part." The project-hub system itself is built on this — five subsystems kept independent by internal cohesion, with cross-module connections deliberately sacrificed so each can evolve on its own.

## Connections

- [[plugin-architecture-vs-defaults]] — decoupling as the architectural core of the plugin idea.
- [[cohesion-coupling-decomposition-heuristic]] — the complementary principle: decompose by internal cohesion.
