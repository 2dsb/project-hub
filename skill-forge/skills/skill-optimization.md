---
id: "sk-20260515-skill-optimization"
slug: "skill-optimization"
title: "Skill 刻意优化"
status: active
score: 0.55
iterations:
  count: 1
  success_count: 1
  fail_count: 0
defects: []
xp: 10
created: 2026-05-15
updated: 2026-05-28
---

# Skill 刻意优化

**Skill 固化不是终点，是优化的起点**。用 lyra（提示词优化器）对已有 skill 进行结构化审查和改进——补漏、去冗余、提升可执行性。

## 离线

**我的职责**：使用某个 skill 时，关注以下信号——

- **输出偏差**：skill 的执行结果和我预期的不一致（比如少做了某步、顺序不对、输出格式错了）
- **卡顿感**：执行中需要我额外解释或纠正才能继续（说明 skill 的步骤描述不够清晰）
- **场景变化**：原来的 skill 是针对旧情境写的，现在情境变了但 skill 没更新
- **有新经验**：我在离线场景中实践了这个 skill，发现了更好的做法

发现信号后，记一句话：**"Skill [名称] 的 [哪个步骤] 出了问题/可以这样改进：[描述]"**。下次对话时触发本 skill。

若优化过程的 output 本身出现偏差（如 AI 未经 lyra 就给了建议、跳过了用户确认步骤），同样视为触发本 skill 的信号。

## 在线

### 触发时机

- 用户说"优化 skill X"或"审查 skill X"
- 用户在 skill 执行后给出负面评价（M20 场景 4），AI 主动建议"要不要用 lyra 审查一下这个 skill？"
- 某个 skill 的 defects 条目 ≥ 3（M20 自动触发提示"

### Steps

- order: 1
  action: "识别优化目标：和用户确认——(1) 要优化哪个 skill？(2) 当前的问题是什么？（输出偏差/卡顿/场景变化/新经验/缺陷累积）(3) 用户希望优化后达成什么效果？将目标写成一两句话，作为后续 lyra 的输入目标。"
  note: "优化不是重写。目标聚焦：解决当前问题，不随意扩大范围。"
  execute_skill: null
  skill_args: {}
  on_failure: "stop"

- order: 2
  action: "准备 lyra 输入：将目标 skill 的完整文件内容 + 优化目标 + 用户的具体反馈/缺陷记录打包，整理成 lyra 可处理的上下文。若 skill 步骤中包含嵌套引用（execute_skill），将子 skill 的核心内容摘要一并附带。"
  note: "lyra 输入必须包含三要素：目标 skill 全文 + 一句优化目标 + 所有已知反馈/缺陷。缺一则 lyra 产出可能偏离。若嵌套 skill 的步骤超过 3 步，附子 skill 摘要（标题 + 步骤数 + 核心 action 摘要）。"
  execute_skill: null
  skill_args: {}
  on_failure: "stop"

- order: 3
  action: "调用 lyra 生成优化提示词：将步骤 2 准备好的上下文（目标 skill + 优化目标 + 用户反馈/缺陷记录）传给 lyra，要求 lyra 产出一个'优化提示词'——该提示词用于指导 AI 对 skill 进行结构化审查和改进。lyra 产出后，检查提示词是否包含明确的审查指令——具体到'审查什么'和'怎么判断'。若提示词只有笼统方向、无可执行指令 → 追问 lyra 1-2 轮补充具体审查标准。"
  note: "lyra 的职责是写提示词，不是直接给建议。参考 v2→v3 经验：lyra 产出 sort-prompt，AI 用 sort-prompt 执行整理。本步骤同理。"
  execute_skill: null
  skill_args: {}
  on_failure: "prompt"

- order: 4
  action: "用优化提示词改进 skill：将 lyra 产出的优化提示词作为输入，AI 逐条执行提示词中的审查要求——分析当前 skill 的各步骤是否满足标准，输出具体修改建议（展示原内容 vs 建议修改，标注变更类型：补漏/去冗余/精确化/边界覆盖）。用户逐条确认/拒绝/修改后，将确认的变更写入 skill 文件，更新 score（+0.1~+0.5）+ `updated` 日期。"
  note: "用户判断权高于 AI 和 lyra。lyra 产出的提示词是指南，不是命令。"
  execute_skill: null
  skill_args: {}
  on_failure: "prompt"

## 补充规则

- 若 lyra 拒绝处理（输入格式不支持等），AI 自行执行手动审查：按四个维度（步骤逻辑与冗余/表述精确性/离线在线闭环/边界与失败处理）逐条输出问题 + 建议改法 + 优先级，格式同 step 4 的修改建议表
- 优化后，AI 逐条检查目标 skill 的 defects 条目。若某条对应的步骤已被修改 → 建议标记 resolved，展示给用户确认。用户确认后方可标记
- 与 skill-collection 的关系：collection 负责 0→1 创建，本 skill 负责 1→N 优化
