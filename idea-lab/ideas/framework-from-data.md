---
id: idea-20260604-ffd01
title: 从数据建框架，而非从框架找数据
tags:
- methodology
- meta-cognition
- structure-analysis
- research-method
status: raw
created: 2026-06-04
updated: '2026-07-30'
source_type: null
source_path: null
importance: 0
permanent_note_material: false
material_since: null
material_expiry_days: 14
promoted_from: null
links:
- type: project
  slug: linguistic-structure-analysis
  label: 方法论来源
related_entities:
- type: ideas
  slug: local-pattern-patching-failure
  relation: concept-relation
  strength: 0.95
  dimensions:
  - concept-relation
  - complement
  bidirectional: true
  source: auto
- type: ideas
  slug: practice-to-theory
  relation: complement
  strength: 0.8
  dimensions:
  - complement
  bidirectional: true
  source: auto
- type: ideas
  slug: natural-language-narration-methodology
  relation: concept-relation
  strength: 0.8
  dimensions:
  - concept-relation
  bidirectional: true
  source: auto
- type: ideas
  slug: fix-result-backward
  relation: structural-similarity
  strength: 0.55
  dimensions:
  - structural-similarity
  bidirectional: true
  source: auto
- type: ideas
  slug: consumer-vs-creator
  relation: complement
  strength: 0.5
  dimensions:
  - complement
  bidirectional: true
  source: auto
- type: ideas
  slug: 生活中的结构性理解
  relation: complement
  strength: 0.6
  dimensions:
  - complement
  bidirectional: true
  source: auto
- type: ideas
  slug: 概念的划分
  relation: complement
  strength: 0.5
  dimensions:
  - complement
  bidirectional: true
  source: auto
- type: idea
  slug: natural-language-narration-methodology
  relation: overlap
  strength: 0.6
  dimensions:
  - tag-overlap
  bidirectional: true
  source: auto
- type: project
  slug: linguistic-structure-analysis
  relation: related
  strength: 0.5
  dimensions:
  - tag-overlap
  bidirectional: false
  source: auto
---



# 从数据建框架，而非从框架找数据

## 问题

在语言结构分析项目中，基于 Ch05 P1-P5（21 句）的观察，过早地将 topic→elaboration 升格为"唯一结构关系"。当句26-29 出现不符合这个框架的组织模式（场景构造）时，框架公理碎裂。

根本错误：**用极少的数据（5 段高度论证性段落）建立了一个声称通用的框架。**

## 核心原则

**先积累数据，让模式自然聚类，再建框架。** 不是先定义类型库再找例子验证——那是自我确认。是在足够多的分析实例积累后，回头看出哪些组织模式反复出现、哪些是偶然的。

当前阶段的任务不是建框架，是扩大数据集。

## 具体策略

1. **分析时不套框架**。逐句标注概念约束（24 种类型已证明稳定，可继续使用），每段的组织方式用自然语言描述，不强行归入 topic→elaboration 或任何已有类型。自然语言描述不做术语化。

2. **积累足够数据后再聚类**。至少 3 章完整分析（或等量的其他文本）之后，回头读这些自然语言描述，自然看到的聚类才是真正的句法策略类型。

3. **在数据量达标前冻结框架文件**。constraint-types.md 可以继续生长（回补机制已足够稳定），但 text-structure-types.md 和 structure-constraint-mapping.md 冻结。它们当前的内容存为"Ch05 P1-P5 观察笔记"，不作为通用框架引用。

4. **允许目标模糊**。在数据积累阶段，不需要精确描述终极目标。类比：手里有一块矿石，发现里面有金，自然地想"炼金术的通用理论是什么？"但需要先挖更多矿石，才知道这块矿的金含量是典型还是异常。目标会在数据积累中自己清晰。

## 与语言结构分析项目的关系

这条方法论直接来自 v1→v2 框架重构的教训。v1 基于 5 段数据建立，v2 被 1 个反例动摇。正确的顺序是：扩大分析覆盖 → 自然聚类 → 框架形成。
