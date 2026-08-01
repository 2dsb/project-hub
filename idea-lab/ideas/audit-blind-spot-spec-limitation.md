---
id: idea-20260610-ar01
title: 审计盲区：spec对照审查看不到spec本身的缺失
tags:
- meta-cognition
- system-design
- audit
- methodology
- M34
- design-review
status: raw
created: 2026-06-10
updated: '2026-07-30'
source_type: manual
source_path: null
importance: 9
permanent_note_material: false
material_since: '2026-06-10'
material_expiry_days: 30
promoted_from: null
links: []
related_entities:
- type: idea
  slug: m34-source-layer-static-rigidity
  relation: same-pattern
  strength: 0.9
- type: project
  slug: project-hub
  relation: improves-methodology-of
  strength: 0.85
- type: ideas
  slug: four-layer-quality-model
  relation: concept-relation
  strength: 0.9
  dimensions:
  - concept-relation
  - complement
  bidirectional: true
  source: auto
- type: ideas
  slug: local-pattern-patching-failure
  relation: structural-similarity
  strength: 0.65
  dimensions:
  - structural-similarity
  bidirectional: true
  source: auto
- type: ideas
  slug: system-coevolution-p4-self-reinforcement
  relation: complement
  strength: 0.75
  dimensions:
  - complement
  bidirectional: true
  source: auto
- type: ideas
  slug: system-coevolution
  relation: complement
  strength: 0.65
  dimensions:
  - complement
  bidirectional: true
  source: auto
- type: ideas
  slug: nature-of-review
  relation: complement
  strength: 0.55
  dimensions:
  - complement
  bidirectional: true
  source: auto
- type: idea
  slug: four-layer-quality-model
  relation: overlap
  strength: 0.5
  dimensions:
  - tag-overlap
  bidirectional: true
  source: auto
---


# 审计盲区：spec对照审查看不到spec本身的缺失

## 发现过程

M34 经过三轮 recursive-planner 审计（R1: 25发现, R2: 18发现, R3: 14发现），均未发现"模板文本是静态的、不会进化"这一设计缺陷。这个缺陷最终是在用户的一次边缘提问中被发现的："举个例子，suggestion-templates.yaml 中的内容可能会'进化'吗？"

## 根因分析

三层审计标准（M34 自身声明 → 变更成本 → 通用软件原则）能发现 **spec 说了但代码没做的事**，但发现不了 **spec 应该说要没说的事**。

具体来说：
- R017 发现"模板硬编码在 Python 源码中" → R2 提取到 YAML → 标记已解决
- 审计标准判定：原 spec 说"模板应该有格式规范"→ YAML 文件有格式规范 → PASS
- 没有问的问题：**"协同进化"这个名字承诺了什么？模板作为用户最直接感知的系统输出，是否应该也能进化？**

三轮审计的焦点演化也反映了这个盲区：
- R1: 找结构缺失（什么不存在）
- R2: 找回路断裂（什么没连通）
- R3: 找代码错误（什么写错了）
- 没有任何一轮在找：**什么应该进化但被设计成了刚性的**

## 核心洞察

**审计能发现的东西有一个天花板：对照审计只能发现实现和规范之间的差距，不能发现规范本身的缺失。**

要突破这个天花板，需要的是**设计承诺审查**——不看 spec 说了什么，看系统的名称和对外声称的承诺是否被充分实现。

## 避免方法

### 1. 审计标准增加第四层：设计承诺审计

对于每一个声称"可进化"或"可变化"的系统属性，逐一检查：它真的在进化吗？还是只是换了个位置？

### 2. 引入外部质疑者角色（Devil's Advocate）

在审计完成后，一个不看 spec、只看承诺的角色问天真的、外部的问题：
- "你说你在进化。给我三个例子。"
- "还有什么应该进化但没有的？"

### 3. 周期性"承诺-实现"对照

每 30 天列出系统对外声称的所有承诺，用运行时数据验证是否真的在发生。标记"承诺了但没发生"的条目。

### 4. 利用用户的自然提问

用户的天真视角（"这个会进化吗？"）是最高效的检测机制。系统化地将这类提问纳入设计审查流程。

## 关联

- 这是"源层静态僵化"发现的同一种模式：两者都涉及"系统声称的能力和实际能力之间的差距，而这个差距不在 spec 的覆盖范围内"
- 直接改进了项目中枢的审计方法论——不只是 M34 的问题，是所有未来系统审查的问题

## 重要性说明

标注为 importance: 9（最高级），原因：
1. 这不是 M34 的一个局部缺陷，而是**整个审计方法论的结构性盲区**
2. 三轮审计、递减的发现数量给人一种"系统在变好"的安全感，而这种安全感部分地是假的——审计工具本身决定了哪些发现可能出现
3. 如果不修正审计方法，未来所有系统（不仅仅是 M34）都会受同样的盲区影响
4. 修正方法是廉价且可操作的（增加一个审计维度、一个角色、一个周期性检查）

⚠️ Expired without processing, auto-demoted to regular idea (material_since: 2026-06-10, expired: 2026-07-10)
