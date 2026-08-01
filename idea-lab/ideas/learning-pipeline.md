---
id: "idea-20260621-lp01"
title: "Learning Pipeline"
tags: [learning, pipeline, meta-cognition, flow-based-thinking, synthesis]
status: raw
created: 2026-06-21
updated: 2026-06-25
source_type: "manual"
source_path: null
importance: 0
permanent_note_material: false
material_since: null
material_expiry_days: 14
promoted_from: null
links: []
related_entities:
  - type: idea
    slug: "flow-based-thinking"
    relation: "instantiates"
    strength: 1
  - type: idea
    slug: "ai-source-triage"
    relation: "integrates"
    strength: 0.9
  - type: idea
    slug: "peer-cross-teaching"
    relation: "integrates"
    strength: 0.9
  - type: skill
    slug: "reading-blocker-triage"
    relation: "integrates"
    strength: 0.8
  - type: idea
    slug: "goal-singularity"
    relation: "governed-by"
    strength: 0.9
  - type: literature-notes
    slug: "echo-rebuilding-0"
    relation: "complements"
    strength: 0.6
    dimensions: ["concept-relation"]
    bidirectional: true
    source: "auto"
  - type: literature-notes
    slug: "echo-rebuilding-1.1"
    relation: "complements"
    strength: 0.6
    dimensions: ["concept-relation"]
    bidirectional: true
    source: "auto"
  - type: literature-notes
    slug: "echo-rebuilding-1.2"
    relation: "complements"
    strength: 0.6
    dimensions: ["concept-relation"]
    bidirectional: true
    source: "auto"
  - type: literature-notes
    slug: "echo-rebuilding-5.1"
    relation: "complements"
    strength: 0.6
    dimensions: ["concept-relation"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "ai-source-triage"
    relation: "concept-relation"
    strength: 0.85
    dimensions: ["concept-relation", "complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "peer-cross-teaching"
    relation: "concept-relation"
    strength: 0.85
    dimensions: ["concept-relation", "complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "goal-singularity"
    relation: "concept-relation"
    strength: 0.8
    dimensions: ["concept-relation", "complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "flow-based-thinking"
    relation: "complement"
    strength: 0.75
    dimensions: ["concept-relation", "complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "knowledge-reconnection"
    relation: "integrates"
    strength: 0.9
    dimensions: ["complement", "concept-relation"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "locate-first-model-last"
    relation: "related"
    strength: 0.5
    dimensions: ["concept-relation"]
    bidirectional: true
    source: "auto"
  - type: literature-notes
    slug: "卡片笔记写作法c2.2"
    relation: "extends"
    strength: 0.83
    dimensions: ["tag-overlap", "concept-relation"]
    bidirectional: true
    source: "auto"
---

# Learning Pipeline

## Trigger

Today, when piecing together four independent ideas accumulated over the past few weeks, I realized they exactly cover the complete learning workflow — from "what should I learn" to "how to learn it" to "what if I get stuck" to "how do I output it." These aren't four unrelated things; this is a pipeline.

## The Full Pipeline

```
Source                        Router                                Sink
                                    
Find quality sources     AI source triage       Reading blocker       → Analogy (for others)
(flow-based-thinking)    (AI pre-judges what's   triage L1/L2/L3      → Translation (CN→EN)
                         worth learning)         (Stuck? Grade it,    → Reconnection Doc
                         Peer cross-teaching     handle by level)      (for future you)
                         (human pioneers tell
                         you what to learn)

"Where's the best        "What's worth           "How stuck am I,     "Say it in my own
source?"                 spending time on?"       and what now?"       words — to others,
                                                                      or to future me."
```

## Stage Breakdown

### Stage 1: Source → Find Quality Sources

Apply `flow-based-thinking`'s first question: where's the source?

- Ask AI: What's the best introductory material for this field?
- Ask pioneers: You've learned this — what route do you recommend?
- Follow references from courses/papers: trace back to original sources

Output: a high-quality information source (e.g., MIT 6.S184 lecture notes).

### Stage 2: Router → Pre-judge Value, Filter Noise

Insert a pre-judgment layer between the source and "I'm investing time in this."

Two kinds of pre-judges:
- **AI** (`ai-source-triage`): traverse the content structure in advance, mark what's worth reading, what to skip, what to go straight to source
- **Human pioneer** (`peer-cross-teaching`): someone who's already learned it tells you "just read the Introduction + source code, don't need to follow the whole video series"

Output: a streamlined learning path (e.g., "50 minutes to the core" instead of "2 hours browsing everything").

### Stage 3: Router → Handle Blockers During Learning

While progressing along the path, hitting something you don't understand → trigger `reading-blocker-triage`.

- L1: unrecognized symbol but doesn't affect the main thread → skip
- L2: can grasp the gist but can't pin down details → mark, batch-process after finishing the current section
- L3: the entire derivation rests on unknown concepts → pause, fill prerequisites, return

Key principle: **Don't escalate L1 to L3 because you "feel you should understand it."** Be honest — grade based on the actual situation, not emotional escalation.

Output: uninterrupted reading flow + precise gap-filling when necessary.

### Stage 4: Sink → Output in Your Own Way

True understanding = being able to restate in your own words.

Three output modes, each serving a different audience:

- **Analogy** (e.g., mountain navigation story explaining Flow Matching) — for *others*. Lowers cognitive barrier while testing your own understanding. External-facing.
- **Translation** (CN→EN) — for *expression practice*. Turns "I can understand" into "I can express," and the translation process exposes fuzzy spots in understanding. External-facing, but the benefit is internal.
- **Reconnection Doc** (`knowledge-reconnection`) — for *future you*. A PCA-like encode/decode process: after learning, compress your understanding into a structured document that preserves the relationships between concepts (not every fact). When returning after a gap, decode it in ≤30s to reconstruct your mental model. Internal-facing, written once, decoded many times. Follows 4 constraints: low decode cost, structured model output, main points preserved, minimal length.

Output: a public account article, notes, a reconnection doc — or at minimum a summary written in your own words.

## First Real-World Run (MIT 6.S184, 2026-06-21)

```
Source:   Found MIT 6.S184 on project dashboard → got lecture notes PDF
  ↓
Router1: Started reading (haven't applied triage yet — next time, let AI preview TOC+abstract first)
  ↓
Router2: Hit probability notation → graded L2 → marked, AI explained after finishing section → continued
  ↓        Hit completely incomprehensible probability derivation → graded L3 → realized missing college probability prerequisite
  ↓        → paused, created prerequisite micro-task (pending execution)
  ↓
Sink:    Completed analogy story draft in Chinese → began line-by-line English translation
  ↓        (output = public account article, also English practice + understanding verification)
```

## Relationships to Other Ideas

| Component | Position in Pipeline | Role |
|-----------|---------------------|------|
| `flow-based-thinking` | Entire pipeline | Provides the "Source→Router→Sink" skeleton |
| `ai-source-triage` | Router (entry) | AI pre-judges learning value |
| `peer-cross-teaching` | Router (entry) | Human pioneer guidance |
| `reading-blocker-triage` | Router (in-process) | Graded handling of blockers during learning |
| `wm-overflow-prevention` | Router (auxiliary) | Prevents overload when too many parallel tasks |
| `knowledge-reconnection` | Sink (internal) | Encode understanding into structured doc for future-self decode |

The pipeline doesn't require running every node for every learning session. Light reading might only need Source→Sink; challenging new material needs the full Source→Dual Router→Blocker Handling→Sink.

## Second Real-World Run (MIT 6.S184, 2026-06-22) — L3 Escalation & Prerequisite Recursion

```
Source:   Lecture notes PDF already acquired (completed 06-21)
  ↓
Router1: 06-21 — first 3 sections went smoothly (few formulas, context + AI explanations sufficed)
  ↓
Router2: 06-22 — formula density spiked → multiple L2 marks → eventually triggered L3
  ↓        Grading result: missing prerequisite knowledge (rigorous probability definitions) is L3-severe
  ↓        → chose "fill prerequisites first" path (rather than "finish reading, fill gaps later")
  ↓
Sink:    Paused public account series → complete textbook → full lecture notes → resume writing
          (published suspension notice explaining the reason)
```

### New Insights Uncovered by This Run

#### 1. L3 Has an Internal Severity Spectrum

Not all L3 blockers are the same. Under the same L3 label, there are actually two distinctly different situations:

| Severity | Characteristics | Handling |
|----------|----------------|----------|
| **L3-mild** | Missing a single concept or theorem; AI can explain clearly in 15-30 minutes | Insert micro-task, fill same day, return same day |
| **L3-severe** | Missing an entire prerequisite knowledge system (e.g., college probability theory); cannot be filled via short dialogue | Pause project, insert systematic learning task, no deadline |

The 06-22 blocker was L3-severe: not "I don't know this one symbol," but "I'm missing the entire probabilistic language system." This explains why "finish reading first, fill gaps later" doesn't work — every subsequent page speaks this language; if you don't know the language, you can't read what follows.

#### 2. Prerequisite Spiral

Filling prerequisites can trigger **secondary L3s**: open the textbook → discover even more fundamental knowledge is needed → fill that → ... forming a recursive chain.

Response principle (incorporated into `reading-blocker-triage` L3 handling):
- Only fill **one layer** of prerequisites. If that layer itself needs prerequisites → switch to "just-in-time lookup" mode, use AI to explain on demand, don't recursively unfold
- Boundary check: "After filling this layer, can I understand the derivation in the original material?" Yes → stop, go back. No → this layer was the wrong choice, switch materials

#### 3. Another Validation of Goal Singularity

The 06-22 choice embodied `goal-singularity`: the announcement's job was "explain why the series is on hold and apologize" — a standalone information-delivery task. The announcement doesn't need to include learning insights, doesn't need to demonstrate understanding, doesn't need to strike a "yes I'm pausing but I'm still working hard" balance. One goal, one output. Write it, done.
