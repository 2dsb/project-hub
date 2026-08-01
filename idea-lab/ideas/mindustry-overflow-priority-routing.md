---
id: idea-20260608-mo01
title: Mindustry 溢流门优先级路由
tags:
- Mindustry
- logistics
- priority-routing
- overflow-gate
- game-design
status: raw
created: 2026-06-08
updated: '2026-07-30'
source_type: daily
source_path: daily/2026-06-08.md
importance: 0
permanent_note_material: false
material_since: null
material_expiry_days: 14
promoted_from: null
links: []
related_entities:
- type: ideas
  slug: mindustry-resource-routing
  relation: concept-relation
  strength: 0.85
  dimensions:
  - tag-overlap
  - concept-relation
  bidirectional: true
  source: auto
- type: ideas
  slug: flow-based-thinking
  relation: migration
  strength: 0.8
  dimensions:
  - migration
  bidirectional: true
  source: auto
- type: idea
  slug: mindustry-resource-routing
  relation: overlap
  strength: 0.429
  dimensions:
  - tag-overlap
  bidirectional: true
  source: auto
---


# Mindustry 溢流门优先级路由

## 场景
炮塔群 + 基地共存，资源优先级 弹药 > 回收

## 方案
溢流门（优先直行，塞满溢出）/ 反向溢流门（优先侧出，塞满直行）串联实现优先级路由

先给炮塔供弹，炮塔弹药满后自动溢出运回基地

## 优化方向
优先级梯子 — 溢流门级联，直行=高优先级，侧出=低优先级，资源自动从上往下填。炮塔前加缓存箱（vault/container）平滑波次震荡。
