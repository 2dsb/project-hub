---
id: "idea-20260606-sce01-p4"
title: "协同进化 - 问题4：防止系统在错误方向上自我强化"
tags: [system-coevolution, self-reinforcement, safety, feedback-control]
status: raw
created: 2026-06-06
updated: 2026-06-06
source_type: "discussion"
source_path: "ideas/system-coevolution.md"
importance: 0
permanent_note_material: false
material_since: null
material_expiry_days: 14
links:
  - type: idea
    slug: "system-coevolution"
    label: "源讨论"
related_entities:
  - type: idea
    slug: "system-coevolution"
    relation: "design-detail"
    strength: 1
  - type: ideas
    slug: "system-coevolution"
    relation: "concept-relation"
    strength: 0.95
    dimensions: ["concept-relation"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "system-coevolution-p3-autonomy-boundary"
    relation: "complement"
    strength: 0.9
    dimensions: ["complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "audit-blind-spot-spec-limitation"
    relation: "complement"
    strength: 0.75
    dimensions: ["complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "four-layer-quality-model"
    relation: "complement"
    strength: 0.55
    dimensions: ["complement"]
    bidirectional: true
    source: "auto"
---

# 协同进化 - 问题 4：防止系统在错误方向上自我强化

## 核心问题

前三个问题的答案——稀疏但有结构的输入、不可解释但可接受的涌现、高度自主的自我修改——合在一起，放大了一个风险：系统可能沿着一个方向持续强化自己，而那个方向恰好是错的。

### 风险来源

- **数据偏差**：系统只看到用户选择记录的东西。如果用户潜意识回避某个领域，它不会出现在数据里
- **确认偏差**：系统基于早期数据形成模式判断后，可能强化与模式一致的信号、抑制不一致的信号——统计学习的自然倾向，非恶意

## 五个防护机制（全部启用）

### 1. 人的否决权（硬约束）
系统任何自我修改都必须留下可回滚的痕迹。用户可以随时撤销上次修改。

### 2. 反向证据的刻意维护
系统必须主动追踪与自身假设相矛盾的数据。例如系统形成"用户对主题 X 高度关注"的判断，必须同时维护计数器："最近 N 天，用户没有产生任何与 X 相关的新数据"。

### 3. 随机探索注入
系统定期向用户推荐与当前认知网络距离最远的实体——那些最不可能产生关联的连接。目的不是正确，而是打破自我强化。

### 4. 周期性归零
每隔一段时间（N 个版本或 M 周），系统从原始数据重新做一次关联分析，完全忽略之前的结果。如果新结果与旧结果有显著偏差，说明中间某处发生了自我强化失真。

### 5. 用户作为最终纠错信号
用户拥有系统永远没有的东西——真实世界体验、直觉、价值观。系统的目标不是越来越"正确"，而是越来越能激发用户产生新的思考。判断标准不是系统建议的准确率，而是用户是否持续产生有价值的想法和行动。
