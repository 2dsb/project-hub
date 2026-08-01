---
id: "idea-20260731-cms"
title: "Contact Management Simplified: 4-Field Schema"
tags: [people-map, contact-management, simplification, design-decision, data-model]
status: raw
created: 2026-07-31
updated: 2026-07-31
source_type: "manual"
source_path: null
importance: 7
permanent_note_material: false
material_since: null
material_expiry_days: 14
promoted_from: null
links: []
related_entities:
  - type: ideas
    slug: "four-step-networking-method"
    relation: "complement"
    strength: 0.7
    dimensions: ["complement"]
    bidirectional: true
    source: "manual"
---

# Contact Management Simplified: 4-Field Schema

## Source

After the CKGSB event, while preparing to add new contacts to the people-map, the existing 12+ field schema (with `interests`, `recent_updates`, `resources`, `needs`, `birthday`, `identity`, etc.) felt like premature structure. The decision: strip it down to what actually matters.

## The New Schema

Four fields only:

| # | Field | Type | Purpose |
|---|-------|------|---------|
| 1 | `name` | string | Who they are |
| 2 | `contact` | string | How to reach them (WeChat, phone, etc.) |
| 3 | `maintenance_tier` | enum: `core` / `general` / `weak` | How close/important the relationship is |
| 4 | `contact_dates` | list of dates (`YYYY-MM-DD`) | Every date I actively reached out, ran into them and talked, or deepened the connection |

## Why the Old Schema Was Overbuilt

- **`interests` / `recent_updates` / `resources` / `needs`**: requires constant manual maintenance. For 100+ contacts, this becomes a second job. The information naturally lives in memory or the last conversation — not in a stale YAML field.
- **`birthday`**: only matters for core-tier contacts, and even then, a separate reminder system is better.
- **`identity`**: changes over time. Better captured implicitly through interaction log entries.
- **`tags`**: premature categorization. Tags make sense when you have 200+ contacts; at 40, you know who everyone is.

## What `contact_dates` Replaces

The old `## 互动日志` (interaction log) section was free-text — dates mixed with narrative. `contact_dates` strips it to the signal: **when did I last invest in this relationship?** The frequency and recency of dates in this list IS the relationship health metric. No need for prose.

## Migration

Existing 38 contacts (all classmates) will be migrated to the 4-field format. The old fields (`phone`, `weixin_id`, `interests`, `recent_updates`, `resources`, `needs`, `birthday`, `identity`, `tags`) will be dropped.
