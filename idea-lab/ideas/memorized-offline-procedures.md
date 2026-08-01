---
id: "idea-20260627-memproc01"
summary: "Some procedures occur away from screens and AI, requiring full memorization instead of real-time AI guidance. This creates two classes of skills: AI-present, where AI walks you through steps, and offline-memorized, where you must recall the procedure from memory. The skill file becomes a canonical source for review and correction, not an execution guide. In the (M, A) model, an offline-memorized procedure lives entirely in memory during execution, with the artifact consulted only when memory fails or updates are needed. Post-run stretching is the first recognized instance of this class."
title: "Memorized Offline Procedures — When Skills Can't Rely on AI Presence"
tags: [skill-design, memorization, offline, physical, constraint, procedure]
importance: 1.32  # auto
connections:
  - type: skill
    slug: "post-run-stretching"
  - type: idea
    slug: "timeline-based-project-structure"  # auto
  - type: idea
    slug: "implicit-improvement-pattern"  # review: 0.537
  - type: idea
    slug: "success-interrogation-heuristic"  # review: 0.512
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
