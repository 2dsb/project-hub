---
id: idea-20260601-kr01
title: Knowledge Reconnection Mechanism (Knowledge Reconnection Cost Reduction)
tags:
- knowledge-management
- learning
- recovery
- productivity
status: refined
created: 2026-06-01
updated: 2026-06-24
source_type: null
source_path: null
importance: 0
permanent_note_material: false
material_since: null
material_expiry_days: 14
promoted_from: null
related_entities:
  - type: project
    slug: "ai-ability"
    relation: "productivity/efficiency method connection"
    strength: 0.5
    bidirectional: true
    source: "migration"
  - type: ideas
    slug: "behavioral-activation-model"
    relation: "complement"
    strength: 0.5
    dimensions: ["complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "illness-reframing"
    relation: "complement"
    strength: 0.6
    dimensions: ["complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "learning-pipeline"
    relation: "complement"
    strength: 0.55
    dimensions: ["complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "reading-bottleneck"
    relation: "complement"
    strength: 0.5
    dimensions: ["complement"]
    bidirectional: true
    source: "auto"
  - type: project
    slug: "deep-learning-book"
    relation: "application-target"
    strength: 0.8
    dimensions: []
    bidirectional: true
    source: "manual"
  - type: idea
    slug: "transfer-high-leverage"
    relation: "transfer-source"
    strength: 0.8
    dimensions: []
    bidirectional: true
    source: "manual"
---
# Knowledge Reconnection Mechanism

> **v2 (2026-06-24)**: Refined with PCA encode/decode framework. Triggered by reading Deep Learning (Goodfellow) — memory decay between sessions, especially with technical vocabulary.

## Core Model: Encode/Decode (PCA Analogy)

Knowledge reconnection is an **encode/decode process**, analogous to PCA:

- **Encode** = writing the reconnection doc after reading → compressing the content into a low-dimensional representation (like keeping the first *k* principal components)
- **Decode** = reading the reconnection doc later → reconstructing the knowledge structure from the compressed form

The goal is NOT lossless reconstruction. It's **dimensionality preservation**: capture the directions of maximum variance in the original understanding — the structural relationships between concepts — not every data point.

### Four Constraints on the Encode

| # | Constraint | What It Rules Out |
|---|-----------|-------------------|
| 1 | **Low decode cost** — minimal time, energy, and mental effort to reconstruct | Raw re-reading, dense summaries |
| 2 | **Structured model output** — decode produces a mental model, not flat facts | Bullet lists that preserve facts but lose relationships |
| 3 | **Main points preserved** — the decoded structure covers the essential content (details can be omitted, main points must survive) | Over-aggressive compression that drops structural nodes |
| 4 | **Minimal length** given 1–3 — the doc should be as short as possible while satisfying the above | Verbose notes that are just the original in disguise |

The PCA metaphor naturally handles the tension between constraints 2 and 3: a structured model requires encoding *relationships* on top of content, which costs more dimensions than a flat summary. The trade-off is between doc length and explained variance — find the elbow where additional detail yields diminishing returns.

## Encode: Writing the Reconnection Doc (During/After Learning)

Instead of taking notes for future reference, write explicitly **for future reconstruction**. The distinction: notes document "what's in the book"; reconnection docs encode "what I understood and how."

### Structure

The reconnection doc's format adapts to the content's natural organization — there is no fixed template, only invariants. The Ch2 instance used a 4-layer architecture (abstraction → representations → operations → features → questions) because linear algebra has a natural taxonomic structure. A narrative-heavy chapter might use an argument chain + counterarguments format. Domain-adaptive, not one-size-fits-all.

**Invariants** (every reconnection doc must have these):

1. **Start summary** (≤30s decode): A compact table or 3-line summary at the top — the entry point for the impatient returning reader
2. **Structural model**: The concepts organized into relationships, in whatever form fits the content (dependency graph, layer architecture, argument chain, etc.). This is constraint 2 made concrete.
3. **Residuals section**: Content that resisted structuring, explicitly listed with reasons. Constraint 3 made transparent.
4. **Progression marker**: Where stopped, what's next, recommended decode order

### Encoding Procedure: Structure-First with Residual Disclosure

The procedure prioritizes constraint 2 (structured model) as far as possible, then honestly documents what resists structuring — this transparency serves constraint 3 (main points preserved) because knowing what's NOT in the model is itself structural information.

**Step 1: Maximize structure.** For each concept/section, attempt to fit it into the dependency graph or self-explanation format. Push as far as it goes.

**Step 2: Document residuals.** For content that genuinely resists structuring (e.g., empirical observations, caveats that don't form a dependency, historical context, edge cases), list them explicitly in a **Residuals** section:

```
### Residuals
<!-- Content that resisted structuring. Listed explicitly so constraint 3 is preserved — nothing important is silently dropped. -->
- [fact/caveat/observation] — why it doesn't fit the graph
```

**Step 3: Self-check.** After encoding, scan the residuals list. Ask: *Could any of these be structural after all?* If yes, promote it into the graph. If no, it stays — the gap is honest.

This prevents the silent failure mode: a doc that looks structured but silently dropped important content. The residuals section makes incompleteness visible and actionable.

### Full Encoding Workflow (Human + AI)

The procedure above is the structural logic. But actually producing a reconnection doc involves a human-AI division of labor. The Ch2 Linear Algebra doc (2026-06-24, `resources/deep-learning/ch2-linear-algebra.md`) established this workflow as a concrete instance:

**Phase 1: Human outlines the architecture.** After finishing the chapter, the human holds the content in working memory. Their job is to articulate the *organization* — not the definitions:

1. What is the primary abstraction hierarchy of this chapter? (e.g., scalar→vector→matrix→tensor)
2. What are the major categories of concepts? (e.g., representations, operations, features, questions)
3. How do these categories relate? (e.g., operations are global, features are representation-local)
4. What are the capstone compositions? (e.g., PCA ties everything together)
5. What resists structuring? (explicitly name the residuals)

The human does NOT write formal definitions — that's the AI's job. The human provides the *structural skeleton*.

**Phase 2: AI assembles the doc.** Given the skeleton, the AI:

1. Writes rigorous definitions for every concept (fundamental equation → define pieces → compact form)
2. Maps all linkages — both within categories and cross-category
3. Formats the dependency graph and linkages summary
4. Ensures residuals are explicitly listed with reasons
5. Adds the start summary (≤30s decode entry point)

**Phase 3: Human reviews and corrects.** This is where structural flaws surface:

- **False analogies**: The AI may force a metaphor that doesn't hold (e.g., scalar=word, vector=sentence). The human catches these because they violate the structure's internal logic.
- **Definition format**: The human enforces the definition flow (e.g., start from Av=λv, not from A=VΛV⁻¹).
- **Factual errors**: The AI may get mathematical relationships wrong (e.g., singular values = |eigenvalues|, not squared). The human's working memory of the chapter catches these.

**Phase 4: Constraint compliance check.** After corrections, verify all 4 constraints:

| Constraint | Check |
|-----------|-------|
| 1 — Low decode cost | Is there a ≤30s entry point (start summary)? |
| 2 — Structured model | Does decode produce a mental model, not a fact list? |
| 3 — Main points preserved | Are residuals explicitly listed? Does anything important live only in the residuals that should be structural? |
| 4 — Minimal length | Can any section be cut without violating 1-3? |

If any constraint fails, iterate. The Ch2 doc required one iteration (add start summary for constraint 1, correct eigendecomposition↔SVD for constraint 3).

**Key insight about the human-AI split**: The human provides *structural insight* (what the concepts are and how they relate — the directions of variance). The AI provides *definitional precision* and *linkage mapping* (filling in the details consistently). The human's review catches errors where the AI's pattern-matching produces plausible but wrong outputs. This division maps to the PCA analogy: the human picks the principal components; the AI computes the projection.

**Example instance**: `resources/deep-learning/ch2-linear-algebra.md` — 5 categories, 14 standard-form features + 5 decomposition features, 3 residuals, full linkage map, ~330 lines with start summary.

## Decode: Reconstructing Knowledge (When Returning After a Gap)

1. **Read the start summary first** — ≤30s to reconstruct the architecture. Anchors your brain to the problem space before diving in.
2. **Traverse the structural model** — however the doc organizes it (dependency graph, layer architecture, argument chain). Trace from foundational concepts outward; let dependents rebuild naturally.
3. **Check residuals** — the explicitly listed gaps tell you what the model *doesn't* capture. If a residual matters for your current purpose, go to the source for just that point.
4. **Accept gaps** — the goal is knowing "where I was and what's next," not perfect recall. If a concept doesn't reconstruct, that's a signal to re-read only that specific section of the original.

## Why This Works

The PCA analogy captures something the original "re-entry point" concept didn't: **the doc is a projection, not a summary**. A summary preserves content at reduced resolution. A projection preserves *directions of variation* — the structural axes along which the knowledge is organized. Decoding from a projection requires an active reconstruction step (like PCA inverse transform), which is cognitively more engaging than passive re-reading and produces a more integrated mental model.

## Application Target

- **Deep Learning Book** (Goodfellow): Apply per-chapter. Each chapter's reconnection doc follows the 4-constraint encode format. Decode before each new chapter to maintain continuity.
- **General**: Any dense technical reading with multi-session timeline. Particularly valuable when sessions are irregular or interrupted.

## Relationship to Existing System

- `skills/low-energy-cognitive.md`: Maintains thinking during low-energy periods; this mechanism manages knowledge recovery *after* such periods
- `resources/` directory: Reconnection docs should live alongside the resource they encode (e.g., `resources/deep-learning/ch2-pca.md` alongside chapter notes)
- `daily/` files: Recovery progress logged in daily reflections
