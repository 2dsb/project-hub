---
id: idea-20260601-8a3b1c
title: 联系人管理系统
tags:
- contacts
- crm
- relationships
- personal-data
status: raw
created: 2026-06-01
updated: 2026-06-01
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
    relation: "学习方法/认知方法论关联"
    strength: 0.5
    bidirectional: true
    source: "migration"
  - type: ideas
    slug: "relationship-modeling"
    relation: "tag-overlap"
    strength: 0.6
    dimensions: ["tag-overlap"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "social-strategy-skill"
    relation: "complement"
    strength: 0.5
    dimensions: ["complement"]
    bidirectional: true
    source: "auto"
---
# 联系人管理系统

记录认识的人，包含字段：
- 姓名
- 电话号码
- 与我的关系
- 身份/职业
- 生日

资源可视度（双向信息不对称问题）：
- 我的问题：我能调动的资源（直接+间接）别人看不到 → 别人不会主动找我
- 别人的问题：我很难判断别人到底有多少"隐藏资源"（他的人脉、技能、信息渠道）
- 撬动二级资源：如何通过直接联系人，触达他们背后更大的资源网络？
  - 例：A 本身帮不了我，但 A 的朋友 B 正好有我需要的东西
  - 关键：让 A 愿意为我打开他的人脉，需要 A 对我有足够信任+对我需求的清晰理解

关系维护功能：
- 核心原则：投其所好——维持联络不靠泛泛的问候，靠"记得对方在意什么"
- 记录对方的兴趣点、关注领域、近期动态，在以下时机自然触达：
  - 生日问候（基础）
  - 看到对方感兴趣的内容（文章、播客、活动、机会）→ 转发 + 一句"想到你可能感兴趣"
  - 对方所在领域的新动态（行业新闻、政策变化）→ 分享 + 问对方怎么看
  - 对方近期提过的困扰/目标 → 后续跟进"上次你说的 XX 怎么样了？"
  - 共同回忆触发（老照片、纪念日、母校新闻）
- 定期联络提醒（如"已 N 个月未联系 X，要发个消息吗？"）——但提醒本身只是触发，联络内容必须基于"投其所好"的记录
- 维护投入分级：核心关系（主动挖掘话题）vs 一般关系（生日+偶发投喂）vs 弱关系（保持可见但不过度投入）

人脉价值化（利用人脉创造价值）：
- 需求对接：询问联系人各自的需求/资源，匹配供需，促成交易或合作，形成三赢（双方获益 + 我获得信息费/人情/关系强化）
- 信息套利：知道 A 懂什么、B 需要什么，撮合信息不对称
- 技能资源共享池：知道谁会什么、谁缺什么，做资源调度者
- 协作撮合：发现共同兴趣/互补技能的人，促成项目合作
- 机会分发：看到机会（工作/项目/资源）时快速匹配到合适的人

目的：认识的人越来越多，需要系统化管理联系人信息，主动维护重要关系，并在维护关系的基础上发掘人脉的潜在价值。

## 可能的 Skill 化方向

本想法可能适合做成"联系人关系维护"类个人 skill，涵盖联系人数据的增删查改、维护提醒、以及人脉价值化的匹配辅助。核心功能可能包括：

- **数据层**：联系人实体（`entities/` 下），包含基础信息 + 兴趣点/关注领域 + 最近动态
- **维护端**：基于"投其所好"原则的智能提醒——不是到日子催你发消息，而是在 AI 浏览到与某联系人的兴趣匹配的内容时主动提示"要不要转发给 X？"
- **价值化端**：需求/资源匹配查询——当用户提到某需求时，AI 检索联系人库中谁可能有相关资源或技能
- **与 daily 集成**：当日有联系人相关事件（生日、回复等待、承诺兑现）时写入 daily 提醒区

此 skill 的复杂度高于其他三个（illness-reframing / knowledge-reconnection / low-energy-cognitive），因为涉及实体 schema 设计、数据存储结构、以及多维度查询。实现前需要先确定联系人实体的字段规范和存储位置。
