---
id: idea-20260610-qc01
title: Four-Layer Product Quality Model: 6 Cross-Layer Comparisons + 4 Internal Consistencies = 10-Dimensional Audit Space
tags:
- meta-cognition
- system-design
- quality-assurance
- audit
- methodology
- framework
summary: "The Four-Layer Product Quality Model classifies any product into Philosophy, Acceptance Criteria, Spec, and Product levels, yielding a complete audit space of 6 cross-layer comparisons (C(4,2)) plus 4 internal consistencies, totalling 10 dimensions. The recursive-planner audit framework only"
importance: 10
connections:
- type: idea
  slug: audit-blind-spot-spec-limitation
- type: project
  slug: project-hub
- type: idea
  slug: system-coevolution
- type: idea
  slug: system-coevolution-p2-interpretability
- type: idea
  slug: system-coevolution-p4-self-reinforcement
- type: idea
  slug: knowledge-as-dictionary-of-perspectives
- type: idea
  slug: unified-python-execution-model
- type: idea
  slug: abstraction-barrier-as-dual-perspective-bridge
- type: idea
  slug: objective-importance-scoring
- type: idea
  slug: reconnection-doc-method
  - type: idea
    slug: "checklist-completeness-audit"  # review: 0.504
---
# Four-Layer Product Quality Model: 6 Cross-Layer Comparisons + 4 Internal Consistencies = 10-Dimensional Audit Space

## Model

Any "product" (software system, document, design) is produced at four levels:

```
Philosophy ──→ Acceptance Criteria ──→ Spec ──→ Product
```

| Level | Definition | Example in M34 |
|------|------|-------------|
| **Philosophy** | Why this product exists, what fundamental promises it claims to deliver | "Coevolution," "All structures can change," "Global data reachability" |
| **Acceptance Criteria** | Measurable, decidable criteria that the philosophy is translated into | The 5 perfection standards in perfection-roadmap |
| **Spec** | Concrete design specification — how to do it, what format, what algorithm | `skills/coevolution-system.md` Steps 1-7 |
| **Product** | Actual output — code, config, docs, runtime behavior | `scripts/` + `resources/coevolution/` + actual runtime results |

## Six Cross-Layer Comparison Types

4 levels → C(4,2) = 6 pairs. These 6 comparisons **exhaust all possible audit types**. There is no 7th.

| # | Comparison Pair | Audit Type | Question |
|---|--------|---------|------|
| **1** | Philosophy ↔ Acceptance Criteria | **Commitment Translation Audit** | Has every aspect of the philosophy been correctly translated into measurable criteria? Are there dimensions in the philosophy that the criteria missed? Are there criteria measuring things the philosophy doesn't care about? |
| **2** | Philosophy ↔ Spec | **Design Philosophy Audit** | Do the Spec's design decisions embody the philosophy? Or is the spec chasing engineering convenience and forgetting the original intent? |
| **3** | Philosophy ↔ Product | **Design Promise Audit** | Does the product actually deliver what the philosophy claims? Skip the spec — hold the product directly against the philosophy. This is the "naive user" perspective. |
| **4** | Acceptance Criteria ↔ Spec | **Criteria Coverage Audit** | Does every acceptance criterion have a corresponding implementation design in the spec? Is the spec over-engineered beyond what the acceptance criteria demand? |
| **5** | Acceptance Criteria ↔ Product | **Acceptance Testing** | Does the product actually pass the acceptance criteria? This is "testing" in the truest sense — checking behavior, not code. |
| **6** | Spec ↔ Product | **Correspondence Audit** | Does the code literally align with the spec? This is what the three rounds of recursive-planner audit have been doing. |

### Four-Level Internal Consistency

Beyond comparing against the other 3 levels, each level may also have internal quality issues — involving no other level. C(4,2) + 4 = **10 dimensions**. This is the complete audit space.

| # | Audit Target | Audit Type | Question |
|---|---------|---------|------|
| **7** | Philosophy Internal | **Philosophical Coherence Audit** | Are there contradictions among the philosophy's various declarations? "Must evolve but must not change structure" — can these two promises coexist? Has it promised something it cannot deliver? |
| **8** | Acceptance Criteria Internal | **Measurement Completeness Audit** | Is every acceptance criterion measurable? Are there mutually contradictory criteria (two criteria that cannot be satisfied simultaneously)? Are there implicit dependencies on undefined preconditions? |
| **9** | Spec Internal | **Design Consistency Audit** | Are there logical contradictions between different sections of the spec? Does an algorithm description in one place depend on a concept undefined elsewhere? Do referenced files and directories exist? |
| **10** | Product Internal | **Engineering Quality Audit** | Does the code have bugs, performance issues, or security vulnerabilities? Are module boundaries clear? Even if the product perfectly matches the spec (#6 PASS), the code itself may have engineering quality issues beyond correctness (e.g., memory leaks, O(n²) complexity, missing exception handling). |

**The complete quality space = 6 cross-layer comparisons + 4 internal consistencies = 10 dimensions.** There is no 11th dimension.

## Discovery Process

This model emerged from a meta-cognition dialogue after M34's three rounds of perfection:

1. The user asked "Will the content in suggestion-templates.yaml evolve?"
2. Answer: "No" — the template text is static and rigid
3. Follow-up: Why did the three audit rounds (R1: 25 findings, R2: 18 findings, R3: 14 findings) miss this?
4. Root cause: The three audit rounds only did **#6 (Spec↔Product)**. The discovery path for template rigidity is **#3 (Philosophy↔Product)** — directly holding the "coevolution" philosophy against the product reveals that templates don't evolve
5. **If only #6 is done, this problem can never be discovered** — because #6's reference points do not include "philosophy"

## M34's Audit Coverage Status

```
         ┌── #7: Never done ❌
         │
Philosophy ── Acc. Criteria ── Spec ── Product
  │    ┌── #8: Never done ❌    │     ┌── #9: Partial ✅    │     ┌── #10: Partial ✅
  │    │                        │     │                     │     │
  │    │   └─────∧──────────────┘     │   └─────∧───────────┘     │
  │    │         #4 ❌                │         #6 ✅              │
  │    │                             │                            │
  │    └─────────∧───────────────────┘                            │
  │              #5 ❌                                            │
  │                                                               │
  └───────────────────────────────────────────────────────────────┘
           #1 ❌, #2 ❌, #3: Occasional (user-triggered) ⚠️
```

| Dimension | Status | Notes |
|------|------|------|
| #6 Spec↔Product | ✅ Full coverage | Three rounds of recursive-planner audit |
| #9 Spec Internal | ⚠️ Partial | Cross-reference errors corrected, but logical contradictions not systematically checked |
| #10 Product Internal | ⚠️ Partial | Simplify catches duplicate code, but perf/security not checked |
| #3 Philosophy↔Product | ⚠️ Occasional | Only triggered by user-initiated questions (e.g., the template rigidity discovery) |
| #1, #2, #4, #5, #7, #8 | ❌ Never | Never been systematically executed |

**Out of 10 dimensions: 1 fully covered, 2 partially covered, 1 occasionally covered, 6 never covered.**

## Generalization: This Is Not an M34 Problem — It's a Universal Audit Law

Any audit framework that only does #6 (including recursive-planner) has an inherent ceiling: **correspondence audit can only find things the spec says but the product doesn't do. It cannot find things the spec should have said but didn't, much less things the philosophy should have demanded but the acceptance criteria didn't require.**

To break through this ceiling, different audit roles and different reference points are needed:

| Comparison | Required Role | Reference Point |
|------|-----------|--------|
| #6 Spec↔Product | Correspondence Auditor (A/B/D/E) | Spec + code |
| #5 Acc. Criteria↔Product | Test Executor | Acceptance criteria + runtime data |
| #4 Acc. Criteria↔Spec | Requirements Reviewer | Acceptance criteria + spec |
| #3 Philosophy↔Product | Devil's Advocate / Naive User | Philosophy statement + product behavior |
| #2 Philosophy↔Spec | Design Philosopher | Philosophy + spec design decisions |
| #1 Philosophy↔Acc. Criteria | Product Manager | Philosophy + acceptance criteria |
| #7 Philosophy Internal | Logician | Philosophy statements set |
| #8 Acc. Criteria Internal | Measurement Engineer | Acceptance criteria set |
| #9 Spec Internal | Systems Architect | Full spec text |
| #10 Product Internal | Engineering Quality Reviewer | Product code/config |

**recursive-planner is not a complete quality assurance framework — it covers #6 (correspondence audit) plus partial aspects of #9 and #10.** The remaining 7 dimensions require external review or a naive perspective that does not read the spec.

## Operational Recommendations

For any important system in Project Hub, when auditing:

1. **Declare coverage scope**: Clearly state which dimensions (1-10) the current audit is covering
2. **Mark uncovered dimensions**: Explicitly note which dimensions were not checked — "zero findings" does not equal "zero problems"
3. **Periodic full-dimensional audits**: Not all 10 dimensions every time (too costly), but at least every N iterations do #1-#3 and #7-#8 (philosophy-level audits)
4. **Built-in Devil's Advocate**: Introduce a role that does not read the spec and only looks at philosophy and product behavior (covering #3)

## Connections

- Directly derived from the `audit-blind-spot-spec-limitation` discovery, elevating it from "one specific M34 defect" to "a universal framework for all audits"
- Used for audit methodology improvements in Project Hub
- Can be used to assess the limitations of the recursive-planner framework itself
- Related to the "streaming thought framework": the 4 layers can be viewed as a source→transform→spec→sink flow graph

## Importance Rationale

Marked as importance: 10 (highest). Reasons:

1. **This is not a defect in a specific system, but a structural framework for audit methodology itself** — it impacts quality assurance for all future systems in Project Hub (not just M34)
2. **It explains why "zero findings" can be a false positive** — not because the audit was not rigorous, but because the audit dimensions were incomplete
3. **The 10 dimensions are exhaustive** — C(4,2)=6 cross-layer comparisons + 4 internal consistencies = 10 dimensions. This is a closed formal model that won't go stale or require revision (unlike most ideas, this is not a hypothesis — it's a complete classification system)
4. **Directly actionable** — each comparison maps to a specific audit role and input, implementable as role extensions to recursive-planner
5. **Generalizes beyond Project Hub** — any product development that has a "philosophy layer" (games, writing, system design) fits this four-layer model
