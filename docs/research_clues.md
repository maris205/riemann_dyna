# HP-Dynamics 后续研究线索库

**文件名：** `research_clues.md`  
**版本：** v0.1  
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
**证据：** `HEURISTIC` + `MODELING_CHOICE` + `CONDITIONAL_THEOREM` + scoped `PROVED_OBSTRUCTION`
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

The audit defines a recurrent modeled tower with one symbol (m\geq1) for the
even label (L=2m), and the anchored fibre law

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
fixed-point witness. First-return gaps are not themselves periodic orbits;
the tower is an additional modeling choice. Equality of its all-even alphabet
with the physical exact-(U_c) interval/kneading branch system is still open.

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
completed-ξ divisor. The next smallest task is to prove or refute the exact
physical return support and certify branch weights before introducing any
non-lattice roof.

Artifacts:

- `configs/source_locks/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK.yaml`
- `evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T080528Z.yaml`
- `artifacts/p4_logistic_recurrent_uc_anchored_clock/structural_audit.json`
- `formal/obstructions/unit_lattice_clock_vertical_periodicity.md`
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
**证据：** `OPEN`，但已有明确闭合条件  
**状态：** `PROMISING`  
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

### 最小测试

对候选 determinant residual 构造：

```text
annular H∞ residual
annular H2 residual
log-derivative residual
argument-principle discrepancy
```

### 风险

有限网格上的小 norm 不能自动升级为全环域定理。

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
**状态：** `PROMISING`  
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
**状态：** `PROMISING`  
**对应层：** `A1`, `A2`, `A4`, `B1`, `B4`

### 内容

Quantum graph 的 primitive cycles、magnetic phases 和 secular determinant 使其天然适合连接 classical orbit 与 quantum spectrum。

### 最大风险

直接把 edge length 设置为 \(\log p\) 会变成人工编码。

### 最小测试

搜索低复杂度 graph grammar，使边长或 cycle length 由生成规则产生，而不是逐个输入。

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
4. `[NEXT]` Define an intrinsic recurrent base whose periodic orbits leave the static-limit slice, then freeze a nondegenerate same-object determinant before assigning a formal candidate ID
5. Candidate-specific shuffled-period / random-weight / random-phase controls
6. Candidate-specific signed cycle expansion and moving-cutoff drift

## Priority 1 — 最值得并行的三条 Route-A 路线

1. Twisted Hénon / kicked symplectic maps  
2. Higher-memory symbolic suspension  
3. Low-complexity magnetic quantum graphs  

## Priority 2 — 旧 RH 解析纵深

1. Common-clock signed completion  
2. Actual head/counterloop transport  
3. Critical and lower-sideband compensation  
4. Off-alias aggregate  
5. Direct annular theorem  

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
commit: "current checkpoint; evaluation source commit pending"
consequence: "The recurrent construction escapes OBR-007 but remains a non-candidate REVISE audit. Certify the exact-U_c physical first-return branches and invariant weights before defining a non-lattice roof or transfer determinant."
```
