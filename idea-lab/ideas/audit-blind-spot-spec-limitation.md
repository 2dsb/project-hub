---
id: idea-20260610-ar01
title: Audit Blind Spot — Spec-based review misses what the spec itself is missing
tags:
- meta-cognition
- system-design
- audit
- methodology
- M34
- design-review
summary: "Spec-based review can only find discrepancies between implementation and spec; it is blind to gaps in the spec itself. The M34 recursive-planner audits failed to catch that template text was static and would never evolve, despite the system’s own co-evolution claim, because the audit criteria only verified that the spec’s explicit requirements were met. This structural blind spot creates a false sense of security as finding counts drop across rounds. To break through, audit methodology needs a Design Commitment Audit layer that checks whether publicly promised properties, like evolvability, are actually realized, supplemented by a Devil’s Advocate role asking naive questions and periodic commitment-reality comparisons driven by user inquiry."
importance: 5.27  # auto
connections:
- type: idea
  slug: "m34-source-layer-static-rigidity"
- type: project
  slug: "project-hub"
- type: idea
  slug: "four-layer-quality-model"
- type: idea
  slug: "local-pattern-patching-failure"
- type: idea
  slug: "system-coevolution-p4-self-reinforcement"
- type: idea
  slug: "system-coevolution"
- type: idea
  slug: "nature-of-review"
  - type: idea
    slug: "checklist-completeness-audit"  # review: 0.534
  - type: idea
    slug: "standard-engineering"  # review: 0.514
  - type: idea
    slug: "two-perspective-system-correctness"  # auto, review: 0.510
---
# Audit Blind Spot — Spec-based review misses what the spec itself is missing

## Discovery Process

M34 went through three rounds of recursive-planner audits (R1: 25 findings, R2: 18 findings, R3: 14 findings), and none of them caught the design flaw that "template text is static and will never evolve." This flaw was ultimately discovered through an offhand user question: "For example, could the content in suggestion-templates.yaml 'evolve'?"

## Root Cause Analysis

The three-layer audit criteria (M34's own declaration → change cost → universal software principles) can catch **things the spec said to do but the code didn't do**, but cannot catch **things the spec should have said but didn't**.

Concretely:
- R017 found "templates hardcoded in Python source" → R2 extracted to YAML → marked resolved
- Audit criteria judged: original spec says "templates should have format specs" → YAML file has format specs → PASS
- The question nobody asked: **What does the name "co-evolution" promise? As the most directly user-facing system output, shouldn't templates be capable of evolving too?**

The focus evolution across the three audit rounds also reflects this blind spot:
- R1: looking for structural gaps (what doesn't exist)
- R2: looking for broken loops (what isn't connected)
- R3: looking for code errors (what's written wrong)
- Not a single round looked for: **what should evolve but was designed as rigid**

## Core Insight

**What an audit can find has a ceiling: spec-based review can only find gaps between implementation and spec — it cannot find gaps in the spec itself.**

Breaking through this ceiling requires **design commitment review** — not checking what the spec says, but checking whether the system's name and its publicly claimed promises are fully realized.

## Prevention Methods

### 1. Add a fourth layer to audit criteria: Design Commitment Audit

For every system property that claims to be "evolvable" or "mutable," check one by one: is it actually evolving? Or did it just move to a different location?

### 2. Introduce an external challenger role (Devil's Advocate)

After the audit completes, a role that doesn't read the spec and only looks at the promises asks naive, outsider questions:
- "You say you evolve. Give me three examples."
- "What else should evolve but doesn't?"

### 3. Periodic "commitment-reality" comparison

Every 30 days, list all promises the system publicly makes, and verify against runtime data whether they are actually happening. Flag entries that are "promised but not happening."

### 4. Leverage the user's natural questions

The user's naive perspective ("Does this evolve?") is the most effective detection mechanism. Systematize incorporating such questions into the design review process.

## Connections

- This is the same pattern as the "source-layer static rigidity" finding: both involve "a gap between what the system claims to be capable of and what it actually does, and this gap falls outside the spec's coverage."
- Directly improves the project hub's audit methodology — not just an M34 issue, but a problem for all future system reviews.

## Importance Note

Marked as importance: 9 (highest level), reasons:
1. This is not a local defect in M34, but a **structural blind spot in the entire audit methodology**
2. Three rounds of audits with decreasing finding counts creates a false sense of security that "the system is improving" — and that sense of security is partially fake, because the audit tool itself determines which findings can appear
3. If the audit method is not corrected, all future systems (not just M34) will be affected by the same blind spot
4. The fix is cheap and actionable (add one audit dimension, one role, one periodic check)

