---
id: "idea-20260713-is01"
title: "Objective Importance Scoring — Two Orthogonal Dimensions for Idea Evaluation"
tags: [meta-cognition, importance-scoring, idea-evaluation, m33, cross-axis, system-design, methodology, objective-metrics]
summary: "The note proposes replacing subjective importance scores with an objective two-dimensional metric: Knowledge-Layer Centrality, measuring an idea's structural position in the idea graph via hubness and generativity, and Execution-Layer Penetration, measuring how many projects and skills reference the idea, with projects weighted double. These dimensions are orthogonal because an idea can be deeply central yet unused, or widely applied without being theoretically central. The composite score weights penetration slightly higher (0.55) as a bias toward action, but dependency on M33 cross-axis scanning makes M33 maintenance essential to compute penetration and prevent collapse into a single dimension."
body_hash: "5cabbc0b"
importance: 2.49  # auto
connections:
  - type: idea
    slug: "knowledge-as-dictionary-of-perspectives"  # auto
  - type: idea
    slug: "four-layer-quality-model"  # auto
  - type: idea
    slug: "cohesion-coupling-decomposition-heuristic"  # auto
  - type: idea
    slug: "system-coevolution"  # auto
  - type: idea
    slug: "audit-blind-spot-spec-limitation"  # auto
  - type: project
    slug: "project-hub"
---
# Objective Importance Scoring — Two Orthogonal Dimensions

## Problem

Current `importance` scores are assigned manually at creation time with no standard — leading to drift: a highly practical idea like knowledge-reconnection gets `importance: 0` while others get `7-9` with no consistent justification. Subjective "feels important" doesn't scale.

## Evolution: Three → Two Dimensions

Initial proposal had three dimensions:
1. Unification Power — backlink count × strength
2. Cross-Axis Influence — project/skill references
3. Generative Power — descendant idea count

Analysis revealed they aren't orthogonal:
- **Generative ⊂ Unification**: generative backlinks (`extends`, `builds-on`, etc.) are a subset of all backlinks
- **Unification ↔ Cross-Axis positively correlated**: central ideas are more likely to be discovered and linked to projects

Two genuinely independent axes emerge:

| Dimension | Measures | Orthogonal because... |
|-----------|----------|----------------------|
| **Knowledge-Layer Centrality** | Idea's position in the idea graph | A purely structural property of the knowledge graph |
| **Execution-Layer Penetration** | Whether the idea has crossed into projects/skills | Central ≠ used; used ≠ central |

A deep philosophical concept can score 1.0 on centrality and 0 on penetration. A practical tool can score near 0 on centrality and 1.0 on penetration. These are independent axes.

---

## Dimension 1: Knowledge-Layer Centrality

**What it measures**: How central is this idea in the idea graph?

**Formula**:
```
centrality = w_hub × hubness_score + w_gen × generativity_score
```

Where:
- `hubness_score` = Σ(all backlink strengths) / max, normalized across all ideas
- `generativity_score` = count of backlinks with relation ∈ {extends, builds-on, behavioral-corollary, direct-corollary, generalizes, instance-of, solves} / max, normalized
- `w_hub = 0.5`, `w_gen = 0.5` (provisional)

**Data source**: `ideas/*.md` → `related_entities[].slug` + `.strength` + `.relation`

**Rationale**: Hubness and generativity aren't independent *within* the knowledge layer (generativity ⊂ hubness), but they capture distinct flavors: being widely cited vs. being a seed that produces new ideas. Blending them into one dimension keeps the top-level axes clean and orthogonal.

---

## Dimension 2: Execution-Layer Penetration

**What it measures**: Has this idea crossed into the execution system?

**Formula**:
```
penetration = (project_refs × w_project + skill_refs × w_skill) / max_possible
```

**Calculation**:
1. Scan all `projects/*.md` and `skills/*.md` files' `related_entities[]` fields
2. Count how many projects reference this idea (via `type: "idea"`)
3. Count how many skills reference this idea
4. Weighted sum:
   - `w_project = 2.0` — projects represent active execution, heavier weight
   - `w_skill = 1.0` — skills are capability definitions, lighter weight
5. Normalize

**Data source**: `projects/*.md` and `skills/*.md` → `related_entities[]`

**Rationale**: This is the closest proxy for "behavioral impact" computable from existing data. An idea linked to a project has entered the execution pipeline — it's changing what you *do*, not just what you *know*. Pure knowledge-layer ideas score zero here regardless of elegance — and that's correct: penetration measures a different thing than centrality.

**Critical dependency**: This dimension requires healthy M33 cross-axis scanning. Without it, all ideas score zero on penetration — the entire scoring system collapses to one dimension. M33 maintenance is the backbone of this system.

---

## Composite Score

```
importance = w_centrality × centrality + w_penetration × penetration
```

### Weight Discussion

**Current provisional weights**:

| Weight | Value | Reasoning |
|--------|-------|-----------|
| `w_centrality` | **0.45** | Structural importance in the knowledge graph — the idea's theoretical weight |
| `w_penetration` | **0.55** | Execution impact carries slightly more weight — an idea that changes behavior is more important than one that only enriches understanding |

**Open questions**:
1. `w_penetration > w_centrality` reflects a bias toward action. But some ideas (especially foundational philosophical ones) may take months to penetrate execution — linking lag penalizes them unfairly. Should there be a "grace period" for new ideas?
2. Time decay: an idea referenced heavily 3 months ago but silent since may be less relevant now. Apply exponential decay to backlink contributions?
3. Centrality sub-weights (`w_hub`, `w_gen`): is 50/50 the right split, or should hubness (being referenced by peers) outweigh generativity (being extended)?

---

## Anti-Drift Safeguards

- Scores recomputed automatically on every M33 full scan (or on-demand via `analyze importance`)
- Manual `importance` field in YAML becomes **read-only** — the computed score is written to a separate `computed_importance` field
- If the user disagrees with a computed score, the fix is to **update the links** (add missing `related_entities`), not to manually override the number
- This ensures the score always reflects the actual graph structure

---

## Relationship to M33

M33 cross-axis scanning is the **computation infrastructure** for this system. Without it:
- Dimension 2 (penetration) = 0 for all ideas
- The entire scoring system collapses to one dimension
- Behavioral impact becomes invisible to the importance metric

This makes M33 maintenance no longer optional — it's the backbone of idea evaluation.
