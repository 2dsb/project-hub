---
id: "idea-20260629-we01"
title: "Willingness Experiment: Continue vs. Switch"
tags: [experiment, meta-cognition, willingness, decision-making, project-management]
status: raw
created: 2026-06-29
updated: 2026-06-29
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
    slug: timeline-based-project-structure
    relation: tests-mechanism-of
    strength: 0.9
    dimensions: [concept-relation]
    bidirectional: true
    source: manual
---

# Willingness Experiment: Continue vs. Switch

> Tests the willingness dynamics described in [[timeline-based-project-structure]] — specifically the tension between continuity fatigue and milestone gravity.

## Design

**Question**: When I feel resistance to continuing a project after N consecutive days, is it better to push through or switch to something else?

**Two arms**:
- **Continue** — push through the resistance, stay on the same project
- **Switch** — switch to a different project for the session

**Fixed conditions**:
- Same time block: Deep Work I (14:00–17:00) or equivalent energy-peak slot
- Continue project: Deep Learning Book (Chapters)
- Switch project: PyTorch (torch.nn module)
- Record mental/physical scores at session start

**N**: 5 trials per arm = 10 total sessions

## Outcome Metrics

| Metric | Scale | Question |
|--------|-------|----------|
| Output quality | 1–10 | How good was the work produced this session? |
| Output volume | pages/sections | How much got done? |
| Session satisfaction | 1–10 | How did I feel after the session? (energy, regret, momentum) |
| Next-day carryover | 1–10 | Did this make the *next* session easier or harder? |

Hypothesis: Continue may score higher on output volume but lower on satisfaction and next-day carryover. The interesting result is whether the trade-off is worth it.

## Trial Log

| # | Date | Arm | Start M/P | Project | Quality | Volume | Satisfaction | Next-Day | Notes |
|---|------|-----|-----------|---------|---------|--------|-------------|----------|-------|
| 1 | 2026-06-29 | continue | 70/70 | DL Book Ch5 | | | | | |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |
| 4 | | | | | | | | | |
| 5 | | | | | | | | | |
| 6 | | | | | | | | | |
| 7 | | | | | | | | | |
| 8 | | | | | | | | | |
| 9 | | | | | | | | | |
| 10 | | | | | | | | | |

## Analysis

After 10 trials, compare arm means across all 4 metrics. Look for:
- Significant differences (≥1.5 pt gap on 1–10 scale)
- Trade-off patterns (one metric up, another down)
- Interaction with mental/physical scores
- Whether the pattern shifts over trials (adaptation effect)
