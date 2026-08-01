---
id: "sk-20260602-bilingual-reading"
slug: "bilingual-reading"
title: "双语书章节分析"
status: active
score: 0.0
iterations:
  count: 0
  success_count: 0
  fail_count: 0
defects: []
xp: 0
created: 2026-06-02
updated: 2026-06-02
---

# 双语书章节分析

**触发条件**：用户提供英文书章节文本，说"分析这一章""生成阅读笔记""中英对照+约束标注""三层分析"。

**核心原则**：将英文书的一章转化为两份互补文档——(1) 中英对照句级约束标注，让你看清每句话在概念之间建立了什么关系；(2) 三层结构分析，让你看清句子如何组成段落、段落如何组成文章。两份文档加一张可缩放 Mermaid 图，构成完整的章节理解。

**依赖的共享数据层**：
- [shared/constraint-types.md](shared/constraint-types.md) — 24 种概念约束关系类型（词句层）
- [shared/text-structure-types.md](shared/text-structure-types.md) — topic→elaboration 为唯一结构关系 + 语义角色对 + 兄弟关系（句间+段间）
- [shared/structure-constraint-mapping.md](shared/structure-constraint-mapping.md) — 结构↔约束双向映射层
- [shared/mermaid-subgraph-spec.md](shared/mermaid-subgraph-spec.md) — Mermaid 子图输出规范

---

## 离线

**用户职责**：

1. **准备文本**：提供英文书章节的完整文本（告知文件路径或直接粘贴）。如果文本来自特定书籍，告知书名和章节号。
2. **确认输出目录**：默认输出到 `resources/<book-slug>/` 目录下。如果目录不存在，AI 会创建。
3. **标记不确定的标注**：在文档 1 中，对自己不确定的约束标注旁标记"？"，后续可追溯原文验证。
4. **画图检验**：阅读两份文档后，不看原文尝试画出三层图（段间结构→段内句间结构→概念约束关系）。画不出来的就是没真正理解的。
5. **与 inquiry-essay 联动**：如果读后想写相关主题的文章，概念约束图可以直接作为写作输入。

---

## 在线

### 触发时机

- 用户提供英文书章节路径，说"分析这一章""生成阅读笔记"
- 用户说"中英对照+约束标注""三层结构分析"
- 用户粘贴一段英文文本，说"帮我做双语约束分析"

### Steps

- order: 1
  action: "确认输入与输出。\n\n(1) 确认文本来源：用户提供的文件路径或粘贴的文本。如果是文件路径，读取全文并确认章节边界（查找 'CHAPTER X' 标记或用户指定的行范围）。\n\n(2) 确认输出目录：默认 `resources/<book-slug>/`。如果目录不存在则创建。文件命名规则：`ch<章节号>-<章节英文简称>.md`（文档 1）和 `ch<章节号>-<章节英文简称>-structural-analysis.md`（文档 2）。\n\n(3) 如果该章节已有分析文件，询问用户：'已发现该章节的已有分析，是覆盖还是跳过已有部分？'"
  note: "确保文本边界正确，避免截断或混入其他章节内容。"
  execute_skill: null
  skill_args: {}

- order: 2
  action: "文本预处理。\n\n(1) 将英文原文按自然段拆分（以空行/换行为段落边界）。记录每个段落的起止行号。\n\n(2) 在每个段落内，按句拆分（以 . ! ? ; : 为主要分隔符，注意 Mr./Dr./U.S. 等缩写不拆分）。给每句编号（全章连续编号，从 1 开始）。\n\n(3) 统计：总段数、总句数、平均句/段。如果章超过 3000 字，提醒用户并询问是否分段处理。"
  note: "准确的句/段拆分是后续所有分析的基础。特别注意英文缩写、对话中的标点等拆分陷阱。"
  execute_skill: null
  skill_args: {}

- order: 3
  action: "生成文档 1：中英对照 + 句级约束标注。\n\n**结构**：按主题将段落归入若干节（通常 8-20 节），每节有标题。每句一个条目，格式如下：\n\n```markdown\n**1.**\n> [英文原句]\n\n[中文翻译]\n\n`[约束类型]` [约束说明]\n```\n\n**约束标注规则**：\n- 使用 [shared/constraint-types.md](shared/constraint-types.md) 中的 9 种类型标注概念间约束关系\n- 每个约束标注必须包含：约束类型 + 涉及的概念对（≥2 个概念）+ 原文证据（关键短语引用）\n- 无新增约束的句子标注为 `[无约束] 修辞/举例/重复，可加速`\n- 中英对照：翻译要求准确而非优美，保留原文逻辑结构，不添加原文没有的内容\n\n**节末**：每节结束时，生成该节的概念约束子图（Mermaid，仅本节概念节点和约束边）。\n\n**全章末**：生成全章概念约束图（Mermaid，合并所有节）。附加质量提示：孤立节点、矛盾边、密度评估。"
  note: "这是最耗时的一步。核心原则：约束标注不是摘要——不重述句子内容，只标注这一句对概念之间的关系施加了什么约束。中文翻译是为方便快速查阅，不是文学翻译。"
  execute_skill: null
  skill_args: {}

- order: 4
  action: "生成文档 2：三层结构分析。\n\n**零、段落映射表**：将自然段映射到文档 1 的节，标注每节包含哪些自然段和句子编号。\n\n**一、文章层 — 段间结构关系**：\n- 分析节与节之间的结构关系，使用 [shared/text-structure-types.md](shared/text-structure-types.md) 段层级 topic→elaboration 语义变体（thesis→support / problem→solution / abstract→concrete 等，旧标签保留为速记）\n- 格式：`节A → 节B [结构类型]: 关系说明（1-2 句）`\n- 附全文章结构类型总览（缩进层级图）\n- 标注文章的整体论证结构特征（线性/螺旋式/对比式等）\n\n**二、段落层 — 关键句间结构关系**：\n- 在每个节内部，标注相邻句对之间的结构关系，使用 [shared/text-structure-types.md](shared/text-structure-types.md) 语义角色对和兄弟关系（topic→elaboration / claim→evidence / contrast 等）\n- 格式：`句A-句B [结构类型]: 关系说明`\n- 如果 3+ 连续句构成复合结构（如 claim→evidence→analysis 链），标注整组而非逐对标注\n- 修辞句/过渡句/纯举例句可标注为 [无结构边]\n\n**三、三层 Mermaid 子图**：\n- 按照 [shared/mermaid-subgraph-spec.md](shared/mermaid-subgraph-spec.md) Mode A 规范生成完整三层子图\n- 文章层：节子图 + 节间粗边（`==>`）+ 结构类型标签\n- 段落层：句子图节点（可折叠为句组）+ 句间实线边（`-->`）\n- 词句层：概念节点 + 约束边细线（`-->|约束类型|`）\n- 每个节子图内标注句子编号范围\n\n**四、实例级深潜**：\n- 选取 2 组关键段间结构边，按 [shared/structure-constraint-mapping.md](shared/structure-constraint-mapping.md) Section 三格式展示嵌套展开\n- 每组深潜展示：段间结构边 → 内部句间结构 → 内部概念约束 → 原文证据位置\n\n**五、质量评估**：\n- 段间层：覆盖率、连通性、冗余度\n- 句间层：覆盖率、连通性\n- 跨层一致性：段间结构类型与其内部概念约束模式是否匹配（参考 structure-constraint-mapping.md）\n\n**六、结构特征总评**：1-3 段总结本章的论证结构策略和关键结构发现。"
  note: "文档 2 的重点不是重复文档 1 的句级约束，而是展示约束的层级组织——哪些句子和段落出于什么结构目的组合在一起。"
  execute_skill: null
  skill_args: {}

- order: 5
  action: "生成交互式 Mermaid HTML 查看器。\n\n将文档 2 中的三层 Mermaid 子图嵌入一个独立 HTML 文件，包含：\n- 缩放控制（+/- 按钮，20%-300%）\n- 适应屏幕按钮\n- 深色主题（适合长时间阅读）\n- 文件名：`ch<章节号>-graph.html`，放在同目录下\n\nHTML 模板参考已有的 `resources/naked-economics/ch05-graph.html`。"
  note: "Mermaid 子图在 Markdown 中渲染体验差（字体小、无法缩放），HTML 版本是可交互的主要查看方式。"
  execute_skill: null
  skill_args: {}

- order: 6
  action: "输出收尾与项目文件更新。\n\n(1) 告知用户两份文档和 HTML 查看器的路径。\n\n(2) 如果章节属于已有项目（如 naked-economics.md），更新项目文件中对应章节的状态为 ✅ 并添加文档链接。\n\n(3) 给出手动练习建议：'试着不看原文，画出这一章的三层图——先画段间结构，再画段内句间关系，最后填充概念约束。画不出来的地方，回去看文档 1 的对应部分。'\n\n(4) 提醒 inquiry-essay 联动：'如果之后想写与这一章主题相关的文章，这两份文档中的概念约束图和结构图可以直接作为写作的输入。'"
  note: "阅读的终点是理解，理解的检验是能不看原文画出三层图。"
  execute_skill: null
  skill_args: {}

- order: 7
  action: "约束类型库回补。分析完成后，检查本次标注中使用的所有约束类型，与 [shared/constraint-types.md](shared/constraint-types.md) 和 [shared/text-structure-types.md](shared/text-structure-types.md) 中已定义的类型逐一对比。\n\n(1) **列出新出现的约束**：提取标注中使用的、但在两个共享类型库中找不到对应条目的约束标签。区分'概念约束类型'（应进入 constraint-types.md）和'结构关系类型'（应进入 text-structure-types.md）。\n\n(2) **判断是否值得纳入**：\n  - 本次分析中该类型出现 ≥3 次 → 值得纳入（有复用价值）\n  - 出现 1-2 次但含义清晰、未来可能复用 → 可以纳入（标注为'初步'）\n  - 仅出现 1 次且可能是已有类型的变体 → 不纳入，标注为'归入已有类型 X'\n\n(3) **按扩展机制补充**：对决定纳入的新类型，按照对应共享文件的扩展机制（暂停→命名→定义→追加）写入。更新类型库的演进记录。\n\n(4) **更新映射文件**：如果新增了概念约束类型，检查 [shared/structure-constraint-mapping.md](shared/structure-constraint-mapping.md) 中是否需要补充新的结构→约束映射规则。\n\n(5) **告知用户**：列出本次新增了哪些类型、哪些被归入已有类型、哪些暂不纳入及原因。"
  note: "类型库是活的——每次分析都是类型库生长的机会。不要跳过这一步：不把新出现的约束类型写回共享文件，下次分析还会从同样不完整的类型库出发。本步骤也适用于用户说'整理新出现的约束'时独立触发。"
  execute_skill: null
  skill_args: {}

---

## 补充规则

- 英文原文超过 3000 字 → 分段处理，每 1500-2000 字暂停一次，询问"继续下一段？"
- 用户说"只看句级约束，不做结构分析"→ 跳过 Step 4 和 Step 5，仅生成文档 1
- 用户说"只看结构分析，句级已有"→ 跳过 Step 3，仅生成文档 2（但需要引用已有的文档 1 路径）
- 中文翻译风格：以准确传递原文逻辑为优先，不追求文学性。学术/经济类概念保留英文原文在括号中
- 输出文件路径遵循 `resources/<book-slug>/` 惯例，与项目文件 `projects/<book-slug>.md` 对应
- 约束类型和结构类型名称保持中文，Mermaid 图中的边标签可混用中英文简写以保证紧凑
- 与 inquiry-essay 联动：文档 1 和文档 2 的概念约束图可以直接作为 inquiry-essay Step 2 的输入基线
- 本 skill 是 connection-reading.md Mode A 在英文书场景的具体化——如果用户已经在 connection-reading 流程中，不需要重复触发本 skill
