---
id: "idea-20260621-gs01"
summary: "The Goal Singularity principle asserts that every activity should pursue exactly one goal, because splitting attention between two sets of evaluation criteria overloads limited working memory and degrades both outcomes. Instead of attempting to "kill two birds with one stone," separate tasks like understanding and language expression into two independent activities (e.g., first draft in native language, then translate), halving cognitive load and improving total efficiency. This cognitive goal perspective complements the learning pipeline's source-route-sink decomposition, demanding that during the sink stage, "output in your own words" and "express in the target language" be split. The principle applies mainly to learning and creation scenarios, with natural communication as an exception, and its detection question is noticing simultaneous weighing of two evaluation criteria."
title: "Goal Singularity"
tags: [meta-cognition, learning, productivity, focus, goal-design]
importance: 3.27  # auto
connections:
  - type: idea
    slug: "learning-pipeline"  # auto
  - type: skill
    slug: "reading-blocker-triage"
  - type: idea
    slug: "completion-vs-quitting"  # auto
  - type: idea
    slug: "breadth-first-trap"  # auto
  - type: idea
    slug: "clarity-as-universal-principle"  # auto
  - type: idea
    slug: "attention-pointer-learning-model"  # auto
  - type: idea
    slug: "attention-as-bottleneck"  # review: 0.550
  - type: idea
    slug: "success-interrogation-heuristic"  # review: 0.507
---
# Goal Singularity

## Trigger
After finishing the Chinese draft and English translation of the MIT 6.S184 analogy story, I realized that writing in Chinese and translating into English are two completely different activities — the former checks understanding, the latter practices language. If I had written in English from the start, the two goals would have interfered with each other: "Did I understand this correctly?" and "Does this sound natural?" battling for the same cognitive slot.

## Core Idea
**Every activity should have exactly one goal.** Not "kill two birds with one stone," but "one bird, one stone" — aim, then fire.

When you mix two goals into a single activity, both suffer. Split them into two independent activities, each pursuing a single goal, and the total efficiency actually goes up.

## Why "Two Birds, One Stone" Is a Trap Here

```
Two birds, one stone (wrong):
  Write analogy story in English → simultaneously pursue "correct understanding" + "natural language"
  → attention split in half → neither side done well

One bird, one stone (right):
  Activity 1: Write analogy story in Chinese → pursue only "understand correctly, express clearly"
  Activity 2: Translate sentence by sentence into English → pursue only "language sounds natural"
  → cognitive load halved per activity → both done well
```

Cognitive psychology explanation: working memory is limited (~4 chunks). Optimizing two goals simultaneously means maintaining two sets of evaluation criteria in your head at once — that's a working memory overflow in itself (see `wm-overflow-prevention`).

## Examples

| Scenario | Mixed together (wrong) | Split apart (right) |
|----------|------------------------|---------------------|
| Learning a new concept | Take notes in English | First understand in native language → then write notes in English |
| Writing a blog post | Write directly in English | First draft in native language → then translate |
| Reading a paper | Look up every unknown word | First rough-read for understanding → then go back and look up words |
| Learning to code | Watch tutorial while coding a project | First watch → then code |

## Relationship with the Learning Pipeline

`learning-pipeline` decomposes the learning process from the "source → route → sink" perspective; goal singularity decomposes it from the **cognitive goal** perspective. The two are orthogonal but complementary:

- Learning pipeline asks: **Where is the information at this stage?** (source / route / sink)
- Goal singularity asks: **What is my brain pursuing at this stage?** (understanding? expression? memorization?)

During the pipeline's "sink" stage, goal singularity demands that "output in your own words" and "express in the target language" be split into two independent activities — which is exactly the native-language-draft → translate pattern.

## One Exception

Some activities naturally have only one goal and need no splitting. Example: chatting with a friend — the goal is simply "communicate"; there's no tension of "first understand in native language, then express in English." This principle mainly applies to learning/creation scenarios where goals can be cleanly separated.

## Detection Question
When you feel yourself "weighing two sets of criteria in your head simultaneously while doing one thing," the goals haven't been fully separated. Ask yourself: am I pursuing A or B right now? If the answer is "both" → split into two steps.
