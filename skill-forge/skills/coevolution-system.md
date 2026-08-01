---
id: "sk-20260606-coe"
slug: "coevolution-system"
title: "协同进化系统"
status: active
score: 0.0
iterations:
  count: 0
  success_count: 0
  fail_count: 0
defects: []
xp: 0
created: 2026-06-06
updated: 2026-06-06
depends_on: ["sk-20260606-era"]
---

# 协同进化系统（M34，扩展 M33）

**核心功能**：在 M33 实体关系分析系统的静态关联基础上，构建三层动态协同进化能力——模式检测（Layer 1）、建议生成（Layer 2）、效果追踪（Layer 3）——基于统一可嵌套时间轴数据模型，实现"检测→建议→追踪→反馈权重调整→更新检测"的完整闭环。

**设计原则**：AI-native 系统——所有分析逻辑是行为规范（prompt/procedure），由 Claude Code 在触发时执行。系统观察相关性，不声称因果性（P2）。所有自主修改可逆（M-1）。emergent domain 定期重置防止先验漂移（M-4）。

---

## 离线

本系统在用户不直接交互时自动运行（日常 start sync 扩展 + 周日全量扫描），但以下职责需要用户主动执行：

用户职责：
1. **审批高优先级建议**：每日 start sync 内联呈现高优先级建议时，决定接受、拒绝或稍后处理。系统最多呈现 3 条，避免过载
2. **定期查看系统状态**：通过 `coevolution status` 命令或直接阅读 `resources/coevolution/state.md`，了解当前模式检测数量、建议采纳率、domain prior 权重分布和反自强化机制运行状态
3. **手动触发周期重置**：当建议出现重复或偏离方向时，手动执行 `coevolution reset` 将 emergent domain prior 重置为技术领域基线（技术域 prior 保留），或先执行 `coevolution snapshot` 创建快照再决定是否重置
4. **审查自主修改**：定期检查 `resources/coevolution/modifications/` 目录中的自主行为修改记录，确认每项修改合理或执行回滚（"revert M34 modification <id>"）
5. **否决权**：所有自主修改默认可逆（`reversible: true`），含完整 `previous_state` 快照和回滚指令。用户拥有最终否决权，任何修改均可一键回滚

---

## 在线

### 触发时机

| 触发方式 | 时机 | 行为 |
|---------|------|------|
| 自动 — start sync 扩展 | 每日 `start` 同步检查步骤 2c（M33 知识轴+跨轴扫描完成后） | 追加 timeline + 工作日轻量模式检测（P-T + P-A）+ 周日全量 4 种模式 + 建议生成 + 反自强化检查（M-2, M-4；周日额外 M-3） |
| 自动 — 周日全量扫描 | 周日 start sync 中（M33 扫描完成后） | 全量模式检测（P-T + P-C + P-R + P-A）+ 建议生成 + 效果追踪 + domain prior 权重更新 + 反自强化检查（M-2, M-3, M-4） |
| 手动 — 命令 | 用户输入命令 | 按命令范围执行对应操作（6 个命令，见下方命令注册表） |

### 命令注册

| 命令 | 动作 | 说明 |
|------|------|------|
| `analyze patterns` | 模式检测 | 手动触发全量模式检测（4 种类型全部运行：P-T 时间趋势、P-C 主题聚类、P-R 转化率、P-A 异常检测），写入 `patterns/`，追加 timeline 条目 |
| `analyze suggestions` | 建议生成 | 基于现有高置信度模式（confidence >= 0.6）生成新建议（S-P 具体提案、S-Q 挑衅性问题、S-R 行为反思、S-H 习惯建议），写入 `suggestions/`，追加 timeline 条目 |
| `analyze effects` | 效果追踪 | 扫描近期建议的采纳情况和效果（实体关联检测 + 统计关联检测），更新 `effect_observations`，置信度 >= 0.4 的效果反馈至 domain prior 权重 |
| `coevolution status` | 状态摘要 | 输出当前协同进化系统状态摘要（活跃模式数、建议数及状态分布、效果数及平均效应量、domain prior 权重、修改记录、反自强化运行状态） |
| `coevolution reset` | 周期重置 | 手动触发 emergent domain prior 重置（M-4），创建快照后重置为技术领域基线。技术域 prior 保留不变 |
| `coevolution snapshot` | 快照 | 创建当前 domain prior 快照到 `snapshots/`（不执行重置）。用于修改前保存检查点 |

### 统一可嵌套时间轴 Schema

所有系统事件（日常状态变更、实体创建/修改、关联检测、分析会话、AI 对话轮次、模式检测、建议生成/采纳、行为修改）均表示为统一的可嵌套时间轴条目，存储于 `resources/coevolution/timeline.yaml`（单一文件，append-only，git-diffable YAML）。

```yaml
# 每个时间轴条目是一个 YAML document，以 "---" 分隔

# [必填] ISO 8601 时间戳（含时区偏移）。精确到秒（AI 交互）或天（日常笔记）
timestamp: "2026-06-05"

# [必填] 事件来源类型（枚举，共 10 种）
source_type:
  enum:
    - daily-note             # 从 daily/*.md 提取
    - entity-created         # 实体 YAML `created` 字段
    - entity-modified        # 实体 YAML `updated` 字段
    - related-entity-detected # 实体 related_entities[] 条目
    - raw-analysis           # 语言结构分析会话
    - conversation-turn      # AI 对话轮次
    - pattern-detected       # Layer 1 模式检测输出（运行时）
    - suggestion-generated   # Layer 2 建议生成输出（运行时）
    - suggestion-adopted     # Layer 3 效果追踪：用户采纳了建议
    - behavior-modified      # M-1：自主行为修改已执行

# [必填] 记录的主要状态变更。格式："domain.property: old_value -> new_value"
state_switch: "idea.status: raw -> classified"

# [可选] 递归嵌套的子状态变更列表。同一 schema，嵌套深度上限 5 层
# 用于复合事件（如一次日常回顾包含多个任务完成、分数变更和想法记录）
sub_states:
  - state_switch: "project.task: pending -> completed"
    entity_ref: {type: project, slug: gaokao-chinese}
    context_snapshot: "Anki 实词 Day 5 完成"
    metadata: {task_index: 1, completed_marker: "[x]"}

# [可选] 事件涉及的实体引用
entity_ref:
  type: idea           # string (entity type, dynamically discovered from project directories)
  slug: ai-amplifier

# [可选] 事件来源的日常笔记引用
daily_ref:
  date: "2026-06-05"

# [可选] 语义上下文快照（<= 500 字符）
context_snapshot: >
  Anki 实词 Day 5 完成 + 自测卷 #3 完成（最后一套），全部备考任务完结。

# [可选] AI 对话追踪（多轮次）
conversation_trace:
  - turn_index: 1
    role: user                    # user | assistant | system
    summary: "请求分析 Ch05 P1 段的语言组织方式"

# [可选] 自由格式扩展元数据（按 source_type 命名空间组织）
metadata:
  mental_score: 70
  physical_score: 70
  pairing_domain: "idea--literature-note"  # M33 配对域（related-entity-detected 条目）
```

### 模式输出 Schema

Layer 1 产出的 4 种模式（P-T 时间趋势、P-C 主题聚类、P-R 转化率、P-A 异常检测）共享统一 envelope，存储于 `resources/coevolution/patterns/p-{YYYYMMDD}-{hash6}.yaml`。

```yaml
# 统一模式 envelope（所有 4 种类型共用）
pattern_id: "p-20260606-a1b2c3"          # 格式：p-{YYYYMMDD}-{hash6}
pattern_type: "temporal-trend"           # temporal-trend | topic-cluster | conversion-rate | anomaly
detected_at: "2026-06-06T08:30:00+08:00"
data_window: {start: "2026-05-07", end: "2026-06-06"}
confidence: 0.72                         # >= 0.6 进入 Layer 2；0.3-0.6 标记低置信度；< 0.3 丢弃
low_confidence: false
description: "idea 创建速率在 tag='meta-cognition' 集群中连续 14 天上升（斜率 +0.15/天，R^2=0.78）"

# 源数据引用（指向 timeline.yaml 范围或实体文件）
source_data_refs:
  - type: timeline-range
    path: "resources/coevolution/timeline.yaml"
    entry_range: "2026-05-07..2026-06-06"

# 受影响的实体列表
affected_entities:
  - {type: idea, slug: ai-amplifier}
  - {type: idea, slug: meta-cognition-tool}

# Domain 分类（用于自动权重初始化）
domain:
  technical: "idea--permanent-note"  # 15 个 M33 配对之一，或 "orphan"
  emergent: null                     # null | "cluster-N"（P-C 跨域聚类）

# 权重向量（从 domain prior 初始化，0.1 下限强制执行）
weight_vector: {A: 0.25, B: 0.25, C: 0.25, D: 0.25}
# A=探索新颖性 B=行为改变 C=闭环反馈 D=反强化防御

# [可选] 反证据列表（M-2 追加，>= 3 条时降低 pattern confidence）
counter_evidence: []

# 类型特定载荷（仅一个 section 存在，匹配 pattern_type）：
#   temporal-trend → trend_data   (滑动窗口线性回归结果 + 标签集群 + 趋势方向)
#   topic-cluster  → cluster_data (聚类实体 + 凝聚力分数 + 跨配对类型 + emergent_label)
#   conversion-rate → conversion_data (转化路径 + 转化率 + 前后窗口对比 + 趋势)
#   anomaly        → anomaly_data (Z-score + 异常类型 + 受影响实体 + 异常日上下文)
```

### 建议输出 Schema

Layer 2 产出的 4 种建议（S-P 具体提案、S-Q 挑衅性问题、S-R 行为反思、S-H 习惯建议）共享统一 envelope，存储于 `resources/coevolution/suggestions/s-{YYYYMMDD}-{hash6}.yaml`。

```yaml
# 统一建议 envelope（所有 4 种类型共用）
suggestion_id: "s-20260606-a1b2c3"      # 格式：s-{YYYYMMDD}-{hash6}
suggestion_type: "proposal"             # proposal | question | reflection | habit
generated_at: "2026-06-06T08:30:15+08:00"
source_patterns: ["p-20260606-d4e5f6"]  # 触发此建议的 pattern ID(s)
priority: 0.82                          # >= 0.7 高优先级内联呈现；0.4-0.69 中优先级归档；< 0.4 低优先级仅可搜索
priority_rationale: "cluster_size(7) * cohesion_score(0.68) * (1-has_project(0)) = 4.76 -> clamped 1.0"
content: >
  主题聚类 'meta-cognition + AI 工具' 包含 7 个实体（5 idea + 2 lit-note），
  凝聚力 0.68，且无关联 project。建议创建一个 project 来统筹该方向的探索。

# 生命周期状态
status: "active"  # active | adopted | dismissed | snoozed | superseded | ignored
adopted_at: null                  # Layer 3 检测到采纳时填入
effect_observed: null             # Layer 3 追加效果观察
dismissed_at: null                # 用户驳回时填入
dismissal_reason: null            # M-5：用户提供或 AI 推断的驳回原因

# 建议目标实体
target_entities:
  - {type: idea, slug: ai-amplifier}
  - {type: idea, slug: meta-cognition-tool}

delivered_inline: true            # 优先级 >= 0.7 的内联呈现
delivered_at: null
snoozed_until: null               # 稍后处理后 7 天重新浮现
target_hash: "abc123..."          # SHA-256(sorted target entity slugs) 前 16 字符，用于去重

# 类型特定载荷（仅一个 section 存在，匹配 suggestion_type）：
#   proposal   → proposal_data   (源聚类信息 + project 覆盖检查 + 优先级计算追踪)
#   question   → question_data   (异常/趋势触发信息 + gap 描述 + 备选问题措辞)
#   reflection → reflection_data (评分轨迹 + project 活动关联 + 主要相关性)
#   habit      → habit_data      (创建/处理率对比 + 历史对比 + 习惯建议子类型 + 备选措辞)
```

**内联呈现格式**（高优先级建议，每日 start sync 中最多 3 条）：
```
M34 建议 [#1/3] (S-P, 0.82): 主题聚类 'meta-cognition + AI 工具' 包含 7 个实体（5 idea + 2 lit-note），凝聚力 0.68，且无关联 project。建议创建一个 project 来统筹该方向的探索。
  [接受 / 拒绝 / 稍后]
```

**去重算法**：新建议写入前，对 status=active 或 snoozed 的同类型已有建议计算 target_entities 的 Jaccard 相似度。Jaccard >= 0.5 且同类型 -> 跳过写入，刷新已有建议的 generated_at。若新建议 priority 比已有建议高 >= 0.2，则写入新建议并将旧建议标记为 superseded。

**优先级分层**：
- **高（>= 0.7）**：内联呈现，最多 3 条/次
- **中（0.4-0.69）**：归档至 suggestions/，用户询问时浮现
- **低（< 0.4）**：仅归档，可搜索不可主动浮现

### 效果信号 Schema

Layer 3（效果追踪层）被动观察建议生成后的行为变化。效果信号追加到 suggestion 文件的 `effect_observations` 列表中。检测频率：每周日全量扫描时执行。

```yaml
# 追加到 suggestion 文件的效果观察条目
effect_observations:
  - detected_at: "2026-06-13T08:30:00+08:00"
    detection_method: "entity-linked"          # entity-linked | statistical-correlation
    confidence: 0.72                           # >= 0.4 反馈至 domain prior；< 0.4 仅审计记录
    low_confidence: false
    description: >
      Suggestion s-20260606-a1b2c3 (proposal) 后，project
      'meta-cognition-exploration' 创建于 2026-06-10，引用 7 个目标实体中的 4 个。
      实体关联检测，置信度 0.72。(P2: 观察到相关性，非因果性)
    magnitude: 0.65                            # [-1.0, 1.0] 正=有益方向，负=适得其反
    evidence:                                  # 具体证据条目
      - type: entity-created
        detail: "Project 'meta-cognition-exploration' 创建于 2026-06-10，tags [meta-cognition, ai, self-improvement]"
        timestamp: "2026-06-10"
        entity_ref: {type: project, slug: meta-cognition-exploration}
      - type: entity-status-change
        detail: "Idea 'ai-amplifier' status raw -> classified on 2026-06-11"
        timestamp: "2026-06-11"
        entity_ref: {type: idea, slug: ai-amplifier}

    # 反馈至 domain prior 的权重 delta（仅 confidence >= 0.4 时写入）
    feedback:
      affected_domains:
        - technical: "idea--project"
          emergent: null
      weight_delta: {A: -0.05, B: 0.25, C: 0.25, D: -0.05}
      learning_rate: 0.05
```

**两种检测机制**：
1. **实体关联检测**（entity-linked）：检查建议的 target_entities 是否在建议生成后出现状态变更、新增 related_entities、或新 project 引用。适用于 S-P 和 S-Q 类型。检测窗口：建议生成后 >= 7 天。
2. **统计关联检测**（statistical-correlation）：比较建议生成前后 14 天时间窗口的目标指标均值变化，使用 Welch's t-test 和 Cohen's d 效应量。适用于 S-R 和 S-H 类型。检测窗口：建议生成后 >= 14 天。

**反馈闭环**：效果观察（confidence >= 0.4）-> 计算 weight_delta（正效果：B+C 增、A+D 减；负效果：D 增、A+B+C 减；中性效果：A 增、D+B+C 减）-> 乘以 learning_rate (0.05) -> 更新 domain prior 权重向量 -> 每 10 次效果观察触发 EMA 重算（alpha=0.3）。

### 修改 Schema（M-1）

自主行为修改记录存储于 `resources/coevolution/modifications/m-{YYYYMMDD}-{hash6}.yaml`。所有修改默认可逆，含完整 `previous_state` 快照和分步回滚指令。

```yaml
modification_id: "m-20260606-a1b2c3"
modification_type: "threshold-adjustment"     # behavior-rule-change | threshold-adjustment | weight-override | pattern-filter-update
executed_at: "2026-06-06T08:30:30+08:00"
notified: true                                # P3：是否已通知用户
reversible: true                              # 默认可逆
status: "active"                              # active | reverted | confirmed | expired

# 修改前的完整状态快照（用于回滚）
previous_state:
  target_path: "parameters.floor"
  value: {floor: 0.1}
  captured_at: "2026-06-06T08:30:29+08:00"
  value_hash: "sha256..."
  description: "Domain prior floor was 0.1 (default)"

# 修改后的新状态
new_state:
  target_path: "parameters.floor"
  value: {floor: 0.15}
  applied_at: "2026-06-06T08:30:30+08:00"
  value_hash: "sha256..."
  description: "Floor raised to 0.15 for stronger anti-reinforcement defense"

# 分步回滚指令（AI 可直接执行，无需额外上下文）
rollback_instructions: >
  1. Open domain-taxonomy.yaml
  2. Set parameters.floor to 0.1 (previous_state.value.floor)
  3. Update meta.last_updated to current timestamp
  4. Set this modification status to 'reverted'
  5. Append timeline entry (source_type: behavior-modified, state_switch: modification reverted)
  6. Notify user of successful rollback

source_suggestion: "s-20260606-a1b2c3"        # 触发此修改的建议
source_patterns: ["p-20260606-d4e5f6"]
rationale: >
  Layer 3 检测到 domain 'idea--project' 的建议驳回率 60%（含负面用户反馈）。
  将 floor 从 0.1 提升至 0.15 以加强该域的反强化防御。保守调整（+0.05），在自主限制范围内。
expires_at: null                               # 设置后自动过期回滚
```

**回滚触发**：用户输入 "revert M34 modification <id>" 或 "回滚修改 <id>"。系统读取 modification 文件的 `rollback_instructions` 和 `previous_state.value` 执行回滚。回滚是幂等的（已回滚的修改再次回滚为 no-op）。

### Domain Taxonomy 参考

**15 个技术域**（继承 M33 的 4 个维度组，15 个实体配对）：

| 组 | 配对 | 实体类型 | 维度数 | 阈值 | 初始权重 |
|----|------|---------|--------|------|---------|
| A: 知识-知识 | idea↔文献笔记↔永久笔记（3对） | idea, lit-note, perm-note | 8 | 0.40 | A=0.25 B=0.25 C=0.25 D=0.25 |
| B: 知识↔执行 | idea/笔记↔project（3对） | idea, lit-note, perm-note, project | 5 | 0.35 | A=0.25 B=0.25 C=0.25 D=0.25 |
| C: 知识↔Skill | idea/笔记↔skill（3对） | idea, lit-note, perm-note, skill | 4 | 0.35 | A=0.25 B=0.25 C=0.25 D=0.25 |
| D: 执行-执行 | project↔skill（1对） | project, skill | 4-5 | 0.35 | A=0.25 B=0.25 C=0.25 D=0.25 |

**权重向量含义**：A=探索新颖性（鼓励发现新模式而非重复已知聚类），B=行为改变（优先产生可观察行为变化的模式），C=闭环反馈（优先能完成"模式->建议->效果"全流程的模式），D=反强化防御（抑制产生重复建议或负面效果的模式）。每个权重 >= 0.1（下限），总和 = 1.0。

**emergent domain**：Layer 1 P-C 主题聚类发现的跨域聚类在满足 (a) cohesion_score >= 0.6 且 (b) 跨越 >= 2 个技术域组时，自动创建为 emergent domain。其权重向量初始化为组成技术域的加权平均（按 entity count 加权）。Emergent domain 每 30 天重置（M-4），快照保存至 `snapshots/`。

---

## 执行步骤

### 步骤 1：加载时间轴和实体状态

在每次执行前，加载系统运行所需的全部输入数据。

1. 读取 `resources/coevolution/timeline.yaml`（如果文件不存在，说明迁移未执行，跳过所有检测步骤并在输出中提示"时间轴未迁移，请先执行迁移脚本"）：
   - 解析所有 YAML document（`yaml.safe_load_all()`）
   - 按 `source_type` 过滤：`daily-note`（评分轨迹）、`entity-created` / `entity-modified`（实体生命周期）、`related-entity-detected`（关系网络）、`pattern-detected` / `suggestion-generated` / `suggestion-adopted`（系统运行历史）
   - 构建时间序列索引：按日期分组的 `{date: [entries]}` 映射，用于趋势和异常检测的滑动窗口计算
2. 读取实体 YAML frontmatter（`ideas/`、`literature-notes/`、`permanent-notes/`、`projects/`、`skills/`，共 ~308 个文件）：
   - 提取：`tags`、`status`、`summary`（如有）、`created`、`updated`（如有）、`related_entities`（如有）
   - 排除：`status: discarded` 的 idea、`status: closed/abandoned` 的 project
   - **每日想法提取（`daily_idea_extractor()`）**：作为实体加载的补充步骤，扫描 `daily/\*.md` 文件中的 `## 想法` 节，检测未链接到独立实体文件的孤立想法（orphaned ideas）。对于无有效 Markdown 链接的想法，生成虚拟实体条目（`type: idea`，基于内容的 slug，摘要取自行文）。虚拟实体在去重后合并到实体列表中。此机制确保从日常笔记中提及但尚未创建独立文件的想法仍被系统识别和分析。
3. 加载 `domain-taxonomy.yaml`（`resources/coevolution/domain-taxonomy.yaml`），获取当前技术域的 weight_vector 和全部 emergent domain 的 weight_vector
4. 加载 `state.md`（`resources/coevolution/state.md`），获取 `last_reset_date`（M-4 检查）、配置参数和最近的系统摘要
5. 根据触发上下文确定扫描模式：
   - **轻量模式**（工作日 start sync 扩展）：仅执行步骤 2 的 P-T 和 P-A 检测，跳过 P-C 和 P-R
   - **全量模式**（周日 start sync 或 `analyze patterns` 命令）：执行全部 4 种模式检测 + 步骤 3-5-6-7

### 步骤 2：运行模式检测（Layer 1 — 4 种类型）

基于时间轴和实体数据，运行 4 种模式检测算法。轻量模式仅执行 P-T 和 P-A，全量模式执行全部 4 种。

**P-T — 时间趋势检测**（每日 + 周日）：

1. 从 timeline.yaml 查询数据窗口内（默认 30 天）的所有 `entity-created` 和 `entity-modified` 条目
2. 按标签集群分组实体：使用单链接聚类，将 Jaccard(tags) >= 0.3 的实体合并为同一集群
3. 对每个集群（>= 3 个实体）构建每日创建计数的时间序列，拟合线性回归：`y = slope * day_index + intercept`，计算 R^2
4. 额外指标：从 `daily-note` 条目中提取 `mental_score` 和 `physical_score`，构建同样的滑动窗口回归
5. 趋势方向判定：slope > 0.05/天 且 R^2 >= 0.3 → "up"；slope < -0.05/天 且 R^2 >= 0.3 → "down"；否则 "flat"
6. 置信度 = min(R^2 * 1.2, 1.0) * min(|slope| * 3, 1.0) * min(cluster_size / 10, 1.0)
7. 对每个满足 |slope| > 0 且 R^2 >= 0.3 的集群创建一个 P-T 模式，写入 `patterns/p-{date}-{hash6}.yaml`

**P-C — 主题聚类检测**（仅周日全量扫描）：

1. 遍历全部 312 个实体，构建共现矩阵：
   - 标签相似度 = Jaccard(entity_i.tags, entity_j.tags)
   - 结构链接 = 1.0 if entity_i.related_entities 包含 entity_j（或反之），else 0.0
   - 共享邻居数 = |N(i) ∩ N(j)| / max(|N(i)|, |N(j)|, 1)，其中 N(k) = 通过 related_entities 关联的实体
   - 合并分数 = 0.4 * 标签相似度 + 0.4 * 结构链接 + 0.2 * 共享邻居数
2. 转换为距离矩阵：distance(i,j) = 1.0 - combined_score
3. 运行层次聚类（average linkage），在距离 = 0.65 处切割树状图（无预设 K 值）
4. 对每个聚类（>= 3 个实体）：
   - 计算凝聚力 = 聚类内平均(1 - distance)
   - 确定跨配对类型：将实体类型对映射到 M33 的 15 个配对域，统计跨组数
   - 提取主导标签（出现在 >= 50% 聚类实体的标签）
   - 置信度 = cohesion_score * min(cluster_size / 5, 1.0)
5. 过滤：cohesion_score >= 0.3 才保留。P2 合规：聚类可无标签（`emergent_label: null` 有效）
6. 对每个通过过滤的聚类创建 P-C 模式

**P-R — 转化率检测**（仅周日）：

1. 从 timeline.yaml 查询状态转换条目（`state_switch` 字段），聚焦 5 条关键转化路径：
   - idea: raw -> classified
   - idea: classified -> project（idea 转为 project）
   - idea: classified -> permanent-note（idea 合成为永久笔记）
   - literature-note: raw -> processed
   - permanent-note: draft -> published
2. 对每条路径，计算转化率 = 完成转化的实体数 / 窗口内符合源状态的实体数
3. 与上一窗口（同样长度）的转化率对比：rate_delta >= +0.05 → "up"；<= -0.05 → "down"；否则 "stable"
4. 置信度 = logistic(sample_size)：1.0 / (1.0 + exp(-5*(eligible_count - 3)/3)) * min(1.0, sqrt(eligible_count/10))
5. 对每条满足 eligible_count >= 3 的路径创建 P-R 模式

**P-A — 异常检测**（每日 + 周日）：

1. 对每个追踪指标（实体创建突发频率、关系密度、标签词汇变化、mental_score 骤降、physical_score 骤降、project 速度峰值），维护 30 天滚动序列
2. 计算滚动均值（μ_30）和滚动标准差（σ_30）。对每日值计算 Z = (value - μ_30) / σ_30。若 σ_30 == 0，Z = 0
3. 标记异常：|Z| >= 2.0 → positive-spike（Z >= 2.0）或 negative-drop（Z <= -2.0）
4. 置信度 = min(|Z| / 4.0, 1.0)。Z=2.0 → 0.5, Z=3.0 → 0.75, Z=4.0+ → 1.0
5. 特殊规则：同一天同类型实体创建 > 3 个 → 直接标记为创建突发异常（Z >= 2.0 按构造）
6. 对每个检测到的异常创建 P-A 模式

**噪音过滤**（所有模式产出后统一应用）：
- confidence < 0.3 → 直接丢弃，不写入 patterns/
- 0.3 <= confidence < 0.6 → 写入 patterns/，标记 `low_confidence: true`，不进入 Layer 2
- confidence >= 0.6 → 写入 patterns/，标记 `low_confidence: false`，进入步骤 3（Layer 2）

### 步骤 3：运行建议生成（Layer 2 — 4 种类型）

基于步骤 2 产出的高置信度模式（confidence >= 0.6），生成 4 种建议。去重检查在所有写入前执行。

**S-P — 具体提案**（触发条件：P-C 模式，高凝聚力聚类）：

1. 提取 P-C 聚类的实体列表、主导标签和凝聚力分数
2. 检查现有 project 覆盖：加载全部 project（`projects/`，7 个文件），计算每个 project 的 tags 与聚类主导标签的 Jaccard。若 Jaccard >= 0.4 → `has_project = true`
3. 若无覆盖 project：
   - 提案子类型判定：ideas >= 3 且 perm-notes == 0 → "synthesis-review"；lit-notes >= 2 且 ideas == 0 → "exploration"；否则 → "create-project"
   - 优先级 = min(cluster_size * cohesion_score * (1 - has_project_bool) / 5.0, 1.0)
   - 生成提案文本："主题聚类 '{dominant_tags}' 包含 N 个实体（type breakdown），凝聚力 {cohesion}，且无关联 project。建议..."
4. 写入 `suggestions/s-{date}-{hash6}.yaml`

**S-Q — 挑衅性问题**（触发条件：P-A 异常或 P-T 显著趋势）：

1. 提取异常/趋势的 gap 描述和统计参数
2. 问题子类型判定：creation_rate 高 synthesis_rate 低 → "synthesis-gap"；创建突发 → "attention-burst"；trend 下降 → "declining-interest"；转化率降 → "processing-bottleneck"；评分-项目错配 → "score-behavior-gap"
3. 优先级 = min(anomaly_z_score * gap_duration_days / 50.0, 1.0)
4. 生成挑衅式问题文本（1-3 句，使用反问句式鼓励用户反思）
5. 写入 `suggestions/`

**S-R — 行为反思**（触发条件：评分趋势与 project 活动存在显著关联）：

1. 从 timeline.yaml 提取 mental_score/physical_score 时间序列（最近 30 天）
2. 提取 project 活动指标：每日任务完成数、活跃 project 数、实体创建数
3. 计算 mental_score 与活跃 project 数的 Pearson r。若 r < -0.5 且 R^2 >= 0.3 → 触发反思
4. 优先级 = min(trend_r_squared * |avg_score_trend_slope| * 10 / 5.0, 1.0)
5. 反思子类型：project 数上升分数下降 → "project-overload"；完成率上升但分数不改善 → "diminishing-returns"；连续 >= 5 天低分 → "recovery-needed"
6. 生成反思文本（1-3 句，数据驱动但不评判），写入 `suggestions/`

**S-H — 习惯建议**（触发条件：创建率与处理率存在显著失衡）：

1. 对每种知识实体类型（idea, literature-note, permanent-note），从 timeline.yaml 计算：
   - creation_rate = 最近 7 天的 entity-created 计数 / 7
   - processing_rate = 最近 7 天的状态推进计数 / 7
2. 比较比例：creation_rate / max(processing_rate, 0.1)。若 > 2.0 → 显著失衡
3. 优先级 = min(creation_rate / max(processing_rate, 0.1) / 20.0, 1.0)
4. 习惯子类型：creation_rate >> processing_rate → "backlog-warning"；processing_rate = 0 持续 >= 7 天 → "review-reminder"；processing_rate > creation_rate → "positive-reinforcement"
5. 生成具体可操作的习惯建议文本，写入 `suggestions/`

**M-3 随机探索注入**（仅周日全量扫描时，与 S-P/S-Q/S-R/S-H 并行触发）：
- 生成随机浮点数 p in [0.0, 1.0)。若 p < 0.05：
  - 从 15 个 M33 配对中随机选择一个最近 30 天未被任何建议的 source_patterns 引用的配对
  - 从该配对的实体中随机选择 3-5 个作为 target_entities
  - 生成一个简单的 proposal 类型建议（priority 固定为 0.5，`source: "random-exploration"`，`delivered_inline: false`）
  - 标记 `[探索性建议]` 前缀以区别于模式驱动的建议

**去重**（所有建议写入前）：
- 加载所有 status=active 或 snoozed 的同类型已有建议
- 计算新建议与每个已有建议的 target_entities Jaccard 相似度
- 若 Jaccard >= 0.5 且同类型 → 跳过，刷新已有建议的 generated_at
- 若新建议 priority 比已有建议高 >= 0.2 → 写入新建议，旧建议标记为 superseded

### 步骤 4：内联呈现高优先级建议

在每日 start sync 扩展（步骤 2c-f）中执行。仅在生成了高优先级建议（priority >= 0.7, status=active）时触发。

1. 从 steps 3 产出的建议中筛选 priority >= 0.7 且 status = "active" 的建议
2. 若数量 > 3，按优先级降序选择前 3 条。优先级相同时的排序规则：target_entities 更多 > S-P > S-Q > S-R > S-H > 更新生成时间
3. 按内联呈现格式输出（每条 2 行）：
   ```
   M34 建议 [#N/3] ({type_abbrev}, {priority}): {content}
     [接受 / 拒绝 / 稍后]
   ```
4. 用户响应处理：
   - "接受"：suggestion.status → "adopted"，追加 timeline 条目（`source_type: suggestion-adopted`）。若为 S-P 类型，可选询问是否立即创建建议的 project
   - "拒绝"：suggestion.status → "dismissed"，记录 dismissal_reason（用户提供或留空）。执行 M-5：源 pattern 置信度 -0.2 + 该域 D 权重 +0.05
   - "稍后"：suggestion.status → "snoozed"，snoozed_until = now + 7 days
   - 无响应（14 天）：auto-transition → "ignored"
5. 若用户说"今天不再显示建议"或等价表述：跳过本次会话的后续内联呈现。建议仍生成并归档
6. 输出附加到 M33 摘要行后：
   ```
   知识轴扫描：N 组新关联（高价值 M 组）| 跨轴扫描：K 组新关联 | M34: P patterns, S suggestions (H high-priority)
   ```
   若无新模式或建议：`| M34: no new patterns`

### 步骤 5：运行效果追踪（Layer 3 — 被动观察）

仅周日全量扫描时执行，或通过 `analyze effects` 命令手动触发。Elapsed time since suggestion generation 不足时跳过。

**实体关联检测**（entity-linked）：

1. 加载所有 suggestions（status IN ("active", "adopted", "snoozed")，generated_at <= now - 7 days，target_entities 非空）
2. 对每条建议：
   - 读取每个 target_entity 的当前 YAML 状态
   - 从 timeline.yaml 查询该实体在建议生成时间点之前的最新状态（作为参考状态）
   - 判定 hit/miss：实体在 generated_at 之后出现了 status 变更、tags 变更、related_entities 新增、或新 project 引用（Jaccard >= 0.3）→ hit
   - 对 S-P 建议额外检查：是否有新 project 创建且其 tags 与源聚类的 dominant_tags 的 Jaccard >= 0.4
   - 计算 hit_ratio = hit_count / total_target_entities
   - 置信度 = hit_ratio * (1.0 if new_project_found else 0.7) * min(days_since_suggestion / 14, 1.0) + evidence_boost（最多 +0.3）
3. 若 confidence >= 0.3 → 创建 effect_observation，追加到 suggestion 的 effect_observations 列表。若 confidence >= 0.4 → 计算 feedback weight_delta
4. 若 hit_ratio >= 0.3 → 设置 suggestion.status = "adopted"

**统计关联检测**（statistical-correlation）：

1. 加载所有 S-R 和 S-H suggestions（status IN ("active", "adopted", "snoozed")，generated_at <= now - 14 days）
2. 对每条建议确定追踪指标（从 suggestion 的 reflection_data 或 habit_data 提取）和期望方向
3. 构建前后窗口（各 14 天）：从 timeline.yaml 查询指标时间序列
4. 比较前后窗口：均值差、斜率反转（是否在期望方向）、Welch's t-test（p 值）、Cohen's d（效应量）
5. 置信度 = 0.4 * (1.0 if slope_reversal else 0.6) + 0.3 * min(cohens_d / 0.8, 1.0) + 0.3 * (1.0 if significant_at_005 else 0.5)
6. magnitude = sign * tanh(|mean_difference| / before_std)
7. 若 confidence >= 0.3 → 创建 effect_observation。若 directional_alignment = true 且 confidence >= 0.5 → suggestion.status = "adopted"
8. 若 confidence >= 0.4 → 计算 feedback weight_delta

**两种检测的关键差异**：
- 实体关联检测最小等待 7 天（让实体状态变化有足够时间发生）
- 统计关联检测最小等待 14 天（需要足够数据点进行有意义的 before/after 比较）
- 置信度 < 0.3 → 不创建 effect_observation（噪音过滤）
- 置信度 < 0.4 → 创建 observation 但标记 `low_confidence: true`，不反馈至 domain prior

### 步骤 6：更新自动权重系统（Domain Prior 演化）

在步骤 5 的效果追踪完成后执行。仅处理 confidence >= 0.4 的效果观察。

1. 收集本轮所有新的效果观察（confidence >= 0.4）
2. 对每条观察：
   - 从 source suggestion 的 source_patterns 确定受影响域（technical domain pairing 或 emergent cluster）
   - 读取 Layer 3 计算的 `feedback.weight_delta`
   - 应用 learning_rate：`effective_delta[i] = weight_delta[i] * 0.05`
   - 更新域 weight_vector：`new_weight[i] = old_weight[i] + effective_delta[i]`
   - 应用 0.1 floor + 重归一化（clamp 低于 0.1 的权重，从高于 0.1 的权重中按比例扣除以保持 sum=1.0）
   - 追加 `prior_history` 条目：`{timestamp, old_vector, delta_applied, new_vector, source_effect_id}`
   - 递增 `effect_count` 和 `ema_decay_count`
   - 追加 timeline 条目（`source_type: behavior-modified`，`state_switch: "domain_prior.{domain}: old_vector -> new_vector"`）
3. 对每个域，检查 `ema_decay_count >= 10`：
   - 收集该域最近 N（min(10, available)）个 pattern 的 weight_vector
   - 计算 EMA：`ema_vector[i] = 0.3 * w[i] + 0.7 * ema_vector[i]`（迭代每个 pattern）
   - 设置 `domain.weight_vector = ema_vector`（floor + 重归一化后）
   - 重置 `ema_decay_count = 0`
4. 若出现 emergent domain：
   - 检查 P-C 聚类是否满足条件（cohesion_score >= 0.6，跨越 >= 2 个技术域组）
   - 初始化权重向量 = 组成技术域的加权平均（按 entity count 加权）
   - 应用 0.1 floor + 重归一化
   - 添加到 `domain-taxonomy.yaml` 的 `emergent_domains` 列表
5. 将更新后的 domain prior 写回 `domain-taxonomy.yaml`

**权重 delta 符号约定**：
- **正效果（magnitude > 0.2）**：B (+45%), C (+45%)。系统在此域运作良好，鼓励更多行为改变和闭环。A (-20%), D (-10%)
- **负效果（magnitude < -0.2）**：D (+60%)。系统在此域产生适得其反的建议，大幅强化防御。B (-30%), A (-10%), C (-10%)
- **中性效果（|magnitude| <= 0.2）**：A (+60%)。无显著变化，鼓励探索新方法。D (-20%), B (-10%), C (-10%)

### 步骤 7：应用反自强化检查（M-2、M-3、M-4）

在每次模式检测后执行（轻量模式：M-2 + M-4；全量/Sunday 模式：M-2 + M-3 + M-4）。

**M-2 — 反证据追踪**（每次扫描）：

1. 对每个活跃 pattern（confidence >= 0.3，写入 patterns/ 不超过 30 天）：
   - 在最新的 M33 扫描数据中（或直接读取实体文件）搜索与该 pattern 的主张矛盾的实体
   - 例如：若 P-T 显示 "tag X 的趋势上升"，检查 tag X 中是否有实体被丢弃（status: discarded）或 status 回退
   - 例如：若 P-C 显示 "聚类 Y 凝聚力 0.68"，检查聚类中是否有实体在最新扫描中移除了 related_entities 链接
2. 对每个找到的矛盾实体：
   - 追加 `counter_evidence` 条目至 pattern 文件：`{detected_at, description, contradicts, strength}`
   - 追加 timeline 条目（`source_type: pattern-detected`，`state_switch: "pattern.counter_evidence: null -> detected"`）
3. 若某 pattern 的 `counter_evidence` 条目数 >= 3：
   - 降低 pattern 置信度：`confidence -= 0.1 * sum(strength for each counter_evidence entry)`
   - 若新 confidence < 0.6 → `low_confidence: true`（不再进入 Layer 2）
   - 若新 confidence < 0.3 → 不删除文件，但标记为 `low_confidence: true` 并在下次扫描时跳过

**M-3 — 随机探索注入**（仅周日全量扫描）：

1. 生成随机浮点数 p in [0.0, 1.0)
2. 若 p < 0.05（可在 state.md 中配置）：
   - 选择随机实体配对（从 15 个 M33 配对中选一个最近 30 天未被任何建议 source_patterns 引用的配对）
   - 随机选择 3-5 个该配对的实体作为 target_entities
   - 生成探索性建议（S-P 类型，priority 固定 0.5，`source: "random-exploration"`，`delivered_inline: false`）
   - 追加 timeline 条目

**M-4 — 周期重置**（每次扫描）：

1. 从 `state.md` 读取 `last_reset_date`
2. 若 `last_reset_date + 30 days <= today`（或用户手动触发 `coevolution reset`）：
   - 创建快照：将当前全部 domain prior（技术域 + emergent 域）写入 `resources/coevolution/snapshots/domain-priors-YYYY-MM-DD.yaml`
   - 重置所有 emergent domain 的 weight_vector → 组成技术域的加权平均（按 entity count）
   - 技术域 prior **保留不变**（累积长期经验）
   - 更新 `state.md`：`last_reset_date = today`
   - 追加 timeline 条目
   - 输出："M-4 周期重置已执行。N emergent domain 已重置为技术领域基线。快照已保存。"
3. 若无需重置：跳过

---

## 修改执行步骤（P3 自主修改）

当系统在 Domain Prior 演化（步骤 6）或反自强化检查（步骤 7）中判定需要自主修改行为规则、阈值或权重时：

1. **判定修改类型和范围**：
   - `threshold-adjustment`：调整数值阈值（如 confidence 丢弃阈值、内联优先级阈值、anomaly Z-score 阈值、weight_floor、learning_rate 等）
   - `weight-override`：直接覆盖某域的 weight_vector（M-5 驳回触发、反证据累积达临界阈值）
   - `behavior-rule-change`：添加/修改/移除行为规则（如去重规则、抑制规则、检测范围规则）
   - `pattern-filter-update`：添加/修改/移除模式过滤规则
2. **捕获修改前状态**：
   - 读取当前目标参数值作为 `previous_state.value`
   - 生成 `value_hash`（SHA-256(json.dumps(value, sort_keys=True))）
   - 记录 `captured_at` 时间戳
3. **生成分步回滚指令**（AI 可直接执行，无需额外上下文）：
   - 列出具体文件路径和字段路径
   - 每步使用祈使句式
   - 包含验证步骤（hash 比对）
4. **写入修改文件**：
   - 路径：`resources/coevolution/modifications/m-{YYYYMMDD}-{hash6}.yaml`
   - `reversible: true`（始终）
   - `notified: true`（始终，P3 后通知模式）
   - 填入 `source_suggestion`、`source_patterns`、`affected_domain`、`rationale`
5. **通知用户**（在 start sync 输出中追加）：
   ```
   M34 自动修改 [#m-{hash6}]: {rationale 摘要}
   [回滚: revert M34 modification m-{hash6}]
   ```
6. **追加 timeline 条目**：`source_type: behavior-modified`，`state_switch: "modification.{modification_id}: executed"`
7. **保守性约束**：自主调整幅度限制在 <= 当前值的 20% 或 <= 0.05 绝对值（取较大者）。超出此范围的调整需要用户确认（`reversible: false` + 内联确认提示）

---

## 参考文件

| 文件 | 内容 |
|------|------|
| `resources/coevolution/timeline.yaml` | 统一可嵌套时间轴（所有系统事件的单一时间线，append-only YAML，10 种 source_type） |
| `resources/coevolution/state.md` | 当前系统状态摘要（活跃模式数、建议数及分布、domain prior 权重、修改记录、配置参数、last_reset_date） |
| `resources/coevolution/patterns/` | 模式检测报告存档（p-{YYYYMMDD}-{hash6}.yaml，4 种类型，immutable envelope + 可变 counter_evidence） |
| `resources/coevolution/suggestions/` | 建议存档（s-{YYYYMMDD}-{hash6}.yaml，4 种类型，可变 status + effect_observations） |
| `resources/coevolution/modifications/` | 行为修改存档（m-{YYYYMMDD}-{hash6}.yaml，含 previous_state 快照和分步回滚指令） |
| `resources/coevolution/snapshots/` | Domain prior 快照（M-4 周期重置时创建，文件名 domain-priors-YYYY-MM-DD.yaml） |
| `resources/coevolution/domain-taxonomy.yaml` | Domain 分类与自动权重注册表（15 个技术域 + N 个 emergent 域，每域含 weight_vector、prior_history、效果计数） |
| 时间轴 Schema | 见本文"统一可嵌套时间轴 Schema"节——字段类型、验证规则、source_type 枚举 |
| 模式 Schema | 见本文"输出规范"节——4 种类型、噪音过滤阈值、检测频率、输入数据合同 |
| 建议 Schema | 见本文"输出规范"节——4 种类型、优先级分层、去重算法、内联呈现格式 |
| 效果 Schema | 见本文"Step 5: Layer 3 效果追踪"节——2 种检测机制、反馈闭环算法 |
| 修改 Schema | 见本文"修改 Schema"节——4 种修改类型、回滚执行步骤、安全保障 |
| 迁移计划 | 见本文"时间轴填充"节——4 阶段、4 数据源、per-source 提取逻辑 |
| 集成设计 | 见本文"Context Sync"节——start 扩展、6 命令规格、连锁更新表 |
| `audit-output.md`（Section 8） | M33 技术域列表（15 个配对、4 个维度组、每配对实体类型和阈值）——M34 的 domain taxonomy 权威来源 |
