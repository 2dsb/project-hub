---
id: idea-20260830-life-state-machine-content
title: "Life-State Machine Content — Controllable, State, and Dynamics"
tags:
  - state-machine
  - modeling
  - agency
  - scope-selection
  - life-modeling
  - energy-management
  - dynamics
  - control
summary: "# Life-State Machine Content  **One sentence**: This file fills in the *content* of the life-state-machine formalism: `controllable` is fixed to \"thinking while deciding, nothing otherwise\"; `State(t)"
body_hash: "e826dd24"
connections:
  - type: idea
    slug: "life-state-machine"
  - type: idea
    slug: "agency-as-scope-selection"
importance: 2.94  # auto
---
# Life-State Machine Content

**One sentence**: This file fills in the *content* of the life-state-machine formalism: `controllable` is fixed to "thinking while deciding, nothing otherwise"; `State(t)` is a finite nested-JSON triple {internal, external, interaction} with provisional components; and the dynamics are the known evolution laws of M, P, and willingness plus the segment/oscillator structure — all provisional, extended as new components and mechanisms are encountered.

## Relationship to the Formalism

Builds on **[[life-state-machine]]** (the two-arrow formalism `State(t) -~-> Action(t); State(t), Action(t) → State(t+1)`, with `~ = controllable(State(t))`) and the philosophy in **[[agency-as-scope-selection]]**. This file concretizes the abstract formalism: what the scope is, what the state contains, how the dynamics run.

## 1. controllable — Fixed

```
controllable(S) = "thinking"  if  S.is_deciding == 1
                 else None
```

**Rationale**: Only while making a decision does the agent treat itself as subjectively agentic (主观能动的). Everything else — whether thinking or acting — is execution: determined (+ subjectively-uncontrollable random variables). Agency lives exactly in the deliberation interval and nowhere else.

## 2. State(t) — Components and Representation

**Representation**: JSON — a finite nested list/dict, truncated to what is human-observable (attention filter) and influential.

**Components** (provisional — new ones added as encountered):

```
State(t) = {
  internal: {
    M(知识理解),               // knowledge understanding — decays in gaps, deepens with engagement
    P(体力/精力),               // physical capacity — the shared resource gating cognitive work
    willingness,                // the force driving transitions (continuity fatigue / milestone gravity)
    is_deciding,                // deliberation flag — read by controllable
    当前情绪/状态                // current mood / state
  },
  external: {
    A(工件),                    // artifacts: files, notes, tools, data
    环境状态                     // environment state
  },
  interaction: {
    当前时间段类型(高/低占用),    // current segment type: high- or low-occupancy
    最近行为链,                  // recent behavior chain
    进行中的交互                  // ongoing interactions
  }
}
```

## 3. Dynamics — State(t), Action(t) → State(t+1)

Candidate mechanisms (provisional):

- **M** — decays during gaps, deepens during engagement.
- **P** — `P_next = P_baseline + exercise_short_term_boost(yesterday) − sleep_quality_penalty(cognitive_arousal_before_bed)`; baseline evolves slowly with cumulative exercise vs. inactivity.
- **Willingness** — continuity fatigue pushes away from a project; milestone gravity pulls toward completion. The A⇄B oscillator: A→B via willingness fatigue / P depletion / capability blockage; B→A via leisure satiation / external (social) gravity.
- **Segments** — the day is a sequence of time blocks; high→low occupancy pairing enables consolidation (reflection) and attention-residue release.
- **Action (broad sense)** — includes mental actions, decisions, and physical actions; anything the agent does.

## 4. The Value — A Unified Language for Life's Causal Chains

The framework's real value is that nearly all of life's scattered empirical knowledge — influence chains, causal chains, non-structural experience — can be described in this one language. Every piece of knowledge falls into exactly one of two slots:

1. **A State component** — what the system is like (current condition).
2. **A dynamics mechanism** — how the system changes (a transition law).

Examples:

- "Slept too late last night → tired today" = dynamics (the P equation's `sleep_quality_penalty`).
- "Drink more water" — forces a classification: a State component (hydration) that feeds a mechanism (P maintenance), or a mechanism itself. The forced classification exposes the assumption behind each piece of advice.
- "A switch from state A to state B" = dynamics (a transition).

Once life-knowledge is in this language, life becomes *analyzable*: components and mechanisms can be computed, simulated, and optimized — strategy is the design activity on top of this language.

**A self-referential note**: when designing strategies, one assumes subjective agency — the meta-level act of choosing the scope (`controllable`) itself presupposes the agency it defines. The model cannot prove agency from within; it presupposes it, including at the meta-level. This mirrors the self-referential structure `T = Φ(T)` (GENERATIVE-CORE) and keeps the scope-selection view self-consistent: the deepest choice presupposes what it defines.

## 5. The Prescriptive Layer — Objective and Strategy

The framework is *descriptive*: it stores life-knowledge as components and rules. To **design and optimize** strategy, a normative layer is added:

```
Goal:  maximize J(State(t))  for future t
```

Strategy has **four degrees of freedom** — the levers from [[strategy-three-component-model]] — the ways one acts to improve strategy:

| # | Lever | What it means here |
|---|---|---|
| 1 | Clarify J | refine the objective — what you are actually optimizing for |
| 2 | Modify controllable | redraw the scope — because controllable is subjectively determined, under different States you may declare different components of State subjectively controllable |
| 3 | Clarify State & Dynamics | model the current state and its transition laws more accurately |
| 4 | Change policy | under controllable's freedom constraint, switch the concrete choice rule |

The levers co-evolve: executing a policy (4) yields new observations → clarifies State/Dynamics (3) → sharpens the policy's design. The whole loop — **maximize future J by simultaneously clarifying J, redrawing controllable, modeling State/Dynamics, and adjusting policy** — is the meta-strategy.

## 6. How to Extend — From Observation to Component and Rule

The framework grows by observation. Three rules keep the growth principled:

**6.1 Admission criterion.** A candidate State component or Dynamics rule enters only if it is:

- **Observable** — reachable by the human attention filter ([[interaction-as-dictionary]] §5);
- **Influential** — it actually changes the trajectory of the dynamics;
- **Stable** — consistent across repeated observation, not a one-off.

**6.2 Test loop.** Propose a candidate → record observations → compare → adopt or drop. Enrichment stays self-correcting rather than ad hoc.

**6.3 Format flexibility — natural language is fine.** Not every rule must be translated into strict formal form; natural language suffices when it does. Example: add "did I sleep well last night" into `State(P)`, and store "sleeping late likely causes tomorrow-morning drowsiness" as a Dynamics rule. The formats of `State(t)` and `Dynamics(t)` need not be strict — **comprehensibility is the only requirement**. Formalization is a tool, not an obligation.

## To Be Extended

- A concrete `J(State)` — how to actually define the objective in practice.
- Formal transition rules for each component (natural-language rules are now explicitly allowed).
- Whether physical actions fall inside any reachable scope.
