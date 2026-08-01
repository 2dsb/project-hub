---
slug: train-travel
title: Train Travel
status: active
score: 1.0
xp: 0
created: 2026-06-22
updated: 2026-06-22
tags:
  - travel
  - train
  - logistics
defects: []
iterations:
  count: 1
  success_count: 1
  fail_count: 0
related_skills: []
related_entities:
  - type: "idea"
    slug: "goal-singularity"
    relation: "applies-to"
    strength: 0.3
    bidirectional: false
    source: "auto"
---

# Train Travel

> Personal skill: end-to-end train travel workflow, from booking to arrival. Solidified from first solo trip (Shanghai → Jingmen, 2026-06-22).

---

## 离线 (Offline — User's Independent Actions)

### 1. Booking (≥2 days before)

- Book on 12306 app. Ticket tied to your ID card — no paper ticket needed.

### 2. Packing (day of, ~5h before)

**The suitcase / backpack split:**

| Suitcase (train-unnecessary) | Backpack (train-necessary) |
|---|---|
| Clothes, pants, socks | ID card |
| Medicine, hand cream pouch | Mask |
| Nasal rinse kit (cup, bottle, salt) | Phone kit (phone + charging cable) |
| Gifts for others | Laptop kit |
| | Kindle kit |
| | Jump rope |
| | Cash |
| | Jacket |
| | Pencil case |
| | Study materials for the train |
| | Water bottle |

**Rule**: If you can't reach it mid-ride, it shouldn't be in the backpack. If you won't touch it until arrival, it shouldn't be in the backpack.

### 3. Departure (~2h before)

- Leave for the station. Buffer: arrive ~1h before departure.

### 4. At the station (T-1h to T-20min)

- Enter → find security checkpoint (ID card only)
- After security → find your ticket gate number (e.g., 7A/7B)
- Wait near gate → board when called (~T-20min)

### 5. Arrival

- Exit station through the exit gate (ID card only)
- Receipt/invoice: available at station self-service machines using ID card

---

## 在线 (Online — AI-Assisted)

### Trigger

User says "I'm taking a train" / "train trip coming up" / "help me prep for a train trip."

### Steps

1. **Check booking status** — ask: "Ticket booked on 12306?" If not → remind to book ≥2 days ahead
2. **Verify departure time** — ask for departure time, calculate: leave home at T-2h, aim to arrive at station by T-1h
3. **Run packing checklist** — present the suitcase/backpack table above, ask user to confirm each item and note any additions for this specific trip
4. **Pre-departure reminder** — if the AI session is active near departure time: remind "ID card in backpack? Leave by X:XX"
5. **Post-trip debrief** — after the trip: ask "Anything different from the plan? New items to add or tips to record?" → update this skill
