---
id: "idea-20260609-dp01"
summary: "the daily→ideas pipeline is broken"
title: "daily→ideas Pipeline Broken: Daily Ideas Not Auto-Extracted"
tags: [process, pipeline, m34, daily-note, idea-extraction]
importance: 5
connections:
  - type: idea
    slug: "m34-source-layer-static-rigidity"  # auto
  - type: idea
    slug: "flow-based-thinking"  # auto
  - type: idea
    slug: "conversation-as-data-source"  # auto
  - type: idea
    slug: "system-coevolution"  # auto
  - type: idea
    slug: "system-coevolution-p1-data-coverage"  # auto
  - type: idea
    slug: "chat-as-idea-source"  # auto
---
# daily→ideas Pipeline Broken: Daily Ideas Not Auto-Extracted

## Discovery
On 06-09, while reviewing the co-evolution system, I noticed that all 7 ideas from yesterday's (06-08) daily note were never extracted as standalone idea files. The newest idea file dates back to 06-06.

## Concrete Case
The 06-08 daily note had 7 ideas. Among them, "Flow-Based Thinking Framework" was explicitly labeled as "a thinking tool worth preserving independently," and a `resources/thinking-tools/flow-based-thinking.md` already exists — yet there is no corresponding entry under the ideas directory.

## Impact
- Ideas exist only within daily notes and are invisible to M34 (daily notes are entities, but the "idea" sub-entries within them are not independent entities)
- Knowledge-axis scanning, pattern detection, and suggestion generation cannot reach these ideas
- The most valuable daily cognitive output gets stranded in journal entries and never enters the knowledge system

## Root Cause
There is no automated or semi-automated extraction pipeline from daily notes to ideas. The user must manually perform the operation of "extract ideas from daily note into idea files" — and this operation is not covered by any system, skill, or reminder.

## Possible Improvement Directions
1. At the end of each day, auto-detect "idea" sections in the daily note and prompt the user to confirm extraction
2. Alternatively: expand the source concept of idea entities to allow direct referencing of daily note sub-entries
3. Or: add a "yesterday idea backfill check" step to the `start` flow
