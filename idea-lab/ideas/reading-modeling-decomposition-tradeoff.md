---
id: "idea-20260711-rm01"
title: "Reading-Modeling Decomposition Tradeoff — Explained by Cohesion-Coupling Heuristic"
tags: [reading, modeling, methodology, decomposition, learning, cohesion-coupling, tradeoff]
summary: "The reading-modeling decomposition tradeoff arises from two competing costs: merge costs when modeling after each chapter, which are editorial boundaries that often don't align with natural conceptual subsystems, and memory decay costs when modeling after the whole book, since memory (M) fades over time. The cohesion-coupling heuristic shows that optimal decomposition chooses boundaries to maximize internal cohesion and minimize coupling, not inherit editorial splits; chapters are narrative units, not structural ones. Consequently, the ideal strategy is somewhere between per-chapter and whole-book modeling, such as after a natural conceptual cluster, balancing merge costs against memory decay. Pre-reading lowers merge costs by providing a rough map, and structural patience avoids forcing structure on non-conceptual boundaries."
body_hash: "2ce1ca2c"
importance: 3.91  # auto
connections:
  - type: idea
    slug: cohesion-coupling-decomposition-heuristic
  - type: idea
    slug: how-to-deal-with-complexity
  - type: idea
    slug: breadth-first-trap
  - type: idea
    slug: structural-patience
  - type: idea
    slug: attention-pointer-learning-model
  - type: idea
    slug: locate-first-model-last
  - type: idea
    slug: knowledge-as-dictionary-of-perspectives
  - type: project
    slug: deep-learning-book
  - type: idea
    slug: "content-independent-framework"  # review: 0.565
  - type: idea
    slug: "connection-reading"  # auto, review: 0.546
  - type: idea
    slug: "framework-extraction-pattern"  # auto, review: 0.537
  - type: idea
    slug: "reading-writing-unity"  # auto, review: 0.529
  - type: idea
    slug: "framework-from-data"  # auto, review: 0.513
---
# Reading-Modeling Decomposition Tradeoff

## The Tradeoff

When reading a book to build a model:

| Strategy | Pros | Cons |
|----------|------|------|
| Model after each chapter | Low memory load, incremental | Chapters ≠ natural subsystem boundaries → frequent model merging needed |
| Model after the whole book | One clean decomposition, no merging | Requires holding everything in memory; early chapters fade before reaching the end |
| Model after a whole field | Optimal decomposition possible | Superhuman memory requirement |

This is a **two-cost problem**: merge costs (from bad decomposition boundaries) vs. memory decay costs (from M declining with time away from material). The optimal strategy sits at the point where these two costs balance — not at either extreme.

### The Memory Decay Side

From the [[timeline-based-project-structure]]: Memory (M) is a state variable that **rises with engagement and decays with time away**. If you read Chapter 1 on day 1 and don't model until day 30 (after finishing the whole book), M for Chapter 1 has decayed substantially. By the time you're ready to model, you've lost the detail you'd need for a good decomposition.

This means the "whole book first" strategy has a hidden cost: **the decomposition may be structurally optimal, but it's built from degraded material**. You're making clean cuts on blurry memories.

### The Two-Cost Curve

```
Cost
 ↑
 │   ╲ merge cost (decreases as you wait longer to model)
 │    ╲
 │     ╲____ total cost (U-shaped)
 │     ╱
 │    ╱
 │   ╱ memory decay cost (increases as you wait longer to model)
 └─────────────────────→ Time before modeling
     per-chapter     whole-book
```

The optimal modeling point is where total cost is minimized — neither right after each chapter, nor after the whole book. It's somewhere in between, likely after a **natural conceptual cluster** (a set of chapters that form a high-cohesion unit).

## Explanation via Cohesion-Coupling

The cohesion-coupling heuristic says: a good decomposition has high internal cohesion and sparse external coupling. 

**Chapters are editorial boundaries, not structural ones.** A book's chapter divisions serve narrative and pedagogical purposes — they don't necessarily reflect the natural concept boundaries of the subject matter. Concepts span chapters; later chapters reframe earlier ones; a single chapter may contain tightly-coupled material that belongs together but also loose references to other chapters.

So if you treat chapters as subsystems and model each one independently:
- The chapter-subsystem has **unknown** internal cohesion (might be high, might not)
- The coupling between chapter-subsystems is **uncontrolled** — could be sparse, could be dense
- You'll discover the coupling later (when later chapters reference earlier concepts) → model merging

Conversely, if you wait until you've read everything:
- You can *choose* the subsystem boundaries that maximize cohesion and minimize coupling
- The decomposition is structural, not editorial
- But the memory cost may be prohibitive

## The Ideal (Superhuman) Strategy

Read an entire field's literature, hold it all in memory, then perform a single optimal decomposition. This is only possible for a superhuman — or for a system with perfect external memory.

## Practical Implications

1. **Chapter-by-chapter modeling is a memory-management compromise**, not an optimal decomposition strategy. The merge costs are the price of bounded memory.
2. **The optimal reading unit for modeling is not the chapter** — it's whatever unit minimizes inter-unit coupling. This might be a cluster of related chapters, or a concept thread that runs through multiple chapters.
3. **Pre-reading (skimming the whole book first) reduces merge costs**: even a shallow map of the territory lets you anticipate coupling before committing to sub-models.
4. **This explains why "read the whole book, then model" produces better models** — not because of some vague "holistic understanding," but because the decomposition boundaries are chosen structurally rather than inherited editorially.

## Connection to [[structural-patience]]

Structural patience says: don't force structure too early. This is why — premature structure inherits editorial boundaries that don't match conceptual boundaries.
