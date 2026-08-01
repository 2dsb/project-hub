---
id: "sk-20260627-prstr"
slug: "post-run-stretching"
title: "Post-Run Stretching Routine"
status: active
score: 0.0
iterations:
  count: 0
  success_count: 0
  fail_count: 0
defects: []
xp: 0
created: 2026-06-27
updated: 2026-06-27
---

# Post-Run Stretching Routine

**Trigger**: After a run. User says "stretch" / "post-run stretch" / "拉伸", or AI prompts after running session is recorded in daily.

7 stretches, 14 total poses (most are bilateral). Hold each stretch 20-30 seconds. Breathe steadily — don't hold breath.

## Offline

**My responsibilities**:

1. Do this after every run. No skipping.
2. Hold each stretch 20-30 seconds. Don't rush.
3. Breathe steadily through each hold. Don't hold breath.
4. If a stretch causes sharp pain (not gentle tension), ease off.
5. Order matters — start standing (1-4), move to floor (5-7).

## Online

### Trigger Timing

- After user records a running session in daily
- User says "stretch" / "拉伸" / "post-run stretch"

### Steps

- order: 1
  action: "Present the full 7-stretch sequence. Remind user: hold 20-30s each, breathe steady, sharp pain = stop."
  note: "The AI doesn't need to walk through each stretch in real-time — the user knows the routine. Just present the reference."
  execute_skill: null
  skill_args: {}
  on_failure: "stop"

- order: 2
  action: "After user confirms completion, ask: 'All 7 done? Any stretch feel particularly tight today?' Record tight areas to today's daily notes for tracking over time."
  note: "Tightness patterns over time can reveal imbalances or developing issues."
  execute_skill: null
  skill_args: {}
  on_failure: "stop"

---

## The 7-Stretch Sequence

### 1. Hip Flexor Stretch (髂腰肌) — Left / Right

Stand in a lunge position. Back knee on ground, front knee at 90°. Push hips forward until you feel the stretch in the front of the back-leg hip. Hold. Switch sides.

### 2. Hamstring Stretch (大腿后侧) — Left / Right

Stand, extend one leg forward with heel on ground, toes up. Slightly bend the standing knee. Hinge forward at hips (not waist) until you feel the stretch along the back of the extended thigh. Hold. Switch sides.

### 3. Quadriceps Stretch (大腿前侧) — Left / Right

Stand, bend one knee, bring heel toward glute. Hold ankle with same-side hand. Keep knees together, push hip slightly forward. Hold. Switch sides. (Hold a wall if balance is an issue.)

### 4. Glute Stretch (臀大肌) — Left / Right

Stand, cross one ankle over opposite knee (figure-4). Slowly sit back as if into a chair until you feel the stretch in the crossed-leg glute. Hold. Switch sides. (Hold a wall or desk for support.)

### 5. Inner Thigh Stretch (大腿内侧) — Both Sides

Sit on floor, soles of feet together, knees out to sides. Hold ankles. Gently press knees toward floor with elbows. Keep back straight. Hold.

### 6. IT Band / Outer Thigh Stretch (髂胫束) — Both Sides

Sit on floor, legs extended. Cross one leg over the other, foot flat outside opposite knee. Twist torso toward the bent knee, using opposite elbow against the outside of the bent knee for gentle leverage. Hold. Switch sides.

### 7. Calf Stretch (小腿) — Both Sides

Stand facing a wall. Step one foot back, keep it straight, heel pressed into ground. Front knee bent. Lean toward wall until you feel the stretch in the back-leg calf. Hold. Switch sides.
