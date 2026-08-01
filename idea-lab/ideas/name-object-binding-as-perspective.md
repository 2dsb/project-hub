---
id: "idea-20260711-nb01"
title: "Name-Object Binding as a Perspective on Program Execution"
tags: [cs61a, binding, environment-diagram, mutation, identity, mental-model, python]
status: raw
created: 2026-07-11
updated: 2026-07-11
source_type: "manual"
source_path: null
importance: 7
permanent_note_material: true
material_since: "2026-07-11"
material_expiry_days: 14
promoted_from: null
links: []
related_entities:
  - type: idea
    slug: environment-diagram-dual-perspective
    relation: extends
    strength: 0.85
  - type: idea
    slug: call-tree-as-third-perspective
    relation: complementary-perspective
    strength: 0.8
  - type: idea
    slug: abstraction-barrier-as-dual-perspective-bridge
    relation: related
    strength: 0.6
  - type: project
    slug: cs61a
    relation: emerged-from
    strength: 0.85
  - type: idea
    slug: unified-python-execution-model
    relation: integrated-into
    strength: 0.9
    dimensions: [concept-relation, complement]
    bidirectional: true
    source: auto
  - type: idea
    slug: knowledge-as-dictionary-of-perspectives
    relation: instance-of
    strength: 0.6
    dimensions: [concept-relation]
    bidirectional: true
    source: auto
  - type: idea
    slug: human-machine-code-reading-gap
    relation: related
    strength: 0.5
    dimensions: [concept-relation]
    bidirectional: true
    source: auto
---

# Name-Object Binding as a Perspective on Program Execution

## Discovery

From CS61A Week 2 — the observation that names are not values; they're references to objects. The binding relationship between a name and an object is itself a distinct perspective on program execution, orthogonal to the tree-based views.

## The Binding Perspective

In Python's execution model:
- Names live in frames (environments)
- Objects live in the heap
- Names are bound to objects via references (arrows in environment diagrams)
- This binding can change in two fundamentally different ways:
  1. **Rebinding**: name now points to a different object (`x = y`, `x = x + 1`)
  2. **Mutation**: the object itself changes, but the name still points to the same object (`x.append(5)`, `x[0] = 9`)

## Why This Is a Distinct Perspective

The three tree perspectives (def tree, frame tree, call tree) show **structural** relationships:
- Def tree: what's defined inside what (static nesting)
- Frame tree: which frame is linked to which parent (environment chain)
- Call tree: which call invokes which sub-call (runtime invocation)

The binding perspective shows **referential** relationships:
- Which names refer to which objects
- Whether two names refer to the *same* object (identity, `is`)
- Whether two names refer to objects with the *same value* (equality, `==`)
- How rebinding vs mutation propagates through the name graph

## Phenomena This Lens Clarifies

1. **Identity vs equality**: `a is b` checks same object binding; `a == b` checks same value. Two names can bind to different objects with the same value.
2. **Mutable default argument trap**: `def f(s=[]):` — the default value object is created once at definition time, and the name `s` binds to that same object on every call. Mutation accumulates.
3. **`nonlocal`**: Rebinding a name in an enclosing frame (not the current one). The binding perspective makes it clear this is about *which frame's name* gets rebound, not about objects.
4. **Immutable containers with mutable elements**: A tuple `([1,2], 3)` — the tuple binding is immutable (can't rebind `s[0]`), but the list object it references is mutable (`s[0][0] = 4` works).

## Relation to the Portal Model

The Portal Model's frame trees already show name→object arrows in environment diagrams. But elevating binding to a **first-class perspective** rather than an implementation detail of frame trees reveals patterns that are otherwise easy to miss:
- Aliasing: multiple names → same object
- The distinction between rebinding and mutation is the core of Python's execution semantics

## Potential Fruit

1. **Four-perspective framework**: def tree (static structure), frame tree (environment structure), call tree (computation flow), binding graph (reference structure). Is this the complete set?
2. **Teaching sequence**: binding should be taught *before* mutation — if students don't understand that names are references, mutation looks like magic
3. Connection to [[how-to-deal-with-complexity]] — the binding perspective may be a general tool for understanding any language with reference semantics
