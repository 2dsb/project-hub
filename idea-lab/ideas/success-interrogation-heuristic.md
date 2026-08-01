---
id: "idea-20260719-success-interrogation-heuristic"
title: "Success Interrogation Heuristic — Generalize, Replicate, Migrate"
status: raw
source_type: daily
source_path: null
importance: 3
permanent_note_material: true
material_since: 2026-07-19
material_expiry_days: 30
promoted_from: null
tags:
  - meta-cognition
  - success
  - replication
  - migration
  - learning
  - heuristics
related_entities:
  - type: idea
    slug: leverage-existing-vs-build-from-scratch
    relation: applies-pattern
    strength: 0.7
    dimensions: [concept-relation]
    bidirectional: true
    source: manual
  - type: idea
    slug: transfer-high-leverage
    relation: applies-pattern
    strength: 0.6
    dimensions: [concept-relation]
    bidirectional: true
    source: manual
links: []
created: 2026-07-19
updated: 2026-07-19
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
