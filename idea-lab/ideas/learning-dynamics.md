---
id: idea-20260730-learning-dynamics
title: "Learning Dynamics — Forces Governing Knowledge Acquisition"
tags:
  - meta-cognition
  - learning
  - dynamics
  - optimization
  - actionable
summary: "The note extends the two-axis model of knowledge mastery, where objects have horizontal interaction density c and vertical cross-filter binding p, by defining forces that drive acquisition, drag, and phase transitions. Acquisition forces like exposure, deliberate mapping, and execution push c and p upward, while drag forces such as decay, interference, and attention competition pull them downward. Phase transitions to higher recursion levels are triggered by saturation, deliberate comparison, or external perturbation. The framework raises open questions about optimal sequencing, decay curves, transfer efficiency, and individual parameters, and it integrates with the /teach method and the MAP model’s M and Willingness. Explicit per-track tracking of c and p is proposed as a next step."
body_hash: "e497d141"
importance: 3.76  # auto
connections:
  - type: idea
    slug: knowledge-mastery-two-axis-model
  - type: idea
    slug: interaction-as-dictionary
  - type: idea
    slug: teach-method-fixes
  - type: idea
    slug: "implicit-improvement-pattern"  # auto
  - type: idea
    slug: "freedom-exploration-generator"  # auto
  - type: idea
    slug: "memorization-in-pipeline"  # auto
  - type: idea
    slug: "attention-pointer-learning-model"  # auto
  - type: idea
    slug: "speed-first-model-second-batch-tradeoff"  # review: 0.599
  - type: idea
    slug: "transfer-high-leverage"  # review: 0.599
  - type: idea
    slug: "learning-pipeline"  # review: 0.545
  - type: idea
    slug: "structural-patience"  # review: 0.540
  - type: idea
    slug: "knowledge-transfer-fidelity"  # review: 0.527
  - type: idea
    slug: "locate-first-model-last"  # review: 0.502
  - type: idea
    slug: "attention-as-bottleneck"  # auto, review: 0.549
  - type: idea
    slug: "practice-as-learning-purpose"  # auto, review: 0.515
  - type: idea
    slug: "goal-singularity"  # auto, review: 0.513
  - type: idea
    slug: "learning-method-v2"  # auto
  - type: idea
    slug: "hermeneutic-circle-learning"  # auto, review: 0.570
  - type: idea
    slug: "practice-necessity-willingness-tradeoff"  # auto, review: 0.572
  - type: idea
    slug: "occupancy-pair-scheduling"  # auto, review: 0.516
  - type: idea
    slug: "teach-task-volume-scaling"  # auto, review: 0.508
---
# Learning Dynamics — Forces Governing Knowledge Acquisition

**One sentence**: If the two-axis model describes the state space of knowledge mastery, learning dynamics describes the forces — what accelerates acquisition, what creates drag, what triggers phase transitions between levels, and what determines efficiency.

## State Space (from two-axis model)

An object X in a given filter has state (c, p) where:
- c ∈ [0, 1]: horizontal interaction density (name-only → dense interaction map)
- p ∈ [0, 1]: vertical cross-filter binding strength (unbound → memory-bound)

Plus level L ∈ {0, 1, 2, ...}: which recursion level the object sits at.

## Candidate Forces

### Acquisition forces (push c, p upward)

| Force | Acts on | Mechanism |
|---|---|---|
| **Exposure** | c | New interaction patterns discovered through lesson content, reading, or exploration. Rate limited by attention bandwidth. |
| **Deliberate mapping** | c | Explicitly drawing concept maps, enumerating interactions, writing explanations. More efficient than passive exposure but more cognitively expensive. |
| **Execution** | p | Writing code, solving problems, building projects. Each execution attempt strengthens vertical bindings. |
| **Cross-domain transfer** | c (new filter) | Recognizing that a pattern from domain A applies in domain B. Opens a new filter for an existing object. |
| **Teaching/explaining** | c, p | Articulating X to someone else forces you to fill gaps in both horizontal and vertical maps. |

### Drag forces (pull c, p downward)

| Force | Acts on | Mechanism |
|---|---|---|
| **Decay** | c, p | Interaction patterns fade if not accessed. Rate likely domain-dependent and individually variable. |
| **Interference** | c | Similar-but-different patterns (e.g., SQLAlchemy vs Django ORM) create false horizontal interactions that must be unlearned. |
| **Complexity ceiling** | c | For structural domains, the interaction network grows super-linearly. Beyond some density, new interactions are harder to discover because they depend on existing ones. |
| **Attention competition** | c, p | Learning X means not learning Y. The opportunity cost is real — attention is zero-sum. |

### Phase transition triggers (jump L → L+1)

| Trigger | Mechanism |
|---|---|
| **Saturation** | c and p are sufficiently high across enough Level L objects that stable cross-object patterns become visible. |
| **Deliberate comparison** | Actively comparing Level L objects (not just accumulating them). This is the "deliberate thinking" you identified — it doesn't happen automatically. |
| **External perturbation** | Someone points out the pattern to you, or a conversation (like this one) forces articulation. |

## Key Questions (Open)

1. **Optimal sequencing**: Given (c, p) for object X, what's the marginal return of one more concept lesson vs. one more practice lesson? Is there an optimal ratio that changes with (c, p)?

2. **Decay curves**: How fast do c and p decay without reinforcement? Is decay faster for p than c? Does decay rate decrease as (c, p) approach 1?

3. **Transfer efficiency**: When does learning X accelerate learning Y? What properties of X and Y predict transfer — shared horizontal patterns? Shared vertical bindings? Proximity in filter space?

4. **Saturation detection**: How do you know when c is "dense enough" to start practice? The current heuristic is "when you stop asking recursive questions" — can this be formalized?

5. **Individual parameters**: How much do acquisition rates, decay rates, and transfer coefficients vary between individuals? Between domains for the same individual?

6. **Optimal cycle length**: The current method uses "rapid concept push → one big exam." Is there an optimal concept-push length? Too short → insufficient density for the exam to be productive. Too long → decay on early concepts before the exam starts.

## Relationship to /teach Method

The /teach method already implicitly optimizes some of these forces:
- **Maximizes exposure rate** — AI-generated custom lessons are higher bandwidth than textbooks or video
- **Enforces deliberate mapping** — passing criteria require explaining in your own words
- **Concentrates execution** — one big exam rather than distributed exercises (all-or-nothing vertical binding push)
- **Minimizes interference** — custom curriculum avoids irrelevant content

What it doesn't yet optimize:
- **Decay management** — no spaced repetition, no retrieval practice schedule
- **Cross-domain transfer detection** — the AI can't observe patterns across tracks (only the learner can)
- **Saturation detection** — currently heuristic ("when recursive questions stop")
- **Phase transition triggering** — deliberate comparison is left to the learner's initiative

## Practical Next Steps

1. **Track (c, p) explicitly** per track. Current "progress %" conflates the two axes. A simple 2-number state per track would make dynamics visible.
2. **Experiment with retrieval practice scheduling** — does revisiting a concept lesson N days later reduce decay?
3. **Formalize saturation detection** — at what point in a concept push does the marginal return per lesson drop?

## Open Integration: MAP + Willingness ↔ Two-Axis Model

From [[timeline-based-project-structure]], M (Memory) describes "mastery of specific content within the project — at every level, from highest architecture to lowest detail." This is precisely the aggregate of all (c, p) states across all objects in the project:

- M is the **coarse-grained, single-number summary** per project
- (c, p) is the **fine-grained, per-object decomposition** within M

When M decays during a gap (time away from project), individual c and p values decay — and the two may decay at different rates. p (vertical bindings) might decay faster than c (horizontal concept maps), or vice versa.

**Willingness** — the force driving state transitions (continuity fatigue vs. milestone gravity) — may also decompose:

- Does rapid c advancement drain willingness differently than rapid p advancement?
- Is continuity fatigue driven by time-on-project or by (c, p) advancement magnitude?
- Can tracking c and p separately predict which gap type is approaching?

**Unresolved.** The two frameworks were developed independently (MAP in June, two-axis model in July). Their integration is an open problem.
