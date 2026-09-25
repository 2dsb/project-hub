---
id: idea-20260826-knowledge-map-format
title: Knowledge Map Format (MAP.md)
tags:
  - knowledge-map
  - teach-method
  - format-design
  - learning
summary: "MAP.md is a workspace-root file serving as the single source of truth for a constructed, provisional, revisable knowledge map. It records nodes at every level, dependency edges, the 0/1 state of every minimal leaf node, anchors marking good-enough bottoms, and the single-thread open flip. The format uses frozen node ids, needs prerequisites, and learning-record citations such as LR-NNNN to evidence every checked leaf. Its state machine enforces one lesson at a time through IDLE, AWAITING-DEMONSTRATION, and AWAITING-RESOLUTION, with reconstruction as unit operation a. Reconstruction may change structure but preserves authored check states and node ids, and the only allowed reversal is a traceable re-zero with a superseding learning record."
body_hash: "05fbb1cc"
connections:
  - type: idea
    slug: "fundamental-model-of-learning"  # auto
  - type: idea
    slug: "goal-predicate-f"  # auto, review: 0.562
  - type: idea
    slug: "knowledge-reconnection"  # auto, review: 0.544
  - type: idea
    slug: "learning-method-v2"  # auto, review: 0.537
  - type: idea
    slug: "pattern-pipeline"  # auto, review: 0.526
  - type: idea
    slug: "knowledge-mastery-two-axis-model"  # auto, review: 0.518
  - type: idea
    slug: "teach-application-scope"  # auto, review: 0.515
  - type: idea
    slug: "plugin-architecture-vs-defaults"  # auto, review: 0.505
  - type: idea
    slug: "teach-method-fixes"  # auto, review: 0.504
  - type: idea
    slug: "single-advancement-method-first-pass"  # auto, review: 0.503
  - type: idea
    slug: "letters-to-future-self"  # auto, review: 0.530
  - type: idea
    slug: "learning-cycle-microstructure"  # auto, review: 0.585
importance: 2.97  # auto
---
# Knowledge Map Format (MAP.md)

From the `/teach` optimization attempt (2026-08-24). The optimization as a whole failed and was rolled back, but this design — the single source of truth for the constructed knowledge map — was judged excellent and is preserved here in full.

# MAP.md Format

`MAP.md` lives at the workspace root. It is the single source of truth for the current constructed knowledge map: nodes at every level, dependency edges, the 0/1 state of every minimal node, and the single-thread focus. The map is **constructed, provisional, and revised** — it is never a claim about the "real" structure of the domain, only about the structure we can build from the information sources we have.

## File structure

```md
# MAP — {Topic}

Status: IDLE | AWAITING-DEMONSTRATION | AWAITING-RESOLUTION
Open flip: {node-id[, node-id…]} | none
f: see MISSION.md §Goal predicate f · f-critical: {id, id, ...}
progress: leaves X/Y ✓ · anchors K · f decidable: yes/no (f-critical M/N mapped)
v{n} · constructed {date} from {source} (provisional)

## {root}
  {node}
    {node}
  {node}  [anchor]

## {root}
  ...

## History
- v{n} {date} · via {source} · changed: {what} · preserved: {what}
```

## Header lines

| Line | Content |
|---|---|
| `Status:` | `IDLE` — no flip in progress · `AWAITING-DEMONSTRATION` — the open flip's lesson was produced, user demonstration pending · `AWAITING-RESOLUTION` — the open flip's demonstration failed, still on the same node. |
| `Open flip:` | The node, or small set of tightly-related nodes, of the current lesson — the current single thread — or `none`. Exactly one open flip at a time. |
| `f:` | Reference only — no clause text here. `f-critical: {ids}` is the minimal node set whose states decide f (the "construct until f is decidable and true" target). When f is fuzzy or `endless`, write `f-critical: {}` and `f decidable: no` — there is no target set yet. When an arbiter result is pending, add `f awaiting: {arbiter}`. |
| `progress:` | `leaves X/Y ✓` — X of Y leaves (including `[anchor]` leaves) are 1. `anchors K` — number of anchor leaves. `f decidable: yes/no` — every f-critical node exists in the map **AND every f clause has a check procedure**; `(f-critical M/N mapped)` when the nodes all exist. An empty `f-critical: {}` is **not** vacuously decidable — it means `f decidable: no` until f clarifies. |
| `v{n}` | Version, bumped on every reconstruction. The stamp records construction source and marks the map provisional. |

**Deriving `f-critical`:** from MISSION's f clauses, take the union of every clause's `nodes:` references, expanded down to leaves (arbiter clauses contribute nothing); write the set in the header, and refresh it whenever f changes.

## Node syntax

```
{indent} {state?} {id}: {label} [anchor] [needs: id, id] [(LR-NNNN)] [(prior)]
```

- **Indent** — two spaces per level. A node with deeper-indented children is a **parent** and carries **no state token**; its state is derived from its leaf descendants (a parent is 1 iff all its leaf descendants are 1).
- **State** — `0` or `✓`, authored **only on leaves** (childless nodes, including `[anchor]` leaves). A `✓` must carry `(LR-NNNN)` — its evidence record; prior knowledge files one too (with the `Node:` line), and the `(prior)` tag is an optional map-side flag that does **not** replace the record. A bare `✓` is a red flag.
- **id** — a frozen slug (`cli.args`, `lang.ownership`). Created once, **never rewritten on re-parenting**; the prefix is a birth-time name, not the current path. Ids are the cross-link keys for learning records and lessons.
- **`[anchor]`** — the good-enough bottom: a leaf we know has a layer below but deliberately did not descend. It is a leaf, so it carries state.
- **`[needs: ...]`** — cross-parent prerequisites. A node may flip only when every id in `needs` is 1. Within one parent, children are assumed bottom-up in list order unless an explicit `needs` overrides.
- **`(LR-NNNN)`** — the learning record that evidences the flip.

## Granularity (scale-invariance, made operational)

- **Nesting depth is unbounded.** Any number of levels (domain → subdomain → … → minimal node); a leaf is simply the deepest node at the current granularity.
- A leaf is the current **minimal node** — the only flip target.
- **Good-enough bottom ≡ one-demonstration-sized**: a leaf must be small enough that one demonstration can flip it (a lesson may contain several such demonstrations — see SKILL.md's lesson-scope note). If it cannot, descend (split the map, never split the flip). The original "~30 minutes to explain" heuristic is the approximation to this. When `f-critical` is empty (fuzzy or `endless`), the "affects the current f" condition is dropped — one-demonstration-sized alone governs descent.
- When an anchor is descended (its children revealed), the coarse ✓ does **not** transfer: the new children start at 0. Only structure moves on reconstruction — authored states do not.

## The single-thread state machine

```
IDLE ──select X, produce lesson, set Status + Open flip──▶ AWAITING-DEMONSTRATION
                                                              │ user demonstrates, passes
                                                              ▼ verify ✓, write LR, clear marker
                                                           IDLE
                                                              ▲
AWAITING-RESOLUTION (Open flip: X) ◀─── demonstration failed
```

- **AWAITING-DEMONSTRATION**: the only valid continuation is to get the demonstration, verify each node against its own check, and record. Authoring any other lesson is forbidden.
- **AWAITING-RESOLUTION**: continue the same flip — re-teach the same node, or subdivide the map for it. A replacement lesson for the *same* node is allowed; a new flip is not. **Re-teaching** produces a replacement lesson and returns to `Status: AWAITING-DEMONSTRATION` with the same `Open flip`. **Subdividing** is a reconstruction: the node becomes a parent, its new children start at 0, and the next child becomes the open flip (`Status: AWAITING-DEMONSTRATION`).
- **Partial pass (multi-node lesson):** passed nodes flip to 1; the open-flip set shrinks to the failed node(s), which stay 0 with `Status: AWAITING-RESOLUTION`.
- **Abandoning** a flip is legal and explicit: record why, return to `IDLE`.
- A fresh session that opens an `AWAITING-*` state finishes the open flip before anything else.

## Reconstruction (unit operation a)

**Triggers.** A reconstruction happens when: (1) a new information source changes *structure* — new nodes, a different coarse-graining, re-ordered/added dependency edges, or a correction to a node's state; (2) the next flip is blocked (no 0-node has all its `needs` satisfied); (3) the user repeatedly fails or is confused in an assessed region (wrong bottom or wrong grain); (4) the user offers a structural reframing; (5) f changes (see MISSION-FORMAT).

A source that only deepens or illustrates nodes already in the map is **not** a reconstruction — cite it in `RESOURCES.md` and keep flipping.

**What changes** — the node set, the dependency edges, the coarse-graining, the version, one History line.

**What is preserved** — all authored `✓` states, all node ids, the single-thread invariant, and all anchors except the ones being deliberately descended.

**Re-zero (the one allowed reversal)** — a `✓` returns to 0 only when: a source proves it was wrongly learned, a re-verification fails (storage decay), or the node's pass bar no longer holds because its requirement/spec moved (a project node whose API or format changed). **Every re-zero files a learning record** — a superseding record carrying the `Node:` line (for decay/spec-drift the cause is the record body) — so the reversal is traceable and the map's `✓` links stay accountable. Knowledge does not otherwise "un-happen".

## History

One bullet per reconstruction: date, source, what changed, what was preserved. The decision-grade narrative lives in a learning record the History line links to; History itself stays a one-line index so "why is the map shaped this way" is answerable.

## Relationship to other files

- `NOTES.md` — the dependency sketch moves out to here; `NOTES.md` returns to preferences and working notes only.
- `learning-records/` — the evidence that a `✓` is justified; a superseded record justifies a re-zero. Each flip record carries a `Node:` line pointing back here.
- `MISSION.md` — home of f; this file references it, never restates it.
- `GLOSSARY.md` — canonical labels used as node names.
- `lessons/`, `reference/`, `RESOURCES.md` — unchanged.

## Example

```
# MAP — Rust CLI
Status: AWAITING-DEMONSTRATION | Open flip: lang.lifetimes
f: see MISSION.md §Goal predicate f · f-critical: {cli.regex, cli.args, lang.ownership}
progress: leaves 3/7 ✓ · anchors 1 · f decidable: yes (f-critical 3/3 mapped)
v0.2 · reconstructed 2026-08-24 via Rust Book ch.10 (provisional)

## project.cli
  ✓ cli.scaffold: crate + cargo build works            (LR-0001)
  0  cli.args: parse CLI args        [needs: lang.ownership]
  0  cli.regex: implement a matcher  [anchor]

## lang
  ✓ lang.ownership: ownership & borrow rules           (LR-0003)
  0  lang.lifetimes: lifetimes       [needs: lang.ownership]
  0  lang.traits: traits & generics
    0  lang.traits.basic: what generics are
    0  lang.traits.composition: derive + bounds

## History
- v0.1 2026-08-24 · via mission + agent knowledge · initial construction
- v0.2 2026-08-24 · via Rust Book ch.10 · descended lang.traits anchor into two leaves; preserved lang.ownership ✓
```
