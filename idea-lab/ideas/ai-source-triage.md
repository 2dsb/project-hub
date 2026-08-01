---
id: "idea-20260620-ast01"
title: "AI 预筛选学习源（AI source triage）"
tags: [learning, ai-amplifier, flow-based-thinking, information-filtering]
status: raw
created: 2026-06-20
updated: 2026-06-20
source_type: "manual"
source_path: null
importance: 0
permanent_note_material: false
material_since: null
material_expiry_days: 14
promoted_from: null
links: []
related_entities:
  - type: idea
    slug: "flow-based-thinking"
    relation: "applies-framework"
    strength: 0.8
  - type: idea
    slug: "reading-bottleneck"
    relation: "addresses"
    strength: 0.6
  - type: idea
    slug: "ai-amplifier"
    relation: "instance-of"
    strength: 0.5
  - type: idea
    slug: "peer-cross-teaching"
    relation: "sibling-pattern"
    strength: 0.8
  - type: idea
    slug: "learning-pipeline"
    relation: "integrated-into"
    strength: 0.9
  - type: ideas
    slug: "learning-pipeline"
    relation: "concept-relation"
    strength: 0.85
    dimensions: ["concept-relation", "complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "peer-cross-teaching"
    relation: "complement"
    strength: 0.8
    dimensions: ["tag-overlap", "complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "ai-amplifier"
    relation: "complement"
    strength: 0.65
    dimensions: ["tag-overlap", "complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "flow-based-thinking"
    relation: "tag-overlap"
    strength: 0.6
    dimensions: ["tag-overlap"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "reading-bottleneck"
    relation: "complement"
    strength: 0.55
    dimensions: ["complement"]
    bidirectional: true
    source: "auto"
---

# AI 预筛选学习源

## 触发
看 Karpathy Zero to Hero 视频，逐集观看浪费了一定时间。更好的方法是先看 introduction 部分理解目的，再直接读源码。但问题是：不看完视频，无法知道哪些部分值得看。

## 核心想法
在流式思维的学习流中，在源和路由之间插入 AI 预筛选层：

```
源 → AI 预筛选 → 路由 → 汇
```

AI 做的事：提前遍历内容结构，输出"哪些部分值得投入时间，哪些可以跳过/直达源码/看摘要即可"。

## 今天的具体案例
micrograd 视频 — 如果 AI 提前告知"intro 帮你理解目的，之后就是逐行讲 engine.py，你直接读源码更快"，就能跳过中间浪费时间。

## 案例 2：X.com feed
逐个遍历 follow 内容 → 遇到不关注主题（如政策）+ 重复内容 + 过度详细（如 Anthropic safeguard 长篇声称，只需知道要点）。AI 可以同时做**过滤器**（去掉无关主题）和**浓缩器**（重复/过度详细内容压缩为要点）。

## 模式归纳
两类场景共享同一底层：线性遍历信息源效率极低。AI 在用户投入时间前做一轮去噪+压缩。区别仅在于 AI 角色侧重不同：

| 信息源 | AI 角色 | 操作 |
|--------|---------|------|
| 视频课程 | 预筛选 | 判断哪些部分值得看，哪些跳过或直达源码 |
| X.com feed | 过滤器+浓缩器 | 去无关主题 + 压缩重复/冗余内容 |
| 书籍 | 预筛选 | 目录+摘要→指出核心章节，跳过铺垫 |
| 论文 | 预筛选+浓缩 | abstract+intro+结论→核心贡献一句话 |
| 长文 | 浓缩器 | 压缩为要点，标注值得精读的段落 |

泛化核心：任何"需要先投入时间才能判断价值"的信息源，AI 都可以做 triage（分诊）——先于用户遍历，返回价值密度最高的子集。
