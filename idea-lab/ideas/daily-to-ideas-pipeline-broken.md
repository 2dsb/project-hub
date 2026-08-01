---
id: "idea-20260609-dp01"
title: "daily→ideas 管道缺失：每日想法未自动提取"
tags: [process, pipeline, M34, daily-note, idea-extraction]
status: raw
created: 2026-06-09
updated: 2026-06-09
source_type: "manual"
source_path: null
importance: 5
permanent_note_material: false
material_since: null
material_expiry_days: 14
promoted_from: null
links: []
related_entities:
  - type: idea
    slug: "m34-source-layer-static-rigidity"
    relation: "instance-of"
    strength: 0.85
  - type: idea
    slug: "flow-based-thinking"
    relation: "affected-by"
    strength: 0.7
  - type: ideas
    slug: "m34-source-layer-static-rigidity"
    relation: "complement"
    strength: 0.8
    dimensions: ["complement", "structural-similarity"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "conversation-as-data-source"
    relation: "complement"
    strength: 0.75
    dimensions: ["concept-relation", "complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "system-coevolution"
    relation: "complement"
    strength: 0.7
    dimensions: ["concept-relation", "complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "system-coevolution-p1-data-coverage"
    relation: "complement"
    strength: 0.7
    dimensions: ["complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "chat-as-idea-source"
    relation: "complement"
    strength: 0.7
    dimensions: ["complement"]
    bidirectional: true
    source: "auto"
---

# daily→ideas 管道缺失：每日想法未自动提取

## 发现
06-09 查看协同进化系统时，发现昨日（06-08）daily note 中的 7 个想法全部未提取为独立 idea 文件。最新 idea 停留在 06-06。

## 具体案例
06-08 daily note 有 7 个想法，其中"流式思维框架"明确标记为"值得独立保存的思维工具"，且已有 `resources/thinking-tools/flow-based-thinking.md`，但 ideas 目录中无对应条目。

## 影响
- 想法只在 daily note 中存在，不被 M34 感知（daily note 是实体，但其中的"想法"子条目不是独立实体）
- 知识轴扫描、模式检测、建议生成均无法触及这些想法
- 日常最有价值的认知产出滞留在日记中，无法进入知识体系

## 根因
不存在 daily note → ideas 的自动或半自动提取流程。用户必须手动执行"将 daily note 中的想法提取为 idea"这一操作——而这个操作没有被任何 system/skill/reminder 所覆盖。

## 可能的改进方向
1. 每日收尾时自动检测 daily note 中的"想法"区块，提示用户确认提取
2. 或：将 idea 实体的 source 概念扩展，允许 daily note 的子条目被直接引用
3. 或：在 `start` 流程中加入"昨日想法补录检查"步骤
