---
id: "idea-20260621-lp01"
title: "Learning Pipeline"
tags: [learning, pipeline, meta-cognition, flow-based-thinking, synthesis]
summary: "The learning pipeline structures the process of acquiring new knowledge from source to output using flow-based-thinking’s source-router-sink framework. Quality sources are identified through AI recommendations, pioneer advice, and reference tracing. A router stage then pre-judges material value via AI source triage and peer cross-teaching to filter noise before investing time. During learning, reading blocker triage grades stuck points into L1 (skip), L2 (mark and batch-process), or L3 (pause to fill prerequisites), with an explicit rule against emotionally escalating L1 to L3. The sink stage outputs understanding through analogy for others, translation for expression practice, or a reconnection doc for future you, which encodes compressed conceptual relationships that can be decoded quickly after a gap. Real-world runs with MIT 6.S184 revealed that L3 blockers span a severity spectrum, where L3-mild is a single concept fillable in minutes while L3-severe represents entire prerequisite systems requiring systematic study. Filling prerequisites can trigger recursive L3s, but the principle is to fill only one layer and switch to just-in-time lookup if further depths are needed, ensuring boundary checks prevent infinite descent."
body_hash: "45e10426"
importance: 8.25  # auto
connections:
  - type: idea
    slug: "flow-based-thinking"  # auto
  - type: idea
    slug: "ai-source-triage"  # auto
  - type: idea
    slug: "peer-cross-teaching"  # auto
  - type: project
    slug: "reading-blocker-triage"
  - type: idea
    slug: "goal-singularity"  # auto
  - type: permanent
    slug: "echo-rebuilding-0"
  - type: permanent
    slug: "echo-rebuilding-1.1"
  - type: permanent
    slug: "echo-rebuilding-1.2"
  - type: permanent
    slug: "echo-rebuilding-5.1"
  - type: idea
    slug: "knowledge-reconnection"  # auto
  - type: idea
    slug: "locate-first-model-last"  # auto
  - type: permanent
    slug: "卡片笔记写作法c2.2"
  - type: idea
    slug: "memorization-in-pipeline"  # auto
  - type: idea
    slug: "freedom-exploration-generator"  # auto, review: 0.575
  - type: idea
    slug: "transfer-high-leverage"  # auto, review: 0.553
  - type: idea
    slug: "learning-dynamics"  # auto, review: 0.545
  - type: idea
    slug: "teach-method-fixes"  # auto, review: 0.508
  - type: idea
    slug: "implicit-improvement-pattern"  # auto, review: 0.501
  - type: idea
    slug: "knowledge-mastery-two-axis-model"  # auto
  - type: idea
    slug: "data-pattern-prediction-chain"  # auto
  - type: idea
    slug: "structural-patience"  # auto, review: 0.582
  - type: idea
    slug: "three-layer-framework"  # auto, review: 0.556
  - type: idea
    slug: "breadth-first-trap"  # auto, review: 0.552
  - type: idea
    slug: "reconnection-doc-method"  # auto, review: 0.550
  - type: idea
    slug: "human-structure-ai-completeness"  # auto, review: 0.549
  - type: idea
    slug: "success-interrogation-heuristic"  # auto, review: 0.548
  - type: idea
    slug: "attention-as-bottleneck"  # auto, review: 0.535
  - type: idea
    slug: "leverage-existing-vs-build-from-scratch"  # auto, review: 0.526
  - type: idea
    slug: "knowledge-transfer-fidelity"  # auto, review: 0.526
  - type: idea
    slug: "attention-pointer-learning-model"  # auto, review: 0.523
  - type: idea
    slug: "daily-to-ideas-pipeline-broken"  # auto, review: 0.515
  - type: idea
    slug: "pass-criteria-as-curriculum-design"  # auto, review: 0.513
  - type: idea
    slug: "data-structure-first-code-reading"  # auto, review: 0.507
  - type: idea
    slug: "inquiry-essay-method"  # auto, review: 0.505
  - type: idea
    slug: "the-zettelkasten-method"  # auto, review: 0.504
  - type: idea
    slug: "learning-method-v2"  # auto
  - type: idea
    slug: "hermeneutic-circle-learning"  # auto
  - type: idea
    slug: "enumerative-as-scaffold-for-generative"  # auto, review: 0.595
  - type: idea
    slug: "ai-centered-new-education-industry"  # auto, review: 0.510
  - type: idea
    slug: "teach-task-volume-scaling"  # auto, review: 0.538
  - type: idea
    slug: "practice-necessity-willingness-tradeoff"  # auto, review: 0.503
  - type: idea
    slug: "pattern-pipeline"  # auto
  - type: idea
    slug: "fundamental-model-of-learning"  # auto, review: 0.518
  - type: idea
    slug: "letters-to-future-self"  # auto, review: 0.537
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
