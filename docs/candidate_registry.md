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
Four formal Route-A candidates are registered: two symbolic baselines,
`TH-0001`, and `QG-0001`.
SS-0001 is STOP_SCOPED by the finite-state divisor-count obstruction.
SS-0002 escapes that finite-state theorem but is STOP_SCOPED by the
finite-area Selberg/Weyl divisor obstruction.
CTRL-0001 is a passed-with-limitations A2 evaluator positive control, explicitly not a formal
candidate and not eligible for an SS candidate number.
P4-LOGISTIC-MONOTONE-CLOCK-LIFT is a non-candidate structural audit:
it is STOP_SCOPED under OBR-007 and does not change the formal-candidate count.
P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK is a second non-candidate structural
audit: it escapes OBR-007 with genuine recurrent tower orbits, but remains
REVISE / ROUTE_A_EXPLORATORY and does not change the formal-candidate count.
Its physical exact-(U_c) first-return alphabet, asymptotic physical mass ratio,
and explicit adjacent-ratio convergence rate are proved, while an exact
finite-order mass law, the modeled tower coupling, and the arithmetic
interpretation remain open.
P4-LOGISTIC-UC-POLAR-INTRINSIC-ROOF is a lock-only continuation. It freezes a
doubled polar Markov phase space, the intrinsic positive roof `tau=log|G'|`,
separate physical and suspension clocks, one analytic Banach space, and one
conditional Fredholm convention. It is `DEFINED_NOT_EVALUATED`, is not a
formal candidate, and does not change the inherited Route-A tuple.
P4-LOGISTIC-UC-POLAR-NONLATTICE is the completed sealed-word audit. It proves
the full primitive periods for `R` and `LR` have irrational ratio, so the
intrinsic roof is non-lattice. This is a `PROVED` positive structural prior,
not an A2 determinant pass or a new formal candidate.
P4-LOGISTIC-UC-POLAR-COMPLEX-BRANCH is the completed frozen-radius complex
audit. At the unchanged `epsilon=1/1000` it proves one common holomorphic
`a`/`Log(a)`, two globally univalent signed composite inverse branches, all
four compact inclusions, and matching-space invariance. It is a `PROVED`
positive structural prior, not a nuclearity or determinant pass and not a new
formal candidate.
TH-0001 is the first formal Hénon-family candidate. It freezes one target-free
autonomous non-palindromic three-kick superstep, has a complete global signed
real primitive-orbit prefix through G-period two, and now has a proved
same-order unitary Fourier-integral lift on L2(R). Its superseding Route-A
tuple is `(A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)` /
`ROUTE_A_EXPLORATORY` with `GO_WITH_LIMITATIONS`; no arithmetic orbit law or
determinant is supplied. `OBR-011` now proves that the ordered three-kick
kernel cannot be globally reduced to one nondegenerate phase chart; the
factorized unitary remains valid and Route B remains closed.
QG-0001 is the first formal magnetic-quantum-graph candidate. It freezes an
asymmetric squarefree lollipop-theta graph and its exact harmonic `1/n` scale
tower. The natural direct-sum magnetic Laplacian is self-adjoint with compact
resolvent and has the target-free all-order count `Theta(K log K)`, but its raw
coefficient is wrong. `OBR-012` proves that the naive unregularized Euler
product has no finite nonzero value and that the standard direct-sum bond
operator is not trace class. The base-component sinc audit now also proves
that the bond zero at `k=0` is exactly double and spurious, and supplies an
entire normalized physical characteristic. The final same-operator audit
proves that `H^{-1}` is trace class and opens the exact relative determinant
`det_F(I-k^2 H^{-1})=product_n chi_0(k/n)`. Its analytic audit tuple is
`(A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE,
A4_UNITARY_OR_SCATTERING_CANDIDATE)`, but the target interpretation remains
`(A1_WEAK, A2_FAIL, A3_FAIL, A4_UNITARY_OR_SCATTERING_CANDIDATE)`: the exact
divisor coefficient is wrong by the immutable factor `2*L_0`. QG-0001 is
therefore `STOP_SCOPED` / `ROUTE_A_REJECTED`; Route B remains closed.
No candidate has entered Route B.
```

The Logistic clock-lift audit is intentionally not given a candidate entry.
Its strict-monotone base confines every full periodic orbit to the static-limit
slice, and its formal orbit determinant adds no data beyond that parent. It is
tracked in `docs/research_clues.md`, `docs/obstruction_registry.md`, and the
Route-A evaluation tree rather than promoted to `SS-0003` or another formal ID.

The recurrent exact-(U_c) audit is also intentionally not promoted. Its
modeled all-even tower has an exact primitive census and full-fibre witnesses.
The later support audit proves that the physical invariant core has exactly one
nondegenerate interval branch per even return label and no odd branch; ambient
odd branches are transient and have zero mass for every invariant probability.
Each physical branch maps diffeomorphically onto the full event interior, so
every finite return-label word has a nonempty open cylinder. This upgrades the
finite-word alphabet provenance from a modeling choice to `PROVED`, but
the subsequent endpoint-density theorem now also proves existence and full
support of the physical acip, positivity of every physical branch, and the
asymptotic mass ratio
`1/(2*U_c*(U_c-1))`. The later polar-cone audits additionally give target-free
certified enclosures of `h(0)`, the absolute endpoint coefficient, and finite
physical masses for returns 12, 14, 16, and 18. The validated sharp audit uses
a complete Arb cover to obtain `0.20655<h(0)<0.40008`. It does not supply a
finite-rank/resolvent enclosure, the modeled tower measure/coupling, an
arithmetic primitive-orbit correspondence, or a
determinant. A later cusp-adapted audit now proves an explicit adjacent
physical-mass-ratio rate from branch index 6 onward, but it does not restore
the ordinary-`BV` spectral argument or give an exact finite-order mass law. The
unaccelerated induced map remains blocked as an ordinary
uniformly expanding `BV` map by `OBR-009`, and the old unit return-label clock
remains blocked by `OBR-008`. The exact polar roof now escapes the hypothesis
of `OBR-008`: its sealed `R` and `LR` periods are proved rationally
independent. The frozen complex audit now also supplies the same-object
radius-`1/1000` transfer-operator domain, common logarithm germ, compact
branch inclusion, and matching-space invariance. It does not supply the
doubled partition-hit trace ledger, nuclearity, a Fredholm determinant, or a
divisor-count theorem. The audit remains
`P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK`, with Route-A tuple
`(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` and verdict `REVISE`.

The follow-up `P4-LOGISTIC-UC-POLAR-PARTITION-TRACE` audit freezes the
geometric half-open convention `I_L=[-pi/2,0)`, `I_R=[0,pi/2]`, proves the
exact boundary graph `P->P`, `Q->P`, `Z->Q`, and shows that the partition point
is preperiodic. It also certifies cyclic-word and endpoint-copy quotient
bookkeeping through length eight and proves that the weighted-family range lies
in the matching kernel. This is a geometric ledger result only: the local
analytic trace correction at the boundary fixed point remains `OPEN`, so no
determinant or Route-B status changes.

Latest evaluation:

```text
evaluations/route_a/P4-LOGISTIC-UC-POLAR-PARTITION-TRACE/20260807T032000Z.yaml
```

The polar suspension source lock is
`configs/source_locks/P4-LOGISTIC-UC-POLAR-INTRINSIC-ROOF.yaml` at source
commit `4d5cd7e346445317d2ed19ef90a484cca09c3588`. Lock v2 clarifies the
composite complex branches, exact physical conjugacy, one-way witness logic,
and deferred partition-hit trace ledger without changing the real map or roof.

The completed non-lattice theorem is recorded at source commit
`36a38f0db16652bf0e0c1459be6c69f6bdafec12` with exact multiplier
polynomials, finite-field irreducibility gates, and a common-field norm proof.

The completed complex-branch theorem is recorded at source commit
`3ae5e23508e27129cfa5910473b944026b904ea3`. It keeps
`epsilon=1/1000`, proves a common complex contraction below `0.59626`, and
gives a compact margin above `0.00040374` for all four branch pairs.

Next smallest test: derive the local matching-space trace correction at the
boundary fixed point `P=-pi/2` under the frozen half-open ledger. Do not audit
nuclearity, Fredholm zeros, target divisors, or Route B before that identity.

Portfolio decision: under the RH breadth-first rule, this is the
candidate-local resume task only. The project-level next task parks the
Logistic branch and opens `CLUE-A4-001` to freeze one explicit target-free
Twisted Hénon / kicked-symplectic object for a low-cost Route-A prefilter.

汇总表：

| Candidate ID | Family | Current state | Route A | Route B | Strongest evidence | Main blocker | Next task |
|---|---|---|---|---|---|---|---|
| QG-0001 | Harmonic magnetic lollipop-theta graph tower | `STOP_SCOPED` (exact relative determinant and divisor) | Analytic `(A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_UNITARY_OR_SCATTERING_CANDIDATE)`; target `A2/A3_FAIL` / `ROUTE_A_REJECTED` | Not invoked | `H^{-1}` trace class and exact `det_F(I-k^2 H^{-1})=product_n chi_0(k/n)` | Exact divisor coefficient is `2*L_0 ~= 12.7647` times target; no orbit trace law | Park; reopen only as a new lock with intrinsic normalization/tower law |
| TH-0001 | Target-free non-palindromic three-kick Hénon ratchet | `ANALYTIC_REVIEW` (UPO cutoff still <=2) | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)` / `ROUTE_A_EXPLORATORY` | Not invoked | Exact symplecticity, complete signed UPO prefix, unitary FIO lift, and exact internal-caustic obstruction | No determinant, arithmetic orbit law, higher-period completeness, or full nonlinear antiunitary audit | Stop phase sub-audit; reopen only with an explicit multi-chart phase/Maslov ledger |
| SS-0001 | Higher-memory symbolic suspension control | `STOP_SCOPED` | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` / `ROUTE_A_REJECTED` | Not invoked | Exact mod-3 modes, orbit census, determinant, and scoped family theorem | Finite-state finite-dimensional roof determinants have `O(T)` divisor count | Wait for an explicit countable-state or infinite-dimensional escape object |
| SS-0002 | Countable-state symbolic suspension / modular transfer operator | `STOP_SCOPED` | `(A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)` / `ROUTE_A_REJECTED` | Not invoked | Exact C6 holonomy, nuclear Fredholm determinant, Selberg identity, and natural Laplacian | Same determinant has at least `Omega(T^2)` Selberg spectral zeros, not `Theta(T log T)` | Define one explicit non-Selberg nuclear object and prove its own divisor-count regime before assigning SS-0003 |

Evaluator controls are tracked separately and do not change the formal-candidate count:

| Control ID | Role | Control verdict | Candidate scope | Strongest evidence | Main limitation |
|---|---|---|---|---|---|
| CTRL-0001 | Four-channel q-Pochhammer Fredholm A2 positive control | `GO_WITH_LIMITATIONS` | `STOP_SCOPED`; not a formal candidate | Independent direct-product winding and Fredholm-coefficient root discovery pass all frozen gates, including balanced corruption and executable ledger controls | Sampled winding is a numerical anti-alias diagnostic, not an interval proof; engineered factors have no natural prime orbit or completed-xi structure |

---

## QG-0001 — Harmonic magnetic lollipop-theta tower

### Identity

- **Family:** Low-complexity magnetic quantum graph
- **Parent clue:** `CLUE-A4-003`
- **Created:** 2026-08-06
- **Current status:** `STOP_SCOPED` (exact same-operator determinant has the wrong frozen divisor count)
- **Owner:** sole main research agent
- **Branch:** `main`
- **Latest source commit:** `b5ad4c9ce4305cf055a2e6a3ae957ba4fda7e90b`
- **Uses prime table:** `false`
- **Uses zero table:** `false`

### Exact definition

The base graph has three `L--R` edges and one `L--D` pendant:

\[
(\ell_0,\ell_1,\ell_2,\ell_3)=(1,\sqrt2,\sqrt3,\sqrt5),
\qquad
(\alpha_0,\alpha_1,\alpha_2,\alpha_3)
=\left(0,\frac\pi3,\frac{2\pi}3,0\right).
\]

Vertices `L,R` have covariant Kirchhoff conditions of degrees four and
three; `D` is Dirichlet. Component `n>=1` scales every metric length by
`1/n` while keeping the listed L-outward magnetic line integrals fixed. The
candidate is the disjoint union of all components. Its raw orbit clock is
metric length and its quantum spectral variable is positive wavenumber
`K=sqrt(lambda)`.

### Source lock

```text
configs/source_locks/QG-0001.yaml
configs/source_locks/QG-0001-BASE-CHARACTERISTIC.yaml
configs/source_locks/QG-0001-RELATIVE-FREDHOLM.yaml
```

The current determinant convention is
`D_H(k)=det_F(I-k^2 H^{-1})=det_rel(H-k^2,H)`. It equals the normally
convergent component product `product_n chi_0(k/n)`. This determinant is kept
separate from the failed primitive-orbit Euler product, the non-trace-class
direct-sum bond blocks, and the heat/spectral zeta. Prime/zero tables, fitted
graph scales, nonlinear clock changes, and ledger mixing remain forbidden.

### Route-A status

```yaml
a1: A1_WEAK
a2: A2_ANALYTIC_DETERMINANT (target interpretation A2_FAIL)
a3: A3_PARTIAL_ANALYTIC_STRUCTURE (target interpretation A3_FAIL)
a4: A4_UNITARY_OR_SCATTERING_CANDIDATE
overall: ROUTE_A_REJECTED
scoped_verdict: STOP_SCOPED
latest_evaluation: evaluations/route_a/QG-0001/20260806T123946Z.yaml
```

### Route-B status

```yaml
b1: NOT_INVOKED
b2: NOT_INVOKED
b3: NOT_INVOKED
b4: NOT_INVOKED
b5: NOT_INVOKED
overall: NOT_INVOKED
latest_evaluation: null
```

### Positive evidence

- Exact exhaustive enumeration gives 10, 45, and 330 primitive oriented
  orbits at topological periods 2, 4, and 6. Direct based-word traces agree
  with the primitive/repetition ledger at every period through six.
- The 6-by-6 sinc-matching matrix defines an even entire base characteristic
  \(\mathcal C_{\rm phys}(k)\) at all wavenumbers, including `k=0` and
  individual edge-Dirichlet points. Exact algebra gives

  \[
  \Delta_{\rm bond}(k)
  =-\frac43 k^2e^{ikL_0}\mathcal C_{\rm phys}(k),
  \qquad
  \mathcal C_{\rm phys}(0)
  =\sqrt2+\sqrt3+\sqrt5+\sqrt6+\sqrt{15}+3\sqrt{10}>0.
  \]

  Thus the bond zero at `k=0` is exactly double and spurious. After dephasing,
  \(\chi_0(k)=1-4.4035597019537134\ldots k^2+O(k^4)\).
- The asymmetric degree/boundary decoration has only the identity graph
  automorphism, and the flux class is not gauge equivalent to its negative;
  the inherited local geometric antiunitary class is excluded.
- Closed magnetic forms define self-adjoint component Laplacians with
  \(H_n\simeq n^2H_1\). The Dirichlet terminal gives a positive base gap;
  together with this exact scaling, it makes the direct-sum resolvent compact.
- In fact, the inverse is trace class:

  \[
  \operatorname{Tr}(H^{-1})
  =\zeta(2)\operatorname{Tr}(H_1^{-1})
  =7.2435653691436857\ldots.
  \]

  Complete divisor and growth control prove

  \[
  \chi_0(k)=\det_F(I-k^2H_1^{-1}),
  \qquad
  D_H(k)=\prod_{n\geq1}\chi_0(k/n)
  =\det_F(I-k^2H^{-1}).
  \]

  The factorwise `exp(-i*k*L_0/n)` counterphase is forced by the exact bond
  identity. In `k`, the product has genus one, order one, and infinite type;
  in `k^2`, it has genus zero and order one-half.
- With `L_0=1+sqrt(2)+sqrt(3)+sqrt(5)`, the positive-wavenumber count is

  \[
  N_H(K)=\frac{L_0}{\pi}K\log K+O(K).
  \]

  Thus the target `K log K` exponent arises without arithmetic target data.

### Failed controls and known obstructions

- Primitive metric periods `L_p/n` accumulate at zero and have no
  log-prime or von-Mangoldt law.
- The exact pendant bounce has weight `1/2` and period `2*sqrt(5)/n`.
  Therefore the naive Euler product has no finite nonzero value. For the
  standard component bond block, the trace norm tends to `8`, so its direct
  sum is not trace class and has no standard Fredholm determinant (`OBR-012`).
- The genuine Fredholm divisor has positive roots `n*sqrt(lambda_j(H_1))`
  and its exact counting coefficient is larger than the positive Riemann-zero
  coefficient by the factor `2*L_0 ~= 12.7646646949`. No rescaling is
  permitted and no zero-free factor can repair the divisor (`OBR-013`).
- The identity `zeta_H(z)=zeta(2z)*zeta_H1(z)`
  is a heat/spectral-zeta identity in the exponent variable, not a secular
  divisor in `K`.
- The Fredholm logarithm contains inverse spectral moments; no theorem
  identifies them with the frozen primitive-orbit periods and signed weights.
- An abstract spectral-basis conjugation necessarily exists for this
  self-adjoint compact-resolvent operator, but no local, geometric, or
  orbit-reversal interpretation is asserted. A prime-power trace formula,
  completed-ξ structure, and Route B remain absent.

### Reproduction

```bash
python3 experiments/qg_0001_harmonic_magnetic_tower.py \
  --quiet \
  --output artifacts/qg_0001/route_a_prefilter.json
python3 -m unittest -v tests/test_qg_0001_harmonic_magnetic_tower.py
python3 experiments/qg_0001_base_characteristic.py \
  --quiet \
  --output artifacts/qg_0001/base_characteristic_zero.json
python3 -m unittest -v tests/test_qg_0001_base_characteristic.py
python3 experiments/qg_0001_relative_fredholm.py \
  --quiet \
  --output artifacts/qg_0001/relative_fredholm.json
python3 -m unittest -v tests/test_qg_0001_relative_fredholm.py
python3 -m unittest discover -v
```

### Artifacts

```text
configs/source_locks/QG-0001.yaml
configs/source_locks/QG-0001-BASE-CHARACTERISTIC.yaml
configs/source_locks/QG-0001-RELATIVE-FREDHOLM.yaml
evaluations/route_a/QG-0001/20260806T090351Z.yaml
evaluations/route_a/QG-0001/20260806T111927Z.yaml
evaluations/route_a/QG-0001/20260806T123946Z.yaml
experiments/qg_0001_harmonic_magnetic_tower.py
experiments/qg_0001_base_characteristic.py
experiments/qg_0001_relative_fredholm.py
artifacts/qg_0001/route_a_prefilter.json
artifacts/qg_0001/base_characteristic_zero.json
artifacts/qg_0001/relative_fredholm.json
formal/results/qg_0001_harmonic_magnetic_tower.md
formal/results/qg_0001_base_characteristic_zero.md
formal/results/qg_0001_relative_fredholm.md
formal/obstructions/harmonic_graph_tower_naive_determinant.md
tests/test_qg_0001_harmonic_magnetic_tower.py
tests/test_qg_0001_base_characteristic.py
tests/test_qg_0001_relative_fredholm.py
```

### Claim boundary

**Established:** one explicit target-free infinite magnetic graph, an exact
signed/oriented primitive prefix, the local geometric antiunitary obstruction,
a natural self-adjoint compact-resolvent operator, the all-order `K log K`
counting exponent, failure of the naive Euler product, and failure of trace
class for the standard direct-sum bond operator. The base physical
characteristic, exact spurious bond-zero order, trace-class inverse, exact
same-operator relative determinant, complete divisor, genus/order ledger, and
strict frozen coefficient obstruction are also established.

**Not established:** an arithmetic orbit law, a primitive-orbit trace identity,
the correct leading coefficient, a completed-ξ divisor, Route B,
Hilbert–Pólya, or RH. The exact determinant proves that the correct leading
coefficient cannot arise within this lock.

### Reopening condition and project next task

QG-0001 has no further candidate-local task under the frozen normalization:
the exact divisor obstruction is decisive. Reopen only with an intrinsically
different graph normalization or component law fixed before target data; that
is a new source lock. The project-level next task pivots to `CLUE-A3-001` and
inspects the legacy RH handoff for one explicit same-ledger annular residual
object before creating a formal candidate.

### Decision history

| Date | Previous state | New state | Evidence | Commit | Reviewer |
|---|---|---|---|---|---|
| 2026-08-06 | `ANALYTIC_REVIEW` | `STOP_SCOPED` | Exact trace-class relative determinant and immutable divisor-count obstruction | `b5ad4c9ce4305cf055a2e6a3ae957ba4fda7e90b` | sole main research agent |
| 2026-08-06 | `ANALYTIC_REVIEW` | `ANALYTIC_REVIEW` | Exact sinc-matching base characteristic; spurious bond zero removed with normalized Taylor ledger | `af41439b609a5dfb863931ed1e56a0598de5f003` | sole main research agent |
| 2026-08-06 | `GENERATED` | `ANALYTIC_REVIEW` | Exact Route-A structural prefilter; intrinsic `K log K` count and `OBR-012` | `ce0d4424a95a9392c9e8755a4a11b1cfcabc0e77` | sole main research agent |

---

## TH-0001 — Target-free non-palindromic three-kick Hénon ratchet

### Identity

- **Family:** Twisted Hénon / kicked symplectic map
- **Parent clue:** `CLUE-A4-001`
- **Created:** 2026-08-06
- **Current status:** `ANALYTIC_REVIEW` (UPO completeness remains strictly scoped to frozen `G`-period `<=2`)
- **Owner:** sole main research agent
- **Branch:** `main`
- **Latest commit:** `a4cb10640c44559f0520386d9c84e65c9b873134`
- **Uses prime table:** `false`
- **Uses zero table:** `false`

### Exact definition

On \((\mathbb R^2,dq\wedge dp)\), let

\[
F_a(q,p)=(1-aq^2-p,q),
\qquad
G=F_{5/2}\circ F_{3/2}\circ F_{1/2}.
\]

One application of `G` is the only clock unit. The half-integer ramp is a
target-free `MODELING_CHOICE`; it is not a claimed natural arithmetic constant.

### Source lock

```text
configs/source_locks/TH-0001.yaml
```

The lock fixes exact rational polynomial data, signed raw-coordinate
normalization, `determinant_convention: NOT_OPENED`, and complete real primitive
periods only through two `G`-supersteps. Prime/zero/GUE/USTC data and all
legacy fitted parameters are forbidden.

### Route-A status

```yaml
a1: A1_WEAK
a2: A2_FAIL
a3: A3_FAIL
a4: A4_NATURAL_QUANTIZATION
overall: ROUTE_A_EXPLORATORY
scoped_verdict: GO_WITH_LIMITATIONS
latest_evaluation: evaluations/route_a/TH-0001/20260806T053410Z.yaml
```

### Route-B status

```yaml
b1: NOT_INVOKED
b2: NOT_INVOKED
b3: NOT_INVOKED
b4: NOT_INVOKED
b5: NOT_INVOKED
overall: NOT_INVOKED
latest_evaluation: null
```

### Positive evidence

- Each kick is exact-symplectic and has the common generating function
  \(S_a(q,Q)=qQ-q+(a/3)q^3\); `G` is an exact-symplectic polynomial
  automorphism of algebraic dynamical degree eight.
- The inherited swap reversor fails at an exact witness point, and all affine
  anti-symplectic involutions are excluded by highest-degree comparison.
- Exact Groebner/Sturm elimination gives four primitive real period-one
  orbits and eight primitive real period-two orbits, globally on \(\mathbb R^2\)
  with no search box or random seed. All 20 phase points are hyperbolic.
- The same generating functions define
  \(U_a=\mathcal F_+M_a\) on \(L^2(\mathbb R)\) with positive-real
  normalization; Plancherel and modulus-one multiplication prove each factor
  and the ordered three-kick product are everywhere-defined unitaries.
- The natural parent-swap antiunitary \(A=\mathcal F_+C\) is an involution and
  reverses each kick, but its inverse word does not reverse the non-palindromic
  superstep. The inherited cyclic clock-reflection class is excluded.
- The ordered three-kick phase has internal Hessian determinant
  \(15q_1q_2-1\), with exact caustic witness \((1,1/15)\). This strictly
  blocks a global single reduced phase while leaving factorized unitarity intact.

### Failed controls and known obstructions

- No prime-like period law, von-Mangoldt repetition weight, or higher-period
  completeness is established; A1 remains `A1_WEAK`.
- No determinant or analytic structure has been opened; A2 and A3 are
  `FAIL`/`NOT_TESTABLE` by design.
- `OBR-010` excludes the audited low-depth legacy one-/two-kick reversible
  subclasses and affine reversors, but arbitrary nonlinear or non-polynomial
  anti-symplectic reversors remain an open obligation.
- The unitary FIO is a Floquet propagator, not a self-adjoint Hamiltonian;
  no logarithm branch, spectral type, determinant, or Route-B domain is frozen.
- `OBR-011` forbids a global single-phase/Maslov ledger under the current chart.
  Reopening requires an explicit multi-chart caustic-transition construction.

### Reproduction

```bash
python3 experiments/th_0001_three_kick_henon.py \
  --quiet \
  --output artifacts/th_0001/route_a_prefilter.json
python3 -m unittest -v tests/test_th_0001_three_kick_henon.py
python3 -m unittest discover -v
```

### Artifacts

```text
evaluations/route_a/TH-0001/20260806T024238Z.yaml
evaluations/route_a/TH-0001/20260806T045554Z.yaml
evaluations/route_a/TH-0001/20260806T053410Z.yaml
artifacts/th_0001/route_a_prefilter.json
artifacts/th_0001/fio_quantization_audit.json
artifacts/th_0001/phase_caustic_audit.json
formal/results/th_0001_three_kick_prefilter.md
formal/results/th_0001_fio_quantization.md
formal/obstructions/low_depth_henon_reversibility.md
formal/obstructions/th_0001_single_phase_caustic.md
configs/source_locks/TH-0001-FIO.yaml
experiments/th_0001_fio_quantization.py
experiments/th_0001_phase_caustic_audit.py
tests/test_th_0001_three_kick_henon.py
tests/test_th_0001_fio_quantization.py
tests/test_th_0001_phase_caustic_audit.py
```

### Claim boundary

**Established:** one frozen autonomous target-free map, exact symplecticity and
inverse, low-complexity reversibility obstruction, a complete signed real
primitive-orbit prefix through `G`-period two, and a same-order unitary
Fourier-integral lift on `L^2(R)` with the inherited antiunitary class audited.

**Not established:** arbitrary nonlinear time-reversal breaking or antiunitary
exclusion, arithmetic orbit correspondence, any Zeta/Fredholm determinant,
global analytic structure, self-adjoint Hamiltonian, Route B, Hilbert--Pólya,
or RH.

### Next smallest test

Stop the phase sub-audit at `OBR-011`. Reopen it only with an explicit
multi-chart phase/Maslov ledger and caustic transition rules; otherwise apply
the breadth rule to a new candidate. Do not compute a spectrum or determinant.

### Decision history

| Date | Previous state | New state | Evidence | Commit | Reviewer |
|---|---|---|---|---|---|
| 2026-08-06 | `GENERATED` | `UPO_PASSED` (cutoff-scoped) | Exact Route-A prefilter; `A1_WEAK/A2_FAIL/A3_FAIL/A4_FORMAL_HINT` | `fb69649afbda27006d56471c5680b590f90ba43b` | sole main research agent |
| 2026-08-06 | `UPO_PASSED` (cutoff-scoped) | `ANALYTIC_REVIEW` | Same-order unitary FIO and inherited antiunitary audit; `A4_NATURAL_QUANTIZATION` | `836f5880fac6abfb29ee031e1136e24504e2b0a9` | sole main research agent |
| 2026-08-06 | `ANALYTIC_REVIEW` | `ANALYTIC_REVIEW` | `OBR-011`: exact internal caustic blocks global single-phase reduction; tuple unchanged | `a4cb10640c44559f0520386d9c84e65c9b873134` | sole main research agent |

---

## SS-0001 — Mod-6 Cayley symbolic-suspension baseline

### Identity

- **Family:** Higher-memory symbolic suspension control
- **Parent candidate:** 1D mod-2 projection clue
- **Created:** 2026-08-02
- **Current status:** `STOP_SCOPED`
- **Owner:** sole main research agent
- **Branch:** `main`
- **Latest commit:** current `HEAD` (research content introduced in `5abca8f`)
- **Uses prime table:** `false`
- **Uses zero table:** `false`

### Exact definition

The base is the directed Cayley graph

\[
\operatorname{Cay}(\mathbb Z/6\mathbb Z,\{+1,-1\}),
\]

with the left shift on bi-infinite admissible paths, constant suspension roof
\(\tau=1\), zero potential, and adjacency matrix \(A\). The frozen determinant is

\[
D(s)=\det(I-e^{-s}A).
\]

### Source lock

```text
configs/source_locks/SS-0001.yaml
```

### Route-A status

```yaml
a1: A1_WEAK
a2: A2_FAIL
a3: A3_FAIL
a4: A4_FORMAL_HINT
overall: ROUTE_A_REJECTED
latest_evaluation: evaluations/route_a/SS-0001/20260802T163302Z.yaml
```

### Route-B status

```yaml
b1: NOT_INVOKED
b2: NOT_INVOKED
b3: NOT_INVOKED
b4: NOT_INVOKED
b5: NOT_INVOKED
overall: NOT_INVOKED
latest_evaluation: null
```

### Positive evidence

- The mathematical object is parameter-free and does not query primes or zeros.
- Primitive and repeated orbit counts are exactly reproducible by adjacency traces and Möbius inversion.
- Nontrivial mod-3 Fourier modes occur, so residue memory can be added without directly encoding a prime table.
- The determinant is exact:
  \(D(s)=(1-4e^{-2s})(1-e^{-2s})^2\).

### Failed controls and obstructions

- All odd symbolic periods vanish because the graph is bipartite.
- The clock is integral and supplies no intrinsic \(\log p\) mechanism.
- The divisor is a finite union of vertical arithmetic progressions.
- The zero count is \(O(T)\), not the Riemann-von Mangoldt \(\Theta(T\log T)\) count.
- The canonical graph adjacency quantization is finite-dimensional and cannot open Route B.

### Reproduction

```bash
python3 -m unittest -v tests/test_ss_0001_mod6_cayley.py
python3 experiments/ss_0001_mod6_cayley.py --max-period 24 --output artifacts/ss_0001/route_a_baseline.json
```

### Claim boundary

**Established:** SS-0001 is exactly analyzable, contains mod-3 character modes, and is structurally incompatible with the completed-\(\xi\) divisor.

**Not established:** the result does not yet cover countable-state systems, unbounded roofs, non-locally-constant potentials, or infinite-dimensional nuclear transfer operators.

### Next smallest test

Do not create `SS-0002` until a countable-state or infinite-dimensional
mathematical object has an explicit intrinsic clock and determinant convention
that lies outside the proved finite-state obstruction.

### Decision history

| Date | Previous state | New state | Evidence | Commit | Reviewer |
|---|---|---|---|---|---|
| 2026-08-02 | `GENERATED` | `STOP_SCOPED` | Exact determinant and divisor-count mismatch | `5abca8f` | sole main research agent |
| 2026-08-02 | `STOP_SCOPED` | `STOP_SCOPED` | Family-level finite-state finite-roof zero-count theorem | `5abca8f` | sole main research agent |

---

## SS-0002 — Paired-Gauss commutator-cover Mayer operator

### Identity

- **Family:** Countable-state symbolic suspension / modular transfer operator
- **Parent candidate:** `SS-0001` and the `CLUE-A1-002` reopening condition
- **Created:** 2026-08-03
- **Current status:** `STOP_SCOPED`
- **Owner:** sole main research agent
- **Branch:** `main`
- **Latest commit:** current checkpoint; source state `934d85c`
- **Uses prime table:** `false`
- **Uses zero table:** `false`

### Exact definition

Let

\[
\Gamma=\operatorname{PSL}_2(\mathbb Z),\qquad
\alpha:\Gamma\to C_6,
\quad \alpha(S)=3,\quad\alpha(T)=1,
\]

and set \(\Gamma_{\rm com}=\ker\alpha=[\Gamma,\Gamma]\). For the paired
Gauss map \(H=G^2\), use inverse branches

\[
\phi_{a,b}(z)=\frac{z+a}{b(z+a)+1},
\qquad a,b\geq1,
\]

with branch matrix

\[
A_{a,b}=
\begin{pmatrix}1&a\\b&ab+1\end{pmatrix}
=ST^{-b}ST^a
\]

and cocycle \(c(a,b)=a-b\pmod 6\). On
\(\mathcal A(D_{3/2})\otimes\mathbb C^6\), freeze

\[
(\mathcal M_s f)_r(z)
=\sum_{a,b\ge1}[b(z+a)+1]^{-2s}
f_{r-(a-b)}\!\left(\frac{z+a}{b(z+a)+1}\right).
\]

The only determinant convention is

\[
D_{\rm ab}(s)=\det_{\rm Fr}(I-\mathcal M_s)
=Z_{\Gamma_{\rm com}}(s).
\]

The defining operator is nuclear of order zero for \(\Re s>1/2\); the
Selberg identity is first used for \(\Re s>1\), then continued only through
the cited theorem chain.

### Source lock

```text
configs/source_locks/SS-0002.yaml
```

### Route-A status

```yaml
a1: A1_WEAK
a2: A2_FAIL
a3: A3_FAIL
a4: A4_NATURAL_QUANTIZATION
overall: ROUTE_A_REJECTED
latest_evaluation: evaluations/route_a/SS-0002/20260803T012711Z.yaml
```

### Route-B status

```yaml
b1: NOT_INVOKED
b2: NOT_INVOKED
b3: NOT_INVOKED
b4: NOT_INVOKED
b5: NOT_INVOKED
overall: NOT_INVOKED
latest_evaluation: null
```

### Positive evidence

- The object is countable-branch, infinite-dimensional, and non-locally
  constant, so it genuinely escapes `OBR-005`.
- Exact paired-branch and cocycle checks pass on disjoint frozen digit blocks.
- The regular `C6` representation retains character modes of orders two,
  three, and six without reading arithmetic tables.
- Nonzero base holonomy is handled correctly: a holonomy of order `d` produces
  `6/d` primitive lifts with length multiplied by `d`.
- The Fredholm determinant and the canonical hyperbolic Laplacian are natural,
  theorem-backed objects using the same closed-geodesic clock.

### Failed controls and obstructions

- Primitive lengths are modular closed-geodesic lengths, not a natural
  rational-prime `log p` clock.
- No von-Mangoldt prime-power amplitude is generated.
- The inherited modular cusp spectrum already contributes at least
  `T^2/12 + o(T^2)` positive-height Selberg zeros.
- The full area-`2*pi` finite-surface resonance law has a two-sided `T^2`
  main term, incompatible with completed-`xi` `Theta(T log T)` counting.
- The modular scattering determinant contains a separate zeta ratio and cannot
  be glued to the Mayer determinant.

### Reproduction

```bash
python3 -m unittest -v tests/test_ss_0002_commutator_mayer.py
python3 experiments/ss_0002_commutator_mayer.py --output artifacts/ss_0002/route_a_structural_audit.json
```

### Artifacts

```text
artifacts/ss_0002/route_a_structural_audit.json
docs/literature/ss_0002_gauss_mayer_sources.md
formal/obstructions/finite_area_selberg_weyl_mismatch.md
```

### Claim boundary

**Established:** SS-0002 is a rigorous escape from the finite-state theorem,
but its same-object Selberg divisor is structurally incompatible with
completed `xi`.

**Not established:** no prime correspondence, completed-xi determinant,
Route-B entry, Hilbert--Polya operator, or RH claim is obtained.

### Next smallest test

Before creating `SS-0003`, define one explicit non-Selberg countable-state or
nuclear transfer object and prove which zero-count regime its own Fredholm
determinant permits. A proposal that borrows a separate scattering quotient is
inadmissible.

### Decision history

| Date | Previous state | New state | Evidence | Commit | Reviewer |
|---|---|---|---|---|---|
| 2026-08-03 | `GENERATED` | `STOP_SCOPED` | Exact regular-holonomy audit, Mayer/Artin identity, and finite-area Weyl mismatch | current checkpoint (source `934d85c`) | sole main research agent |

---

## Evaluator control (not a formal candidate) — CTRL-0001

This entry is an explicit exception to the formal-candidate-only registry rule:
it records reusable evaluation infrastructure and must never be interpreted as
`SS-0003`.

### Identity

- **Family:** Synthetic diagonal trace-class / q-Pochhammer Fredholm control
- **Created:** 2026-08-03
- **Formal candidate:** `false`
- **Control verdict:** `GO_WITH_LIMITATIONS`
- **Candidate-scope verdict:** `STOP_SCOPED`
- **Uses prime table:** `false`
- **Uses zero table:** `false`

On

\[
\mathcal H=\ell^2(\{A_+,A_-,B,C\}\times\mathbb N_0),
\qquad
\mathcal L_s e_{c,n}=a_cq_c^n e^{-s}e_{c,n},
\]

the only determinant ledger is

\[
D(s)=\det_{\rm Fr}(I-\mathcal L_s)
=\prod_c\prod_{n\ge0}(1-a_cq_c^ne^{-s}).
\]

The four channels, rectangle, cutoffs, scoring boundary, and fault injections
are frozen in `configs/source_locks/CTRL-0001.yaml`.

### Route-A control status

```yaml
a1: A1_WEAK
a2: A2_ANALYTIC_DETERMINANT
a3: A3_PARTIAL_ANALYTIC_STRUCTURE
a4: A4_FAIL
overall_as_candidate: ROUTE_A_REJECTED
control_verdict: GO_WITH_LIMITATIONS
candidate_scope: STOP_SCOPED
latest_evaluation: evaluations/route_a/CTRL-0001/20260803T171847Z.yaml
route_b: NOT_INVOKED
```

Candidate interpretation:

```yaml
a1: A1_FAIL
a2: A2_FAIL
a3: A3_FAIL
a4: A4_FAIL
overall: ROUTE_A_REJECTED
```

### Positive evidence

- The analytic trace-class family and entire Fredholm determinant are exact.
- Coefficient root discovery is independent of direct-product
  argument-principle counting.
- The frozen rectangle contains exactly `22/12/5/5` total/core/upper/lower
  roots with minimum boundary clearance `0.07`.
- `K=16` exposes 28 roots and only 6 strict matches; `K=20` has the correct
  count but only 15 strict matches; `K>=24` passes all one-to-one matches.
- Successive `512/1024` contour grids pass the `pi/3` phase-step gate, while
  the coarser frozen grids are reported rather than silently accepted.
- Balanced corruption preserves every regional count but produces exactly
  four missing and four extra roots.
- The `r=4` trace cancellation ratio is `0.0099415`; replacing channel weights
  by absolute values changes the winding count from 22 to 30.
- Executable ledger controls give determinant winding `+22`, reciprocal pole
  winding `-22`, `D'/D` contour integral converging to `22`, and winding zero
  for the order-four truncated-log exponential.
- Supplemental `K=28` mpmath recomputations at 50/80/120 dps all find 22 roots;
  complex128-to-120-dps drift is `5.41e-13`.

The control verdict is limited because endpoint sampling plus a phase-step gate
does not constitute a rigorous interval-arithmetic proof excluding every
between-sample winding. The exact divisor is analytic; the contour sampler is a
numerical regression diagnostic.

### Claim boundary

This is a regression benchmark for determinant conventions, root discovery,
argument counting, cutoff drift, missing/extra matching, and signed complex
cancellation. It has no natural primitive classical dynamics, rational-prime
clock, completed-xi divisor, physical quantization, Route-B status, or RH
content. It must not be promoted from fixed-control success to a theorem about
another candidate.

### Reproduction

```bash
python3 -m unittest -v tests/test_ctrl_0001_qpochhammer.py
python3 experiments/ctrl_0001_qpochhammer.py \
  --quiet \
  --output artifacts/ctrl_0001/route_a_positive_control.json
```

### Next smallest test

Apply the same ledger, winding, cutoff, and balanced-corruption requirements to
the next explicitly defined non-Selberg candidate before interpreting any
numerical zero match. Do not allocate `SS-0003` before that object is explicit.

---

## 6. 初始候选族占位

以下是候选族，不是已经通过评估的候选。

### Family A — Twisted Hénon / kicked symplectic maps

```text
Status: TH-0001 is active in analytic review
Expected Route-A focus: A1, A4
Main risk: generic GUE without arithmetic orbit structure
```

### Family B — Higher-memory symbolic suspension

```text
Status: SS-0001 and SS-0002 are STOP_SCOPED under OBR-005 and OBR-006
Expected Route-A focus: A1, A2, A3
Main risk: hidden direct encoding of primes
```

### Family C — Low-complexity magnetic quantum graphs

```text
Status: QG-0001 is STOP_SCOPED by OBR-013; the broader family remains open only for a new source-locked object
Expected Route-A focus: A1, A2, A4
Main risk: edge lengths chosen post hoc as log primes
```

### Family D — Legacy Hardy signed-completion route

```text
Status: LEGACY-ANNULAR-RESIDUAL-001 is source-locked as a non-candidate A3 diagnostic; no RH-LEG-001 has been allocated
Expected Route-A focus: A2, A3
Current verdict: NOT_TESTABLE; standalone residual promotion is STOP_SCOPED
Main risk: missing physical-clock q-selected tau stream and moving-order theorem
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
