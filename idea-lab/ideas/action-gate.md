---
id: idea-20260906-action-gate
title: "The Action Gate — Free Will Ranges Only Over State-Feasible Actions"
tags:
  - state-machine
  - life-modeling
  - agency
  - free-will
  - scope-selection
  - control
  - mental-clutter
  - dynamics
summary: "The Action Gate holds that free will selects only within a state-determined feasible set, never over actions directly. Each interaction A has a startup requirement req(A) on internal state; the feasible set F(S) contains only interactions whose requirements the current state satisfies. Agency is scope selection within that menu, so willing an infeasible action like deep work in a degraded state is empty. The asymmetric-gate trap means degraded states collapse F(S) toward entertainment and other state-worsening defaults, leaving no feasible state-improving exit. The practical lever is navigation of feasibility: act on the state through feasible steps until the desired action opens, rather than trying to force it by will."
body_hash: "2e8628f1"
connections:
  - type: idea
    slug: "agency-as-scope-selection"
  - type: idea
    slug: "life-state-machine"
  - type: idea
    slug: "mental-clutter-degree"
  - type: idea
    slug: "idle-as-unstable-state"
  - type: idea
    slug: "life-state-machine-content"  # auto
importance: -1
---
# The Action Gate (门控)

**One sentence**: Switching from one interaction with the world to another is gated — for any interaction A, if the internal state does not satisfy A's startup requirement, then even while the agent is *freely deciding*, the option "next, do A" does not exist. Free will selects within the feasible menu; the state determines the menu.

## 1. The Mechanism — Every Interaction Has a Startup Requirement

The observation behind it: whether a person can switch their current interaction-state with the outside world usually depends on the person's internal state — the phenomenon called "startup cost" in [[mental-clutter-degree]]. That is not an annoyance to push through; it is a dynamics mechanism of the state machine. Formalize:

- Each interaction A carries a requirement `req(A)` on the internal state — e.g., meaningful work wants low C (混乱度) and high P; sleep wants mid-range C; entertainment has essentially no requirement.
- The **feasible set** at a state is `F(S) = { A : S.internal satisfies req(A) }`.
- Dynamics rule: the transition "next, do A" is possible **only if** A ∈ F(S).

## 2. The Claim — Free Will Ranges Over the Menu, Not Over Actions

The sharp consequence (the valuable part), stated as the gate principle:

> For an interaction A between person and environment: if the person's internal state does not satisfy A's requirement, then when the person exercises free will in deciding, the option "next step: do A" does **not** exist.

So agency never conjures actions from nothing. The will selects only among the options the state has left open:

- The **state determines the menu** — `F(S)` is fixed by internal state, a determined fact.
- **Agency** (the stipulated `controllable`, per [[agency-as-scope-selection]]) decides *which menu item to take*.
- Willing an infeasible action is vacuous — "I freely decide to start deep work" is empty if deep work ∉ F(S). The failure is not a failure of will; it is a fact about the menu.

This makes the determinism/agency split precise once more: not "state determines action," but *state determines the option set; the agent's choice determines which option is realized*. The gate is the determined part of every choice.

## 3. The Asymmetric-Gate Trap

Gates are not symmetric, and the asymmetry is what makes degraded states sticky:

| Action type | req(A) | Feasibility in a degraded state (C↑, P↓) |
|---|---|---|
| Entertainment (phone, games) | ~none | Always open — the default filler |
| Meaningful / growth work | low C, high P | Usually closed |
| Sleep | mid-range C | Window-dependent |

When the internal state degrades, `F(S)` collapses toward exactly the actions that degrade it further — the menu itself pushes you toward what worsens the state. Often **no state-improving action is feasible at all**, so the only exit is to wait until the state passively improves (rest, time). This is the idle-wait trap of [[idle-as-unstable-state]]: with the tether shrinking F(S), every feasible exit degrades C.

A corollary for judgment: "bad choices" are usually not made at the instant of choice. The menu was already narrowed by the state — which was itself shaped by earlier (gated, feasible) choices. Accountability lives up the chain of states, not at the single moment of deciding.

## 4. The Practical Lever — Operate on the State, Not on the Will

If A ∉ F(S), willpower cannot help. The honest two-step strategy:

1. **Check the menu before willing.** If A is gated closed, stop trying to decide A.
2. **Act on state.** Pick a feasible B whose dynamics move the internal state so that `req(A)` becomes satisfied — then A opens.

Strategy becomes *navigation of feasibility*: a chain of feasible actions that unlocks the next action. This gives formal justification to "preparation" and "putting yourself in a state to act," and reframes the goal from "decide to work" to "arrange the state in which work is an option." (Compare the strategy levers in [[life-state-machine-content]].)

## 5. Relation to Neighboring Ideas

- **Refines [[agency-as-scope-selection]]**: freedom was stipulated via the `controllable` scope; here it is additionally *bounded* — `controllable` decides which steps you steer, `F(S)` decides which next steps exist. Agency is selection within the intersection.
- **Lives in [[life-state-machine]]**: a new dynamics constraint — the `-~->` (controllable choice) arrow ranges only over the feasible set.
- **Instantiated by [[mental-clutter-degree]]**: that idea supplies the concrete `req(A)` (startup gating) and the asymmetry that makes entertainment the low-effort default.
- **Demonstrated by [[idle-as-unstable-state]]**: the tether shrinks F(S); the two feasible exits both degrade state.

## 6. Open Questions

- **Graded or binary gate?** Startup *cost* suggests feasibility is graded — a partially-degraded state makes A possible but costly/slow — with the hard gate an idealization at the extremes. Where is the threshold?
- **The meta-gate.** Is *entering deliberation* (`is_deciding = 1`) itself gated — feasible only under some states? If C is too high, can one even deliberate, or does the mind stay on autopilot? (Ties to whether C is directly steerable — an open question in [[mental-clutter-degree]].)
- **Is req internal-only?** The gate was stated on internal state. But external structure also sets startup cost (friction). Is "reduce the friction to make A feasible" a second, independent lever — an *external* gate?
