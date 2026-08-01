---
id: "idea-20260627-memproc01"
title: "Memorized Offline Procedures — When Skills Can't Rely on AI Presence"
tags: [skill-design, memorization, offline, physical, constraint, procedure]
status: raw
created: 2026-06-27
updated: 2026-06-27
source_type: "manual"
source_path: null
importance: 0
permanent_note_material: false
material_since: null
material_expiry_days: 14
promoted_from: null
links: []
related_entities:
  - type: skill
    slug: post-run-stretching
    relation: first-instance
    strength: 0.9
    dimensions: [concept-relation]
    bidirectional: true
    source: manual
  - type: idea
    slug: timeline-based-project-structure
    relation: relates-to-m-model
    strength: 0.4
    dimensions: [concept-relation]
    bidirectional: true
    source: manual
---

# Memorized Offline Procedures

## The Constraint

Some procedures happen **away from screens and AI** — stretching after a run, cooking, physical exercises, in-person social interactions. During these moments, you cannot consult a skill document or ask AI to walk you through steps.

For these, the standard skill format (offline responsibility + online AI-guided steps) is the wrong container.

## The Requirement

The procedure must be **memorized**. Not "referenced when needed" — fully internalized. The skill file becomes the canonical source for review and correction, not the execution guide.

## Design Implication

This splits skills into two classes:

| Class | Execution Context | Memory Requirement | AI Role |
|-------|-------------------|-------------------|---------|
| **AI-present** | At a screen, AI available | Low — AI walks you through | Real-time guide |
| **Offline-memorized** | Away from screens | High — must recall from memory | Reviewer/corrector after the fact |

Post-run stretching is the first recognized instance of the second class. The skill file documents the routine; the user memorizes it; AI checks in afterward ("did you do it? anything tight?").

## Connection to (M, A) Model

An offline-memorized procedure lives entirely in **M** (memory) during execution. The skill file is the **A** (artifact) backup — consulted only when M fails (forgot a stretch) or needs updating (found a better variation).
