# 文本结构类型库

> 共享于 [connection-reading.md](../connection-reading.md) 和 [inquiry-essay.md](../inquiry-essay.md)。阅读是解网（提取结构+约束），写作是织网（编码结构+约束）——同一个类型库，两个方向。本文档定义**结构层面**的关系类型，与 [constraint-types.md](constraint-types.md) 定义的概念约束关系（词句层面）互补且正交。

---

## 框架总览

```
结构关系（1 种，递归）:
  topic → elaboration

语义角色（N 种，开放）:
  topic 的角色: problem / claim / cause / effect / general / abstract / ...
  elaboration 的角色: solution / evidence / effect / cause / specific / concrete / ...

兄弟关系（3 种）:
  contrast / sequence / concession
```

---

## 一、topic → elaboration（唯一结构关系）

topic→elaboration 是文本组织的**唯一结构关系**，在所有层级上递归出现（详见[分形结构](#topicelaboration-的分形结构)）。其余一切标签——无论是旧的"句间结构类型"还是旧的"段间结构类型"——本质上都是 topic 和 elaboration 节点的**语义角色**，或 elaboration 块内部兄弟节点的**连接方式**。

### 父子轴

```
topic ── elaboration ── sub-elaboration ── ...
  ↑           ↑               ↑
  problem    solution        evidence
  claim      evidence        example
  general    specific        data
  cause      effect          mechanism
  ...
```

topic 的语义角色描述了"这个 topic 是什么类型的陈述"。elaboration 的语义角色描述了"它在用什么方式展开这个 topic"。结构关系始终是 topic→elaboration——不同的语义角色对只是填充了不同的内容。

### 兄弟轴

同一个 elaboration 块内部，多个并列的 elaboration 句子之间可能存在兄弟关系：

```
topic
  ├── elaboration A  ←→ [contrast] ←→  elaboration B
  ├── elaboration C  → [sequence] →    elaboration D
```

兄弟关系不推翻"唯一结构关系是 topic→elaboration"——它们和 topic→elaboration 不在同一个轴上。父子轴是层级（嵌套），兄弟轴是同层（连接）。
### 角色变异：自封闭 topic 与闭合性终端
标准 topic→elaboration 角色分配：topic 提出问题/锚定话题，elaboration 展开答案。但在实际文本中，topic 和 elaboration 终端偶尔偏离这一默认分工。
两个变异成对出现——自封闭 topic 制造了 elaboration 的"晋升"，闭合性终端为该晋升提供了收束方式。
#### 自封闭 topic (self-closing topic)
**定义**：topic 句在内部完成了本应委托给 elaboration 的因果/解释工作。topic 不仅锚定话题，还嵌入了答案。
**偏离**：标准 topic 只提问（"这是什么？""为什么会发生？"），elaboration 负责回答。自封闭 topic 把答案也吞了——"这事会发生，原因是 X"。elaboration 不再回答 topic 提出的问题（那个问题 topic 自己答完了），而是被提升到更高层操作：验证（确认确实如此）、深化（分析为什么无解）、裁决（这意味着什么）。
**识别信号**：topic 句内部出现因果标记（"because""which is too X to Y""the reason is"），且后续 elaboration 不重复该因果链。
**实例**（Ch05 P5 句 18）：
```
"which is just too alluring to go away"
→ [因果] 直觉吸引力 → 反复复活，在 topic 句内部闭合
→ elaboration（句19-21）不解释"为什么反复"，而是确认+深化+裁决
```
**与标准 topic 的对比**：
| 维度 | 标准 topic | 自封闭 topic |
|------|-----------|-------------|
| topic 包含什么 | 话题锚点 | 话题 + 因果答案 |
| elaboration 做什么 | 回答问题 | 验证 + 深化 + 裁决 |
| elaboration 依赖 topic 的程度 | 话题方向 | 断言内容（elaboration 默认 topic 的答案为真） |
#### 闭合性终端 (closing terminal)
**定义**：elaboration 块的末句不展开主题，而是宣告论证结束。它不添加新信息，而是对已完成的论证施加一个外部/上位视角的终止标记。
**偏离**：标准 elaboration 终端要么锚定（P1 的 $75,000）、要么暴露（P2 的隐藏前提）、要么平行对比（P3 的退出↔加入）、要么补充证据（P4 的耶鲁取消）。这些都是 elaboration 的内部操作——它们**展开**主题，只是以不同方式。闭合性终端不是展开——它是**终止 elaboration**。
**识别信号**：末句引用外部权威做价值裁决（而非提供新证据/新分析），且裁决的语言压缩了整个论证弧线的两端（如"Radical and Terrible"分别对应诱惑力和必然失败）。
**实例**（Ch05 P5 句 21）：
```
The Atlantic: "Very Radical and Very Terrible"
→ 不是展开——裁决是 metacognitive 操作，"这个讨论结束了"
→ "Radical" = P1-P2 的论证重量（诱惑力）
→ "Terrible" = P3-P5 的论证重量（必然失败）
→ 裁决者不是作者——外部视角封死论证弧线
```
**与标准 elaboration 终端的对比**：
| 维度 | 标准终端 | 闭合性终端 |
|------|---------|-----------|
| 操作性质 | 展开（exposition） | 终止（closure） |
| 是否添加新信息 | 是（锚定数字/隐藏前提/新证据） | 否（压缩已完成的论证） |
| 与 topic 的关系 | 服务于 topic 的展开 | 服务于论证的结束 |
| 视角 | 内部（作者继续论证） | 外部（引用权威来封口） |
#### 两种变异的配对逻辑
自封闭 topic 和闭合性终端成对出现并非巧合——topic 封了口（答案内置），终端就必须封口（裁决终止），否则论证会"漏"：如果 topic 自己回答了问题但终端还在展开新维度，topic 的内置答案就不构成真正的闭合。topic 封口 + 终端封口 = 完整闭合。中间夹着的 elaboration（验证+深化）服侍的不是 topic 提出的问题，而是 topic 做出的断言。
判定流程：
1. topic 句是否在内部包含因果/解释标记？→ 是：自封闭 topic
2. 末句是否引用外部裁决且不添加新信息？→ 是：闭合性终端
3. 两者同时出现？→ 自封闭-闭合对，elaboration 被整体提升为"断言验证"而非"问题回答"

### elaboration 终端功能

elaboration 块的末句不仅收束本段——它决定这个块在更大层级中的角色如何被定义。终端不是"结尾"，是 elaboration 语义块向更高层级暴露的**接口**。

五种已识别的终端功能（Ch05 P1-P5）：

| # | 终端类型 | 实例 | 向内操作 | 向外操作（层级接口） |
|---|---------|------|---------|-------------------|
| 1 | 锚定 | P1 $75,000 | 把抽象因果链蒸馏为可感知的数字 | 为 P2 提供可计算的前提（"高收入者还款多"） |
| 2 | 暴露隐藏前提 | P2 句9 对称假设 | 在自证闭环完成后暴露脆弱点 | 为 P3 提供攻击面——跨段 contrast 的具体断裂点 |
| 3 | 平行对比 | P3 句13↔14 | 把两翼并置，展开后对称收束 | 为 P4 的命名提供完整的机制画面（两翼都已展示） |
| 4 | 证据+额外 | P4 句17 | 验证+延伸，两信息可分离 | 为 P5 提供可验证的事实锚点（"耶鲁实验取消了"），P5 不再需要复述理论 |
| 5 | 闭合性终端 | P5 句21 | metacognitive 裁决，终止论证 | 不向下一段暴露接口——seal 而非 interface。Section 结束 |

**终端与 elaboration 驱动模式的对应**：

| 驱动模式 | 终端功能 | 为什么是这个终端 |
|---------|---------|----------------|
| staircase（逐对依赖） | 锚定 | 长链需要一个重量级终点，否则论证悬浮 |
| 独立+共生环（自证闭环） | 暴露隐藏前提 | 闭环太完美——需要暴露脆弱点，为反转留口 |
| 自组织因果（因果展开因果） | 平行对比 | 两翼不能合并——对称本身就是结论 |
| funnel（三维独立） | 证据+额外 | 漏斗底部天然是"验证层" |
| 自封闭 topic + 嵌套对 | 闭合性终端 | topic 封口→终端也必须封口（成对变异） |

**接口 vs 封口**：前四种终端的共性是 formatted output——elaboration 块把自己的输出格式化为下一块的输入。闭合性终端打破这个模式——下一段不在同一个论证弧线内（或根本没有下一段），所以不需要向下暴露接口。它做的事不是 interface 而是 seal。

**验证方式**：把每种终端换到另一种驱动模式上，看会不会别扭。锚定接到 P5 上（"Oregon 计划每年还款 $X"）——别扭，因为 P5 在宣布模式必然性，不需要具体数字。终端功能不是自由选择——是 elaboration 驱动模式要求了它。
---

## 二、语义角色对（旧 12 种类型的归位）

原 Level A 的 12 种"句间结构类型"实际上是 topic→elaboration 在不同语义场景下的填充。它们可以全部表示为 topic 角色 → elaboration 角色的组合：

| # | 旧标签 | topic 角色 | elaboration 角色 | 说明 |
|---|--------|-----------|-----------------|------|
| 1 | topic→elaboration | definition / claim | example / detail / definition | 旧类型中的"原型"——topic 和 elaboration 未指定具体语义 |
| 2 | claim→evidence | claim | evidence（数据/引文/实例） | A 在逻辑上依赖 B 来确立真实性 |
| 3 | evidence→analysis | evidence | analysis（解读/推论） | B 解释 A 的含义或引申推论 |
| 4 | general→specific | general（一般陈述） | specific（具体个案） | B 让 A 变得可感知，A 本身不需证明 |
| 5 | specific→general | specific（具体案例） | general（一般规律） | B 从 A 中归纳出规律 |
| 6 | cause→effect | cause（原因） | effect（结果） | 因果链沿时间或逻辑方向推进 |
| 7 | effect→cause | effect（结果） | cause（原因） | 先宣布结果再追溯原因 |
| 8 | restatement | statement（原陈述） | restatement（重述） | B 用不同措辞重述 A，通常伴随细微细化 |
| 9 | transition | summary（收束） | preview（预告） | A 收束当前，B 预告下一段方向 |

其中 #2-#8 是 elaboration 方式的不同语义填充，#9（transition）是 topic→elaboration 在段落边界处的特殊形式——旧段的收束作为"铺垫"，新段的起始作为"展开"。

**语义角色表是开放的**——随着阅读量增加，可能发现新的 topic 角色（如 dilemma、hypothesis、concession 作为 topic）和新的 elaboration 方式，直接追加角色名，不需要新增"结构类型"。


**委托模型的局限性**：语义角色对隐含一个前提——topic 把解释/证明/细化的工作委托给 elaboration。当 topic 不委托（如自封闭 topic 内置了因果答案），elaboration 接收不到标准委托时，第一层的语义角色对无法准确描述该段的结构。P5 句18 最接近 `claim→evidence`（topic=claim），但偏离了该角色对的前提——topic 不是"需要证据支撑的可质疑断言"，而是"已经自带答案的断言"。elaboration 被解除了解释义务，被提升为验证+深化+裁决。P5 句21 同样偏离——不是 evidence 回答"凭什么信你"，而是裁决宣告"讨论到此为止"。这不是选错了角色对——是委托模型本身被悬置了。当识别到自封闭 topic + 闭合性终端的成对出现时，不强行归入第一层语义角色对，应用第三层（驱动模式）+ 第四层（终端功能）的分析框架。
**旧标签仍可作为速记使用**：`claim→evidence` 比"topic(claim)→elaboration(evidence)"简洁，标注时可以继续用旧格式，但理解上应将其视为语义角色对而非独立结构类型。

---

### 易混淆辨析：`general→specific` vs `claim→evidence`

这两个类型都涉及"B 让 A 更具体"，但核心功能不同。判断标准不是"B 是否比 A 具体"，而是 **A 在逻辑上是否依赖 B 来确立其真实性**。

| 维度 | general→specific | claim→evidence |
|------|------------------|----------------|
| **核心功能** | 解释（exposition） | 说服（argumentation） |
| **B 回答的问题** | "这个一般性描述具体长什么样？" | "我凭什么相信你说的？" |
| **A 的独立地位** | A 本身不需要证明（已被接受或自明） | A 是一个可被质疑的断言，需要支撑 |
| **去掉 B 后的效果** | A 仍然成立，只是不够直观 | A 的信用悬空，读者可能不信 |

**实例对比**（均来自 Naked Economics Ch05）：

- `general→specific`：句 7 描述定价公式（"你可以用平均工资算出还款百分比"）→ 句 8 给出脑外科医生 vs. 多哥抗病者的具体例子。公式本身是数学自足的——你不需要例子来证明公式可以计算，例子只是让你看到计算落实在人身上的效果。
- `claim→evidence`：句 4 断言"大额债务迫使毕业生做好（赚钱）而非行善"→ 句 5 给出 $75,000 贷款当不了老师的例子。这是一个可被质疑的规范性断言（"真的吗？有没有可能两者兼顾？"），例子需要出来支撑它。

**判定流程**：遇到疑似情况时，先问——如果读者对 A 说"我不信，你拿什么证明"，B 能不能回应这个挑战？如果能 → `claim→evidence`；如果读者的反应不是"不信"而是"不太明白，举个例子"→ `general→specific`。

### 复合模式：`general↔specific` 共生环

`general→specific` 和 `specific→general` 是方向可逆的一对类型。当它们在同一文本单元内**连续出现**（形成 general→specific→general 或 specific→general→specific 的序列），会产生超出各自标签加总的涌现功能。

**为何成立闭环**

general 和 specific 互相为对方提供信用，缺一不可：

| 方向 | 功能 | 缺了反向会怎样 |
|------|------|---------------|
| general → specific | 让抽象可感知 | 没有反向收束，specific 沦为孤例——"你只是碰巧找了个支持的例子" |
| specific → general | 让个例获得普遍意义 | 没有反向奠基，general 沦为空洞——"说得对但跟我有什么关系" |

general 给 specific **意义**（"这个例子在说明一个规律"），specific 给 general **血肉**（"这个规律在现实中真实发生"）。

**与 `cause→effect` 的本质区别**

因果是**方向锁定的**——不能交换原因和结果。但 general 和 specific 是**方向可逆的**——概括→具体和具体→概括都可以是合法的论证推进。正因为方向可逆，它们才能形成闭环而不显重复。

**实例**（Ch05 P2，句 7-8-9）

```
句7（操作性的 general: 定价公式，"怎么算"）
  ↓  general→specific
句8（specific: 脑外科医生 vs. 多哥抗病者）
  ↓  specific→general
句9（结论性的 general: 平均抵消～收支平衡，"为什么成立"）
```

三句构成**自证闭环**：公式→例子证明了公式不是空壳，例子→结论证明了个例不是孤例。句 7 和句 9 都是 general 但不重复——句 7 回答 how（操作），句 9 回答 why（结论）。经过句 8 的具体化，句 9 比句 7 多了一层被检验过的分量。

**与定义三角的区别**：共生环是线性的（general→specific→general，三个节点串联，首尾是不同内容），定义三角是闭合的（名字/一般定义/实例 三个节点两两之间有不同的结构关系，靠语义等价闭合）。共生环回答"为什么要相信"，定义三角回答"这个词到底是什么意思"。详见下文「定义三角」。

**标注约定**

当检测到 general↔specific 连续成环时，在逐对标注之外附加：

```
[general↔specific 共生环: 句A→句B→句C]
```

这不是一个新的关系类型，而是一个**涌现属性**——标识作者在抽象和具体之间往返而非单向推进。它的存在本身就是一个信号：此处的论证密度高于普通单向段落，句子之间不仅仅是"谁展开谁"的线性关系，而是互相增强的有机整体。

### 复合模式嵌套：块级结构 + 共生环

当放射状 elaboration 块内部恰好包含一个共生环时，形成**两层嵌套**：

```
外层 — 块级放射状：
  句A [topic]
    ↓
  {句B, 句C, 句D} [elaboration]

内层 — elaboration 块内部：
  [general↔specific 共生环: 句B→句C→句D]
```

两层之间是**互相依赖**的关系：

| 层 | 提供什么 | 缺了它会怎样 |
|----|---------|-------------|
| 外层（块级） | 给内层一个**共同目标**——三句话都在回应同一个 topic，不是随意堆砌 | 不知道这三句话为什么放在一起 |
| 内层（共生环） | 给外层一个**内部结构**——三句话之间不是平行罗列，而是互相增强的有机整体 | 不知道三句话之间有什么化学反应 |

**实例**（Ch05 P2，句 6-9）

```
外层：句6 [topic: "能自融资"] → {句7, 句8, 句9} [elaboration]
内层：[general↔specific 共生环: 句7→句8→句9]

嵌套后的完整标注：
  句6 [topic] → {句7, 句8, 句9} [elaboration]
    句7: 操作性的 general — 定价公式（how）
    句8: specific — 极端个例（what it looks like）
    句9: 结论性的 general — 收支平衡（why）
    → [general↔specific 共生环: 句7→句8→句9]
```

**设计含义**：块级表示（放射状结构）提供了**嵌套的语法**——它允许在一个结构边内部展开次级关系。共生环提供了**嵌套的内容**——它是块内可能出现的涌现模式之一。两者的设计是互相配合的：块级表示使得发现共生环成为可能（逐对标注下你不会想到去看 7-8-9 是否构成闭环），而共生环的存在使得块级表示不只是"把并列项打包"的便利标记，而是揭示了块内真正的组织结构。

这不是唯一可能的嵌套组合。块内还可能出现其他涌现模式（如 contrast+concession 形成的对立→调和闭合），当发现新模式时，遵循同样的思路——先标注块级主结构，再标注块内涌现模式，最后描述两层之间的相互依赖关系。

---

## 段间关系：不是独立类型

原 Level B 定义了 12 种"段间结构关系"。经 Ch05 P1-P5 全弧线验证，它们可以全部归入框架已有的两个层级：

### 归入 topic→elaboration

这些"段间类型"只是 topic→elaboration 在段层级的语义变体——topic 和 elaboration 被赋予了特定的语义角色，但结构关系本身不变：

| 旧 Level B 标签 | 实际是什么 | 语义角色 |
|-----------------|-----------|---------|
| thesis→support | topic→elaboration | topic = 论点，elaboration = 支撑 |
| problem→solution | topic→elaboration | topic = 问题，elaboration = 方案 |
| question→answer | topic→elaboration | topic = 问题，elaboration = 回答 |
| background→foreground | topic→elaboration | topic = 背景，elaboration = 前景 |
| abstract→concrete | topic→elaboration | topic = 抽象理论，elaboration = 具体应用 |
| concrete→abstract | topic→elaboration | topic = 具体案例，elaboration = 一般规律 |
| synthesis→conclusion | topic→elaboration | topic = 综合，elaboration = 结论 |

它们不是七种不同的结构关系——是 topic→elaboration 在七种语义场景下的应用。区分"problem→solution"和"question→answer"有意义的是内容分析，不是结构分析。

### 归入语义角色对/兄弟关系（跨尺度应用）

这些"段间类型"就是语义角色对和兄弟关系，只是连接的单元从句子变成了段落（或段群）：

| 旧 Level B 标签 | 等同于 | 说明 |
|-----------------|--------|------|
| contrast | 句间 contrast | 兄弟 elaboration 块之间的对立——P2（理论建立）↔ P3（机制崩塌） |
| claim→counterclaim | 句间 contrast | 两个段群之间的立场对立 |
| counterclaim→rebuttal | 句间 concession | 反方段群 → 驳斥段群 |
| comparison | 句间 contrast | 两个段落之间的并置比较 |
| chronological | 句间 sequence | 跨段的时间/步骤序列 |

### 剩余

| 旧 Level B 标签 | 归入 |
|-----------------|------|
| digression | 不是结构关系——是主题偏离标记，属于内容分析而非结构分析 |

### 结论

段间不需要独立的类型库。**层级树 + 语义角色对/兄弟关系已经覆盖了段间关系**——兄弟 elaboration 块之间的关系就是兄弟关系在较大粒度上的应用，父子块之间的关系就是 topic→elaboration。

---

## 段落断点

段落断点不创造新的结构关系类型，但它**改变关系的分量**。同样的结构关系，落在段内和落在段边界上，论证体验不同。

### 段落断点的升级效应

以句间 contrast 为例：

```
不升级（段内 contrast）：
  句13（退出）↔ 句14（加入）
  → "这两个方向不同"——读者理解为一组平行对比

升级（跨段 contrast）：
  P2 句9（break even）→ [段落断点] → P3 句10（no hope of working）
  → "上一段建立的全部理论信心在此被推翻"——读者体验为论证方向反转
```

段落断点把 contrast 从"相邻内容的差异"升级为"整个论证块的对立"。这不是新的类型——它仍然是 contrast——但它在 topic 层级树中标记了一个**重要分支点**：从这个断点开始，树的一侧（建立）和另一侧（推翻）构成了全论证中最粗的一对兄弟分支。

### 段落断点 = 树中的分支标记

```
Layer 3: 一、Hope 奖学金
  ├── P1-P2 (理论建立)         ← 分支
  │     ├── P1
  │     └── P2
  ├── P3-P4 (机制崩塌)         ← 分支（段落断点在此）
  │     ├── P3
  │     └── P4
  └── P5 (模式确认)            ← 分支
```

每个段落断点都是 topic 层级树中的一个分叉。不是所有分叉都等重——跨段 contrast 标记的分叉比段内句间 contrast 的分叉重，因为它连接的是更大的 elaboration 块。

### 为什么作者在特定位置插入段落断点

| 功能 | 说明 | 例子 |
|------|------|------|
| 升级论证转折 | 段内 contrast → 跨段 contrast，论证方向反转 | P2→P3 |
| 将收束转化为起跑 | 把命名放在新段首，从前段的"终点"变成新段的"起点" | P3→P4（句15 回顾型命名） |
| 标记论证层次 | 大 topic 下的子 elaboration 块用段断点分开 | P1/P2（定义/理论） |
| 节奏控制 | 长段后短段 = 加速，短段后长段 = 减速 | P5 四个短句快速收束 |

### 标注中的处理

段落断点本身不是结构类型——不需要在边标中新增标签。它的作用是**提示标注者检查**：

1. 断点两侧的兄弟 elaboration 块之间是否有语义角色对或兄弟关系（contrast、cause→effect 等）？
2. 该关系是否因为段落断点而具有比段内同类型关系更大的论证分量？
3. 断点是否位于 pivot 位置（如 P4 的回顾型命名）？

如果三个问题的答案都是"是"，在树的对应分叉处标注分量升级。

---


## 标注约定：链式结构与放射状结构

### 问题

现有的 24 种类型均采用**逐对标注**（句A→句B，段A→段B），隐含假设结构关系是线性传递的。但实际文本中存在两种不同的组织方式：

- **链式结构**：句1 → 句2 → 句3 → 句4，每句话主要依赖前一句话，论证逐层推进
- **放射状结构**：一个 topic sentence 辐射到多句 elaboration，各句独立回应 topic，句间无强依赖

逐对标注在链式结构中成立，但在放射状结构中会**扭曲实际组织**——把并列的 elaboration 强行串成接力链，让人误以为句子是线性传递的。

### 块级表示

当段落存在明显的 topic sentence 且后续句子共同构成 elaboration block（而非接力链）时，使用块级表示：

```
句A [topic] → {句B, 句C, 句D} [elaboration]
  句B: [该句在块内的角色——从哪个维度展开 topic]
  句C: [该句在块内的角色]
  句D: [该句在块内的角色]

  [块内句间关系]（可选——仅当句子间存在有意义的局部承接时才标注）
  句B-C [类型]: [说明]
```

### 判定标准

**删除测试**：删除句A后，句B 是否仍然有意义地承接于句C？

- 链式：句B 依赖句A，句C 依赖句B——删除中间任一句会打断论证流
- 放射状：句B、C、D 各自独立回应句A——删除句B 不影响句C 对句A 的展开

**实例对比**（均来自 Naked Economics Ch05）：

| | P1（句 1-5，依赖有序 elaboration） | P2（句 6-9，独立 elaboration） |
|---|---|---|
| 结构 | 句1 [topic] → {句2→句3→句4→句5} [elaboration: 依赖有序] | 句6 [topic] → {句7, 句8, 句9} [elaboration: 独立] |
| 删除测试 | 删句2，句3（投行家 vs 社工）悬空——读者不知道还款机制，无法理解为什么投行家要多付 | 删句7（定价公式），句8（脑外科 vs 多哥抗病者）仍可直接回应句6——你不需要知道公式也能理解交叉补贴的逻辑 |
| 维度分工 | what→how→why→anchor，顺序不可重排 | how / what / why，顺序可重排 |
| 块内关系 | 逐对依赖链：general→specific → cause→effect → claim→evidence | 共生环：[general↔specific 共生环: 句7→句8→句9] |

### Elaboration 块的两种内部组织

`topic → {elaboration block}` 的主结构确定后，elaboration 块内部存在两种不同的组织逻辑：

**依赖有序 elaboration（staircase）**

后续句之间存在强顺序依赖，维度层层下钻，删除中间任一句会打断论证流。标注时块内关系使用逐对依赖链：

```
句A [topic] → {句B→句C→句D} [elaboration: 依赖有序]
  句B: [维度1 —— 必须先建立此维度，后续句才能展开]
  句C: [维度2 —— 依赖句B提供的前提]
  句D: [维度3 —— 依赖句C的推论]
```

依赖有序 elaboration 有两种子形态：

**staircase 型**（P1, P3）：维度层层下钻靠前维度的**内容**提供后维度的前提——必须知道还款机制（句2）才能理解投行家多付（句3），必须知道方向判断（句12）才能理解退出/加入（句13-14）。

**funnel 型**（P4）：维度依次下钻靠的是**逻辑先后**而非内容传递——必须先知道是什么（句15后半句），才能推导导致什么（句16），然后用实证锚定（句17）。三个维度共享同一个外部 pivot（句15前半句）作为唯一 topic，维度间的排序来自"定义→后果→实证"的逻辑顺序，而非前一个维度的内容提供了后一个维度的前提。

| | staircase (P1, P3) | funnel (P4) |
|---|---|---|
| 排序驱动力 | 前维度内容 → 后维度前提 | 逻辑先后（定义→后果→实证） |
| topic 来源 | 段内产生 | 外部（前段论证蒸馏出的名字） |
| 删除中间句 | 打断论证流 | 打断逻辑流——后果没了原因，实证没了待证对象 |
| 每个维度与 topic 的关系 | 间接——通过前维度连接到 topic | 直接——每个维度各自回应 topic |

funnel 型有两个已观测变体：

| 变体 | 维度序列 | topic 来源 | 实例 |
|------|---------|-----------|------|
| 定义→后果→实证 | 操作性定义 → 因果后果 → 实证锚定 | 外部 pivot（前段蒸馏的名字） | P4 |
| 实例→分析→裁决 | 具体实例 → 结构分析 → 权威裁决 | 段内自锚定（句内断言+嵌入因果） | P5 |

**独立 elaboration（spokes）**

各句独立回应 topic，各句承担不同的语义角色（如一个给 example、一个给 evidence），删除任一句不影响其他句对 topic 的展开。块内若存在组织结构，来自涌现模式（如共生环）或兄弟关系（contrast/sequence），而非顺序依赖：

```
句A [topic] → {句B, 句C, 句D} [elaboration: 独立]
  句B: [维度1]
  句C: [维度2]
  句D: [维度3]
  → [涌现模式: ...]（可选）
```

**判定**：删除 elaboration 块的中间句——剩余句子是否仍能各自独立回应 topic？能 → 独立；不能 → 依赖有序。

### 句与维度的非一对一关系

块级表示中用句编号作为维度标签仅为便利，实际上一句可以承载**多个并列的 elaboration 维度**。elaboration 的单元是概念操作，不是句子。

**实例**（Ch05 P1，句 2）

```
句 2: "Students could borrow money ... repay ... with a percentage of their annual income
       rather than the usual fixed payments of principal plus interest."

一个句子，两个独立的概念操作：
  [定义] what it is — 收入比例还款机制
  [对比] what it is not — 非传统固定还款
```

两者各自独立地回应 topic（"Hope 奖学金是什么"）。定义从内部建立概念，对比从外部建立边界。不是一个服务于另一个——缺了对比，读者只知道机制长什么样但不知道它相对于什么来说是新的。

**标注格式**：多维度句在块内拆分为多行，每行标注约束类型：

```
句A [topic] → {句B, 句B, 句C} [elaboration: ...]
  句B [定义]: what it is — ...
  句B [对比]: what it is not — ...
      ↳ 两个并列维度共驻于同一句
  句C: ...
```

**适用范围**：依赖有序和独立 elaboration 块都可能出现多维度句。独立块中的多维度句（两个维度各自独立回应 topic）进一步强化了放射状特征；依赖有序块中的多维度句则为后续句提供了更丰富的承接基础。

### 涌现模式：定义三角

当名字、一般定义、具体实例三个节点两两之间形成不同结构关系且靠语义等价闭合时，构成**定义三角**（definitional triangle）。三个节点分别是：

- **名字（label）**：概念名称——"这被称为什么"
- **一般定义（general definition）**：操作性定义——"这意味着什么"
- **具体实例（specific instance）**：名字所归纳的具体例子——"这看起来是什么样的"

**三边关系**：

```
具体实例 ── specific→general ──→ 名字
    ↑                               │
    │  (语义等价: 同一内容,          │ topic→elaboration
    │   不同抽象层级)                │
    │                               ↓
    └── general→specific（隐含）── 一般定义
```

| 边 | 关系 | 方向 | 说明 |
|---|---|---|---|
| 实例 → 名字 | specific→general | 归纳 | 从具体实例中提取概念标签 |
| 名字 → 一般定义 | topic→elaboration | 展开 | 标签被操作性内容填充 |
| 一般定义 → 实例 | general→specific（隐含） | 验证 | 一般定义的每个要素都能在实例中找到对应 |

**闭合效应**：名字概括了实例，定义展开了名字，实例又是定义的实例化。不需要外部证据，三个节点互相支撑——定义被自证。读者通过走完三角的三个边而对概念建立完整理解。

**与共生环的关键区别**：

| | 共生环 | 定义三角 |
|---|---|---|
| 拓扑结构 | 线性（A→B→C，三点串联） | 闭合（三点两两相连） |
| 推动力 | general 和 specific 互相提供信用 | 语义等价——三个节点是同一内容的不同抽象层级 |
| 回答的问题 | "为什么要相信这个规律？" | "这个词到底是什么意思？" |
| 首尾关系 | 首尾是两个不同的 general（操作性的 vs. 结论性的） | 首尾语义等价（实例 = 一般定义的具体化） |
| 实例 | P2 句7→8→9 | P4 句13-14 + 句15前半句 + 句15后半句 |

**标注格式**：

```
[涌现模式: 定义三角 — 句A, 句B, 句C]
  句A（具体实例）: ...
    ↓  specific→general
  句B（名字）: ...
    ↓  topic→elaboration
  句C（一般定义）: ...
    ↓  general→specific（隐含）
  句A  ← 与句C语义等价

  三角闭合效应: [说明三个节点如何互相支撑]
```

**判定条件**：

1. 存在一个被命名的概念（名字节点）
2. 该名字从前面演示的具体实例中归纳而来（specific→general）
3. 名字后面紧跟操作性定义（topic→elaboration）
4. 操作定义的要素能在具体实例中找到对应——即实例和定义是语义等价的

**注意**：定义三角是跨句/分句的涌现模式——实例和名字可能跨段（句13-14在P3，句15在P4），名字和定义可能在同一个句子的两个分句中（句15前半句/后半句）。它的三个节点跨越了段落边界和分句边界，因此逐句标注不会发现它。

### 嵌入因果（句内 cause→effect）

当因果链不跨越句对而封装在单个句子内部时，称为**嵌入因果**。后半句是前半句的原因（或反过来），不需要后续句来建立因果关系。

**识别**：句内出现 because/since/which is why 等因果连接词，或逗号/破折号后的分句携带前句的原因。

**标注**：
```
句A [topic]: "断言 + 嵌入因果"
  前半句: 断言（如"不会消失"）
  后半句: 原因（如"too alluring"）—— [因果]（已显式, 嵌入）
    ↳ 嵌入因果不等后续句证明——断言自带原因
```

**实例**（Ch05 P5句18）：
```
"Bill Clinton was not the last to dally with this idea, which is just too alluring to go away."
  前半句: "not the last" — 断言模式反复
  后半句: "too alluring" — 嵌入因果 — 直觉吸引力→反复复活
```

**与 cause→effect 句间结构的区别**：句间 cause→effect 把因果链展开为两个论证单元，句 A 是原因、句 B 是结果（或反过来）。嵌入因果把因果链压缩为单句内的两个分句，在 topic 锚定时一并给出——"不仅说是什么，还说为什么"。

### 形式-内容重合

当句子的**句法结构**恰好表演了它所描述的**概念结构**时，称为形式-内容重合。这不是结构关系或概念约束，而是**语法形式和语义内容的同构**——句子的构造方式本身就是论证的一部分。

**识别信号**：
- 嵌套结构（括入/递归）恰好描述嵌套或递归概念
- 并列结构恰好描述对比或并列概念
- 重复结构恰好描述重复或循环概念

**实例**（Ch05 P5句19）：
```
"Pay It Forward, which was a rewarmed version of the HOPE Scholarship
 (which was a rewarmed version of the Yale plan)."

嵌套括号的句法结构：Pay It Forward → (HOPE → (Yale))
概念内容：翻版套翻版 = 模式复现
→ 句法嵌套表演了概念的嵌套递归——形式即内容
```

**标注**：在概念约束标签后追加"形式-内容重合"标记，说明句法形式如何映射概念内容。

### 与逐对标注的共存规则

两种标注可以共存于同一段落：

1. **先判定主结构**：该段是否有 topic sentence？后续句是 elaboration block 还是接力链？
2. **用块级表示标注顶层关系**：`topic → {elaboration block}`，标注块类型（依赖有序 / 独立）
3. **再填充块内次级关系**：依赖有序块用逐对依赖链，独立块检查是否存在涌现模式

不要将依赖有序 elaboration 强行表示为独立，也不要把独立 elaboration 强行压缩为逐对链。块级表示提供统一的顶层语法，块类型区分内部的两种组织逻辑。

### 段间层级的适用

放射状结构同样出现在段→篇层面。例如，引言段可能同时作为多个主体段的 thesis，这些主体段之间没有线性顺序依赖：

```
P1 [thesis] → {P2, P3, P4} [support]
  P2: 经济论据
  P3: 历史先例
  P4: 道德论证
```

判定标准相同：删除 P1 后，P2→P3 之间是否有有意义的承接？如果三个主体段各自独立支撑引言段的论点，则是放射状；如果 P3 建立在 P2 的论证之上，则是链式。

### 句内分句间结构

topic→elaboration 和语义角色对同样适用于**句子内部的分句之间**。当分号、冒号或破折号将一句分为两个有独立论证功能的半句时，两个半句之间可以存在与句间相同的 topic→elaboration 关系及其语义填充。标注时前缀 `句内` 以区分粒度：

```
前半句（topic）: "..."
  ↓  [句内 topic→elaboration]
后半句（elaboration）: "..."
```

**与句间结构的关系**：句内分句间结构不替代句间结构——它们是**嵌套的**。一句内部的分句关系完成之后，整句作为一个单元参与它与相邻句的句间结构。标注时先标注句内结构，再标注整句在段落中的句间关系。

**实例**（Ch05 P4句15）：
```
句15 [定义]（回顾型命名）
  前半句: "The result is called adverse selection" — 回顾性指针
    ↓  [句内 topic→elaboration]
  后半句: "sort themselves in or out based on private information" — 操作性定义
整句 → 句16 [cause→effect]: 回顾型命名 → 后果追溯
```

**粒度边界**：仅在分句具有独立论证功能时使用句内标注。逗号分隔的并列短语、非限制性定语从句等不构成独立论证单元，不需要句内标注。

### 复合结构叠加：cause→effect + claim→evidence

当作者用因果链的终端产物作为该因果链的实证时，同一条结构边上同时存在两种结构关系：**cause→effect**（事件之间的因果关系）和 **claim→evidence**（作者引用后果来确认逻辑推演的真实性）。两者不是竞争关系，也不是独立的边——它们是同一条边上叠加的两个视角。

**叠加条件**：证据恰好是因果链的结果。即句B的内容同时满足：
1. 它是句A所描述机制的逻辑后果（cause→effect）
2. 它的真实发生确认了句A逻辑推演的正确性（claim→evidence）

**与普通 claim→evidence 的区别**：普通的 claim→evidence 中，证据是外部引入的（如数据引用、第三方案例），与主张之间没有因果必然性。叠加模式中，证据就是因果链本身在现实中的实例——主张的机制必然产生某结果，这个结果确实发生了。

**叠加的暴露效应**：当证据包含一个不参与因果链的因素时，叠加反而让两种关系的边界变得可见。如 P4句17 中"行政成本高昂"只参与 claim→evidence（为计划失败提供额外证据），不参与 cause→effect（句16的因果链没有产生它）——两个因素在证据句中共存但角色不同，恰好暴露了叠加的存在。

**标注格式**：
```
句A → 句B [cause→effect + claim→evidence（叠加）]
      ↳ cause→effect: [说明因果链]
      ↳ claim→evidence: [说明举证功能]
      ↳ 叠加条件: [证据如何恰好是因果链的终端产物]
```

**实例**（Ch05 P4句16→17）：
```
句16 → 句17 [cause→effect + claim→evidence（叠加）]
      ↳ cause→effect: 逆向选择机制因果地导致耶鲁实验还款不足
      ↳ claim→evidence: 耶鲁实验的还款不足确认了句16逻辑推演的真实性
      ↳ 叠加条件: "还款低于预期" = 定价模型崩溃的实例
      → 行政成本只参与 claim→evidence，不参与 cause→effect
```

**注意**：这不是一个新的结构关系类型——它是两个语义角色对在特定条件下的共存。在标注时使用 `+` 连接两个类型名来标记叠加。如果叠加模式在更多文本中被反复观测到，可考虑提升为正式复合模式。

#### 跨尺度叠加

复合叠加不限于句间。当作者的论证同时在做两件事（展开话题 + 推进因果链），且两条线在同一个终端节点汇合时，叠加可以出现在跨段长弧上。P3句11 → P4句15（5句跨度）同时承载 topic→elaboration 和 cause→effect，叠加条件相同——因果链恰好是 elaboration 的展开形式。

叠加的**本质**不是两个标签贴在一起，而是作者的论证具有双重目的。叠加的**尺度**（句间/跨段）取决于两条线汇合需要多长的论证弧——因果链短则句间叠加，因果链跨越整段则跨段叠加。两种尺度的叠加可以出现在同一文本中（如 Ch05 P3→P4 跨段叠加 + P4 句16→17 句间叠加），形成嵌套的叠加结构。

---

## topic→elaboration 的分形结构

topic→elaboration 是文本组织的**底层语法**，在所有层级上自相似地重复出现。语义角色（cause→effect、claim→evidence、general→specific 等）是 elaboration 块**内部**的展开方式——它们回答"这个 elaboration 以什么形式推进"，但外层壳始终是 topic→elaboration。

### 四层自相似

以 Ch05 P1-P5（第五章第一节）为例，topic→elaboration 同时在四个层级出现：

```
Layer 3 — 段群
  P1-P2 [topic: Hope 奖学金的设计与理论]
    │
    └── P3-P5 [elaboration: 设计为什么失败 + 失败的必然性]

Layer 2 — 段间
  P3 [topic: 信息不对称]
    │
    └── P4 [elaboration: 信息不对称的结果——逆向选择]
          │
          └── P5 [elaboration: 逆向选择的必然——模式反复]

Layer 1 — 段内（五段各有一个 topic→elaboration 块）
  P1: 句1 [topic] → {句2-5} [elaboration]
  P2: 句6 [topic] → {句7-9} [elaboration]
  P3: 句11 [topic] → {句12-14} [elaboration]
  P4: 句15前半句 [topic] → {句15后半句, 16, 17} [elaboration]
  P5: 句18 [topic] → {句19-21} [elaboration]

Layer 0 — 句内分句
  句15: 前半句 [topic] → 后半句 [elaboration]
```

四个层级使用**同一种结构关系**——topic→elaboration。区别只在于 topic 和 elaboration 的粒度：在 Layer 3 它们是多段群，在 Layer 2 是段落，在 Layer 1 是句子，在 Layer 0 是分句。这不是偶然类比——是同一组织原则在不同尺度上的递归应用。

### topic 是层级位置，不是句子属性

同一句话可以同时是 topic 和 elaboration——取决于你在看哪个层级：

```
句15前半句
  Layer 3: elaboration（它是 P3-P5 elaboration 块的一部分）
  Layer 2: elaboration（它是 P4 段的内容，P4 是 P3 的 elaboration）
  Layer 1: topic（它是 P4 段内 elaboration 块的 topic）
  Layer 0: topic（它是句15内部 前半句→后半句 的 topic 端）
```

"topic"不是某句话的内在标签——它是在特定层级上"被后续内容展开"的那个节点。同一句话在更高层级是 elaboration（被包裹），在更低层级是 topic（包裹别人）。这是分形结构的核心含义：**每个节点向上看是 elaboration，向下看是 topic**。

### 语义角色在 elaboration 块内部的使用

Elaboration 块内部的句子连接方式由语义角色对描述——每个句子承担一种 elaboration 角色，相对于它的前一句或相对于 topic：

- P1 elaboration 块内部：general→specific → cause→effect → claim→evidence（staircase）
- P2 elaboration 块内部：general→specific → specific→general（共生环）
- P3 elaboration 块内部：cause→effect → contrast（自组织因果，contrast 在此为兄弟关系）
- P4 elaboration 块内部：cause→effect → cause→effect+claim→evidence（funnel）
- P5 elaboration 块内部：claim→evidence → specific→general → evidence→analysis+claim→evidence（funnel）

每一段的 elaboration 块内部可以使用不同的语义角色组合——但每一段的外壳（父子轴）始终是 topic→elaboration。语义角色描述的是"这个 elaboration 句在用什么方式展开"——它可以是 cause/effect/evidence/example/specific/general 等，角色表开放。

### topic 层级树

将文本递归切分为 topic→elaboration 后，所有 topic 节点形成一棵树：

```
一、Hope 奖学金与逆向选择
  ├── P1: "Hope 奖学金" — 方案定义
  │     └── P2: "能自融资" — 理论支撑
  ├── P3: "信息不对称" — 机制揭秘
  │     ├── P4: "逆向选择" — 机制命名 + 后果
  │     │     └── P5: "会反复出现" — 模式确认
  │     └── [P4 内部]
  │           └── 句16: 因果后果
  │                 └── 句17: 实证
  └── [P1 内部]
        └── 句3: 投行家vs社工
              └── 句4: 债务→职业约束
                    └── 句5: $75,000 锚定
```

这棵树的**根**是全文节（"一、Hope 奖学金与逆向选择"），**叶子**是终端句（不再被任何句展开的句子，如句5、句17、句21）。任意两个节点的结构关系 = 它们在树中的位置关系：兄弟节点可能是 cause→effect 或 contrast，父子节点始终是 topic→elaboration。

### 分析方法：先建树，再填内部关系

1. **递归切分**：从最大层级开始（全文 → 段群 → 段 → 句），在每个层级识别 topic 句和它的 elaboration 块边界。判定标准：删除候选 topic 后，后续内容是否失去被组织的目的？
2. **构建 topic 树**：将所有 topic 节点按父子关系连接。父 = 被展开者，子 = 展开者（子同时也是下层 elaboration 的 topic）。
3. **填充语义角色**：在 elaboration 块内部，标注句子间的具体展开方式（cause→effect、claim→evidence、contrast 等语义角色对和兄弟关系）。这些只在块内部有意义——跨块的句子不直接比较。
4. **标注跨块涌现模式**：检查是否存在跨块的 contrast、共生环、定义三角等——这些不在树的父子/兄弟关系中自动出现。

**与旧方法的区别**：旧方法是"逐对判断语义角色对"——把所有句子对当作平等的候选项，逐一标注。新方法是"先建 topic→elaboration 树，再在块内部填充语义角色"——先确定骨架，再描述血肉。前者容易把 topic→elaboration 当作语义角色对中的一种来和其他角色混合标注；后者承认它是不同层级的东西——唯一的结构关系 vs. 多样的语义填充。

---

## 扩展机制

当遇到无法用 topic→elaboration 树 + 已有语义角色对/兄弟关系解释的结构模式时：

1. **暂停**：确认这确实是一个新的语义角色对或兄弟关系，而非已有类型的变体。先尝试用 topic→elaboration 树 + 已有类型的组合来解释。
2. **命名**：用"source→target"的格式命名语义角色对，或为新的兄弟关系命名。
3. **定义**：写出含义、典型模式（一组例句）、识别信号词（如有）。
4. **追加**：将新类型加入本文件对应章节（语义角色表或兄弟关系表）。

**不再区分段间类型**：原 Level B 已并入 topic→elaboration（语义变体）+ 语义角色对/兄弟关系（跨尺度应用）。新发现的关系若连接的是段落/段群而非句子，不需要新增"段间类型"——它是已有类型的跨尺度应用，或 topic→elaboration 在新语义场景下的表现。

类型库是**活的**——随着阅读量的增加，新的语义角色对和涌现模式会被发现。任何一方（connection-reading 阅读方向、inquiry-essay 写作方向）发现的新类型，自动适用于另一方。

---

## 结构图结构

**节点**：`{文本单元引用（如 "P1" 或 "P2 句3"）, 摘要?}` — 被分析的文本片段及其简要概括

**边**：`{源节点 → 目标节点, 结构关系类型（topic→elaboration / 语义角色对 / 兄弟关系 / 段间语义变体）, 证据信号?}` — 有向结构关系，证据信号为可选字段，记录识别该关系所依据的语言/结构线索

---

## 结构图质量指标

- **覆盖率 (Coverage)** = 实际标记的结构边数 / 可能的句对/段对数。衡量论证结构被完整映射的程度。低覆盖率提示分析不够深入，有大量潜在的句子/段落关系未被识别。
- **连通性 (Connectivity)** = 至少参与一条结构边的句子/段落所占百分比。孤立单元过多（<50%）提示文本整合度弱，或分析遗漏了大量关系。
- **层次深度 (Hierarchy Depth)** = 从篇章→段落→句子的嵌套层数。一致的深度暗示作者有意为之的结构设计；深度跳跃（某层缺失）可能是分析盲区或文本结构薄弱处。
- **冗余度 (Redundancy)** = 同一对文本单元之间存在多条同类型结构边。提示该单元的结构功能不清晰——它在论证中可能同时承担多个角色，需要重新审读。

---

## 与概念约束的关系

本文档定义**结构关系**——topic→elaboration 树（所有层级的骨架）+ 语义角色对（elaboration 块内部的展开方式）+ 兄弟关系（并列节点的连接方式）。[constraint-types.md](constraint-types.md) 定义**概念约束关系**（概念与概念之间）。两者正交：

- 一篇文章可以结构清晰但概念约束稀疏（修辞多于论证），也可以概念约束密集但结构散乱（论证力强但组织弱）。
- 完整分析需要两套类型库同时工作：topic→elaboration 树告诉你"骨架怎么搭的"，语义角色对告诉你"elaboration 内部怎么推进的"，概念约束告诉你"作者到底说了什么"。
- 两套类型的关系映射见 [structure-constraint-mapping.md](structure-constraint-mapping.md)（双向映射层）。

---

## 演进记录

| 日期 | 变更 | 来源 |
|------|------|------|
| 2026-06-02 | 创建：24 种结构关系类型（Level A 12 种 + Level B 12 种）+ 标注约定（链式/放射状/块级表示）+ 易混淆辨析 + 共生环复合模式 | recursive-planner Step 2 |
| 2026-06-02 | 新增：句与维度的非一对一关系 + 多维度句标注格式 | Ch05 P1句2 实战发现 |
| 2026-06-03 | 新增：句内分句间结构 — Level A 类型适用于句子内部的分句之间 + 复合结构叠加 cause→effect + claim→evidence — 当证据恰好是因果链终端产物时的叠加模式 + 跨尺度叠加 — 叠加可跨段出现 | Ch05 P4 句15-17 深潜发现 |
| 2026-06-03 | 新增：涌现模式 — 定义三角（名字/一般定义/具体实例 三点闭合，语义等价驱动） | Ch05 P4 句13-14 + 句15 深潜发现 |
| 2026-06-03 | 新增：依赖有序 elaboration 的两种子形态 — staircase 型（内容驱动）vs funnel 型（逻辑先后驱动，共享外部 pivot） | Ch05 P4 深潜发现 |
| 2026-06-03 | 新增：funnel 型两个变体（定义→后果→实证 / 实例→分析→裁决）+ 嵌入因果 + 形式-内容重合 | Ch05 P5 深潜发现 |
| 2026-06-03 | 新增：topic→elaboration 的分形结构 — 四层自相似（段群/段间/段内/句内）+ topic 是层级位置不是句子属性 + 壳层/核层二分（同日被终极简化替代）+ topic 层级树 + 分析方法（先建树再填内部关系） | Ch05 P1-P5 全弧线观测 |
| 2026-06-03 | 简化：Level B 废除 — 原 12 种段间类型归入 topic→elaboration（语义变体）+ 核层类型/语义角色对（跨尺度应用，同日被终极简化替代）+ 新增段落断点功能（升级效应/分支标记/标注处理） | Ch05 P1-P5 全弧线观测 |
| 2026-06-03 | 终极简化：框架头重写 — topic→elaboration 为唯一结构关系（1 种）+ 旧 12 种类类型降级为语义角色对（N 种，开放）+ 兄弟关系（3 种: contrast/sequence/concession）+ 全文引用更新 | Ch05 P1-P5 全弧线观测 |
| 2026-06-04 | 新增：角色变异 — 自封闭 topic (self-closing topic) + 闭合性终端 (closing terminal)。两种变异成对出现：topic 内置因果答案迫使 elaboration 从"回答问题"晋升为"验证+深化+裁决"，终端从"展开"变异为"闭合"。判定流程与配对逻辑。 | Ch05 P5 深潜发现 |
| 2026-06-04 | 新增：elaboration 终端功能 — 五种终端类型（锚定/暴露隐藏前提/平行对比/证据+额外/闭合性终端）+ 终端与驱动模式的对应 + 接口 vs 封口 distinction + 语义角色对委托模型的局限性（自封闭 topic 与闭合性终端悬置委托模型时第一层角色对失效） | Ch05 P5 深潜发现 |
