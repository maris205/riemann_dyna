# HP-Dynamics Operator Obligations

**文件名：** `operator_obligations.md`  
**版本：** v0.1  
**用途：** 记录所有 Route-B 候选尚未完成的算子理论义务、证明入口、阻塞条件和最小下一定理。

---

## 1. 使用原则

本文件不是候选列表，也不是 Route-B Skill 的替代品。

它只记录：

- 已被 Route A 授权进入 Route B 的候选；
- 或主 Agent 明确批准进行有限 early operator audit 的候选。

普通 Route-A 数值候选不应提前在此创建大量形式算子任务。

每条 obligation 必须对应：

```text
B1 — operator definition
B2 — self-adjointness
B3 — spectral type
B4 — exact trace formula
B5 — completed-xi determinant/divisor equality
```

---

## 2. 总体 Gate 映射

```text
Gate A:
canonical intrinsic dynamical spectral determinant

Gate B:
time-oriented scattering or unitary completion

Gate C:
genuine self-adjoint generator and intrinsic T log T law

Gate D:
von Mangoldt-weighted prime-power traces

Gate E:
equality with the completed-zeta divisor
```

映射关系：

```text
Route-A A1–A3  → Gate A
Route-A A4/B1 → Gate B
B2–B3         → Gate C
B4            → Gate D
B5            → Gate E
```

不同候选或不同 determinant decomposition 的局部 Gate 结果不能拼接成完整证书。

---

## 3. 义务状态

每条 obligation 使用一个状态：

```text
UNOPENED
DEFINED
PARTIAL
BLOCKED
PROVED
REFUTED
NOT_TESTABLE
STOP_SCOPED
SUPERSEDED
```

证据等级：

```text
PROVED
CONDITIONAL_THEOREM
NUMERICALLY_CERTIFIED
NUMERICAL_OBSERVATION
HEURISTIC
MODELING_CHOICE
OPEN
```

---

# 4. B1 — 完整算子定义

## B1 目标

定义：

\[
H:\mathcal D(H)\subset\mathcal H\to\mathcal H.
\]

必须明确：

```text
Hilbert space
measure
inner product
dense domain
boundary conditions
operator action
closedness or closability
spectral parameter map
relation to Route-A candidate
```

## B1 检查表

```text
[ ] Hilbert space is explicit
[ ] Inner product is explicit
[ ] Measure is explicit
[ ] Dense domain is explicit
[ ] Boundary conditions are explicit
[ ] Operator action is explicit
[ ] Closedness or closability is addressed
[ ] E ↔ 1/2+iE is explicit
[ ] Construction is natural, not post-hoc
[ ] No direct use of the zero list
```

## B1 常见阻塞

- 只有有限矩阵；
- 只有 formal Hamiltonian；
- domain 缺失；
- boundary condition 由零点拟合决定；
- classical clock 与 quantum clock 不一致；
- 量子对象与 Route-A determinant 无明确关系。

---

# 5. B2 — 自伴随性

## B2 目标

证明：

\[
H=H^\ast.
\]

或证明本质自伴随性。

可用路线：

```text
Kato–Rellich
quadratic forms
deficiency indices
boundary triplets
essential self-adjointness
unitary equivalence
canonical self-adjoint extension
bounded positive metric similarity theorem
```

## B2 检查表

```text
[ ] Symmetry is proved on the stated domain
[ ] Adjoint domain is identified
[ ] Deficiency indices are controlled, when relevant
[ ] Extension is unique or canonical
[ ] Boundary form vanishes under the chosen conditions
[ ] Perturbation assumptions are verified
[ ] PT symmetry is not used as a substitute for proof
[ ] Real numerical eigenvalues are not used as proof
```

## B2 常见错误

```text
symmetric ≠ self-adjoint
formal Hermitian ≠ self-adjoint
PT-symmetric ≠ automatically real spectrum
real finite spectrum ≠ self-adjointness
```

---

# 6. B3 — 目标谱类型

## B3 目标

证明候选具有 Hilbert–Pólya 所需的谱结构。

可能形式：

- compact resolvent；
- confining quadratic form；
- trace-class heat kernel；
- 受控离散 resonance formulation；
- 其他严格的目标谱机制。

## B3 检查表

```text
[ ] Essential spectrum is identified
[ ] Discrete spectrum is established where required
[ ] Multiplicity is controlled
[ ] Counting law is derived
[ ] Compact resolvent or equivalent mechanism is proved
[ ] Spectral determinant is well-defined
[ ] No uncontrolled spectral pollution
[ ] T log T behavior is intrinsic
```

## B3 重要规则

紧致相空间不是必要条件。

需要判断的是：

```text
the actual operator spectral type
```

---

# 7. B4 — 精确 prime-power 迹公式

## B4 目标

对合适测试函数 \(f\)，建立：

\[
\operatorname{Tr}f(H)
=
\text{smooth term}
+
\sum_p\sum_{r\ge1}
A_{p,r}\widehat f(r\log p).
\]

必须解释：

- primitive primes；
- repetitions；
- \(\log p\)；
- \(p^{-r/2}\)；
- phases；
- multiplicities；
- smooth term；
- distributional convergence。

## B4 检查表

```text
[ ] Trace is mathematically defined
[ ] Primitive and repeated contributions are separated
[ ] Weights are derived, not inserted
[ ] Same clock and normalization are used
[ ] Smooth Weyl term is correct
[ ] Error term is explicit and sufficient
[ ] Signed/complex cancellation is preserved
[ ] Local orbit identity is not promoted to global trace identity
[ ] No incompatible determinant ledgers are glued
```

## B4 常见阻塞

- 只有 Gutzwiller 类比；
- 只有有限个周期轨道；
- amplitudes 事后拟合；
- local row 被冒充为 cyclic trace；
- 取绝对值后破坏 cancellation；
- moving-order theorem 缺失。

---

# 8. B5 — completed-\(\xi\) 行列式恒等式

## B5 目标

证明：

\[
\det_\zeta(E-H)
=
e^{q(E)}
\xi\!\left(\frac12+iE\right).
\]

## B5 检查表

```text
[ ] Zeta-regularized determinant exists
[ ] Normalization is fixed
[ ] Entire prefactor is explicit
[ ] Prefactor is zero-free
[ ] Multiplicities agree
[ ] No extra eigenvalues
[ ] No missing zeros
[ ] Equality is global
[ ] Analytic continuation is controlled
[ ] Growth order is controlled
[ ] Proof does not assume RH
```

只有 B1–B5 在同一兼容构造中全部完成，才允许完整 Hilbert–Pólya claim。

---

## 9. 候选义务模板

复制下面模板：

```markdown
## <candidate_id> — Operator obligation ledger

### Route-A entry

```yaml
route_a_verdict:
route_a_tuple:
entry_authorized:
evaluation_file:
source_commit:
```

### Proposed operator

```text
Hilbert space:
Measure:
Inner product:
Operator:
Domain:
Boundary conditions:
Spectral parameter:
Relation to classical candidate:
```

### B1 — Operator definition

```yaml
status: UNOPENED
evidence_status: OPEN
proved:
open:
blocked_by:
next_smallest_theorem:
artifacts:
```

### B2 — Self-adjointness

```yaml
status: UNOPENED
evidence_status: OPEN
proposed_method:
proved:
open:
blocked_by:
next_smallest_theorem:
artifacts:
```

### B3 — Spectral type

```yaml
status: UNOPENED
evidence_status: OPEN
proposed_mechanism:
proved:
open:
blocked_by:
next_smallest_theorem:
artifacts:
```

### B4 — Trace formula

```yaml
status: UNOPENED
evidence_status: OPEN
target_formula:
proved:
open:
blocked_by:
next_smallest_theorem:
artifacts:
```

### B5 — Determinant/divisor equality

```yaml
status: UNOPENED
evidence_status: OPEN
target_identity:
proved:
open:
blocked_by:
next_smallest_theorem:
artifacts:
```

### Gate status

```yaml
gate_a:
gate_b:
gate_c:
gate_d:
gate_e:
```

### Claim boundary

**Established:**

- 

**Not established:**

- 

### Current smallest theorem

- 

### Reopening conditions

- 

### Decision history

| Date | Layer | Old status | New status | Evidence | Commit | Reviewer |
|---|---|---|---|---|---|---|
```

---

## 10. 当前状态

```text
No candidate has yet been authorized for a full Route-B evaluation.
```

当前汇总：

| Candidate | B1 | B2 | B3 | B4 | B5 | Strongest result | Main blocker | Next theorem |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | No Route-B candidate | Wait for Route-A authorization |

---

## 11. Early operator audit

主 Agent 可在 Route A 尚未完全通过时批准有限审计，但只能回答：

```text
1. 是否存在自然 Hilbert 空间？
2. 是否存在明确 operator/domain？
3. 是否有明显的 self-adjointness obstruction？
4. 是否属于已知 exact trace-formula 框架？
5. 是否值得继续 Route A？
```

early audit 不得输出：

```text
ROUTE_B_PARTIAL_REALIZATION
HILBERT_POLYA_REALIZATION
```

其结果应标记为：

```text
ROUTE_B_FORMAL_ONLY
或
ROUTE_B_NOT_TESTABLE
```

---

## 12. 最小定理原则

任何时候只推进最小未完成义务。

示例：

```text
B1 未完成
→ 不讨论 determinant equality

B2 未完成
→ 不把 real spectrum 当作 spectral host

B3 未完成
→ 不声称具有正确离散谱

B4 未完成
→ 不把 orbit analogy 当作 prime trace formula

B5 未完成
→ 不声称完成 Hilbert–Pólya
```

推荐顺序：

```text
domain
→ closedness
→ symmetry
→ self-adjointness
→ spectral type
→ counting law
→ trace formula
→ determinant identity
```

---

## 13. 维护规则

更新本文件的时机：

- Route A 授权新候选进入 Route B；
- early operator audit 被批准；
- 某个 B 层义务被证明、阻塞或否定；
- 出现新的 operator-theoretic lemma；
- Gate 状态变化；
- 候选被 Route B 淘汰；
- 新的 smallest next theorem 被确定。

完整 Route-B 评估保存于：

```text
evaluations/route_b/<candidate_id>/<timestamp>.yaml
```

本文件只保存义务摘要和当前前沿。
