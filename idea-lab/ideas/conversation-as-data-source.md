---
id: idea-20260608-cd01
title: Conversation as Data Source
tags:
- system-design
- coevolution
- data-source
- conversation
- M34
summary: "Conversations are the sole entry point for information into the system, yet they are not currently saved, resulting in the loss of the richest behavioral data. The M34 system uses four data sources—daily notes, entity CRUD, M33 relations, and raw analysis—and a fifth source of conversation logs should be added. Treating the chat window as a conveyor belt, archiving what moves across it prevents valuable data from dropping away uncollected. Unresolved implementation issues include whether to save raw transcripts or extract structured ideas, where to store the logs, and how to handle long conversations through compression or summarization."
importance: 0
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
