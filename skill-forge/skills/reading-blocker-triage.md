---
id: "sk-20260621-rb-triage"
slug: "reading-blocker-triage"
title: "Reading Blocker Triage"
status: active
score: 1.0
iterations:
  count: 0
  success_count: 0
  fail_count: 0
defects: []
xp: 0
created: 2026-06-21
updated: 2026-06-22
source_idea: "daily/2026-06-21.md"
related_entities:
  - type: skill
    slug: "wm-overflow-prevention"
    relation: "shares-escalation-pattern"
    strength: 0.7
  - type: idea
    slug: "ai-source-triage"
    relation: "applies-to-reading-context"
    strength: 0.6
  - type: idea
    slug: "learning-pipeline"
    relation: "integrated-into"
    strength: 0.8
---

# Reading Blocker Triage

**Trigger conditions**:
- User reports "I don't understand this symbol/formula/concept" or "I'm stuck" while reading technical material (lecture notes, papers, documentation)
- AI observes the user lingering on a passage/formula too long, or repeatedly requesting explanations for the same type of symbol

**Core principle**: Not every "I don't get it" requires stopping to look it up immediately. First grade it — how severe is the blocker? — then decide how much effort to spend handling it. L1 let it go, L2 mark it, L3 pause.

## Offline

**User responsibilities**:

1. **Honest grading**: When you hit something you don't understand, first ask yourself — "Can I keep reading?" Yes → L1 or L2; no → L3. Don't escalate L1 to L3 because you "feel you should understand it."
2. **Centralized marking**: For L2 blockers, just mark them (highlight / underline / jot one word), don't look them up immediately. Batch-process all L2 marks after finishing the current section.
3. **Decisive pause on L3**: If the missing prerequisite knowledge is too large, don't force through it. Pause the project, create a prerequisite micro-task, come back after learning it. Forcing through = wasted time + building wrong understanding.
4. **Distinguish "need to know" from "want to know"**: Can't read a symbol but can continue → L2 (need to know, but not right now). Curious about a detail unrelated to the main thread → curiosity, not a blocker.

## Online

**AI behavior**:

### Step 0: Confirm the Signal

If the user just says "I don't get this" or "I'm stuck," first ask a scoping question:
- "Is it a **single symbol/term** you don't understand, or an **entire chain of derivation logic**?"

Single symbol → proceed to Step 1 grading. Entire derivation → go straight to L3 handling (an entire passage not making sense indicates a large prerequisite gap).

### Step 1: Grading

Based on the user's description, classify the blocker into one of three levels:

| Level | Signal | Criterion |
|-------|--------|-----------|
| **L1 — No significant impact** | "I don't recognize this symbol, but I roughly know what it's saying" | After skipping the symbol, the paragraph's main point is still understandable; the unknown symbol is "noise" not "circuit break" |
| **L2 — Affects precise understanding** | "I get the general idea, but I can't follow the formulas, can't pin down the details" | The paragraph's main point is understandable, but formulas/derivations can't be tracked; needs symbol explanation for full comprehension |
| **L3 — Complete blockage** | "I can't understand anything after this; the entire derivation is built on concepts I don't know" | The missing knowledge is a prerequisite dependency for what follows; can't continue without filling it |

**If the user can't self-grade** → AI proactively asks the L1/L2/L3 assessment question: "If you skip this symbol, can you still read the next paragraph?"

### Step 2: Level-Based Handling

#### Step 2.L1: Let It Go

1. **Confirm skip**: "This doesn't affect understanding the main thread — skip it for now."
2. **Optional micro-explanation**: If the user is curious, explain the symbol's meaning in one sentence (no expansion, no derivation). Right back to the text after that sentence.
3. **Don't record**: L1 blockers aren't worth recording — they're normal reading "noise," recording cost > benefit.

#### Step 2.L2: Mark → Batch Process

1. **Mark**: User makes a lightweight mark at that spot (highlight / underline / jot one word). AI reminds: "Just note it down — we'll look everything up together after finishing this section."
2. **Continue reading**: Don't interrupt; finish the rest of the current section (or chapter).
3. **Batch process**: After finishing the current section, AI handles all L2 marks together:
   - For each mark, give a concise explanation (1-3 sentences, no more than one screen), no derivation expansion
   - If multiple marks point to the same concept → merge explanations
   - After explaining, ask the user: "Is this enough for you to understand what you just read?" If not → escalate to L3
4. **Record to project notes**: Append L2 explanation content to project progress log as "prerequisite patches."

#### Step 2.L3: Pause → Fill Gaps → Return

1. **Confirm pause**: "This blocker indicates you're missing a chunk of prerequisite knowledge. I recommend pausing reading — fill in that piece first, then come back."
2. **Extract missing knowledge**: AI explicitly identifies what's missing — specific to concept/theorem/notation system. "You need: probability density functions + conditional probability + expected value — these three pieces."
3. **Create micro-task**: Turn the missing knowledge into an independent micro-task, record in project checklist or daily:
   - Format: `[ ] Prerequisite: XXX (source: <recommended resource>, estimated X minutes)`
4. **Set return condition**: Clarify what level counts as "enough" — not mastery, just "can understand the derivation in the passage that was blocking you."
5. **Return to breakpoint**: After user completes the micro-task, AI brings user back to the original reading position, rebuilding context in 1-2 sentences: "You were stuck on formula Y on page X — you should recognize this notation now. Ready to continue?"

### Step 3: Post-Blocker Recovery Check

After L3 handling is complete (user has learned the prerequisite and returned to the text), confirm:
- "Does the part you were stuck on make sense now?"
- If still not → the extracted missing knowledge was incomplete; return to Step 2.L3 to supplement more prerequisites
- If it makes sense now → continue reading

**Cumulative monitoring**: If L3 triggers ≥ 3 times in the same material, AI proactively suggests: "This material's prerequisite threshold might be higher than expected — want to do a comprehensive assessment of what else needs filling first, then fill everything at once before returning?"

#### L3 Severity Sub-Spectrum (v2, added 2026-06-22)

Not all L3 blockers are the same. After classifying something as L3, the AI needs to further distinguish severity, because this determines the handling strategy:

| Severity | Characteristics | Handling | Estimated Time |
|----------|----------------|----------|----------------|
| **L3-mild** | Missing a single concept or theorem; can be explained clearly in a short dialogue | Insert micro-task → fill same day → return to text same day | 15-30 minutes |
| **L3-severe** | Missing an entire prerequisite knowledge system (e.g., probability theory, linear algebra); cannot be filled via short dialogue | Pause project → create independent learning task → no deadline; return to text after completion | Days to weeks |

**Assessment rule**: AI asks itself — "Can I make the user understand this missing knowledge in no more than 30 minutes of dialogue?" Yes → L3-mild; no → L3-severe.

**Special handling for L3-severe**:
1. Clearly explain the severity judgment to the user: "This isn't about you not knowing one symbol — you're missing the entire probabilistic language system. Every subsequent page speaks this language, so 'finish reading first, fill gaps later' won't work."
2. Issue a notice (if the project has external commitments, e.g., a public account series) — explain the reason for pausing, set an "open-ended" expectation
3. Create an independent prerequisite learning project or task, tracked in INDEX

#### Prerequisite Spiral Guard (v2, added 2026-06-22)

When filling prerequisites, the prerequisite itself may need even more fundamental prerequisites — forming a recursive chain.

**Guard rule**: Only allow **one layer** of prerequisite unfolding.

```
Source material ──L3──▶ Prerequisite A ──another L3──▶ Prerequisite B?
                                         │
                           ┌─────────────┘
                           ▼
                    Switch to just-in-time lookup mode
                    (use AI to explain concepts in B
                     on demand, don't create new
                     prerequisite learning tasks)
```

**Boundary check**: "After filling A, can I understand the derivation in the original material?"
- Yes → stop here, return to source material
- No → A was the wrong choice (not the prerequisite actually needed), switch materials

**Switch signal**: When the user triggers L3 again while filling prerequisite A → AI does not create a new prerequisite task; instead enters just-in-time lookup mode: "This new blocker inside the prerequisite — I'll explain it in one sentence, you keep going — no recursive unfolding."

---

## Online

(Offline section additions are synced to online — AI automatically applies the L3 severity sub-spectrum and recursive spiral guard rules when executing Step 2.L3.)
