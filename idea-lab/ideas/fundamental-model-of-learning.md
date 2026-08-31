---
id: idea-20260826-fundamental-model-of-learning
title: Fundamental Model of Learning
tags:
  - learning
  - knowledge-map
  - teach-method
  - meta-cognition
  - model
summary: "A five-part theory of learning holds that the knowledge map is constructed, partial, and revisable, not discovered, and forms a recursive DAG of minimal indivisible knowledge nodes with binary 0/1 states. Learning is single-threaded: exactly one minimal node flips from 0 to 1 only when its prerequisites are already 1. The goal is a verification predicate f that evaluates the constructed map and determines how much map to construct. With f fixed, only two unit operations exist: reconstruct the map using a new information source or choose which zero node to flip. The model separates learning invariants from implementation machinery and remains valuable despite the rolled-back /teach optimization."
body_hash: "cd258855"
connections:
  - type: idea
    slug: "knowledge-map-format"  # auto
  - type: idea
    slug: "learning-dynamics"  # auto, review: 0.588
  - type: idea
    slug: "knowledge-mastery-two-axis-model"  # auto, review: 0.586
  - type: idea
    slug: "attention-pointer-learning-model"  # auto, review: 0.586
  - type: idea
    slug: "hermeneutic-circle-learning"  # auto, review: 0.575
  - type: idea
    slug: "freedom-exploration-generator"  # auto, review: 0.568
  - type: idea
    slug: "pattern-pipeline"  # auto, review: 0.566
  - type: idea
    slug: "goal-predicate-f"  # auto, review: 0.560
  - type: idea
    slug: "knowledge-reconnection"  # auto, review: 0.557
  - type: idea
    slug: "learning-method-v2"  # auto, review: 0.555
  - type: idea
    slug: "data-pattern-prediction-chain"  # auto, review: 0.536
  - type: idea
    slug: "transfer-high-leverage"  # auto, review: 0.530
  - type: idea
    slug: "memorization-in-pipeline"  # auto, review: 0.524
  - type: idea
    slug: "reconnection-doc-method"  # auto, review: 0.523
  - type: idea
    slug: "learning-pipeline"  # auto, review: 0.518
  - type: idea
    slug: "ai-cannot-learn-after-training"  # auto, review: 0.516
  - type: idea
    slug: "structural-patience"  # auto, review: 0.514
  - type: idea
    slug: "human-structure-ai-completeness"  # auto, review: 0.509
  - type: idea
    slug: "implicit-improvement-pattern"  # auto, review: 0.502
  - type: idea
    slug: "structure-native-learning-machine"  # auto, review: 0.540
  - type: idea
    slug: "structure-native-tools"  # auto, review: 0.512
importance: 2.94  # auto
---
# Fundamental Model of Learning

A 5-part theory of how learning works, distilled during the `/teach` optimization attempt (2026-08-24). The full optimization failed and was rolled back, but the underlying model — separable from the machinery built on it — remains valuable.

## The 5 Postulates

### 1. The Knowledge Map Is Constructed, Not Discovered

There is no complete map of any domain. The knowledge map is built from the information sources you find and the user provides, combined with the model's own knowledge. It is always partial, always provisional, always revisable. In the broad sense the map includes not just knowledge but the application, combination, and construction of knowledge — which is what makes "complete a project" a legitimate goal.

### 2. The Structure Is a Recursive DAG

A domain is a level-1 node; its subdomains are level-2; and so on down to minimal indivisible units of knowledge. Each minimal node has exactly two states: 0 (not known) or 1 (known). Higher levels are coarse-grainings of the same minimal nodes, not a separate kind of truth.

### 3. Learning Is Single-Threaded

At any one time, exactly one minimal node flips from 0 to 1, and it may only flip when its prerequisites are already 1.

### 4. The Goal Is a Verification Predicate f

The goal is a function f that takes the constructed map G (some nodes 0, some 1) and returns 0 or 1: goal not achieved, or achieved. f is the only input that comes from outside the learning itself, and it constrains how much map to construct — "construct until f is decidable and true".

### 5. Exactly Two Unit Operations

With f fixed, every unit of work is either (a) reconstruct the map using a new information source — the user's or the AI's — or (b) choose which 0 to flip to 1. Everything else — order, spread, assessment rhythm — is a strategy on the map.

## Value

The model separates the invariants of learning (what a goal is, what a knowledge structure is, how learning proceeds) from the machinery that implements them. Even when the implementation built on it (MAP.md, the single-thread state machine, the strategy catalogue) proved too heavy for daily use, the model itself stands as a useful lens for thinking about learning systems.
