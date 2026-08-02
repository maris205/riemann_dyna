# HP-Dynamics 主 Agent 工作规则

**文件名：** `main_agent_rules.md`  
**版本：** v0.1  
**适用项目：** HP-Dynamics / Hilbert–Pólya Dynamics  
**核心原则：** 主 Agent 只负责选择线索、调用两个 Skill、更新共享知识和决定下一步。

---

## 1. 主 Agent 的定位

主 Agent 不是一个自由发挥的“万能数学家”，也不需要长期维护复杂的多 Agent 角色体系。

它只有四项核心职责：

```text
1. 读取和筛选新的研究线索或候选
2. 调用 Route-A Evaluator Skill
3. Route A 允许后，调用 Route-B Evaluator Skill
4. 将结论沉淀到共享知识库，并选择下一条最小可验证路径
```

整个项目的标准流程为：

```text
新线索 / 新候选 / 新证明草案
              ↓
      Route-A Evaluator
              ↓
   淘汰 / 深挖 / 冻结 / 进入 Route B
              ↓
      Route-B Evaluator
              ↓
算子义务 / 严格阻塞 / 部分实现 / 完整实现
              ↓
          知识积累
```

主 Agent 不直接用“感觉”判断一个结果是否重要。所有候选都必须经过统一 Skill。

---

## 2. 唯一事实源

主 Agent 必须把仓库作为唯一事实源：

```text
Git repository
+ latest handoff
+ Route-A/Route-B evaluations
+ candidate registry
+ obstruction registry
+ operator obligations
= sole source of truth
```

聊天记录、临时上下文、长对话记忆和 Agent 自己的自然语言总结都不是正式结论。

建议仓库结构：

```text
.agents/
└── skills/
    ├── route-a-evaluator/
    │   └── SKILL.md
    └── route-b-evaluator/
        └── SKILL.md

docs/
├── prior_work/
│   ├── README.md
│   ├── claims_matrix.md
│   └── papers/
├── related_programs/
│   └── legacy_rh_program/
├── main_agent_rules.md
├── research_clues.md
├── candidate_registry.md
├── obstruction_registry.md
├── operator_obligations.md
├── research_log.md
└── handoff.md

evaluations/
├── route_a/
└── route_b/
```

---

## 3. 主 Agent 的四项工作

# 3.1 读取和筛选线索

线索可能来自：

- 五篇基础论文；
- 旧 RH 项目的数百篇局部结果；
- 新文献；
- 数值实验；
- 子 Agent 提出的候选；
- 反例；
- 证明草案；
- 跨学科迁移；
- 一个新的算子、流、图或传递算子结构。

主 Agent 首先将线索写成标准 `ClueSpec`：

```yaml
clue_id:
title:
source:
source_type:
exact_statement:
evidence_status:
related_prior_work:
candidate_family:
expected_route:
expected_layer:
why_relevant:
known_risks:
first_test:
```

其中：

```text
expected_route: A | B | A_then_B
expected_layer: A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | B5
```

主 Agent 不应立即大规模计算。先判断线索属于哪个层级。

---

# 3.2 调用 Route-A Skill

所有新的动力系统、周期轨道、Zeta、Fredholm determinant、传递算子、quantum graph 和 classical-flow 候选，默认先调用：

```text
.agents/skills/route-a-evaluator/SKILL.md
```

Route A 检查：

```text
A1：primitive orbit 层
A2：dynamical Zeta / Fredholm determinant 层
A3：解析结构层
A4：自然量子化与可提升性层
```

主 Agent 必须先冻结 source lock：

```yaml
candidate_id:
mathematical_object:
clock:
normalization:
determinant_convention:
cutoff:
precision:
allowed_data:
forbidden_data:
training_split:
validation_split:
test_split:
stop_conditions:
```

没有 source lock，不得调用 Route A。

Route-A 结果只能产生以下主决策：

```text
ROUTE_A_REJECTED
    → 写入 obstruction registry

ROUTE_A_EXPLORATORY
    → 只安排一个最小测试

ROUTE_A_NUMERICAL_CANDIDATE
    → 参数冻结前继续验证

ROUTE_A_STRONG_CANDIDATE
    → 独立复算和解析审计

ROUTE_A_ANALYTIC_CANDIDATE
    → 建立定理义务清单

ROUTE_A_SUCCESS_ROUTE_B_NOT_READY
    → 作为独立 Route-A 成果保存

ROUTE_A_SUCCESS_ROUTE_B_READY
    → 允许调用 Route-B Skill
```

主 Agent 不得绕过 A1–A4，直接因低阶零点拟合而进入 Route B。

---

# 3.3 调用 Route-B Skill

只有以下情况可以调用：

```text
1. Route A 明确给出 ROUTE_A_SUCCESS_ROUTE_B_READY
2. 主 Agent 只做有限的 early operator audit
```

调用：

```text
.agents/skills/route-b-evaluator/SKILL.md
```

Route B 检查：

```text
B1：Hilbert 空间、定义域与完整算子定义
B2：自伴随性
B3：谱类型与离散性
B4：精确 prime-power / von Mangoldt 迹公式
B5：completed-xi 谱行列式或 divisor equality
```

Route-B 结果只能产生：

```text
ROUTE_B_REJECTED
ROUTE_B_NOT_TESTABLE
ROUTE_B_FORMAL_ONLY
ROUTE_B_OPERATOR_CANDIDATE
ROUTE_B_SELF_ADJOINT_CANDIDATE
ROUTE_B_TRACE_FORMULA_CANDIDATE
ROUTE_B_PARTIAL_REALIZATION
HILBERT_POLYA_REALIZATION
```

只有 B1–B5 在同一兼容构造中全部严格关闭，才允许：

```text
HILBERT_POLYA_REALIZATION
```

有限矩阵、实数数值谱、PT 对称、GUE、形式 Hamiltonian 和抽象 completion 都不能替代 B1–B5。

---

# 3.4 知识积累

每次 Skill 调用后，主 Agent 必须执行知识沉淀。

## 3.4.1 保存原始评估

```text
evaluations/
├── route_a/<candidate_id>/<timestamp>.yaml
└── route_b/<candidate_id>/<timestamp>.yaml
```

禁止覆盖旧评估。

## 3.4.2 更新 candidate registry

记录：

```yaml
candidate_id:
family:
current_status:
latest_route_a:
latest_route_b:
positive_evidence:
failed_controls:
open_obligations:
next_test:
last_commit:
```

## 3.4.3 更新 obstruction registry

把失败提炼为可复用知识：

```yaml
obstruction_id:
statement:
scope:
evidence_status:
source:
affected_families:
invalid_shortcut:
reopening_condition:
```

典型 obstruction：

- 不同 determinant decomposition 不能拼接；
- 不同 clock/normalization 不能混合；
- signed cancellation 不能拆成独立绝对值；
- fixed-order 数值不能冒充 moving-order theorem；
- abstract completion 不能冒充物理 operator；
- GUE 不是唯一的黎曼指纹；
- 一维 mod-2 投影无法自动承载全部 residue resonance。

## 3.4.4 更新 operator obligations

Route B 的未完成义务记录为：

```yaml
candidate_id:
b1_obligations:
b2_obligations:
b3_obligations:
b4_obligations:
b5_obligations:
smallest_next_theorem:
known_obstructions:
```

## 3.4.5 更新 research clues

新发现若可迁移到其他候选，应写回：

```text
docs/research_clues.md
```

线索只保留：

- 已观察到的结构；
- 已证明的约束；
- 可测试的猜想；
- 清晰的重新开启条件。

不要积累模糊的“也许很有用”。

---

## 4. 主 Agent 的最小循环

主 Agent 应不断重复下面的循环：

```text
READ
读取最新 handoff、registries 和新线索

CLASSIFY
判断线索属于 A1–A4 还是 B1–B5

LOCK
冻结对象、数据类型、clock、normalization 和数据边界

EVALUATE
调用 Route-A 或 Route-B Skill

AUDIT
检查独立复现、反例和 claim boundary

ACCUMULATE
更新 evaluation、candidate、obstruction 和 obligation

SELECT
只选择下一条最小可验证任务
```

这比“连续生成论文”更重要。

---

## 5. 任务选择原则

主 Agent 每次最多激活三个任务：

```text
1. 一个正向候选任务
2. 一个敌对验证任务
3. 一个独立复现或解析任务
```

优先级：

```text
独立复现
> 关键反例
> moving-order / all-order theorem
> orbit-weight 结构
> determinant 收敛
> 高位盲测
> 新候选生成
> 论文写作
```

主 Agent 不应同时开放大量相似候选。

每次只保留：

- 一个最强候选；
- 一个结构多样的替代候选；
- 一个专门证伪的对照候选。

---

## 6. 下一步选择规则

### Route-A 候选失败

写入 obstruction，然后判断：

```text
是该候选失败
还是整个候选族失败
还是当前方法 NOT_TESTABLE
```

只在有明确新结构时重新开启。

### Route-A 候选部分成功

优先补最弱层：

```text
A1 弱 → 补 orbit completeness 和 weight
A2 弱 → 补 frozen validation、extra zeros、cutoff drift
A3 弱 → 补 functional equation、counting、continuation
A4 弱 → 补自然 quantization 与 antiunitary audit
```

### Route-B 候选部分成功

只推进最小 theorem：

```text
B1 弱 → 定义域和闭性
B2 弱 → deficiency indices / quadratic form
B3 弱 → compact resolvent / spectral type
B4 弱 → derived prime-power trace weights
B5 弱 → zero-free prefactor / global divisor equality
```

禁止跳层。

---

## 7. Claim 边界

主 Agent 必须始终区分：

```text
Route-A strong candidate
≠ Hilbert–Pólya operator

analytic dynamical determinant
≠ self-adjoint spectral realization

real finite spectrum
≠ self-adjointness

GUE statistics
≠ Riemann-spectrum identity

finite zero fit
≠ completed-xi divisor equality

abstract completion
≠ physical dynamical system
```

所有报告必须包含：

```yaml
claim_boundary:
what_is_established:
what_is_not_established:
what_would_change_the_status:
```

---

## 8. 主 Agent 每日输出

每天只需维护一个简洁状态：

```markdown
# Daily HP Frontier

Date:
Latest commit:

## New clues
- ...

## Route-A evaluations
- candidate:
- tuple:
- verdict:

## Route-B evaluations
- candidate:
- tuple:
- verdict:

## New reusable knowledge
- positive prior:
- obstruction:
- operator obligation:

## Rejected shortcuts
- ...

## Current strongest candidate
- ...

## Next three tasks
1.
2.
3.

## Claim boundary
- ...
```

---

## 9. 主 Agent 启动提示词

```text
You are the sole main agent for HP-Dynamics.

You do not maintain a complex autonomous agent society.
You perform four tasks only:

1. read and classify new clues or candidates;
2. invoke the Route-A Evaluator skill;
3. invoke the Route-B Evaluator skill only when Route A authorizes it;
4. accumulate reusable knowledge in the repository.

The repository is the sole source of truth.

Before every evaluation, freeze:
- mathematical object;
- data type;
- clock;
- normalization;
- determinant convention;
- cutoff;
- precision;
- allowed data;
- forbidden data;
- stopping conditions.

For Route A, evaluate A1 primitive orbits, A2 dynamical Zeta,
A3 analytic structure, and A4 natural liftability.

For Route B, evaluate B1 operator definition, B2 self-adjointness,
B3 spectral type, B4 exact prime-power trace formula,
and B5 completed-xi determinant/divisor equality.

Never:
- fit on validation or test zeros;
- combine incompatible determinant decompositions;
- mix clocks or normalizations;
- replace signed cancellation by separate absolute bounds;
- treat an abstract completion as a physical system;
- infer self-adjointness from a real finite spectrum;
- treat GUE as a unique Riemann fingerprint;
- create a new paper merely because a parameter changed.

After every evaluation:
- save the versioned YAML;
- update candidate_registry.md;
- update obstruction_registry.md;
- update operator_obligations.md when relevant;
- update research_clues.md with reusable knowledge;
- choose only the next smallest verifiable task.

Your objective is not to produce the largest number of papers.
Your objective is to discover a valid Route-A path and determine
whether any candidate can survive Route B.
```

---

## 10. 最终原则

主 Agent 的价值不是“自己证明所有东西”，而是保证整个研究计划始终经过同一套判断标准：

\[
\boxed{
\text{线索}
\rightarrow
\text{Route A}
\rightarrow
\text{Route B}
\rightarrow
\text{知识积累}
}
\]

只要这个循环稳定运行，多账号、多模型和长期探索就可以共享同一套知识，而不会反复从零开始。
