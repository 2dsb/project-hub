---
id: "idea-20260731-cms"
title: "Contact Management Simplified: 4-Field Schema"
tags: [people-map, contact-management, simplification, design-decision, data-model]
importance: 7
connections:
  - type: idea
    slug: "four-step-networking-method"
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

The old `## Interaction Log` section was free-text — dates mixed with narrative. `contact_dates` strips it to the signal: **when did I last invest in this relationship?** The frequency and recency of dates in this list IS the relationship health metric. No need for prose.

## Migration

Existing 38 contacts (all classmates) will be migrated to the 4-field format. The old fields (`phone`, `weixin_id`, `interests`, `recent_updates`, `resources`, `needs`, `birthday`, `identity`, `tags`) will be dropped.
