---
id: "idea-20260626-attn01"
title: "Attention as the Bottleneck — Single-Threaded Execution in Learning & Life"
tags: [attention, bottleneck, single-threading, goal-singularity, learning-design, life-modeling]
status: raw
created: 2026-06-26
updated: 2026-06-26
source_type: "manual"
source_path: null
importance: 0
permanent_note_material: false
material_since: null
material_expiry_days: 14
promoted_from: null
links: []
related_entities:
  - type: idea
    slug: goal-singularity
    relation: shares-core
    strength: 0.85
    dimensions: [concept-relation]
    bidirectional: true
    source: manual
  - type: idea
    slug: timeline-based-project-structure
    relation: constrains
    strength: 0.8
    dimensions: [concept-relation]
    bidirectional: true
    source: manual
  - type: idea
    slug: attention-pointer-learning-model
    relation: complement
    strength: 0.7
    dimensions: [concept-relation, complement]
    bidirectional: true
    source: auto
---

# Attention as the Bottleneck

## Core Fact

A person can only attend to **one thing at a time**. This is not a preference or a habit — it's a hardware constraint. Multi-tasking is rapid context-switching, not true parallelism.

## Implications for the Project Structure Model

The (M, A) model describes project states and transitions, but it doesn't specify a crucial constraint: **only one project can be in execution at any given moment**. Attention is the single-threaded CPU.

This means:
- The day's time blocks are **mutually exclusive** — allocating 08:00–12:00 to DL Book means NO other project gets attention during that window
- The central design problem becomes **scheduling**: given N projects each with their own (M, A) state and expected value, which one gets the next attention slot?
- M-decay happens to ALL unattended projects simultaneously while you focus on one

## Connection to Goal-Singularity

Goal-singularity says: one action should serve one purpose. Attention-singularity says: one moment can hold one action. They're the same constraint at different levels — purpose (why) and execution (when).

## Design Questions

- Can attention constraints be used to **simplify** rather than frustrate? (If you can only do one thing, pick it and stop worrying about the rest.)
- How should the scheduling algorithm work given the (M, A) model + value objective?
- What does "attention residue" (carrying project A's mental state into project B's time block) do to the effective M dynamics?
- Can reconnection docs be seen as a way to **reduce attention residue** — giving the mind a clean save point so it can fully release project A and fully engage project B?
