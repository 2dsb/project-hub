---
id: "idea-20260731-cms"
title: "Contact Management Simplified: 4-Field Schema"
tags: [social-resources, contact-management, simplification, design-decision, data-model]
summary: "After the CKGSB event, the contact management schema was stripped from an overbuilt twelve-plus field structure to four fields: name, contact, maintenance_tier (core, general, or weak), and contact_dates. The old fields like interests, recent_updates, resources, needs, birthday, identity, and tags demanded constant manual maintenance and became stale or premature. The contact_dates list replaces free-text interaction logs by recording every outreach or deepening encounter, making frequency and recency the relationship health metric. Existing thirty-eight classmate contacts will be migrated and the old fields dropped."
body_hash: "d20d7de1"
importance: 3.48  # auto
connections:
  - type: idea
    slug: "four-step-networking-method"  # auto
  - type: idea
    slug: "contact-management"  # auto
---
# Contact Management Simplified: 4-Field Schema

## Source

After the CKGSB event, while preparing to add new contacts to the social-resources, the existing 12+ field schema (with `interests`, `recent_updates`, `resources`, `needs`, `birthday`, `identity`, etc.) felt like premature structure. The decision: strip it down to what actually matters.

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
