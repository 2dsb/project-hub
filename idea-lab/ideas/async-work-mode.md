---
id: idea-20260814-async-work-mode
title: "Async Work Mode — Overlap Tasks Instead of Idling While You Wait"
tags:
  - time-management
  - productivity
  - async
  - workflow
  - task-overlap
summary: "The note argues for switching from a synchronous, single-threaded work mode to an async work mode where waiting on an agent is treated like a Python coroutine that yields to other tasks. Instead of idle-waiting, use the waiting window as a slot to start the next task, draft the next piece, or drain another queue, because idle-waiting splits the day into non-overlapping working and waiting stretches with a hidden cost. The open question is how to choose gap-filling work without letting context-switching costs eat the time gain."
body_hash: "3c9d63ad"
connections:
  - type: idea
    slug: "attention-as-bottleneck"  # auto, review: 0.546
  - type: idea
    slug: "low-occupancy-segment-reflection"  # auto, review: 0.538
  - type: idea
    slug: "timeline-based-project-structure"  # auto, review: 0.536
  - type: idea
    slug: "efficiency-formula"  # auto, review: 0.504
  - type: idea
    slug: "idle-as-unstable-state"  # auto, review: 0.580
importance: 0.0  # auto
---
# Async Work Mode — Overlap Tasks Instead of Idling While You Wait

When I'm doing something that requires waiting — like waiting for an agent to finish executing — I tend to fall into an idle waiting state. This is single-threaded, synchronous mode: one task blocks, and nothing else runs until it returns.

The insight is to switch to an async model, the way Python's `async` works. Instead of blocking on the wait, treat the waiting task as a coroutine and yield to other work. The waiting window becomes a slot for a second task, so time is used more fully.

Concretely: while an agent runs, don't just watch it — start the next task, draft the next piece, or drain another queue. The cost of idle-waiting is hidden but real, because it splits the day into "working" and "waiting" stretches with no overlap.

Open question: how do you pick what to fill the gap with, without the context-switching cost eating the gain?
