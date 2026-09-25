---
id: "idea-20260719-success-interrogation-heuristic"
title: "Success Interrogation Heuristic — Generalize, Replicate, Migrate"
tags:
  - meta-cognition
  - success
  - replication
  - migration
  - learning
  - heuristics
summary: "The Success Interrogation Heuristic—Generalize, Replicate, Migrate—turns a single win into a permanent capability upgrade by identifying the reusable mechanism behind a success. When something works unusually well, ask three questions: generalize to find the abstract pattern, replicate to reuse the exact mechanism, and migrate to port the underlying principle to a different domain. For example, the teach skill automated transformation of structured source material into interactive lessons, enabling an intense learning sprint. The heuristic includes a falsification step to detect context-bound, person-bound, or phase-bound constraints that block migration. While the teach skill is confirmed reusable, whether the automated-transformation principle can migrate beyond learning remains an open question."
body_hash: "4f5cd439"
importance: 1.76  # auto
connections:
  - type: idea
    slug: "leverage-existing-vs-build-from-scratch"  # auto
  - type: idea
    slug: "transfer-high-leverage"  # auto
  - type: idea
    slug: "framework-extraction-pattern"  # review: 0.579
  - type: idea
    slug: "freedom-exploration-generator"  # review: 0.561
  - type: idea
    slug: "practice-as-learning-purpose"  # review: 0.537
  - type: idea
    slug: "teach-method-fixes"  # review: 0.534
  - type: idea
    slug: "memorized-offline-procedures"  # review: 0.512
  - type: idea
    slug: "goal-singularity"  # review: 0.507
  - type: idea
    slug: "methodology-change-timing"  # review: 0.506
  - type: idea
    slug: "memorization-in-pipeline"  # review: 0.503
  - type: idea
    slug: "learning-pipeline"  # auto, review: 0.548
  - type: idea
    slug: "pass-criteria-as-curriculum-design"  # auto, review: 0.535
  - type: idea
    slug: "knowledge-mastery-two-axis-model"  # auto, review: 0.535
  - type: idea
    slug: "teach-coverage-check"  # auto, review: 0.527
  - type: idea
    slug: "peer-cross-teaching"  # auto, review: 0.505
  - type: idea
    slug: "analogical-transfer-conditions"  # auto, review: 0.503
  - type: idea
    slug: "hermeneutic-circle-learning"  # auto, review: 0.547
  - type: idea
    slug: "learning-method-v2"  # auto, review: 0.526
  - type: idea
    slug: "ai-centered-new-education-industry"  # auto, review: 0.513
  - type: idea
    slug: "enumerative-as-scaffold-for-generative"  # auto, review: 0.513
  - type: idea
    slug: "practice-necessity-willingness-tradeoff"  # auto, review: 0.501
  - type: idea
    slug: "pattern-pipeline"  # auto
  - type: idea
    slug: "plugin-architecture-vs-defaults"  # auto, review: 0.569
  - type: idea
    slug: "goal-predicate-f"  # auto, review: 0.535
  - type: idea
    slug: "sunk-cost-tug-and-salvage"  # auto, review: 0.531
  - type: idea
    slug: "teach-application-scope"  # auto, review: 0.547
  - type: idea
    slug: "learning-cycle-microstructure"  # auto, review: 0.565
---
# Success Interrogation Heuristic — Generalize, Replicate, Migrate

## The trigger

This learning sprint (3 tracks, 3 days, ~17 lessons across Python/RAG/Agents) succeeded largely because of one factor: finding and using the teach skill (mattpocock/teach), which automated lesson generation from structured source materials. Without it, each lesson would have required manual design — impossible in the available time.

The meta-question: **can this success factor be generalized, replicated, or migrated to other contexts?**

## The heuristic

Every time something works unusually well, ask three questions:

1. **Generalize**: What's the abstract pattern behind this success? (Here: "automated transformation of structured source material into interactive lessons" — not specific to Python or RAG or Agents.)
2. **Replicate**: Can I use the exact same mechanism again? (Here: yes — the teach skill is reusable for any future learning track with structured source material.)
3. **Migrate**: Can the underlying principle be ported to a different domain? (Here: the principle is "find a tool that automates the transformation from raw material to consumable output." In other domains: code generation, note summarization, plan generation — any structured-input-to-structured-output pipeline.)

## Why this matters

Most success analysis focuses on *what happened* (the outcome). This heuristic focuses on *what made it happen* (the mechanism). Outcomes are one-shot; mechanisms are reusable. If you can identify the mechanism behind a success and determine its portability, you convert a single win into a permanent capability upgrade.

## Counter-examples (when migration fails)

Not every success mechanism migrates. Some are:

- **Context-bound**: the mechanism only works in a specific environment (e.g., the internship deadline created urgency that won't exist later)
- **Person-bound**: the mechanism depends on a specific person's availability or skill
- **Phase-bound**: the mechanism works at one stage of learning but not another

The interrogation should include a falsification step: "under what conditions would this NOT work?"

## Status

The teach skill itself is a confirmed win — it's reusable (the skill file exists, the lesson format is templated). The open question is whether the *automated-transformation principle* can be migrated to other project types beyond learning.
