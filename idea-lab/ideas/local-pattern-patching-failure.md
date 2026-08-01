---
id: idea-20260604-lppf01
title: 局部规律无法通过不断修正推广到全局
tags:
- methodology
- meta-cognition
- epistemology
- induction
- framework-design
status: raw
created: 2026-06-04
updated: '2026-07-30'
source_type: direct-experience
source_path: projects/linguistic-structure-analysis.md
importance: 0
permanent_note_material: false
material_since: null
material_expiry_days: 14
promoted_from: null
links:
- type: idea
  slug: framework-from-data
  label: 姊妹原则：从数据建框架
- type: project
  slug: linguistic-structure-analysis
  label: 触发场景
related_entities:
- type: ideas
  slug: framework-from-data
  relation: concept-relation
  strength: 0.95
  dimensions:
  - concept-relation
  - complement
  bidirectional: true
  source: auto
- type: ideas
  slug: natural-language-narration-methodology
  relation: concept-relation
  strength: 0.75
  dimensions:
  - concept-relation
  bidirectional: true
  source: auto
- type: ideas
  slug: audit-blind-spot-spec-limitation
  relation: structural-similarity
  strength: 0.65
  dimensions:
  - structural-similarity
  bidirectional: true
  source: auto
- type: literature-notes
  slug: 卡片笔记写作法c1.3
  relation: complements
  strength: 0.5
  dimensions:
  - tag-overlap
  - concept-relation
  - complement
  - structural-similarity
  bidirectional: true
  source: auto
- type: literature-notes
  slug: 卡片笔记写作法c2.2
  relation: complements
  strength: 0.5
  dimensions:
  - tag-overlap
  - concept-relation
  - complement
  - structural-similarity
  bidirectional: true
  source: auto
- type: literature-notes
  slug: 技术的本质c2.2
  relation: complements
  strength: 0.5
  dimensions:
  - tag-overlap
  - concept-relation
  - complement
  - structural-similarity
  bidirectional: true
  source: auto
- type: idea
  slug: three-layer-framework
  relation: overlap
  strength: 0.5
  dimensions:
  - tag-overlap
  bidirectional: true
  source: auto
---


# 局部规律无法通过不断修正推广到全局

## 问题

在语言结构分析项目中，最早的"基本原理"——topic→elaboration 是唯一结构关系——基于 Ch05 P1-P5（5 段高度论证性段落）建立。当句 26-29 出现不符合的段落组织模式（场景构造）时，采用了"不断修正"的策略：在原有模板上添加新条目，试图让框架容纳新情况。

结果：模板越来越复杂（topic→elaboration → topic→elaboration + 场景构造 → + 平行枚举 → + 困境探索...），但并没有变得更"通用"——每一轮修正仍然只是把新的局部现象贴到旧框架上。最终框架变得无法接受与运用。

## 核心判断

**局部规律加上局部规律，不等于全局规律。** 不断修正的每一步，都是在当前框架（一个局部经验的代数表达）上做加法，而不是在更接近全局规律。这类似于在一条曲线上逐点做切线——每一步都拟合了当前点，但整体形状并不收敛到真正的曲线。

正确顺序：先积累足够多样的样本，让模式自然聚类，再归纳框架。归纳发生在数据积累之后，而不是在每一次新数据到来时。

## 具体策略

因为"积累足够样本再总结"这件事本身很困难（需要承受"手里有数据但没有框架"的不确定性），配套设置了一套工作流：

1. **分析阶段禁用框架标签**。逐段用自然语言描述组织方式，不套任何已有术语。
2. **积累门槛**。至少 3 章完整分析（或等量文本）之后，才回头做聚类和归纳。
3. **冻结框架文件**。在数据量达标前，text-structure-types.md 和 structure-constraint-mapping.md 保持冻结，当前内容降级为"Ch05 P1-P5 观察笔记"。

## 与 from-data 想法的关系

`framework-from-data.md` 说的是"应该怎么做"（从数据建框架）。这个想法说的是"为什么旧做法会失败"——不断修正本质上是把归纳和积累倒置：每次新数据不是进入样本池等待聚类，而是直接冲击框架结构。两者是同一方法论转变的正面和反面。
