# HP-Dynamics Handoff

## Current status — QG-0001 harmonic magnetic graph-tower prefilter

Current clue: `CLUE-A4-003`.

Candidate ID: `QG-0001` — harmonic magnetic lollipop-theta tower.

- Formal candidate: `true`
- Candidate state: `ANALYTIC_REVIEW` (primitive directed-bond cutoff `<=6`)
- Source commit: `ce0d4424a95a9392c9e8755a4a11b1cfcabc0e77`
- Source lock: `configs/source_locks/QG-0001.yaml`
- Route-A evaluation:
  `evaluations/route_a/QG-0001/20260806T090351Z.yaml`
- Route-A tuple:
  `(A1_WEAK, A2_FAIL, A3_FAIL, A4_UNITARY_OR_SCATTERING_CANDIDATE)`
- Overall Route A: `ROUTE_A_EXPLORATORY`
- Route-B tuple: `(NOT_INVOKED, NOT_INVOKED, NOT_INVOKED, NOT_INVOKED, NOT_INVOKED)`
- Scoped verdict: `GO_WITH_LIMITATIONS`
- Route B: inactive and not authorized

### Source lock

The base graph has three `L--R` edges and one `L--D` pendant with frozen
lengths and `L`-outward magnetic line integrals

\[
(\ell_0,\ell_1,\ell_2,\ell_3)=(1,\sqrt2,\sqrt3,\sqrt5),
\qquad
(\alpha_0,\alpha_1,\alpha_2,\alpha_3)
=\left(0,\frac\pi3,\frac{2\pi}3,0\right).
\]

`L,R` have covariant Kirchhoff conditions of degrees four and three, and `D`
is Dirichlet. Component `n` is the exact `1/n` metric scaling with fixed edge
phases. Raw metric length and positive wavenumber `K=sqrt(lambda)` are the only
clocks. No arithmetic table, fit, scale, offset, unfolding, nonlinear clock,
or determinant regularization is permitted. The determinant convention is
`NOT_OPENED`.

### Route-A result

- `A1_WEAK`: exact signed/oriented primitive counts are `10`, `45`, and `330`
  at topological periods `2`, `4`, and `6`; all trace/repetition identities
  through period six pass exactly.
- `A2_FAIL`: the pendant bounce gives Euler factors tending to `1/2`. For the
  standard directed-bond block,

  \[
  B_n(s)=S\,\operatorname{diag}_b
  \left(e^{-s\ell_b/n+i\alpha_b}\right),
  \qquad \lVert B_n(s)\rVert_1\to8,
  \]

  so the naive product has no finite nonzero value and the direct sum is not
  trace class (`OBR-012`).
- `A3_FAIL`: the natural operator count is

  \[
  N_H(K)=\frac{1+\sqrt2+\sqrt3+\sqrt5}{\pi}K\log K+O(K),
  \]

  but its coefficient is wrong by the multiplicative factor
  `12.764664694883523`, and no characteristic determinant or completed-ξ
  analytic ledger exists.
- `A4_UNITARY_OR_SCATTERING_CANDIDATE`: the component and direct-sum magnetic
  Laplacians are self-adjoint; \(H_n\simeq n^2H_1\), the base gap is positive,
  and the direct sum has compact resolvent. The inherited local geometric
  antiunitary class is excluded.

### Strongest evidence

The target-free `1/n` grammar produces a genuine all-order `K log K`
wavenumber count and compact resolvent, with exact signed primitive/repetition
data and no use of prime or zero tables.

### Strongest failure

Periods accumulate at zero; no arithmetic orbit law or von-Mangoldt weights
appear; the naive Euler product and standard direct-sum Fredholm construction
fail; and the raw counting coefficient is wrong. The separate identity
`zeta_H(z)=zeta(2z)*zeta_H1(z)` is a spectral-zeta identity, not a wavenumber
secular divisor.

### New reusable knowledge

A harmonic graph tower can escape the fixed finite-graph `O(K)` count while
failing determinant existence at the shortest orbit. Counting order,
trace-class eligibility, and divisor type must be kept separate. An abstract
spectral-basis conjugation exists for every self-adjoint compact-resolvent
operator; the proved symmetry statement excludes only the inherited local
geometric class and gives no abstract antiunitary exclusion.

### Updated files

- `configs/source_locks/QG-0001.yaml`
- `experiments/qg_0001_harmonic_magnetic_tower.py`
- `artifacts/qg_0001/route_a_prefilter.json`
- `formal/results/qg_0001_harmonic_magnetic_tower.md`
- `formal/obstructions/harmonic_graph_tower_naive_determinant.md`
- `tests/test_qg_0001_harmonic_magnetic_tower.py`
- `evaluations/route_a/QG-0001/20260806T090351Z.yaml`
- `docs/candidate_registry.md`
- `docs/obstruction_registry.md`
- `docs/research_clues.md`
- `docs/research_log.md`
- `HP_HANDOFF.md`
- `CHANGELOG.md`

`docs/operator_obligations.md` is unchanged because Route B remains closed.

### Tests

- Focused QG-0001 suite: `8/8 passed` (`0.234 s`).
- Full repository suite: `209/209 passed` (`61.312 s`).
- YAML parse, byte-reproduction gate, and `git diff --check`: passed.

### Reproduction commands

```bash
git status --short --branch
git pull --rebase origin main
python3 experiments/qg_0001_harmonic_magnetic_tower.py \
  --quiet \
  --output artifacts/qg_0001/route_a_prefilter.json
python3 -m unittest -v tests/test_qg_0001_harmonic_magnetic_tower.py
python3 -m unittest discover -v
python3 -c 'import yaml; p="evaluations/route_a/QG-0001/20260806T090351Z.yaml"; d=yaml.safe_load(open(p,encoding="utf-8")); print(d["a1"]["verdict"], d["a2"]["verdict"], d["route_b_invocation_allowed"])'
sha256sum artifacts/qg_0001/route_a_prefilter.json \
  experiments/qg_0001_harmonic_magnetic_tower.py \
  configs/source_locks/QG-0001.yaml \
  formal/results/qg_0001_harmonic_magnetic_tower.md \
  formal/obstructions/harmonic_graph_tower_naive_determinant.md \
  tests/test_qg_0001_harmonic_magnetic_tower.py
git diff --check
```

### Claim boundary

Established: the frozen graph tower, exact primitive prefix, inherited local
geometric antiunitary obstruction, self-adjoint compact-resolvent natural
operator, intrinsic `K log K` counting exponent, and `OBR-012`.

Not established: a log-prime orbit law, von-Mangoldt trace weights, a
same-object regularized determinant, the correct coefficient, completed-ξ
divisor, Route B, Hilbert–Pólya, or RH.

### Next smallest task

Derive the entire physical base-component characteristic function at `k=0`,
prove the exact order and removal of every spurious bond-secular zero, and
identify the first nonzero normalized Taylor coefficient. Only after that may
one explicit genus-one relative component product be frozen. Do not borrow
spectral-zeta zeros and do not invoke Route B.

Recommended verdict: `GO_WITH_LIMITATIONS`.

## Previous checkpoint — TH-0001 same-order unitary FIO lift

Current clue: `CLUE-A4-001`.

Candidate ID: `TH-0001` — target-free non-palindromic three-kick Hénon ratchet.

- Formal candidate: `true`
- Candidate state: `ANALYTIC_REVIEW` (UPO prefix complete only through `G`-period `<=2`)
- Source commit: `a4cb10640c44559f0520386d9c84e65c9b873134`
- Source lock: `configs/source_locks/TH-0001-FIO.yaml`
- Route-A evaluation: `evaluations/route_a/TH-0001/20260806T053410Z.yaml`
- Route-A tuple: `(A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`
- Overall Route A: `ROUTE_A_EXPLORATORY`
- Scoped verdict: `GO_WITH_LIMITATIONS`
- Route B: not evaluated, inactive, and not authorized

### A4 object and theorem

With `hbar=1`, Lebesgue `L^2(R,dq)`, and the positive-real normalization,

\[
S_a(q,Q)=qQ-q+\frac a3q^3,
\qquad
U_a=\mathcal F_+M_a,
\qquad
U_G=U_{5/2}U_{3/2}U_{1/2}.
\]

The mixed Hessian is exactly one, so the canonical graph is the frozen kick.
The multiplication phase is modulus one and `F_+` is unitary by Plancherel;
therefore every factor and the ordered product are everywhere-defined unitaries
on `L^2(R)`. The product inverse has the reverse factor order. The triple
kernel is retained as an iterated oscillatory integral; no global absolute
convergence or single-phase reduction is claimed at caustics.

The exact internal phase Hessian is

\[
\begin{pmatrix}3q_1&1\\1&5q_2\end{pmatrix},
\qquad \det=15q_1q_2-1,
\]

and \((q_1,q_2)=(1,1/15)\) is a rational caustic witness. `OBR-011` therefore
blocks a global single reduced phase/Maslov chart, but does not affect the
factorized unitary.

### Antiunitary audit

The natural parent-swap antiunitary is `A=F_+ C`, with `A^2=I` and
`A q A^{-1}=p`, `A p A^{-1}=q`. It reverses each individual kick exactly, but

```text
A U_(5/2) U_(3/2) U_(1/2) A^{-1}
  = U_(5/2)^(-1) U_(3/2)^(-1) U_(1/2)^(-1)
  != U_(1/2)^(-1) U_(3/2)^(-1) U_(5/2)^(-1)
  = U_G^(-1).
```

The reverse word is not a cyclic rotation of the forward word. The exact
classical witness remains
`RGR(0,0)=(-1/2,-5/8) != G^(-1)(0,0)=(-1/2,-1/8)`. This excludes only the
inherited affine/metaplectic clock-reflection class; arbitrary nonlinear or
non-geometric antiunitaries remain `OPEN`.

### Tests and claim boundary

- Focused FIO suite: `12/12 passed`.
- Full repository: `196/196 passed`.
- Focused phase-caustic suite: `5/5 passed`.
- FIO artifact SHA-256: `0eb583e54b69d3372b582a204c871f7b5f446143353cd6831fea3c27a893fc3e`.
- Phase artifact SHA-256: `a5b8ed95b6832ed47b2da7f1a4a00878c9e64bde0b513cc96a39049ef4a17912`.
- FIO generator SHA-256: `9cff63faf27f56e48f89caf1eab45e07e092c61b6c78e3a9b07beb1836c77bfb`.

Established: same-order unitary FIO, exact canonical graph, inherited
antiunitary one-kick identities, and their non-palindromic three-kick failure.

Not established: arbitrary antiunitary exclusion, self-adjoint Hamiltonian,
spectral type, determinant, trace formula, Route B, Hilbert--Pólya, or RH.

Next smallest task: stop the phase sub-audit at `OBR-011`. Reopen only with an
explicit multi-chart phase/Maslov ledger and caustic transition rules; do not
infer it from signed multipliers or compute spectra/determinants.

Recommended verdict: `GO_WITH_LIMITATIONS` for the scoped A4 audit.

## Previous checkpoint — TH-0001 three-kick Hénon Route-A prefilter

Current clue: `CLUE-A4-001`.

Candidate ID: `TH-0001` — target-free non-palindromic three-kick Hénon ratchet.

- Formal candidate: `true`
- Source commit: `fb69649afbda27006d56471c5680b590f90ba43b`
- Source lock: `configs/source_locks/TH-0001.yaml`
- Route-A evaluation: `evaluations/route_a/TH-0001/20260806T024238Z.yaml`
- Route-A tuple: `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`
- Overall Route A: `ROUTE_A_EXPLORATORY`
- Scoped verdict: `GO_WITH_LIMITATIONS`
- Candidate state: `UPO_PASSED` only for the frozen `G`-period `<=2` cutoff
- Route B: not evaluated, inactive, and not authorized

### Source lock

\[
F_a(q,p)=(1-aq^2-p,q),
\qquad
G=F_{5/2}\circ F_{3/2}\circ F_{1/2}.
\]

The phase space is \((\mathbb R^2,dq\wedge dp)\). One application of `G` is
the sole clock; the three micro-kicks are not separate primitive periods. The
half-integer ramp is a target-free modeling choice. The determinant convention
is explicitly `NOT_OPENED`; prime/zero/GUE/USTC data and all legacy fitted
parameters are forbidden.

### Route-A tuple and evidence

- `A1_WEAK`: exact Groebner/Sturm elimination certifies a global real prefix of
  4 primitive period-one and 8 primitive period-two orbits (20 phase points),
  all hyperbolic; no arithmetic orbit law or higher-period completeness.
- `A2_FAIL`: no transfer operator, cycle product, Fredholm determinant, or zero
  ledger is defined.
- `A3_FAIL`: no determinant means no functional equation, completed-xi divisor,
  continuation, or moving-order count can be tested.
- `A4_FORMAL_HINT`: exact generating functions give a same-order
  Fourier-integral quantization hint; a Hilbert space, domain, unitary theorem,
  and complete antiunitary audit are not yet frozen.

The inherited swap reversor fails at an exact origin witness, and all affine
anti-symplectic involutions are excluded. `OBR-010` records the reusable
low-depth obstruction; arbitrary nonlinear/non-polynomial reversors remain
open, so no absolute time-reversal-breaking claim is made.

### Tests and reproducibility

- Focused suite: `10/10 passed`.
- Full repository: `184/184 passed`.
- Artifact SHA-256: `f50e806512b45a49223dd1ee7fac2689858949a7172a02e73e82d1a03a5e104a`.
- Generator SHA-256: `f3da9e8d1ce5690a0ae96350c0392c53bf7e42cf6bb71fc108dddbbc056745a4`.

```bash
python3 experiments/th_0001_three_kick_henon.py --quiet \
  --output artifacts/th_0001/route_a_prefilter.json
python3 -m unittest -v tests/test_th_0001_three_kick_henon.py
python3 -m unittest discover -v
git diff --check
```

### Claim boundary and next smallest task

Established: one explicit autonomous exact-symplectic target-free map, the
frozen clock/normalization, low-depth reversibility obstruction, and complete
signed real primitive-orbit data through `G`-period two.

Not established: arbitrary nonlinear reversor exclusion, arithmetic orbit law,
any determinant or global analytic structure, quantum operator/domain,
Route B, Hilbert--Pólya, or RH.

Next smallest task: freeze same-order Fourier-integral quantization
`U=U_(5/2)U_(3/2)U_(1/2)` on `L^2(R)`, prove normalization and unitarity, and
audit natural antiunitary symmetry. Do not compute spectra, fit zeros, define a
determinant, or invoke Route B.

Recommended verdict: `GO_WITH_LIMITATIONS` for the scoped prefilter.

## Previous checkpoint — frozen-radius exact-$U_c$ polar complex branches

Current clue: `CLUE-A1-004`

Candidate ID: no new formal candidate. Scoped audit:
`P4-LOGISTIC-UC-POLAR-COMPLEX-BRANCH`, following
`P4-LOGISTIC-UC-POLAR-NONLATTICE` under parent candidate
`P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK`.

- Formal candidate: `false`
- Implementation source commit: `3ae5e23508e27129cfa5910473b944026b904ea3`
- Source lock:
  `configs/source_locks/P4-LOGISTIC-UC-POLAR-COMPLEX-BRANCH.yaml`
- Route-A evaluation:
  `evaluations/route_a/P4-LOGISTIC-UC-POLAR-COMPLEX-BRANCH/20260805T125236Z.yaml`
- Route-A tuple: `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`
- Overall Route A: `ROUTE_A_EXPLORATORY`
- Scoped verdict: `GO_WITH_LIMITATIONS`
- Parent verdict: `REVISE`
- Route-B tuple: not evaluated; Route B is inactive and not authorized

### Source lock and theorem

The radius is unchanged:

\[
\epsilon=\frac1{1000}.
\]

The two branch stadiums have one convex union $U$. On that single domain the
audit constructs

\[
t(z)=\sqrt{\frac{1+\rho\sin z}{U_c}},
\qquad
a(z)=\frac{\sqrt{1+t(z)}\sqrt{\rho+t(z)}}{4t(z)},
\]

using separate right-half-plane principal roots, and the common logarithm

\[
\ell(z)=-\log4+\frac12\Log(1+t(z))
+\frac12\Log(\rho+t(z))-\Log t(z).
\]

The composite branches are primitives of this same $a$,

\[
\phi_L(z)=\int_{\pi/2}^{z}a(w)\,dw,
\qquad
\phi_R(z)=-\int_{\pi/2}^{z}a(w)\,dw,
\]

so the signed derivatives remain

\[
\phi_L'=+a,
\qquad
\phi_R'=-a.
\]

They obey the locked coordinate identity

\[
S(\rho\sin\phi_\sigma(z))=\rho\sin z.
\]

No independent holomorphic forward $G$ is asserted on the noninjective
endpoint caps of $q=\rho\sin$.

The exact analytic inequalities and 100-digit Arb margins give

\[
\begin{aligned}
\operatorname{Re}\frac{1+\rho\sin z}{U_c}&>0.29559,\\
|t(z)-t(x)|&<0.000324,\\
|\ell(z)-\ell(x)|&<0.000851,\\
\sup_{\overline U}|a|&<0.59626<1.
\end{aligned}
\]

The logarithm bound gives $\operatorname{Re}a>0$, hence both primitive-defined
branches are globally univalent on the convex stadium. For every target
component $j$ and source branch $\sigma$,

\[
\phi_\sigma(\overline{U_j})
\subset\{w:\operatorname{dist}(w,I_\sigma)<0.00059626\}
\Subset U_\sigma,
\]

with compact margin greater than `0.00040374`.

### Strongest evidence

The proof covers the full frozen complex domains and all four `LL`, `LR`,
`RL`, and `RR` pairs without a complex grid. It combines exact $U_c$
identities, one common right-half-plane functional calculus, a primitive
construction that removes the endpoint scalar branch points, a global
univalence lemma, and outward Arb scalar margins. The saved certificate is
byte reproducible and an independent adversarial review found no blocking
mathematical issue.

### Strongest failure

The target copy and multiplicity for every orbit that hits the doubled
partition point are still undefined. Therefore no trace ledger is frozen.
Nuclearity, a Fredholm determinant, an exact orbit trace formula, root counts,
target divisor, global completed-$\xi$ structure, and quantization remain
absent. A2 therefore remains failed.

### New reusable knowledge

For a polar map with endpoint cancellations, the safest complex continuation
is to construct the common inverse derivative and its logarithm first, then
recover both branches as primitives. A strict complex contraction gives all
four compact inclusions at once, while a small common-log variation bound
upgrades local continuation to global univalence. This avoids incompatible
endpoint `sqrt/asin` germs and preserves signed orientation.

Portfolio rule: this candidate has accumulated a clean reusable theorem edge
without changing `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`. Preserve its local
trace-ledger continuation, but give the project-level slot to a structurally
different candidate rather than extending the Logistic proof chain by
default.

### Updated files

- `CHANGELOG.md`
- `DERIVATION_PACKAGE.md`
- `HP_HANDOFF.md`
- `artifacts/p4_logistic_uc_polar_complex_branch/complex_branch_certificate.json`
- `configs/source_locks/P4-LOGISTIC-UC-POLAR-COMPLEX-BRANCH.yaml`
- `docs/candidate_registry.md`
- `docs/main_agent_rules.md`
- `docs/obstruction_registry.md`
- `docs/research_clues.md`
- `docs/research_log.md`
- `evaluations/route_a/P4-LOGISTIC-UC-POLAR-COMPLEX-BRANCH/20260805T125236Z.yaml`
- `experiments/p4_logistic_uc_polar_complex_branch.py`
- `formal/results/exact_uc_polar_complex_branch.md`
- `tests/test_p4_logistic_uc_polar_complex_branch.py`

`docs/operator_obligations.md` is unchanged because Route B remains closed.

### Tests and reproduction

Focused complex-branch audit: `13/13 passed`.

Full repository: `174/174 passed`.

```bash
python3 experiments/p4_logistic_uc_polar_complex_branch.py \
  --quiet \
  --output artifacts/p4_logistic_uc_polar_complex_branch/complex_branch_certificate.json
python3 -m unittest -v tests/test_p4_logistic_uc_polar_complex_branch.py
python3 -m unittest discover -v
python3 -c 'import yaml; p="evaluations/route_a/P4-LOGISTIC-UC-POLAR-COMPLEX-BRANCH/20260805T125236Z.yaml"; d=yaml.safe_load(open(p,encoding="utf-8")); print(d["a1"]["verdict"], d["a2"]["verdict"], d["route_b_invocation_allowed"])'
sha256sum artifacts/p4_logistic_uc_polar_complex_branch/complex_branch_certificate.json experiments/p4_logistic_uc_polar_complex_branch.py
git diff --check
```

Artifact and generator SHA-256:

```text
8ab64528f5bfe2e84dc24b42ee6bd3bb93e07d668e849a6614eda9f01c495404  artifacts/p4_logistic_uc_polar_complex_branch/complex_branch_certificate.json
307cd1184f4ddd26489b3a1daed28fa7307b7de159329fbd4fb24a27b381694f  experiments/p4_logistic_uc_polar_complex_branch.py
```

### Claim boundary and next smallest task

Established: one common holomorphic $t$, $a$, and $\Log(a)$ on the frozen
radius-`1/1000` domain; two globally univalent signed composite inverse
branches; all four compact inclusions; and well-defined matching-space
weighted composition for each fixed $s$.

Not established: partition-hit trace multiplicity, nuclearity, a Fredholm
determinant, arithmetic orbit weights, completed-$\xi$ structure,
quantization, Route B, Hilbert--Polya, or RH.

Candidate-local resume task: freeze only the doubled-partition target-copy
and multiplicity rule for partition-hit traces on the matching space.

Project-level next smallest task: apply the RH breadth-first rule and park the
Logistic branch at this stable checkpoint. Open `CLUE-A4-001` and freeze
exactly one explicit target-free Twisted Hénon / kicked-symplectic object from
the legacy Hénon parent. Its first Route-A prefilter is limited to autonomous
map definition, symplecticity, antiunitary/time-reversal audit, and
reproducible short primitive UPOs. Do not fit zeros or define a determinant in
that first task.

Recommended verdict: `REVISE` (`GO_WITH_LIMITATIONS` for this scoped theorem).

## Previous checkpoint — exact-$U_c$ polar non-lattice theorem

Current clue: `CLUE-A1-004`

Candidate ID: no new formal candidate. Scoped audit:
`P4-LOGISTIC-UC-POLAR-NONLATTICE`, following the corrected
`P4-LOGISTIC-UC-POLAR-INTRINSIC-ROOF` lock under parent candidate
`P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK`.

- Formal candidate: `false`
- Implementation source commit: `36a38f0db16652bf0e0c1459be6c69f6bdafec12`
- Route-A evaluation:
  `evaluations/route_a/P4-LOGISTIC-UC-POLAR-NONLATTICE/20260805T110654Z.yaml`
- Route-A tuple: `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`
- Overall Route A: `ROUTE_A_EXPLORATORY`
- Scoped verdict: `GO_WITH_LIMITATIONS`
- Parent verdict: `REVISE`
- Route-B tuple: not evaluated; Route B is inactive and not authorized

### Source lock and theorem

The source lock keeps exactly the intrinsic roof

\[
\tau(\theta)=\log|G'(\theta)|
\]

and the sealed primitive words `R` and `LR`. Their signed multipliers are
recorded first,

\[
\Lambda_R=-\alpha<0,
\qquad
\Lambda_{LR}=-\beta<0,
\]

and their full primitive roof periods are

\[
T_R=\log\alpha,
\qquad
T_{LR}=\log\beta.
\]

The period of `LR` is not divided by its symbolic length two. Exact reduction
gives

\[
\alpha=4(U_c-1),
\qquad
\alpha^3+4\alpha^2+16\alpha-64=0,
\]

and an irreducible degree-nine polynomial for $\beta$. Their norms are

\[
N(\alpha)=2^6,
\qquad
N(\beta)=2^{36}.
\]

If $T_{LR}/T_R=a/b\in\mathbb Q$ in lowest terms, common-field norms force
$a=2b$, hence the sole possible relation is $\beta=\alpha^2$. The exact
identity

\[
H_{U_c}(\alpha^2)
=-8192(U_c-2)(2U_c-3)\ne0
\]

for $3/2<U_c<2$ excludes it. Therefore

\[
\boxed{T_{LR}/T_R\notin\mathbb Q},
\]

so the intrinsic polar roof is non-lattice.

### Strongest evidence

The proof is exact rather than a finite-precision irrationality test. It uses
an exact fixed-point factorization, the exact degree-12 period-two dynatomic
quotient, a multiplier identity in
$\mathbb Q[U_c,X]/(P(U_c),D_2(X))$, mod-3 and mod-5 irreducibility
certificates, algebraic norms, and the final exact nonvanishing identity.
Twenty exact algebra gates pass. Decimal orbit coordinates are retained only
as target-free diagnostics and carry no proof weight.

### Strongest failure

Non-lattice behavior removes the old unit-clock vertical-periodicity
obstruction for this roof, but it does not establish the frozen
`epsilon=1/1000` complex branch continuations, common `Log(a)` germ, compact
branch inclusion, matching-space invariance, partition-hit trace rule,
nuclearity, or a Fredholm determinant. There is still no arithmetic
prime-orbit law, target divisor, global analytic structure, or quantization.
A2 therefore remains failed.

### New reusable knowledge

For a full-branch expanding roof, two intrinsic primitive periods suffice to
prove non-lattice when their multiplier magnitudes are proved
multiplicatively independent. Algebraic norms can collapse all possible
logarithmic rational relations to a finite exact case, avoiding any bounded
denominator or decimal-ratio argument. `OBR-008` remains valid for the old unit
clock but no longer applies to this non-lattice roof by its stated scope.

### Updated files

- `CHANGELOG.md`
- `DERIVATION_PACKAGE.md`
- `HP_HANDOFF.md`
- `configs/source_locks/P4-LOGISTIC-UC-POLAR-NONLATTICE.yaml`
- `docs/candidate_registry.md`
- `docs/obstruction_registry.md`
- `docs/research_clues.md`
- `docs/research_log.md`
- `evaluations/route_a/P4-LOGISTIC-UC-POLAR-NONLATTICE/20260805T110654Z.yaml`
- `experiments/p4_logistic_uc_polar_nonlattice.py`
- `formal/results/exact_uc_polar_nonlattice.md`
- `artifacts/p4_logistic_uc_polar_nonlattice/nonlattice_certificate.json`
- `tests/test_p4_logistic_uc_polar_nonlattice.py`

`docs/operator_obligations.md` is unchanged because Route B remains closed.

### Tests and reproduction

Focused non-lattice audit: `13/13 passed`.

Full repository: `161/161 passed`.

```bash
python3 experiments/p4_logistic_uc_polar_nonlattice.py \
  --quiet \
  --output artifacts/p4_logistic_uc_polar_nonlattice/nonlattice_certificate.json
python3 -m unittest -v tests/test_p4_logistic_uc_polar_nonlattice.py
python3 -m unittest discover -v
python3 -c 'import yaml; p="evaluations/route_a/P4-LOGISTIC-UC-POLAR-NONLATTICE/20260805T110654Z.yaml"; d=yaml.safe_load(open(p,encoding="utf-8")); print(d["a1"]["evidence_status"], d["a2"]["verdict"], d["route_b_invocation_allowed"])'
sha256sum artifacts/p4_logistic_uc_polar_nonlattice/nonlattice_certificate.json experiments/p4_logistic_uc_polar_nonlattice.py
git diff --check
```

### Claim boundary and next smallest task

Established: the exact signed `R` and `LR` multipliers, their irreducible
minimal polynomials and norms, multiplicative independence, irrational full
primitive-period ratio, and the non-lattice intrinsic roof.

Not established: an arithmetic orbit law, the frozen-radius complex operator
domain, endpoint trace multiplicity, nuclearity, a Fredholm determinant,
completed-$\xi$ structure, quantization, Route B, Hilbert--Polya, or RH.

Next smallest task: audit only the frozen `epsilon=1/1000` composite complex
inverse branches, common `Log(a)` germ, and compact branch inclusion. Do not
audit nuclearity, Fredholm zeros, or target divisors in that task.

Recommended verdict: `REVISE` (`GO_WITH_LIMITATIONS` for this scoped theorem).

## Previous checkpoint — exact-$U_c$ polar intrinsic-roof source lock

Current clue: `CLUE-A1-004`

Candidate ID: no new formal candidate. Lock-only audit ID:
`P4-LOGISTIC-UC-POLAR-INTRINSIC-ROOF`, following
`P4-LOGISTIC-UC-BRANCH-MASS-RATE` under parent candidate
`P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK`.

- Formal candidate: `false`
- Source commit: `4d5cd7e346445317d2ed19ef90a484cca09c3588`
- Source lock:
  `configs/source_locks/P4-LOGISTIC-UC-POLAR-INTRINSIC-ROOF.yaml`
- Route-A tuple: inherited `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`; no new
  Route-A evaluation has been performed
- Checkpoint status: `DEFINED_NOT_EVALUATED`
- Route-B tuple: not evaluated; Route B is inactive and not authorized

### Source lock

The frozen base is the two-full-branch polar Markov map

\[
S=-f^2|_{[-\rho,\rho]},
\qquad
q(\theta)=\rho\sin\theta,
\qquad
G=q^{-1}\circ S\circ q,
\]

on the doubled branch space
$I_L\sqcup I_R=[-\pi/2,0_L]\sqcup[0_R,\pi/2]$. Its intrinsic roof is

\[
\tau(\theta)=\log|G'(\theta)|>0,
\qquad
T_\gamma=\sum_{k=0}^{n-1}\tau(G^k\theta)
=\log|(G^n)'(\theta)|.
\]

One base step represents exactly two iterates of the original Logistic map,
whereas the suspension/determinant clock is the positive roof time. These two
clocks are frozen separately and may not be substituted for one another.

The complex lock fixes `epsilon=1/1000`, two stadium neighborhoods, the
matching branchwise analytic Banach space

```text
B_epsilon = {(v_L,v_R): v_sigma analytic on U_sigma,
             continuous on closure(U_sigma), v_L(0)=v_R(0)}
```

and the conditional weighted family

\[
(\mathcal L_s v)_j(z)
=a(z)^s\bigl[v_L(\phi_L(z))+v_R(\phi_R(z))\bigr].
\]

The sole intended determinant notation is
$D_{\rm pol}(s)=\det_{\rm Fr}(I-\mathcal L_s)$, but only if a later audit
proves the frozen operator nuclear. It is not an established determinant at
this checkpoint.

### Strongest evidence

The exact branch formulas, orientations, endpoint extensions, and expansion
theorem give

```text
phi_L' = +a
phi_R' = -a
inf |G'| = 4/U_c^2 > 1
inf tau = log(4/U_c^2) > 0
tau(0_L)=tau(0_R)=(1/2) log(8/U_c)
```

Thirteen executable lock gates verify the real inverse identities and signed
derivatives, the exact reflected physical conjugacy, outward endpoint
positivity bounds, doubled-versus-quotient ledger separation, frozen complex
obligations, the one-way lattice logic, data firewall, and route status. No
prime, zero, zeta, xi, USTC, or fitted data enters.

### Strongest failure

The composite complex branches and holomorphic `Log(a)` have not yet been
certified on the `1/1000` neighborhoods. Compact branch inclusion, invariance
of the analytic space, nuclearity, the partition-hit endpoint trace rule, and
Fredholm determinant existence are all open. The roof has not yet passed a
non-lattice theorem. Therefore A2 remains failed and no divisor, zero, or
quantization claim is available.

### New reusable knowledge

The natural determinant data type for this polar object requires three
separations: doubled Markov coding versus quotient interval, signed branch
orientation versus positive roof magnitude, and two-iterate physical time
versus intrinsic log-Jacobian suspension time. The notation
`det_Fr(I-L_s)` must remain conditional until the same frozen complex-space
operator is proved nuclear.

### Updated files

- `CHANGELOG.md`
- `DERIVATION_PACKAGE.md`
- `HP_HANDOFF.md`
- `configs/source_locks/P4-LOGISTIC-UC-POLAR-INTRINSIC-ROOF.yaml`
- `docs/candidate_registry.md`
- `docs/research_clues.md`
- `docs/research_log.md`
- `tests/test_p4_logistic_uc_polar_intrinsic_roof_lock.py`

`docs/obstruction_registry.md` is unchanged because no new obstruction is
proved. `docs/operator_obligations.md` is unchanged because Route B remains
closed.

### Tests and reproduction

Focused lock audit: `13/13 passed`.

Full repository: `148/148 passed`.

```bash
python3 -m unittest -v tests/test_p4_logistic_uc_polar_intrinsic_roof_lock.py
python3 -m unittest discover -v
python3 -c 'import yaml; p="configs/source_locks/P4-LOGISTIC-UC-POLAR-INTRINSIC-ROOF.yaml"; d=yaml.safe_load(open(p,encoding="utf-8")); print(d["audit_id"], d["route_status_at_lock"]["checkpoint_status"], d["route_status_at_lock"]["recommended_verdict"])'
git diff --check
```

### Claim boundary and next smallest task

Established: one explicit target-free real polar Markov suspension object,
doubled branch convention, intrinsic positive roof, separated clocks, exact
interior inverse formulas, frozen intended analytic space and conditional
transfer family, sole determinant convention, data split, and stopping rules.

Not established: non-lattice behavior, complex-domain branch inclusion,
nuclearity, an actual Fredholm determinant, arithmetic primitive-orbit law,
global analytic structure, quantization, Route B, Hilbert--Polya, or RH.

Next smallest task: audit only whether the sealed primitive words `R` and
`LR` have multiplicatively independent positive multipliers and therefore
prove the roof non-lattice. Failure to close that proof returns `REVISE` or
`NOT_TESTABLE`; it does not prove lattice behavior. Do not audit Fredholm
nuclearity or compare target zeros in that task.

Recommended verdict: `REVISE`; checkpoint status `DEFINED_NOT_EVALUATED`.

## Previous checkpoint — quantitative exact-$U_c$ branch-mass-ratio rate

Current clue: `CLUE-A1-004`

Candidate ID: no new formal candidate. Scoped audit:
`P4-LOGISTIC-UC-BRANCH-MASS-RATE`, strengthening parent audit
`P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE` and parent candidate
`P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK`.

- Formal candidate: `false`
- Implementation source commit: `dbcb58d21ff93ef842df869c177a3ec3e8c0a785`
- Route-A evaluation:
  `evaluations/route_a/P4-LOGISTIC-UC-BRANCH-MASS-RATE/20260805T083731Z.yaml`
- Supersedes the preserved `20260805T035348Z` evaluation only for provenance
  clarity; the theorem and Route-A tuple are unchanged.
- Route-A tuple: `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`
- Overall Route A: `ROUTE_A_EXPLORATORY`
- Scoped verdict: `GO_WITH_LIMITATIONS`
- Parent verdict: `REVISE`
- Route-B tuple: not evaluated; Route B is inactive and not authorized

### Source lock

`configs/source_locks/P4-LOGISTIC-UC-BRANCH-MASS-RATE.yaml` fixes the exact
$U_c$ Logistic map, physical branch endpoints and masses, the cusp space

\[
\mathcal X_{1/200}
=\{c\,t^{-1/2}+b(t):b\in L^\infty(0,1/200]\},
\qquad
\|v\|=|c|+\|b\|_\infty,
\]

one physical iterate per clock tick, full-acip normalization, absent
determinant convention, all branch indices $n\geq6$, 100-digit Arb precision,
allowed and forbidden data, train/validation/test boundaries, and stopping
conditions. Adjacent masses retain the same physical coefficient $C_h$;
independent marginal coefficient intervals may not be divided.

### Strongest evidence

The new computer-assisted gate is one directed Arb interval evaluation on the
complete local domain, proving

```text
7/20 < psi' < 9/25
0 < psi'' < 4/25
```

The root bracket, sharp coefficient lower bound, cusp remainder, and sealed
`delta_5` endpoint interval are inherited certified inputs from the parent
audits. Together with the exact Fraction ledger, they give, for every
$n\geq6$,

\[
\boxed{
\left|
\frac{\mu(C_{2n+2})}{\mu(C_{2n})}-\frac{U_c^2}{4}
\right|
\leq\frac{36}{5}\sqrt{\delta_{n-1}}
<\frac{243}{625}\left(\frac35\right)^{n-6}.
}
\]

This is an all-tail, target-free measure-theoretic theorem edge. It is not a
fixed-order extrapolation and does not use prime, zero, zeta, xi, or USTC data.

### Strongest failure

Physical first-return branch masses are observables, not primitive periodic
orbits. The rate supplies no arithmetic multiplicity, phase, repetition, or
von-Mangoldt law. No $s$-dependent transfer operator, Fredholm determinant,
completed-$\xi$ structure, or natural quantization is defined. `OBR-008` and
`OBR-009` remain active, and the legacy ordinary-`BV` spectral proof remains
refuted.

### New reusable knowledge

For adjacent cusp masses, cancellation of the common leading coefficient must
be carried out in one joint ledger. Dividing independent marginal mass
intervals permits incompatible values of $C_h$ and loses the rate. A frozen
cusp decomposition plus a complete derivative interval and exact endpoint
contraction can yield an all-tail ratio theorem without a spectral-gap claim.

### Updated files

- `CHANGELOG.md`
- `DERIVATION_PACKAGE.md`
- `HP_HANDOFF.md`
- `configs/source_locks/P4-LOGISTIC-UC-BRANCH-MASS-RATE.yaml`
- `docs/candidate_registry.md`
- `docs/obstruction_registry.md`
- `docs/prior_work/README.md`
- `docs/prior_work/claims_matrix.md`
- `docs/research_clues.md`
- `docs/research_log.md`
- `evaluations/route_a/P4-LOGISTIC-UC-BRANCH-MASS-RATE/20260805T083731Z.yaml`
- `experiments/p4_logistic_uc_branch_mass_rate.py`
- `formal/results/exact_uc_branch_mass_rate.md`
- `tests/test_p4_logistic_uc_branch_mass_rate.py`
- `artifacts/p4_logistic_uc_branch_mass_rate/rate_certificate.json`

`docs/operator_obligations.md` is unchanged because Route B remains closed.

### Tests and reproduction

Focused rate audit: `12/12 passed`.

Full repository: `135/135 passed`.

```bash
python3 experiments/p4_logistic_uc_branch_mass_rate.py \
  --quiet \
  --output artifacts/p4_logistic_uc_branch_mass_rate/rate_certificate.json
python3 -m unittest -v tests/test_p4_logistic_uc_branch_mass_rate.py
python3 -m unittest discover -v
python3 -c 'import flint; print(flint.__version__, flint.__FLINT_VERSION__)'
python3 -c 'import yaml; paths=["configs/source_locks/P4-LOGISTIC-UC-BRANCH-MASS-RATE.yaml","evaluations/route_a/P4-LOGISTIC-UC-BRANCH-MASS-RATE/20260805T035348Z.yaml","evaluations/route_a/P4-LOGISTIC-UC-BRANCH-MASS-RATE/20260805T083731Z.yaml"]; [yaml.safe_load(open(p,encoding="utf-8")) for p in paths]'
sha256sum artifacts/p4_logistic_uc_branch_mass_rate/rate_certificate.json experiments/p4_logistic_uc_branch_mass_rate.py
git diff --check
```

Artifact and generator SHA-256:

```text
a6baa8ae9603bd4cebe3a26a85ce537c020282b9a2ae0902e26d37c7e15cc9ae  artifacts/p4_logistic_uc_branch_mass_rate/rate_certificate.json
fd5ea988a5156b2ea9cb3798ba01d58bc328b8d99dda40856581a5b8378eab57  experiments/p4_logistic_uc_branch_mass_rate.py
```

### Claim boundary and next smallest task

Established: the frozen cusp-adapted space, a complete local derivative
certificate, the shared-coefficient mass ledger, and the displayed explicit
adjacent-ratio rate for every physical branch $n\geq6$.

Not established: an exact finite-order mass law, ordinary-`BV` spectral gap,
arithmetic primitive-orbit law, determinant, global analytic structure,
quantization, Route B, Hilbert--Polya, or RH.

Next smallest task: freeze the existing polar suspension object only: the map
$G$, its two branches, intrinsic positive roof $\tau=\log|G'|$, physical
clock relation, analytic function space, determinant convention, data split,
and stopping conditions. Do not audit non-lattice behavior or Fredholm
existence until that source lock is complete.

Recommended verdict: `REVISE` (`GO_WITH_LIMITATIONS` for this scoped audit).

## Previous checkpoint — validated sharp exact-$U_c$ polar cone

Current clue: `CLUE-A1-004`

Candidate ID: no new formal candidate. Scoped audit:
`P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE`, strengthening parent candidate
`P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK`.

- Formal candidate: `false`
- Implementation source commit: `f34117824702404fe0837f5811a5465d33cc65de`
- Route-A evaluation:
  `evaluations/route_a/P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE/20260805T012200Z.yaml`
- Route-A tuple: `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`
- Scoped verdict: `GO_WITH_LIMITATIONS`
- Parent verdict: `REVISE`
- Route-B tuple: not evaluated; Route B is inactive and not authorized

### Source lock

`configs/source_locks/P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE.yaml` fixes the
exact distortion formula, the 100-digit $U_c$ bracket, `python-flint 0.9.0`,
FLINT `3.6.0`, 100 decimal digits, a $2^{18}$ closed cover of `t in [0,1]`,
the lower-witness interval, cone slope, normalizations, finite returns, allowed
data, and stopping conditions.

### Strongest evidence

An Arb directed interval cover proves

```text
0.17013 < D=sup|d_eta log(a)| < 0.17014
kappa=U_c^2/4 < 0.595744
A=42535/101064
0.17014 + 0.595744*A = A
```

The resulting target-free safe enclosures are

```text
w(0)   in [0.22460, 0.43504]
g_A(0) in [0.41310, 0.80016]
h(0)   in [0.20655, 0.40008]
C_h    in [0.09461, 0.18327]
```

Using the inherited explicit endpoint remainder, the physical mass intervals
are tightened to

```text
C_12: [0.0029623667412445, 0.0090289530684826]
C_14: [0.0020334760261950, 0.0051059183301683]
C_16: [0.0013068364718538, 0.0029454892619841]
C_18: [0.0008124254452971, 0.0017206760060806]
```

### Strongest failure and reusable knowledge

The interval is still broad and no exponential finite-order remainder is
proved. The computation certifies an analytic cone constant; it is not a
finite-rank resolvent theorem and does not create an arithmetic primitive-orbit
law or determinant. `OBR-008` and `OBR-009` remain active.

Reusable knowledge: a full directed interval cover can sharpen the analytic
cone without introducing an operator truncation. Closed cells cover every
between-grid point; interval dependency only widens the result. Finite-mass
certification must also seal endpoint-radius, interval-order, and physical-label
gates.

### Updated files

- `CHANGELOG.md`
- `DERIVATION_PACKAGE.md`
- `HP_HANDOFF.md`
- `configs/source_locks/P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE.yaml`
- `docs/candidate_registry.md`
- `docs/obstruction_registry.md`
- `docs/prior_work/README.md`
- `docs/prior_work/claims_matrix.md`
- `docs/research_clues.md`
- `docs/research_log.md`
- `evaluations/route_a/P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE/20260805T012200Z.yaml`
- `experiments/p4_logistic_uc_acip_sharp_cone_enclosure.py`
- `formal/results/exact_uc_acip_sharp_cone_enclosure.md`
- `tests/test_p4_logistic_uc_acip_sharp_cone_enclosure.py`
- `artifacts/p4_logistic_uc_acip_sharp_cone_enclosure/interval_certificate.json`

`docs/operator_obligations.md` is unchanged because Route B remains closed.

### Tests and reproduction

Focused sharp-cone audit: `12/12 passed`.

Full repository: `123/123 passed`.

```bash
python3 experiments/p4_logistic_uc_acip_sharp_cone_enclosure.py \
  --quiet \
  --output artifacts/p4_logistic_uc_acip_sharp_cone_enclosure/interval_certificate.json
python3 -m unittest -v tests/test_p4_logistic_uc_acip_sharp_cone_enclosure.py
python3 -m unittest discover -v
python3 -c 'import flint; print(flint.__version__, flint.__FLINT_VERSION__)'
python3 -c 'import yaml; paths=["configs/source_locks/P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE.yaml","evaluations/route_a/P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE/20260805T012200Z.yaml"]; [yaml.safe_load(open(p,encoding="utf-8")) for p in paths]'
sha256sum artifacts/p4_logistic_uc_acip_sharp_cone_enclosure/interval_certificate.json
git diff --check
```

Artifact SHA-256:

```text
dec8f8c1a6a7dc329d3338fc835ac34e538c0555283d2cc968c09c31e5e5e231  artifacts/p4_logistic_uc_acip_sharp_cone_enclosure/interval_certificate.json
```

### Claim boundary and next smallest task

Established: the full-domain distortion certificate, sharper safe density and
endpoint-coefficient intervals, and four tighter physical branch masses.

Not established: a closed form, narrow high-accuracy or resolvent enclosure,
quantitative or exponential finite-order remainder, arithmetic orbit law,
determinant, analytic completion, quantization, Route B, Hilbert--Pólya, or RH.

Next smallest task: derive a quantitative convergence rate for the physical
branch-mass ratio in an explicitly frozen analytic or cusp-adapted norm. Do not
compare zeros or define a determinant before that theorem exists.

Recommended verdict: `REVISE`.

## Previous checkpoint — exact-$U_c$ polar-cone density enclosure

Current clue: `CLUE-A1-004`

Candidate ID: none. Parent and scoped audit IDs:

```text
P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK
P4-LOGISTIC-UC-ACIP-ENDPOINT-DENSITY
P4-LOGISTIC-UC-ACIP-CONE-ENCLOSURE
```

- Formal candidate: `false`
- Source commit: `8f270de6546928385b93e1dd0b8b78c7ffd40ea8`
- Route-A evaluation:
  `evaluations/route_a/P4-LOGISTIC-UC-ACIP-CONE-ENCLOSURE/20260804T233200Z.yaml`
- Route-A tuple: `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`
- Scoped cone verdict: `GO_WITH_LIMITATIONS`
- Parent-candidate verdict: `REVISE`
- Route B: inactive and not authorized
- Formal candidate count: unchanged (`SS-0001`, `SS-0002` only)

### Source lock

`configs/source_locks/P4-LOGISTIC-UC-ACIP-CONE-ENCLOSURE.yaml` fixes the exact
`U_c` Logistic map, the polar proof coordinate, the physical clock, the three
density normalizations, the `61/100` local endpoint remainder, branches
`C_12,C_14,C_16,C_18`, the 100-digit root and pi brackets, and the forbidden
data. The pi bracket is independently checked by exact rational Machin-series
intervals.

### Strongest evidence

The inverse-branch transfer operator preserves a positive log-Lipschitz cone
with slope `3/4`: the exact contraction is below `3/5`, the logarithmic weight
distortion is below `3/10`, and
`3/10+(3/5)(3/4)=3/4`. Normalization then gives the coarse target-free bounds

```text
w(0) in [0.1668010108790061, 0.5418010108790062]
h(0) in [0.1533974450330445, 0.4982637116356998]
C_h in [0.0702656899853137, 0.2282361579437251]
```

The explicit endpoint estimate
`|h(-rho+t)-C_h*t^(-1/2)| <= 61/100` for `0<t<=1/200` gives certified
positive absolute masses for physical returns `12,14,16,18`.

### Strongest failure

The enclosure is intentionally coarse. It is not a sharp Ulam or finite-rank
resolvent certificate and does not prove the legacy exponential remainder.
There is still no arithmetic primitive-orbit law, non-lattice clock,
s-dependent Fredholm determinant, global completed-xi structure, or natural
quantization. `OBR-009` and `OBR-008` remain active.

### New reusable knowledge

A validated log-Lipschitz cone can replace a finite-rank spectral-tail argument
for absolute local density and finite branch-mass bounds. This supplies a
target-free numerical theorem edge while preserving the physical clock and
the distinction between `w`, `g_A`, and `h`.

### Updated files

- `CHANGELOG.md`
- `DERIVATION_PACKAGE.md`
- `configs/source_locks/P4-LOGISTIC-UC-ACIP-CONE-ENCLOSURE.yaml`
- `docs/candidate_registry.md`
- `docs/obstruction_registry.md`
- `docs/prior_work/README.md`
- `docs/prior_work/claims_matrix.md`
- `docs/research_clues.md`
- `docs/research_log.md`
- `formal/results/exact_uc_acip_cone_enclosure.md`
- `experiments/p4_logistic_uc_acip_cone_enclosure.py`
- `tests/test_p4_logistic_uc_acip_cone_enclosure.py`
- `artifacts/p4_logistic_uc_acip_cone_enclosure/certified_bounds.json`
- `evaluations/route_a/P4-LOGISTIC-UC-ACIP-CONE-ENCLOSURE/20260804T233200Z.yaml`

### Tests and reproduction

Focused cone audit: `12/12 passed`.

Full repository: `111/111 passed`.

Artifact SHA-256:

```text
c0933c7a9df45f38fb403541aab7643e4e1f771bf7c277e4d144b80cb63f635d  artifacts/p4_logistic_uc_acip_cone_enclosure/certified_bounds.json
```

```bash
python3 experiments/p4_logistic_uc_acip_cone_enclosure.py \
  --quiet \
  --output artifacts/p4_logistic_uc_acip_cone_enclosure/certified_bounds.json
python3 -m unittest -v tests/test_p4_logistic_uc_acip_cone_enclosure.py
python3 -m unittest discover -v
python3 -c 'import yaml; paths=["configs/source_locks/P4-LOGISTIC-UC-ACIP-CONE-ENCLOSURE.yaml","evaluations/route_a/P4-LOGISTIC-UC-ACIP-CONE-ENCLOSURE/20260804T233200Z.yaml"]; [yaml.safe_load(open(p,encoding="utf-8")) for p in paths]'
sha256sum artifacts/p4_logistic_uc_acip_cone_enclosure/certified_bounds.json
git diff --check
```

### Claim boundary and next smallest task

Established: a coarse certified enclosure of `h(0)`, the absolute endpoint
coefficient, an explicit local remainder, and four finite physical branch
masses. Not established: a sharp finite-rank/resolvent enclosure, an
exponential remainder, any determinant or arithmetic interpretation, Route B,
Hilbert–Pólya, or RH.

Next smallest task: either prove a frozen cusp-adapted finite-rank/resolvent
tail bound to sharpen the enclosure, or prove a quantitative remainder for the
branch-mass asymptotic. Do not compare zeros or introduce a roof in this task.

Recommended verdict: `REVISE`.

## Previous checkpoint — exact-($U_c$) physical-acip endpoint theorem

Current clue: `CLUE-A1-004`

Candidate ID: none. Parent and scoped audit IDs:

```text
P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK
P4-LOGISTIC-UC-ACIP-ENDPOINT-DENSITY
```

- Formal candidate: `false`
- Source commit: `84111b3f436ed1e8111c871719e32b70a4def098`
- Route-A evaluation:
  `evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T162511Z.yaml`
- Route-A tuple: `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`
- Overall: `ROUTE_A_EXPLORATORY`
- Scoped endpoint verdict: `GO_WITH_LIMITATIONS`
- Parent-candidate verdict: `REVISE`
- Route B: inactive and not authorized
- Formal candidate count: unchanged (`SS-0001`, `SS-0002` only)

The endpoint-density task is closed positively. This strengthens A1 but does
not create `SS-0003`: no arithmetic primitive-orbit law, von-Mangoldt trace,
s-dependent Fredholm determinant, non-lattice Riemann clock, or natural
quantization has been obtained.

### Source lock

Let

\[
f(x)=1-U_cx^2,
\qquad
U_c^3-2U_c^2+2U_c-2=0,
\qquad
\rho=U_c-1,
\]

on the physical core `J=[-rho,1]`. The named measure is the unique physical
absolutely continuous invariant probability `mu_ac`, normalized by
`mu_ac(J)=1`, with density `h=d mu_ac/dx`.

One `f` iterate remains one physical clock tick. The map `T=f^2` on
`A=[-rho,rho]`, its reflection `S=-T`, and the polar coordinate
`x=rho*sin(theta)` are proof coordinates only. The conditional `T`-acip on
`A` has density `g_A=2h`; it may not be mixed with the full `f`-acip ledger.

No determinant is defined. Prime tables, zero tables, zeta/xi evaluations,
USTC data, fitted weights, and orbit histograms as theorem evidence are
forbidden. The source lock is
`configs/source_locks/P4-LOGISTIC-UC-ACIP-ENDPOINT-DENSITY.yaml`.

### Strongest evidence

For

\[
T(x)=-\rho+2U_c^2x^2-U_c^3x^4,
\qquad S=-T,
\]

the polar conjugate is a two-full-branch analytic Markov map with

\[
\inf|G'|=\frac4{U_c^2}=2U_c\rho>1.
\]

The Jiang–Ruelle analytically expanding Markov RPF theorem applies: the
desingularized density is branchwise analytic, has matching traces at the
nonpolar point zero, and is strictly positive. After reflection and the
two-band lift, the exact Logistic map has a unique full-support physical acip
with `0<h(0)<infinity` and local Lipschitz regularity at zero.

The exact physical Perron–Frobenius ledger then gives

\[
\boxed{
h(-\rho+t)
=\frac{h(0)}{\sqrt2U_c}t^{-1/2}+O(1)
\qquad(t\downarrow0).
}
\]

Combining this with the independently proved endpoint-length ratio yields

\[
\boxed{
\frac{\mu_{\rm ac}(C_{2n+2})}{\mu_{\rm ac}(C_{2n})}
\longrightarrow
\frac1{2U_c(U_c-1)}
=\frac{U_c^2}{4}
=0.5957439419765593735\ldots.
}
\]

Ruelle (2009), Theorem 9 and Remark 16(a), independently cross-check the spike
coefficient. The Baladi–Smania citation is locked to corrected equation (1.1)
in the 2023 supplement to arXiv:2008.01654v4; the leading coefficient is
unchanged from the published formula.

### Strongest failure and reusable knowledge

The result proves an asymptotic physical mass ratio, not an exact finite-order
geometric law or the stronger legacy exponential-remainder formula. A closed
form or rigorous numerical enclosure for `h(0)` and selected finite branch
masses is still absent. First-return branches remain observables rather than
arithmetic primitive periodic orbits, and the modeled tower measure/coupling
remains additional structure.

`OBR-009` remains active. The raw unaccelerated first-return map still has
derivative infimum zero on every branch, so the legacy ordinary-`BV`
Lasota–Yorke/spectral-gap proof is refuted. The new theorem repairs only its
mass-ratio conclusion by a direct density argument; it does not restore that
operator or define a Fredholm determinant. `OBR-008` continues to block every
unit-lattice continuation as a completed-xi divisor.

Reusable knowledge: a quadratic postcritical cusp can be removed by a polar
coordinate, turning the parity-reduced exact-`U_c` map into a uniformly
expanding analytic Markov proof object while preserving the original physical
clock and normalization ledger.

### Updated files

- `CHANGELOG.md`
- `DERIVATION_PACKAGE.md`
- `configs/source_locks/P4-LOGISTIC-UC-ACIP-ENDPOINT-DENSITY.yaml`
- `docs/literature/exact_uc_acip_density_sources.md`
- `docs/prior_work/README.md`
- `docs/prior_work/claims_matrix.md`
- `docs/research_clues.md`
- `docs/candidate_registry.md`
- `docs/obstruction_registry.md`
- `docs/research_log.md`
- `experiments/p4_logistic_uc_acip_endpoint_density.py`
- `formal/results/exact_uc_acip_endpoint_density.md`
- `formal/results/exact_uc_first_return_support.md`
- `tests/test_p4_logistic_uc_acip_endpoint_density.py`
- `tests/test_p4_logistic_uc_first_return_support.py`
- `artifacts/p4_logistic_uc_acip_endpoint_density/structural_audit.json`
- `evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T162511Z.yaml`

`docs/operator_obligations.md` is unchanged because Route B remains closed.

### Tests and reproduction

Focused endpoint audit: `10/10 passed`.

Focused endpoint plus first-return support audits: `26/26 passed`.

Full repository: `99/99 passed`.

Artifact SHA-256:

```text
ef015a2f1f4fc475c7daf8b87c1a2fedc75f35b8e76e151eb588b279eca53a8e  artifacts/p4_logistic_uc_acip_endpoint_density/structural_audit.json
```

Commands:

```bash
python3 experiments/p4_logistic_uc_acip_endpoint_density.py \
  --quiet \
  --output artifacts/p4_logistic_uc_acip_endpoint_density/structural_audit.json
python3 -m unittest -v tests/test_p4_logistic_uc_acip_endpoint_density.py
python3 -m unittest -v \
  tests/test_p4_logistic_uc_acip_endpoint_density.py \
  tests/test_p4_logistic_uc_first_return_support.py
python3 -m unittest discover -v
python3 -c 'import yaml; paths=["configs/source_locks/P4-LOGISTIC-UC-ACIP-ENDPOINT-DENSITY.yaml","evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T162511Z.yaml"]; [yaml.safe_load(open(p,encoding="utf-8")) for p in paths]'
sha256sum artifacts/p4_logistic_uc_acip_endpoint_density/structural_audit.json
git diff --check
```

### Claim boundary and next smallest task

Established: physical-acip existence, uniqueness, physicality and full
support; finite positive `h(0)`; the exact endpoint inverse-square-root law;
positive mass for every physical even branch; and the asymptotic physical
branch-mass ratio.

Not established: a rigorous numerical enclosure of `h(0)`, exact finite-order
branch weights, an exponential remainder/rate, the modeled tower
measure/coupling, arithmetic primitive-orbit weights, a non-lattice clock, an
s-dependent Fredholm/completed-xi determinant, natural quantization, Route B,
Hilbert–Pólya, or RH.

Next smallest task: use the uniformly expanding polar coordinate and a frozen
validated approximation theorem to enclose `h(0)`, the absolute endpoint
coefficient, and selected finite branch masses. Record discretization,
truncation, rounding, normalization, and stopping errors separately; use no
prime or zero data.

Recommended verdict: `REVISE`.

---

## Previous checkpoint — exact-(U_c) first-return support closure

Current clue: `CLUE-A1-004`

Candidate ID: none. Parent audit and scoped support audit:

```text
P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK
P4-LOGISTIC-UC-FIRST-RETURN-SUPPORT
```

- Formal candidate: `false`
- Operational verdict: `REVISE`
- Route-A tuple: `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`
- Overall Route-A interpretation: `ROUTE_A_EXPLORATORY`
- Route B: inactive and not authorized
- New reusable obstruction: `OBR-009`
- Evaluation: `evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T105010Z.yaml`
- Evaluation source commit: `cd2ba4e7fabbcb5ace2466427a57e4d500eeaa27`
- Formal candidate count: unchanged (`SS-0001`, `SS-0002` only)

The exact physical first-return alphabet is now proved. This removes the prior
interval/kneading support obligation, but it does not promote the recurrent
Logistic construction to `SS-0003`: exact invariant weights, an arithmetic
primitive-orbit law, a viable Fredholm determinant, and a non-lattice clock
remain absent.

## Current source lock

Let

\[
f(x)=1-U_cx^2,
\qquad
U_c^3-2U_c^2+2U_c-2=0,
\qquad
\rho=U_c-1.
\]

The ambient and physical domains are frozen separately:

\[
X=[-1,1],
\qquad
J=f(X)=[-\rho,1],
\]

with event sets

\[
L_X=[-1,0),
\qquad
L_J=[-\rho,0).
\]

Zero is a non-event. For (D\in\{X,J\}),

\[
C_m(D)=L_D\cap
\bigcap_{j=1}^{m-1}f^{-j}(D\setminus L_D)
\cap f^{-m}(L_D).
\]

One iterate of (f) is one clock tick. The proof coordinate (T=f^2) does not
replace the clock. Ambient and physical return ledgers may not be mixed.

The support audit freezes an all-order theorem, a 100-decimal rational
enclosure of (U_c), 130-digit outward square-root bounds, a certified endpoint
prefix through branch 154 / return 308, and independent 180-digit midpoint
checks through branch 64. Prime tables, zero tables, target zeta/xi values,
USTC data, fitted gap weights, and empirical transition matrices are forbidden.

The parent recurrent tower remains

\[
\mathcal B=\{(\omega,j):\omega\in\mathbb N_{\geq1}^{\mathbb Z},
1\leq j\leq2\omega_0\},
\]

with one symbol (m) for physical label (2m) and the terminally anchored fibre
from lock version 3. The tower zeta and full reciprocal Artin--Mazur ledger
remain distinct; no first-return Fredholm determinant is defined.

## Strongest evidence

The algebraic identity (U_c\rho^2=1-\rho) gives the exact band swap

\[
f([-\rho,\rho])=[\rho,1],
\qquad
f([\rho,1])=[-\rho,\rho].
\]

Define

\[
h(y)=\sqrt{\frac{1-y}{U_c}},
\qquad
r_0=0,
\qquad
r_{n+1}=h(h(r_n)).
\]

Then (r_n\uparrow\rho) and

\[
C_2(J)=(-r_1,0),
\qquad
C_{2n}(J)=(-r_n,-r_{n-1}]\quad(n\ge2),
\qquad
C_{2n+1}(J)=\varnothing.
\]

Therefore

\[
\boxed{S_{\rm top}^{J}=2\mathbb N_{\ge1}},
\]

and every physical even label has exactly one nondegenerate interval branch.
The only nonreturning point is (-\rho).

More strongly,

\[
f^{2n}:\operatorname{int}C_{2n}(J)\longrightarrow(-\rho,0)
\]

is a real-analytic diffeomorphism for every (n). Hence every finite word of
positive even return labels has a nonempty open cylinder. The recurrent
tower's unrestricted finite-word alphabet now has physical provenance; its
full two-sided infinite completion, invariant measure, and aged fibre coupling
remain separate modeling choices.

On ambient (X), transient odd branches fill `[-1,-rho)`, so

\[
\boxed{S_{\rm top}^{X}=\mathbb N_{\ge1}}.
\]

Every invariant probability assigns those ambient odd branches zero mass.
Conditionally on the named physical acip having full support (J), every
physical even branch has strictly positive mass. This audit does not reprove
that support theorem, and exact values and mass asymptotics are not proved.

The rational certificate strictly separates the first 154 endpoint intervals,
and all 64 independent high-precision midpoint checks return at their predicted
first time. The parent recurrent tower retains its exact primitive census;
the signed full-fibre witness/residual ledger through period 16 remains a
separately labeled finite numerical prefix.

## Strongest failure and reusable knowledge

First-return branches are observables, not arithmetic primitive periodic
orbits. The renewal measure/coupling remains modeled, exact physical-acip
weights are unknown, and there is no log-prime clock or von-Mangoldt amplitude.

`OBR-009` proves that the natural unaccelerated first-return map is not
uniformly expanding. On (C_2),

\[
(f^2)'(x)=4U_c^2x f(x)\longrightarrow0
\qquad(x\uparrow0),
\]

and `x=-0.01` gives derivative magnitude `0.0953043164222... < 1`.
Every branch has derivative infimum zero, while the inverse Jacobian has a
square-root singularity at (-\rho). The old ordinary-`BV`
Lasota--Yorke/spectral-gap proof and its geometric branch-weight theorem are
therefore not established.

The endpoint-length ratio has the proved limit

\[
\lambda=\frac{1}{4U_c^2(U_c-1)^2}
=0.35491084440177\ldots.
\]

Only under the explicit open density hypothesis

\[
\frac{d\mu_{\rm ac}}{dx}(-\rho+t)
=C\,t^{-1/2}(1+o(1)),
\qquad C>0,
\qquad t\downarrow0,
\]

would the branch-mass ratio tend to

\[
\sqrt\lambda=\frac{1}{2U_c(U_c-1)}
=0.59574394197656\ldots.
\]

This is an `OPEN_CONDITIONAL_CLUE`, not a theorem. `OBR-008` independently
keeps every unit-lattice continuation `STOP_SCOPED` as a completed-ξ divisor.

## Current files

- `DERIVATION_PACKAGE.md`
- `configs/source_locks/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK.yaml`
- `configs/source_locks/P4-LOGISTIC-UC-FIRST-RETURN-SUPPORT.yaml`
- `experiments/p4_logistic_recurrent_uc_anchored_clock.py`
- `experiments/p4_logistic_uc_first_return_support.py`
- `tests/test_p4_logistic_recurrent_uc_anchored_clock.py`
- `tests/test_p4_logistic_uc_first_return_support.py`
- `artifacts/p4_logistic_recurrent_uc_anchored_clock/structural_audit.json`
- `artifacts/p4_logistic_uc_first_return_support/structural_audit.json`
- `formal/results/exact_uc_first_return_support.md`
- `formal/obstructions/exact_uc_first_return_nonuniform_expansion.md`
- `formal/obstructions/unit_lattice_clock_vertical_periodicity.md`
- `evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T105010Z.yaml`
- `docs/prior_work/README.md`
- `docs/prior_work/claims_matrix.md`
- `docs/research_clues.md`
- `docs/candidate_registry.md`
- `docs/obstruction_registry.md`
- `docs/research_log.md`

`docs/operator_obligations.md` is unchanged because Route B remains closed.

## Verification and reproduction

Focused support tests:

```text
16/16 passed
```

Focused recurrent tests:

```text
16/16 passed
```

Full repository:

```text
89/89 passed
```

Artifact SHA-256 values:

```text
93e591511aad7503d2c06cb786efacafdd575c4b0623fbcc1062bc77068cc101  artifacts/p4_logistic_uc_first_return_support/structural_audit.json
f29984b0ae0fe610524c9d48e2d9ca64528519c599d4a28061d12d20b5a0f496  artifacts/p4_logistic_recurrent_uc_anchored_clock/structural_audit.json
```

Commands:

```bash
python3 -m unittest -v tests/test_p4_logistic_uc_first_return_support.py
python3 -m unittest -v tests/test_p4_logistic_recurrent_uc_anchored_clock.py
python3 experiments/p4_logistic_uc_first_return_support.py \
  --quiet \
  --output artifacts/p4_logistic_uc_first_return_support/structural_audit.json
python3 experiments/p4_logistic_recurrent_uc_anchored_clock.py \
  --quiet \
  --output artifacts/p4_logistic_recurrent_uc_anchored_clock/structural_audit.json
python3 -m unittest discover -v
python3 -c 'import yaml; paths=["configs/source_locks/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK.yaml","configs/source_locks/P4-LOGISTIC-UC-FIRST-RETURN-SUPPORT.yaml","evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T105010Z.yaml"]; [yaml.safe_load(open(p,encoding="utf-8")) for p in paths]'
sha256sum artifacts/p4_logistic_uc_first_return_support/structural_audit.json artifacts/p4_logistic_recurrent_uc_anchored_clock/structural_audit.json
git diff --check
```

## Claim boundary and next smallest task

Established: exact physical/ambient return support, one full physical interval
branch per even label, the full finite-word return language, zero invariant
mass for ambient odd branches, conditional branch positivity under the named
full-support-acip hypothesis, rational endpoint certification through return
308, and the nonuniform-expansion obstruction.

Not established: realization of every infinite return-label sequence or a
complete full-shift conjugacy, exact acip branch weights, their asymptotic
ratio, a repaired transfer-operator theorem, complete fibre multiplicities,
arithmetic prime-orbit correspondence, non-lattice clock,
Fredholm/completed-ξ structure, natural quantization, Route B,
Hilbert--Pólya, or RH.

Next smallest task:

\[
\frac{\mu(C_{2n+2})}{\mu(C_{2n})}
\stackrel{?}{\longrightarrow}
\frac{1}{2U_c(U_c-1)}.
\]

Prove or refute the displayed physical-acip endpoint-density asymptotic.
Freeze either a direct Misiurewicz density argument, a weighted/cusp-adapted
function space, or a further accelerated inducing domain. Do not fit weights
or introduce a non-lattice roof before this is explicit.

Recommended verdict: `REVISE`.

---

## Previous checkpoint — exact-(U_c) recurrent Logistic audit

Current clue: `CLUE-A1-004`

Candidate ID: none. Audit ID:

```text
P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK
```

- Formal candidate: `false`
- Operational verdict: `REVISE`
- Route-A tuple: `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`
- Overall Route-A interpretation: `ROUTE_A_EXPLORATORY`
- Route B: inactive and not authorized
- New reusable obstruction: `OBR-008`
- Evaluation source commit: `95e72606c75e039ba3457a727e2d05377e35daf0`
- Formal candidate count: unchanged (`SS-0001`, `SS-0002` only)

The recurrent tower escapes the strict-monotone orbit-collapse obstruction
`OBR-007`, but it is not promoted to `SS-0003`. The link between its modeled
one-symbol-per-even alphabet and the complete physical exact-(U_c)
first-return branch system is not yet interval/kneading certified.

## Current source lock

The parent is

\[
f_u(x)=1-ux^2,
\]

where (U_c) is the unique real root of

\[
u^3-2u^2+2u-2=0.
\]

The frozen implementation value is

```text
U_c = 1.5436890126920764
hex = 0x1.8b2f3400b4fdcp+0
```

and

\[
0\to1\to1-U_c\to U_c-1\to U_c-1.
\]

The legacy literal `1.543689` is left of the exact point by
(-1.2692076278852937\times10^{-8}) and is only a control.

The event is (L=\{x<0\}); gaps are first-return times to (L). The critical
seed (x_0=0) has one (L)-hit and no gap sequence, so numerical gap
statistics use four frozen generic initial states.

The recurrent modeled tower is

\[
\mathcal B=\{(\omega,j):\omega\in\mathbb N_{\geq1}^{\mathbb Z},
1\leq j\leq2\omega_0\},
\]

with symbol (m) carrying exactly (L=2m) updates. The fibre law is

\[
\mu(j,L)=U_c+k\left[
\log^{-2}(100000+j)-\log^{-2}(100000+L)
\right],
\]

where `k=6.764850551029437`. The terminal branch returns `U_C` directly, so
(mu(L,L)=U_c) bitwise before renewal. The inherited `k` is target-contaminated
legacy provenance and contributes no arithmetic evidence.

Prime/zero tables, primality predicates, target zeta/xi evaluations, USTC data,
fitted phases, empirical transition matrices, best-seed selection, and
determinant-ledger mixing are forbidden.

## Strongest evidence

The frozen gap diagnostic uses burn-in `20000` and `300000` updates for each of
four initial states. For deltas (10^{-5},10^{-6},10^{-7}):

- exact center: zero odd gaps;
- every left control: zero odd gaps;
- every right control: positive odd-gap count;
- rounded `1.543689`: remains on the even left side.

The correct statement is that the odd-gap channel opens to the right. It is
not a composite-only channel. Low-count long-tail support is seed, cutoff,
precision, and last-bit sensitive and is not used as a definition.

The modeled tower has

\[
Z_T(z)=\frac{1-z^2}{1-2z^2},
\qquad
\#\operatorname{Fix}(G^{2r})=2(2^r-1),
\]

with no odd-period fixed points. Direct cyclic-word enumeration and Möbius
inversion agree through period 16: 70 primitive tower orbits. Every one has a
primitive full-fibre fixed-point witness, terminal (U_c) updates, and a
signed multiplier. The maximum return residual is

```text
3.7761460625063137e-14
```

The full reciprocal Artin--Mazur ledger is distinct from the tower zeta:

\[
D_{\rm AM,F}(z)=
\exp\left(-\sum_{n\geq1}\frac{\#\operatorname{Fix}(F^n)}n z^n\right).
\]

The bound

\[
N_G(n)\leq N_F(n)\leq2^nN_G(n)<4^n
\]

gives convergence of its logarithm for (|z|<1/4). No Fredholm determinant or
analytic continuation is claimed.

## Strongest failure and reusable knowledge

First-return gaps are observables, not primitive periodic orbits. The recurrent
tower is an extra modeling choice; one interval branch for every even label and
the physical invariant weights remain unproved. There is no log-prime clock,
von-Mangoldt repetition law, or arithmetic orbit correspondence.

`OBR-008` proves that every nonzero single-valued meromorphic
(H(e^{-s})) is (2\pi i)-periodic and has only (O(T)) divisor count in a
bounded real strip. It cannot equal the completed-ξ
(Theta(T\log T)) divisor. A zero-free prefactor cannot change that count.

Thus the current unit clock is `STOP_SCOPED` as a Riemann determinant, while
the broader exact-(U_c) branch audit remains `REVISE` and active.

## Current files

- `DERIVATION_PACKAGE.md`
- `configs/source_locks/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK.yaml`
- `experiments/p4_logistic_recurrent_uc_anchored_clock.py`
- `tests/test_p4_logistic_recurrent_uc_anchored_clock.py`
- `artifacts/p4_logistic_recurrent_uc_anchored_clock/structural_audit.json`
- `formal/obstructions/unit_lattice_clock_vertical_periodicity.md`
- `evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T080528Z.yaml`
- `docs/research_clues.md`
- `docs/candidate_registry.md`
- `docs/obstruction_registry.md`
- `docs/research_log.md`

`docs/operator_obligations.md` is unchanged because Route B remains closed.

## Verification and reproduction

Focused tests at the current checkpoint:

```text
16/16 passed
```

Full repository:

```text
73/73 passed
```

The regenerated artifact is byte-identical. SHA-256:

```text
16fc53e17a56eb84e491abd12d927cb0644fae9e3a543b8a9b25ca06d77f41cf
```

Commands:

```bash
python3 -m unittest -v tests/test_p4_logistic_recurrent_uc_anchored_clock.py
python3 experiments/p4_logistic_recurrent_uc_anchored_clock.py \
  --quiet \
  --output artifacts/p4_logistic_recurrent_uc_anchored_clock/structural_audit.json
python3 -m unittest discover -v
python3 -c 'import yaml; paths=["configs/source_locks/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK.yaml","evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T080528Z.yaml"]; [yaml.safe_load(open(p,encoding="utf-8")) for p in paths]'
git diff --check
```

## Claim boundary and next smallest task

Established: exact (U_c), correct legacy endpoint diagnosis, exact terminal
anchor, target-free odd-channel boundary, modeled tower primitive census,
signed full-fibre witnesses, local Artin--Mazur convergence, and `OBR-008`.

Not established: complete physical return support and weights, full fibre-root
multiplicity, arithmetic prime correspondence, von-Mangoldt trace formula,
Fredholm/completed-ξ determinant, natural quantization, Route B,
Hilbert--Pólya, or RH.

Next smallest task:

\[
S_{\rm top}=\{m:C_m\ne\varnothing\},
\qquad
C_m=L\cap\bigcap_{j=1}^{m-1}f^{-j}(I\setminus L)\cap f^{-m}(L).
\]

Prove or refute (S_{\rm top}=2\mathbb N) at exact (U_c), certify the
interval/kneading branches, and determine which branches have positive
invariant weight. Do not introduce a non-lattice roof before it is derived from
the same target-free dynamics.

---

## Previous checkpoint — compact monotone-clock audit (retained)

The `CLUE-A1-004` autonomous Logistic slow-clock audit is complete.

- Audit ID: `P4-LOGISTIC-MONOTONE-CLOCK-LIFT`
- Formal candidate: `false`
- Operational verdict: `STOP_SCOPED`
- Route-A tuple: `(A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`
- Overall Route-A interpretation: `ROUTE_A_REJECTED`
- Route B: inactive and not authorized
- New reusable obstruction: `OBR-007`

The audit does not allocate `SS-0003` or any other formal candidate ID.
`SS-0001` and `SS-0002` remain the two completed formal Route-A baselines,
both `STOP_SCOPED`. `CTRL-0001` remains a
`GO_WITH_LIMITATIONS` evaluator control and is not a candidate.

The earlier occupation-conditioned Logistic eigenphase observable remains
separately `STOP_SCOPED`. The present result evaluates a new mathematical
object: an exact compact autonomous clock lift, not the empirical matrix.

## Current entry files

- `configs/source_locks/P4-LOGISTIC-MONOTONE-CLOCK-LIFT.yaml`
- `experiments/p4_logistic_monotone_clock_lift.py`
- `tests/test_p4_logistic_monotone_clock_lift.py`
- `artifacts/p4_logistic_monotone_clock_lift/structural_audit.json`
- `formal/obstructions/strict_monotone_clock_orbit_collapse.md`
- `evaluations/route_a/P4-LOGISTIC-MONOTONE-CLOCK-LIFT/20260804T025047Z.yaml`
- `docs/research_clues.md`
- `docs/candidate_registry.md`
- `docs/obstruction_registry.md`
- `docs/research_log.md`

## Frozen mathematical object

The legacy micro schedule is

\[
\mu_n=u_c+\frac{k}{\log^2(n+10)},
\qquad n\geq1,
\]

with

\[
k=0.1185699450083701,
\qquad
u_c=1.543078787606443,
\]

so that

\[
\mu_1=1.5637,
\qquad
\mu_{10^6}=1.5437.
\]

Set

\[
v_n=\frac1{\log(n+10)}
\]

and define on

\[
X=[-1,1]\times[0,1/\log11]
\]

the compact autonomous skew product

\[
F(x,v)=\left(1-(u_c+kv^2)x^2,G(v)\right),
\]

where

\[
G(v)=
\begin{cases}
\displaystyle
\frac1{\log(e^{1/v}+1)}
=
\frac{v}{1+v\log(1+e^{-1/v})},&v>0,\\[6pt]
0,&v=0.
\end{cases}
\]

The source lock uses the continuum anchor

\[
(x_0,v_1)=(0.5,1/\log11).
\]

The historical empirical discretization placed its point mass at the cell
containing `0.5`; that matrix object, its fitted epsilon, and its eigenphases
are excluded from this audit.

No prime, Riemann-zero, `xi`, `zeta`, or USTC table is read. There is no phase
scale, partition, Gaussian kernel, affine spectral map, unfolding, modulo
clock, reset, clamp, or repeated finite monodromy.

## Exact schedule and phase-space checks

For every \(v>0\) and integer \(m\geq0\),

\[
G^m(v)
=
\frac1{\log(e^{1/v}+m)}
=
\frac{v}{1+v\log(1+me^{-1/v})}.
\]

Therefore

\[
G^{n-1}(1/\log11)=\frac1{\log(n+10)},
\]

which exactly reproduces the frozen schedule.

The parameter range is

\[
0<u_c\leq u_c+kv^2\leq1.5637<2.
\]

Thus every fibre map sends `[-1,1]` into itself and \(F:X\to X\) is
well-defined.

The diagnostic direct-versus-closed clock maximum error over the frozen
periods was `1.1102230246251565e-16`. The short direct-versus-lifted trajectory
maximum error over all five frozen initial `x` controls was zero in binary64.
These diagnostics check the implementation; the structural result below is
exact.

## Proved periodic-orbit obstruction

For any skew product

\[
F(y,b)=(f_b(y),g(b)),
\]

one has

\[
\operatorname{Fix}(F^m)
=
\bigcup_{b\in\operatorname{Fix}(g^m)}
\left\{
(y,b):
f_{g^{m-1}b}\circ\cdots\circ f_b(y)=y
\right\}.
\]

For the frozen compact clock,

\[
G^m(v)<v
\]

for every \(v>0\) and \(m\geq1\), while \(G^m(0)=0\). Hence

\[
\boxed{
\operatorname{Fix}(F^m)
=
\operatorname{Fix}(f_{u_c}^m)\times\{0\}
}
\]

and

\[
\operatorname{Prim}(F)
=
\operatorname{Prim}(f_{u_c})\times\{0\}.
\]

Every full periodic orbit lies on the static-limit boundary. No periodic orbit
visits or samples the aging interior.

Moreover,

\[
G'(0)=1.
\]

Every boundary orbit therefore has a neutral clock multiplier. A usual
hyperbolic stability factor involving `det(I-DF^m)` is degenerate in that
direction. Removing the multiplier by hand would define a different
determinant ledger.

This theorem is registered as:

```text
OBR-007 — Strict-monotone clock lifts collapse periodic orbits to the clock fixed set
```

## Frozen determinant convention

The sole ledger is

\[
Z_{\rm AM,F}(z)
=
\exp\left(
\sum_{m\geq1}\frac{\#\operatorname{Fix}(F^m)}m z^m
\right),
\qquad
D_{\rm AM,F}(z)=Z_{\rm AM,F}(z)^{-1},
\]

interpreted only as a formal Artin--Mazur power series.

The fixed-set theorem gives

\[
D_{\rm AM,F}=D_{\rm AM,f_{u_c}}
\]

coefficient by coefficient. The slow-clock lift contributes no new
periodic-orbit determinant data beyond the static limiting Logistic parent.

No convergence, analytic continuation, root ledger, Ruelle determinant,
Fredholm determinant, functional equation, Gamma factor, trivial-zero ledger,
or completed-`xi` divisor is asserted.

## Adversarial controls

- A point fixed by the first fibre map returns in `x`, but the clock changes,
  so it is not a full-state fixed point.
- Periodizing the clock at `P=8,32,64` makes step `P+1` reuse `mu_1`; each
  control changes the original schedule.
- Clamping at those cutoffs creates different static parent parameters, hence
  a cutoff-dependent orbit ledger.
- The true boundary parent parameter is `u_c`, not the finite-window endpoint
  `1.5437` and not the separate legacy regression value `1.543689`.
- The formal Artin--Mazur ledger remains separate from matrix, projected-cycle,
  logarithmic-derivative, Koopman, and Fredholm ledgers.

Every frozen schedule, invariance, clock, trajectory, projected-return,
boundary-parent, modulo, clamp, source-lock parity, and ledger-separation gate
passed.

## Route-A interpretation

```text
A1_FAIL / PROVED
```

All primitive orbits are static-limit boundary orbits. There is no aging
primitive grammar, intrinsic `log p` clock, or von-Mangoldt repetition
structure.

```text
A2_FAIL / PROVED
```

The reciprocal Artin--Mazur formal series reduces exactly to the static parent.
No new analytic determinant is produced, and the neutral clock multiplier
blocks the usual hyperbolic stability weight.

```text
A3_FAIL / NOT_TESTABLE
```

No analytic determinant exists to test conjugation symmetry, functional
equation, completed factors, zero count, continuation, or divisor equality.

```text
A4_FAIL / NOT_TESTABLE
```

The compact autonomous map is noninvertible, singular at `x=0`, and has no
frozen symplectic/contact/scattering structure, Hilbert space, operator domain,
or same-clock natural quantization.

Overall:

```text
(A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)
ROUTE_A_REJECTED
STOP_SCOPED
Route B not invoked
```

## Repository updates

Created:

- `configs/source_locks/P4-LOGISTIC-MONOTONE-CLOCK-LIFT.yaml`;
- `experiments/p4_logistic_monotone_clock_lift.py`;
- `tests/test_p4_logistic_monotone_clock_lift.py`;
- `artifacts/p4_logistic_monotone_clock_lift/structural_audit.json`;
- `formal/obstructions/strict_monotone_clock_orbit_collapse.md`;
- `evaluations/route_a/P4-LOGISTIC-MONOTONE-CLOCK-LIFT/20260804T025047Z.yaml`.

Updated:

- `docs/candidate_registry.md`, with an explicit non-candidate summary note;
- `docs/obstruction_registry.md`, with `OBR-007`;
- `docs/research_clues.md`;
- `docs/research_log.md`;
- this handoff.

Unchanged by design:

- `docs/operator_obligations.md`, because Route B remains closed;
- the formal candidate count, because this audit failed before promotion;
- all legacy repositories, caches, checkpoints, and prior artifacts.

## Verification

Focused tests:

```text
11/11 passed
```

Full repository:

```text
57/57 passed
```

The regenerated artifact was byte-identical with SHA-256:

```text
579967237444cd6b4835cfa5932c9e95771ad279e06846422d95076d26348989
```

Both new YAML files parse successfully.

Reproduction commands:

```bash
python3 -m unittest -v tests/test_p4_logistic_monotone_clock_lift.py
python3 experiments/p4_logistic_monotone_clock_lift.py \
  --quiet \
  --output artifacts/p4_logistic_monotone_clock_lift/structural_audit.json
python3 -m unittest discover -v
python3 -c 'import yaml; paths=["configs/source_locks/P4-LOGISTIC-MONOTONE-CLOCK-LIFT.yaml","evaluations/route_a/P4-LOGISTIC-MONOTONE-CLOCK-LIFT/20260804T025047Z.yaml"]; [yaml.safe_load(open(p,encoding="utf-8")) for p in paths]'
git diff --check
```

Runtime for the new audit: CPython `3.12.3`; the implementation uses only the
Python standard library. PyYAML `6.0.2` is used by the parity test.

## Claim boundary

Established:

- exact compact autonomous embedding of the frozen logarithmic schedule;
- forward invariance of the declared phase space;
- exact fixed-set and primitive-orbit collapse to the static-limit slice;
- neutral clock multiplier and the resulting stability-weight warning;
- exact formal determinant reduction to the static parent;
- modulo and clamped clocks are different, cutoff-dependent systems;
- a reusable strict-monotone-base skew-product obstruction.

Not established:

- an analytic, Ruelle, transfer-operator, or Fredholm determinant;
- rational-prime or von-Mangoldt orbit structure;
- completed-`xi` analytic structure or divisor equality;
- a no-go theorem for every autonomous lift;
- natural quantization, self-adjointness, Route B, Hilbert--Polya, RH, or a
  physical spectral realization.

## Next smallest task

Do not tune or numerically zero-match the present lift.

The next object must be a new intrinsic recurrent base \(G\) with at least one
nontrivial periodic orbit. It must be proved that its full-space periodic
orbits leave the static-limit slice while its observable or roof genuinely
reproduces logarithmic aging. A nondegenerate same-object determinant must then
be frozen before any target comparison.

No such recurrent-base object is currently mathematically defined. This is the
current stopping condition; the alternative reopening is a fully defined
chronological transfer-cocycle determinant with a frozen function space,
horizon, clock, normalization, repetition law, and trace theorem.
