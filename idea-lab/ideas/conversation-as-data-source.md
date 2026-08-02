---
id: idea-20260608-cd01
title: Conversation as Data Source
tags:
- system-design
- coevolution
- data-source
- conversation
- M34
summary: "The core claim is that conversation logs are an essential but currently missing data source for the M34 system, because the chat window is the sole entry point for information, and failing to archive conversations means losing the richest behavioral data. The solution proposes saving conversations before each session ends to feed them into the M34 timeline, likening the unarchived flow to ore dropping off a conveyor belt. Implementation issues include deciding between raw transcript versus structured extraction and choosing a save location."
body_hash: "06dd021f"
importance: 3.73  # auto
connections:
- type: idea
  slug: system-coevolution-p1-data-coverage
- type: idea
  slug: m34-source-layer-static-rigidity
- type: idea
  slug: chat-as-idea-source
- type: idea
  slug: system-coevolution
- type: idea
  slug: daily-to-ideas-pipeline-broken
  - type: idea
    slug: "conversation-topic-flow"  # review: 0.539
  - type: idea
    slug: "contact-management"  # review: 0.512
---
# Conversation as Data Source

## Trigger
Realized that the only way "information enters" the system is through the chat window. All thinking, decisions, and ideas happen inside conversations — if those conversations aren't saved, the richest behavioral data is lost.

## Problem
M34 currently has 4 data sources (daily notes, entity CRUD, M33 relations, raw analysis), but is missing a 5th: conversation logs.

## Solution
Save the conversation before each session ends, and use it as a new data source for the M34 timeline.

## Flow Perspective
The chat window is the "conveyor belt" between user and system — if what moves across that belt doesn't get archived, it's like ore coming off a mining rig and dropping straight onto the ground, never collected.

## Implementation Issues to Resolve
- Save format: raw transcript vs. structured extraction (pull out ideas / decisions / action items)
- Save location: `daily/` directory vs. standalone `transcripts/` directory vs. feed directly into the timeline
- Privacy / length: conversations can be very long and may need compression or summarization
