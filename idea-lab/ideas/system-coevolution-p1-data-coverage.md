---
id: "idea-20260606-sce01-p1"
title: "协同进化 - 问题1：数据粒度与覆盖度"
tags: [system-coevolution, data-model, meta-cognition, time-axis]
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
    slug: "conversation-as-data-source"
    relation: "concept-relation"
    strength: 0.85
    dimensions: ["concept-relation", "complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "m34-source-layer-static-rigidity"
    relation: "complement"
    strength: 0.8
    dimensions: ["complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "daily-to-ideas-pipeline-broken"
    relation: "complement"
    strength: 0.7
    dimensions: ["complement"]
    bidirectional: true
    source: "auto"
---

# 协同进化 - 问题 1：数据粒度与覆盖度

## 核心结论

要让系统从数据中涌现结构（而非人预设结构），需要足够密度的原始数据输入。结论是：不需要"更多输入"，而是从已有和自然产生的输入中提取更多信息。

## 统一方案：一张可嵌套的时间轴

边界层和递归层共享同一套记录机制——在时间轴上标记"此刻发生了变化"，区别仅在于分辨率。

```
时间轴（按需展开/折叠）
├── 状态切换：编程 → 阅读
│   ├── 子切换：配置环境 → 核心逻辑 → 重构
│   │   └── 角度转换：思路 A → 思路 B
│   └── 自由字段：有什么异常/摩擦/卡住？
├── 状态切换：阅读 → 运动
│   └── ...
└── ...
```

## 三个数据来源（按利用程度）

### 1. 状态切换记录（边界层）
- **触发点**：从一个状态切换到另一个状态时
- **判断标准**：上一个状态是否"值得记录"
- **输入方式**：对话输入（主通道）；手机端记录或线下模板 + 晚间统一输入（补充）
- **覆盖范围**：行动切换、社交互动、重要决定、思维产出、情绪/精力波动

### 2. 递归子状态记录（内部分解层）
- **机制**：精确到分钟的时间轴打草稿 + 晚间复盘叙述
- **与边界层的关系**：是边界层的细化，不是两套独立流程
- **关键洞见**：打草稿并非对状态的干扰——在打草稿过程中发现价值、进入心流是常见的正向循环
- **风险**：深度沉浸时可能遗漏 → 事后回填 + AI 辅助生成叙述草稿（用户只需修改）
- **负担估算**：5 个状态 × 2 个子切换 = 10 段叙述，每段 2-3 句话，约 15-20 分钟/天

### 3. 对话本身就是数据（已有但未被结构化利用）
- 每一轮对话——问什么、争论什么、在什么话题上停留最久——已经携带大量信息
- 当前状态：对话结束后丢失，未被提取结构化信息

## 覆盖判断

| 生活痕迹类型 | 覆盖 | 说明 |
|---|---|---|
| 行动切换 | 是 | 状态边界触发 |
| 社交互动 | 是 | 切换时回忆刚发生的社交状态 |
| 重要决定 | 是 | 决定往往发生在状态切换点 |
| 思维产出 | 是 | ideas 捕捉 + 递归子状态记录 |
| 情绪/精力波动 | 是 | 切换时评价上一个状态的能量 |
| 状态内摩擦细节 | 是 | 自由字段补足 |
| 微小习惯动作 | 否 | 太细，不值得覆盖 |
| 睡眠/饮食/生理 | 部分 | 有状态切换点可捕捉（起床、饭后） |

## 设计原则

- **在线层最小化中断**：打草稿只需时间戳 + 关键词，不要求完整叙述
- **离线层完成意义建构**：晚间复盘，AI 生成叙述草稿 → 用户修改
- **不要求额外输入**：从已有行为痕迹中提取，而非要求更多记录
- **两张表合并为一张时间轴**：边界和递归是同一结构的不同分辨率
