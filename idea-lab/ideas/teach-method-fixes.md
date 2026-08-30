---
id: idea-20260730-teach-method-fixes
title: "/teach Method Fixes — Concept/Practice Split and Bottom-Up Sequencing"
tags:
  - teach-method
  - pedagogy
  - curriculum-design
  - actionable
summary: "The /teach method should split lessons into concept (no code, horizontal interaction density) and practice (code reading, vertical cross-filter bindings), sequenced bottom-up from the lowest abstraction. Mixing horizontal and vertical learning in one lesson triggers recursive questioning, as does top-down sequencing from high abstractions. Alternating concept maps then code reading, bottom-up, eliminates the dependency chain problem. This restructured rapid-concept-push cycle reserves independent writing for the integrative exam. Retrofit existing tracks only when lessons fail due to recursive questioning."
body_hash: "0ad93588"
importance: 4.53  # auto
connections:
  - type: idea
    slug: knowledge-mastery-two-axis-model
  - type: idea
    slug: interaction-as-dictionary
  - type: idea
    slug: "explaining-excellent-sheep-with-theory"  # review: 0.566
  - type: idea
    slug: "pass-criteria-as-curriculum-design"  # review: 0.565
  - type: idea
    slug: "practice-as-learning-purpose"  # review: 0.565
  - type: idea
    slug: "data-structure-first-code-reading"  # review: 0.538
  - type: idea
    slug: "success-interrogation-heuristic"  # review: 0.534
  - type: idea
    slug: "learning-pipeline"  # review: 0.508
  - type: idea
    slug: "inquiry-essay-method"  # review: 0.500
  - type: idea
    slug: "teach-coverage-check"  # auto, review: 0.545
  - type: idea
    slug: "the-teacher"  # auto, review: 0.527
  - type: idea
    slug: "peer-cross-teaching"  # auto, review: 0.524
  - type: idea
    slug: "memorization-in-pipeline"  # auto, review: 0.511
  - type: idea
    slug: "learning-method-v2"  # auto
  - type: idea
    slug: "enumerative-as-scaffold-for-generative"  # auto
  - type: idea
    slug: "hermeneutic-circle-learning"  # auto, review: 0.535
  - type: idea
    slug: "ai-centered-new-education-industry"  # auto, review: 0.502
  - type: idea
    slug: "teach-task-volume-scaling"  # auto
  - type: idea
    slug: "practice-necessity-willingness-tradeoff"  # auto, review: 0.594
  - type: idea
    slug: "plugin-architecture-vs-defaults"  # auto, review: 0.569
  - type: idea
    slug: "pattern-pipeline"  # auto, review: 0.549
  - type: idea
    slug: "knowledge-map-format"  # auto, review: 0.504
  - type: idea
    slug: "teach-application-scope"  # auto
  - type: idea
    slug: "single-advancement-method-first-pass"  # auto, review: 0.549
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
