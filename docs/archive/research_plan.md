# AI 驱动的 Hilbert–Pólya 动力学系统搜索：完整研究规划

**项目代号：RiemannForge / HP-Dynamics**  
**版本：v0.1**  
**核心定位：Theory-Guided AI Search for a Riemann Dynamical Determinant**

---

## 0. 项目总览

本项目不直接要求 AI “证明黎曼猜想”，而是把问题拆成两个层次：

### 路线 A：动力学 Zeta / Fredholm 行列式搜索

寻找一个结构自然、可复现、可解析研究的经典动力系统或传递算子，使其加权动力学行列式满足

\[
D_{\mathrm{dyn}}(s)\approx e^{g(s)}\xi(s),
\]

并在逐步提高周期轨道截断阶数后，对黎曼非平凡零点、Riemann–von Mangoldt 计数函数、函数方程和局部 GUE 统计呈现稳定收敛。

路线 A 的目标是发现一个可信的“黎曼动力学行列式候选”。即使无法进一步构造严格自伴随算子，也已经属于重要成果。

### 路线 B：严格 Hilbert–Pólya 实现

对路线 A 中最强候选，构造 Hilbert 空间与量子算子

\[
H:\mathcal D(H)\subset\mathcal H\to\mathcal H,
\]

证明其自伴随性、谱离散性，并建立严格的谱行列式恒等式

\[
\det_{\zeta}(E-H)=e^{q(E)}
\xi\!\left(\frac12+iE\right).
\]

路线 B 成功将构成完整 Hilbert–Pólya 实现，并蕴含黎曼猜想。

---

## 1. 成功等级定义

项目从一开始就采用分级成功标准，避免把“数值拟合”误写成“证明”。

### S0：基础设施成功

完成可复现的候选生成、UPO 枚举、周期轨道权重计算、动力学 Zeta 构造、复零点定位和盲测评估平台。

### S1：弱路线 A 成功

发现候选系统，在参数冻结后，对未参与优化的零点窗口保持显著优于随机基线、GUE 代理和打乱轨道基线的预测能力。

### S2：强路线 A 成功

候选满足：

1. 原始周期轨道长度与 \(\log p\) 存在稳定、非偶然对应；
2. 重复轨道权重接近 \((\log p)p^{-r/2}\) 所要求的结构；
3. 截断动力学行列式的零点随周期上限增加稳定收敛；
4. 函数方程、共轭对称、全局计数函数和局部统计同时成立；
5. 结果由两个独立算法复现；
6. 候选规则中未直接编码素数表或零点表。

这已经可以形成高水平的“黎曼 Zeta 的经典动力学实现”论文。

### S3：路线 B 部分成功

找到自然量子化 \(F\mapsto U_F\) 或 \(F\mapsto H_F\)，并证明算子对称性、可闭性或本质自伴随性的关键部分。

### S4：完整路线 B 成功

证明：

\[
H=H^\ast,
\qquad
(H-zI)^{-1}\ \text{紧致或具有目标离散谱},
\]

以及

\[
\det_{\zeta}(E-H)=e^{q(E)}
\xi\!\left(\frac12+iE\right).
\]

---

## 2. 已有论文提供的理论先验

现有工作不是最终答案，而是搜索空间的强先验与负向约束。

### 2.1 Prime–Chaos 工作：算术骨架先验

已有结果提示：

- 素数筛与 Logistic 映射 band-merging / Misiurewicz 临界结构存在符号动力学联系；
- 奇偶刚性可以表现为动力系统禁止字；
- 非自治 logarithmic aging 可能承担密度衰减；
- 孪生素数常数可作为低阶算术不变量进行校准。

路线 A 不应从任意微分方程盲搜，而应优先搜索具有明确符号编码、临界轨道骨架和可控周期轨道的系统。

### 2.2 Transient Chaos 工作：一维模型的边界

已有结果指出：

- 一维 unimodal 映射在有限筛阶段存在 MSS admissibility 缺陷；
- 这些缺陷在宏观遍历意义下可以衰减；
- 一维有限状态投影可以捕获 mod-2 奇偶刚性；
- 但无法产生 Hardy–Littlewood mod-3 resonance；
- 因而一维模型更像 prime arithmetic 的 abelian / mod-2 holographic projection。

由此得到核心搜索结论：

\[
\boxed{\text{Logistic 模型保留为先验和基线，不再作为最终完整宿主。}}
\]

主搜索应转向二维以上、具有相位记忆、残数类记忆或非阿贝尔扩张的系统。

### 2.3 Sequential Birkhoff 工作：非自治漂移的解析先验

已有工作给出慢参数漂移的条件框架：

- uniform inducing scheme；
- uniform Lasota–Yorke inequality；
- transfer operator spectral gap；
- Keller–Liverani stability；
- uniform decay of correlations；
- one-sided parameter set；
- logarithmic drift \(u_n\to u_c\)。

因此非自治候选必须优先选择能够验证上述结构的系统族，而不是任意经验 schedule。

### 2.4 Non-autonomous Logistic 谱工作：数值基线

此前利用有限维 transfer matrix、Gaussian smoothing、时间平均和 eigenphase mapping 得到过零点相关数值现象。新项目将其保留为：

- 复现实验基线；
- 有限精度与过拟合研究对象；
- 数值 Zeta 管线的对照组。

但不把单点锚定、线性回归或有限网格谱相似视作路线 A 的通过条件。

### 2.5 Area-Preserving Hénon 工作：保守提升先验

已有工作完成了：

\[
\text{1D dissipative arithmetic projection}
\longrightarrow
\text{2D area-preserving candidate host}.
\]

其重要价值是：

- 明确 \(\det J=1\) 的保守提升方向；
- 引入自然的周期轨道、同宿结构和 Floquet 量子化；
- 建立全局计数与局部 GUE 诊断；
- 显示低误差最优点可能非常尖锐，稳健误差明显更高；
- 明确 GUE 统计是必要但不具有唯一性的诊断。

新项目应把 Hénon 视为“母模板”，重点探索 Hénon-like symplectic map 加磁相位、拓扑 twist、多分支记忆和非自治扩张。

---

## 3. 核心数学目标

### 3.1 完成化目标函数

优先使用完成化黎曼函数

\[
\xi(s)
=
\frac12 s(s-1)\pi^{-s/2}
\Gamma\!\left(\frac{s}{2}\right)\zeta(s),
\]

避免只匹配 \(\zeta(s)\) 时遗漏 Gamma 因子、平凡零点、极点与函数方程。

路线 A 的最终目标写为

\[
D_{\mathrm{dyn}}(s)
=
e^{g(s)}\xi(s),
\]

其中 \(g(s)\) 为不引入额外零点的整函数。

### 3.2 加权动力学 Zeta

对原始周期轨道集合 \(\mathcal P\)，定义

\[
Z_{\mathrm{dyn}}(s)
=
\prod_{\gamma\in\mathcal P}
\left(1-w_\gamma e^{-sT_\gamma}\right)^{-1},
\]

或相应 Fredholm determinant

\[
D_{\mathrm{dyn}}(s)
=
\det(I-\mathcal L_s).
\]

工程实现必须在配置中明确 determinant convention，禁止在不同实验中混用 \(Z\)、\(1/Z\)、\(Z'/Z\)。

### 3.3 轨道字典目标

理想对应关系为

\[
p\leftrightarrow \gamma_p,
\qquad
T_{\gamma_p}=\log p,
\]

并在第 \(r\) 次重复轨道上产生

\[
A_{\gamma_p,r}
\sim
\frac{\log p}{p^{r/2}},
\]

以及正确的 Maslov、磁通或拓扑相位。

仅有 \(T_p\approx \log p\) 不算完整通过，必须同时考察：

- primitive orbit multiplicity；
- repetitions；
- monodromy / stability multiplier；
- phase；
- degeneracy；
- orbit orientation。

---

## 4. 研究假设

### H1：高维提升假设

一维 Logistic 的 mod-2 骨架能够嵌入二维或更高维保守系统，而新增自由度承担 mod-3 及更高 residue-class memory。

### H2：磁拓扑 twist 假设

在 symplectic map 或 suspension flow 中加入磁相位、holonomy 或 orientation-dependent phase，可在保持保守量子化的同时打破反幺正时间反演对称性，产生 GUE 类。

### H3：Prime orbit roof-function 假设

某类 symbolic suspension、graph flow 或 transfer operator 的 roof function 与 Jacobian 权重能够自然地产生 \(\log p\) 与 \(p^{-1/2}\) 结构，而非人工逐个编码。

### H4：解析延拓假设

候选的 transfer operator 在合适 Banach/Hilbert 空间上具有核性、迹类性质或可控亚纯延拓，使 cycle expansion 不只是有限截断拟合。

### H5：自然量子化假设

强路线 A 候选存在不依赖零点拟合的自然量子化，并可建立 classical orbit determinant 与 quantum spectral determinant 的桥梁。

---

## 5. 候选系统优先级

### Tier 0：校准与对照

这些系统不作为发现结果，只用于测试评估管线。

1. **Synthetic Euler-product positive control**  
   直接使用 \(T_p=\log p\)、标准权重构造目标 Zeta，验证零点定位与截断误差。

2. **Shuffled-prime control**  
   打乱 \(\log p\) 顺序或加入随机扰动，检测指标是否能识别算术结构消失。

3. **Random-weight control**  
   保留周期，随机化稳定权重和相位。

4. **GUE / CUE control**  
   验证局部统计指标不能单独区分黎曼系统。

5. **Random symplectic-map control**  
   检验“混沌 + GUE”是否产生大量假阳性。

### Tier 1：最高优先级

#### A. Hénon-like symplectic maps with twist

一般形式：

\[
p_{n+1}=p_n-\partial_q V(q_n)+A_\theta(q_n,p_n),
\]

\[
q_{n+1}=q_n+\partial_p T(p_{n+1}).
\]

可搜索组件：

- cubic/quartic/multimodal \(V(q)\)；
- magnetic phase；
- kick sequence；
- orientation-dependent twist；
- slow logarithmic schedule；
- compact torus / bounded box；
- multi-sheet cover。

优点：继承现有 Hénon 代码与经验，周期轨道和 Floquet 量子化均较自然。

#### B. Symbolic subshift + suspension flow

定义有限或可数状态转移图、roof function \(\tau(e)\)、势函数 \(\phi(e)\)，形成

\[
Z(s)=
\prod_{\gamma}
\left(
1-e^{-sT_\gamma+\Phi_\gamma}
\right)^{-1}.
\]

优点：

- UPO 枚举最清晰；
- cycle expansion 最成熟；
- 可逐步加入 mod-2、mod-3、mod-\(q\) 记忆；
- 适合解析证明；
- 容易建立 transfer operator。

风险：可能过于接近“人工编码素数”，必须设置复杂度和非循环性约束。

#### C. Twisted baker / cat / kicked maps

在紧致相空间上构造多分支辛映射，引入 magnetic flux 或 unitary twist。

优点：

- 量子化成熟；
- UPO 可精确枚举；
- 时间反演破缺可明确检测；
- 适合大规模搜索。

### Tier 2：重要并行方向

#### D. Quantum / metric graphs

利用 primitive cycles、edge lengths 和 magnetic phases 构造 spectral determinant。

优点：经典周期轨道与量子谱之间已有精确 trace formula 结构。

风险：若 edge length 直接设为 \(\log p\)，仅是编码而非发现。必须搜索低复杂度生成规则。

#### E. Expanding maps / Schottky-type transfer operators

搜索具有核 transfer operator、Fredholm determinant 和严格解析延拓的系统。

优点：路线 A 的解析成功概率较高。

#### F. Contact Anosov / geodesic flows

研究 Ruelle / Selberg 型行列式与量子谱桥梁。

优点：最接近经典—量子严格对应范式。

风险：计算和证明成本高，不适合第一阶段大规模盲搜。

### Tier 3：长期探索

- noncommutative geometry；
- adelic / \(p\)-adic dynamics；
- arithmetic hyperbolic surfaces；
- trace-formula categorical constructions；
- operator algebras and non-self-adjoint similarity transforms。

---

## 6. 候选系统 DSL

为防止 AI 生成无法比较的任意代码，定义统一 CandidateSpec。

```python
@dataclass(frozen=True)
class CandidateSpec:
    family: str
    dimension: int
    phase_space: dict
    parameters: dict
    map_definition: dict
    flow_definition: dict | None
    symbolic_partition: dict | None
    roof_function: dict | None
    potential_function: dict | None
    weight_rule: dict
    boundary_conditions: dict
    time_reversal_rule: dict
    quantization_hint: dict | None
    schedule: dict | None
    description_length: int
    uses_prime_table: bool
    uses_zero_table: bool
```

硬约束：

- `uses_prime_table=False`
- `uses_zero_table=False`
- 候选定义不得调用 benchmark 数据文件；
- 搜索器只接收训练指标，不接触验证与测试零点；
- 所有参数和函数表达式必须可序列化；
- 对每个候选计算 description length；
- 禁止通过高阶插值、多项式列表或神经网络权重隐式记忆零点。

---

## 7. 软件架构

```text
hp-dynamics/
├── README.md
├── pyproject.toml
├── configs/
│   ├── candidates/
│   ├── searches/
│   └── benchmarks/
├── src/hpdyn/
│   ├── core/
│   │   ├── specs.py
│   │   ├── protocols.py
│   │   └── registry.py
│   ├── candidates/
│   │   ├── logistic.py
│   │   ├── henon.py
│   │   ├── twisted_henon.py
│   │   ├── kicked_maps.py
│   │   ├── subshifts.py
│   │   ├── quantum_graphs.py
│   │   └── controls.py
│   ├── orbits/
│   │   ├── symbolic_enum.py
│   │   ├── newton_solver.py
│   │   ├── interval_solver.py
│   │   ├── primitive.py
│   │   ├── monodromy.py
│   │   └── database.py
│   ├── zeta/
│   │   ├── conventions.py
│   │   ├── euler_product.py
│   │   ├── cycle_expansion.py
│   │   ├── fredholm.py
│   │   ├── analytic_continuation.py
│   │   └── root_finding.py
│   ├── spectral/
│   │   ├── riemann_data.py
│   │   ├── counting.py
│   │   ├── unfolding.py
│   │   ├── gue_metrics.py
│   │   ├── functional_equation.py
│   │   └── robustness.py
│   ├── search/
│   │   ├── stages.py
│   │   ├── objectives.py
│   │   ├── evolutionary.py
│   │   ├── bayesian.py
│   │   ├── novelty.py
│   │   └── scheduler.py
│   ├── certification/
│   │   ├── argument_principle.py
│   │   ├── interval_roots.py
│   │   ├── truncation_bounds.py
│   │   └── reproducibility.py
│   ├── agents/
│   │   ├── generator.py
│   │   ├── falsifier.py
│   │   ├── theorist.py
│   │   ├── formalizer.py
│   │   └── reviewer.py
│   └── cli.py
├── tests/
├── experiments/
├── notebooks/
├── reports/
├── artifacts/
├── formal/
│   ├── lean/
│   └── theorem_notes/
└── docs/
```

### 核心 CLI

```bash
hpdyn reproduce logistic-prime
hpdyn reproduce henon-spectrum
hpdyn enumerate-upos --candidate configs/candidates/x.yaml --period-max 16
hpdyn build-zeta --orbit-db artifacts/orbits/x.parquet
hpdyn locate-zeros --determinant artifacts/zeta/x.json
hpdyn evaluate --run-id RUN_ID --split validation
hpdyn search --config configs/searches/twisted_henon_v1.yaml
hpdyn certify --run-id RUN_ID
hpdyn report --run-id RUN_ID
```

---

## 8. 多 Agent 分工

### 8.1 Candidate Generator

职责：

- 基于当前最优候选提出结构性变异；
- 只能调用 Candidate DSL；
- 输出新候选的数学定义、参数范围与动机；
- 不接触测试数据。

### 8.2 Orbit Analyst

职责：

- 枚举 primitive UPO；
- 去除重复轨道；
- 计算周期、作用量、monodromy、稳定乘子和相位；
- 给出漏轨道风险报告。

### 8.3 Zeta Builder

职责：

- 构建 Euler product、cycle expansion 和 Fredholm approximation；
- 对不同 determinant convention 分开实现；
- 估计截断误差和收敛半径。

### 8.4 Spectral Validator

职责：

- 训练、验证、测试严格隔离；
- 计算零点坐标、计数函数、函数方程、GUE 指标；
- 执行 shuffled / random-weight / random-map 对照。

### 8.5 Operator Theorist

职责：

- 检查量子化自然性；
- 提议 Hilbert 空间、定义域和边界条件；
- 分析对称性、自伴随性、紧致预解式和谱行列式。

### 8.6 Formalizer

职责：

- 将已稳定的有限组合引理、轨道唯一性、对称性和算子命题转成 Lean；
- 不形式化尚未稳定的猜测。

### 8.7 Adversarial Falsifier

职责：

- 主动寻找额外零点；
- 改变网格、精度、截断、初始条件和 unfolding；
- 检测数据泄露、参数记忆和单位变化；
- 尝试构造与候选表现相同的随机替代模型。

### 8.8 Research Manager

职责：

- 记录每个结论的 epistemic status：
  - established；
  - proved in project；
  - numerically certified；
  - numerical observation；
  - heuristic；
  - conjecture；
- 未通过盲测的结果不得进入主结论。

---

## 9. 搜索漏斗

### Stage 0：硬结构过滤

淘汰：

- 无可定义 UPO；
- 轨道大量逃逸且无 trapped set；
- 无自然权重规则；
- 量子化完全依赖事后拟合；
- 明确使用 prime / zero lookup；
- 描述复杂度超限；
- 时间反演结构与目标矛盾且无可控 twist；
- 数值不稳定。

### Stage 1：廉价符号代理

预算：每候选秒级。

指标：

- topological entropy；
- parity rigidity；
- residue-memory capacity；
- primitive orbit growth；
- orbit-length histogram；
- Lyapunov spectrum；
- trapped-set size；
- antiunitary symmetry test。

保留前 1%–5%。

### Stage 2：短 UPO 字典

预算：每候选分钟级。

- period max 8–16；
- primitive orbit deduplication；
- \(T_\gamma\) 与 \(\log p\) 的 assignment cost；
- stability-weight consistency；
- phase consistency；
- orbit-count growth。

保留前 0.1%–1%。

### Stage 3：低阶动力学 Zeta

预算：每候选 10 分钟至数小时。

- cycle expansion order 6、8、10、12；
- 前 20 个零点训练；
- 参数冻结；
- 检查第 21–100 零点；
- 检查额外零点和截断稳定性。

### Stage 4：高阶盲测

- 第 101–1000 零点；
- 高度分散的随机 holdout windows；
- 不允许重新缩放；
- 不允许修改 offset；
- 不允许重新选择 unfolding；
- 与所有对照模型比较。

### Stage 5：数值认证

- argument principle 计数；
- interval arithmetic；
- root isolation；
- 两种独立 UPO 枚举算法；
- 两种独立 determinant 计算；
- truncation stability；
- precision scaling；
- containerized reproduction。

### Stage 6：路线 B 入口审查

只有同时满足以下条件才进入：

1. 轨道结构不是纯拟合；
2. 有自然 Hilbert 空间；
3. 有自然量子化；
4. 自伴随性有可执行证明路线；
5. determinant identity 有已知理论工具可借用；
6. 候选在高阶盲测中稳定。

---

## 10. Loss Function

总损失：

\[
\mathcal L_{\mathrm{total}}
=
\lambda_1\mathcal L_{\mathrm{orbit}}
+
\lambda_2\mathcal L_{\mathrm{weight}}
+
\lambda_3\mathcal L_{\mathrm{zero}}
+
\lambda_4\mathcal L_{\mathrm{count}}
+
\lambda_5\mathcal L_{\mathrm{FE}}
+
\lambda_6\mathcal L_{\mathrm{GUE}}
+
\lambda_7\mathcal L_{\mathrm{robust}}
+
\lambda_8\mathcal L_{\mathrm{complexity}}
+
\mathcal P_{\mathrm{hard}}.
\]

### 10.1 Orbit length loss

对 primitive periods \(T_j\) 与训练素数 \(\log p_j\) 使用 Hungarian assignment：

\[
\mathcal L_{\mathrm{orbit}}
=
\frac1M
\min_{\pi}
\sum_{j=1}^{M}
\frac{|T_j-\log p_{\pi(j)}|^2}
     {1+\log^2 p_{\pi(j)}}.
\]

需额外惩罚：

- unmatched orbits；
- duplicated prime assignments；
- excessive degeneracy；
- missing repetitions。

### 10.2 Weight loss

\[
\mathcal L_{\mathrm{weight}}
=
\frac1{|\Omega|}
\sum_{(p,r)\in\Omega}
\left|
\log |A_{p,r}|
-
\log\left(\frac{\log p}{p^{r/2}}\right)
\right|^2.
\]

相位单独计算 circular distance。

### 10.3 Zero loss

使用局部平均间距归一化：

\[
\mathcal L_{\mathrm{zero}}
=
\frac1N
\sum_n
\left(
\frac{\widehat\gamma_n-\gamma_n}
     {\Delta_{\mathrm{mean}}(\gamma_n)}
\right)^2.
\]

训练损失仅可访问训练区。

### 10.4 Counting-function loss

\[
\mathcal L_{\mathrm{count}}
=
\left\|
N_{\mathrm{dyn}}(E)
-
N_{\mathrm{RvM}}(E)
\right\|^2,
\]

其中

\[
N_{\mathrm{RvM}}(E)
=
\frac{E}{2\pi}\log\frac{E}{2\pi}
-
\frac{E}{2\pi}
+
\frac78
+\cdots.
\]

### 10.5 Functional-equation loss

\[
\mathcal L_{\mathrm{FE}}
=
\mathbb E_{s\in\mathcal G}
\frac{|D(s)-D(1-s)|^2}
     {1+|D(s)|^2+|D(1-s)|^2}.
\]

### 10.6 GUE loss

包含：

- nearest-neighbor spacing distribution；
- pair correlation；
- number variance \(\Sigma^2(L)\)；
- Dyson–Mehta \(\Delta_3(L)\)。

GUE loss 权重不能高于 orbit、weight、zero 和 count loss，因为 GUE 是通用混沌特征。

### 10.7 Robustness loss

改变：

- UPO cutoff；
- cycle order；
- floating precision；
- grid；
- seed；
- initial conditions；
- root-finding contour；

若结果大幅变化则惩罚。

### 10.8 Complexity loss

\[
\mathcal L_{\mathrm{complexity}}
=
c_1(\text{参数个数})
+c_2(\text{表达式节点数})
+c_3(\text{状态数})
+c_4(\text{特殊常数数目}).
\]

### 10.9 Hard penalty

以下情况直接赋无穷损失：

- benchmark leakage；
- 显式调用 primes/zeros；
- 测试后重新拟合；
- determinant convention 不明确；
- 结果不能复现；
- 数值异常被静默忽略。

---

## 11. 数据集与盲测协议

### 11.1 Riemann zero split

建议初始划分：

- Train：1–20；
- Validation-1：21–100；
- Validation-2：101–300；
- Test：301–1000；
- Deep Test：从更高位置抽取多个不连续窗口。

最终论文发布前再保留一组团队未查看的 sealed holdout。

### 11.2 Prime orbit split

- Train primes：前 20 或前 50；
- Validation primes：接续区间；
- Test primes：更大素数区间；
- 检查对应是否随 \(p\) 增大持续，而不是低阶偶然。

### 11.3 对照数据

必须包括：

- shuffled \(\log p\)；
- random lengths with same density；
- random weights；
- Poisson spectrum；
- GUE/CUE spectrum；
- random symplectic maps；
- 系统参数邻域样本。

### 11.4 参数冻结规则

训练结束后生成不可修改 manifest：

```yaml
candidate_hash: ...
code_commit: ...
parameters: ...
determinant_convention: ...
orbit_cutoffs: ...
precision: ...
unfolding_rule: ...
created_at: ...
```

后续验证只读取 manifest。

---

## 12. UPO 计算方法

### 12.1 映射类系统

对周期 \(n\) 求解

\[
F^n(x)-x=0.
\]

流程：

1. symbolic word enumeration；
2. coarse seed generation；
3. Newton / quasi-Newton；
4. interval Newton certification；
5. primitive period test；
6. cyclic symmetry canonicalization；
7. orbit orientation normalization；
8. monodromy matrix；
9. stability multiplier；
10. action / phase。

### 12.2 Flow 类系统

- 选择 Poincaré section；
- 搜索 return map fixed points；
- 计算 primitive flow period；
- 对重复轨道单独标记；
- 使用 variational equation 计算 monodromy。

### 12.3 防止漏轨道

- symbolic enumeration 与 random shooting 双算法交叉；
- orbit count 与 topological entropy 对照；
- 周期增长率异常时标记 incomplete；
- interval boxes coverage；
- known benchmark maps 回归测试。

---

## 13. 动力学 Zeta 计算

### 13.1 三种并行实现

1. **Direct Euler product**：用于低周期快速筛选；
2. **Cycle expansion**：利用 shadowing cancellations；
3. **Transfer-operator Fredholm determinant**：用于强候选与解析研究。

### 13.2 收敛诊断

对 cutoff \(T_{\max}\) 或 cycle order \(N\) 检查：

\[
D_N(s)\to D_{N+1}(s),
\qquad
\widehat\gamma_n^{(N)}
\to
\widehat\gamma_n^{(N+1)}.
\]

必须报告：

- root drift；
- zero count drift；
- contour integral residual；
- omitted-orbit estimate；
- precision dependence。

### 13.3 复零点定位

- coarse complex grid；
- argument principle；
- contour subdivision；
- Newton refinement；
- interval root enclosure；
- conjugate-pair consistency。

---

## 14. 路线 B 的证明任务树

### B1. Hilbert 空间

明确：

- \(\mathcal H\)；
- 测度；
- 内积；
- dense domain；
- boundary conditions。

### B2. 算子定义

构造：

- Hamiltonian \(H\)；
- Floquet unitary \(U\)；
- generator；
- transfer-operator-to-quantum correspondence。

### B3. 自伴随性

优先路线：

- Kato–Rellich；
- quadratic form；
- essential self-adjointness；
- deficiency indices；
- boundary triplets；
- unitary equivalence；
- similarity to self-adjoint operator with bounded positive metric。

### B4. 离散谱

证明：

- compact resolvent；
- confining form；
- trace-class heat kernel；
- suitable scattering resonance interpretation。

### B5. Trace formula

目标：

\[
\operatorname{Tr}f(H)
=
\text{smooth term}
+
\sum_{p,r}
A_{p,r}\widehat f(r\log p).
\]

要求是严格恒等式或具有可控误差的极限，而非仅半经典直觉。

### B6. Spectral determinant

构造 zeta-regularized determinant，并证明

\[
\det_\zeta(E-H)
=
e^{q(E)}
\xi\!\left(\frac12+iE\right).
\]

### B7. Formal verification

优先形式化：

- 算子对称性；
- 边界条件；
- primitive orbit combinatorics；
- determinant finite approximations；
- 关键有限恒等式；
- 解析证明中的易错引理。

---

## 15. 阶段规划

## Phase 0：工程基线（第 1–2 周）

目标：

- 建立仓库、CI、配置系统和实验注册；
- 导入 primes 与 Riemann zeros benchmark；
- 实现 epistemic-status 模板；
- 实现 train/validation/test 隔离；
- 完成 synthetic Euler-product positive control。

交付：

- `hpdyn` CLI；
- 50+ 单元测试；
- baseline report；
- 可复现容器。

通过标准：

- synthetic determinant 能稳定恢复目标零点；
- shuffled control 显著退化；
- 不同精度结果一致。

## Phase 1：复现既有论文（第 3–6 周）

任务：

- Logistic band-merging；
- MSS symbolic sequence；
- Q3/Q5 defects；
- parity-gap diagnostics；
- sequential drift；
- Hénon phase portrait；
- homoclinic tangency；
- quantum / Markov spectrum；
- GUE diagnostics。

目的不是重复发表，而是建立可信回归测试。

交付：

- `reproduce/` 全套脚本；
- 每篇论文的 claim-status 对照表；
- 数值敏感性报告。

## Phase 2：通用 UPO–Zeta 引擎（第 7–12 周）

任务：

- primitive orbit enumeration；
- interval Newton；
- monodromy；
- cycle expansion；
- argument-principle root finder；
- orbit database；
- benchmark maps 测试。

交付：

- Logistic、Hénon、cat map、baker map 的 UPO 测试；
- UPO 完备性报告；
- Zeta convention 文档。

## Phase 3：三条候选线并行（第 13–20 周）

### Track A：Twisted Hénon

- magnetic twist；
- broken antiunitary symmetry；
- compactification；
- slow schedule；
- UPO search。

### Track B：Symbolic Suspension

- mod-2 baseline；
- mod-3 lift；
- multi-residue state graph；
- roof and potential search；
- exact transfer matrix。

### Track C：Twisted Quantum Graph

- low-complexity graph grammar；
- generated edge lengths；
- magnetic flux；
- exact trace formula。

每条 Track 均执行 Stage 0–3。

## Phase 4：AI 搜索与盲测（第 21–32 周）

- evolutionary search；
- Bayesian optimization；
- novelty search；
- LLM structural mutations；
- adversarial controls；
- high-order holdout。

交付：

- top 20 candidate registry；
- frozen manifests；
- validation leaderboard；
- negative-result catalog。

## Phase 5：强候选认证与路线 A 论文（第 33–44 周）

- 更高 UPO cutoff；
- 独立算法；
- interval certification；
- function equation；
- zero-free / extra-zero scan；
- robustness；
- complexity audit；
- theoretical lemma extraction。

可能输出：

1. 搜索基础设施论文；
2. 路线 A 候选论文；
3. 若无强候选，则输出系统性 negative result / impossibility boundary。

## Phase 6：路线 B 可行性（第 45–60 周）

- 为 top 1–3 候选构造量子化；
- 定义 Hilbert 空间；
- 研究自伴随性；
- 建立局部 trace formula；
- 判断是否值得长期推进。

## Phase 7：严格 Hilbert–Pólya（开放周期）

该阶段不设置虚假的固定截止时间，以 theorem milestone 管理。

---

## 16. 前 14 天 Codex 冲刺

### Day 1–2：仓库与配置

- Python 3.12；
- `uv` 或 Poetry；
- ruff、mypy、pytest；
- Typer CLI；
- YAML/Pydantic 配置；
- GitHub Actions；
- Dockerfile。

### Day 3：Benchmark 数据

- primes；
- \(\log p\)；
- Riemann zeros；
- Riemann–von Mangoldt；
- split manager；
- sealed test interface。

### Day 4–5：Synthetic Euler Product

- truncated Euler product；
- completed factors；
- complex evaluation；
- argument-principle zero count；
- root refinement。

### Day 6–7：Controls

- shuffled lengths；
- random weights；
- Poisson；
- GUE/CUE；
- random symplectic spectrum。

### Day 8–9：Logistic UPO

- symbolic orbit enumeration；
- primitive detection；
- period and multiplier；
- regression tests。

### Day 10–11：Hénon UPO

- periodic root solver；
- monodromy；
- orbit canonicalization；
- known fixed points / short cycles tests。

### Day 12：Cycle Expansion v0

- direct product；
- logarithmic form；
- numerical stabilization；
- cutoff comparison。

### Day 13：Evaluation

- zero normalized MAE；
- count loss；
- GUE diagnostics；
- robustness suite。

### Day 14：Baseline Report

输出：

- `reports/sprint_01.md`；
- plots；
- JSON metrics；
- failure list；
- next sprint issue list。

---

## 17. 首批 GitHub Issues

1. Scaffold Python package and CI  
2. Implement immutable CandidateSpec  
3. Implement experiment registry  
4. Add Riemann zero dataset loader  
5. Add prime and log-prime dataset loader  
6. Implement split firewall  
7. Implement synthetic Euler-product control  
8. Implement completed \(\xi\)-factor utilities  
9. Implement complex contour argument principle  
10. Implement root isolation  
11. Implement shuffled-length control  
12. Implement random-weight control  
13. Implement GUE/CUE baseline generator  
14. Implement symbolic primitive word enumeration  
15. Implement Logistic periodic-orbit solver  
16. Implement Hénon periodic-orbit solver  
17. Implement monodromy and stability weights  
18. Implement orbit canonicalization  
19. Implement cycle expansion v0  
20. Implement zero matching metrics  
21. Implement Riemann–von Mangoldt count metric  
22. Implement functional-equation residual  
23. Implement GUE diagnostics  
24. Implement reproducibility manifest  
25. Reproduce Q3/Q5 MSS defects  
26. Reproduce Hénon short-cycle spectrum  
27. Add TwistedHénon candidate  
28. Add symbolic suspension candidate  
29. Add quantum-graph control  
30. Generate Sprint 01 report

---

## 18. 工程质量要求

- 所有 public API 带 type hints；
- 数值异常不得静默 `except`；
- 每个算法给出 precision 和 tolerance；
- 所有随机过程显式 seed；
- 每个实验自动保存 commit hash；
- 所有图由脚本生成；
- 数据与图分离；
- 不允许 notebook 成为唯一实现；
- 关键计算至少两条独立 code path；
- 长任务支持 checkpoint；
- 支持 CPU 多进程；
- 后续再加入 GPU；
- 不使用 test zeros 调参；
- 每个结论带 epistemic status。

---

## 19. 主要风险与应对

### 风险 1：有限零点过拟合

应对：

- 小训练集；
- 连续与不连续 holdout；
- 参数冻结；
- complexity penalty；
- shuffled controls；
- 高位零点盲测。

### 风险 2：UPO 指数爆炸

应对：

- symbolic pruning；
- cycle expansion；
- shadowing cancellations；
- distributed enumeration；
- 先选 uniformly hyperbolic candidates。

### 风险 3：edge-of-chaos 导致 Zeta 不收敛

应对：

- 将临界模型作为先验，不强制候选停在非一致双曲点；
- 搜索其 uniformly hyperbolic extension；
- 使用 induced maps；
- 对非双曲候选设置高计算成本惩罚。

### 风险 4：GUE 假阳性

应对：

- GUE 只做低权重指标；
- 强制 orbit weights、actual zeros、counting function 和 functional equation 同时通过。

### 风险 5：直接编码素数

应对：

- Candidate DSL；
- source audit；
- description length；
- 禁止 lookup；
- 训练/测试数据隔离；
- 对常数表达式做静态检查。

### 风险 6：路线 A 无法量子化

应对：

- 这不否定路线 A 的价值；
- 单独发表 classical dynamical determinant；
- 继续搜索同 determinant 的可量子化 realization。

### 风险 7：路线 B 证明过难

应对：

- 拆解为 operator-domain、self-adjointness、compactness、trace formula、determinant 五篇/五阶段；
- 优先选择理论工具成熟的候选族。

---

## 20. 论文路线

### Paper A0：Benchmark / Infrastructure

**题目方向：**  
*An AI-Ready Benchmark for Inverse Trace-Formula Search*

内容：

- Candidate DSL；
- UPO–Zeta engine；
- blind evaluation；
- controls；
- reproducibility；
- negative baselines。

### Paper A1：Strong Candidate

**题目方向：**  
*Theory-Guided Search for a Riemann Dynamical Determinant*

内容：

- 候选系统；
- primitive orbit dictionary；
- weighted cycle expansion；
- blind zero tests；
- analytic structure；
- robustness。

### Paper A2：Higher-Rank Arithmetic Lift

若 symbolic suspension / higher-dimensional lift 成功：

*From a Mod-2 Holographic Prime Model to Higher-Rank Arithmetic Dynamics*

### Paper B1：Quantization

*Quantization of a Prime-Orbit Dynamical System*

### Paper B2：Hilbert–Pólya Realization

仅在严格证明完成后使用该标题。

---

## 21. Codex 主提示词

下面内容可直接交给 Codex：

```text
You are the lead research engineer for the HP-Dynamics project.

Goal:
Build a reproducible research platform for theory-guided search of classical dynamical systems whose weighted dynamical zeta/Fredholm determinant approximates the completed Riemann xi function. The platform must support a later rigorous Hilbert–Pólya operator program.

Non-negotiable rules:
1. Never use validation or test Riemann zeros for optimization.
2. Candidate definitions must not read prime tables or zero tables.
3. Every determinant convention must be explicit.
4. Every numerical result must include precision, truncation, tolerance, seed, commit hash, and configuration.
5. Separate proved, numerically certified, numerical, heuristic, and conjectural statements.
6. Do not hide numerical failures.
7. Implement reusable modules, not notebook-only prototypes.
8. Add tests before expanding search complexity.

Initial milestone:
Complete Phase 0 and the 14-day sprint described in docs/research_plan.md.

Required stack:
- Python 3.12
- numpy, scipy, mpmath, sympy
- pydantic, typer, rich
- numba where useful
- pandas or polars for orbit tables
- pytest, hypothesis, mypy, ruff
- matplotlib for plots
- optional python-flint for interval/certified arithmetic

First deliverables:
1. Repository scaffold.
2. CandidateSpec and experiment registry.
3. Riemann/primes datasets with split firewall.
4. Synthetic Euler-product positive control.
5. Shuffled/random/GUE controls.
6. Logistic and Hénon short-period UPO solvers.
7. Cycle-expansion v0.
8. Argument-principle complex root finder.
9. Evaluation metrics.
10. reports/sprint_01.md.

Before coding:
- Read all documents under docs/prior_work/.
- Create docs/claims_matrix.md listing every prior claim and its status.
- Create docs/architecture.md.
- Create GitHub-style issues in docs/issues/.
- Then implement milestone tasks in small tested commits.

At the end of every work session:
- Run tests.
- Save metrics.
- Update the research log.
- List failed assumptions.
- Propose only the next smallest verifiable step.
```

---

## 22. 最终执行建议

第一阶段不要只押 Hénon，也不要同时铺开十几类系统。建议采用“三主线 + 一基线”：

\[
\boxed{
\begin{aligned}
&\text{Baseline: Logistic / current Hénon reproduction}\\
&\text{Track A: Twisted Hénon / kicked symplectic maps}\\
&\text{Track B: Symbolic suspension with higher residue memory}\\
&\text{Track C: Low-complexity twisted quantum graphs}
\end{aligned}}
\]

原因：

- Track A 最接近现有代码；
- Track B 最适合 UPO–Zeta 和解析证明；
- Track C 最接近 exact trace formula 与路线 B；
- 三者可以相互提供结构线索，而非互相替代。

最现实且高价值的近期目标是：

\[
\boxed{
\text{在 6–10 个月内得到一个经严格盲测的强路线 A 候选，}
}
\]

或者得到一个清晰的维数、对称性或 orbit-weight 不可能性边界。

无论哪一种，都将把现有 prime-chaos 系列从“数值类比”推进到“可证伪、可认证、可量子化评估的逆迹公式研究计划”。
