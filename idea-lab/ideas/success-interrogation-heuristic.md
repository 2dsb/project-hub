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
summary: "The Success Interrogation Heuristic prompts asking Generalize, Replicate, and Migrate each time something works unusually well, converting single wins into permanent capability upgrades by focusing on the reusable mechanism rather than the one-shot outcome. For a learning sprint that succeeded because the teach skill automated transforming structured source material into interactive lessons, the abstract pattern is automated transformation of raw material into consumable output, which is replicable via the skill file and might migrate to other structured-input-to-structured-output pipelines like code generation or note summarization. The interrogation includes a falsification step identifying when the mechanism is context-bound, person-bound, or phase-bound, ensuring portability is not assumed blindly."
importance: 3
connections:
  - type: idea
    slug: "leverage-existing-vs-build-from-scratch"
  - type: idea
    slug: "transfer-high-leverage"
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
