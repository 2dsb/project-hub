---
id: "idea-20260627-memproc01"
title: "Memorized Offline Procedures — When Skills Can't Rely on AI Presence"
tags: [skill-design, memorization, offline, physical, constraint, procedure]
importance: 0
connections:
  - type: skill
    slug: "post-run-stretching"
  - type: idea
    slug: "timeline-based-project-structure"
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
