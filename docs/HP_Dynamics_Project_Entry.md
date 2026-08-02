# HP-Dynamics 项目入口

**项目代号：** HP-Dynamics / RiemannForge  
**核心目标：** 受理论线索约束地搜索可能实现黎曼 \(\xi\) 函数的动力学行列式，并判断其是否能够进一步提升为严格的 Hilbert–Pólya 算子。

---

## 1. 项目定位

本项目不直接要求 AI “证明黎曼猜想”。

它把问题拆成两条路线：

### Route A：发现与验证

寻找经典动力系统、符号系统、传递算子、量子图或 Fredholm 行列式，使其满足

\[
D_{\mathrm{dyn}}(s)\approx e^{g(s)}\xi(s),
\]

并在周期轨道、动力学 Zeta、解析结构和自然量子化四个层面通过验证。

### Route B：算子化与严格证明

对 Route A 的最强候选，构造

\[
H:\mathcal D(H)\subset\mathcal H\to\mathcal H,
\]

证明自伴随性、正确谱类型、精确 prime-power 迹公式，并最终证明

\[
\det_\zeta(E-H)
=
e^{q(E)}
\xi\!\left(\frac12+iE\right).
\]

Route A 成功、Route B 失败，仍然可能构成重要的“黎曼动力学行列式”成果。

---

## 2. 项目只依赖两个核心 Skills

```text
.agents/
└── skills/
    ├── route-a-evaluator/
    │   └── SKILL.md
    └── route-b-evaluator/
        └── SKILL.md
```

### Route-A Evaluator

负责：

```text
A1：primitive orbit 层
A2：dynamical Zeta / Fredholm determinant 层
A3：解析结构层
A4：自然量子化与可提升性层
```

典型输出：

```text
ROUTE_A_REJECTED
ROUTE_A_EXPLORATORY
ROUTE_A_NUMERICAL_CANDIDATE
ROUTE_A_STRONG_CANDIDATE
ROUTE_A_ANALYTIC_CANDIDATE
ROUTE_A_SUCCESS_ROUTE_B_NOT_READY
ROUTE_A_SUCCESS_ROUTE_B_READY
```

### Route-B Evaluator

负责：

```text
B1：Hilbert 空间、定义域和完整算子定义
B2：自伴随性
B3：谱类型与离散性
B4：精确 prime-power / von Mangoldt 迹公式
B5：completed-xi 行列式或 divisor equality
```

典型输出：

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

---

## 3. 主 Agent 只做四件事

```text
1. 读取并分类新线索或新候选
2. 调用 Route-A Evaluator
3. Route A 允许后调用 Route-B Evaluator
4. 将结果沉淀到共享知识库，并选择下一条最小可验证路径
```

工作循环：

```text
新线索
  ↓
分类为 A1–A4 或 B1–B5
  ↓
冻结 source lock
  ↓
调用对应 Skill
  ↓
独立复现与敌对审计
  ↓
更新知识库
  ↓
只选择下一条最小任务
```

详细规则见：

```text
docs/main_agent_rules.md
```

---

## 4. 共享知识库

### 4.1 基础论文

```text
docs/prior_work/
├── README.md
├── claims_matrix.md
└── papers/
```

五篇基础论文提供：

```text
Paper 1：prime sieve 与符号动力学线索
Paper 2：一维模型的 MSS 缺陷和 mod-2 表达上限
Paper 3：慢漂移的条件性遍历理论
Paper 4：早期谱数值实验和过拟合警告
Paper 5：面积保持 Hénon 母模板
```

这些论文是搜索先验，不是完整 Hilbert–Pólya 实现。

### 4.2 旧 RH 纵向研究路线

```text
docs/related_programs/prime_dynamics_theory/
```

旧 RH 项目提供：

- signed-completion 经验；
- wrong-clock obstruction；
- determinant-gluing 禁区；
- sideband / off-alias 问题；
- abstract completion 不等于 physical operator；
- moving-order theorem 的必要性。

### 4.3 后续线索库

```text
docs/research_clues.md
```

只保存：

- 可复用结构；
- 已证明约束；
- 可测试猜想；
- 明确 reopening condition。

### 4.4 候选、阻塞与算子义务

```text
docs/candidate_registry.md
docs/obstruction_registry.md
docs/operator_obligations.md
```

---

## 5. 标准候选流程

每个候选必须经过：

```text
GENERATED
  ↓
Route A / A1
  ↓
Route A / A2
  ↓
Route A / A3
  ↓
Route A / A4
  ↓
Route B / B1–B5
```

评估结果版本化保存：

```text
evaluations/
├── route_a/<candidate_id>/<timestamp>.yaml
└── route_b/<candidate_id>/<timestamp>.yaml
```

不得覆盖旧评估。

---

## 6. Route A 的最低判断标准

### A1：轨道层

至少检查：

\[
p\leftrightarrow\gamma_p,
\qquad
T_{\gamma_p}\approx\log p,
\]

以及：

\[
A_{\gamma_p,r}
\approx
\frac{\log p}{p^{r/2}}.
\]

必须包含：

- primitive / repetition；
- monodromy；
- stability；
- phase；
- orientation；
- multiplicity；
- orbit completeness。

### A2：动力学 Zeta 层

必须明确使用：

```text
Z
1/Z
Z'/Z
det(I-L_s)
```

中的哪一种对象。

必须经过：

```text
训练
→ 参数冻结
→ validation
→ sealed test
→ extra-zero scan
→ cutoff stability
```

### A3：解析结构层

检查：

- conjugation symmetry；
- functional equation；
- Gamma factor；
- trivial zeros；
- pole removal；
- Riemann–von Mangoldt counting；
- analytic continuation；
- moving-order control。

### A4：自然可提升性

检查：

- 是否存在自然 quantization；
- 是否有 unitary/scattering completion；
- 是否保留同一 clock 和 normalization；
- 是否明确处理 antiunitary time reversal；
- 是否存在自然 Hilbert 空间与定义域候选。

---

## 7. Route B 的最低判断标准

### B1：完整算子

必须明确：

```text
Hilbert space
measure
inner product
dense domain
boundary conditions
operator action
closedness / closability
```

### B2：自伴随性

必须真正证明：

\[
H=H^\ast.
\]

以下都不够：

```text
有限矩阵实谱
PT 对称
形式 Hermitian
对称算子
```

### B3：正确谱类型

需要：

- compact resolvent；
- 或其他严格的目标离散谱机制；
- 正确 multiplicity；
- 正确计数函数；
- 可定义的 spectral determinant。

### B4：精确迹公式

目标：

\[
\operatorname{Tr}f(H)
=
\text{smooth term}
+
\sum_p\sum_{r\ge1}
A_{p,r}\widehat f(r\log p).
\]

权重必须由系统推导，而不是人工写入。

### B5：completed-\(\xi\) 恒等式

目标：

\[
\det_\zeta(E-H)
=
e^{q(E)}
\xi\!\left(\frac12+iE\right).
\]

需要证明：

- determinant 存在；
- prefactor zero-free；
- 无额外 eigenvalues；
- 无遗漏 zeros；
- multiplicity 一致；
- 全局恒等式成立。

---

## 8. 非协商规则

任何候选都不得：

1. 使用 validation/test zeros 调参；
2. 在定义中直接读取 prime 或 zero 表；
3. 混用不同 determinant convention；
4. 混用不同 clock 或 normalization；
5. 将 signed cancellation 拆成独立绝对值；
6. 将 abstract completion 当成 physical system；
7. 将 GUE 当成唯一的黎曼指纹；
8. 将有限实谱当成自伴随证明；
9. 将固定截断结果当成 all-order theorem；
10. 隐藏额外零点、失败 seed 或数值不稳定。

---

## 9. 当前优先研究线索

优先 Route-A 候选：

```text
1. Twisted Hénon / kicked symplectic maps
2. Higher-memory symbolic suspension
3. Low-complexity magnetic quantum graphs
4. Legacy Hardy signed-completion / annular route
```

关键开放问题：

### OQ-1

能否从低复杂度规则自然产生

\[
T_{\gamma_p}=\log p
\]

而不直接编码素数？

### OQ-2

能否自然产生

\[
A_{\gamma_p,r}
\sim
\frac{\log p}{p^{r/2}}?
\]

### OQ-3

能否找到同时具有强 Route-A determinant 和自然 self-adjoint lift 的候选？

---

## 10. 项目成功等级

```text
S0：评估和计算基础设施可复现
S1：冻结参数后通过初步盲测
S2：强 Route-A 候选
S3：Route-B 部分实现
S4：完整 Hilbert–Pólya 实现
```

项目近期目标是：

```text
找到真正值得解析深挖的 Route-A 候选，
或者证明某个候选族存在明确结构性障碍。
```

---

## 11. 启动顺序

主 Agent 启动时依次读取：

```text
1. 本文件
2. docs/main_agent_rules.md
3. .agents/skills/route-a-evaluator/SKILL.md
4. .agents/skills/route-b-evaluator/SKILL.md
5. docs/research_clues.md
6. docs/prior_work/README.md
7. docs/prior_work/claims_matrix.md
8. latest handoff
9. latest candidate / obstruction / obligation registries
```

之后：

```text
选择一个线索
→ 创建 source lock
→ 调用 Route-A Skill
→ 保存 evaluation
→ 更新知识库
→ 选择下一条最小任务
```

---

## 12. 文档关系

本文件是项目入口。

原完整研究计划保留为历史设计和工程参考：

```text
docs/archive/HP_Dynamics_Research_Plan_v0.1_full.md
```

需要软件架构、完整 Loss Function、数据划分、UPO 算法、CLI、阶段计划或首批 Issues 时，再查阅该归档文件。

日常研究不再要求主 Agent 每次读取完整旧计划。

---

## 13. 一句话总结

\[
\boxed{
\text{线索}
\rightarrow
\text{Route A 发现与验证}
\rightarrow
\text{Route B 算子化与证明}
\rightarrow
\text{知识积累}
}
\]

项目不以论文数量为目标，而以找到一条真实、可证伪、可积累、可能通向 Hilbert–Pólya 的小路为目标。
