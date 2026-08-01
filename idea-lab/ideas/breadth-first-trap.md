---
id: idea-{ts-1748960400-b3d5f2}
title: 广度搜索→深度执行
tags:
- productivity
- information-overload
- execution
- meta-skill
status: raw
classified_tags:
- 可执行类
source_type: manual
importance: 2
permanent_note_material: false
created: 2026-06-03
updated: 2026-06-03
related_entities:
  - type: project
    slug: "ai-ability"
    relation: "生产力/效率方法关联"
    strength: 0.5
    bidirectional: true
    source: "migration"
  - type: ideas
    slug: "flow-based-thinking"
    relation: "complement"
    strength: 0.7
    dimensions: ["complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "goal-singularity"
    relation: "complement"
    strength: 0.6
    dimensions: ["complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "completion-vs-quitting"
    relation: "complement"
    strength: 0.65
    dimensions: ["complement"]
    bidirectional: true
    source: "auto"
  - type: ideas
    slug: "certainty-gravity"
    relation: "complement"
    strength: 0.65
    dimensions: ["complement"]
    bidirectional: true
    source: "auto"
  - type: literature-notes
    slug: "卡片笔记写作法c3.4"
    relation: "extends"
    strength: 0.92
    dimensions: ["tag-overlap", "concept-relation"]
    bidirectional: true
    source: "auto"
  - type: literature-notes
    slug: "优秀的绵羊c6.3"
    relation: "complements"
    strength: 0.62
    dimensions: ["tag-overlap", "concept-relation", "structural-similarity"]
    bidirectional: true
    source: "auto"
---
# 广度搜索→深度执行

## 模式 A：搜索过载（横向）
**症状**：做一件事前打开 15-20 个参考网页（教程/视频/攻略/工具站），脑中多线程切换。

**根因**：用"广度优先搜索"做"深度优先"的事——预判式搜索是焦虑驱动的伪效率，切换成本远超信息价值。

**解法**：
1. **开始前写 3 步链**：不搜任何东西，先用一句话写清步骤链，严格一次只看当前步骤
2. **搜索限流**：搜到结果只开最相关的 1-2 个页面，选源标准：官方文档 > 近期博客 > 视频教程
3. **撞墙才搜**：不预判后面需要什么，先动手，卡住再搜
4. **用 AI 替代多网页**：配置型任务直接问 AI 分步指引

**触发**：打开超过 5 个参考页面 → 关掉全部，写步骤链，回到当前步骤。

---

## 模式 B：依赖嵌套（纵向）
**症状**：想做 X，攻略说需要先做 A；A 需要先做 C、D；C 又需要……整条依赖链在脑中维护，耗尽工作记忆。

**根因**：脑中递归展开依赖树 → 栈溢出。大脑不是终端，不适合维护多层调用栈。

**解法**：
1. **先画依赖树，不执行**：从目标反推，把整棵树写下来。外化 = 卸载认知负荷
2. **从叶子开始执行**：树的最底层叶子 = "现在就能做的事"。做完划掉，自底向上。不需要记住全局，只看"下一个可执行的叶子是什么"
3. **遇到新依赖就挂到树上**：执行中发现新前提条件 → 直接在树上加子节点 → 回到步骤 2

**触发**：脑中嵌套超过 3 层"要先……就要先……" → 停下来，画依赖树。
