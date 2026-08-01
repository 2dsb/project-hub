---
id: "sk-20260606-era"
slug: "entity-relationship-analysis"
title: "实体关系分析系统"
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
depends_on: []
---

# 实体关系分析系统（Expanded M29/M30）

**核心功能**：跨 5 种实体类型（ideas、literature-notes、permanent-notes、projects、skills）自动分析关系，将结果写入统一的 `related_entities` YAML 字段。

**设计原则**：AI-native 系统——分析逻辑是行为规范（prompt/procedure），由 Claude Code 在触发时执行。迁移脚本是唯一的机械组件。

---

## 离线

用户职责：
1. **审批维度**：首次部署时通过 `dimension-registry.md` 审批各配对的分析维度
2. **执行迁移**：在 `bf` 备份后，手动触发 `migrate-relations` 将旧字段迁移至统一格式
3. **手动关联**：可通过 `entity X 关联到 Y` 建立手动关系（`source: "manual"`，不会被自动扫描覆盖）
4. **定期审查**：运行 `analyze dimensions` 检查维度注册表是否需要更新
5. **质量判断**：自动扫描结果仅供辅助，最终判断哪些关联有价值由用户决定

---

## 在线

### 触发时机

| 触发方式 | 时机 | 行为 |
|---------|------|------|
| 自动 — start sync | 每日 `start` 同步检查（M28 步骤 2c） | 增量扫描知识轴 + 跨轴 |
| 自动 — 实体创建/修改 | 任何实体文件创建，或 body/tags/summary 修改（chain update） | 单实体轻量扫描 |
| 手动 — 命令 | 用户输入命令 | 按命令范围执行扫描 |
| 手动 — `analyze dimensions` | 用户要求刷新维度 | 重新推导维度提案 → 用户审批 |

### 命令注册

| 命令 | 范围 | 默认模式 | 支持 `↔` 精确配对 |
|------|------|---------|-------------------|
| `analyze knowledge-axis` | 配对 1-3（知识↔知识） | 增量扫描全部知识实体 | yes |
| `analyze project-relations` | 配对 4,7,10,13,14 | 全部 project 全量扫描 | yes |
| `analyze skill-crossrefs` | 配对 4,6,8,10 | 全部 skill 全量扫描 | yes |
| `analyze idea-crossrefs` | 配对 1,2,4,5 | 全部 idea 全量扫描 | yes |
| `analyze literature-crossrefs` | 配对 1,3,6,7 | 全部 literature-note 全量扫描 | yes |
| `analyze permanent-crossrefs` | 配对 2,3,8,9 | 全部 permanent-note 全量扫描 | yes |
| `analyze cross-axis` | 配对 4,5,6,7,8,9 | 知识↔执行全量扫描 | yes |
| `analyze entity <slug>` | 指定实体 vs 全部其他类型 | 单实体深扫 | no |
| `analyze dimensions` | 维度注册表 | 重新推导+审批 | no |
| `analyze all` | 全部 10 配对 | 全量（**重度操作，执行前警告**） | yes |
| `migrate-relations` | 迁移旧字段 | 一次性迁移 | no |

### 统一关联字段 Schema

```yaml
related_entities:
  - type: "idea" | "literature-note" | "permanent-note" | "project" | "skill"
    slug: ""
    relation: ""       # 维度缩写，如 "tag-overlap", "concept-relation", "explicit-link"
    strength: 0.0-1.0
    dimensions: []     # 贡献的维度 ID 列表，如 ["KK-01", "KK-02"]
    bidirectional: true
    source: "auto" | "manual" | "migration" | "M29"
```

---

## 执行步骤

### 步骤 1：确定扫描范围

根据触发命令，确定要扫描的配对和实体范围。

1. 读取 `dimension-registry.md`（路径：`.recursive-planner/L0-overall-plan/dimension-registry.md`）
2. 根据命令确定配对列表（参见上方命令注册表）
3. 确定实体范围：
   - **增量模式**（`knowledge-axis` 默认）：仅扫描自上次扫描后新增或 body 修改的实体。通过 git diff 或文件 mtime 判断。
   - **全量模式**（其他命令默认）：扫描范围内全部实体
   - **单实体模式**（`analyze entity <slug>`）：仅扫描指定实体 vs 全部其他类型
   - **`--full` flag**：强制全量，覆盖默认增量

### 步骤 2：加载实体数据

对每个待扫描的实体对 (A, B)：

1. 读取两个实体的 YAML frontmatter
2. 提取：`tags`、`title`、`summary`（如有）、`status`、`updated`、body text
3. 排除：`status: discarded` 的 idea、`status: closed/abandoned` 的 project
4. 跳过 A=B（自引用）

### 步骤 3：执行维度评分

对当前配对在 `dimension-registry.md` 中定义的每个维度，按评分算法计算 0.0-1.0 分数。

**通用维度评分模板**：

**tag-overlap（标签重叠）**：
```
从 Entity A 和 Entity B 提取 tags 字段。如果 B 是 skill（无 tags 字段），从 B 的 body text 中提取 3-5 个关键词作为伪标签。
计算 Jaccard = |A_tags ∩ B_tags| / |A_tags ∪ B_tags|。
如果任一方标签数为 0 → score = 0。
cite: 列出重叠的标签。
```

**concept-relevance（概念关联）**：
```
阅读 Entity A 和 Entity B 的 body text。
各用一句话提炼核心概念。
判断关系：subset/superset = 0.8, neighbor（共享父概念）= 0.5, loosely related = 0.3, unrelated = 0。
cite: 引用体现关系的具体段落。
```

**contradiction（矛盾）**：
```
判断两个实体是否对同一问题持有互斥观点。
是 → score = 1.0（标记为 always-retain）。
否 → score = 0。
cite: 引用矛盾的具体表述。
```

**complement（互补）**：
```
判断两个实体是否覆盖同一主题的不同侧面，合并后信息更完整。
full complement（覆盖互补侧面）= 0.8, partial = 0.5, none = 0。
cite: 说明各自覆盖的侧面。
```

**migration（可迁移）**：
```
判断 Entity A 中的方法/框架是否可以应用到 Entity B 的领域。
direct applicability（直接可用）= 0.8, analogy（类比迁移）= 0.5, none = 0。
cite: 说明可迁移的方法和适用方式。
```

**structural-similarity（结构相似）**：
```
比较两个实体的论证/解释结构。是否都使用因果链？是否都以定义开篇？
identical structure = 0.8, similar pattern = 0.5, different = 0。
cite: 描述各自的结构特征。
```

**temporal-proximity（时间接近）**：
```
计算 date_diff = |A.updated - B.updated|（天数）。
score = 1 - min(date_diff, 365) / 365。
cite: 两个日期。
```

**explicit-link（显式链接）**：
```
检查 Entity A 的 related_entities（或旧字段 links/parent_project/depends_on 等）中是否已存在对 Entity B 的引用。
存在 → score = 1.0（标记为 always-retain）。
不存在 → score = 0。
cite: 引用已有的链接字段。
```

详细评分算法参见 `dimension-registry.md`。每个配对的具体维度组合和 pair-specific 维度也在 registry 中定义。

### 步骤 4：计算聚合强度并过滤

```
aggregate_strength = avg(所有非零维度分数)

if any_dimension_is_always_retain AND that_dimension_score == 1.0:
    retain = true  # 绕过阈值
elif aggregate_strength >= pairing_threshold:
    retain = true
else:
    retain = false  # 丢弃
```

配对阈值：
- 知识-知识（配对 1-3）：0.4
- 跨类型（配对 4-12）：0.35
- 执行-执行（配对 13-15）：0.35

### 步骤 5：写入关联（含合并逻辑）

对每个保留的关联，构造 `related_entities` 条目并写入两个实体。

**合并规则**（写入前检查）：

1. 读取 Entity A 现有的 `related_entities` 列表
2. 查找是否已有同一 `(type, slug)` 的条目：
   - **不存在** → 新增，`source: "auto"`
   - **存在且 source="manual"** → 跳过，不修改
   - **存在且 source="auto" 或 "M29"** → 更新 strength、dimensions，保留用户可能修改过的 relation label
   - **存在且 source="migration"** → 更新 strength、dimensions，保留原始 relation label
3. 写入 Entity A
4. 对 Entity B 执行同样的合并逻辑（双向写入）

**输出摘要格式**：
```
配对 [typeA↔typeB]: 扫描 N 对，发现 M 组新关联（强度 ≥ 阈值），更新 K 组已有关联
总计：X 组新关联，Y 组已更新
```

### 步骤 6：start sync 集成

在每日 `start` 同步检查（M28 步骤 2c）中：

1. 运行增量知识轴扫描（配对 1-3）—— 与当前 M29 行为一致
2. 运行轻量跨轴扫描（配对 4,5,7,8,10,11）—— 仅知识↔执行
3. 输出合并摘要：
   ```
   知识轴扫描：N 组新关联（高价值 M 组）| 跨轴扫描：K 组新关联
   ```
4. 对 strength ≥ 0.7 或矛盾关系 → 主动建议碰撞

### 步骤 7：auto-trigger（实体创建/修改时）

当任何实体文件被创建，或其 body/tags/summary 被修改时（chain update 触发）：

1. 仅扫描该实体 vs 全部其他类型（单实体模式，等同于 `analyze entity <slug>`）
2. 如果该实体是知识类型（idea/lit-note/perm-note），额外运行知识轴扫描
3. 不运行全量扫描
4. 静默写入，仅在发现高强度关联（≥0.7）时主动提示

---

## 迁移脚本执行步骤（migrate-relations 命令）

**前置条件**：用户已 `bf` 备份，已 git commit。

1. 读取 `migration-mapping.md`（`.recursive-planner/L0-overall-plan/migration-mapping.md`）
2. 遍历全部实体文件（~330 个），对每个文件：
   a. 读取 YAML frontmatter
   b. 按映射表提取旧字段值
   c. 构造新的 `related_entities` 条目（`source: "migration"`, `strength: 0.5`, `dimensions: []`）
   d. 如果文件已有 `related_entities`（如 ideas 从 M29）→ 合并，去重键为 `(type, slug)`
   e. 删除旧字段
   f. 写回文件
3. 输出迁移报告：文件修改数、条目创建数、条目合并数、错误（如有）
4. 建议用户 `git diff` 检查后 commit

---

## 参考文件

| 文件 | 内容 |
|------|------|
| `dimension-registry.md` | 15 配对的维度定义 + 评分算法 |
| `migration-mapping.md` | 旧字段 → related_entities 映射表 |
| `schema-audit.md` | 6 种实体类型的完整 YAML schema |
| `m29-m30-audit.md` | 现有 M29/M30 行为规范提取 |
