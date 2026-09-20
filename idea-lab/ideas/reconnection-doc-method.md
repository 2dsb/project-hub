---
id: idea-20260702-reconnection-method
title: Three-Layer Classification Method for Reconnection Docs
tags:
  - knowledge-reconnection
  - methodology
  - framework
  - meta-cognition
summary: "The three-layer classification method uses the conceptual, technical architecture, and math layers as a starting lens to partition any important concept via three yes/no questions: is it precise and unambiguous, does it explain why something works, and would it still be true if no algorithm used it. Within each layer, concepts are organized by causal direction, Q→A constraint chain, or object-to-features-to-embedding correspondence. Cross-layer connections follow exactly four patterns: conceptual induces technical structure, math yields high-entropy conceptual ideas, math embeds at specific positions in the technical architecture, and within technical, Q leads to A through constraint. Any content resisting classification is listed explicitly as a residual. This approach, validated on 116 concepts, makes classification mechanical and redirects human effort to the intellectually interesting cross-layer connections. It extends the knowledge-reconnection method by adding a systematic, universal classification step before encoding, derived from the static three-layer framework."
body_hash: "fb4db999"
importance: 5.15  # auto
connections:
  - type: idea
    slug: "three-layer-framework"  # auto
  - type: idea
    slug: "knowledge-reconnection"  # auto
  - type: idea
    slug: "four-layer-quality-model"  # auto
  - type: idea
    slug: "checklist-completeness-audit"  # auto
  - type: idea
    slug: "content-independent-framework"  # auto
  - type: idea
    slug: "human-structure-ai-completeness"  # auto
  - type: idea
    slug: "residuals-as-honesty-device"  # auto
  - type: idea
    slug: "structural-patience"  # auto
  - type: idea
    slug: "transfer-high-leverage"  # review: 0.554
  - type: idea
    slug: "framework-from-data"  # review: 0.512
  - type: idea
    slug: "knowledge-as-dictionary-of-perspectives"  # auto
  - type: idea
    slug: "data-pattern-prediction-chain"  # auto, review: 0.585
  - type: idea
    slug: "interaction-as-dictionary"  # auto, review: 0.554
  - type: idea
    slug: "learning-pipeline"  # auto, review: 0.550
  - type: idea
    slug: "connection-reading"  # auto, review: 0.549
  - type: idea
    slug: "flow-based-thinking"  # auto, review: 0.546
  - type: idea
    slug: "local-pattern-patching-failure"  # auto, review: 0.543
  - type: idea
    slug: "classification-of-concepts"  # auto, review: 0.533
  - type: idea
    slug: "interaction-as-essence-heuristic"  # auto, review: 0.518
  - type: idea
    slug: "fix-result-backward"  # auto, review: 0.505
  - type: idea
    slug: "understanding-a-field-in-layers"  # auto, review: 0.570
  - type: idea
    slug: "discipline-division-and-internal-structure"  # auto, review: 0.553
  - type: idea
    slug: "fundamental-model-of-learning"  # auto, review: 0.523
  - type: idea
    slug: "broad-then-deep-recursion"  # auto, review: 0.520
  - type: idea
    slug: "pattern-pipeline"  # auto, review: 0.501
  - type: idea
    slug: "structure-native-learning-machine"  # auto, review: 0.520
  - type: idea
    slug: "interpretable-world-model-pipeline"  # auto, review: 0.503
  - type: idea
    slug: "letters-to-future-self"  # auto, review: 0.525
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

