---
id: idea-20260604-lppf01
title: Local Patterns Cannot Be Generalized Through Continuous Patching
tags:
- methodology
- meta-cognition
- epistemology
- induction
- framework-design
summary: "Continuous patching of local patterns fails to produce a global framework because each addition only fits a new local phenomenon onto an old structure, analogous to drawing tangents that never converge to the true curve. The correct method is to accumulate diverse samples, let patterns cluster, then induce the framework. This requires delaying framework labeling until a threshold (e.g., three chapters) is reached, freezing existing framework files in the meantime. The idea explains why the old approach fails, while framework-from-data.md describes the positive method; together they represent an inversion of induction and accumulation."
importance: 3.92  # auto
connections:
- type: idea
  slug: framework-from-data
- type: project
  slug: linguistic-structure-analysis
- type: idea
  slug: natural-language-narration-methodology
- type: idea
  slug: audit-blind-spot-spec-limitation
- type: permanent
  slug: 卡片笔记写作法c1.3
- type: permanent
  slug: 卡片笔记写作法c2.2
- type: permanent
  slug: 技术的本质c2.2
- type: idea
  slug: three-layer-framework
  - type: idea
    slug: "structural-patience"  # auto
  - type: idea
    slug: "framework-extraction-pattern"  # auto, review: 0.565
  - type: idea
    slug: "data-pattern-prediction-chain"  # auto, review: 0.519
  - type: idea
    slug: "freedom-exploration-generator"  # auto, review: 0.515
  - type: idea
    slug: "system-coevolution-p2-interpretability"  # auto, review: 0.512
---
# Local Patterns Cannot Be Generalized Through Continuous Patching

## The Problem

In the linguistic structure analysis project, the earliest "fundamental principle" — that topic→elaboration is the only structural relationship — was established based on Ch05 P1-P5 (5 highly argumentative paragraphs). When sentences 26-29 exhibited a paragraph organization pattern (scene construction) that didn't fit, a "continuous patching" strategy was adopted: adding new entries to the existing template, trying to make the framework accommodate new cases.

The result: the template grew increasingly complex (topic→elaboration → topic→elaboration + scene construction → + parallel enumeration → + dilemma exploration...), but it did not become more "universal" — each round of patching merely glued a new local phenomenon onto the old framework. Eventually the framework became impossible to accept or use.

## Core Judgment

**Local patterns plus local patterns do not equal a global pattern.** Each step of continuous patching is addition on top of the current framework (an algebraic expression of local experience), not a move closer to a global pattern. This is analogous to drawing tangents point by point on a curve — each step fits the current point, but the overall shape does not converge to the true curve.

The correct order: first accumulate a sufficiently diverse set of samples, let patterns cluster naturally, then induce a framework. Induction happens after data accumulation, not every time new data arrives.

## Concrete Strategy

Because "accumulate enough samples before summarizing" is itself difficult (it requires tolerating the uncertainty of "having data but no framework"), a supporting workflow was set up:

1. **Ban framework labels during the analysis phase.** Describe the organizational pattern of each paragraph in natural language, without applying any existing terminology.
2. **Accumulation threshold.** Only after at least 3 full chapters of analysis (or an equivalent amount of text) do you go back to cluster and induce.
3. **Freeze framework files.** Until the data threshold is met, text-structure-types.md and structure-constraint-mapping.md remain frozen, with their current content downgraded to "Ch05 P1-P5 observation notes."

## Relationship to the from-data Idea

`framework-from-data.md` describes "what should be done" (build frameworks from data). This idea describes "why the old approach fails" — continuous patching is essentially an inversion of induction and accumulation: each new data point does not enter the sample pool to await clustering, but directly impacts the framework structure. The two are the positive and negative sides of the same methodological shift.
