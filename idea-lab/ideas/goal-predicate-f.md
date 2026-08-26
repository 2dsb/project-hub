---
id: idea-20260826-goal-predicate-f
title: Goal Predicate f
tags:
  - goal-predicate
  - teach-method
  - mission-design
  - learning
summary: "The Goal Predicate f expresses \"done\" as a checkable conjunction of falsifiable clauses, each referencing MAP.md nodes or an external arbiter such as an exam or deadline. It is the only workspace element that comes from outside learning and serves as the arbiter of completion. f may begin fuzzy, so a provisional direction-f is written and clarifying f becomes a first learning goal, updated as the user's understanding sharpens. Evaluation makes f true only when all f-critical nodes are checked and non-node check procedures pass, with pending external results recorded as awaiting-arbiter. Only the user changes f; external arbiters are ground truth."
body_hash: "777b85af"
connections:
  - type: idea
    slug: "knowledge-map-format"  # auto, review: 0.562
  - type: idea
    slug: "fundamental-model-of-learning"  # auto, review: 0.560
  - type: idea
    slug: "success-interrogation-heuristic"  # auto, review: 0.535
  - type: idea
    slug: "pass-criteria-as-curriculum-design"  # auto, review: 0.529
  - type: idea
    slug: "goal-singularity"  # auto, review: 0.506
importance: 0.0  # auto
---
# Goal Predicate f

From the `/teach` optimization attempt (2026-08-24). The optimization as a whole failed and was rolled back, but this design — the goal made checkable as a falsifiable predicate — was judged excellent and is preserved here in full, verbatim from the failed version's `MISSION-FORMAT.md`.

## The `## Goal predicate f` section

f is the goal made checkable: a conjunction of clauses, each **falsifiable** and each referencing either **map nodes** (from `MAP.md`) or an **external arbiter** (an exam, a deadline, a reviewer). It is the only thing in the workspace that comes from outside the learning itself, and it is the arbiter of "done".

### Writing f

Upgrade each "Success looks like" bullet to a clause: replace the evaluative verb with an observable action + condition + result, and name the referenced nodes.

**f may start fuzzy — and that is normal.** The user often has only a direction, a felt sense, before learning clarifies it. When that's the case: write a provisional f from whatever the user *can* state (a direction, one or two clauses, a goal they can't yet define precisely), mark it as clarifying, and make *clarifying f* a first goal of learning. As nodes flip, the user's understanding sharpens — and so does their ability to state f. Every time the user can say what they want more precisely, update f and record the shift in a learning record. The user's growing ability to state f is itself evidence of learning. **While f stays fuzzy (or is `endless`), `MAP.md` records `f-critical: {}` and `f decidable: no`** — no target set yet; the map header reflects f's clarifying status.

- "I can use Rust well" → `C1: I can implement, from memory and without notes, a Rust program that reads a file, parses lines, and handles errors, and it compiles and runs (nodes: {ownership, error handling, file I/O}).`

- "I pass CPA Economic Law" → `C1: I can reproduce every knowledge point in the official syllabus from memory (nodes: {per-chapter syllabus nodes}). C2: I score ≥60/100 on a full timed mock paper (arbiter: mock paper). C3: C1 and C2 hold by 2026-12-05 (deadline).`

  **Elicitation probes** (use as needed to draw f out of the user):

1. *Terminal* — "When we're done, what exactly will be true? How would someone check it without asking you?"
2. *Falsification* — "What would count as NOT done? A concrete state where we both agree the goal is unmet?"
3. *Artifact* — "What will exist that doesn't exist now — a running program, a written piece, a recorded demo?"
4. *Action* — "What will you be able to DO, that you can't do now, that I could watch you do?"
5. *External arbiter* — "Does anything outside this workspace grade this — an exam, a deadline, a customer? What exactly do they check?"
6. *Terminal vs continue* — "Is there a real stopping point, or will 'done' be a checkpoint we pick and then raise? Or do you want to keep going with no end at all?" No end → a checkpoint f (re-derive on each achievement), or `endless` (f ≡ 0) if the user wants to learn forever; never pretend there's a terminal.
7. *Time* — "By when? Does the date change the predicate (must pass by T) or just the pace?"
8. *Depth* — "If you hit the easy version of this today, would you call it done — or is there a bar you'd insist on?"
9. *Nodes* — for each success bullet: "Which pieces must be in place before this bullet is checkable?"

### Rules for f

**How f(G) is evaluated:** a node-clause is satisfied iff every id in its `nodes:` set is ✓; f(G)=1 iff all f-critical nodes are ✓ **AND** every non-node clause's check procedure has been performed and passed. Arbiter clauses with a pending result → `awaiting-arbiter`.

- **Never write f from your own guess.** Every clause is user-named, or user-confirmed after you restate it. If the user cannot produce a checkable clause, do not invent one — interview harder, or start with a provisional direction-f and let learning clarify it (see Writing f). A fake-precise f is worse than an honest fuzzy one.
- **If the user has no terminal goal**, mark it `shape note: checkpoint-and-re-derive` — f=true is then never "the end"; it is the signal to re-derive a deeper f with the user. **If the user explicitly wants no end at all** (learn forever), record `shape note: endless` (f ≡ 0): f is never true, "done" is never declared, and the loop continues indefinitely anchored by interest and ZPD.
- **Check f against the map before choosing the next operation.** f(G)=1 → done (or re-derive). f(G)=0 → keep going. f **undecidable** → diagnose the cause first: a clause references nodes the map lacks (→ reconstruct the map so f becomes decidable); a clause has no check procedure (→ restate it as a checkable action with the user); or f is itself still fuzzy — the user cannot yet say what they want precisely (→ teach with the shallow-first default, continuing as the hermeneutic loop until f clarifies; see STRATEGY-SPACE.md). The right move differs by cause.
- **Only the user changes f.** You may propose; the user confirms. On change: record a learning record (old f, new f, why, the diff), update this section in place, and re-anchor the map — flipped nodes stay 1, new f-critical nodes get added.
- **A deadline is part of f, not a mood.** If the goal is time-indexed, say so explicitly.
- **External arbiters are ground truth.** When f names an exam or grader, your evaluation is a *prediction*; the external result, when it arrives, supersedes and is recorded — this is normal, not a checking failure. While such a result is pending, the f-state is **awaiting-arbiter** (neither true, false, nor undecidable): record the prediction and wait.
