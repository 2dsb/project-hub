---
id: "idea-20260731-cms"
title: "Contact Management Simplified: 4-Field Schema"
tags: [social-resources, contact-management, simplification, design-decision, data-model]
summary: "The contact management schema was simplified from over 12 fields to just four: name, contact, maintenance_tier (core, general, or weak), and contact_dates (a list of YYYY-MM-DD dates of active outreach or meaningful encounters). The old fields like interests, recent_updates, resources, needs, birthday, identity, and tags were overbuilt because they required constant manual maintenance and became stale, while premature categorization didn't suit a small set of contacts. The contact_dates field replaces free-text interaction logs, acting as a relationship health metric based on frequency and recency. Existing contacts will be migrated by dropping the obsolete fields."
body_hash: "73947901"
importance: 3.58  # auto
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
