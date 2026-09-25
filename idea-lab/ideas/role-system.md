---
id: idea-20260925-role-system
title: "The Role System — Roles Classify Action State; One at a Time, Switched by a Marker"
tags:
  - state-machine
  - life-modeling
  - roles
  - attention
  - habits
  - mental-clutter
  - methodology
summary: "A role is a classification of action state—learner, builder, planner, manager—and at any moment full commitment to exactly one role is best because roles compete for the same mental resources, so doing two at once crowds out both and leaves each action outside the feasible set F(S) from action-gate. Role matching means the current action lies in F(S) for the current state. Switching roles requires a deliberate, discrete, observable, cheap marker, which acts as the controllable boundary drawn in life-state-machine and navigates feasibility rather than forcing willpower. The open design problem is the right role set, proposed as the maximal partition of actions into mutually-interfering classes."
body_hash: "7c0186b4"
connections:
  - type: idea
    slug: "action-gate"  # auto
  - type: idea
    slug: "life-state-machine-content"  # auto
  - type: idea
    slug: "life-state-machine"  # auto
  - type: idea
    slug: "activity-cost-benefit"  # auto, review: 0.595
  - type: idea
    slug: "idle-as-unstable-state"  # auto, review: 0.593
  - type: idea
    slug: "attention-as-bottleneck"  # auto, review: 0.565
  - type: idea
    slug: "integrating-fragmented-life-strategies"  # auto, review: 0.542
  - type: idea
    slug: "mental-clutter-degree"  # auto, review: 0.534
  - type: idea
    slug: "fundamental-model-of-learning"  # auto, review: 0.510
  - type: idea
    slug: "pattern-pipeline"  # auto, review: 0.506
importance: 1.96  # auto
---
# The Role System — Roles Classify Action State; One at a Time, Switched by a Marker

**One sentence**: A **role** is a classification of action state — *learner*, *builder*, *planner*, *manager*, and others — and at any moment fully committing to exactly one role is the best available choice, because two at once crowd out the same mental resources and both are done badly; the switch between roles is performed by a **deliberate, discrete marker** (a gesture, for example).

## The Roles

*Learner*, *builder*, *planner*, *manager*, and others — the list is explicitly **not** closed. What matters for now is the shape, not the membership.

## Claim 1 · One Role at a Time

For this user, at any given moment, **full commitment to a single role is the best choice**.

The argument is the failure case: doing two roles at once — *learner* and *planner*, say — means mental resources are **crowded out**, and the result is that **both are done badly**.

This is not a preference about style. It is a claim that roles **compete for one resource**, and that the competition is severe enough that splitting is strictly worse than sequencing.

## Claim 2 · A Role Is a Classification of Action State

Two linked statements:

- **A role classifies action state.** It is a partition of what you are doing, not a mood or a job title.
- **Role matching is the unity of *action state* and *mental state*.** You are "in role" when what you are doing and the state you are doing it in are the same thing.

The existing formalism makes this precise. [[action-gate]] holds that every interaction `A` has a **startup requirement** `req(A)` on internal state, and that the feasible set `F(S)` contains only those interactions the current state actually satisfies — free will selects *within* that menu, never over actions directly.

Read through that:

> **Role matching = the current action lies in `F(S)` for the current state.**

Doing learner work while in a manager state is not a discipline failure. It is an action that is **not in the feasible set**, and [[action-gate]] already establishes what happens then: willing an infeasible action is empty, and trying to force it fails.

That is why doing two roles is worse than doing them in sequence. Interleaving them means the state satisfies neither role's requirement, so **both actions sit outside `F(S)`** for the whole stretch.

## Claim 3 · The Switch Is a Deliberate Marker

The role system is proposed as a **habit to be cultivated**, and the mechanism is a deliberate marker that switches and installs you into a role:

1. Make the marker → switch to **learner** → commit to studying, and nothing else.
2. Some time later, make the marker again → switch to **manager** → check information, email, messages, arrange things.

The marker is the **boundary between roles**.

A gesture is offered as an example, explicitly *"just an analogy"* — which is the useful framing, because it turns the gesture into a **specification**. What the mechanism needs is a marker that is:

| Property | Why it's required |
|---|---|
| **Deliberate** | You choose it — this is where control is exercised |
| **Discrete** | It happened or it didn't; no ambiguity about which role you're in |
| **Observable** | You can *verify* the switch, unlike an internal intention |
| **Cheap** | It costs nothing, so it can be used many times a day |

Any marker meeting those four works. The gesture is one instance.

In [[life-state-machine]] terms, the marker is what **draws the controllable boundary** at that step — the practical realization of the `-~->` arrow, which marks "the possibility of drawing a subjectively-controllable boundary exists here." The role system is what that arrow looks like in daily operation.

And note what the marker is *not*: it is not willpower applied to the role. [[action-gate]]'s practical lever is **navigation of feasibility** — act on the state through feasible steps until the desired action opens, rather than forcing it. The marker is exactly such a step: an action on the *state*, taken so that the role's `F(S)` opens.

## The Design Question: What Is the Right Role Set?

The role list is open, so its **membership is the actual design problem**, and no principle for it has been stated.

A principle is available from the user's own criterion. Roles should not be defined by semantic category ("what kind of work is this?") but by **mutual interference** ("which actions degrade each other when done together?"). The user's own example is the evidence: learner and planner are in different roles *because* doing both at once ruins both.

That suggests: **the role set is the maximal partition of actions into mutually-interfering classes.**

Its two failure modes are symmetric:

- **Too few roles** — classes that conflict get merged, and the mixing the system exists to prevent becomes unavoidable.
- **Too many roles** — each switch costs something, and the switching overhead eats the benefit.

## Open Questions

- **Does this contradict [[async-work-mode]]?** That idea argues for overlapping tasks and filling wait windows instead of idling; this one argues against running two things at once. They cannot both hold unconditionally. A likely resolution: switching is cheap when **deliberate and role-aligned** (filling a wait with more work *from the same role*) and expensive when it mixes roles — which would also answer async-work-mode's own open question about gap-fillers eating the time gain. Worth settling, since both ideas are live.
- **How is a role's startup requirement set?** [[action-gate]] gives every action a `req(A)`. Does each role need its own state precondition, and can the marker actually *establish* that state or only signal intent to?
- **What is the switching cost, quantitatively?** Same problem as [[activity-cost-benefit]]'s relaxation time: without a number, "one at a time is better" can't be checked against the cases where one-at-a-time is clearly worse.
- **Is the marker learned, or does it need to be arbitrary?** A cultural gesture carries meaning that may help or interfere. Whether the marker's content matters, or only its consistency, is untested.
- **What happens to unassigned time?** Roles cover action, but a stretch with no role is exactly the unstable state described in [[idle-as-unstable-state]].

## Related

- [[life-state-machine]] — supplies the formalism; the marker is a drawn `-~->` boundary
- [[action-gate]] — the key link: role matching = the action lies in `F(S)`; role-mixing = both actions fall outside it
- [[mental-clutter-degree]] — multitasking raises 混乱度, which is *why* two roles degrade each other rather than merely slowing things down
- [[attention-as-bottleneck]] — attention is single-threaded; the role system is that fact made operational
- [[agency-as-scope-selection]] — agency as choosing within the feasible scope, which is what the marker navigates
- [[activity-cost-benefit]] — the same state-cost logic applied to choosing activities rather than to roles
- [[idle-as-unstable-state]] — the boundary case: no role assigned
