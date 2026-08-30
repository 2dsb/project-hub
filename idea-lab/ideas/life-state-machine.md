---
id: idea-20260830-life-state-machine
title: "Life-State Machine — Deterministic Dynamics with a Stipulable Controllable Boundary"
tags:
  - state-machine
  - modeling
  - agency
  - scope-selection
  - control
  - life-modeling
summary: "Life is modeled as a life-state machine with deterministic dynamics and a subjectively-stipulated controllable boundary. The formalism uses two arrows: → means determines, while -~-> marks the possibility of drawing a subjectively-controllable boundary at that step. Transitions take the form State(t) -~-> Action(t) and State(t), Action(t) → State(t+1), where ~ equals controllable(State(t)). The controllable function is freely stipulable and returns a scope separating what is subjectively controllable from what is uncontrollable. Everything outside that returned scope is determined or subjectively-uncontrollable random, so when no scope is returned the transition is fully determined."
body_hash: "2784b5ce"
connections:
  - type: idea
    slug: "agency-as-scope-selection"
  - type: idea
    slug: "life-state-machine-content"
importance: 2.94  # auto
---
# Life-State Machine

**One sentence**: Life is modeled as a state machine with two arrows — `→` (determines) and `-~->` (a step where a subjectively-controllable boundary may be drawn): `State(t) -~-> Action(t)` and `State(t), Action(t) → State(t+1)`, where `~ = controllable(State(t))` is a freely stipulable function returning a scope.

## The Formalism

- `→` means **determines**.
- `-~->` means the **possibility of drawing a subjectively-controllable boundary** exists at this step.

```
State(t) -~-> Action(t)
State(t), Action(t) → State(t+1)
```

where

```
~ = controllable(State(t))
```

`controllable` is a **subjectively-stipulated** function: it takes the current state and returns a **scope** — what is subjectively controllable and what is subjectively uncontrollable. The function can be set **arbitrarily**.

## Example

```
controllable(S) = "thinking"  if  S.is_deciding == 1
                 else None
```

When `is_deciding == 1`, thinking falls inside the controllable scope; otherwise the scope is empty and the transition is fully determined.

## Note

Everything outside the returned scope is determined (+ subjectively-uncontrollable random variables).
