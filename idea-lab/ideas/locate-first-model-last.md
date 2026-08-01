---
id: "idea-20260713-lp01"
title: "Locate-First, Model-Last — A Learning Paradigm Shift Driven by the Dictionary Model"
tags: [learning, modeling, paradigm, methodology, knowledge-representation, multi-perspective, dictionary-model, two-pass, efficiency]
status: raw
created: 2026-07-13
updated: 2026-07-13
source_type: "manual"
source_path: null
importance: 9
permanent_note_material: true
material_since: "2026-07-13"
material_expiry_days: 30
promoted_from: null
links: []
related_entities:
  - type: idea
    slug: knowledge-as-dictionary-of-perspectives
    relation: direct-corollary
    strength: 0.95
  - type: idea
    slug: reading-modeling-decomposition-tradeoff
    relation: solves
    strength: 0.9
  - type: idea
    slug: two-pass-reading-strategy
    relation: generalizes
    strength: 0.85
  - type: idea
    slug: cohesion-coupling-decomposition-heuristic
    relation: motivated-by
    strength: 0.8
  - type: idea
    slug: breadth-first-trap
    relation: avoids
    strength: 0.7
  - type: idea
    slug: attention-pointer-learning-model
    relation: behavioral-corollary
    strength: 0.85
    dimensions: [concept-relation, complement]
    bidirectional: true
    source: auto
  - type: idea
    slug: structural-patience
    relation: extends
    strength: 0.6
    dimensions: [concept-relation, complement]
    bidirectional: true
    source: auto
  - type: idea
    slug: attention-as-bottleneck
    relation: related
    strength: 0.45
    dimensions: [concept-relation]
    bidirectional: true
    source: auto
  - type: idea
    slug: learning-pipeline
    relation: related
    strength: 0.5
    dimensions: [concept-relation]
    bidirectional: true
    source: auto
---

# Locate-First, Model-Last — A Learning Paradigm Shift

## The Problem

**Old paradigm: model as you learn.** While reading/learning, try to build the structural model simultaneously. This fails because:

1. **Cohesion-coupling says premature modeling is unreliable**: Without knowing the full landscape, you can't choose good decomposition boundaries. Chapter-by-chapter modeling creates merge costs because chapters are editorial boundaries, not structural ones ([[reading-modeling-decomposition-tradeoff]]).

2. **The dictionary model reveals a dimensionality problem**: If a knowledge domain has N perspectives (keys), each knowledge point lives in an N-dimensional space. With only a small sample of points seen so far, clustering/classifying in high dimensions is noise — the structure you infer will be wrong.

3. **Modeling overhead kills learning velocity**: The cognitive cost of trying to model while learning is high, and most of it is wasted on structures that will be revised or discarded once more is known.

## The New Paradigm: Two Interleaved Phases + One Final Phase

**Important**: Steps 1 and 2 are NOT strictly sequential. The key hierarchy is not knowable a priori — you discover it *through* the knowledge points. You can't know "environment diagram" is a perspective until you learn what an environment diagram is. The key set co-evolves with the locating process.

### Phase 1 — Map Keys & Locate Points (Interleaved)

These two activities happen simultaneously, each feeding the other:

**1a. Maintain a provisional key hierarchy.** Start with whatever keys you can guess (e.g., "this CS topic probably has an algorithmic layer and a program layer"). This is a living sketch, not a fixed coordinate system.

**1b. For each knowledge point encountered:**
1. Understand it
2. Locate it against the current key hierarchy — determine its approximate coordinates
3. **If the point doesn't fit** — if it reveals a perspective you hadn't considered → extend the key hierarchy. The point itself teaches you what keys exist.
4. Move on

The key hierarchy is *discovered* through the points, not imposed before them. By the time you've traversed all knowledge points, the key set is complete — because the points themselves define it.

### Phase 2 — Model After Full Coverage

Only after the entire domain has been traversed and every point located:
1. Analyze intra-layer structure (how points within the same key relate)
2. Analyze inter-layer relationships (how values under different keys correspond or constrain each other)
3. Build the model — now with complete information

Modeling moves from being a **process** (ongoing, interleaved with learning) to being a **finale** (one pass at the end, with a full map).

## Why This Works

This is the **two-pass reading strategy generalized to any learning domain** ([[two-pass-reading-strategy]]):
- Pass 1 = Phase 1: traverse all knowledge points, simultaneously building the key hierarchy and locating each point within it
- Pass 2 = Phase 2: with global context and a complete key set, build the structure (model)

It directly avoids the **breadth-first trap** ([[breadth-first-trap]]): going deep before going wide. Locate-first forces breadth-first traversal.

It solves the **reading-modeling decomposition tradeoff** ([[reading-modeling-decomposition-tradeoff]]): by separating location from modeling, you eliminate the merge-cost side of the tradeoff entirely. Location has no merge cost — coordinates don't conflict.

It's a **direct behavioral corollary of the dictionary model** ([[knowledge-as-dictionary-of-perspectives]]): if knowledge points are vectors in a high-dimensional space, then you need enough samples before PCA/clustering makes sense. Premature modeling = PCA on 5 points in a 10-dimensional space.

## Concrete Contrast

| | Old Paradigm | New Paradigm |
|---|---|---|
| **While learning** | Understand + model simultaneously | Understand + locate only |
| **Cognitive load** | High (dual task) | Low (single task) |
| **Model accuracy** | Low (partial information) | High (full information) |
| **Velocity** | Slow (modeling overhead per point) | Fast (O(1) per point) |
| **Modeling phase** | Distributed throughout | Concentrated at end |
| **Revision cost** | High (model rewrites) | Zero (coordinates don't conflict) |
