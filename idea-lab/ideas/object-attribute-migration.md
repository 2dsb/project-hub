---
id: "idea-20260719-object-attribute-migration"
title: "Object-Attribute Model as Migratable Perspective"
status: raw
source_type: daily
source_path: null
importance: 2
permanent_note_material: true
material_since: 2026-07-19
material_expiry_days: 30
promoted_from: null
tags:
  - python
  - perspective
  - migration
  - epistemology
  - knowledge-modeling
related_entities:
  - type: idea
    slug: knowledge-as-dictionary-of-perspectives
    relation: extends
    strength: 0.9
    dimensions: [concept-relation, complement]
    bidirectional: true
    source: manual
  - type: idea
    slug: name-object-binding-as-perspective
    relation: extends
    strength: 0.7
    dimensions: [concept-relation]
    bidirectional: true
    source: manual
  - type: idea
    slug: interaction-as-dictionary
    relation: related
    strength: 0.7
    dimensions: [concept-relation]
    bidirectional: true
    source: manual
links: []
created: 2026-07-19
updated: 2026-07-19
---

# Object-Attribute Model as Migratable Perspective

## Raw intuition

Python's `object.attribute` model — where everything is an object, objects have attributes accessed via dot notation, and a name is just a binding to an object — might be migratable to domains far beyond programming. The `.` operator is a universal accessor: given a thing and a lens, return the thing's manifestation under that lens.

This is a narrower claim than `knowledge-as-dictionary-of-perspectives` (which already uses the dictionary model). The specific question here is: **what does the `.` (dot) operator buy us as a thinking tool, beyond what `[key]` (bracket) already gives us?**

## Potential migration targets (undeveloped)

- **Relationships**: a person `.` a context = their role in that context (`alice.workplace = "colleague"`, `alice.family = "daughter"`)
- **Concepts**: a concept `.` a domain = its meaning in that domain (`recursion.math = "inductive definition"`, `recursion.cs = "self-calling function"`)
- **Identity**: the self `.` a situation = the aspect of self that shows up (`me.presentation = "confident"`, `me.alone = "reflective"`)

## Why `.` instead of `[key]`

The dot implies structured, known-at-design-time attributes — a schema. Bracket implies open-ended, runtime keys — a map. The dot enforces that perspectives must be named, finite, and stable. This constraint may be productive: it forces you to commit to a fixed set of lenses rather than ad-hoc key invention.

## Status

Immature. Needs more migration examples to test whether the `.` metaphor actually adds value beyond the existing dictionary-of-perspectives framework, or is just a syntactic variant of the same idea.
