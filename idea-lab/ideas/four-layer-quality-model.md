---
id: idea-20260610-qc01
title: 四层产品质量模型：6种比照 + 4层自洽 = 10维审查空间
tags:
- meta-cognition
- system-design
- quality-assurance
- audit
- methodology
- framework
status: raw
created: 2026-06-10
updated: '2026-07-30'
source_type: manual
source_path: null
importance: 10
permanent_note_material: true
material_since: '2026-06-10'
material_expiry_days: 60
promoted_from: null
links: []
related_entities:
- type: idea
  slug: audit-blind-spot-spec-limitation
  relation: generalizes
  strength: 1
- type: project
  slug: project-hub
  relation: methodology-foundation-for
  strength: 1
- type: ideas
  slug: audit-blind-spot-spec-limitation
  relation: concept-relation
  strength: 0.9
  dimensions:
  - concept-relation
  - complement
  bidirectional: true
  source: auto
- type: ideas
  slug: system-coevolution
  relation: complement
  strength: 0.6
  dimensions:
  - complement
  bidirectional: true
  source: auto
- type: ideas
  slug: system-coevolution-p2-interpretability
  relation: complement
  strength: 0.55
  dimensions:
  - complement
  bidirectional: true
  source: auto
- type: ideas
  slug: system-coevolution-p4-self-reinforcement
  relation: complement
  strength: 0.55
  dimensions:
  - complement
  bidirectional: true
  source: auto
- type: ideas
  slug: knowledge-as-dictionary-of-perspectives
  relation: structural-similarity
  strength: 0.5
  dimensions:
  - concept-relation
  - structural-similarity
  bidirectional: true
  source: auto
- type: ideas
  slug: unified-python-execution-model
  relation: related
  strength: 0.5
  dimensions:
  - concept-relation
  - structural-similarity
  bidirectional: true
  source: auto
- type: ideas
  slug: abstraction-barrier-as-dual-perspective-bridge
  relation: related
  strength: 0.5
  dimensions:
  - concept-relation
  - structural-similarity
  bidirectional: true
  source: auto
- type: ideas
  slug: objective-importance-scoring
  relation: prior-art-for
  strength: 0.6
  dimensions:
  - concept-relation
  - complement
  bidirectional: true
  source: auto
- type: idea
  slug: reconnection-doc-method
  relation: overlap
  strength: 0.429
  dimensions:
  - tag-overlap
  bidirectional: true
  source: auto
---


# 四层产品质量模型：6种比照 + 4层自洽 = 10维审查空间

## 模型

任何"产品"（软件系统、文档、设计）的制作有四个层级：

```
理念 ──→ 验收标准 ──→ Spec ──→ 产品
```

| 层级 | 定义 | M34 中的例子 |
|------|------|-------------|
| **理念** | 这个产品为什么存在、它声称要实现什么根本性的承诺 | "协同进化"、"所有结构都可以改变"、"全域数据可达" |
| **验收标准** | 理念被翻译成的可测量、可判定的准则 | perfection-roadmap 的 5 条完美标准 |
| **Spec** | 具体的设计规范——怎么做、什么格式、什么算法 | `skills/coevolution-system.md` Step 1-7 |
| **产品** | 实际产出——代码、配置、文档、运行时行为 | `scripts/` + `resources/coevolution/` + 实际运行效果 |

## 六种比照方式

4 层 → C(4,2) = 6 对。这 6 种比照**穷尽了所有可能的审查类型**。不存在第 7 种。

| # | 比照对 | 审查类型 | 问题 |
|---|--------|---------|------|
| **1** | 理念 ↔ 验收标准 | **承诺翻译审查** | 理念的每一条都被正确翻译成可测量的标准了吗？有没有理念中的维度被标准遗漏了？有没有标准测量了理念不在乎的东西？ |
| **2** | 理念 ↔ Spec | **设计哲学审查** | Spec 的设计决策体现了理念吗？还是 spec 在追求工程便利而忘记了初衷？ |
| **3** | 理念 ↔ 产品 | **设计承诺审查** | 产品真的实现了理念声称的东西吗？跳过 spec，直接用理念去照产品——这是"天真用户"的视角 |
| **4** | 验收标准 ↔ Spec | **标准覆盖审查** | 每条验收标准在 spec 中都有对应的实现设计吗？spec 是否有超出验收标准的过度设计？ |
| **5** | 验收标准 ↔ 产品 | **验收测试** | 产品真的通过了验收标准吗？这是真正意义上的"测试"——不检查代码，检查行为 |
| **6** | Spec ↔ 产品 | **对照审计** | 代码和 spec 在字面上对齐吗？这是 recursive-planner 三轮审计一直在做的事 |

### 四层内部自洽性

每层除了要和另外 3 层比照，自身也可能有内部质量问题——不涉及任何其他层。C(4,2) + 4 = **10 维**，这是完整的审查空间。

| # | 审查对象 | 审查类型 | 问题 |
|---|---------|---------|------|
| **7** | 理念内部 | **哲学自洽审查** | 理念的各项声明之间有没有矛盾？"既要进化又不许改结构"——这两个承诺能共存吗？有没有承诺了自己做不到的事？ |
| **8** | 验收标准内部 | **测量完备性审查** | 每一条验收标准都是可测量的吗？标准之间有没有互相矛盾（两条标准不可能同时满足）？有没有隐式地依赖了未定义的前置条件？ |
| **9** | Spec 内部 | **设计一致性审查** | Spec 的不同章节之间有没有逻辑矛盾？某处的算法描述是否依赖了另一处未定义的概念？引用的文件和目录是否存在？ |
| **10** | 产品内部 | **工程质量审查** | 代码有没有 bug、性能问题、安全漏洞？模块边界是否清晰？即使产品和 spec 完全一致（#6 PASS），代码本身也可能有正确性之外的工程质量问题（如内存泄漏、O(n²) 复杂度、异常处理缺失） |

**完整的质量空间 = 6 种跨层比照 + 4 层内部自洽 = 10 维。** 不存在第 11 维。

## 发现过程

这个模型源于 M34 三轮完美化之后的一次元认知对话：

1. 用户问 "suggestion-templates.yaml 中的内容会进化吗？"
2. 答案是"不会"——模板文本是静态的、刚性的
3. 追问：为什么三轮审计（R1: 25发现, R2: 18发现, R3: 14发现）都没发现这个问题？
4. 根因：三轮审计只做了 **#6（Spec↔产品）**。模板刚性的发现路径是 **#3（理念↔产品）**——直接用"协同进化"这个理念去照产品，发现模板不会变
5. **如果只做 #6，这个问题永远不可能被发现**——因为 #6 的参照物里不包含"理念"

## M34 的审查覆盖现状

```
         ┌── #7: 从未做过 ❌
         │
理念 ────── 验收标准 ────── Spec ────── 产品
  │    ┌── #8: 从未做过 ❌     │     ┌── #9: 部分 ✅    │     ┌── #10: 部分 ✅
  │    │                       │     │                  │     │
  │    │   └─────∧─────────────┘     │   └─────∧────────┘     │
  │    │         #4 ❌               │         #6 ✅           │
  │    │                             │                        │
  │    └─────────∧───────────────────┘                        │
  │              #5 ❌                                        │
  │                                                           │
  └───────────────────────────────────────────────────────────┘
           #1 ❌, #2 ❌, #3: 偶发（用户触发）⚠️
```

| 维度 | 状态 | 说明 |
|------|------|------|
| #6 Spec↔产品 | ✅ 全覆盖 | 三轮 recursive-planner 审计 |
| #9 Spec 内部 | ⚠️ 部分 | 交叉引用错误被修正，但逻辑矛盾未系统检查 |
| #10 产品内部 | ⚠️ 部分 | simplify 做了重复代码检查，但性能/安全未查 |
| #3 理念↔产品 | ⚠️ 偶发 | 仅在用户主动提问时触发（如模板刚性发现） |
| #1, #2, #4, #5, #7, #8 | ❌ 从未 | 从未被系统性地执行过 |

**10 维中：1 维全覆盖，2 维部分覆盖，1 维偶发覆盖，6 维从未覆盖。**

## 推广：这不是 M34 的问题，是所有审查的规律

任何只做 #6 的审查框架（包括 recursive-planner）都有一个内在的天花板：**对照审计只能发现 spec 说了但产品没做的事，发现不了 spec 应该说要没说的事，更发现不了理念应该要求而验收标准没要求的事。**

要突破这个天花板，需要不同的审查角色和不同的参照物：

| 比照 | 需要的角色 | 参照物 |
|------|-----------|--------|
| #6 Spec↔产品 | 对照审计者（A/B/D/E） | spec + 代码 |
| #5 验收标准↔产品 | 测试执行者 | 验收标准 + 运行时数据 |
| #4 验收标准↔Spec | 需求审查者 | 验收标准 + spec |
| #3 理念↔产品 | Devil's Advocate / 天真用户 | 理念声明 + 产品行为 |
| #2 理念↔Spec | 设计哲学家 | 理念 + spec 设计决策 |
| #1 理念↔验收标准 | 产品经理 | 理念 + 验收标准 |
| #7 理念内部 | 逻辑学家 | 理念声明集合 |
| #8 验收标准内部 | 测量工程师 | 验收标准集合 |
| #9 Spec 内部 | 系统架构师 | spec 全文 |
| #10 产品内部 | 工程质量审查者 | 产品代码/配置 |

**recursive-planner 不是完整的质量保证框架——它覆盖了 #6（对照审计）+ #9 和 #10 的部分方面。** 剩下的 7 个维度需要外部审视或不读 spec 的天真视角。

## 操作化建议

对于项目中枢中的任何重要系统，审查时应该：

1. **声明覆盖范围**：明确当前审查在做哪几个维度（1-10）
2. **标记未覆盖维度**：明确哪些维度没有被检查——"零发现"不等于"零问题"
3. **周期性全维度审查**：不每次做全部 10 维（成本太高），但至少每 N 次迭代做一次 #1-#3 和 #7-#8（理念级审查）
4. **内置 Devil's Advocate**：引入一个不读 spec、只看理念和产品行为的角色（覆盖 #3）

## 关联

- 直接源于 `audit-blind-spot-spec-limitation` 的发现，将其从"M34 的一个具体缺陷"提升为"所有审查的通用框架"
- 用于项目中枢的审查方法论改进
- 可用于评估 recursive-planner 框架本身的局限性
- 与"流式思维框架"有关联：4 层可以看作一个 source→transform→spec→sink 的流图

## 重要性说明

标注为 importance: 10（最重要的），原因：

1. **这不是一个具体系统的缺陷，而是审查方法论本身的结构性框架**——影响项目中枢中所有未来系统（不仅仅是 M34）的质量保证
2. **它解释了为什么"零发现"可以是假阳性**——不是因为审查不严格，而是因为审查的维度不完整
3. **10 维是穷尽的**——C(4,2)=6 种跨层比照 + 4 层内部自洽 = 10 维。这是一个封闭的形式化模型，不会过时或需要修订（与大多数 idea 不同，这不是一个假设，而是一个完备的分类体系）
4. **直接导向可操作的改进**——每种比照对应一个具体的审查角色和输入，可以实现为 recursive-planner 的角色扩展
5. **推广到项目中枢之外**——任何有"理念层"的产品开发（游戏、写作、系统设计）都适用这个四层模型
