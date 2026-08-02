# HP-Dynamics 多 Agent 研究执行计划

**文件名：** `agent_plan.md`  
**版本：** v0.1  
**适用项目：** HP-Dynamics / RiemannForge  
**目标周期：** 30 天高强度探索，兼容后续 6 个月完整研究计划  
**运行模式：** 一个主 Agent 统一调度，多个受限子 Agent 并行执行，仓库为唯一事实源

---

## 0. 总原则

本项目采用：

\[
\boxed{
\text{一个主 Agent}
+
\text{多个专业子 Agent}
+
\text{单一仓库事实源}
+
\text{严格状态机}
+
\text{敌对验证}
}
\]

项目目标不是让多个 Agent 同时“自由证明 RH”，而是将复杂研究拆成可验证、可停止、可复现的最小任务。

所有账号、API、计算资源和订阅必须在授权范围内使用，并遵守相应服务条款。不得共享账号凭证、绕过平台限制或通过自动化规避正常配额机制。

---

# 1. 项目目标

## 1.1 30 天目标

高概率目标：

1. 完成 UPO–Zeta 通用研究平台；
2. 完成五篇基础论文与旧 RH 路线的关键回归；
3. 跑通三个横向 Route-A Track；
4. 建立一个纵向旧 RH 解析 Track；
5. 形成冻结候选、反例和 obstruction registry；
6. 找到若干值得继续解析研究的候选。

中等概率目标：

- 找到 1–3 个参数冻结后仍能通过初步盲测的 S1 候选；
- 提炼新的周期轨道、权重或 signed-cancellation 结构；
- 在旧 RH Track 中得到一个新的 moving-order theorem 或严格阻塞结果。

惊喜目标：

- 找到强 Route-A 候选；
- 候选的轨道长度、稳定权重、零点、计数函数与解析结构同时稳定；
- 找到自然量子化入口。

## 1.2 不作为 30 天承诺的目标

以下目标不可作为时间承诺：

- 完整 Hilbert–Pólya 算子；
- 自伴随性与紧致预解式的完整证明；
- von Mangoldt 加权迹公式；
- 与 completed \(\xi\) 的严格 divisor equality；
- 黎曼猜想证明。

---

# 2. 唯一事实源

所有 Agent 必须遵守：

```text
Git repository
+ current handoff
+ claims matrix
+ frozen manifests
+ result registry
= sole source of truth
```

聊天记录、Agent 自己的长期上下文、临时笔记和口头总结都不是项目事实源。

建议仓库根目录包含：

```text
AGENTS.md
agent_plan.md
RH_HANDOFF.md
HP_HANDOFF.md
CHANGELOG.md

docs/
├── research_plan.md
├── architecture.md
├── prior_work/
│   ├── README.md
│   └── claims_matrix.md
├── related_programs/
│   └── legacy_rh_program/
├── obstruction_registry.md
├── candidate_registry.md
├── research_log.md
└── issues/

src/hpdyn/
legacy/
experiments/
artifacts/
reports/
formal/
```

---

# 3. Agent 拓扑

## 3.1 主 Agent：`hp-project-lead`

主 Agent 是唯一拥有以下权限的 Agent：

- 确定当前研究路线；
- 激活或停止 Track；
- 创建候选 ID；
- 修改 handoff；
- 修改全局 claims matrix；
- 决定参数冻结；
- 决定候选状态迁移；
- 合并分支；
- 创建发布 commit；
- 授权论文写作；
- 宣布 `GO`、`STOP_SCOPED`、`NOT_TESTABLE` 或 `REJECTED`。

主 Agent 不应亲自承担所有计算。它的核心职责是：

```text
任务分解
→ 资源调度
→ 定义冻结
→ 结果审核
→ 冲突消解
→ 状态迁移
→ 研究方向调整
```

## 3.2 同时活跃的子 Agent 上限

默认最多三个子 Agent 并行：

1. 一个发现或构造 Agent；
2. 一个计算或实验 Agent；
3. 一个敌对审计 Agent。

出现论文草稿后，`hp-paper-writer` 替换其中一个子 Agent，不作为第四个并行 Agent。

草稿进入发布阶段后，`hp-release-qa` 再替换一个只读站位。

原因：

- 数学定义容易漂移；
- 多 Agent 并行修改同一对象容易产生 determinant convention 冲突；
- 并发越多，验证和整合成本增长越快；
- 三个专业站位足以形成发现—计算—证伪闭环。

---

# 4. 专业 Agent 角色

## 4.1 `hp-candidate-generator`

### 职责

- 生成新的动力系统候选；
- 对现有候选进行低复杂度结构变异；
- 提出跨学科迁移方案；
- 使用 Candidate DSL 输出可序列化候选；
- 给出候选的数学动机和可证伪预测。

### 禁止

- 读取 test 或 sealed Riemann zeros；
- 直接读取 prime/zero lookup 表来定义候选；
- 用高阶多项式、神经网络权重或超长常数表隐式记忆数据；
- 修改候选验证结果；
- 声称发现 Hilbert–Pólya 算子。

### 输出格式

```yaml
candidate_id:
parent_id:
family:
exact_definition:
structural_change:
motivation:
free_parameters:
description_length:
expected_orbit_signature:
expected_failure_mode:
required_compute:
recommended_first_test:
```

---

## 4.2 `hp-orbit-zeta-worker`

### 职责

- 枚举 primitive UPO；
- 进行轨道去重和完备性检查；
- 计算 period、action、monodromy、stability、phase；
- 构建 direct product、cycle expansion 或 Fredholm approximation；
- 定位复零点；
- 记录截断和精度依赖。

### 强制数据结构

每个周期轨道至少保存：

```python
OrbitContribution(
    orbit_id=...,
    primitive_period=...,
    repetition=...,
    action=...,
    stability_multiplier=...,
    amplitude=...,
    phase=...,
    orientation_sign=...,
    alias_class=...,
    certification_status=...,
)
```

不得只保存绝对权重。旧 RH 路线已经显示，signed/complex cancellation 可能是问题核心。

### 输出格式

```yaml
candidate_id:
orbit_cutoff:
primitive_orbit_count:
expected_orbit_count:
completeness_warning:
zeta_convention:
precision:
root_count:
root_locations:
cutoff_drift:
extra_zero_scan:
artifacts:
reproduction_command:
```

---

## 4.3 `hp-spectral-validator`

### 职责

- 实施 train / validation / test 隔离；
- 计算 zero loss；
- 计算 Riemann–von Mangoldt counting loss；
- 计算 functional-equation residual；
- 计算 GUE diagnostics；
- 运行 shuffled/random/control candidates；
- 检查参数冻结后的泛化。

### 禁止

- 看见 validation/test 后重新调参；
- 改变 unfolding 以改善结果；
- 事后改变 scale 或 offset；
- 只报告最优 seed；
- 忽略额外零点。

### 输出格式

```yaml
candidate_id:
manifest_hash:
split:
metrics:
control_comparison:
extra_zeros:
missing_zeros:
robustness:
leakage_audit:
verdict:
```

---

## 4.4 `hp-proof-auditor`

### 职责

- 审查定义、假设和结论；
- 搜索反例；
- 检查 theorem 是否偷换数据类型；
- 检查不同 determinant decomposition 是否被非法拼接；
- 检查时钟、归一化和 cutoff 是否统一；
- 检查 signed sum 是否被错误地拆成绝对值；
- 检查抽象 completion 是否被误写为物理系统；
- 标记未证明的 moving-order 结论。

### 标准判决

```text
GO
GO_WITH_LIMITATIONS
REVISE
STOP_SCOPED
NOT_TESTABLE
REJECTED
```

### 输出格式

```yaml
claim:
data_type:
clock:
normalization:
hypotheses:
proved:
not_proved:
counterexample:
hidden_fit:
scope_violation:
verdict:
next_smallest_test:
```

---

## 4.5 `hp-legacy-rh-worker`

### 职责

专门负责 Track D：

- 读取 `RH_HANDOFF.md`；
- 保持旧 RH 路线的数据类型、物理时钟和 Hardy normalization；
- 推进 actual noisy-head/counterloop、critical alias、lower sideband、off-alias aggregate 或 annular norm 路线；
- 将旧 RH 的 obstruction 转为新项目可复用规则。

### 强制限制

- 不得把 RH-341 的 abstract completion 当作物理 operator；
- 不得使用错误时钟；
- 不得把 mandatory atom 和 signed complement 分别取绝对值；
- 不得在没有 theorem edge 时创建下一编号；
- 不得将 Gate A–E 标记为完成。

---

## 4.6 `hp-operator-theorist`

只在候选达到 `ANALYTIC_REVIEW` 后激活。

### 职责

- 寻找自然 Hilbert 空间；
- 明确定义域和边界条件；
- 检查自然量子化；
- 研究反幺正时间反演对称性；
- 分析对称性、自伴随性和紧致预解式；
- 搜索 exact trace formula 或 spectral determinant identity。

### 禁止

不得因有限矩阵具有实谱就声称自伴随。

---

## 4.7 `hp-paper-writer`

只在主 Agent 给出明确 `GO` 后激活。

### 职责

- 根据冻结结果和 claims registry 写论文；
- 不创造新数学结果；
- 不修改实验；
- 严格区分 theorem、conditional theorem、numerical observation、heuristic 和 modeling choice。

论文写作过程中发现逻辑缺口，应停止写作并返回主 Agent。

---

## 4.8 `hp-release-qa`

### 职责

- 运行全部测试；
- 校验结果文件；
- 检查图表与正文一致；
- 检查 claim status；
- 检查提交文件范围；
- 检查 PDF、字体、引用和可复现命令；
- 检查 handoff 是否更新。

---

# 5. 账号与资源分配

本计划按“资源槽位”分配，不绑定特定账号。资源槽只使用合法授权、符合服务条款的账号或计算资源。

## 5.1 两个资源槽

如果当前只有两个可用槽位：

### Slot 1：主 Agent

```text
hp-project-lead
+ 短时 proof audit
+ 仓库整合
```

### Slot 2：轮换 Worker

按 6–12 小时轮换：

```text
Track A worker
→ Track B worker
→ validator
→ Track C worker
→ legacy RH worker
→ validator
```

这种模式最稳健，避免额度耗尽后项目失去主控。

## 5.2 三个资源槽

```text
Slot 1：主 Agent
Slot 2：当前主搜索 Track
Slot 3：proof auditor / validator
```

主搜索 Track 每 12–24 小时轮换一次。

## 5.3 四至五个资源槽

```text
Slot 1：主 Agent
Slot 2：Track A — twisted symplectic
Slot 3：Track B — symbolic suspension
Slot 4：Track C — magnetic quantum graph
Slot 5：Track D — legacy RH / adversarial validation
```

即使有更多槽位，同时写权限仍限制在：

```text
1 个主 Agent
+ 最多 3 个互不重叠的子工作区
```

多余资源优先用于：

- 独立复算；
- 只读文献搜索；
- 对照实验；
- proof audit；
- 长时间数值任务。

不应继续增加自由写入 Agent。

---

# 6. 分支与工作区规则

建议使用独立 worktree：

```text
worktrees/
├── lead/
├── track-a/
├── track-b/
├── track-c/
├── track-d/
└── audit/
```

分支命名：

```text
lead/main-integration
track-a/<candidate-or-task>
track-b/<candidate-or-task>
track-c/<candidate-or-task>
track-d/<rh-task>
audit/<candidate-or-claim>
```

## 6.1 文件所有权

同一时刻一个文件只能有一个写入 Owner。

示例：

```yaml
src/hpdyn/candidates/twisted_henon.py: track-a
src/hpdyn/candidates/subshifts.py: track-b
src/hpdyn/candidates/quantum_graphs.py: track-c
docs/related_programs/legacy_rh_program/: track-d
HP_HANDOFF.md: lead only
claims_matrix.md: lead only
candidate_registry.md: lead only
```

## 6.2 子 Agent 禁止事项

子 Agent 不得：

- 直接 push 到 main；
- 修改 handoff；
- 修改全局 claims matrix；
- 修改不属于自己的 Track；
- 合并其他分支；
- 删除 unrelated caches 或研究文件；
- 创建论文编号；
- 发布结果。

---

# 7. 候选状态机

每个候选只能处于一个状态：

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

## 7.1 状态迁移

```text
GENERATED
  ↓ hard structural checks
STRUCTURE_PASSED
  ↓ UPO completeness and weight checks
UPO_PASSED
  ↓ training-only Zeta evaluation
ZETA_TRAIN_PASSED
  ↓ immutable manifest
PARAMETERS_FROZEN
  ↓ blind validation
VALIDATION_PASSED
  ↓ adversarial controls
ADVERSARIAL_PASSED
  ↓ theory audit
ANALYTIC_REVIEW
  ↓ natural quantization path
ROUTE_B_ELIGIBLE
```

任何阶段都可进入：

```text
REJECTED
STOP_SCOPED
NOT_TESTABLE
```

## 7.2 状态变更记录

```yaml
candidate_id:
previous_state:
new_state:
date:
commit:
manifest:
evidence:
metrics:
failed_controls:
known_assumptions:
reviewer:
next_action:
```

只有主 Agent 可批准状态迁移。

---

# 8. 任务激活协议

## 8.1 Source Lock

任何任务开始前，子 Agent 必须冻结：

```text
对象定义
数据类型
参数范围
时钟
归一化
cutoff
determinant convention
训练数据
禁止访问的数据
预期输出
停止条件
```

Source Lock 示例：

```yaml
task_id: HP-A-017
candidate_id: TH-0042
data_type: primitive_orbit_ledger_v2
clock: map_iteration
normalization: completed_xi_v1
cutoff: period <= 14
determinant_convention: det_I_minus_L
train_zeros: 1..20
forbidden_zeros: 21+
stop_conditions:
  - orbit completeness below 95%
  - direct prime lookup detected
  - extra-zero count exceeds threshold
```

## 8.2 GO 条件

只有以下结果可以触发新一轮状态变化：

- 新的可复现候选；
- 新的严格反例；
- 新的解析恒等式；
- 新的 certified numerical result；
- 明确降低某个开放问题；
- 新的物理或数学 obstruction；
- 独立算法复现。

以下不算 theorem edge：

- 换图；
- 换 seed；
- 轻微降低训练 loss；
- 重新措辞；
- 相同结论的另一次有限拟合；
- 没有新严格内容的论文编号。

---

# 9. 24 小时运行节奏

## 9.1 推荐周期

每 24 小时分为四个研究窗口：

### Window A：00:00–06:00

- 长时间 UPO 枚举；
- 参数扫描；
- determinant 计算；
- 独立复算。

### Window B：06:00–12:00

- 主 Agent 汇总；
- proof auditor 检查夜间结果；
- 淘汰明显伪影；
- 冻结值得继续的候选。

### Window C：12:00–18:00

- 结构变异；
- 理论迁移；
- 新候选小预算筛选；
- 旧 RH 解析任务。

### Window D：18:00–24:00

- adversarial validation；
- 控制实验；
- 写入 research log；
- 创建下一轮 source lock；
- checkpoint 和 git 同步。

实际时间可调整，但必须保留：

```text
生成
→ 计算
→ 审计
→ 汇总
```

四个阶段。

## 9.2 每 6–12 小时 checkpoint

子 Agent 输出：

```yaml
task:
status:
compute_used:
completed:
best_result:
strongest_failure:
artifacts:
reproduction_command:
blocker:
recommended_verdict:
```

不得只返回长篇自然语言总结。

---

# 10. 额度与上下文管理

## 10.1 主 Agent 额度保护

主 Agent 不运行大规模细节计算。

主 Agent 主要消耗用于：

- 阅读 compact evidence；
- 任务分解；
- 冲突消解；
- 关键证明审计；
- 更新 handoff；
- 最终决策。

大规模代码生成、实验和文献扫描交给 Worker。

## 10.2 Context Reset 协议

任何 Agent 上下文过长或即将更换资源槽时，必须生成 handoff：

```markdown
# Agent Handoff

Task:
Branch:
Commit:
Source lock:
Definitions:
Completed:
Failed:
Strongest evidence:
Artifacts:
Exact reproduction command:
Known risks:
Next smallest step:
Forbidden shortcuts:
```

新 Agent 只从仓库 handoff 接续，不依赖旧对话。

## 10.3 Token 节流

子 Agent 应优先返回：

- 路径；
- commit；
- JSON metrics；
- 表格；
- 精确 blocker；
- reproduction command。

避免重复粘贴完整论文、完整日志和大段代码。

---

# 11. 四条 Track

## Track A：Twisted symplectic dynamics

研究对象：

- twisted Hénon；
- kicked maps；
- torus compactification；
- magnetic phase；
- broken antiunitary symmetry；
- non-autonomous or autonomous higher-dimensional lift。

首要问题：

- 是否存在稳定的 prime-like primitive orbit dictionary？
- twist 是否自然产生正确相位？
- 是否支持自然 Floquet quantization？
- 是否仅产生通用 GUE，而没有算术内容？

## Track B：Symbolic suspension

研究对象：

- finite/countable subshifts；
- mod-2 → mod-3 → higher residue memory；
- roof function；
- weighted transfer operator；
- exact cycle expansion。

首要问题：

- \(\log p\) 是否能从低复杂度规则产生？
- \(p^{-r/2}\) 是否能由 Jacobian/potential 产生？
- 是否避免直接编码素数？
- 是否存在核 transfer operator？

## Track C：Magnetic quantum graphs

研究对象：

- low-complexity graph grammar；
- generated edge lengths；
- magnetic flux；
- exact trace formula；
- unitary scattering matrix。

首要问题：

- primitive cycles 是否产生 prime-power trace structure？
- edge length 是否自然，而非直接设置为 \(\log p\)？
- 是否能进入 Route B？

## Track D：Legacy Hardy signed-completion route

研究对象：

- actual noisy-head/counterloop transport；
- critical alias \(2k\)；
- lower sideband \(2k-2\)；
- off-alias aggregate；
- direct annular \(H^\infty/H^2\) theorem；
- Gate A activation conditions。

首要规则：

- 统一物理时钟；
- 统一 Hardy 数据类型；
- 保留 signed compensation；
- 无 theorem edge 不创建下一编号。

---

# 12. 每周节奏

## Week 1：基础设施与复现

- 仓库、CI、CandidateSpec；
- train/validation/test firewall；
- synthetic Euler-product positive control；
- shuffled/random/GUE controls；
- 五篇基础论文关键回归；
- 旧 RH route mapping；
- Logistic/Hénon short UPO。

出口标准：

```text
平台能恢复人工正例，
也能拒绝明显随机伪目标。
```

## Week 2：UPO–Zeta 引擎

- primitive orbit；
- monodromy；
- signed/complex weights；
- repetitions；
- cycle expansion；
- argument principle；
- cutoff drift；
- extra-zero scan；
- moving-order metrics。

出口标准：

```text
至少两个已知动力系统的 UPO–Zeta 结果可复现，
且截断误差被显式报告。
```

## Week 3：多 Track 搜索

- Track A/B/C 并行；
- Track D 延续解析纵深；
- 多目标排名；
- 保留多样性；
- 每日淘汰。

出口标准：

```text
Top 20 候选冻结，
每条 Track 至少保留一个非平凡候选或严格负结果。
```

## Week 4：集中证伪

- 停止大规模生成；
- 独立重算；
- 高精度；
- 更高 cutoff；
- 高位零点盲测；
- random controls；
- data leakage audit；
- natural quantization audit；
- frontier report。

出口标准：

```text
3–5 个初步幸存候选，
或明确的系统族不可能性边界。
```

---

# 13. 主 Agent 每日任务

每日必须完成：

1. 查看所有子 Agent checkpoint；
2. 查看 git 状态和未合并分支；
3. 审核候选状态迁移；
4. 更新 `candidate_registry.md`；
5. 更新 `obstruction_registry.md`；
6. 更新 `research_log.md`；
7. 冻结下一轮 source locks；
8. 结束或降级低价值 Track；
9. 确保 validator 未接触训练外数据；
10. 保留一个计算槽用于独立复算。

每日结束摘要：

```markdown
# Daily Frontier

Date:
Active tracks:
Candidates generated:
Candidates rejected:
Candidates frozen:
Best new evidence:
Strongest new obstruction:
Independent reproductions:
Open blockers:
Compute/resource status:
Tomorrow source locks:
Claim boundary:
```

---

# 14. 候选排名

禁止使用单一 zero loss 排名。

建议总评分：

\[
S =
w_1S_{\mathrm{orbit}}
+w_2S_{\mathrm{weight}}
+w_3S_{\mathrm{zero}}
+w_4S_{\mathrm{count}}
+w_5S_{\mathrm{FE}}
+w_6S_{\mathrm{robust}}
+w_7S_{\mathrm{analytic}}
-w_8C_{\mathrm{complexity}}.
\]

其中：

```text
orbit + weight
> zero coordinates
> counting + functional equation
> robustness
> GUE
```

GUE 仅是次级一致性指标。

候选必须单独报告：

- train score；
- validation score；
- adversarial score；
- control margin；
- cutoff drift；
- extra-zero count；
- description length。

---

# 15. 强制对照

每个候选至少与以下对象比较：

1. shuffled orbit lengths；
2. random weights；
3. random phases；
4. same-density random lengths；
5. Poisson spectrum；
6. GUE/CUE spectrum；
7. neighboring candidate parameters；
8. simpler parent candidate；
9. prime-table positive control；
10. data-leakage detector。

候选只有在明显优于其简化模型和随机对照时，才值得继续。

---

# 16. 独立复现门槛

任何结果在进入主日志结论前，必须经过：

```text
原 Worker 复算
→ 独立 Worker 用不同实现复算
→ Proof Auditor 审计
→ 主 Agent 冻结 manifest
```

重大候选还需：

- 不同 precision；
- 不同 UPO enumerator；
- 不同 root finder；
- 不同机器或环境；
- 容器化重现。

---

# 17. 停止规则

## 17.1 `REJECTED`

适用：

- 数据泄露；
- 明确数学错误；
- 额外零点严重；
- 结果完全依赖测试后拟合；
- 候选复杂度等于隐式编码目标；
- 独立复算失败。

## 17.2 `STOP_SCOPED`

适用：

- 当前方法已证明不可能达到所需精度；
- 绝对值 majorant 必然发散；
- 错误时钟或错误数据类型；
- 当前假设无法支持目标结论。

## 17.3 `NOT_TESTABLE`

适用：

- 缺少实际物理 operator；
- 只有 abstract completion；
- 缺少 moving-order theorem；
- UPO 枚举无法认证；
- 所需源对象尚未定义。

停止不是失败。精确的停止条件和 obstruction 是项目成果。

---

# 18. 安全与研究诚信

必须遵守：

- 不把 numerical observation 写成 theorem；
- 不把 finite fit 写成 all-order asymptotic；
- 不把 real finite spectrum 写成 self-adjointness；
- 不把 GUE 写成 Riemann 唯一指纹；
- 不把 abstract determinant 写成 physical dynamics；
- 不把不同 decomposition 的局部结果拼接；
- 不隐藏失败 seed；
- 不使用测试数据调参；
- 不删除负结果。

每个结论必须带状态：

```text
ESTABLISHED_EXTERNAL
PROVED_IN_PROJECT
CONDITIONAL_THEOREM
NUMERICALLY_CERTIFIED
NUMERICAL_OBSERVATION
HEURISTIC
CONJECTURE
MODELING_CHOICE
FITTED_PARAMETER
OPEN
REFUTED
SUPERSEDED
```

---

# 19. 主 Agent 系统提示词

可将下述内容放入主 Agent 的启动提示：

```text
You are the sole project lead for HP-Dynamics.

The repository, not chat memory, is the source of truth.

Your job is to coordinate a theory-guided AI search for dynamical systems
whose weighted dynamical zeta or Fredholm determinant may realize the
completed Riemann xi function, while preserving a strict boundary between
Route A numerical/classical discovery and Route B Hilbert–Pólya proof.

You are the only agent allowed to:
- modify HP_HANDOFF.md;
- approve candidate state transitions;
- merge branches;
- freeze manifests;
- authorize paper writing;
- publish commits;
- change global claim status.

Run at most three subagents concurrently:
1. one candidate/theory worker;
2. one orbit/zeta or legacy-RH worker;
3. one adversarial validator/proof auditor.

A paper writer replaces one worker only after an explicit GO.
Release QA replaces one read-only station after a draft exists.

Before every task, create a source lock fixing:
- mathematical object;
- data type;
- clock;
- normalization;
- cutoff;
- determinant convention;
- allowed data;
- forbidden data;
- stopping conditions.

Never:
- optimize on validation or test zeros;
- combine results from incompatible determinant decompositions;
- switch clocks or normalizations mid-proof;
- split a required signed cancellation into separate absolute bounds;
- treat an abstract algebraic completion as a physical system;
- promote GUE statistics to a unique Riemann signature;
- infer self-adjointness from a finite real spectrum;
- create a new paper or task number without a new theorem edge.

Use the candidate state machine:
GENERATED → STRUCTURE_PASSED → UPO_PASSED →
ZETA_TRAIN_PASSED → PARAMETERS_FROZEN →
VALIDATION_PASSED → ADVERSARIAL_PASSED →
ANALYTIC_REVIEW → ROUTE_B_ELIGIBLE.

At any stage use REJECTED, STOP_SCOPED, or NOT_TESTABLE.

Require independent reproduction before promoting any result.
Keep compact evidence, exact metrics, artifact paths, and reproduction commands.
Update the research log, candidate registry, obstruction registry, and handoff
at every stable checkpoint.

The immediate 30-day objective is not to prove RH. It is to determine whether
the search space contains a genuine strong Route-A candidate, or to produce
new theorem-backed impossibility boundaries.
```

---

# 20. 子 Agent 通用提示词

```text
You are a scoped HP-Dynamics research worker.

Read:
- AGENTS.md
- agent_plan.md
- HP_HANDOFF.md
- docs/prior_work/README.md
- docs/prior_work/claims_matrix.md
- the exact source-lock file for your task

The repository is the sole source of truth.

Do not modify:
- HP_HANDOFF.md
- global claims_matrix.md
- candidate_registry.md
- other tracks
- main branch

Return compact evidence:
- exact definition;
- exact calculation;
- metrics;
- strongest failure;
- artifact paths;
- reproduction command;
- recommended verdict;
- next smallest test.

Do not claim more than your source lock supports.
Stop with STOP_SCOPED or NOT_TESTABLE when the required object or theorem
edge is absent.
```

---

# 21. 第一天启动清单

主 Agent：

```text
[ ] 读取 research_plan.md
[ ] 读取 agent_plan.md
[ ] 读取 prior_work README 和 claims matrix
[ ] 读取 RH_HANDOFF.md
[ ] 检查 git 状态
[ ] 建立 worktrees
[ ] 建立 candidate registry
[ ] 建立 obstruction registry
[ ] 建立 research log
[ ] 冻结 Week 1 source locks
[ ] 启动最多三个子 Agent
```

首批子任务：

### Worker 1

```text
复现 synthetic Euler-product positive control
+ argument-principle root count
```

### Worker 2

```text
复现 Logistic/Hénon short UPO
+ primitive orbit database
```

### Worker 3

```text
敌对审计数据隔离、determinant convention
和五篇论文回归任务
```

完成后再激活 Track A/B/C/D。

---

# 22. 一个月结束时的交付物

```text
HP_HANDOFF.md
30_day_frontier_report.md
candidate_registry.md
obstruction_registry.md
claims_matrix.md
reproduction_manifest.json
top_candidates/
negative_results/
certified_controls/
route_b_entry_audit.md
```

报告必须明确回答：

1. 是否存在通过冻结参数盲测的候选？
2. 是否存在 orbit-weight 层面的真实结构？
3. 结果是否优于随机和简化对照？
4. 是否随 UPO cutoff 稳定？
5. 是否存在额外零点？
6. 是否有自然 quantization？
7. 哪些候选被证明走不通？
8. Gate A–E 分别处于什么状态？
9. 下一阶段最值得投入的唯一三项任务是什么？

---

# 23. 最终执行原则

多账号和 24 小时运行的价值，不在于同时生成更多文字，而在于建立连续循环：

\[
\boxed{
\text{生成候选}
\rightarrow
\text{计算 UPO/Zeta}
\rightarrow
\text{敌对证伪}
\rightarrow
\text{冻结或淘汰}
}
\]

资源增加时，优先增加：

1. 独立复现；
2. 对照实验；
3. proof audit；
4. 方法多样性；
5. 长时间数值计算。

不要优先增加：

- 同一方向的重复参数扫描；
- 未审核的论文数量；
- 自由发挥的写入 Agent；
- 缺乏停止条件的“继续探索”。

项目跑得越快，越需要严格限制 claim、数据类型、时钟、归一化和状态迁移。
