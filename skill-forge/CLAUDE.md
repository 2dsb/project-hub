# skill-forge — Behavior Layer

If idea-lab is about **thinking**, skill-forge is about **doing**. Each skill is a methodology.

## Skill Format

```yaml
---
id: "sk-YYYYMMDD-slug"
slug: "skill-name"
title: "Skill Title"
status: active
score: 0.0           # [-10.0, 10.0]: >0 = mature, <0 = immature, 0 = unverified
iterations:
  count: 0
  success_count: 0
  fail_count: 0
defects: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

## Body Structure

- `## 离线` — What the user does outside AI conversations.
- `## 在线` — AI-driven: trigger conditions + ordered steps. Each step has `order`, `action`, `note`, `on_failure`.

## Lifecycle

Execute → Evaluate (good/bad) → Update score → Iterate. Score evolves with use.
