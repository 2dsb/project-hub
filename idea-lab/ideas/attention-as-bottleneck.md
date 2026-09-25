---
id: "idea-20260626-attn01"
title: "Attention as the Bottleneck — Single-Threaded Execution in Learning & Life"
tags: [attention, bottleneck, single-threading, goal-singularity, learning-design, life-modeling]
summary: "Human attention is a single-threaded bottleneck, like a CPU that can only execute one project at a time, so time blocks are mutually exclusive and the central design problem becomes scheduling which project gets the next attention slot. Unattended projects experience M-decay simultaneously while focus is elsewhere. Goal-singularity and attention-singularity are the same constraint at different levels—purpose and execution. Attention residue, carrying project A’s mental state into project B’s time block, may impair effective M dynamics, and reconnection docs could reduce this residue by acting as clean save points, enabling full release and engagement."
body_hash: "ec855027"
importance: 4.34  # auto
connections:
  - type: idea
    slug: "goal-singularity"  # auto
  - type: idea
    slug: "timeline-based-project-structure"  # auto
  - type: idea
    slug: "attention-pointer-learning-model"  # auto
  - type: idea
    slug: "willingness-experiment"  # review: 0.562
  - type: idea
    slug: "breadth-first-trap"  # review: 0.536
  - type: idea
    slug: "three-mental-resources"  # review: 0.509
  - type: idea
    slug: "speed-first-model-second-batch-tradeoff"  # review: 0.507
  - type: idea
    slug: "transfer-high-leverage"  # review: 0.506
  - type: idea
    slug: "integrating-fragmented-life-strategies"  # auto, review: 0.584
  - type: idea
    slug: "deep-work-recovery-cycle"  # auto, review: 0.574
  - type: idea
    slug: "low-energy-ideation"  # auto, review: 0.562
  - type: idea
    slug: "completion-vs-quitting"  # auto, review: 0.555
  - type: idea
    slug: "learning-dynamics"  # auto, review: 0.549
  - type: idea
    slug: "practice-as-learning-purpose"  # auto, review: 0.544
  - type: idea
    slug: "structural-patience"  # auto, review: 0.537
  - type: idea
    slug: "learning-pipeline"  # auto, review: 0.535
  - type: idea
    slug: "memorization-in-pipeline"  # auto, review: 0.520
  - type: idea
    slug: "where-innovation-comes-from"  # auto, review: 0.520
  - type: idea
    slug: "anki-for-english-conversation"  # auto, review: 0.511
  - type: idea
    slug: "system-coevolution"  # auto, review: 0.510
  - type: idea
    slug: "freedom-exploration-generator"  # auto, review: 0.504
  - type: idea
    slug: "learning-method-v2"  # auto, review: 0.528
  - type: idea
    slug: "hermeneutic-circle-learning"  # auto, review: 0.508
  - type: idea
    slug: "low-occupancy-segment-reflection"  # auto
  - type: idea
    slug: "teach-task-volume-scaling"  # auto
  - type: idea
    slug: "occupancy-pair-scheduling"  # auto, review: 0.568
  - type: idea
    slug: "async-work-mode"  # auto, review: 0.546
  - type: idea
    slug: "practice-necessity-willingness-tradeoff"  # auto, review: 0.544
  - type: idea
    slug: "sunk-cost-tug-and-salvage"  # auto, review: 0.515
  - type: idea
    slug: "idle-as-unstable-state"  # auto
  - type: idea
    slug: "mental-clutter-degree"  # auto
  - type: idea
    slug: "newcomer-window"  # auto, review: 0.509
  - type: idea
    slug: "letters-to-future-self"  # auto, review: 0.508
  - type: idea
    slug: "activity-cost-benefit"  # auto, review: 0.575
  - type: idea
    slug: "role-system"  # auto, review: 0.565
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
