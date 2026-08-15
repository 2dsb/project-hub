---
id: idea-20260802-learning-method-v2
title: "Learning Method v2 — Two-Axis Mastery Cycle with Decay-Aware Maintenance"
importance: -1
tags:
  - learning-method
  - teach-method
  - meta-cognition
  - knowledge-mastery
  - maintenance
  - two-axis-model
summary: "The two-axis model of knowledge mastery separates concept (horizontal interaction density, c) from practice (vertical cross-filter binding, p), with the hard constraint that c must precede p because bindings require an existing conceptual framework. Learning cycles push rapid concept lessons followed by practice lessons that introduce no new concepts, then a three-tier exam spanning all knowledge points to build full-breadth p across easy, medium, and hard tiers. After mastery, maintenance resists decay by first restoring c through free recall (unprompted reconstruction of the concept map) and then restoring p through structured testing with variants—modified tasks that force genuine re-derivation rather than rote recall—scheduled weekly using an Ebbinghaus forgetting curve. This sequencing accounts for p decaying faster than c and c requiring restoration before p can effectively recover, while domain adaptation allows collapsing the practice axis for theory-only fields like CPA Economic Law."
body_hash: "045a8b7f"
connections:
  - type: idea
    slug: "knowledge-mastery-two-axis-model"  # auto
  - type: idea
    slug: "memorization-in-pipeline"  # auto
  - type: idea
    slug: "learning-dynamics"  # auto
  - type: idea
    slug: "teach-method-fixes"  # auto
  - type: idea
    slug: "hermeneutic-circle-learning"  # auto
  - type: idea
    slug: "learning-pipeline"  # auto
  - type: idea
    slug: "enumerative-as-scaffold-for-generative"  # auto
  - type: idea
    slug: "practice-as-learning-purpose"  # auto, review: 0.594
  - type: idea
    slug: "implicit-improvement-pattern"  # auto, review: 0.560
  - type: idea
    slug: "freedom-exploration-generator"  # auto, review: 0.553
  - type: idea
    slug: "structural-patience"  # auto, review: 0.549
  - type: idea
    slug: "goal-singularity"  # auto, review: 0.544
  - type: idea
    slug: "attention-as-bottleneck"  # auto, review: 0.528
  - type: idea
    slug: "success-interrogation-heuristic"  # auto, review: 0.526
  - type: idea
    slug: "pass-criteria-as-curriculum-design"  # auto, review: 0.525
  - type: idea
    slug: "knowledge-reconnection"  # auto, review: 0.522
  - type: idea
    slug: "data-structure-first-code-reading"  # auto, review: 0.518
  - type: idea
    slug: "speed-first-model-second-batch-tradeoff"  # auto, review: 0.502
  - type: idea
    slug: "attention-pointer-learning-model"  # auto, review: 0.500
  - type: idea
    slug: "practice-necessity-willingness-tradeoff"  # auto
  - type: idea
    slug: "teach-task-volume-scaling"  # auto
  - type: idea
    slug: "occupancy-pair-scheduling"  # auto, review: 0.556
---
# Learning Method v2

## Design Principles

The entire method is built on the **two-axis model of knowledge mastery** — concept (horizontal interaction density, c) and practice (vertical cross-filter binding, p) — and their interaction. Every design decision follows from: (1) c and p are independent but mutually catalytic, (2) c must precede p (bindings can only attach to an existing concept map), (3) both decay over time, with p decaying faster than c, and (4) c must be restored before p can be effectively recovered.

The method separates two concerns with different time scales: **learning cycles** (push forward, achieve mastery) and **maintenance** (resist decay, preserve what was mastered).

## Part 1: The Learning Cycle

### Rhythm

Rapid concept push → exam/project verification.

One cycle = a batch of lessons + one exam. The purpose of a cycle is **current mastery (c + p)**, not long-term retention — that's the maintenance phase's job.

### Course Types

#### Concept Lesson

| Dimension | Rule |
|-----------|------|
| **Goal** | Build horizontal interaction density (c) — understand the conceptual system |
| **Starting point** | Begin from the **lowest abstraction level** that can be fully understood (e.g., TCP is the lowest abstraction for FastAPI). Bottom-up sequencing avoids recursive questioning downward |
| **Content** | Concept maps, interaction diagrams, analogies, structural derivations — **no code, no operations** |
| **Pass bar** | Can locate every concept in the system, draw relationship maps, and perform derivations at the conceptual level — **concept-only, no practice involved** |

#### Practice Lesson

| Dimension | Rule |
|-----------|------|
| **Goal** | Build vertical cross-filter binding strength (p) |
| **Content** | **Hands-on tasks**: basic, simple, few in number; **Reading/observation tasks**: can be complex (e.g., tracing full code flow), no active writing required — this protects push speed |
| **Pass bar** | Can read and trace code/operation flows — does NOT require independent writing |
| **Constraint** | **No new concepts.** If practice reveals a new concept, that concept gets its own concept lesson first. **Exception**: distinguish between **blocking** concepts (cannot continue without understanding this) and **incidental** concepts (noticed but not needed for the current task). For blocking concepts, allow a ≤2-minute inline explanation to unblock the flow; if it takes longer, mark it as a pending concept lesson and continue. For incidental concepts, simply note them and move on. This preserves the c-before-p principle without killing flow — the constraint should gate, not interrupt.

#### Sequencing Rules

The ratio of concept to practice lessons varies by domain — no strict 1:1 alternation. Example:

```
Concept×3 → Practice×1 → Concept×2 → Practice×2 → Concept×3 → Practice×2
```

Two hard constraints:
1. **Concept always before practice** — horizontal interaction map must exist before vertical bindings can attach
2. **Practice introduces no new concepts** — only references material from completed concept lessons

> Concept/practice ratio has no fixed formula; adjust per domain. For some domains (e.g., CPA Economic Law), the practice dimension may not exist at all — knowledge has only the concept axis. The split is a domain-dependent tool, not a universal law.

### Exam/Project — Three-Tier Gradient

At the end of each cycle, a three-tier exam builds complete vertical bindings across all knowledge points:

| Tier | Structure | Binding strength | Description |
|------|-----------|-----------------|-------------|
| **Easy** | 5–8 small tasks | Lowest | Practice-lesson-level operations — can read, trace, make small modifications |
| **Medium** | 2–3 mid-sized tasks | Medium | Cross-module combination required, but paths are broadly clear |
| **Hard** | 1 large task | Strongest | Independent design, build from scratch |

Every tier covers **all knowledge points in the cycle** — not deepening block by block, but full breadth × increasing depth per tier.

> Reason for three tiers: OpenClaw experience — 8 lessons then directly to an ultimate challenge, with zero gradient between "can read" and "independent build," resulting in inability to even start.

## Part 2: Maintenance — Resisting Decay

After a cycle ends, both c and p decay over time (p may decay faster than c). Hierarchical domains like math have a natural advantage — new knowledge forces revisiting old knowledge, essentially free maintenance. Flat domains require active maintenance.

### Method

| Axis | Method | Description |
|------|--------|-------------|
| **Theory (c)** | Free recall → check against reference → revisit errors/gaps | Unprompted reconstruction of the entire concept system (draw maps / write relationships), then verify against concept maps or Reconnection Docs to catch errors and omissions. **Note on cost**: full free recall across all domains is heavy. The Ebbinghaus scheduler naturally limits scope — only domains flagged as "at risk" appear each week, not all domains. Additionally, a **lightweight variant** is available when cognitive load is high: instead of drawing the full concept map, pick one random concept as a seed and expand only its directly connected subgraph (3–5 concepts). Less breadth, same retrieval depth, lower burden. |
| **Practice (p)** | Structured testing with **variants** (easy tier) | Pull from the easy task bank and **modify one constraint or condition** — same underlying concept, but the solution path differs enough to require genuine re-derivation rather than rote recall. Example: the original task was "write a function that fetches 3 URLs concurrently"; the variant is "fetch 3 URLs concurrently, but if any one fails, cancel all remaining and return the error." The concept is the same, but the brain must re-engage the derivation path, not just replay a memorized answer. This creates desirable difficulty — the necessary condition for retrieval to strengthen storage. |

**Why variants are non-negotiable**: retrieval strength and storage strength are distinct. If the maintenance test uses tasks identical to the original exam, the brain takes a recognition shortcut — low retrieval effort, no storage strengthening, and the test produces false confidence. The goal of maintenance is to **resist decay**, not to confirm what was already mastered. A task that feels slightly unfamiliar is a task that is working.

Order: c first, then p. Free recall rebuilds the framework; structured testing holds the operational baseline. c must be restored before p can effectively recover, because p's vertical bindings depend on c's horizontal concept net — if the frame collapses, operational training is rebuilding on sand.

### Scheduling

Maintenance lives in `~/project-hub/mission-control/`. Every weekend, generate a **maintenance test** (HTML file) covering all active learning tracks. Content selection follows the **Ebbinghaus forgetting curve**: each knowledge point's last-contact time and estimated decay state determine whether it appears in this week's review.

The maintenance test has two sections:
1. **Free recall** — unprompted reconstruction across all active domains
2. **Structured tests** — easy-tier tasks targeting items the forgetting curve flags as at risk

> Domains are mixed in a single test (e.g., CPA Economic Law and Hermes Agent appear in the same paper). Cross-domain switching increases retrieval difficulty, which strengthens memory; it also mirrors real usage where knowledge from different domains is accessed together.

### Quantified Intuition — State Space Trajectory

The method can be understood through (c, p) coordinates (range 0–1). The following values are illustrative, not precise measurements:

| Phase | (c, p) | Notes |
|-------|--------|-------|
| Start | (0, 0) | Know nothing |
| Concept lessons done | (0.5, 0) | c built first, p stays at zero |
| Practice lessons done | (0.7, 0.3) | c grows further from practice feedback; p begins to establish |
| Easy exam done | (0.8, 0.6) | p gets first full-breadth binding |
| Medium exam done | (0.9, 0.8) | c and p approach peak together |
| Hard exam done | (1.0, 1.0) | Both axes at peak |
| 1 week idle | ≈ (0.7, 0.5) | p decays faster than c |
| 2 weeks idle | ≈ (0.5, 0.3) | Continued decay |
| c maintenance done | ≈ (0.8, 0.5) | Free recall restores c; p unchanged |
| p maintenance done | ≈ (0.9, 0.8) | Structured testing restores p |

Key patterns:
- **c always grows before p**: concept lessons never touch practice; p stays zero in the first phase. Frame first, bindings second.
- **Exams are the main driver of p**: practice lessons only push p to 0.3 (can read); the three-tier exam pushes p from 0.3 to 1.0 (can build independently).
- **p decays faster than c**: one week idle — c drops from 1.0 to 0.7 (frame still there), p drops from 1.0 to 0.5 (hands get rusty).
- **c maintenance before p maintenance**: p bindings attach to c's concept net. If the frame collapses, rebuilding p is futile. Free recall first (fast c repair), then structured tests (restore p on stable c).
- **Maintenance does not aim for 1.0**: the goal is stopping decay, not re-achieving peak. Getting back to 1.0 would require exam-level investment and is usually unnecessary.

### Domain Adaptation — The Framework Is a Tool, Not a Mold

Different disciplines have different positions on the theory-practice spectrum. The framework should bend to the domain, not the other way around.

| Domain type | Concept axis (c) | Practice axis (p) | Lesson structure | Exam adaptation | Maintenance |
|-------------|-----------------|-------------------|------------------|-----------------|-------------|
| **Theory + Practice** (e.g., Python, OpenClaw, LangGraph) | Full | Full | Concept + practice split as designed | Three-tier exam as designed | c + p maintenance as designed |
| **Theory-only** (e.g., CPA Economic Law) | Full | None or minimal | Concept lessons only. No practice lessons — there is no "operation" to bind to | Replace practice exam with **case explanation**: given a concrete case, explain it using the conceptual framework. Tiered by complexity (simple case → composite case → ambiguous/edge case) | c maintenance only. Structured testing replaced by case explanation at easy tier |
| **Practice-heavy** (e.g., a pure tool/lab skill) | Minimal | Full | Light concept framing, then heavy practice. Concept lessons are thin — just enough to locate the tools in a mental map | Exam unchanged (three-tier tasks), but concept check is integrated into task execution rather than a separate pass | p maintenance dominant. Free recall reduced to a quick tool-map sketch |

The CPA example is illustrative: "practice" for economic law means applying legal concepts to specific fact patterns — a form of operational binding, but not the same as writing code. Case explanation sits between pure concept derivation (concept lesson pass bar) and independent operation (code exam) — it tests whether c is dense enough to map onto real situations, without requiring p in the code-writing sense.

**Decision rule**: when starting a new domain, first ask — does this domain have a genuine operational layer? If no, collapse the practice axis. The two-axis model says p = 0 is a valid state; not every domain needs both dimensions.

## Part 3: Physical Separation

| Where | What | Time scale |
|-------|------|-----------|
| `teach-*` project directories | Learning cycles — lesson execution + exams | Per-cycle (days) |
| `~/project-hub/mission-control/` | Maintenance — weekly cross-domain review tests (HTML) | Weekly |

Learning cycles push forward; maintenance holds the line. Two locations, two time scales, two purposes.

## Open Questions

### 1. Bootstrapping the lowest abstraction level

When starting a new domain, the learner does not yet know what the lowest abstraction level is — you cannot identify TCP as the bottom of the FastAPI stack before learning about the stack.

**Resolved principle — "good-enough bottom + downward anchor"**: Do not chase the absolute bottom. Locate the lowest abstraction that is *sufficient for current work*. For FastAPI, that means HTTP protocol and route decorator principles — Socket is not needed to write business logic. Define an explicit stop-loss rule: **if the next abstraction layer down would take more than 30 minutes to explain, AND it does not affect the current task, stop descending. Mark it as a pending patch point and move on.** The pending patch is not ignored — if recursive questioning later reaches it, the anchor tells you where to go. It moves from "unknown unknown" to "known deferred."

The 30-minute threshold doubles as a diagnostic: if AI cannot explain the fundamentals of a layer within 30 minutes, that layer is likely not the true "good-enough bottom" — there may be an intermediate layer that should be surfaced first.

A pre-cycle reconnaissance step remains useful: spend 5–10 minutes having AI draw the domain's dependency hierarchy before the first concept lesson, then identify the good-enough bottom from the map.

### 2. Maintenance test generation

The method assumes weekly generation of a maintenance HTML test covering all active tracks, with content selected by the Ebbinghaus forgetting curve. No mechanism yet exists to: (a) extract knowledge points from each track, (b) track last-contact timestamps per point, (c) estimate current decay state, (d) generate free-recall prompts and structured test items, (e) compile everything into a single HTML file. Without automation or AI-assisted generation, the manual cost of producing the test each week exceeds the maintenance benefit. This is the most operationally blocking open question.

### 3. Feedback loop from maintenance to cycle design

Maintenance reveals information — "this concept's c consistently fails to recover past 0.8," "p on this module decays faster than average" — that should inform the design of future learning cycles. Currently the document treats cycles and maintenance as separate phases with no feedback channel. Resolving this requires designing both the data capture (what to record during maintenance) and the adjustment rules (how to modify a cycle based on that data).
