---
id: idea-20260719-pass-criteria-as-curriculum-design
title: "Pass Criteria as a First-Class Curriculum Design Element"
tags:
  - learning
  - curriculum-design
  - teach
  - pass-criteria
  - assessment
summary: "Pass criteria should be treated as a first-class curriculum design element, not an afterthought, and must be stated before any lesson content because they define the observable behavior that constitutes evidence of learning. An explicit Pass Bar specifies precisely what the learner must be able to do at the exit gate—for example, trace an agent loop rather than write one from scratch—which directly shapes where effort is invested and calms “am I done?” anxiety. This approach reveals whether the lesson’s medium even suits its goal, since a document is wrong when the pass criteria demand a working pipeline. Distinct from learning objectives, the pass criteria form the micro-level of the practice-as-purpose hierarchy, with the internship deadline as the macro-level reason to learn, together creating a two-level purpose structure."
body_hash: "b5aa7984"
importance: 2.93  # auto
connections:
  - type: idea
    slug: practice-as-learning-purpose
  - type: idea
    slug: "teach-method-fixes"  # review: 0.565
  - type: idea
    slug: "teach-coverage-check"  # review: 0.508
  - type: idea
    slug: "explaining-excellent-sheep-with-theory"  # auto, review: 0.547
  - type: idea
    slug: "success-interrogation-heuristic"  # auto, review: 0.535
  - type: idea
    slug: "learning-pipeline"  # auto, review: 0.513
  - type: idea
    slug: "enumerative-as-scaffold-for-generative"  # auto, review: 0.534
  - type: idea
    slug: "learning-method-v2"  # auto, review: 0.525
---
# Pass Criteria as a First-Class Curriculum Design Element

## The observation

During the teach-RAG, teach-Agent, and teach-runoob-python tracks, a pattern emerged: before reading each lesson's document, the natural first question should be "What's the pass criteria?" — not "What will I learn?", but "How will I know I've learned it?"

Examples:
- A lesson on tool calling: pass = can trace a Thought→Action→Observation loop on paper? Or write a working `@tool` decorator? The prep work is completely different.
- A lesson on embeddings: pass = can explain cosine similarity in conversation? Or build a vector search from scratch?
- A lesson on async/await: pass = can read async code without getting lost? Or write a coroutine that fetches 3 URLs concurrently?

## The principle

**Pass criteria are not an afterthought — they are a first-class element of curriculum design.** They should be stated before the lesson content, not after. They determine:

1. **What counts as evidence** — reading comprehension vs. writing ability vs. debugging ability are distinct skills; "I learned X" is meaningless without specifying which one
2. **Where the learner invests effort** — knowing the pass criteria upfront eliminates the "am I done?" anxiety and lets the learner calibrate depth in real time
3. **Whether the lesson is even the right format** — if the pass criteria is "write a working pipeline," a document is the wrong medium; you need a lab

## Implication for the teach skill

Every lesson should lead with an explicit **Pass Bar** statement, e.g.:

> **Pass bar:** After this lesson, you should be able to trace an agent loop given a conversation log — identifying which step is Thought, which is Action, and which is Observation. You do NOT need to write a working agent from scratch.

This is distinct from "learning objectives" (which describe content). The pass bar describes **observable behavior** at the exit gate.

## Connection to practice-as-learning-purpose

The pass criteria are the micro-level version of the practice-as-purpose principle. The internship deadline answers "why learn this at all?"; the pass bar answers "what does 'learned' look like for this specific lesson?" Together they form a two-level purpose hierarchy: macro (practice event) → micro (pass criteria).
