---
id: idea-20260702-operational-criteria
title: Operational Yes/No Criteria Beat Descriptive Labels for Classification
tags:
- methodology
- framework-design
- classification
importance: 2
connections:
  - type: idea
    slug: three-layer-framework
  - type: idea
    slug: reconnection-doc-method
  - type: idea
    slug: content-independent-framework
  - type: idea
    slug: framework-extraction-pattern
---



# Operational Yes/No Criteria Beat Descriptive Labels for Classification

**Insight**: A framework described by its internal logic ("the conceptual layer is high-entropy, the math layer is low-entropy") is hard to use. The same framework described by operational questions ("Is it precise and unambiguous? No → Conceptual") is a 30-second decision tool.

**The three criteria that emerged from Ch5**:
1. "Is it precise and unambiguous?" No → Conceptual. Yes → Technical or Math.
2. "Does it explain *why* something works?" Yes → Math. No → Technical.
3. "Would it still be true if no algorithm used it?" Yes → Math. No → Technical.

**Why this matters**: Descriptive labels require you to first understand the framework, then apply it. Operational questions collapse understanding and application into one step. Each question is a binary test — you don't need to hold the whole framework in your head; you just need three yes/no decisions.

**Rule of thumb**: When designing a classification system, always ask: "Can someone who doesn't understand this system yet use it to classify a new item in 30 seconds?" If not, the labels are descriptive but not operational.
