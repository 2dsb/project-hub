---
id: idea-20260702-reconnection-method
title: Three-Layer Classification Method for Reconnection Docs
tags:
  - knowledge-reconnection
  - methodology
  - framework
  - meta-cognition
summary: "The Three-Layer Classification Method for Reconnection Docs applies the three-layer framework as a"
importance: 3
connections:
  - type: idea
    slug: "three-layer-framework"
  - type: idea
    slug: "knowledge-reconnection"
  - type: idea
    slug: "four-layer-quality-model"
  - type: idea
    slug: "checklist-completeness-audit"
  - type: idea
    slug: "content-independent-framework"
  - type: idea
    slug: "human-structure-ai-completeness"
  - type: idea
    slug: "residuals-as-honesty-device"
  - type: idea
    slug: "structural-patience"
  - type: idea
    slug: "transfer-high-leverage"  # review: 0.554
  - type: idea
    slug: "framework-from-data"  # review: 0.512
---
# Three-Layer Classification Method for Reconnection Docs

**The method**: When building a reconnection doc for a new chapter, use the three-layer framework as the *starting lens*, not as a post-hoc discovery. The process reduces to four steps.

## Step 1: Classify Every Important Concept

Three operational questions map any concept to its layer:

| Question | If Yes | If No |
|----------|--------|-------|
| Is it precise and unambiguous? | → Technical or Math | → Conceptual |
| Does it explain *why* something works? | → Math | → Technical |
| Would it still be true if no algorithm used it? | → Math | → Technical |

These three questions exhaustively partition the space. Every concept lands in exactly one layer.

## Step 2: Organize Within Each Layer

- **Conceptual layer**: Order by causal direction (which idea induced which technical structure)
- **Technical architecture layer**: Q → A, following the constraint chain (high-entropy Q → progressively constrained → low-entropy executable A)
- **Math layer**: Object → features → conceptual correspondence → embedding point in Technical

## Step 3: Map Cross-Layer Connections

Only four standard connection patterns exist:

| Direction | Pattern | Example |
|-----------|---------|---------|
| Conceptual → Technical | Induces / shapes | NFL → necessity of inductive bias |
| Math → Conceptual | Rigorous fact yields high-entropy concept | Bayes error → "perfection is impossible" |
| Math → Technical | Embedded at specific position in A | MLE math → cost function slot |
| Within Technical | Q → A via constraint | E (natural language) → dataset (math structure) |

## Step 4: List Residuals

Content that resists classification. Listed explicitly with reasons — nothing silently dropped.

## Why This Works

The Ch5 reconnection work validated this method on 116 concepts. The three-layer framework was initially discovered bottom-up from the content; it took hours of iterative sorting. But once the framework existed, the classification criteria emerged naturally. Starting from the criteria on the next chapter eliminates the discovery cost — classification becomes mechanical, and the human's energy goes to cross-layer connections (the intellectually interesting part).

## Relationship to Existing Methods

- **Extends** [[knowledge-reconnection]]: Adds a systematic classification step before the encode phase. The original method's "human outlines architecture → AI assembles → human reviews" workflow remains; this method changes what the human does in step 1 from "articulate content-specific organization" to "classify by three universal criteria."
- **Derived from** [[three-layer-framework]]: The three-layer framework is the static structure; this method is the operational procedure for applying it to new content.

