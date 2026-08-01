---
id: "idea-20260719-decision-model-as-next-domain-model"
title: "Decision Model as Next Non-Specialist Domain Model"
importance: 2
tags:
  - decision-making
  - modeling
  - system-architecture
  - meta-cognition
summary: "The next non-specialist domain model to develop is a decision model, which determines what action"
connections:
  - type: idea
    slug: "timeline-based-project-structure"
  - type: idea
    slug: "leverage-existing-vs-build-from-scratch"
  - type: idea
    slug: "precision-fuzziness-tradeoff"
  - type: idea
    slug: "strategy-three-component-model"  # review: 0.530
---
# Decision Model as Next Non-Specialist Domain Model

## The intention

The next "non-specialist domain" model to develop — alongside and potentially merging with [[timeline-based-project-structure]] — is a **decision model**.

## Division of labor

| Model | Question it answers | Status |
|-------|-------------------|--------|
| Timeline-based project structure | *How* do projects evolve over time? What state are they in? | Active development (M, A, P, oscillator, reconnection docs) |
| Decision model | *What* should I do right now, given the state of all projects? | Not yet started |

The timeline model describes the landscape. The decision model navigates it. The timeline model tells you that P is low and two projects have high tension. The decision model tells you whether to rest, exercise, switch projects, or push through.

## Candidate factors for the decision model

Some of today's ideas are naturally factors in this eventual model:

- **Leverage Factor (L)**: find existing solutions vs. build from scratch ([[leverage-existing-vs-build-from-scratch]])
- **Precision vs. Fuzziness**: which mode does the current task demand? ([[precision-fuzziness-tradeoff]])
- **Pass criteria clarity**: is the success condition well-defined? ([[pass-criteria-as-curriculum-design]])
- **Practice proximity**: how soon will this be applied? ([[practice-as-learning-purpose]])

Plus factors already implicit in the timeline model:
- P adequacy (can I even work right now?)
- Tension_i (expected value gap of completing project i)
- Willingness state (continuity fatigue vs. milestone gravity)
- Oscillator phase (am I in A or B?)

## Possible merger

The two models may eventually merge — the decision model is the *controller* that reads the timeline model's state and outputs actions. This is the standard sense-act loop: sense = timeline model (what's the state?), act = decision model (what do I do about it?).

## Status

Intention only. No design work yet. Will find time later.
