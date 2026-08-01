---
id: "idea-20260620-ast01"
summary: "AI Source Triage proposes inserting an AI layer between source and routing in a flow-based learning pipeline to pre-screen content and identify the highest-value-density subset before the user invests time. The AI acts as a pre-screener, filter, or condenser—traversing material like video courses, social feeds, books, or papers to flag skippable parts, strip off-topic content, and compress repetitive detail. The core insight is that linear traversal of information sources is wildly inefficient; AI can perform one pass of denoising and compression to return only what merits deep attention."
title: "AI Source Triage"
tags: [learning, ai-amplifier, flow-based-thinking, information-filtering]
importance: 2.04  # auto
connections:
  - type: idea
    slug: "flow-based-thinking"  # auto
  - type: idea
    slug: "peer-cross-teaching"  # auto
  - type: idea
    slug: "learning-pipeline"  # auto
  - type: idea
    slug: "x-com-information-source"  # review: 0.561
---
# AI Source Triage

## Trigger
Watching Karpathy's Zero to Hero videos episode by episode wasted some time. A better approach: watch the introduction to understand the goal, then go straight to the source code. But the problem is — without watching the full video, you can't know which parts are worth watching.

## Core Idea
Insert an AI pre-screening layer between source and routing in the flow-based learning pipeline:

```
Source → AI Triage → Routing → Sink
```

What the AI does: traverse the content structure ahead of time and output "which parts are worth your time, and which can be skipped / jumped straight to source code / absorbed as a summary."

## Concrete Example From Today
The micrograd video — if the AI had told me upfront "the intro helps you understand the goal, after that it's a line-by-line walkthrough of engine.py — you'd be faster just reading the source directly," I could have skipped the wasted time in the middle.

## Example 2: X.com Feed
Scrolling through followed content one by one → running into off-topic subjects (e.g. policy), repetitive content, and excessive detail (e.g. long Anthropic safeguard claims where you only need the gist). The AI can act as both a **filter** (strip irrelevant topics) and a **condenser** (compress repetitive / overly detailed content into key points).

## Pattern Abstraction
Both scenarios share the same underlying dynamic: linear traversal of information sources is wildly inefficient. The AI does one pass of denoising + compression before the user invests time. The only difference is which AI role gets emphasis:

| Source | AI Role | Action |
|--------|---------|--------|
| Video courses | Pre-screener | Judge which parts are worth watching, which to skip or jump straight to source |
| X.com feed | Filter + condenser | Strip irrelevant topics + compress repetitive/redundant content |
| Books | Pre-screener | TOC + summary → point out core chapters, skip setup/fluff |
| Papers | Pre-screener + condenser | Abstract + intro + conclusion → distill core contribution into one sentence |
| Long-form articles | Condenser | Compress into key points, flag paragraphs worth deep reading |

Generalized core: for any information source that requires upfront time investment to judge its value, AI can do triage — traverse it before the user does and return the highest-value-density subset.
