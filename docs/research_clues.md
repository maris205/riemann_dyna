# HP-Dynamics 后续研究线索库

**文件名：** `research_clues.md`  
**版本：** v0.2
**用途：** 保存可复用、可调用、可证伪的 Hilbert–Pólya 动力学研究线索。

---

## 0. 使用规则

本文件不是结论列表，也不是论文摘要集合。

每条线索必须满足：

```text
1. 有明确来源
2. 有证据等级
3. 能映射到 Route-A 或 Route-B 的具体层
4. 有一个最小可验证实验或 theorem obligation
5. 有明确失败条件
```

线索状态：

```text
ACTIVE
PROMISING
UNDER_TEST
BLOCKED
REFUTED
SUPERSEDED
ARCHIVED
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

项目级调用采用 RH 广度优先：弱候选连续两个 checkpoint 不改变 Route-A
tuple 或主阻塞时，保留其 candidate-local 恢复任务，但 project-level 下一步
转向一个结构不同、数学定义明确的新对象做低成本筛选。严格深挖资源只给
可能升级 Route-A 层级、形成候选族 obstruction，或出现稳定异常信号的路线。

---

# 1. 总体线索链

当前基础研究链为：

\[
\text{素数筛符号结构}
\rightarrow
\text{临界动力学骨架}
\rightarrow
\text{一维表达上限}
\rightarrow
\text{非自治漂移}
\rightarrow
\text{保守/辛提升}
\rightarrow
\text{UPO 与加权 Zeta}
\rightarrow
\text{自然量子化}
\rightarrow
\text{自伴随谱实现}.
\]

这条链只提供搜索先验，不表示每一步已经严格成立。

---

# 2. Route-A 线索

## CLUE-A1-001 — 素数筛的符号动力学骨架

**来源：** Prime–Chaos 基础论文  
**证据：** `HEURISTIC` + 部分数值/组合结构  
**状态：** `ACTIVE`  
**对应层：** `A1`

### 内容

Eratosthenes sieve 的奇偶与禁止字结构可能对应某种临界符号动力学骨架。

### 可迁移结构

- parity rigidity；
- forbidden words；
- kneading-like order；
- finite-state symbolic grammar；
- critical band-merging regime。

### 最小测试

比较候选的 primitive symbolic words 与：

- parity constraints；
- sieve-derived words；
- shuffled symbolic controls。

### 失败条件

候选只能通过逐项输入素数表产生对应关系。

---

## CLUE-A1-002 — 一维模型是 mod-2 投影，不是完整宿主

**来源：** Transient Chaos / Topological Bounds  
**证据：** `PROVED` 与结构性结论混合  
**状态：** `BLOCKED`
**对应层：** `A1`, `A4`

### 内容

一维 unimodal 模型可以表达奇偶骨架，但有限阶段存在 MSS admissibility 缺陷，而且缺乏产生完整 mod-3 及更高 residue resonance 的内部自由度。

### 推论

重点搜索：

- 二维及更高维辛映射；
- higher-memory subshift；
- multi-sheet cover；
- non-Abelian symbolic extension；
- graph flow；
- residue-state suspension。

### 最小测试

构造从 mod-2 状态扩张到 mod-6 或更高 residue memory 的最小状态图，检测是否能产生非平凡 mod-3 resonance，而不直接编码素数。

### 失败条件

增加状态后只是把素数表重新写进 transition table。

### 2026-08-02 基线结果

`SS-0001` 使用不读取素数表的模 6 Cayley 图边移位，证明了有限状态
扩张可以真正携带非平凡 mod-3 character；因此“加入 residue memory”本身
是可实现的。然而常 roof \(1\) 使所有 primitive periods 保持为整数，且

\[
D(s)=\det(I-e^{-s}A)=(1-4e^{-2s})(1-e^{-2s})^2
\]

只有 \(O(T)\) 个高度不超过 \(T\) 的零点，不能满足 completed-\(\xi\) 的
\(\Theta(T\log T)\) 计数。该候选 `STOP_SCOPED`，但线索保留。

### Scoped theorem

`formal/obstructions/finite_state_finite_roof_zero_count.md` 已证明：任何
非零有限状态、有限维、locally constant 正 roof transfer determinant 都是
有限指数和，并且在有界竖直带中的零点计数为 \(O(T)\)。因此有限 residue
memory、有限 sheet 或有限 phase decoration 本身不能达到 completed-\(\xi\)
的 \(\Theta(T\log T)\) divisor。

### 2026-08-03 reopening result

`SS-0002` 明确定义了一个真正位于 `OBR-005` 之外的对象：模曲面交换子群
六层覆盖上的 paired-Gauss regular-holonomy Mayer 算子。它具有：

- 可数无穷分支；
- infinite-dimensional disk-algebra 作用空间；
- 非 locally constant 且无界的双 Gauss roof；
- `Re(s)>1/2` 上的 nuclear Fredholm determinant；
- 不读取 prime/zero 表的内禀 `C6` holonomy。

其冻结行列式为

\[
D_{\rm ab}(s)
=\det_{\rm Fr}(I-\mathcal M_s)
=Z_{[\operatorname{PSL}_2(\mathbb Z),
       \operatorname{PSL}_2(\mathbb Z)]}(s).
\]

因此该对象成功逃离有限状态 `O(T)` theorem，但落入新的 `OBR-006`：
有限指标模覆盖继承至少 \(T^2/12+o(T^2)\) 个正高度谱零点，故同一
Selberg/Fredholm divisor 为 \(\Omega(T^2)\)，仍不能匹配 completed-\(\xi\)
的 \(\Theta(T\log T)\)。自然 Laplace--Beltrami quantization 不改变该失败。

Route-A tuple：

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)
```

候选状态：`STOP_SCOPED`。模散射行列式中的 completed-zeta ratio 属于另一
determinant ledger，不得与 Mayer determinant 拼接。

### Reopening condition

下一对象必须同时位于 `OBR-005` 和 `OBR-006` 之外：先明确一个
non-Selberg countable-state 或 nuclear determinant，冻结 intrinsic clock 与
determinant convention，并证明其自身允许的 divisor-count regime。若需要借用
独立 scattering quotient、prime 表或 zero 表，不得创建 `SS-0003`。

---

## CLUE-A1-003 — Primitive periods 必须与权重一起判断

**来源：** 显式公式与 Route-A 讨论  
**证据：** `ESTABLISHED_EXTERNAL` / 项目规则  
**状态：** `ACTIVE`  
**对应层：** `A1`, `A2`

### 内容

仅有

\[
T_{\gamma_p}\approx\log p
\]

不足以构成黎曼动力学。

还要解释：

\[
A_{\gamma_p,r}
\sim
\frac{\log p}{p^{r/2}}
\]

以及 repetition、phase、orientation 和 multiplicity。

### 最小测试

对每个候选同时计算：

```text
period assignment loss
stability-weight loss
phase consistency
repetition consistency
unmatched-orbit penalty
```

### 失败条件

周期吻合，但权重完全随机或依赖人工拟合。

---

## CLUE-A1-004 — 从非自治系统提升为自治高维系统

**来源：** Prime aging 与 Sequential Birkhoff 工作  
**证据：** `PROVED` + `HEURISTIC` + `MODELING_CHOICE` + scoped `PROVED_OBSTRUCTION`
**状态：** `ACTIVE`
**对应层：** `A1`, `A4`

### 内容

慢漂移 schedule 可以看作更高维自治系统中的额外慢变量。

### 候选形式

\[
(x_{n+1},u_{n+1})=
(F_{u_n}(x_n),G(u_n)).
\]

### 潜在价值

- 避免手工时间依赖；
- 提供统一 phase space；
- 更适合 UPO 和自然量子化；
- 可能把 aging 变成几何 roof function。

### 最小测试

构造最小二维/三维 autonomous lift，比较：

- 原 schedule；
- lifted orbit structure；
- primitive cycle grammar；
- conserved/symplectic extension。

### 风险

lift 可能仅形式化重写，并未产生新的算术结构。

### 2026-08-04 monotone-clock audit

冻结的紧化时钟为

\[
v_n=\frac1{\log(n+10)},
\qquad
G(v)=\frac1{\log(e^{1/v}+1)},
\qquad G(0)=0,
\]

并定义

\[
F(x,v)=\left(1-(u_c+kv^2)x^2,G(v)\right).
\]

该对象精确复现 legacy micro schedule，但对每个 \(m\geq1\)，

\[
\operatorname{Fix}(F^m)
=
\operatorname{Fix}(f_{u_c}^m)\times\{0\}.
\]

因此所有 primitive orbit 都坍缩到静态极限切片；没有周期轨道穿过
aging interior。对应的 reciprocal Artin--Mazur formal series 也只等于静态
父系统的 formal series，且边界 clock multiplier 为 `1`。该严格单调 clock
子类判为 `STOP_SCOPED`，没有创建正式候选，也未启动 Route B。

重新开启必须给出内生 recurrent base，使非平凡周期轨道离开静态极限切片，
并冻结一个非退化的 same-object determinant；或给出完整定义的 chronological
transfer-cocycle determinant。单纯 modulo、reset 或 finite-cutoff clamp 不属于
同一 schedule。

Artifacts:

- `configs/source_locks/P4-LOGISTIC-MONOTONE-CLOCK-LIFT.yaml`
- `evaluations/route_a/P4-LOGISTIC-MONOTONE-CLOCK-LIFT/20260804T025047Z.yaml`
- `artifacts/p4_logistic_monotone_clock_lift/structural_audit.json`
- `formal/obstructions/strict_monotone_clock_orbit_collapse.md`

### 2026-08-04 exact-(U_c) recurrent-clock audit

The next recurrent object fixes the true band-merging anchor as the unique
real root

\[
U_c^3-2U_c^2+2U_c-2=0,
\qquad U_c=1.5436890126920764\ \text{(binary64)},
\]

not the rounded legacy literal `1.543689`. The critical orbit satisfies

\[
0\to1\to1-U_c\to U_c-1\to U_c-1.
\]

For the frozen event (L=\{x<0\}), all tested left and center controls have
zero odd-gap mass, while every tested right control opens an odd-gap channel.
This is a target-free finite numerical phase-boundary diagnostic. The right
support contains odd primes and odd composites; no composite-preference claim
is made, and low-count long-tail support is cutoff/precision sensitive.

The exact physical domain is the forward-invariant core

\[
J=[1-U_c,1]=[-\rho,1],
\qquad \rho=U_c-1,
\]

not the full ambient interval. The band swap

\[
f([-\rho,\rho])=[\rho,1],
\qquad
f([\rho,1])=[-\rho,\rho]
\]

proves that the physical first-return support is exactly
(2\mathbb N_{\geq1}). If

\[
h(y)=\sqrt{\frac{1-y}{U_c}},
\qquad
r_0=0,
\qquad
r_{n+1}=h(h(r_n)),
\]

then (r_n\uparrow\rho) and

\[
C_2(J)=(-r_1,0),
\qquad
C_{2n}(J)=(-r_n,-r_{n-1}]\quad(n\geq2),
\qquad
C_{2n+1}(J)=\varnothing.
\]

Thus every physical even label has exactly one nondegenerate interval branch.
Each branch interior is mapped real-analytically and diffeomorphically by
(f^{2n}) onto `(-rho,0)`, so every finite word of positive even return labels
has a nonempty open cylinder. This proves the recurrent tower's finite-word
alphabet provenance; it does not prove realization of every infinite sequence
or choose the full two-sided completion, its invariant measure, or its aged
fibre coupling.

On ambient `[-1,1]`, transient odd branches fill `[-1,-rho)`, so the ambient
topological support is all positive integers; every invariant probability
assigns those odd branches zero mass. The standard physical acip is now proved
to exist uniquely and have full support (J), so every physical even branch has
positive mass.

The recurrent tower uses this proved physical alphabet, with one symbol
(m\geq1) for the even label (L=2m), and the anchored fibre law

\[
\mu(j,L)=U_c+k\left[
\log^{-2}(a_0+j)-\log^{-2}(a_0+L)
\right],
\]

so each block has exactly (L) updates and the terminal update satisfies
(mu(L,L)=U_c) before renewal. The tower has

\[
Z_T(z)=\frac{1-z^2}{1-2z^2},
\qquad
\#\operatorname{Fix}(G^{2r})=2(2^r-1),
\]

and every primitive tower orbit through period 16 has a signed full-fibre
fixed-point witness. First-return branches are not themselves primitive
periodic orbits, and the tower measure/coupling remains an additional modeling
choice; the finite-word alphabet provenance is now proved.

Route-A result:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
overall: ROUTE_A_EXPLORATORY
audit verdict: REVISE
formal candidate: false
Route B: inactive and not authorized
```

The unit clock substitution (z=e^{-s}) forces a (2\pi i)-periodic divisor
with (O(T)) count in bounded real strips (`OBR-008`), so it cannot be the
completed-ξ divisor. Independently, the unaccelerated physical first-return
map has derivative infimum zero on every branch (`OBR-009`). The legacy
Paper-2 ordinary-`BV` uniform-expansion/spectral-gap proof therefore does not
establish the claimed geometric branch-weight asymptotic.

The direct polar-coordinate density theorem now proves

\[
\frac{d\mu_{\rm ac}}{dx}(-\rho+t)
=\frac{h(0)}{\sqrt2U_c}t^{-1/2}+O(1),
\qquad h(0)>0,
\]

and therefore

\[
\frac{\mu_{\rm ac}(C_{2n+2})}{\mu_{\rm ac}(C_{2n})}
\longrightarrow\frac1{2U_c(U_c-1)}=\frac{U_c^2}{4}.
\]

This repairs the legacy mass-ratio conclusion without restoring the refuted
ordinary-`BV` first-return proof. The validated sharp polar-cone audit uses a
complete directed Arb cover to prove `0.20655<h(0)<0.40008`,
`0.09461<C_h<0.18327`, and tighter intervals for four finite branch masses.
It still does not restore the legacy ordinary-BV spectral proof or an exact
finite-order mass law. The cusp-adapted audit now proves an explicit
adjacent-ratio rate from branch index 6 onward. The polar suspension source
lock now freezes the map, doubled branches, intrinsic roof `tau=log|G'|`,
separate clocks, analytic function space, and conditional determinant
convention. The sealed `R`/`LR` audit now proves their full primitive roof
periods have irrational ratio, so the intrinsic roof is non-lattice. The
frozen radius-`1/1000` complex audit now proves one common logarithm germ,
globally univalent composite inverse branches, all four compact inclusions,
and matching-space invariance. The half-open partition audit then proves the
exact boundary graph and target-copy ledger, while the local boundary theorem
fixes the pure-left trace with no half or doubled factor. The formal candidate
`LOG-0001` now proves order-zero nuclearity of the full matching-space family,
joint entireness of
`Delta(lambda,s)=det_Fr(I-lambda*L_s|_B)`, and the exact signed all-power
based-fixed-point trace formula. This is a genuine analytic determinant but
not an arithmetic or completed-xi determinant. The growth audit now proves
classical order at most two, an `O(T^2)` fixed-real-strip divisor upper bound,
and a zero-free half-plane
`Re(s)>log(2)/log(4/U_c^2)`. These are upper/continuation results, not a sharp
counting law. The conformal-ratio audit now proves
`r_L=r_R<=tanh((500*pi+log(4))/2)<1`, resolves the gap below one at 4096 bits,
and certifies the fully numerical same-determinant envelope
`exp(3.45e689+4.20e682*(1+|s|)^2)`.  The next smallest task is only a
cancellation-safe lower-growth precheck; target zeros remain sealed.

The `LOG-0001-LOWER-GROWTH` audit closes that precheck.  On the safe real
half-plane the complete signed trace-log differentiates locally uniformly and
every real summand is positive.  The exact pure-left term gives
`D_pol'(2)>0.0213`, hence
`M_D(R)>0.0213*(R-2)` for `R>2` and `M_D(R)>0.01065*R` for `R>=4`.
Together with `D_pol(sigma)->1`, this proves that the same determinant is
transcendental entire and has qualitative super-polynomial maximum-modulus
growth.

The separate `LOG-0001-ORDER-LOWER` audit now uses the uniform full-line bound
on `Re(s)>=2`.  A half-plane Phragmen--Lindelof contradiction rules out order
below one, and the inherited upper theorem closes the interval
`1<=ord(D_pol)<=2`.  This does not identify order one versus two or establish
a target divisor.  The next task is the breadth pivot to a newly defined
intrinsic recurrent candidate or a reusable obstruction.

Artifacts:

- `configs/source_locks/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK.yaml`
- `configs/source_locks/P4-LOGISTIC-UC-FIRST-RETURN-SUPPORT.yaml`
- `configs/source_locks/P4-LOGISTIC-UC-ACIP-ENDPOINT-DENSITY.yaml`
- `configs/source_locks/P4-LOGISTIC-UC-ACIP-CONE-ENCLOSURE.yaml`
- `configs/source_locks/P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE.yaml`
- `configs/source_locks/P4-LOGISTIC-UC-BRANCH-MASS-RATE.yaml`
- `configs/source_locks/P4-LOGISTIC-UC-POLAR-INTRINSIC-ROOF.yaml`
- `configs/source_locks/P4-LOGISTIC-UC-POLAR-NONLATTICE.yaml`
- `configs/source_locks/P4-LOGISTIC-UC-POLAR-COMPLEX-BRANCH.yaml`
- `configs/source_locks/P4-LOGISTIC-UC-POLAR-PARTITION-TRACE.yaml`
- `configs/source_locks/P4-LOGISTIC-UC-POLAR-BOUNDARY-TRACE.yaml`
- `configs/source_locks/LOG-0001-NUCLEAR-FREDHOLM.yaml`
- `configs/source_locks/LOG-0001-GROWTH-ORDER.yaml`
- `configs/source_locks/LOG-0001-CONFORMAL-RATIO.yaml`
- `configs/source_locks/LOG-0001-LOWER-GROWTH.yaml`
- `configs/source_locks/LOG-0001-ORDER-LOWER.yaml`
- `evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T080528Z.yaml`
- `evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T105010Z.yaml`
- `evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T162511Z.yaml`
- `evaluations/route_a/P4-LOGISTIC-UC-ACIP-CONE-ENCLOSURE/20260804T233200Z.yaml`
- `evaluations/route_a/P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE/20260805T012200Z.yaml`
- `evaluations/route_a/P4-LOGISTIC-UC-BRANCH-MASS-RATE/20260805T035348Z.yaml`
- `evaluations/route_a/P4-LOGISTIC-UC-BRANCH-MASS-RATE/20260805T083731Z.yaml`
- `evaluations/route_a/P4-LOGISTIC-UC-POLAR-NONLATTICE/20260805T110654Z.yaml`
- `evaluations/route_a/P4-LOGISTIC-UC-POLAR-COMPLEX-BRANCH/20260805T125236Z.yaml`
- `evaluations/route_a/P4-LOGISTIC-UC-POLAR-PARTITION-TRACE/20260807T032000Z.yaml`
- `evaluations/route_a/P4-LOGISTIC-UC-POLAR-BOUNDARY-TRACE/20260807T071000Z.yaml`
- `evaluations/route_a/LOG-0001/20260808T051519Z.yaml`
- `evaluations/route_a/LOG-0001/20260808T104049Z.yaml`
- `evaluations/route_a/LOG-0001/20260808T151232Z.yaml`
- `evaluations/route_a/LOG-0001/20260809T073000Z.yaml`
- `evaluations/route_a/LOG-0001/20260809T110000Z.yaml`
- `artifacts/p4_logistic_recurrent_uc_anchored_clock/structural_audit.json`
- `artifacts/p4_logistic_uc_first_return_support/structural_audit.json`
- `artifacts/p4_logistic_uc_acip_endpoint_density/structural_audit.json`
- `artifacts/p4_logistic_uc_acip_cone_enclosure/certified_bounds.json`
- `artifacts/p4_logistic_uc_acip_sharp_cone_enclosure/interval_certificate.json`
- `artifacts/p4_logistic_uc_branch_mass_rate/rate_certificate.json`
- `artifacts/p4_logistic_uc_polar_nonlattice/nonlattice_certificate.json`
- `artifacts/p4_logistic_uc_polar_complex_branch/complex_branch_certificate.json`
- `artifacts/p4_logistic_uc_polar_partition_trace/partition_trace_certificate.json`
- `artifacts/p4_logistic_uc_polar_boundary_trace/boundary_trace_certificate.json`
- `artifacts/log_0001_nuclear_fredholm/nuclear_fredholm_certificate.json`
- `artifacts/log_0001_growth_order/growth_order_certificate.json`
- `artifacts/log_0001_conformal_ratio/conformal_ratio_certificate.json`
- `artifacts/log_0001_lower_growth/lower_growth_certificate.json`
- `artifacts/log_0001_order_lower/order_lower_certificate.json`
- `experiments/p4_logistic_uc_acip_endpoint_density.py`
- `experiments/p4_logistic_uc_polar_partition_trace.py`
- `experiments/p4_logistic_uc_polar_boundary_trace.py`
- `experiments/log_0001_nuclear_fredholm.py`
- `experiments/log_0001_growth_order.py`
- `experiments/log_0001_conformal_ratio.py`
- `experiments/log_0001_lower_growth.py`
- `experiments/log_0001_order_lower.py`
- `docs/literature/exact_uc_acip_density_sources.md`
- `formal/results/exact_uc_first_return_support.md`
- `formal/results/exact_uc_acip_endpoint_density.md`
- `formal/results/exact_uc_acip_cone_enclosure.md`
- `formal/results/exact_uc_acip_sharp_cone_enclosure.md`
- `formal/results/exact_uc_branch_mass_rate.md`
- `formal/results/exact_uc_polar_nonlattice.md`
- `formal/results/exact_uc_polar_complex_branch.md`
- `formal/results/exact_uc_polar_partition_trace.md`
- `formal/results/exact_uc_polar_boundary_trace.md`
- `formal/results/log_0001_nuclear_fredholm.md`
- `formal/results/log_0001_growth_order.md`
- `formal/results/log_0001_conformal_ratio.md`
- `formal/results/log_0001_lower_growth.md`
- `formal/results/log_0001_order_lower.md`
- `formal/obstructions/exact_uc_first_return_nonuniform_expansion.md`
- `formal/obstructions/unit_lattice_clock_vertical_periodicity.md`
- `tests/test_p4_logistic_uc_first_return_support.py`
- `tests/test_p4_logistic_uc_acip_endpoint_density.py`
- `tests/test_p4_logistic_uc_acip_sharp_cone_enclosure.py`
- `tests/test_p4_logistic_uc_branch_mass_rate.py`
- `tests/test_p4_logistic_uc_polar_intrinsic_roof_lock.py`
- `tests/test_p4_logistic_uc_polar_nonlattice.py`
- `tests/test_p4_logistic_uc_polar_complex_branch.py`
- `tests/test_p4_logistic_uc_polar_partition_trace.py`
- `tests/test_p4_logistic_uc_polar_boundary_trace.py`
- `tests/test_log_0001_nuclear_fredholm.py`
- `tests/test_log_0001_growth_order.py`
- `tests/test_log_0001_conformal_ratio.py`
- `tests/test_log_0001_lower_growth.py`
- `tests/test_log_0001_order_lower.py`
- `tests/test_p4_logistic_recurrent_uc_anchored_clock.py`

---

## CLUE-A2-001 — Weighted dynamical Zeta 是 Route-A 主目标

**来源：** 当前研究规划  
**证据：** `PROJECT_DECISION`  
**状态：** `ACTIVE`  
**对应层：** `A2`

### 目标

\[
D_{\mathrm{dyn}}(s)
\approx
e^{g(s)}\xi(s).
\]

### 候选实现

- direct cycle product；
- Ruelle Zeta；
- Selberg-like determinant；
- transfer-operator Fredholm determinant；
- quantum-graph secular determinant。

### 最小测试

使用人工 Euler-product positive control 验证：

- root finder；
- argument principle；
- cutoff drift；
- extra-zero detection。

### 失败条件

不同实验混用 \(Z\)、\(1/Z\)、\(Z'/Z\) 或 determinant convention。

### 2026-08-03 positive-control closure

`CTRL-0001` 完成了本线索的 evaluator positive control。它不是正式候选，
不得分配 `SS-0003`。冻结对象为四通道对角 trace-class 族

\[
\mathcal L_s e_{c,n}=a_cq_c^ne^{-s}e_{c,n},
\qquad
D(s)=\det_{\rm Fr}(I-\mathcal L_s)
=\prod_c\prod_{n\ge0}(1-a_cq_c^ne^{-s}).
\]

在冻结矩形中，精确 scoring ledger 为 total/core/upper/lower
`22/12/5/5`。根发现使用 q-binomial Fredholm 系数，多项式根仅在
`z=e^{-s}` 中求得后才枚举全部 logarithm branches；argument principle
独立使用 direct mode product。结果包括：

- `K=16` 找到 28 roots，仅 6 个在 `1e-4` 半径内严格匹配；
- `K=20` 虽然 root count 已是 22，但只有 15 个严格匹配；
- `K=24/28/32` 均为 22 个一一匹配，最大误差分别约
  `1.25e-5/8.90e-9/7.83e-13`；
- `N=2` winding 为 18，`N>=3` 为 22，但 `N=40 -> 48` determinant
  contour value drift 仍为 `8.46e-7`，说明 count stability 与 value
  stability 必须分开；
- 冻结的 `128/256` grids 虽给出正确 count，但相邻相位步长未通过
  `pi/3`；`512/1024` successive grids 才被接受；
- balanced corruption 保持 `22/12/5/5` 计数，却被 matcher 报告为
  `4 missing + 4 extra`；
- `r=4` signed trace 的 cancellation ratio 为 `0.0099415`，而将所有
  phase 取绝对值会把 winding count 改成 30。
- executable ledger controls 分别得到 `D` winding `+22`、`1/D` pole
  winding `-22`、`D'/D` contour integral 收敛到 22，以及四阶 truncated-log
  exponential winding `0`；
- `K=28` 的 50/80/120 dps mpmath 复算均找到 22 roots，complex128 与
  120 dps 的最大 root drift 为 `5.41e-13`。

因此，作为 A2 evaluator infrastructure，结论为 `GO_WITH_LIMITATIONS`；作为任何
Riemann-dynamics candidate，结论为 `STOP_SCOPED`。它验证了 root finder、
argument principle、cutoff drift、extra/missing detection 与 determinant
ledger 分离，但不提供自然 primitive orbit、completed-\(\xi\) 结构或 Route B
入口。

限制是：离散 contour endpoint 的 phase-step gate 与 successive refinement
属于 numerical anti-alias diagnostic，不能替代 interval arithmetic 或
`D'/D` 导数上界所给出的严格 winding certificate。控制语境下的 tuple 为
`(A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)`；
若把同一对象解释为 completed-\(\xi\) 候选，则 tuple 为
`(A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`。

下一次调用本线索时，应把 `CTRL-0001` 作为 regression benchmark，要求新
对象在自己的 source lock 下通过同样的 independent winding、one-to-one
matching、balanced corruption 与 signed-cancellation gates。

---

## CLUE-A2-002 — Signed/complex cancellation 是核心结构

**来源：** 旧 RH signed-completion 路线  
**证据：** `PROVED_OBSTRUCTION`  
**状态：** `ACTIVE`  
**对应层：** `A2`, `A3`

### 内容

orbit、diffuse、head 或 sideband 项不能分别取绝对值后再拼接。关键闭合可能依赖精细 signed/complex cancellation。

### 工程要求

所有 orbit records 必须保留：

```text
amplitude
phase
orientation
repetition
alias class
complex sign
```

### 最小测试

比较：

```text
signed cycle expansion
absolute-value majorant
phase-randomized control
```

### 失败条件

候选只能在丢弃相位后“吻合”。

---

## CLUE-A2-003 — Sideband / off-alias 背景不可忽略

**来源：** RH-338 至 RH-341 一类结果  
**证据：** `PROVED_OBSTRUCTION` + `OPEN`  
**状态：** `ACTIVE`  
**对应层：** `A2`, `A3`

### 内容

主 critical order 匹配不代表完整 prefix 或 determinant 已闭合。邻近 sideband 和 off-alias aggregate 可能包含 super-target 原子或额外零点来源。

### 最小测试

每个候选必须报告：

```text
dominant orbit sector
nearest sidebands
off-alias weighted mass
extra-zero scan
punctured aggregate
cutoff migration
```

### 失败条件

只展示主峰或前几个零点。

---

## CLUE-A2-004 — 同一 clock、normalization 和数据类型

**来源：** 旧 RH 路线的 wrong-clock 与 gluing obstruction  
**证据：** `PROVED_OBSTRUCTION`  
**状态：** `ACTIVE`  
**对应层：** `A2`, `A3`, `B4`, `B5`

### 内容

不能用一个 clock 证明 head、另一个 clock 证明 tail，再用第三个 normalization 匹配 spectrum。

### 最小测试

所有结果写入 frozen manifest：

```yaml
clock:
normalization:
determinant_convention:
cutoff:
spectral_map:
```

### 失败条件

任一组件使用不兼容数据类型。

---

## CLUE-A2-005 — 非自治 Logistic 经验转移谱的确定性分支审计

**来源：** Paper 4 legacy notebooks / 用户提出的 Logistic reopening

**证据：** `NUMERICAL_OBSERVATION` + `FITTED_PARAMETER`

**状态：** `BLOCKED`

**对应层：** `A1`, `A2`, `A4`

### 冻结对象

Legacy micro 代码计算

\[
x_{n+1}=1-\mu_nx_n^2,
\qquad
T_{ij}=\sum_n V_n(i)K_{\mu_n,\epsilon}(i,j),
\]

并从 occupation-conditioned finite matrix 的复特征值中丢弃模长、按主值
相角排序，再以第一个黎曼零点定 scale。该对象不是有序 transfer cocycle，
也尚未定义 dynamical Zeta 或 Fredholm determinant。

### 2026-08-03 legacy 审计

- `epsilon=0.001916` 由零点 2--6 选择，零点 1 固定 scale；
- 同一矩阵的 20 次 `eigs` 随机启动又用于挑选最佳结果；
- N=20 误差被评分函数主动奖励，因而 USTC 叠图不是独立验证；
- 保存结果在 fitted zeros 2--6 上 MAE `0.3494`，但 zeros 7--20 的
  retrospective MAE 为 `7.4162`，zeros 21--85 为 `61.7317`；
- anchored ablation 的 MSE `78.08` 高于 all-100-point linear-fit baseline
  的 `28.67`，且 schedule 参数来自相同零点数据的优化家族。

CSR destination-index 归一化得到 (B=TD^{-1})，正确行归一化为
(Q=D^{-1}T)。虽然 (B) 不是 Markov 矩阵，但

\[
B=DQD^{-1},
\]

所以精确 eigenvalues 相同；真正风险是 eigenvector 解释、非正规性和
finite-precision solver conditioning，而不是归一化单独制造相角。

### Target-free smoke result

在保持 (epsilon/dx=5.748) 的 `128 bins x 1000 steps` reduced profile 中：

- fixed-start tight-ARPACK 可以复现 dense top-(|\lambda|) 谱；
- 按 legacy 规则排列的前六个低相角里有五个满足
  (|\lambda|<10^{-3})；
- 半格移动分区后，13 个 resolved modes 的复平面匹配中位漂移
  `0.00943`，90 分位 `0.0883`，最大 `0.15275`。

因此当前低相角 level rule 尚不稳定，但 Logistic 线保留为数值 benchmark
和 autonomous slow-variable lift 的搜索先验。

### Physical-epsilon medium result

在 version-2 source lock 下，本次运行没有读取 zero、prime 或 USTC table，
也没有重新优化参数；但 `epsilon=0.001916` 是历史上由 zeros 2--6 选择的，
所以这是 target-free robustness audit，不是 blind arithmetic validation。

冻结的 `2048 bins x 100000 steps` reference 只产生 4 个
residual-certified upper-half strong branches ((|\lambda|\ge0.5))，低于预注册
门槛 20。所有 mechanics、raw hash/round-trip、solver convergence、`450/450`
Ritz return、residual、强/中层共轭、Q/B、fixed-start、`k=300/450` guard 与
独立 `256 bins x 5000 steps` anchor 上的 dense/sparse solver gate 均通过；
该 anchor 不与四条 reference branches 做 cutoff matching。

- bins 与 time cutoff 的四支 matching 全部稳定，且收敛门通过；
- 跨全部 profile 的 stable intersection 为 3/4，即 `0.75`；
- half-bin translated-domain control 的 median/p90/max complex drift 为
  `0.028783/0.046071/0.051659`，最大 phase drift 为 `0.033001`，
  phase-rank median/max displacement 为 `1/1`；
- median nearest-static normalized distance 为 `0.0009477`；
- dynamic/static margin median 为 `0.03789`，且达到 margin `1.5` 的比例为
  `0`。

因此冻结的 strong-layer empirical phase observable 判为 `STOP_SCOPED`。
该判定不淘汰 Logistic dynamics 本身，也不评价尚未定义的 autonomous lift、
chronological cocycle 或 Fredholm determinant。

### Route-A 边界

```text
formal candidate: none
Route-A status: NOT_TESTABLE
diagnostic tuple: (A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)
empirical phase-observable verdict: STOP_SCOPED
Route B: not authorized
```

### Reopening condition

当前经验相位 observable 内没有更小的合规任务。只有在先明确给出 autonomous
slow-variable lift 或 chronological transfer-cocycle/Fredholm determinant 的
数学对象、clock 与 determinant convention 后，才可用新 source lock 重开。
否则项目转入 `CLUE-A2-001` 的 synthetic Euler-product positive control。
不得由本结果解封新的 zero-match 指标。

Artifacts:

- `configs/source_locks/P4-LOGISTIC-LEGACY-AUDIT.yaml`
- `configs/source_locks/P4-LOGISTIC-DETERMINISTIC-SMOKE.yaml`
- `configs/source_locks/P4-LOGISTIC-MEDIUM-PHYSICAL-EPSILON.yaml`
- `artifacts/p4_logistic_legacy/route_a_pre_candidate_audit.json`
- `artifacts/p4_logistic_legacy/deterministic_smoke_profile.json`
- `artifacts/p4_logistic_medium/branch_audit.json`
- `artifacts/p4_logistic_medium/raw/dynamic_reference_T.npz`
- `artifacts/p4_logistic_medium/raw/static_mean_matched_T.npz`
- `docs/prior_work/logistic_legacy_pre_audit.md`

---

## CLUE-A3-001 — 从逐零点拟合转向 annular norm

**来源：** 旧 RH direct annular route  
**证据：** `CONDITIONAL_THEOREM`；实际 moving-order 数据不可用
**状态：** `NOT_TESTABLE`
**对应层：** `A3`

### 内容

对误差生成函数

\[
g_\sigma(z)
=
\sum_{n\ge2}
\frac{\tau_{\sigma,n}-a_n}{n}z^n
\]

若能在认证环域上控制 \(H^\infty\) 或 \(H^2\) 范数，可能比逐零点拟合更接近整体解析闭合。

### Source-locked data type

`LEGACY-ANNULAR-RESIDUAL-001` 冻结

\[
\tau_{\sigma,n}=\operatorname{Tr}C_\sigma^n,
\qquad
g_\sigma=\log G_H-\log\det_2(I-zC_\sigma),
\]

其中 `C_sigma` 是 `q=1/2` 的 complementary normal spectral realization，
不是已证明的 physical invariant compression，`g_sigma` 也不是独立
determinant。冻结 `R=1.4`、`rho=1.41`，并严格区分 noise clock、trace
order `n`、RH-302 的 `m_sigma` 和 later first-alias clock。

### 审计结论

RH-300 的 (H^\infty/H^2) implication 与 RH-302 的 vanishing-tail
reduction 都成立；最新 RH-371 不改变该结论。当前缺少物理小噪声时钟上
`q=1/2`-selected complementary spectrum / `tau` stream 的 cutoff、precision
和 stopping certificate。早期 fixed-noise finite spectra 与 RH-354 的
normalized selected tail 都不能替代这个数据类型。

Route-A tuple 为

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
```

本线索不是 formal candidate，verdict 为 `NOT_TESTABLE`；将 residual 本身
升级为 candidate 则 `STOP_SCOPED`。Route B 不授权。

### 重新开启后的最小测试

先获得同一账本的 actual `tau_(sigma_k,n)`，冻结 baseline
`sigma_k=lambda^(-2k)`、离散化、spectral cutoff、precision 和 data split，
再且只先构造：

```text
annular H2 residual
cutoff drift
precision drift
```

`log-derivative` 与 argument-principle 检查只有在完整 same-object
determinant 与 holomorphy certificate 存在后才开放。

### 风险

有限网格上的小 norm 不能自动升级为全环域定理；固定阶数据不能升级为
moving-order/all-order 结论；不得用 `q,h,s,E_off` 或 normalized tail
替换 raw signed/complex `p=tau-a`。

---

## CLUE-A3-002 — Completed \(\xi\) 而非裸 \(\zeta\)

**来源：** 当前规划  
**证据：** `PROJECT_DECISION`  
**状态：** `ACTIVE`  
**对应层：** `A3`, `B5`

### 内容

必须处理：

- Gamma factor；
- trivial zeros；
- pole cancellation；
- functional equation；
- entire prefactor。

### 最小测试

把候选 determinant 与：

\[
\xi(s)
\]

而不是仅与前若干非平凡零点比较。

---

## CLUE-A3-003 — Moving-order theorem 优先于固定截断漂亮结果

**来源：** 旧 RH 项目和当前 Route-A 规范  
**证据：** `PROVED_OBSTRUCTION` / `PROJECT_DECISION`  
**状态：** `ACTIVE`  
**对应层：** `A2`, `A3`

### 内容

固定周期、固定矩阵维度或固定 \(k\) 的吻合不能推出 all-order 结构。

### 最小测试

监控：

\[
D_N(s)\to D_{N+1}(s),
\qquad
\widehat\gamma_j^{(N)}
\to
\widehat\gamma_j^{(N+1)}.
\]

### 必须报告

- root drift；
- zero-count drift；
- omitted-orbit estimate；
- precision scaling；
- cutoff scaling。

---

## CLUE-A4-001 — Hénon-like symplectic map 加 magnetic/topological twist

**来源：** Area-preserving Hénon 工作与时间反演讨论  
**证据：** `HEURISTIC` + `MODELING_CHOICE`  
**状态：** `ACTIVE` — `TH-0001` FIO lift complete; global single-phase ledger blocked by `OBR-011`
**对应层：** `A1`, `A4`

### 内容

标准面积保持 Hénon 可作为母模板，但需要显式检查或破坏反幺正时间反演对称性。

### 候选形式

\[
p' = p-\partial_qV(q)+A_\theta(q,p),
\qquad
q' = q+\partial_pT(p').
\]

### 可搜索组件

- magnetic flux；
- orientation-dependent phase；
- topological twist；
- compact torus；
- multi-sheet cover；
- kicked schedule。

### 最小测试

- symplecticity；
- antiunitary symmetry audit；
- primitive UPO；
- Floquet quantization；
- GUE 只作为次级指标。

### 2026-08-05 portfolio activation

The RH breadth-first rule selects this clue as the next project-level task
after parking the exact-$U_c$ Logistic branch at a stable complex-domain
checkpoint. No `TH-0001` candidate exists yet. First inspect the legacy Hénon
parent and freeze exactly one explicit target-free autonomous map, parameter
provenance, clock, normalization, and data firewall. The first prefilter is
limited to symplecticity, antiunitary/time-reversal symmetry, and reproducible
short primitive UPOs; no determinant or zero comparison is opened.

---

## CLUE-A4-002 — Symbolic suspension 可能是最适合解析证明的候选

**来源：** 一维表达上限与 transfer-operator 路线  
**证据：** `HEURISTIC`  
**状态：** `PROMISING`  
**对应层：** `A1`, `A2`, `A3`, `A4`

### 内容

有限/可数状态 subshift 加 roof function 和 potential，可以直接定义 UPO 和 Fredholm determinant。

### 关键问题

- \(\log p\) 是否由低复杂度规则产生；
- 权重是否由 Jacobian/potential 自然产生；
- 是否存在核 transfer operator；
- 是否避免直接编码 primes。

### 最小测试

先构造：

```text
mod-2 baseline
→ mod-6 lift
→ higher residue memory
```

并比较随机图和简化图。

### 2026-08-03 subclass boundary

`SS-0002` 证明 countable branches 和 nuclearity 足以逃离有限状态
`OBR-005`，但并不足以产生 Riemann divisor。若 determinant 直接等于有限面积
模覆盖的 Selberg zeta，则 `OBR-006` 的 \(\Omega(T^2)\) Weyl count 立即阻断。
后续 symbolic-suspension 搜索必须在创建候选前报告自己的 divisor-count
mechanism，而不能仅以“存在 Fredholm determinant”为成功标准。

---

## CLUE-A4-003 — Magnetic quantum graph 作为 Route-A/Route-B 桥梁

**来源：** exact trace formula 思路  
**证据：** `HEURISTIC`  
**状态：** `STOP_SCOPED` for `QG-0001`; broader magnetic-graph clue remains reusable
**对应层：** `A1`, `A2`, `A4`, `B1`, `B4`

### 内容

Quantum graph 的 primitive cycles、magnetic phases 和 secular determinant 使其天然适合连接 classical orbit 与 quantum spectrum。

### 最大风险

直接把 edge length 设置为 \(\log p\) 会变成人工编码。

### 最小测试

搜索低复杂度 graph grammar，使边长或 cycle length 由生成规则产生，而不是逐个输入。

### 2026-08-06 harmonic-tower activation

`QG-0001` freezes one target-free escape from the already-known finite-graph
`OBR-005` class. A fixed asymmetric magnetic lollipop-theta graph with
squarefree lengths is replicated at exact metric scale `1/n`. Its natural
direct-sum magnetic Laplacian has compact resolvent and

\[
N_H(K)=\frac{1+\sqrt2+\sqrt3+\sqrt5}{\pi}K\log K+O(K),
\]

so the target counting exponent arises without prime or zero lookup. The raw
coefficient does not match. `OBR-012` proves that the naive unregularized Euler
product has no finite nonzero value and that the standard direct-sum bond
operator is not trace class. The next test is only the physical base
characteristic function at `k=0`; no determinant regularization or Route B is
yet authorized.

### 2026-08-06 relative-Fredholm closure

The normalized base characteristic and exact component scaling do produce a
genuine same-operator determinant:

\[
H^{-1}\in\mathfrak S_1,
\qquad
D_H(k)=\det_F(I-k^2H^{-1})
=\prod_{n\geq1}\chi_0(k/n).
\]

The component-index genus-one counterphase `exp(-i*k*L0/n)` is forced by the
proved bond identity and the product converges normally. This does not reopen
the naive orbit product or direct-sum bond determinant in `OBR-012`; the local
Fredholm logarithm contains inverse spectral moments, not a proved primitive
orbit trace ledger.

The exact divisor supplies the decisive obstruction

\[
N_H(K)=\frac{L_0}{\pi}K\log K+O(K),
\qquad
2L_0=12.764664694883524\ldots\neq1.
\]

Because the raw clock and normalization are frozen, a zero-free prefactor
cannot repair the leading divisor count (`OBR-013`). `QG-0001` is therefore
`STOP_SCOPED` / `ROUTE_A_REJECTED`, despite the analytic A2/A3 determinant
progress. Reopen the family only with a new intrinsic graph normalization or
component law fixed before target data. Route B remains closed.

---

# CLUE-A1-009 — Coprime renewal suspension

**来源：** 2026-08-09 breadth pivot after the frozen Logistic order audit
**证据：** `MODELING_CHOICE` at creation; upgraded to `PROVED` for the first
trace-class and cycle-ledger theorem edge
**状态：** `ACTIVE`
**对应层：** `A1`, `A2`, `A3`

### 内容

Use the explicit countable recurrent shift

```text
Sigma_cop={(n_k)_{k in Z}: n_k>=2, gcd(n_k,n_{k+1})=1}
tau(n_k)=log(n_0)
```

with symmetric kernel

```text
(L_s)_{mn}=1_{gcd(m,n)=1}(mn)^(-s/2),  Re(s)>1.
```

The cyclic half-roof factors telescope to `prod_i n_i^(-s)`.  The transition
rule is intrinsic and is not a prime table.  A Mobius rank-one decomposition
gives a trace-class holomorphic family on `Re(s)>1`, and exact trace powers
give the coprime cyclic/primitive repetition ledger.

### Strongest reusable evidence

- `||L_s||_1 <= zeta(sigma)^2/zeta(2 sigma)-1` for `sigma=Re(s)>1`;
- the same matrix is unbounded on `ell^2` for `Re(s)<=1`, already on the
  `e_2` column;
- `Tr(L_s)=0` because label one is excluded;
- exact period-two and period-three inclusion-exclusion formulas;
- exact finite rational reproduction through repetition power six.

### Failure boundary

No prime-to-orbit correspondence, von-Mangoldt weight, analytic continuation,
functional equation, `T log T` divisor law, completed-xi equality, or natural
quantization has been shown.  Do not infer arithmetic meaning from the gcd
constraint alone.

### Source lock and first test

```text
configs/source_locks/COPRIME-0001-COUNTABLE-TRACE.yaml
evaluations/route_a/COPRIME-0001/20260809T134933Z.yaml
```

The next smallest test is whether the scalar determinant continues across the
exact `ell^2` operator boundary at `Re(s)=1`, or whether a same-object barrier
can be proved. Root searches and zero comparisons remain forbidden.

---

# 3. Route-B 线索

## CLUE-B1-001 — 自然 Hilbert 空间必须从候选结构中出现

**证据：** `PROJECT_DECISION`  
**状态：** `ACTIVE`  
**对应层：** `B1`

### 内容

Route B 不接受先拟合 spectrum，再临时选择 Hilbert 空间和边界条件。

### 最小 theorem obligation

明确：

```text
Hilbert space
measure
inner product
dense domain
boundary conditions
operator action
closedness
```

---

## CLUE-B2-001 — PT 对称只能作为辅助，不是自伴随证明

**证据：** `ESTABLISHED_EXTERNAL` / 项目规则  
**状态：** `ACTIVE`  
**对应层：** `B2`

### 内容

PT 对称、实数值有限谱和形式 Hermitian 都不足以证明 \(H=H^\ast\)。

### 可行证明工具

- Kato–Rellich；
- essential self-adjointness；
- deficiency indices；
- quadratic forms；
- boundary triplets；
- canonical self-adjoint extension。

---

## CLUE-B3-001 — 关键是 compact resolvent 或正确谱类型，而非紧致相空间

**证据：** `PROJECT_DECISION`  
**状态：** `ACTIVE`  
**对应层：** `B3`

### 内容

非紧致系统也可能具有离散谱；开放系统也可能具有离散 resonances。必须检查实际 operator spectral type。

### 最小 theorem obligation

证明其中之一：

```text
compact resolvent
confining quadratic form
trace-class heat kernel
controlled resonance realization
```

---

## CLUE-B4-001 — von Mangoldt-weighted prime-power trace 是核心门

**来源：** Hilbert–Pólya / explicit-formula 目标  
**证据：** `OPEN`  
**状态：** `ACTIVE`  
**对应层：** `B4`

### 目标

\[
\operatorname{Tr}f(H)
=
\text{smooth term}
+
\sum_p\sum_{r\ge1}
A_{p,r}\widehat f(r\log p).
\]

### 必须解释

- \(\log p\)；
- \(p^{-r/2}\)；
- repetitions；
- multiplicities；
- phases；
- smooth Weyl term。

### 失败条件

只存在半经典类比或低阶数值吻合。

---

## CLUE-B5-001 — completed-xi divisor equality 是最终门

**证据：** `OPEN`  
**状态：** `ACTIVE`  
**对应层：** `B5`

### 目标

\[
\det_\zeta(E-H)
=
e^{q(E)}
\xi\!\left(\frac12+iE\right).
\]

### 必须证明

- determinant 存在；
- prefactor zero-free；
- multiplicity 一致；
- 无额外 eigenvalues；
- 无遗漏 zeros；
- 全局恒等式；
- analytic continuation；
- growth order。

---

# 4. 优先级队列

## Priority 0 — 基础验证

1. `[STOP_SCOPED]` Logistic physical-epsilon medium-fidelity eigenbranch audit
2. `[GO_WITH_LIMITATIONS_CONTROL]` Synthetic Fredholm/Euler-product positive control (`CTRL-0001`, `CLUE-A2-001`)
3. `[STOP_SCOPED]` Strict-monotone autonomous Logistic clock lift (`P4-LOGISTIC-MONOTONE-CLOCK-LIFT`, `OBR-007`)
4. `[DONE]` `LOG-0001` order-at-most-two, `O(T^2)` divisor upper bound, and zero-free right-half-plane theorem
5. `[DONE]` Explicit normalized conformal restriction ratios and fully numerical same-determinant quadratic envelope
6. `[DONE]` Cancellation-safe lower-growth theorem for `D_pol'(2)` and explicit linear maximum-modulus lower bounds
7. `[DONE]` Phragmen--Lindelof audit proving `1<=ord(D_pol)<=2` under the inherited same-object half-plane bound
8. `[NEXT]` Breadth pivot: define one new intrinsic recurrent candidate with an explicit arithmetic-orbit hypothesis, or register a reusable obstruction
9. Candidate-specific shuffled-period / random-weight / random-phase controls only for a newly defined candidate
10. Candidate-specific signed cycle expansion and moving-cutoff drift only for a newly defined candidate
11. `[QUEUED]` Freeze one explicit same-ledger annular residual object from `CLUE-A3-001` after auditing the legacy RH handoff

## Priority 1 — 最值得并行的三条 Route-A 路线

1. Twisted Hénon / kicked symplectic maps
2. Higher-memory symbolic suspension
3. Low-complexity magnetic quantum graphs (`QG-0001` STOP_SCOPED; a new object requires a new lock)

## Priority 2 — 旧 RH 解析纵深

1. Common-clock signed completion  
2. Actual head/counterloop transport  
3. Critical and lower-sideband compensation  
4. Off-alias aggregate  
5. `[QUEUED]` Direct annular theorem, beginning with one explicit same-ledger residual object

## Priority 3 — Route-B 入口

只对 Route-A 强候选启动：

1. natural Hilbert space；
2. operator domain；
3. self-adjointness path；
4. compact resolvent；
5. exact trace formula。

---

# 5. 线索调用模板

```yaml
clue_id:
title:
source:
evidence_status:
current_status:
route:
layer:
candidate_family:
exact_hypothesis:
minimum_test:
success_condition:
failure_condition:
known_obstructions:
latest_evaluation:
next_action:
```

---

# 6. 当前最重要的三个开放问题

## OQ-1

能否从低复杂度动力学规则自然产生：

\[
T_{\gamma_p}=\log p
\]

而不直接编码素数？

## OQ-2

能否从 Jacobian、stability 或 potential 自然产生：

\[
A_{\gamma_p,r}
\sim
\frac{\log p}{p^{r/2}}?
\]

## OQ-3

能否找到一个强 Route-A determinant，同时具有自然 unitary/self-adjoint lift？

这三个问题分别控制：

```text
A1
A1–A2
A4–B1
```

---

# 7. 维护规则

出现以下情况时更新本文件：

- 新候选产生可迁移结构；
- 新 obstruction 被证明；
- 旧线索被反例否定；
- 某线索升级为 theorem；
- Route-A/Route-B Skill 增加新的评估层；
- 旧 RH 路线出现新的 reopening condition。

任何线索升级或降级，必须记录：

```yaml
date:
clue_id:
old_status:
new_status:
evidence:
commit:
consequence:
```

## Status update — CLUE-A1-002

```yaml
date: 2026-08-02
clue_id: CLUE-A1-002
old_status: ACTIVE
new_status: UNDER_TEST
evidence: "SS-0001 exact mod-6 Cayley suspension evaluation"
commit: "5abca8f"
consequence: "Finite residue memory is feasible, but constant-roof finite-state determinants are STOP_SCOPED; next test is the finite-roof O(T) theorem."
```

## Status update — CLUE-A1-002 theorem closure

```yaml
date: 2026-08-02
clue_id: CLUE-A1-002
old_status: UNDER_TEST
new_status: BLOCKED
evidence: "finite-state finite-roof zero-count theorem"
commit: "5abca8f"
consequence: "The finite-state finite-dimensional branch is STOP_SCOPED. Reopen only with an explicit object outside the theorem's assumptions."
```

## Status update — CLUE-A1-002 nuclear reopening closure

```yaml
date: 2026-08-03
clue_id: CLUE-A1-002
old_status: BLOCKED
new_status: BLOCKED
evidence: "SS-0002 paired-Gauss commutator-cover Route-A evaluation and OBR-006"
commit: "current checkpoint; source state 934d85c"
consequence: "A countable-state nuclear escape exists, but the finite-area Selberg subclass is STOP_SCOPED by quadratic Weyl divisor growth. Reopen only with an explicit non-Selberg same-ledger determinant."
```

## Status update — CLUE-A2-005 creation

```yaml
date: 2026-08-03
clue_id: CLUE-A2-005
old_status: null
new_status: UNDER_TEST
evidence: "legacy notebook audit plus target-free deterministic dense/ARPACK smoke profile"
commit: "current checkpoint; source state 338ee15"
consequence: "The fitted prefix is retained as a numerical benchmark, but no formal candidate exists. Freeze and track residual-certified eigenbranches before any new zero comparison or autonomous lift."
```

## Status update — CLUE-A2-005 physical-epsilon closure

```yaml
date: 2026-08-03
clue_id: CLUE-A2-005
old_status: UNDER_TEST
new_status: BLOCKED
evidence: "P4-LOGISTIC-MEDIUM-PHYSICAL-EPSILON version-2 audit: 4 reference strong branches, translated-grid phase-rank failure, and dynamic/static margin median 0.03789"
commit: "current checkpoint; source state ef79805"
consequence: "The frozen occupation-aggregated strong-layer phase observable is STOP_SCOPED, while Route A remains NOT_TESTABLE. Reopen only with an explicit autonomous lift or chronological transfer-cocycle/Fredholm object; do not unlock new zero matching."
```

## Status update — CLUE-A2-001 positive-control closure

```yaml
date: 2026-08-03
clue_id: CLUE-A2-001
old_status: ACTIVE
new_status: ACTIVE
evidence: "CTRL-0001 four-channel q-Pochhammer Fredholm control passes all frozen coefficient, sampled-winding, cutoff, matching, balanced-corruption, executable-ledger, and cancellation gates, with supplemental 50/80/120-dps stability"
commit: "current checkpoint; source state 1088862"
consequence: "The A2 evaluator infrastructure is GO_WITH_LIMITATIONS because sampled winding is not an interval certificate; CTRL-0001 is STOP_SCOPED as a Riemann candidate. Reuse it as a regression benchmark for the next explicit non-Selberg object; do not create SS-0003 from the control."
```

## Status update — CLUE-A1-004 monotone-clock closure

```yaml
date: 2026-08-04
clue_id: CLUE-A1-004
old_status: PROMISING
new_status: BLOCKED
evidence: "P4-LOGISTIC-MONOTONE-CLOCK-LIFT exact compact-clock audit and OBR-007"
commit: "b8fa828"
consequence: "The strict-monotone clock subclass is STOP_SCOPED: every full periodic orbit lies on the static-limit slice and the formal orbit determinant reduces to the static parent. Reopen only with an intrinsic recurrent base or a fully defined chronological transfer-cocycle determinant."
```

## Status update — CLUE-A1-004 recurrent exact-(U_c) audit

```yaml
date: 2026-08-04
clue_id: CLUE-A1-004
old_status: BLOCKED
new_status: ACTIVE
evidence: "P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK exact anchor, recurrent tower census, full-fibre witnesses, and OBR-008"
commit: "95e7260"
consequence: "The recurrent construction escapes OBR-007 but remains a non-candidate REVISE audit. Certify the exact-U_c physical first-return branches and invariant weights before defining a non-lattice roof or transfer determinant."
```

## Status update — CLUE-A1-004 exact-(U_c) first-return support

```yaml
date: 2026-08-04
clue_id: CLUE-A1-004
old_status: ACTIVE
new_status: ACTIVE
evidence: "P4-LOGISTIC-UC-FIRST-RETURN-SUPPORT all-order physical/ambient branch theorem, rational endpoint certificate through return 308, and OBR-009"
commit: "cd2ba4e7fabbcb5ace2466427a57e4d500eeaa27"
consequence: "The physical finite-word alphabet is now proved: one full interval branch for every even label, no physical odd branch, and a nonempty cylinder for every finite even-label word. Ambient odd branches are transient and have zero invariant mass. Route A remains A1_WEAK because exact acip weights, an arithmetic orbit law, and a non-lattice determinant clock are absent. The next task is the endpoint-density / branch-mass-ratio theorem, not a zero fit."
```

## Status update — CLUE-A1-004 exact-($U_c$) acip endpoint theorem

```yaml
date: 2026-08-04
clue_id: CLUE-A1-004
old_status: ACTIVE
new_status: ACTIVE
evidence: "P4-LOGISTIC-UC-ACIP-ENDPOINT-DENSITY direct polar-coordinate acip theorem, corrected published spike cross-check, and independently hardened structural audit"
commit: "84111b3f436ed1e8111c871719e32b70a4def098"
consequence: "The physical acip now exists uniquely with full support, h(-rho+t)=h(0)/(sqrt(2)*U_c)*t^(-1/2)+O(1), and the physical even-branch mass ratio tends to 1/(2*U_c*(U_c-1)). The old ordinary-BV proof remains refuted and Route A remains A1_WEAK/A2_FAIL. Next enclose h(0) and finite branch masses without target data."
```

## Status update — CLUE-A1-004 exact-$U_c$ polar-cone enclosure

```yaml
date: 2026-08-04
clue_id: CLUE-A1-004
old_status: ACTIVE
new_status: ACTIVE
evidence: "P4-LOGISTIC-UC-ACIP-CONE-ENCLOSURE target-free log-Lipschitz cone, explicit endpoint remainder, and certified masses for returns 12,14,16,18"
commit: "8f270de6546928385b93e1dd0b8b78c7ffd40ea8"
consequence: "A coarse absolute enclosure is now available: h(0) in [0.1533974450330445,0.4982637116356999] and C_h in [0.0702656899853137,0.2282361579437252]. Route A remains (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL); next task is a validated sharp tail/resolvent bound or a quantitative remainder, not zero matching."
```

## Status update — CLUE-A1-004 validated sharp exact-$U_c$ polar cone

```yaml
date: 2026-08-05
clue_id: CLUE-A1-004
old_status: ACTIVE
new_status: ACTIVE
evidence: "P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE complete directed Arb cover, sharp invariant cone, and tighter certified masses for returns 12,14,16,18"
commit: "f34117824702404fe0837f5811a5465d33cc65de"
consequence: "The target-free full-domain certificate proves 0.17013<D<0.17014, h(0) in (0.20655,0.40008), and C_h in (0.09461,0.18327). This sharpens the measure-theoretic evidence but does not create an arithmetic primitive-orbit law or determinant, so Route A remains (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL). Next prove a quantitative physical branch-mass-ratio rate in one frozen analytic or cusp-adapted norm; do not compare zeros."
```

## Status update — CLUE-A1-004 quantitative branch-mass-ratio rate

```yaml
date: 2026-08-05
clue_id: CLUE-A1-004
old_status: ACTIVE
new_status: ACTIVE
evidence: "P4-LOGISTIC-UC-BRANCH-MASS-RATE frozen cusp-adapted space, complete Arb derivative interval, exact Fraction rate ledger, and all-tail ratio theorem"
commit: "02727fceef6e7cde3fc4a4452ea409b2faa21f1f"
consequence: "For every n>=6, |mu(C_(2n+2))/mu(C_(2n))-U_c^2/4| <= (36/5)*sqrt(delta_(n-1)) < (243/625)*(3/5)^(n-6). This is a genuine measure-theoretic rate edge but does not create primitive arithmetic orbits or a determinant. Route A remains (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL). Next freeze the polar suspension object (map, branches, roof, clock, function space, determinant convention, data split, and stopping conditions); defer non-lattice/Fredholm audits until that lock is complete."
```

## Status update — CLUE-A1-004 polar intrinsic-roof source lock

```yaml
date: 2026-08-05
clue_id: CLUE-A1-004
old_status: ACTIVE
new_status: ACTIVE
evidence: "P4-LOGISTIC-UC-POLAR-INTRINSIC-ROOF exact lock for doubled polar branches, intrinsic positive roof, separated clocks, analytic space, and conditional Fredholm convention"
commit: "4d5cd7e346445317d2ed19ef90a484cca09c3588"
consequence: "The corrected lock-v2 object is DEFINED_NOT_EVALUATED and creates no formal candidate. The next task is only to prove multiplicative independence of the sealed R/LR roof multipliers; failure is inconclusive rather than a lattice theorem. Complex-space nuclearity, endpoint trace multiplicity, determinant existence, target comparison, and Route B remain closed."
```

## Status update — CLUE-A1-004 exact polar-roof non-lattice theorem

```yaml
date: 2026-08-05
clue_id: CLUE-A1-004
old_status: ACTIVE
new_status: ACTIVE
evidence: "P4-LOGISTIC-UC-POLAR-NONLATTICE exact R/LR multiplier polynomials, finite-field irreducibility certificates, algebraic norms, and multiplicative-independence theorem"
commit: "36a38f0db16652bf0e0c1459be6c69f6bdafec12"
consequence: "The intrinsic roof tau=log|G'| is now PROVED non-lattice because T_LR/T_R is irrational. This escapes the scope of the old unit-clock obstruction OBR-008 but does not establish complex branch inclusion, nuclearity, a Fredholm determinant, arithmetic orbit weights, or target zeros. Route A remains (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL); next audit only the frozen epsilon=1/1000 complex inverse branches and compact inclusion."
```

## Status update — CLUE-A1-004 frozen polar complex branches

```yaml
date: 2026-08-05
clue_id: CLUE-A1-004
old_status: ACTIVE
new_status: ACTIVE
evidence: "P4-LOGISTIC-UC-POLAR-COMPLEX-BRANCH exact common-germ construction, global univalence proof, and 100-digit Arb compact-inclusion margins at epsilon=1/1000"
commit: "3ae5e23508e27129cfa5910473b944026b904ea3"
consequence: "The unchanged frozen complex domain now has one holomorphic t, a, and Log(a), two globally univalent signed composite inverse branches, all four compact inclusions with M<0.59626, and matching-space invariance. This is a PROVED positive structural prior but not nuclearity or a determinant: Route A remains (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL). Next freeze only the doubled partition-hit target-copy and multiplicity rule; defer nuclearity, Fredholm zeros, target divisors, and Route B."
```

## Status update — CLUE-A4-001 RH breadth-first portfolio activation

```yaml
date: 2026-08-05
clue_id: CLUE-A4-001
old_status: PROMISING
new_status: UNDER_TEST
evidence: "Project-level breadth pivot after the Logistic candidate accumulated a stable non-lattice roof and frozen complex branch domain without changing its Route-A tuple"
commit: "3ae5e23508e27129cfa5910473b944026b904ea3"
consequence: "No formal TH-0001 candidate is created. The next task is to inspect the legacy area-preserving Hénon parent and freeze exactly one explicit target-free autonomous Twisted Hénon or kicked-symplectic map. The first Route-A prefilter covers only symplecticity, antiunitary/time-reversal symmetry, and reproducible short primitive UPOs; no determinant or zero fitting is allowed."
```

## Status update — CLUE-A4-001 TH-0001 three-kick prefilter

```yaml
date: 2026-08-06
clue_id: CLUE-A4-001
old_status: UNDER_TEST
new_status: ACTIVE
candidate_id: TH-0001
evidence: "Frozen target-free non-palindromic three-kick Hénon superstep, exact symplectic/generating-function audit, inherited and affine reversor obstructions, and complete global signed UPO prefix through G-period two"
commit: "fb69649afbda27006d56471c5680b590f90ba43b"
evaluation: "evaluations/route_a/TH-0001/20260806T024238Z.yaml"
consequence: "TH-0001 is now a formal candidate with Route-A tuple (A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT), ROUTE_A_EXPLORATORY, and GO_WITH_LIMITATIONS. The short orbit ledger is complete only for G-period <=2; arbitrary nonlinear reversors, higher periods, any determinant, and Route B remain closed. Next freeze same-order Fourier-integral quantization and audit normalization/unitarity plus natural antiunitary symmetry without computing spectra or fitting zeros."
```

## Status update — CLUE-A4-001 TH-0001 same-order unitary FIO lift

```yaml
date: 2026-08-06
clue_id: CLUE-A4-001
old_status: ACTIVE
new_status: ACTIVE
candidate_id: TH-0001
evidence: "TH-0001-A4-FIO-001 exact same-order Fourier-integral factors, Plancherel/modulus-one unitarity on L2(R), exact canonical graph, and inherited antiunitary/cyclic clock-reflection audit"
commit: "836f5880fac6abfb29ee031e1136e24504e2b0a9"
evaluation: "evaluations/route_a/TH-0001/20260806T045554Z.yaml"
consequence: "A4 upgrades from A4_FORMAL_HINT to A4_NATURAL_QUANTIZATION. The ordered U_(5/2)U_(3/2)U_(1/2) propagator is unitary on L2(R), while the natural parent-swap antiunitary reverses each kick but not the non-palindromic superstep. A1 remains weak, A2/A3 remain unopened/failed, arbitrary nonlinear antiunitaries remain OPEN, and Route B stays closed. Preserve the FIO ledger; do not compute spectra or determinants."
```

## Status update — CLUE-A4-001 TH-0001 internal phase caustic

```yaml
date: 2026-08-06
clue_id: CLUE-A4-001
old_status: ACTIVE
new_status: ACTIVE
candidate_id: TH-0001
evidence: "TH-0001-A4-PHASE-CAUSTIC-001 exact ordered internal phase, Hessian determinant 15*q1*q2-1, and rational caustic witness (1,1/15)"
commit: "a4cb10640c44559f0520386d9c84e65c9b873134"
evaluation: "evaluations/route_a/TH-0001/20260806T053410Z.yaml"
obstruction: "OBR-011"
consequence: "A global single reduced phase and global Maslov index are blocked in the current chart, while the ordered oscillatory integral and factorized L2-unitarity remain valid. Do not infer an orbit phase from signed multipliers. Stop this sub-audit unless a multi-chart caustic-transition ledger is explicitly frozen; Route B remains closed."
```

## Status update — CLUE-A4-003 QG-0001 harmonic magnetic tower

```yaml
date: 2026-08-06
clue_id: CLUE-A4-003
old_status: PROMISING
new_status: ACTIVE
candidate_id: QG-0001
evidence: "Exact signed primitive/repetition prefix, natural compact-resolvent magnetic Laplacian, and target-free N(K)=(L0/pi)K*log(K)+O(K) theorem"
commit: "ce0d4424a95a9392c9e8755a4a11b1cfcabc0e77"
evaluation: "evaluations/route_a/QG-0001/20260806T090351Z.yaml"
obstruction: "OBR-012"
consequence: "The harmonic scale tower escapes the fixed finite-graph O(T) count and naturally produces the target counting exponent, but its raw coefficient is wrong and its primitive periods accumulate at zero. The pendant bounce proves that the naive Euler product has no finite nonzero value, while the explicit standard bond blocks have trace norm tending to 8 and hence no trace-class direct sum. Keep heat/spectral zeta separate from a secular divisor; next audit only the physical base characteristic function at k=0. Route B remains closed."
```

## Status update — CLUE-A4-003 QG-0001 base characteristic

```yaml
date: 2026-08-06
clue_id: CLUE-A4-003
candidate_id: QG-0001
subaudit_id: QG-0001-BASE-CHARACTERISTIC-001
old_status: ACTIVE
new_status: ACTIVE
evidence: "The 6x6 sinc-matching determinant is entire and even; C_phys(0)=sqrt(2)+sqrt(3)+sqrt(5)+sqrt(6)+sqrt(15)+3sqrt(10)>0; Delta_bond(k)=-(4/3)k^2*exp(i*k*L0)*C_phys(k) is verified at 80-digit precision, including k=pi"
commit: "af41439b609a5dfb863931ed1e56a0598de5f003"
source_lock: "configs/source_locks/QG-0001-BASE-CHARACTERISTIC.yaml"
evaluation: "evaluations/route_a/QG-0001/20260806T111927Z.yaml"
consequence: "The k=0 bond zero has exact order two and is a plane-wave parametrization artifact, not a physical zero mode. After the explicit zero-free phase removal exp(-i*k*L0), chi_0(k)=1-4.4035597019537134*k^2+O(k^4). This local result does not open a tower determinant or Route B. The next task is one explicit same-operator genus-one relative product with a proved convergence convention."
```

## Status update — CLUE-A4-003 QG-0001 relative Fredholm closure

```yaml
date: 2026-08-06
clue_id: CLUE-A4-003
candidate_id: QG-0001
subaudit_id: QG-0001-RELATIVE-FREDHOLM-001
old_status: ACTIVE
new_status: STOP_SCOPED
evidence: "H^{-1} is trace class; chi_0(k)=det_F(I-k^2 H_1^{-1}); product_n chi_0(k/n)=det_F(I-k^2 H^{-1}) converges normally with exact divisor and multiplicity"
commit: "b5ad4c9ce4305cf055a2e6a3ae957ba4fda7e90b"
source_lock: "configs/source_locks/QG-0001-RELATIVE-FREDHOLM.yaml"
evaluation: "evaluations/route_a/QG-0001/20260806T123946Z.yaml"
obstruction: "OBR-013"
consequence: "The analytic audit reaches A2_ANALYTIC_DETERMINANT and A3_PARTIAL_ANALYTIC_STRUCTURE, but the target interpretation remains A2_FAIL/A3_FAIL. The exact positive divisor count has coefficient L0/pi, larger than the Riemann-von Mangoldt coefficient by 2*L0=12.764664694883524..., and no zero-free factor can repair it under the frozen raw clock. QG-0001 is ROUTE_A_REJECTED/STOP_SCOPED; Route B remains closed. The project pivots breadth-first to CLUE-A3-001."
```

## Status update — CLUE-A1-004 exact-U_c polar partition trace ledger

```yaml
date: 2026-08-07
clue_id: CLUE-A1-004
old_status: ACTIVE
new_status: ACTIVE
evidence: "P4-LOGISTIC-UC-POLAR-PARTITION-TRACE exact endpoint graph, half-open quotient convention, cyclic-word audit through length 8, and matching-range lemma"
commit: "5f055d4f5784528125efbe277c76420cd30a4d32"
consequence: "The geometric target-copy ledger is now explicit: I_L=[-pi/2,0), I_R=[0,pi/2], with the partition point owned by R. The exact boundary graph is P->P, Q->P, Z->Q, so 0 is preperiodic rather than a boundary periodic orbit. Endpoint-copy and cyclic-rotation quotient tests pass, while the local analytic trace correction at P=-pi/2 remains OPEN. Route-A tuple stays (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL); no determinant or Route B is authorized."
```

## Status update — CLUE-A1-004 exact-U_c local boundary trace

```yaml
date: 2026-08-07
clue_id: CLUE-A1-004
old_status: ACTIVE
new_status: ACTIVE
evidence: "P4-LOGISTIC-UC-POLAR-BOUNDARY-TRACE exact weighted-composition trace theorem and 100-digit Taylor-tail certificate"
commit: "fb3fed9355fc1ae0188d4d080f40fadfe6d9ec41"
consequence: "For the unique boundary periodic point P=-pi/2, alpha_0=U_c^2/4 and the local LL trace is alpha_0^s/(1-alpha_0); the pure-L length-n trace is alpha_0^(n*s)/(1-alpha_0^n). P is interior to the complex stadium and has one left lift, so no half or doubled/matching factor appears. This closes the local endpoint trace obligation but not full matching-space nuclearity. Route-A tuple remains (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL), and Route B remains closed."
```

## Status update — CLUE-A1-004 LOG-0001 nuclear Fredholm closure

```yaml
date: 2026-08-08
clue_id: CLUE-A1-004
old_status: ACTIVE
new_status: ACTIVE
candidate_id: LOG-0001
evidence: "Explicit Riemann-map/Taylor order-zero nuclear factorization for every block, complemented matching-space determinant identity, jointly entire canonical Fredholm determinant, exact signed all-power trace theorem, and sealed 510-word regression at 100 digits"
source_commit: "b80900c60044795d2e163edc16de7ed1389e0cd9"
source_lock: "configs/source_locks/LOG-0001-NUCLEAR-FREDHOLM.yaml"
evaluation: "evaluations/route_a/LOG-0001/20260808T051519Z.yaml"
analytic_tuple: [A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL]
riemann_target_tuple: [A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL]
overall: ROUTE_A_EXPLORATORY
verdict: GO_WITH_LIMITATIONS
consequence: "LOG-0001 is now a formal analytic candidate: Delta(lambda,s)=det_Fr(I-lambda*L_s|_B) is a genuine jointly entire same-object determinant and D_pol(s)=Delta(1,s) is entire. This does not supply a log-prime/von-Mangoldt orbit law, divisor count, functional equation, completed-xi structure, quantization, or Route B. Next prove only an intrinsic growth-order bound or high-imaginary-height divisor-count regime; do not compare target zeros first."
```

## Status update — CLUE-A1-004 LOG-0001 growth-order closure

```yaml
date: 2026-08-08
clue_id: CLUE-A1-004
old_status: ACTIVE
new_status: ACTIVE
candidate_id: LOG-0001
evidence: "Two matching-space geometric rank-one streams, an all-order principal-minor majorant with exponent q^2/4-q/2, a global quadratic exponential determinant bound, Jensen divisor upper bounds, and an exact trace-log zero-free half-plane; target-free constants and q<=24 allocations pass at 100 digits"
source_commit: "33986f9633b7f03f2fcc1f6ab914e5e0d69f7050"
research_commit: "ec00bcb"
shared_mirror_commit: "d5ab4b42e66b357859f3b4de560ea5d02bdcf86d"
source_lock: "configs/source_locks/LOG-0001-GROWTH-ORDER.yaml"
evaluation: "evaluations/route_a/LOG-0001/20260808T104049Z.yaml"
analytic_tuple: [A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL]
riemann_target_tuple: [A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL]
overall: ROUTE_A_EXPLORATORY
verdict: GO_WITH_LIMITATIONS
consequence: "The same determinant has classical order at most two, O(T^2) zeros in every fixed real strip, and no zeros for Re(s)>log(2)/log(4/U_c^2), with uniform modulus bounds on each closed sub-half-plane. No exact order, lower growth bound, sharp T log T law, target divisor, quantization, or Route B follows. Next certify explicit conformal restriction ratios r_L,r_R without computing determinant roots."
```

## Status update — CLUE-A1-004 LOG-0001 explicit conformal-ratio closure

```yaml
date: 2026-08-08
clue_id: CLUE-A1-004
old_status: ACTIVE
new_status: ACTIVE
candidate_id: LOG-0001
evidence: "Exact hyperbolic path bound D_*=500*pi+log(4), translation equality r_L=r_R, 4096-bit outward intervals for 1-r_* and -log(r_*), and certified numerical constants in the same determinant's quadratic exponential envelope"
source_commit: "dbb78f10bb3299415e022ecadb20d65e0aac5436"
research_commit: "80107bc8ec2bcb4b5d0dd7a30447c5bc2d075320"
shared_mirror_commit: "ce0e3c88a3daa32ccf79f7fdeb9c0b22695bc6f5"
source_lock: "configs/source_locks/LOG-0001-CONFORMAL-RATIO.yaml"
evaluation: "evaluations/route_a/LOG-0001/20260808T151232Z.yaml"
analytic_tuple: [A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL]
riemann_target_tuple: [A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL]
overall: ROUTE_A_EXPLORATORY
verdict: GO_WITH_LIMITATIONS
consequence: "The proof constants in the existing order-at-most-two theorem are now explicit: r_L=r_R<=tanh((500*pi+log(4))/2)<1 and |D_pol(s)|<=exp(3.45e689+4.20e682*(1+|s|)^2). The constants are coarse upper bounds and give no exact ratio, lower growth, target divisor, quantization, or Route B. Next audit only one cancellation-safe lower-growth mechanism and stop as NOT_TESTABLE if it is not explicit."
```

## Status update — CLUE-A1-004 LOG-0001 cancellation-safe lower growth

```yaml
date: 2026-08-09
clue_id: CLUE-A1-004
old_status: ACTIVE
new_status: ACTIVE
candidate_id: LOG-0001
evidence: "Same-object signed trace-log differentiation at s=2, exact pure-left lower term, 1024-bit outward Arb certificate c_2>0.0213, and Cauchy maximum-modulus bounds"
source_commit: "8cabec587cf0a796f4f004bf5b1b0611de3305f3"
research_commit: "726e42a93a9fabcf07c4c543c1c5962aa0fa1569"
shared_mirror_commit: "8fbe914cf4438a5a792f7e87e0c87e3a88292201"
source_lock: "configs/source_locks/LOG-0001-LOWER-GROWTH.yaml"
evaluation: "evaluations/route_a/LOG-0001/20260809T073000Z.yaml"
analytic_tuple: [A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL]
riemann_target_tuple: [A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL]
overall: ROUTE_A_EXPLORATORY
verdict: GO_WITH_LIMITATIONS
consequence: "D_pol'(2)>0.0213; M_D(R)>0.0213*(R-2) for R>2 and >0.01065*R for R>=4. The determinant is nonconstant and transcendental entire with qualitative super-polynomial maximum-modulus growth. Positive/exact order, zero-count lower bounds, T log T, completed-xi, and Route B remain open. Next: separate Phragmen--Lindelof order-lower audit, then breadth pivot."
```


## Status update — CLUE-A1-004 LOG-0001 Phragmen--Lindelof order lower

~~~yaml
date: 2026-08-09
clue_id: CLUE-A1-004
old_status: ACTIVE
new_status: ACTIVE
candidate_id: LOG-0001
evidence: "Uniform same-object bound on Re(s)>=2, half-plane Phragmen--Lindelof contradiction to ord(D_pol)<1, inherited D_pol'(2)>0.0213 nonconstancy witness, and 1024-bit K_2 certificate"
source_commit: "9b0b09e305579d9ed0ae755b2e499a3bd05a261b"
research_commit: "d1cfa20c6b69503af95abb96ded893eb19329371"
source_lock: "configs/source_locks/LOG-0001-ORDER-LOWER.yaml"
evaluation: "evaluations/route_a/LOG-0001/20260809T110000Z.yaml"
analytic_tuple: [A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL]
riemann_target_tuple: [A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL]
overall: ROUTE_A_EXPLORATORY
verdict: GO_WITH_LIMITATIONS
consequence: "The same determinant now has 1<=ord(D_pol)<=2. Exact order, type, divisor asymptotics, target matching, quantization, Route B, and RH remain open. Apply the breadth pivot next."
~~~

## Status update — CLUE-A1-009 COPRIME-0001 countable trace closure

```yaml
date: 2026-08-09
clue_id: CLUE-A1-009
old_status: ACTIVE
new_status: ACTIVE
candidate_id: COPRIME-0001
evidence: "Mobius rank-one trace-class proof on Re(s)>1, exact cyclic trace-power expansion, period 1--3 primitive census, and Fraction repetition ledger through k=6"
source_lock: "configs/source_locks/COPRIME-0001-COUNTABLE-TRACE.yaml"
evaluation: "evaluations/route_a/COPRIME-0001/20260809T134933Z.yaml"
analytic_tuple: [A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL]
riemann_target_tuple: [A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL]
overall: ROUTE_A_EXPLORATORY
verdict: GO_WITH_LIMITATIONS
consequence: "The first countable recurrent object survives as a target-free theorem edge. The frozen ell^2 matrix is trace class exactly on Re(s)>1 and unbounded on Re(s)<=1. It has no proved prime-orbit law or global divisor mechanism. Next audit only scalar continuation across this boundary or a barrier; keep Route B closed."
```
