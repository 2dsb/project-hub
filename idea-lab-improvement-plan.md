# idea-lab 改进计划（进行中）

状态：Step 3 执行中——190 条 summary 已生成，待计算 connections。

---

## Step 1 — 统一元数据 ✅ 已完成

- [x] 将所有 idea 文件清理为 5 字段 YAML：`id`, `title`, `tags`, `importance`, `connections`
- [x] 生成 `ideas-index.json`

## Step 2 — 合并 permanent-notes ✅ 已完成

- [x] 翻译 66 条 permanent-note，迁移为 idea 格式，丢弃 `0-index`
- [x] 删除 `idea-lab/permanent-notes/`
- [x] 重新生成 `ideas-index.json`

## Step 3 — 计算 Connections 🔧 执行中

### 已完成的准备工作
- [x] 删除 27 个空 body / 无意义文件（217 → 190）
- [x] 清理 44 个文件的旧系统标记（⚠️ / 💡 等）
- [x] 清理所有悬空 connections
- [x] 重新生成 `ideas-index.json`（190 条）
- [x] 第一轮 embedding 试跑（Top-N + Gap Detection），验证方法可行
- [x] 讨论并确定 LLM 摘要方案
- [x] 运行 `generate_summaries.py`，190 条全部成功生成 summary（0 失败）
- [x] 修复：max_tokens 从 300 → 600/1200/2000 渐进重试（DeepSeek v4-pro 推理消耗大）

### 已确定的决策

| # | 决策 | 结论 |
|---|---|---|
| 1 | 方法 | Embedding 相似度（all-mpnet-base-v2）+ Top-N + Gap Detection |
| 2 | 参数 | MAX_CANDIDATES=15, MIN_SCORE=0.45, MAX_SUGGESTIONS=10 |
| 3 | Summary 长度 | ≤100 词，LLM 灵活判断（短文件不凑字数） |
| 4 | Summary 位置 | YAML frontmatter，新 `summary:` 字段 |
| 5 | 嵌入文本 | `title + #tags + summary`（不再用 `body[:300]` 截断） |
| 6 | LLM | DeepSeek v4-pro, API: sk-3578289a53ca446fafde6850cc895e68（用后停用） |
| 7 | SYSTEM_PROMPT | Lyra 优化版（§3 text up to 100 words, 3–6 sentences） |
| 8 | Schema 更新 | 全部做完再统一改 |

### SYSTEM_PROMPT（最终版）

> You are a precise summarization engine for a personal knowledge base.
> Produce a summary in plain English (no markdown, no bullet points, no preamble).
> Output ONLY the summary — never add quotes, labels, or meta-commentary.
> Rules: state core claim directly; compress reasoning as "X because Y, therefore Z";
> include specific terminology; short ideas get short summaries; aim for 3–6 sentences, up to 100 words.

### 下一步

**立即执行：**
```powershell
.venv\Scripts\Activate.ps1
python compute_connections.py
```
- 嵌入文本已改为 `title + #tags + summary`
- MIN_SCORE 暂用 0.45（可能需要根据 summary 质量调高）
- 生成 `connection-suggestions.json`

- [x] 修改 `compute_connections.py`：嵌入文本改为 `title + #tags + summary`
- [x] 调整参数（MIN_SCORE=0.50, MIN_GAP=0.06, MAX_SUGGESTIONS=15, MAX_CANDIDATES=20）
- [x] 运行 `compute_connections.py`，生成 `connection-suggestions.json`（152/190 有建议，共 602 条）
- [x] 142/190 个 idea 接受了 connections（高置信 180 条 + 低置信标记 review 422 条）
- [x] 运行 `write_connections.py` 写回 .md 文件
- [x] 重建 `ideas-index.json`

**之后：**
- [ ] 绘制关系图谱
- [ ] 更新 CLAUDE.md schema 文档（新增 `summary:` 字段）

## Step 4 — 计算 Importance ✅ 已完成

- [x] 选定无向图 PageRank 算法
- [x] 运行 `compute_importance.py`（190 节点，627 边）
- [x] 82 个 idea 自动评分，108 个手动分保留（非 1 值不覆盖）
- [x] 分数缩放至 0–10（一位小数）
- [x] 加入 `maintain.py` 维护链
