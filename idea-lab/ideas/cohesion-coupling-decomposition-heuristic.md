---
id: "idea-20260711-cc01"
summary: "The cohesion-coupling decomposition heuristic states that a good system decomposition requires subsystems with high internal cohesion and sparse external coupling, ideally zero coupling. Derived from the abstraction barrier concept, this principle applies recursively at every scale. High cohesion allows each subsystem to be understood in isolation, while low coupling enables composability, reuse, and localized debugging. For multi-perspective models like the unified Python execution model, each sub-model should be internally coherent with minimal, well-defined interfaces to other sub-models, and zero coupling indicates they should remain separate."
title: "Cohesion-Coupling Decomposition Heuristic — Migrated from Abstraction Barrier Concept"
tags: [system-design, modeling, decomposition, abstraction, cohesion, coupling, methodology, shallow-migration]
importance: 3.27  # auto
connections:
  - type: idea
    slug: "abstraction-barrier-as-dual-perspective-bridge"  # auto
  - type: idea
    slug: "how-to-deal-with-complexity"  # auto
  - type: idea
    slug: "concepts的划分"  # auto
  - type: idea
    slug: "attention-pointer-learning-model"  # auto
  - type: idea
    slug: "unified-python-execution-model"  # auto
  - type: idea
    slug: "knowledge-as-dictionary-of-perspectives"  # auto
  - type: idea
    slug: "locate-first-model-last"  # auto
  - type: idea
    slug: "reading-modeling-decomposition-tradeoff"  # auto
  - type: idea
    slug: "objective-importance-scoring"  # auto
---
# Cohesion-Coupling Decomposition Heuristic

## Source

Shallow migration from CS61A's abstraction barrier concept (Lecture 4). The abstraction barrier separates representation (internal, high cohesion) from use (external, low coupling via a narrow interface). This pattern generalizes.

## The Heuristic

When decomposing a system into subsystems:

> A decomposition is good if subsystems have **high internal cohesion** and **sparse external coupling**. The ideal limit is zero coupling between subsystems.

Applied to models: when building a multi-perspective model (like the [[unified-python-execution-model]]), each sub-model should be internally tight (coherent entities + relationships within the sub-model) and externally sparse (minimal, well-defined interfaces to other sub-models). The extreme case — zero coupling — means the sub-models are fully independent, which may or may not be desirable depending on the goal.

## Recursive Property

The decomposition is **recursive**: each subsystem can itself be decomposed into sub-subsystems following the same principle (high internal cohesion, sparse external coupling). This applies fractally — at every level of granularity, from the top-level architecture down to individual functions. The stopping condition is when a subsystem is simple enough that further decomposition adds more interface complexity than it removes.

## Why This Works

1. **Cognitive manageability**: Each subsystem can be understood independently. Coupling forces you to hold multiple subsystems in your head simultaneously.
2. **Composability**: Low-coupling subsystems can be rearranged, replaced, or reused without cascading changes.
3. **Debug-ability**: When something breaks, the fault is localized to one subsystem (or one interface).
4. **The abstraction barrier is a special case**: It's the deliberate construction of a narrow interface between a high-cohesion implementation and its users.
5. **Recursive applicability**: The same principle works at every scale — you don't need a different decomposition strategy for different levels of the system.

## Application to the Unified Python Execution Model

This heuristic directly informs how to couple the sub-models (def tree, frame tree, call tree, binding graph, change taxonomy, abstraction barriers):

- Each sub-model should have high internal cohesion (clear entities + relationships within its domain)
- Coupling between sub-models should be through narrow, well-defined interfaces (not a tangled web of cross-references)
- The coupling architecture (layered? multi-projection? process-algebraic?) should minimize the number and complexity of inter-model connections
- Zero coupling is the limiting case — if two sub-models are truly independent, they don't belong in the same unified model

## Generality

This isn't specific to Python or CS61A. It applies to:
- Software architecture (microservices, modules, classes)
- Model design (the heuristic itself was discovered while thinking about model coupling)
- Knowledge organization ([[concepts的划分|Classification of Concepts]])
- Any domain where you're dividing a whole into parts
