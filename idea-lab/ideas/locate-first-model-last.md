---
id: "idea-20260713-lp01"
summary: "The "locate-first, model-last" paradigm shifts learning from building a structural model simultaneously with learning to instead first locating each knowledge point in a provisional key hierarchy that is discovered iteratively through the points themselves, and deferring modeling until after full domain traversal. This avoids premature modeling unreliability because, as the dictionary model reveals, knowledge points exist in a high-dimensional space where clustering with few samples produces noise—you need enough points before PCA-like structure makes sense. It eliminates the merge-cost side of the reading-modeling decomposition tradeoff and avoids the breadth-first trap by enforcing breadth-first traversal, much like a two-pass reading strategy. The result is lower cognitive load, faster learning velocity, and highly accurate models built in one concentrated pass with complete information."
title: "Locate-First, Model-Last — A Learning Paradigm Shift Driven by the Dictionary Model"
tags: [learning, modeling, paradigm, methodology, knowledge-representation, multi-perspective, dictionary-model, two-pass, efficiency]
importance: 9
connections:
  - type: idea
    slug: knowledge-as-dictionary-of-perspectives
  - type: idea
    slug: reading-modeling-decomposition-tradeoff
  - type: idea
    slug: two-pass-reading-strategy
  - type: idea
    slug: cohesion-coupling-decomposition-heuristic
  - type: idea
    slug: breadth-first-trap
  - type: idea
    slug: attention-pointer-learning-model
  - type: idea
    slug: structural-patience
  - type: idea
    slug: attention-as-bottleneck
  - type: idea
    slug: learning-pipeline
  - type: idea
    slug: "speed-first-model-second-batch-tradeoff"  # auto
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
