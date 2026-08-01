---
id: "sk-20260516-low-energy"
slug: "low-energy-day"
title: "Low-Energy Day Response"
status: active
score: 3.0
iterations:
  count: 2
  success_count: 1
  fail_count: 0
defects:
  - date: 2026-06-23
    description: "v1 design treated low scores as static — swapped to gentle tasks for the whole day. Missed that behavioral activation (doing normal tasks, socializing) can raise scores within ~3h."
    resolution: "v2 redesign: skill no longer swaps tasks. Two recovery paths added — (1) social accountability (higher leverage, ask first), (2) solo task execution with ~3h endurance window + reassessment checkpoint. Activity pool repositioned as Plan C (last resort)."
    resolved: true
    score_impact: -1.5
xp: 10
created: 2026-05-16
updated: 2026-06-23
---

# Low-Energy Day Response

**Trigger**: Daily startup — `mental_score < 30` or `physical_score < 40`. Can also be manually triggered by saying "low energy mode."

**Core principle (v2)**: Low morning scores are a starting condition, not a fixed label. Two things can pull scores up: **(1) Social accountability** — being around a friend who expects you at your best. Higher leverage, less painful, but requires another person. **(2) Solo task execution** — doing normal work despite feeling terrible. Works within ~3h, but the adaptation window is rough. The skill checks for option 1 first; falls back to option 2. If neither works after reassessment, fall back to gentle activities.

## Offline

**My responsibilities**:

1. **Know my accountability people**: maintain a short mental list of friends who (a) I can reach out to on short notice, (b) expect me to show up as my competent self, and (c) I'd push through discomfort to avoid letting down. These are the highest-leverage recovery tools I have — their mere presence can override a low-energy state faster than any solo strategy.

2. **Maintain a fallback activity pool** — used only if reassessment confirms energy hasn't recovered. Activities are concrete, ≤90 min each, organized by category (going out, hands-on, physical, input, output, micro, zero-effort). Used as Plan C, not the default.

3. **Know the pattern**: first ~3h of solo work on a low-energy day will feel like torture. This is expected. It's not a sign to stop. The question is whether scores recover after pushing through — and the only way to find out is to push through.

## Online

### Trigger Timing

During daily `start`, AI reads the day's mental_score / physical_score. Trigger when either:
- mental_score < 30
- physical_score < 40

User can also say "low energy mode" to manually trigger.

### Steps

- order: 1
  action: "Acknowledge the low scores without catastrophizing. Then ask: 'Is there a friend you can reach out to today — someone you'd want to be at your best around?' If yes → 'That's the move. Social accountability is the fastest override. Study together, do normal tasks together — the friend's presence does the heavy lifting. No special plan needed.' If no → 'No problem. Same plan as any other day, solo. Fair warning: the first ~3 hours will probably suck. That's normal. Push through. We'll reassess after.' In either case, do not swap tasks or reduce the plan."
  note: "Social check comes first because it's higher leverage and less painful. Solo endurance is the fallback, not the default."
  execute_skill: null
  skill_args: {}
  on_failure: "stop"

- order: 2
  action: "Generate or confirm the normal daily plan (same tasks, same intensity as any day). Insert one change: a mandatory reassessment checkpoint after ~3 hours of activity. Mark it clearly in the plan: '⏰ Reassessment: re-rate mental/physical. If recovered → continue. If still low → switch to fallback mode.'"
  note: "The plan is identical to a normal day — same projects, same tasks. The only addition is the checkpoint."
  execute_skill: null
  skill_args: {}
  on_failure: "stop"

- order: 3
  action: "Write the plan to today's daily file. Include the reassessment checkpoint marker. Also include a brief note: 'Low-energy start. Normal plan — push through first ~3h, reassess after.'"
  note: "The daily file records the decision to push through, so the next session's AI knows a reassessment is pending."
  execute_skill: null
  skill_args: {}
  on_failure: "stop"

- order: 4
  action: "At reassessment time (~3h later, or next user interaction after that window): ask user to re-rate mental and physical. If both scores are now above threshold → 'Scores recovered — low-energy mode off. Continue normal day.' Update daily file. If still below threshold → before falling back to the activity pool, ask: 'Still rough. One more thing to try — any friend free right now? Even a short hangout can turn this around.' If yes → social override (keep normal plan, do it together). If no → trigger fallback: generate a gentle rhythm framework from the activity pool for the remaining day."
  note: "Reassessment is the core mechanism. Social check at reassessment catches the case where the user didn't think of it in the morning but might now."
  execute_skill: null
  skill_args: {}
  on_failure: "stop"

## Fallback Rhythm Template (Plan B — only if reassessment fails)

If scores haven't recovered after the ~3h push, generate this for the remaining day. Core rule: no clock times, only sequence order. Each slot offers 2-3 options from the activity pool — the user picks, or says "skip."

```
========================================
Today's Rhythm — Fallback Mode
========================================

🌿 Next: Go outside
   [pick] 2-3 options from going-out category

✋ Then: Do something with your hands
   [pick] 2-3 options from hands-on or physical

🍚 Meal + rest

📖 Then: Quiet input
   [pick] 2-3 options from input category

🚶 Then: Outside again (or skip)
   [pick] 2-3 options from going-out (different from first)

🍜 Dinner

🌙 Wind down
   [pick] 2-3 options from output or input
   Something that makes today feel lived.

💤 Good night.
========================================
```

## Activity Pool (Fallback Only)

Used only when reassessment confirms low energy. Each activity ≤90 min, concrete, no micro-instructions.

**Going out** (leave the screen, preferred):
- Walk the usual route to the park, sit 10 min, return (~60 min)
- Bike ride, no destination (~45 min)
- Library — browse shelves, flip magazines, sit in the study area (~90 min)
- Walk to buy groceries / browse a store (~45 min)
- Walk a different direction — explore an unfamiliar street (~60 min)

**Hands-on**:
- Clear desk surface — surface only, don't expand to drawers (~20 min)
- Organize one drawer — dump everything, keep what you need, wipe clean (~40 min)
- Organize one bookshelf row (~20 min)
- Fold laundry / organize one wardrobe section (~30 min)
- Learn to cook one dish with a parent (~60 min)
- Help wash/chop vegetables (~30 min)

**Physical**:
- Push-ups: 3 sets to failure, 2 min rest between (~15 min)
- Squats: 3 sets × 15 (~10 min)
- Planks: 3 holds to failure (~10 min)
- Full-body stretch: 10 min, neck to ankles

**Input** (paper or audio only, no screens):
- Flip through old test papers / mistake notebooks — just browse, no memorization (~30 min)
- Flip through a physical magazine or book (~30 min)
- Listen to one podcast episode with a clear endpoint (~30-60 min)
- Listen to a full album, do nothing else (~40-60 min)

**Output**:
- Write a letter to your future self (~30 min)
- List "top 10 things I want to do after exams" (~20 min)
- Copy a poem or song lyrics you like (~15 min)
- Taste journal — write down what you ate today (~15 min)
- Clean up phone photos, delete unwanted screenshots (~20 min)

**Micro** (5-15 min, for transitions):
- Make the bed
- Stand by the window, look far
- Close eyes, listen to one song
- Make a cup of tea, drink it slowly
- Water plants (if any)

**Zero-effort** (when you want to do nothing):
- Lie down, close eyes, rest
- Sit and stare — permission to do nothing
- Nap (≤90 min, avoid disrupting night sleep)

## Supplementary Rules

- This skill does not replace Crisis Mode (physical < 30 triggers M18 Crisis Mode, which behaves differently)
- If task pool is empty, AI guides user to come up with one easy fallback task on the spot
- Low-energy days do not track progress advancement — only record whether the reassessment passed or fallback was used
- If low-energy mode triggers for 3 consecutive days, AI proactively asks whether to adjust overall rhythm or see a doctor
- **User autonomy**: user says "skip this slot" → skip. User says "I want to do X instead" → replace current slot option. AI does not argue, persuade, or explain "why you should"
- **Rhythm over efficiency**: the goal is not "accomplish more." Any phrasing that sounds like pushing or rushing is to be avoided — even in normal mode during the adaptation window
- **Slot selection rules**: each slot draws 2-3 options randomly from the corresponding activity pool category. Check yesterday's daily — avoid identical activity combinations. Same activity max 2 consecutive days.
