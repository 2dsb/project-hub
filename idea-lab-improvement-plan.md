# idea-lab 改进计划（进行中）

状态：Step 3 讨论中，执行计划已明确。Step 4 未开始。

---

## Step 1 — 统一元数据 ✅ 已完成

- [x] 将所有 idea 文件清理为 5 字段 YAML：`id`, `title`, `tags`, `importance`, `connections`
- [x] 生成 `ideas-index.json`

## Step 2 — 合并 permanent-notes ✅ 已完成

- [x] 翻译 66 条 permanent-note，迁移为 idea 格式，丢弃 `0-index`
- [x] 删除 `idea-lab/permanent-notes/`
- [x] 重新生成 `ideas-index.json`

## Step 3 — 计算 Connections 🔧 讨论完成，待执行

### 已执行的准备工作
- [x] 删除 27 个空 body / 无意义文件（217 → 190）
- [x] 清理悬空 connections
- [x] 重新生成 `ideas-index.json`（190 条）
- [x] 第一轮 embedding 试跑（Top-N + Gap Detection），验证方法可行

### 已讨论的决策

| # | 决策 | 结论 |
|---|---|---|
| 1 | 方法 | Embedding 相似度（all-mpnet-base-v2）+ Top-N + Gap Detection |
| 2 | 参数 | MAX_CANDIDATES=15, MIN_SCORE=0.45, MAX_SUGGESTIONS=10 |
| 3 | Summary 长度 | 80-100 词，LLM 灵活判断 |
| 4 | Summary 位置 | YAML frontmatter，新 `summary:` 字段 |
| 5 | 嵌入文本 | `title + #tags + summary`（不再用 `body[:300]` 截断） |
| 6 | Schema 更新 | 全部做完再统一改 |

### 执行流程

**Step 0 — 清理历史痕迹**
- [ ] 扫描所有 190 条 idea 的 body
- [ ] 删除旧系统标记：`⚠️ Overdue and unprocessed — automatically downgraded...`
- [ ] 删除旧系统标记：`💡 Promotion recommendation...`
- [ ] 保留真实内容，只去标记

**Step 1 — 生成 LLM 摘要**
- [ ] 写脚本，逐条读取 idea 文件（title + tags + body）
- [ ] 传给 LLM，生成 ≤100 词英文 summary
- [ ] 对空 body 文件（已删除 27 个，确认无遗漏）：不再特殊处理

**Step 2 — 写入 Summary**
- [ ] 将生成的 summary 作为 `summary:` 字段加入每个文件的 YAML frontmatter
- [ ] 更新 `compute_connections.py`：嵌入文本改为 `title + #tags + summary`

**Step 3 — 明确 compute_connections 逻辑**
- [ ] 向用户清晰解释执行逻辑（读什么 → 怎么算 → 输出什么）
- [ ] 根据 summary 质量调整参数（MIN_SCORE 可能需要从 0.45 调高）

**Step 4 — 运行 compute_connections.py**
- [ ] 生成新的 `connection-suggestions.json`
- [ ] 用户审核建议

**之后**
- [ ] 修改 `compute_connections.py`，自动更新 `ideas-index.json`
- [ ] 绘制关系图谱

## Step 4 — 计算 Importance ⏳ 未开始

- [ ] 讨论方法
- [ ] 实现
- [ ] 写回 .md 文件 + 重新生成 index

---

## 未来

- 更新 CLAUDE.md schema 文档
- 关系图谱可视化
