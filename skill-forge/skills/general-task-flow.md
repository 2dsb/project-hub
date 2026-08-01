---
id: "sk-20260515-task-flow"
slug: "general-task-flow"
title: "做事通用流程"
status: active
score: 0.35
iterations:
  count: 2
  success_count: 2
  fail_count: 0
defects: []
xp: 0
created: 2026-05-15
updated: 2026-05-26
---

# 做事通用流程

**四阶段过滤链**：任何任务/想法/机会出现时，按序通过四个阶段，不跳步、不倒置。

## 离线

**我的职责**：面对任何要做的事（包括别人安排的任务、自己冒出的想法、突然出现的机会），按以下顺序过一遍——

1. **值不值得做**：这件事做完，对目标有实质推进吗？不做会怎样？谁受益？——筛掉冲动和噪音。
2. **明确需求**：我到底要什么结果？可接受的最低标准是什么？别人（如果有）期望什么？——避免"做得很好但不是这个"。
3. **制定计划**：拆成最小可执行的步骤，排顺序，估时间。如果有依赖条件，标出来。
4. **开始执行**：按步骤做。遇到偏差回看阶段 2 的需求有没有变。

如果某件事跳过阶段 1 直接到 4（"先做了再说"），做完后发现是浪费——这就是负分信号，记录到活跃 daily 的缺陷区或当前对话的临时缺陷列表，待收尾时归入对应 skill 的 defects。

不需要每件小事都走完整流程。触发条件：预估投入 ≥ 建议值：30 分钟（经验值，可按实际情况调整），或者涉及他人协作。

## 在线

### 触发时机

用户在对话中提到要做一件事，满足以下任一条件时触发——① 用户明确说"帮我走通用流程"；② 用户表述缺少终点/底线/计划，且预估投入 ≥ 30 分钟或涉及他人协作。小事（< 30 分钟且无协作）走口头快速确认，不启动完整四阶段。

### Steps

- order: 1
  action: ""
  note: "委托给 value-judge skill 完整执行三问（目标匹配 + 后果推演 + 时机判断），给出明确结论'值得做 / 不值得做 / 推迟到 X'。若结论为'不值得做'，本 skill 终止，后续步骤自动跳过。"
  execute_skill: "value-judge"
  skill_args:
    context: "用户描述了一件要做的事。若涉及活跃项目，传入项目列表供目标匹配。"
  on_failure: "stop"

- order: 2
  action: ""
  note: "委托给 needs-clarity skill 完整执行四问（终点可视化 + 底线划定 + 决策者识别 + 驱动力判断），产出目标陈述句。若用户拒绝目标陈述句，回到阶段 1 重新判断。"
  execute_skill: "needs-clarity"
  skill_args:
    context: "从 general-task-flow 阶段 1 传入：已确认这件事值得做。"
  on_failure: "prompt"

- order: 3
  action: ""
  note: "委托给 plan-making skill 完整执行倒推拆解 + 粒度检查 + 能量排序 + 检查点设置，产出四列计划表。"
  execute_skill: "plan-making"
  skill_args:
    context: "从 needs-clarity 传入：已确认一句话目标陈述。若当日 daily 存在且含 mental_score / physical_score，传入供能量排序用；若不存在，标注'无当日能量数据'，跳过能量排序环节。"
  on_failure: "prompt"

- order: 4
  action: ""
  note: "委托给 execution-tracker skill 完整执行进度确认 + 偏差诊断（执行偏差 vs 需求偏差）+ 调整决策 + 完成收尾（更新 progress/XP + 触发 skill-collection）。遇到需求偏差时回溯到阶段 2 的目标陈述句作为锚点。"
  execute_skill: "execution-tracker"
  skill_args:
    context: "从 plan-making 传入：已确认的四列计划表。从 needs-clarity 传入：一句话目标陈述（偏差回溯的锚点）。"
  on_failure: "prompt"

## 补充规则

- 预估投入 < 30 分钟且无协作依赖的纯单人任务，可压缩为"口头过一遍"而非正式走四阶段
- 若阶段 1 判断"不值得做"但用户决定做，AI 不阻拦，但记录为负分信号（追加到活跃 daily 缺陷区或临时缺陷列表）（同上）
- 若阶段 2 需求不明确而用户坚持往下走，AI 提醒一轮即可，不反复追问
- 若任意子 skill（value-judge / needs-clarity / plan-making / execution-tracker）不存在，暂停并告知用户缺少依赖 skill，由用户决定是创建对应 skill 还是改用内联步骤替代
