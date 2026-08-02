# HP-Dynamics Candidate Registry

**文件名：** `candidate_registry.md`  
**版本：** v0.1  
**用途：** 记录所有进入正式评估流程的候选系统、当前状态、Route-A / Route-B 结果、已知证据、失败控制和下一步任务。

---

## 1. 使用原则

本文件只记录已经获得唯一 `candidate_id` 的正式候选。

以下内容不应直接进入本文件：

- 尚未形成数学定义的灵感；
- 只有一句描述、没有可复现实验的想法；
- 未冻结 clock、normalization 或 determinant convention 的构造；
- 直接编码 prime / zero 表的候选；
- 未经主 Agent 接受的临时分支。

尚未成熟的想法应先放入：

```text
docs/research_clues.md
```

每个正式候选必须先经过 source lock，再进入 Route-A Skill。

---

## 2. 候选状态

每个候选只能有一个当前状态：

```text
GENERATED
STRUCTURE_PASSED
UPO_PASSED
ZETA_TRAIN_PASSED
PARAMETERS_FROZEN
VALIDATION_PASSED
ADVERSARIAL_PASSED
ANALYTIC_REVIEW
ROUTE_B_ELIGIBLE
REJECTED
STOP_SCOPED
NOT_TESTABLE
ARCHIVED
```

状态含义：

| 状态 | 含义 |
|---|---|
| `GENERATED` | 候选已定义，但尚未完成结构检查 |
| `STRUCTURE_PASSED` | 基本动力学结构、数据边界和复杂度检查通过 |
| `UPO_PASSED` | primitive orbit、repetition、stability 和完整性检查通过 |
| `ZETA_TRAIN_PASSED` | 训练区动力学 Zeta / Fredholm 指标通过 |
| `PARAMETERS_FROZEN` | 参数、cutoff、normalization 和 convention 已冻结 |
| `VALIDATION_PASSED` | 未参与拟合的 validation 区通过 |
| `ADVERSARIAL_PASSED` | 随机、打乱、邻域、精度与额外零点对照通过 |
| `ANALYTIC_REVIEW` | 正在研究解析结构与 moving-order / continuation 问题 |
| `ROUTE_B_ELIGIBLE` | Route A 已授权有限或完整 Route-B 审查 |
| `REJECTED` | 候选被反例、泄漏、不可复现或结构错误淘汰 |
| `STOP_SCOPED` | 当前方法在其假设范围内已被严格阻断 |
| `NOT_TESTABLE` | 缺少定义、数据类型、物理对象或必要 theorem |
| `ARCHIVED` | 暂停，不再分配活跃资源 |

---

## 3. Route-A 与 Route-B 结果

### Route A

使用四元组：

```text
(A1, A2, A3, A4)
```

其中：

```text
A1 — primitive-orbit layer
A2 — dynamical Zeta / Fredholm determinant layer
A3 — analytic-structure layer
A4 — natural-liftability layer
```

总体状态采用：

```text
ROUTE_A_REJECTED
ROUTE_A_EXPLORATORY
ROUTE_A_NUMERICAL_CANDIDATE
ROUTE_A_STRONG_CANDIDATE
ROUTE_A_ANALYTIC_CANDIDATE
ROUTE_A_SUCCESS_ROUTE_B_NOT_READY
ROUTE_A_SUCCESS_ROUTE_B_READY
```

### Route B

使用五元组：

```text
(B1, B2, B3, B4, B5)
```

其中：

```text
B1 — complete operator definition
B2 — self-adjointness
B3 — target spectral type
B4 — exact prime-power trace formula
B5 — completed-xi determinant/divisor equality
```

总体状态采用：

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

## 4. 候选条目模板

复制下面模板创建新候选：

```markdown
## <candidate_id> — <candidate_name>

### Identity

- **Family:** 
- **Parent candidate:** 
- **Created:** 
- **Current status:** `GENERATED`
- **Owner:** 
- **Branch:** 
- **Latest commit:** 
- **Description length:** 
- **Uses prime table:** `false`
- **Uses zero table:** `false`

### Exact definition

```text
<phase space, map/flow/operator, parameterization, boundary conditions>
```

### Source lock

```yaml
data_type:
clock:
normalization:
determinant_convention:
orbit_cutoff:
precision:
allowed_data:
forbidden_data:
training_split:
validation_split:
test_split:
stop_conditions:
```

### Motivation

- 
- 
- 

### Route-A status

```yaml
a1:
a2:
a3:
a4:
overall:
latest_evaluation:
```

### Route-B status

```yaml
b1:
b2:
b3:
b4:
b5:
overall:
latest_evaluation:
```

### Positive evidence

- 

### Failed controls

- 

### Known obstructions

- 

### Open obligations

- 

### Reproduction

```bash
<exact command>
```

### Artifacts

```text
<paths>
```

### Claim boundary

**Established:**

- 

**Not established:**

- 

### Next smallest test

- 

### Decision history

| Date | Previous state | New state | Evidence | Commit | Reviewer |
|---|---|---|---|---|---|
```

---

## 5. Registry summary

当前状态：

```text
Project initialized.
No candidate has yet passed Route A or Route B.
```

汇总表：

| Candidate ID | Family | Current state | Route A | Route B | Strongest evidence | Main blocker | Next task |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | Select first clue and create source lock |

---

## 6. 初始候选族占位

以下是候选族，不是已经通过评估的候选。

### Family A — Twisted Hénon / kicked symplectic maps

```text
Status: clue only
Expected Route-A focus: A1, A4
Main risk: generic GUE without arithmetic orbit structure
```

### Family B — Higher-memory symbolic suspension

```text
Status: clue only
Expected Route-A focus: A1, A2, A3
Main risk: hidden direct encoding of primes
```

### Family C — Low-complexity magnetic quantum graphs

```text
Status: clue only
Expected Route-A focus: A1, A2, A4
Main risk: edge lengths chosen post hoc as log primes
```

### Family D — Legacy Hardy signed-completion route

```text
Status: inherited analytic branch
Expected Route-A focus: A2, A3
Main risk: missing physical moving-order theorem
```

正式激活时必须分配具体 `candidate_id`，不能只用候选族名称进行状态升级。

---

## 7. Candidate ID 规则

建议：

```text
TH-0001    Twisted Hénon
SS-0001    Symbolic Suspension
QG-0001    Quantum Graph
KM-0001    Kicked Map
RH-LEG-001 Legacy RH branch candidate
CTRL-0001  Control
```

同一候选的小参数变化不应自动创建新 ID。

只有在以下情况创建新 ID：

- 数学定义发生结构变化；
- phase space 或 symbolic grammar 改变；
- determinant convention 改变；
- quantization 机制改变；
- parent candidate 已无法代表新构造。

---

## 8. 状态迁移规则

主 Agent 是唯一可批准状态迁移的角色。

每次迁移必须记录：

```yaml
candidate_id:
previous_state:
new_state:
date:
commit:
evaluation_file:
evidence:
failed_controls:
reviewer:
claim_boundary:
next_action:
```

不得因以下原因升级状态：

- 训练 loss 略微下降；
- 换 seed 后出现更好结果；
- 只增加绘图或文字解释；
- 只匹配更低阶零点；
- 未冻结参数的 validation；
- 未报告额外零点；
- 未完成独立复算。

---

## 9. 淘汰与重新开启

### `REJECTED`

适用：

- benchmark leakage；
- 直接编码 prime / zero；
- 独立复算失败；
- 数学定义错误；
- 额外零点严重；
- 结果完全依赖测试后调参。

### `STOP_SCOPED`

适用：

- 当前证明路线被严格 obstruction 阻断；
- 必要 absolute majorant 发散；
- wrong clock；
- incompatible determinant data types；
- theorem 假设无法推出目标结论。

### `NOT_TESTABLE`

适用：

- 物理 operator 尚未定义；
- orbit completeness 无法判断；
- 只有 abstract completion；
- 缺少 moving-order object；
- source lock 不完整。

重新开启必须写明：

```text
reopening condition
new evidence
new mathematical object
why the old obstruction no longer applies
```

---

## 10. 维护规则

更新本文件的时机：

- 新候选正式进入评估；
- Route-A 或 Route-B 有新版本；
- 候选状态变化；
- 新 obstruction 被确认；
- 参数冻结；
- 候选被淘汰或重新开启；
- 主 Agent 选择新的 next smallest test。

本文件只保留摘要。

完整评估必须保存在：

```text
evaluations/route_a/
evaluations/route_b/
```
