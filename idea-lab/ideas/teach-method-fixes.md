---
id: idea-20260730-teach-method-fixes
title: "/teach Method Fixes — Concept/Practice Split and Bottom-Up Sequencing"
tags:
  - teach-method
  - pedagogy
  - curriculum-design
  - actionable
importance: 8
connections:
  - type: idea
    slug: knowledge-mastery-two-axis-model
  - type: idea
    slug: interaction-as-dictionary
---

# /teach Method Fixes — Concept/Practice Split and Bottom-Up Sequencing

**One sentence**: Split every /teach lesson into concept lessons (horizontal interaction density, no code) and practice lessons (vertical cross-filter bindings, code reading bar), sequenced bottom-up from the lowest abstraction that enables understanding.

## Problem

Two structural issues identified across 10 /teach tracks:

### Issue 1: Concept and practice mixed in the same lesson

When a lesson simultaneously builds horizontal interactions (how X relates to Y) and vertical bindings (how to write X in code), neither stabilizes. The learner recursively questions downward until hitting solid ground. Example: OpenClaw Lesson 0001 (5-layer TCP→FastAPI stack, top-down) and Lesson 0008 (SQLAlchemy concepts + code in one session).

### Issue 2: Top-down sequencing from the highest abstraction

Starting from "FastAPI is a web framework" forces the learner to ask "what is a web framework?" → "what is HTTP?" → "what is TCP?" — each answer depends on a concept not yet introduced. The learner must recursively discover the dependency chain. Bottom-up sequencing eliminates this: start from the lowest abstraction needed, build upward.

## Proposed Rules

### Rule 1: Two lesson types

| Type | Goal | Contains | Passing bar |
|---|---|---|---|
| **Concept lesson** | Build horizontal interaction density in the conceptual filter | Concept maps, interaction diagrams, analogies, structural relationships. No code. | "Can explain in your own words and draw the relationship map" |
| **Practice lesson** | Establish vertical cross-filter bindings | Real code, annotated examples, code-reading exercises. No new concepts. | "Can read and trace the code — understand every line's role" |

Note: the practice lesson's passing bar is **code reading**, not independent writing. Independent writing is the exam/project phase — the "one big integrative exam" at the end of the rapid-concept-push cycle. This preserves the existing method's cycle structure.

### Rule 2: Bottom-up sequencing

Determine the **lowest abstraction level** needed to understand the topic. Start there. Build upward.

For networking: TCP → HTTP → FastAPI → the project. Not FastAPI → HTTP → TCP (recursive).

For SQLAlchemy: concept map of objects and their relationships → code that instantiates those objects. Not code first, then "what does this do?"

### Rule 3: Concept lesson always precedes its corresponding practice lesson

A practice lesson's vertical bindings can only attach if the horizontal interaction map already exists. Concept map first, code second. (This is what Lesson 0009→0008 in OpenClaw demonstrated — the numbering is an artifact of discovery, not design.)

### Rule 4: No new concepts in practice lessons

Practice lessons reference only concepts already introduced in prior concept lessons. If a practice lesson reveals a new concept, that concept gets its own concept lesson first. This prevents the recursive-questioning spiral.

## Integration with Existing Method

These rules fit within the existing cycle:

> **Rapid concept push → one big integrative exam/project**

The concept push phase now has internal structure: alternating concept→practice lesson pairs, bottom-up sequenced. The exam/project phase is unchanged — that's where independent writing (strong vertical bindings) is developed.

## When to Apply

- **Next new /teach track**: Apply from the start. Design concept map first, then practice lessons.
- **Existing tracks (OpenClaw, LangGraph, etc.)**: Retrofit only when a lesson fails — if recursive questioning occurs, split the lesson and resequence.
- **Simple/linear topics**: May not need the split. The split is most valuable for structural domains with deep dependency chains.

## Open Questions

- Can concept lessons be multi-level (nested concept maps, zoom-in/zoom-out)? PKU's unified-model.html suggests yes.
- What's the optimal concept→practice ratio? 1:1? 2:1? Domain-dependent?
- When (if ever) should a single lesson combine both types? Possibly for very shallow topics where the dependency chain is flat.
