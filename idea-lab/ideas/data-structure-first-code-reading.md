---
id: "idea-20260719-data-structure-first-code-reading"
title: "Data Structure First — Memorize Shapes Before Reading Code"
importance: 3.47  # auto
tags:
  - learning
  - code-reading
  - data-structures
  - mental-model
  - comprehension
summary: "Memorizing core data structures before reading control flow improves comprehension because data shapes are finite and stable, making code transformations obvious. Once you know the input and output shapes, function bodies become just transformations between them, so code reads like a story instead of requiring constant questioning of types. Rote memorization is underrated: it provides the scaffolding that deeper understanding can later hang on. This data-structure-first approach operates at the single-codebase level and complements locate-first-model-last, which maps perspectives at a knowledge-graph level."
body_hash: "d83552c5"
connections:
  - type: idea
    slug: locate-first-model-last
  - type: idea
    slug: "environment-diagram-dual-perspective"  # auto
  - type: idea
    slug: "human-machine-code-reading-gap"  # review: 0.578
  - type: idea
    slug: "call-tree-as-third-perspective"  # review: 0.569
  - type: idea
    slug: "teach-method-fixes"  # review: 0.538
  - type: idea
    slug: "name-object-binding-as-perspective"  # review: 0.523
  - type: idea
    slug: "attention-pointer-learning-model"  # review: 0.522
  - type: idea
    slug: "memorization-in-pipeline"  # review: 0.511
  - type: idea
    slug: "framework-extraction-pattern"  # review: 0.506
  - type: idea
    slug: "learning-pipeline"  # auto, review: 0.507
  - type: idea
    slug: "data-pattern-prediction-chain"  # auto, review: 0.501
---
# Data Structure First — Memorize Shapes Before Reading Code

## The observation

When learning a new codebase or system, identifying and memorizing the core data structures *before* tracing the control flow dramatically improves comprehension. The data shapes are the skeleton; the code is just the meat moving around it.

Concrete example from the Agent track:

Once you know that `messages` is `list[dict]` where each dict has `{"role": str, "content": str}` (and optionally `tool_calls`, `tool_call_id`, `name`), and that `response` from `llm_chat()` has a `.choices[0].message` shaped the same way — then code like this becomes trivially imaginable:

```python
response = llm_chat(messages, tools=tool_schemas)
messages.append(response.choices[0].message)
messages.append({
    "role": "user",
    "content": f"LLM call failed: {e}. Please continue."
})
```

Without the data shapes memorized, each line requires stopping to ask: "What type is `response`? What keys does `message` have? What does `append` do here?" With the shapes memorized, the code reads like a story.

## The principle

**Data structures are higher-leverage than control flow for initial comprehension.** Reasoning:

1. **Data shapes are finite and stable** — there are usually 3-5 core data types in a system, and they change slowly. Control flow is unbounded and branching.
2. **Data shapes explain the code** — once you know the input shape and output shape of a function, the function body is often obvious (it's just a transformation from A to B).
3. **Rote memorization is underrated** — "just memorize the shapes" is dismissed as shallow, but it provides the scaffolding that deeper understanding can later hang on. You can't reason about transformations if you can't visualize the things being transformed.

## Contrast with locate-first-model-last

`locate-first-model-last` says: map the keys (perspectives) first, build structure later. `data-structure-first` says: within a single key/perspective, memorize the data shapes before tracing the logic. They're complementary: locate-first operates at the knowledge-graph level; data-structure-first operates at the single-codebase level.

## Practical rule

When approaching unfamiliar code:
1. Find the 3-5 core data structures (classes, typed dicts, message formats, DB schemas)
2. Memorize their shapes — literally, be able to draw them from memory
3. *Then* read the code that manipulates them

The memorization step feels like wasted time but is actually the highest-ROI investment in the comprehension process.
