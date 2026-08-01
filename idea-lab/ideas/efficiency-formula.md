---
id: idea-20260512-ef01
title: 效率提升的双路径——逐步更新 vs 系统性更新
tags:
- productivity
- self-improvement
- methodology
- system-design
status: developed
created: 2026-05-12
updated: 2026-06-04
source_type: null
source_path: null
importance: 0
permanent_note_material: false
material_since: null
material_expiry_days: 14
promoted_from: null
related_entities:
  - type: project
    slug: "ai-ability"
    relation: "方法论关联"
    strength: 0.5
    bidirectional: true
    source: "migration"
  - type: project
    slug: "project-hub"
    relation: "项目管理系统优化关联"
    strength: 0.5
    bidirectional: true
    source: "migration"
  - type: ideas
    slug: "increasing-time"
    relation: "complement"
    strength: 0.9
    dimensions: ["complement", "concept-relation"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "meta-skill-efficiency"
    relation: "concept-relation"
    strength: 0.8
    dimensions: ["concept-relation", "complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "integrating-fragmented-life-strategies"
    relation: "complement"
    strength: 0.65
    dimensions: ["complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "low-energy-ideation"
    relation: "complement"
    strength: 0.6
    dimensions: ["complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "iteration-in-life"
    relation: "complement"
    strength: 0.55
    dimensions: ["complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "methodology-change-timing"
    relation: "complement"
    strength: 0.5
    dimensions: ["complement"]
    bidirectional: true
    source: "auto"
  - type: literature-notes
    slug: "卡片笔记写作法c3.4"
    relation: "complements"
    strength: 0.62
    dimensions: ["tag-overlap", "concept-relation", "complement", "structural-similarity"]
    bidirectional: true
    source: "auto"
---
# 效率提升的双路径——逐步更新 vs 系统性更新

## 原始想法（2026-05-12）

成果 = 效率 × 时间。每天 80% 时间完成任务，20% 时间提高效率。

## 修正（2026-06-04）

80/20 时间分配不现实。实际上，"做任务"和"提效率"并非两个独立时间块——它们**同时发生**。

提效率有两种截然不同的路径：

### 路径一：逐步更新（嵌入式）

在执行过程中自动沉淀。不需要单独分配时间。

**流程**：做事情 → 记录为 idea 或 skill → idea 经迭代验证 → 固化为 skill → 效率自然提升

**特征**：
- 与执行同步，不抢占执行时间
- 颗粒度小，每次只改进一个点
- 依赖系统有沉淀机制（idea → skill 管道、评价→固化循环）
- 本质是**在执行中学习**

**实例**：
- 做完一套二模 → 记录错题归因方法 → 固化为"错题复盘 skill"
- 发现某个 Anki 背诵顺序效率低 → 调整顺序 → 记录为 skill 改进
- 每天使用 project-hub → 发现摩擦点 → 记录为需求 → 下次版本迭代修复

### 路径二：系统性更新（跃迁式）

需要专门停下来思考。重构方法论本身或系统的底层架构。

**特征**：
- 需要跳出日常执行，以 meta 视角审视
- 颗粒度大，一次改变影响整个系统
- 频率低但每次影响深远
- 本质是**对学习方法的学习**，或**对系统的系统设计**

**实例**：
- v3→v4 自动化重构（不是修一个 bug，是改变整个执行机制）
- 约束类型库从 9 种扩展到 24 种（不是加一个类型，是重新理解"什么是约束"）
- 80/20 模型本身被推翻（本次修正）
- 对 project-hub 架构的大版本升级

### 两者的关系

```
逐步更新（日常）──────────→ 量变积累
    │                            │
    │ 暴露模式、积累张力          │ 达到临界点
    ↓                            ↓
系统性更新（偶尔）──────────→ 质变跃迁
    │                            │
    │ 改变底层规则                │
    └────────────────────────────┘
        反馈到日常执行中
```

- 逐步更新是**执行过程中的自然排泄**——不需要意志力，系统会自动捕获
- 系统性更新是**对逐步更新积累的张力的回应**——当小的修补不再够用时，就需要重构底层
- 两者不是对立的，而是同一个反馈循环的两个相位

### 实践含义

1. **不要为"提效率"专门预留时间块**。大部分提效率已经在执行中完成了（逐步更新）。
2. **但要识别"系统性更新"的触发信号**：当你连续多次做同类小修补、或对现有框架反复感到不适时，说明该停下来做一次系统性反思了。
3. **系统性更新的时机**：不要在冲刺期做（如考前 3 天不应重构学习方法论）。利用自然间歇——项目收尾后、版本完成后、低能量日（做不了执行但可以做思考）。

## 与现有系统的关系

- `ideas/` + `skills/` 管道 = 逐步更新的基础设施
- project-hub 版本升级（v1→v6.3）= 系统性更新的产物
- `methodology-change-timing.md`（L1/L2/L3 模型）= 系统性更新的**时机限制**——L3（操作层）禁止在关键时期更换
