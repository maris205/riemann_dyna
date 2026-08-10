# HP-Dynamics Handoff

## Current status — CLUE-A4-002 irrational-roof bouquet prefilter

Current clue: `CLUE-A4-002`.

Candidate ID: none; audit `SS-PREFILTER-IRRATIONAL-BOUQUET-001` is explicitly
not a formal candidate and does not allocate `SS-0003`.

- Source lock: `configs/source_locks/SS-PREFILTER-IRRATIONAL-BOUQUET.yaml`
- Route-A evaluation: `evaluations/route_a/SS-PREFILTER-IRRATIONAL-BOUQUET/20260810T162243Z.yaml`
- Formal result: `formal/results/ss_prefilter_irrational_bouquet.md`
- Generator: `experiments/ss_prefilter_irrational_bouquet.py`
- Artifact: `artifacts/ss_prefilter_irrational_bouquet/audit.json`
- Scoped obstruction: `OBR-016`
- Route-A tuple: `(A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)`
- Riemann-target tuple: `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`
- Verdict: `ROUTE_A_REJECTED / STOP_SCOPED`
- Route B: not invoked and not authorized

The same-object determinant is entire and has the exact divisor
`s_{n,k}=-(n^2+2*pi*i*k)/(n+sqrt(2))`; every bounded vertical strip has
`O(T)` zeros because the real zero lines escape to `-infinity`.  The global
periods are incommensurate, but the base is disconnected and not mixing.

The next task is not to promote `SS-0003`: define a connected or renewal
non-Selberg object with a fresh source lock only if its cycle actions remain in
a fixed critical strip.  No root, spectrum, or Route-B work is allowed.

## Previous checkpoint — COPRIME-0001 countable trace and primitive-cycle ledger

Current clue: `CLUE-A1-009`.

Candidate ID: `COPRIME-0001` (formal candidate; first theorem-edge audit).

- Source lock: `configs/source_locks/COPRIME-0001-COUNTABLE-TRACE.yaml`
- Route-A evaluation: `evaluations/route_a/COPRIME-0001/20260809T134933Z.yaml`
- Formal result: `formal/results/coprime_0001_countable_trace.md`
- Generator: `experiments/coprime_0001_countable_trace.py`
- Artifact: `artifacts/coprime_0001/countable_trace_certificate.json`
- Focused tests: `tests/test_coprime_0001_countable_trace.py`
- Scoped obstruction: `OBR-014` / `formal/obstructions/coprime_ell2_operator_boundary.md`
- Route-A tuple: `(A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)`
- Overall/scoped verdict: `ROUTE_A_EXPLORATORY / GO_WITH_LIMITATIONS`
- Route B: not invoked and not authorized

### Frozen object

The countable shift is

```text
Sigma_cop={(n_k)_{k in Z}: n_k>=2, gcd(n_k,n_{k+1})=1}
tau(n_k)=log(n_0)
```

and the symmetric transfer kernel on `ell^2({2,3,...})` is

```text
(L_s)_{mn}=1_{gcd(m,n)=1}(mn)^(-s/2),  Re(s)>1.
```

The only determinant ledger is `D_cop(s)=det_F(I-L_s)`. The label one is
excluded, and the cyclic half-roof factors telescope to
`prod_i n_i^(-s)`. No reciprocal, logarithmic derivative, scattering
quotient, xi factor, prime table, or zero table is admitted.

### Strongest evidence

For `sigma=Re(s)>1`, the Mobius rank-one expansion has trace-norm sum

```text
sum_d |mu(d)| S_d = zeta(sigma)^2/zeta(2 sigma)-1 < infinity.
```

Thus `L_s` is a locally uniformly holomorphic trace-class family. Absolute
cycle summability justifies the exact trace-power identity and the primitive
repetition ledger. There are no period-one cycles; period-two and period-three
orientation factors and inclusion-exclusion formulas pass exactly. The exact
Fraction certificate reproduces the ledger through `k=6`.

The operator boundary is exact: `||L_s e_2||_2^2 = 2^(-sigma) sum_{m>=3,m odd}
m^(-sigma)` diverges for `sigma<=1`. A continuation across `Re(s)=1`, if it
exists, must therefore be a separate scalar determinant theorem beyond the
original bounded `ell^2` operator; it cannot be a silent extension of the same
operator.

### Strongest failure

The coprimality rule has no proved prime-orbit correspondence or
von-Mangoldt weighting. Analytic continuation, global divisor growth,
functional equation, completed-xi equality, and quantization are open. This
is an A2 theorem edge, not a Riemann determinant result.

### Verification

```text
Focused suite: 10/10 passed
Full repository suite after integration: 283/283 passed
```

```bash
python3 experiments/coprime_0001_countable_trace.py --quiet \
  --output artifacts/coprime_0001/countable_trace_certificate.json
python3 -m unittest -v tests/test_coprime_0001_countable_trace.py
git diff --check
```

### Claim boundary and next smallest task

Established: exact trace class on `Re(s)>1`, holomorphic same-object Fredholm
determinant on that half-plane, exact trace powers, and primitive cycles for
periods 1--3.

Not established: prime correspondence, von-Mangoldt trace, continuation,
`T log T` divisor law, completed xi, Route B, Hilbert--Pólya, or RH.

Next smallest task: audit whether the scalar `D_cop(s)` continues across
`Re(s)=1` despite the exact `ell^2` operator boundary, or prove an intrinsic
barrier, preserving the source lock and never searching roots.

Recommended verdict: `GO_WITH_LIMITATIONS`; overall `ROUTE_A_EXPLORATORY`.

## Current status — LOG-0001 Phragmen--Lindelof order lower bound

Current clue: CLUE-A1-004.

Candidate ID: LOG-0001 (formal candidate).

- Evaluation source commit: 9b0b09e305579d9ed0ae755b2e499a3bd05a261b
- HP-Dynamics research commit: `d1cfa20c6b69503af95abb96ded893eb19329371`
- Shared standalone paper-stage mirror: the theorem is recorded in the main
  repository as a scoped analytic audit; the lower-growth standalone mirror
  remains the active shareable paper stage
- Source lock: configs/source_locks/LOG-0001-ORDER-LOWER.yaml
- Route-A evaluation: evaluations/route_a/LOG-0001/20260809T110000Z.yaml
- Formal theorem: formal/results/log_0001_order_lower.md
- Analytic Route-A tuple:
  (A1_WEAK, A2_ANALYTIC_DETERMINANT,
   A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)
- Riemann-target tuple: (A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
- Overall/scoped verdict: ROUTE_A_EXPLORATORY / GO_WITH_LIMITATIONS
- Route-B tuple: all NOT_INVOKED; invocation is not authorized

The frozen determinant remains

\[
D_{\rm pol}(s)=\det_{\rm Fr}(I-\mathcal L_s|_B),
\qquad B=\ker[v_L(0)-v_R(0)].
\]

The inherited signed trace theorem gives a uniform bound

\[
|D_{\rm pol}(s)|\le K_2=e^{B_2}
\quad\text{for }\Re(s)\ge2,
\qquad
B_2=\frac{-\log(1-2\alpha_0^2)}{1-\alpha_0},
\quad \alpha_0=U_c^2/4.
\]

Assume for contradiction that the classical order is \rho<1. Choose
\(\rho<\eta<\mu<1\), set \(g(z)=D_{\rm pol}(2-z)\) on \(\Re z>0\), and use
the principal \(z^\mu\) branch. Since

\[
\Re(z^\mu)\ge\cos(\mu\pi/2)|z|^\mu
\]

in that half-plane, the damped function
\(g(z)e^{-\varepsilon z^\mu}\) is bounded on the large semicircle when
\(\eta<\mu\). The half-disk maximum principle and
\(\varepsilon\downarrow0\) bound the complementary half-plane by \(K_2\).
Liouville then contradicts the inherited witness \(D_{\rm pol}'(2)>0.0213\).

Thus the same determinant satisfies

\[
\boxed{1\le\operatorname{ord}(D_{\rm pol})\le2.}
\]

Order one is sharp under these hypotheses; \(1+e^{-(s-2)}\) is a bounded
order-one example on the corresponding half-plane.

### Strongest evidence

- The bound is uniform in imaginary height on the full line Re(s)=2, not
  merely a real-axis limit.
- The PL damping, half-plane orientation, principal branch, and Liouville
  contradiction were independently audited.
- The 1024-bit scalar certificate verifies B_2, K_2, the inherited
  nonconstancy witness, source hashes, and all logical gates.

### Strongest failure

This does not identify order one versus two, type, divisor asymptotics, a
T log T law, arithmetic orbit weights, a completed-xi divisor, quantization,
Route B, Hilbert--Pólya, or RH. The result is an analytic closure of one
LOG-0001 obligation, not a target-divisor result.

### New reusable knowledge

1. A nonconstant entire function bounded on one closed half-plane has order at
   least one; the strict threshold comes from the half-plane opening \pi.
2. A real-axis limit to one is not enough for this implication; uniform
   vertical-height control on a full boundary line is essential.
3. The order interval 1<=ord<=2 is a reusable structural fact for the frozen
   determinant, but it does not imply a Riemann--von Mangoldt law.

### Updated files

- configs/source_locks/LOG-0001-ORDER-LOWER.yaml
- evaluations/route_a/LOG-0001/20260809T110000Z.yaml
- formal/results/log_0001_order_lower.md
- experiments/log_0001_order_lower.py
- artifacts/log_0001_order_lower/order_lower_certificate.json
- tests/test_log_0001_order_lower.py
- docs/candidate_registry.md
- docs/research_clues.md
- docs/research_log.md
- HP_HANDOFF.md
- CHANGELOG.md

Route B remains closed; no obstruction-registry or operator-obligation entry is
added.

### Tests and reproduction commands

- Focused order-lower suite: `7/7 passed`.
- Full repository suite: `273/273 passed` (`93.770 s`).
- All 57 source-lock/evaluation YAML files parse; `git diff --check` passes.

```bash
python3 experiments/log_0001_order_lower.py --quiet \
  --output artifacts/log_0001_order_lower/order_lower_certificate.json
python3 -m unittest -v tests/test_log_0001_order_lower.py
python3 -m unittest discover -s tests -p 'test_*.py'
python3 -c 'from pathlib import Path; import yaml; fs=list(Path("configs/source_locks").glob("*.yaml"))+list(Path("evaluations").rglob("*.yaml")); [yaml.safe_load(p.read_text(encoding="utf-8")) for p in fs]; print(len(fs))'
git diff --check
```

### Claim boundary and next task

Established: 1<=ord(D_pol)<=2 for the same determinant under the inherited
source lock.

Not established: exact order, type, target zeros, divisor asymptotics,
arithmetic orbit law, completed-xi, quantization, Route B, Hilbert--Pólya, or
RH.

Next smallest task: apply the breadth pivot. Define one new intrinsic recurrent
candidate with an explicit phase space, clock, determinant convention, and a
plausible arithmetic orbit law, or register a reusable structural obstruction.
Do not append another fixed-point estimate to LOG-0001.

Recommended verdict: GO_WITH_LIMITATIONS; overall ROUTE_A_EXPLORATORY.

## Current status — LOG-0001 cancellation-safe lower growth

Current clue: `CLUE-A1-004`.

Candidate ID: `LOG-0001` (formal candidate).

- Evaluation source commit: `8cabec587cf0a796f4f004bf5b1b0611de3305f3`
- HP-Dynamics research commit: `726e42a93a9fabcf07c4c543c1c5962aa0fa1569`
- Shared standalone paper-stage mirror commit: `8fbe914cf4438a5a792f7e87e0c87e3a88292201`
- Source lock: `configs/source_locks/LOG-0001-LOWER-GROWTH.yaml`
- Route-A evaluation: `evaluations/route_a/LOG-0001/20260809T073000Z.yaml`
- Formal theorem: `formal/results/log_0001_lower_growth.md`
- Analytic Route-A tuple:
  `(A1_WEAK, A2_ANALYTIC_DETERMINANT,
  A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)`
- Riemann-target tuple: `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`
- Overall/scoped verdict: `ROUTE_A_EXPLORATORY / GO_WITH_LIMITATIONS`
- Route-B tuple: all `NOT_INVOKED`; invocation is not authorized
- Shared mirror target:
  `hilbert-polya-structure/logistic_dynamics/projects/exact_uc_polar_lower_growth/`

The determinant and every clock, branch sign, matching condition, and
normalization are inherited unchanged:

\[
D_{\rm pol}(s)=\det_{\rm Fr}(I-\mathcal L_s|_B),
\qquad B=\ker[v_L(0)-v_R(0)].
\]

The new lock opens only the safe real point `s=2`.  Writing

\[
\alpha_0=U_c^2/4,\qquad \tau_*=-\log\alpha_0,
\qquad
B_2=\frac{-\log(1-2\alpha_0^2)}{1-\alpha_0},
\]

the complete signed trace logarithm is locally uniformly differentiable on
the inherited zero-free half-plane.  Every real-axis summand has a positive
orientation denominator, so retaining the `n=1` pure-left word only after the
full-ledger positivity proof gives

\[
D_{\rm pol}'(2)\ge
c_2:=e^{-B_2}\frac{\tau_*\alpha_0^2}{1-\alpha_0}
>0.0213.
\]

The 1024-bit outward Arb certificate uses the inherited 100-decimal-digit
root bracket and reports `c_2=0.02130840854978611545...` with 327 relative
accuracy bits.  Cauchy's estimate then gives

\[
M_D(R)>0.0213(R-2)\quad(R>2),
\qquad M_D(R)>0.01065R\quad(R\ge4).
\]

Since the same determinant tends to one on the positive real axis while its
derivative at two is nonzero, it is nonconstant and transcendental entire;
the maximum modulus eventually dominates every fixed power.  This is a
same-object analytic lower-growth result, not a divisor or target-zero result.

### Strongest evidence

- Exact signed denominators and the full repetition ledger are retained; no
  auxiliary-`lambda` coefficient or determinant truncation is substituted.
- Local-uniform differentiated trace-log convergence and strict positivity of
  every real summand were independently audited.
- The pure-left boundary word has exact `epsilon=+1`, multiplier
  `alpha_0`, and matching multiplicity one.
- Focused lower-growth suite: `8/8 passed`; the certificate reproduces
  byte-for-byte under the frozen CPython/python-flint/FLINT environment.

### Strongest failure

The result does not establish positive or exact entire order, exponential
lower type, any zero-count lower bound, a `T log T` law, a log-prime or
von-Mangoldt orbit law, a functional equation, completed-`xi` divisor,
quantization, Route B, Hilbert--Pólya, or RH.  The next order-lower audit is
separately locked and must not be folded into this result.

### New reusable knowledge

1. Positivity on a safe real half-plane can turn one exact signed trace term
   into a rigorous lower bound for the same Fredholm determinant without
   evaluating determinant values or roots.
2. A nonzero derivative plus `D_pol(sigma)->1` proves transcendental-entire
   status, but not positive order or a zero-count asymptotic.
3. A 1024-bit working context with a 100-digit inherited root bracket should
   be reported as interval working precision, not as 300 correct decimal
   output digits.

### Updated files

- `configs/source_locks/LOG-0001-LOWER-GROWTH.yaml`
- `evaluations/route_a/LOG-0001/20260809T073000Z.yaml`
- `formal/results/log_0001_lower_growth.md`
- `experiments/log_0001_lower_growth.py`
- `artifacts/log_0001_lower_growth/lower_growth_certificate.json`
- `tests/test_log_0001_lower_growth.py`
- `docs/candidate_registry.md`
- `docs/research_clues.md`
- `docs/research_log.md`
- `HP_HANDOFF.md`
- `CHANGELOG.md`

`docs/obstruction_registry.md` and `docs/operator_obligations.md` remain
unchanged: no obstruction was proved and Route B is still closed.

### Reproduction commands

```bash
python3 experiments/log_0001_lower_growth.py \
  --quiet \
  --output artifacts/log_0001_lower_growth/lower_growth_certificate.json
python3 -m unittest -v tests/test_log_0001_lower_growth.py
python3 -m unittest discover -s tests -p 'test_*.py'
python3 -c 'from pathlib import Path; import yaml; fs=list(Path("configs/source_locks").glob("*.yaml"))+list(Path("evaluations").rglob("*.yaml")); [yaml.safe_load(p.read_text(encoding="utf-8")) for p in fs]; print(len(fs))'
git diff --check
sha256sum \
  artifacts/log_0001_lower_growth/lower_growth_certificate.json \
  experiments/log_0001_lower_growth.py \
  formal/results/log_0001_lower_growth.md \
  configs/source_locks/LOG-0001-LOWER-GROWTH.yaml \
  evaluations/route_a/LOG-0001/20260809T073000Z.yaml \
  tests/test_log_0001_lower_growth.py
```

### Claim boundary and next task

Established: `D_pol'(2)>0.0213`, the displayed linear maximum-modulus lower
bounds, nonconstant/transcendental-entire status, and qualitative
super-polynomial maximum-modulus growth for the frozen same determinant.

Not established: positive or exact order, exponential lower growth, zero-count
lower bounds, sharp divisor asymptotics, arithmetic orbit weights, target
zeros, functional equation, completed-`xi`, quantization, Route B,
Hilbert--Pólya, or RH.

Next smallest task: under a new source lock, audit whether the proved bounded
right half-plane, finite-order upper bound, and nonconstancy force
`ord(D_pol)>=1` by a Phragmen--Lindelöf argument; then apply the breadth pivot.

Recommended verdict: `GO_WITH_LIMITATIONS`; overall `ROUTE_A_EXPLORATORY`.

## Current status — LOG-0001 explicit conformal restriction ratios

Current clue: `CLUE-A1-004`.

Candidate ID: `LOG-0001` (formal candidate).

- Evaluation source commit: `dbb78f10bb3299415e022ecadb20d65e0aac5436`
- HP-Dynamics research commit: `80107bc8ec2bcb4b5d0dd7a30447c5bc2d075320`
- Shared standalone paper-stage mirror commit:
  `ce0e3c88a3daa32ccf79f7fdeb9c0b22695bc6f5`
- Source lock: `configs/source_locks/LOG-0001-CONFORMAL-RATIO.yaml`
- Route-A evaluation: `evaluations/route_a/LOG-0001/20260808T151232Z.yaml`
- Formal theorem: `formal/results/log_0001_conformal_ratio.md`
- Analytic Route-A tuple:
  `(A1_WEAK, A2_ANALYTIC_DETERMINANT,
  A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)`
- Riemann-target tuple: `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`
- Overall/scoped verdict: `ROUTE_A_EXPLORATORY / GO_WITH_LIMITATIONS`
- Route-B tuple: all `NOT_INVOKED`; invocation is not authorized
- Shared mirror target:
  `hilbert-polya-structure/logistic_dynamics/projects/exact_uc_polar_conformal_ratio/`

The determinant is unchanged:

\[
D_{\rm pol}(s)=\det_{\rm Fr}(I-\mathcal L_s|_B),
\qquad B=\ker[v_L(0)-v_R(0)].
\]

Let the frozen outer stadium radius be `R=1/1000`, the proof-only inner
radius be `r_0=3/5000`, and normalize

\[
h_L(0)=-\pi/4,
\qquad h_R(0)=\pi/4,
\qquad h_\sigma'(0)>0.
\]

With the curvature-`-1` Poincare metric, a midpoint-to-projection path costs
at most `500*pi`, while the projection-to-point disk path costs at most
`log(4)`.  Therefore

\[
r_L=r_R\le
\tanh\!\left(\frac{500\pi+\log4}{2}\right)=:r_*<1.
\]

Writing `t=exp(-(500*pi+log(4)))`, the stable formulas

\[
\delta_*=1-r_*=\frac{2t}{1+t},
\qquad
\beta_*=-\log r_*=\log\frac{1+t}{1-t}
\]

give positive 4096-bit outward intervals. Both quantities begin

```text
3.2418512480136249798375853005287351e-683.
```

The inherited two matching-space streams then satisfy the explicit
coefficient majorant

\[
|a_q(s)|\le q^{q/2}(q+1)
\left(\frac{e^{(103/125)|s|}}{\delta_*}\right)^q
r_*^{q^2/4-q/2}.
\]

Choosing `theta=1/4096` and summing the resulting shifted Gaussian proves

\[
|D_{\rm pol}(s)|\le
\exp\!\left(3.45\times10^{689}
+4.20\times10^{682}(1+|s|)^2\right).
\]

### Strongest evidence

- The proof stays on the same normalized stadium pair and same canonical
  matching-space determinant; no conformal grid, finite matrix, or reciprocal
  zeta is substituted.
- An independent adversarial audit verified the Poincare factor, branch
  interval length, path containment including boundary points, translation
  identity `r_L=r_R`, non-strict comparison `r_sigma<=r_*`, coefficient
  constants, and claim boundary.
- The target-free 4096-bit Arb certificate keeps more than 1000 relative bits
  on both small positive quantities and certifies the published decimal
  ceilings.
- Focused suite: `7/7 passed`; full repository suite: `258/258 passed`;
  standalone mirror suite: `7/7 passed`.
- The standalone 5-page paper compiled twice without warnings, undefined
  references, overfull boxes, or unembedded fonts.

### Strongest failure

The explicit path bound is intentionally coarse for a long, thin stadium.
It proves finite constants but not the exact conformal ratios or true
determinant type. There is no lower growth theorem, sharp divisor asymptotic,
log-prime/von-Mangoldt orbit law, functional equation, completed-`xi`
identity, natural quantization, or Route-B object. No Fredholm or Riemann
roots were computed.

### New reusable knowledge

1. A compact planar restriction ratio can be made explicit by bounding
   hyperbolic distance in the outer domain and transporting through a
   normalized Riemann map; a numerical conformal solver is not always needed.
2. When `r` is exponentially close to one, compute `1-r` and `-log(r)` from
   `t=exp(-D)` rather than from ordinary-precision `tanh(D/2)`.
3. Replacing `product_h(1-r^h)^(-1)` by `(1-r_*)^(-q)` is crude but turns a
   parameterized geometric-stream theorem into a reproducible numerical
   bound.

### Updated files

- `configs/source_locks/LOG-0001-CONFORMAL-RATIO.yaml`
- `evaluations/route_a/LOG-0001/20260808T151232Z.yaml`
- `formal/results/log_0001_conformal_ratio.md`
- `experiments/log_0001_conformal_ratio.py`
- `artifacts/log_0001_conformal_ratio/conformal_ratio_certificate.json`
- `tests/test_log_0001_conformal_ratio.py`
- `docs/candidate_registry.md`
- `docs/research_clues.md`
- `docs/research_log.md`
- `HP_HANDOFF.md`
- `CHANGELOG.md`

`docs/obstruction_registry.md` is unchanged because no impossibility theorem
was proved. `docs/operator_obligations.md` is unchanged because A4 fails and
Route B is not authorized.

### Reproduction commands

```bash
python3 experiments/log_0001_conformal_ratio.py \
  --quiet \
  --output artifacts/log_0001_conformal_ratio/conformal_ratio_certificate.json
python3 -m unittest -v tests/test_log_0001_conformal_ratio.py
python3 -m unittest discover -s tests -p 'test_*.py'
python3 -c 'from pathlib import Path; import yaml; fs=list(Path("configs/source_locks").glob("*.yaml"))+list(Path("evaluations").rglob("*.yaml")); [yaml.safe_load(p.read_text(encoding="utf-8")) for p in fs]; print(len(fs))'
git diff --check
```

### Claim boundary and next task

Established: explicit common conformal-ratio upper bound, positive 4096-bit
gap and logarithmic-rate certificates, and fully numerical constants in the
same determinant's global quadratic exponential upper envelope.

Not established: exact conformal ratios, true growth type, lower growth,
sharp divisor asymptotics, arithmetic orbit weights, determinant roots,
functional equation, completed-`xi`, quantization, Route B,
Hilbert--P\'olya, or RH.

Next smallest task: audit whether one explicit nonzero coefficient or signed
trace term supports a cancellation-safe theorem-level lower bound on the same
determinant's maximum modulus. Return `NOT_TESTABLE` if no such mechanism is
mathematically explicit; do not compute determinant roots.

Recommended verdict: `GO_WITH_LIMITATIONS`.

## Current status — LOG-0001 quadratic growth and zero-free half-plane

Current clue: `CLUE-A1-004`.

Candidate ID: `LOG-0001` (formal candidate).

- Evaluation source commit: `33986f9633b7f03f2fcc1f6ab914e5e0d69f7050`
- HP-Dynamics research commit: `ec00bcb`
- Shared standalone paper-stage mirror commit: `d5ab4b42e66b357859f3b4de560ea5d02bdcf86d`
- Source lock: `configs/source_locks/LOG-0001-GROWTH-ORDER.yaml`
- Route-A evaluation: `evaluations/route_a/LOG-0001/20260808T104049Z.yaml`
- Formal theorem: `formal/results/log_0001_growth_order.md`
- Analytic Route-A tuple:
  `(A1_WEAK, A2_ANALYTIC_DETERMINANT,
  A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)`
- Riemann-target tuple: `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`
- Overall/scoped verdict: `ROUTE_A_EXPLORATORY / GO_WITH_LIMITATIONS`
- Route-B tuple: all `NOT_INVOKED`; invocation is not authorized
- Shared mirror target:
  `hilbert-polya-structure/logistic_dynamics/projects/exact_uc_polar_growth_order/`

The determinant is unchanged:

\[
D_{\rm pol}(s)=\det_{\rm Fr}(I-\mathcal L_s|_B),
\qquad
B=\ker[v_L(0)-v_R(0)].
\]

Normalize Riemann maps from the unit disk to the two frozen outer stadiums and
write `r=max(r_L,r_R)<1` for the proof-only inner-domain ratios. The Taylor
factorization groups directly on `B` into two geometric rank-one streams,
one for each input branch. A principal minor of order `q` is bounded by
`q^(q/2)` times the product of its rank-one norms, while the two-stream
elementary symmetric sum has the quadratic decay

\[
C_r^2(q+1)W(s)^q r^{q^2/4-q/2},
\qquad
W(s)\leq e^{0.824|s|}.
\]

Continuity of the canonical Grothendieck determinant in any frozen
`p`-nuclear ideal with `p<2/3` therefore gives

\[
|D_{\rm pol}(s)|
\leq \exp\!\bigl(C_0+C_1(1+|s|)^2\bigr).
\]

Hence the classical entire-function order is at most two. Jensen's formula,
applied with an outer circle of twice the counted radius and the zero-free
anchor below, gives `O(R^2)` zeros in disks and `O(T^2)` zeros in every fixed
real strip through height `T`.

The exact real inverse-derivative maximum is

\[
\alpha_0=\frac{U_c^2}{4},
\qquad
\tau_*=\log\frac4{U_c^2}.
\]

The signed all-word trace ledger implies absolute convergence of the actual
`lambda=1` trace logarithm whenever

\[
\Re s>
\frac{\log2}{\log(4/U_c^2)}
=1.3382657903899534315\ldots.
\]

Thus `D_pol` has no zeros in that open half-plane. Every closed
sub-half-plane above the threshold has uniform upper and lower modulus bounds,
and `D_pol(s)->1` uniformly in imaginary height as `Re(s)->+infinity`.

### Strongest evidence

- The growth proof uses the same matching-space determinant, not a finite
  matrix, reciprocal zeta, or separately glued ledger.
- The direct matching-space expansion has exactly two streams and the sharper
  exponent `q^2/4-q/2`; an adversarial review checked the stream count,
  determinant limit, sign convention, trace-log disk, and Jensen radius.
- The target-free 100-digit certificate validates `alpha_0`, `tau_*`, the
  zero-free threshold, the safe line `Re(s)=2`, `||ell||<0.824`, and every
  two-stream allocation through `q=24`.
- Focused suite: `7/7 passed`.
- Full repository suite: `251/251 passed`.

### Strongest failure

The theorem supplies only upper bounds. It does not prove exact order two, a
lower growth bound, a sharp fixed-strip divisor asymptotic, or a `T log T`
law. It neither establishes nor excludes the Riemann--von Mangoldt regime.
There is still no log-prime/von-Mangoldt orbit law, functional equation,
completed-`xi` divisor, natural quantization, or Route-B object. No Fredholm
or Riemann roots were computed.

### New reusable knowledge

For a finite number of geometric nuclear streams with parameter weights
`exp(O(|s|))`, the determinant coefficients acquire Gaussian decay in rank,
which yields an `exp(O(|s|^2))` global envelope. A positive roof lower bound
separately yields a bounded zero-free closed sub-half-plane through the exact
signed trace ledger. Neither theorem alone gives a sharp divisor asymptotic.

### Updated files

- `configs/source_locks/LOG-0001-GROWTH-ORDER.yaml`
- `evaluations/route_a/LOG-0001/20260808T104049Z.yaml`
- `formal/results/log_0001_growth_order.md`
- `experiments/log_0001_growth_order.py`
- `artifacts/log_0001_growth_order/growth_order_certificate.json`
- `tests/test_log_0001_growth_order.py`
- `docs/candidate_registry.md`
- `docs/obstruction_registry.md`
- `docs/research_clues.md`
- `docs/research_log.md`
- `HP_HANDOFF.md`
- `CHANGELOG.md`

`docs/operator_obligations.md` remains unchanged because A4 fails and Route B
is not authorized.

### Reproduction commands

```bash
python3 experiments/log_0001_growth_order.py \
  --quiet \
  --output artifacts/log_0001_growth_order/growth_order_certificate.json
python3 -m unittest -v tests/test_log_0001_growth_order.py
python3 -m unittest discover -s tests -p 'test_*.py'
git diff --check
```

### Claim boundary and next task

Established: same-object order at most two, `O(T^2)` disk/fixed-strip divisor
upper bounds, an explicit zero-free right half-plane, and uniform modulus
bounds on every closed sub-half-plane above the threshold.

Not established: arithmetic orbit weights, determinant roots, exact order,
lower or sharp divisor asymptotics, completed-`xi`, target zeros, quantization,
Route B, Hilbert--P\'olya, or RH.

Next smallest task: certify explicit numerical upper bounds for the normalized
conformal restriction ratios `r_L,r_R` of the frozen stadium pair. Do not
compute determinant roots.

Recommended verdict: `GO_WITH_LIMITATIONS`.

## Previous checkpoint — LOG-0001 nuclear Fredholm determinant

Current clue: `CLUE-A1-004`.

Candidate ID: `LOG-0001` (formal candidate).

- Evaluation source commit: `b80900c60044795d2e163edc16de7ed1389e0cd9`
- HP-Dynamics research commit: `e3358c3a90ec67c2f1cf8b883107ad0fcf3cc64a`
- Shared mirror commit: `e6cf4f21b5d82adaec40cb542d952cf491a0b909`
- Source lock: `configs/source_locks/LOG-0001-NUCLEAR-FREDHOLM.yaml`
- Route-A evaluation: `evaluations/route_a/LOG-0001/20260808T051519Z.yaml`
- Analytic Route-A tuple:
  `(A1_WEAK, A2_ANALYTIC_DETERMINANT,
  A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)`
- Riemann-target tuple: `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`
- Overall/scoped verdict: `ROUTE_A_EXPLORATORY / GO_WITH_LIMITATIONS`
- Route-B tuple: all `NOT_INVOKED`; invocation is not authorized
- Shared mirror target:
  `hilbert-polya-structure/logistic_dynamics/projects/exact_uc_polar_nuclear_fredholm/`

The frozen object is the exact-$U_c$ polar transfer family on

\[
X=A(U_L)\oplus A(U_R),
\qquad
B=\ker[v_L(0)-v_R(0)].
\]

The radius-`3/5000` stadiums are proof-only intermediate domains inside the
unchanged radius-`1/1000` operator domains. An explicit Riemann-map/Taylor
expansion proves that every block, the full ambient family, and its matching
restriction are nuclear of order zero. The family is locally bounded and
entire in every $p$-nuclear ideal for `0<p<=1`.

Because $\mathcal L_s(X)\subset B$, relative to
$X=B\oplus\mathbb Ce$,

\[
\mathcal L_s=
\begin{pmatrix}\mathcal L_{s,B}&b_s\\0&0\end{pmatrix}.
\]

Hence matching introduces no half or doubled factor, and

\[
\Delta(\lambda,s)
=\det_{\rm Fr}(I-\lambda\mathcal L_{s,B})
\]

is a canonical jointly entire Grothendieck Fredholm determinant. In
particular, $D_{\rm pol}(s)=\Delta(1,s)$ is entire. For every $n\ge1$,

\[
\operatorname{Tr}\mathcal L_s^n
=\sum_{\omega\in\{L,R\}^n}
\frac{e^{-sT_\omega}}
     {1-\varepsilon_\omega e^{-T_\omega}},
\qquad
\varepsilon_\omega=(-1)^{\#R(\omega)}.
\]

The block paths use an explicit reverse-order bijection to these based words.
Distinct rotations are retained when distinct, and the `1/n` trace-log factor
gives the correct repetition coefficient.

### Strongest evidence

- The nuclear expansion is explicit; compactness is not substituted for
  nuclearity.
- The complemented matching identity exactly equates ambient and matching
  traces/determinants.
- An adversarial proof review passed after the block-word index was corrected.
- A target-free 100-digit regression passes all 510 based words of lengths
  one through eight: fixed point, strict itinerary, contraction, cyclic
  transport, signed denominator, and pure-left boundary checks all pass.
- Focused suite: `6/6 passed`; full suite: `244/244 passed`.

### Strongest failure

No log-prime/von-Mangoldt primitive-orbit law, growth-order or high-height
divisor theorem, functional equation, Gamma/trivial-zero ledger,
completed-$\xi$ divisor, natural quantization, or target-zero result exists.
Fredholm and Riemann zeros were not computed.

### New reusable knowledge

Compact inclusion between the frozen disk algebras admits an order-zero
Taylor nuclear factorization. A complemented matching kernel preserves an
ambient nuclear determinant when the operator range lies in that kernel.
Neither fact supplies arithmetic orbit weights or a target divisor.

### Updated files

- `configs/source_locks/LOG-0001-NUCLEAR-FREDHOLM.yaml`
- `evaluations/route_a/LOG-0001/20260808T051519Z.yaml`
- `formal/results/log_0001_nuclear_fredholm.md`
- `experiments/log_0001_nuclear_fredholm.py`
- `artifacts/log_0001_nuclear_fredholm/nuclear_fredholm_certificate.json`
- `tests/test_log_0001_nuclear_fredholm.py`
- `docs/candidate_registry.md`
- `docs/obstruction_registry.md`
- `docs/research_clues.md`
- `docs/research_log.md`
- `HP_HANDOFF.md`
- `CHANGELOG.md`

`docs/operator_obligations.md` is unchanged because A4 fails and Route B is
closed.

### Reproduction commands

```bash
python3 experiments/log_0001_nuclear_fredholm.py \
  --quiet \
  --output artifacts/log_0001_nuclear_fredholm/nuclear_fredholm_certificate.json
python3 -m unittest -v tests/test_log_0001_nuclear_fredholm.py
python3 -m unittest discover -s tests -p 'test_*.py'
git diff --check
```

### Claim boundary and next task

Established: full matching-space order-zero nuclearity, the canonical jointly
entire same-object determinant, conjugation symmetry, and the exact signed
all-power based-fixed-point trace.

Not established: arithmetic orbit weights, determinant growth/divisor count,
completed-$\xi$, target zeros, quantization, Route B, Hilbert--Pólya, or RH.

Next smallest task: prove an intrinsic high-imaginary-height divisor-count
regime or strict growth-order bound for $D_{\rm pol}(s)$ without target-zero
comparison.

Recommended verdict: `GO_WITH_LIMITATIONS`.

## Previous checkpoint — CLUE-A1-004 exact-U_c local boundary trace

Current clue: `CLUE-A1-004`.

Audit ID: `P4-LOGISTIC-UC-POLAR-BOUNDARY-TRACE` (non-candidate).

- Formal candidate: `false`
- Current HP commit: `5642bd7`
- Shared mirror commit: `99b5713` on `git@github.com:maris205/hilbert-polya-structure.git`
- Source lock: `configs/source_locks/P4-LOGISTIC-UC-POLAR-BOUNDARY-TRACE.yaml`
- Route-A evaluation: `evaluations/route_a/P4-LOGISTIC-UC-POLAR-BOUNDARY-TRACE/20260807T071000Z.yaml`
- Route-A tuple: `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`
- Scoped verdict: `REVISE` / `GO_WITH_LIMITATIONS`
- Route B: inactive and not authorized

For the unique boundary periodic point `P=-pi/2`, put

\[
\alpha_0=\phi_L'(P)=\frac{U_c^2}{4}
=0.5957439419765593735\ldots.
\]

The exact local weighted-composition traces are

\[
\operatorname{Tr}T_{s,L}
=\frac{\alpha_0^s}{1-\alpha_0},
\qquad
\operatorname{Tr}_P T_{s,L}^n
=\frac{\alpha_0^{ns}}{1-\alpha_0^n}.
\]

There is no half-weight and no doubled/matching factor: `P` is interior to the
complex stadium and belongs only to the left component. The right inverse germ
at target `P` is not fixed.

### Evidence and tests

- Exact polynomial reduction proves the endpoint graph and
  `alpha_0=U_c^2/4 in (0,1)`.
- The frozen compact inclusion makes the single weighted composition nuclear
  of order zero on `A(U_L)`.
- Target-free Taylor traces were checked at powers 1--4,
  `s=0,1/2,1,2+i`, and cutoffs 4,8,16,32,64; maximum exact-tail residual is
  below `2e-101` at 100 digits.
- Focused suite: `6/6 passed`.

### Claim boundary

Established: the unique local boundary trace and all pure-left powers.

Not established: nuclearity of the full two-component matching-space family,
a full Fredholm determinant, arithmetic orbit law, completed-xi structure,
quantization, Route B, Hilbert--Polya, or RH.

### Next smallest task

Prove nuclearity of the full two-component weighted family on the frozen
matching space. Do not evaluate Fredholm zeros first.

## Previous checkpoint — CLUE-A1-004 exact-U_c polar partition trace ledger audit

Current clue: `CLUE-A1-004`.

Audit ID: `P4-LOGISTIC-UC-POLAR-PARTITION-TRACE` (non-candidate).

- Formal candidate: `false`
- Audit state: `PROVED_HALF_OPEN_GEOMETRIC_LEDGER_REVISE_TRACE`
- HP source commit before this checkpoint: `0e6152d8b477cb7c75cc3648e62ce18ed094031c`
- Current HP commit: `1f236c404e3a549dc639cf4d616cc8dfae846c67`
- Shared mirror commit: `15da669` on `git@github.com:maris205/hilbert-polya-structure.git`
- Source lock: `configs/source_locks/P4-LOGISTIC-UC-POLAR-PARTITION-TRACE.yaml`
- Route-A evaluation: `evaluations/route_a/P4-LOGISTIC-UC-POLAR-PARTITION-TRACE/20260807T032000Z.yaml`
- Route-A tuple: `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`
- Scoped verdict: `REVISE` / `GO_WITH_LIMITATIONS`
- Route B: inactive and not authorized

### Frozen ledger

The exact parameter is the unique real root

\[
U_c^3-2U_c^2+2U_c-2=0,
\]

with no use of the rounded legacy literal. The geometric half-open partition is

\[
I_L^{\rm ho}=[-\pi/2,0),
\qquad
I_R^{\rm ho}=[0,\pi/2].
\]

The doubled labels `0_L` and `0_R` remain distinct for branch coding, but the
geometric projection identifies them and assigns the partition point to `R`.
The exact boundary graph is

\[
P=-\pi/2\mapsto P,
\qquad Q=\pi/2\mapsto P,
\qquad Z=0\mapsto Q.
\]

Thus `0` is preperiodic, not a boundary periodic orbit. The target-free
certificate passes half-open disjointness, cyclic rotation, endpoint-copy swap,
signed orientation, and matching-range checks through symbolic word length 8.

### Important trace boundary

The geometric quotient rule counts one canonical half-open cyclic lift per
geometric partition-hit orbit. This is not yet an analytic trace identity.
Matching at zero only proves that the weighted-family range lies in the
matching kernel. Conditionally, if a later nuclear extension exists, the block
form `[[L_B,*],[0,0]]` gives `Tr_X(L^n)=Tr_B(L_B^n)`; it does not halve the
source-branch cyclic sum. A toy rank-one matrix confirms this. No universal
`2^h` endpoint factor is allowed.

### Strongest evidence

The endpoint graph is exact from the critical polynomial identities, and the
partition point has no periodic boundary cycle. The half-open ledger is now
explicit and reproducible without prime/zero data.

### Strongest failure

The local analytic trace correction at the boundary fixed point `P=-pi/2`
remains open. Nuclearity, Fredholm determinant existence, divisor comparison,
quantization, Route B, and RH claims remain closed.

### Updated files

- `configs/source_locks/P4-LOGISTIC-UC-POLAR-PARTITION-TRACE.yaml`
- `experiments/p4_logistic_uc_polar_partition_trace.py`
- `artifacts/p4_logistic_uc_polar_partition_trace/partition_trace_certificate.json`
- `formal/results/exact_uc_polar_partition_trace.md`
- `tests/test_p4_logistic_uc_polar_partition_trace.py`
- `evaluations/route_a/P4-LOGISTIC-UC-POLAR-PARTITION-TRACE/20260807T032000Z.yaml`
- `docs/research_clues.md`
- `docs/candidate_registry.md`
- `docs/research_log.md`
- `HP_HANDOFF.md`

### Tests and reproduction

```bash
python3 experiments/p4_logistic_uc_polar_partition_trace.py \
  --quiet \
  --output artifacts/p4_logistic_uc_polar_partition_trace/partition_trace_certificate.json
python3 -m unittest -v tests/test_p4_logistic_uc_polar_partition_trace.py
```

### Next smallest task

Derive the local matching-space trace correction at `P=-pi/2` under this lock,
or stop the Logistic branch. Do not open nuclearity or Fredholm zeros before
that identity. The project-level breadth rule still keeps the structurally
different Hénon/QG branches separate; this is a candidate-local Logistic
resume task only.

## Previous checkpoint — CLUE-A3-001 same-ledger annular residual audit

Current clue: `CLUE-A3-001`.

Candidate ID: none. Non-candidate audit ID:
`LEGACY-ANNULAR-RESIDUAL-001`.

- Formal candidate: `false`
- Audit state: `DEFINED_NOT_TESTABLE`
- HP source commit: `e1a2934f506c5d65a1649c0020511ca5e4442eb0`
- Legacy source commit: `2d01633de0bcf0ecd1310291e2547cff417e13a0`
  (RH-371)
- Source lock:
  `configs/source_locks/LEGACY-ANNULAR-RESIDUAL-001.yaml`
- Route-A evaluation:
  `evaluations/route_a/LEGACY-ANNULAR-RESIDUAL-001/20260806T140210Z.yaml`
- Route-A tuple: `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`
- Overall Route A: `ROUTE_A_EXPLORATORY` as a diagnostic only
- Scoped verdict: `NOT_TESTABLE`
- Standalone-candidate verdict: `STOP_SCOPED`
- Route-B tuple:
  `(NOT_INVOKED, NOT_INVOKED, NOT_INVOKED, NOT_INVOKED, NOT_INVOKED)`
- Route B: inactive and not authorized

### Source lock

For the folded noisy quadratic-map operator `K_sigma`, set

\[
A_\sigma=K_\sigma/r_H,
\qquad r_H=17/20.
\]

After removing the Perron and negative-parity algebraic eigenvalues, put the
remaining eigenvalues of modulus at most `q=1/2`, with algebraic
multiplicity, on the normal diagonal realization `C_sigma`. The frozen direct
residual is

\[
g_\sigma(z)
=\sum_{n\ge2}\frac{\tau_{\sigma,n}-a_n}{n}z^n,
\qquad
\tau_{\sigma,n}=\operatorname{Tr}(C_\sigma^n).
\]

The sole determinant convention is

\[
D_{\sigma,\mathrm{tail},2}(z)=\det_2(I-zC_\sigma),
\qquad
g_\sigma=\log G_H-\log D_{\sigma,\mathrm{tail},2},
\]

with both logarithms zero at `z=0`. Thus `g_sigma` is not a determinant and
`exp(-g_sigma)=D_(sigma,tail,2)/G_H` is a ratio. `C_sigma` is an exact normal
spectral realization of the complementary factor, not a proved physical
invariant compression.

The Hardy normalization is frozen at

\[
R=7/5,
\qquad \rho=141/100,
\qquad
\rho_*=r_H\lambda=1.426787483864074\ldots.
\]

The definition uses all `n>=2`. RH-302's proof split alone uses
`m_sigma=ceil(4 log(1/sigma))`; it is not the physical first-alias clock. A
future numerical pre-audit, if actual compatible spectra become available,
is frozen to the baseline physical sequence `sigma_k=lambda^(-2k)` without
identifying `k`, `n`, or `m_sigma`.

### Route-A result

- `A1_WEAK`: the underlying noisy quadratic-map family is intrinsic and
  target-free, but this audit supplies no arithmetic primitive-orbit law,
  repetition weights, or complete orbit census.
- `A2_FAIL`: the complementary `det_2` factor and the residual sign are exact,
  but the residual is not a standalone determinant, the factor is not the full
  physical determinant, and no target divisor comparison is licensed.
- `A3_FAIL` / `NOT_TESTABLE`: RH-300 proves the conditional implication at
  every fixed `R<rho<rho_star`; at `rho=1.41`, its `H-infinity` and `H2`
  constants are `139.0070922` and `8.2924679`. RH-302 proves the tails vanish
  and reduces the problem to the moving head. The actual moving signed/complex
  coefficient stream and its annular norm are unavailable in the required
  physical-clock data type.
- `A4_FAIL`: `C_sigma` is an auxiliary normal realization, not a natural
  quantization; no same-clock unitary/scattering lift or HP operator domain is
  defined.

The latest legacy endpoint RH-371 is an independent capacity obstruction and
does not activate this route. The legacy handoff still labels RH-300 an
inactive annular criterion and retains route coordinate
`actual_same_clock_unnormalized_head_transport_open`. RH-354's normalized
selected tail cannot replace the raw `p=tau-a` ledger.

### Strongest evidence

The exact identity

\[
g_\sigma=\log G_H-log\det_2(I-zC_\sigma)
\]

fixes the data type and sign without primes or Riemann zeros. On the strict
radius `rho=1.41`, the certified annular criterion has positive margins on
both sides, and the slope-four noisy and deterministic tails vanish. This
reduces the entire A3 question to one explicit moving-head norm.

### Strongest failure

The repository contains earlier fixed-noise finite spectral snapshots, but
not the `q=1/2`-selected complementary spectrum/trace stream on the frozen
physical small-noise schedule with discretization, cutoff, precision, and
stopping controls. Fixed-order convergence, finite boundary grids, RH-354's
normalized tail, or substitution of full-trace/head/counterloop coefficients
cannot pay the all-order obligation.

### New reusable knowledge

An annular residual is a diagnostic layer, not automatically a new candidate.
Before any norm plot, freeze the physical complement, algebraic
multiplicities, `det_2` sign, Hardy norm, noise schedule, trace order, and
head/tail clock separately. A finite spectrum produced for another cutoff or
clock is not reusable merely because it comes from the same map.

### Updated files

- `configs/source_locks/LEGACY-ANNULAR-RESIDUAL-001.yaml`
- `evaluations/route_a/LEGACY-ANNULAR-RESIDUAL-001/20260806T140210Z.yaml`
- `docs/research_clues.md`
- `docs/candidate_registry.md`
- `docs/research_log.md`
- `HP_HANDOFF.md`

`docs/obstruction_registry.md` is unchanged because no new physical
obstruction was proved. `docs/operator_obligations.md` is unchanged because
Route B remains closed.

The ongoing shareable mirror is maintained at
`git@github.com:maris205/hilbert-polya-structure.git` under
`logistic_dynamics/`. Each result-bearing stage gets one self-contained paper
subproject; this audit does not open a manuscript because it adds no theorem
edge.

### Tests and reproduction

- Legacy focused suites: `39/39 passed`:
  RH-300 `4/4`, RH-302 `3/3`, RH-309 `5/5`, RH-311 `3/3`,
  RH-361 `20/20`, and Volume IV `4/4`.
- Outer full repository suite: `225/225 passed` (`63.548 s`).
- All 43 outer YAML files parse successfully.
- The nested legacy repository is clean at RH-371 commit `2d01633`.

```bash
python3 -m pytest -q -p no:cacheprovider \
  docs/related_programs/prime_dynamics_theory/papers/RH-300-annular-analytic-prefix-criteria/tests
python3 -m pytest -q -p no:cacheprovider \
  docs/related_programs/prime_dynamics_theory/papers/RH-302-annular-tail-moving-head-reduction/tests
python3 -m pytest -q -p no:cacheprovider \
  docs/related_programs/prime_dynamics_theory/papers/RH-309-endpoint-hardy-mismatch-barrier/tests
python3 -m pytest -q -p no:cacheprovider \
  docs/related_programs/prime_dynamics_theory/papers/RH-311-ten-layer-annular-mass-frontier-review/tests
python3 -m pytest -q -p no:cacheprovider \
  docs/related_programs/prime_dynamics_theory/papers/RH-361-ten-layer-signed-completion-and-upper-counterloop-review/tests
python3 -m pytest -q -p no:cacheprovider \
  docs/related_programs/prime_dynamics_theory/papers/RH-VOL4-noisy-head-annulus-signed-completion-synthesis/tests
python3 -m unittest discover -v
python3 - <<'PY'
from pathlib import Path
import yaml
files = list(Path('configs/source_locks').glob('*.yaml')) + list(Path('evaluations').rglob('*.yaml'))
for path in files:
    yaml.safe_load(path.read_text(encoding='utf-8'))
print(len(files))
PY
git diff --check
```

### Claim boundary

Established: the explicit target-free residual object, exact same-ledger
`det_2` ratio identity, all clocks and Hardy normalizations, the strict-radius
conditional theorem, vanishing-tail reduction, and precise data-availability
boundary.

Not established: actual moving-head or full annular convergence, a physical
compression realizing `C_sigma`, a primitive arithmetic orbit law, a
completed-xi determinant/divisor, a functional equation, target counting law,
quantization, Route B, Hilbert--Polya, or RH.

### Next smallest task

Stop this clue under `NOT_TESTABLE`. Reopen only when the repository gains an
actual same-ledger `q=1/2` complementary spectrum or `tau_(sigma_k,n)` stream
on `sigma_k=lambda^(-2k)`, with frozen discretization, cutoff, precision, data
split, and stopping controls, or when a proof of the `H2(1.41)` moving-head
limit is supplied. Then test that one norm without refitting.

Recommended verdict: `NOT_TESTABLE`.

## Previous checkpoint — QG-0001 relative Fredholm closure

Current clue: `CLUE-A4-003`.

Candidate ID: `QG-0001`; subaudit ID:
`QG-0001-RELATIVE-FREDHOLM-001`.

- Formal candidate: `true`
- Candidate state: `STOP_SCOPED`
- Source commit: `b5ad4c9ce4305cf055a2e6a3ae957ba4fda7e90b`
- Source lock: `configs/source_locks/QG-0001-RELATIVE-FREDHOLM.yaml`
- Route-A evaluation:
  `evaluations/route_a/QG-0001/20260806T123946Z.yaml`
- Analytic Route-A tuple:
  `(A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_UNITARY_OR_SCATTERING_CANDIDATE)`
- Target interpretation:
  `(A1_WEAK, A2_FAIL, A3_FAIL, A4_UNITARY_OR_SCATTERING_CANDIDATE)`
- Overall Route A: `ROUTE_A_REJECTED`
- Route-B tuple: `(NOT_INVOKED, NOT_INVOKED, NOT_INVOKED, NOT_INVOKED, NOT_INVOKED)`
- Recommended verdict: `STOP_SCOPED`
- Route B: inactive and not authorized

### Source lock

The object is the same frozen direct-sum magnetic Laplacian

\[
H=\bigoplus_{n\geq1}H_n,
\qquad H_n\simeq n^2H_1,
\]

in raw wavenumber `k=sqrt(lambda)`. The only opened determinant is

\[
D_H(k)=\det_F(I-k^2H^{-1})
=\det_{\rm rel}(H-k^2,H).
\]

It is normalized by `D_H(0)=1` and uses all components/eigenvalues. Numerical
controls use frozen `N=8,16,32,64,128,256`, samples
`k=0.11,0.25,0.5,0.731`, and 80 digits. Prime/zero tables, target fitting,
spectral rescaling, clock changes, standalone counterphase products, and
mixing with orbit Euler, bond-block, heat-zeta, or completed-xi ledgers are
forbidden.

### Route-A result

- `A1_WEAK`: the prior signed primitive prefix remains exact through period
  six, but no log-prime period law or primitive-orbit identity for the new
  determinant exists.
- `A2_ANALYTIC_DETERMINANT` analytically, but `A2_FAIL` as a Riemann target:

  \[
  H^{-1}\in\mathfrak S_1,
  \qquad
  \chi_0(k)=\det_F(I-k^2H_1^{-1}),
  \]

  \[
  \boxed{
  D_H(k)=\prod_{n\geq1}\chi_0(k/n)
  =\det_F(I-k^2H^{-1}).
  }
  \]

  The product converges normally. In `k` it has genus one, order one, and
  infinite type; in `k^2` it has genus zero and order one-half.
- `A3_PARTIAL_ANALYTIC_STRUCTURE` analytically, but `A3_FAIL` for the target:
  the zeros are `+/-n*sqrt(lambda_j(H_1))`, with coincidence multiplicities
  added, and

  \[
  N_H(K)=\frac{L_0}{\pi}K\log K+O(K).
  \]

  The leading coefficient is larger than the Riemann-von Mangoldt coefficient
  by

  \[
  2L_0=2+2\sqrt2+2\sqrt3+2\sqrt5
  =12.764664694883524\ldots.
  \]

  No zero-free factor can repair this divisor.
- `A4_UNITARY_OR_SCATTERING_CANDIDATE`: the determinant belongs to the same
  natural self-adjoint operator, clock, domain, and boundary conditions, but
  this cannot rescue the failed target divisor. Route B remains closed.

### Strongest evidence

Trace-class scaling gives

\[
\operatorname{Tr}(H^{-1})
=\zeta(2)\operatorname{Tr}(H_1^{-1})
=7.24356536914368571711\ldots,
\]

and trace-norm block convergence proves the infinite determinant identity.
The implementation reproduces the factorwise bond-phase identity below
`1.06e-81`; the leading-tail-corrected `N=128 -> 256` product drift is below
`3.18e-9` at every frozen sample.

### Strongest failure

`OBR-013` is decisive for the frozen object: its actual Fredholm divisor has
the wrong immutable leading count. Separately, `OBR-012` still blocks the
naive primitive-orbit and direct-sum bond products, and no von-Mangoldt trace
identity exists.

### New reusable knowledge

For any positive compact metric-graph base of total length `L` with exact
`1/n` scaling, the inverse-Laplacian relative determinant has
`N(K)=(L/pi)K log K+O(K)`; completed-xi divisor matching therefore requires
the necessary condition `L=1/2` before any target data are inspected. A valid
inverse-spectral determinant does not repair a distinct divergent orbit
product.

### Updated files

- `configs/source_locks/QG-0001-RELATIVE-FREDHOLM.yaml`
- `experiments/qg_0001_relative_fredholm.py`
- `artifacts/qg_0001/relative_fredholm.json`
- `formal/results/qg_0001_relative_fredholm.md`
- `formal/obstructions/harmonic_graph_tower_divisor_coefficient.md`
- `tests/test_qg_0001_relative_fredholm.py`
- `evaluations/route_a/QG-0001/20260806T123946Z.yaml`
- `docs/candidate_registry.md`
- `docs/obstruction_registry.md`
- `docs/research_clues.md`
- `docs/research_log.md`
- `HP_HANDOFF.md`
- `CHANGELOG.md`

`docs/operator_obligations.md` is unchanged because Route B remains closed.

### Tests and reproduction

- Relative-Fredholm focused suite: `8/8 passed` (`3.175 s`).
- Parent QG focused suites: `16/16 passed` (`1.170 s`).
- Full repository suite: `225/225 passed` (`63.813 s`).
- All 41 YAML files parse; `git diff --check` passed.

```bash
python3 experiments/qg_0001_relative_fredholm.py \
  --quiet \
  --output artifacts/qg_0001/relative_fredholm.json
python3 -m unittest -v tests/test_qg_0001_relative_fredholm.py
python3 -m unittest -v \
  tests/test_qg_0001_base_characteristic.py \
  tests/test_qg_0001_harmonic_magnetic_tower.py
python3 -c 'import yaml; p="evaluations/route_a/QG-0001/20260806T123946Z.yaml"; d=yaml.safe_load(open(p,encoding="utf-8")); print(d["a2"]["verdict"], d["a3"]["verdict"], d["overall_verdict"], d["route_b_invocation_allowed"])'
sha256sum artifacts/qg_0001/relative_fredholm.json \
  experiments/qg_0001_relative_fredholm.py \
  configs/source_locks/QG-0001-RELATIVE-FREDHOLM.yaml \
  formal/results/qg_0001_relative_fredholm.md \
  formal/obstructions/harmonic_graph_tower_divisor_coefficient.md \
  tests/test_qg_0001_relative_fredholm.py
python3 -m unittest discover -v
git diff --check
```

Hashes:

```text
86feb67502ed814f4cb44a99a04615950e762aca7bcdcf4552d70c925d9f5afc  artifacts/qg_0001/relative_fredholm.json
9c20e150292765d92c304f2defedf2dccd6704480c5bdc04a9ad4bff54c99672  experiments/qg_0001_relative_fredholm.py
1d36f5bbbfa4015a5e17ceff57bd28787b423bd84021d899afe837f7eb244b0c  configs/source_locks/QG-0001-RELATIVE-FREDHOLM.yaml
9dbeb4f45bda1a1656efd6454352482281e6ba16e2686997f28e39229f962caf  formal/results/qg_0001_relative_fredholm.md
6758c9dda29b6c3c3287895952f56b328f237eaf092c913e2b260ca1fa39e531  formal/obstructions/harmonic_graph_tower_divisor_coefficient.md
890637a85a4fe39647b47ec56748a83b4e6059e2d73328128237d3d344ae8531  tests/test_qg_0001_relative_fredholm.py
550885625aefaf1f416374e61c484f1ad6eea99d53e1ef72bc5a8347fb866767  evaluations/route_a/QG-0001/20260806T123946Z.yaml
```

### Claim boundary

Established: a genuine same-operator trace-class Fredholm determinant, exact
component product and counterphase, complete divisor/multiplicity ledger,
trace coefficient, entire growth, counting law, and strict frozen
divisor-coefficient obstruction.

Not established: a primitive-orbit trace identity, log-prime/von-Mangoldt
weights, completed-xi functional equation or divisor, Route B,
Hilbert--Polya, or RH.

### Next smallest task

QG-0001 has no candidate-local continuation under its current lock. Apply the
RH breadth-first rule: inspect the legacy RH handoff for `CLUE-A3-001` and
freeze exactly one explicit same-ledger annular residual object before
creating or evaluating a formal candidate. Do not import a prior zero fit or
mix residual clocks.

Recommended verdict: `STOP_SCOPED`.

## Previous checkpoint — QG-0001 base-component characteristic audit

Current clue: `CLUE-A4-003`.

Candidate ID: `QG-0001`; subaudit ID:
`QG-0001-BASE-CHARACTERISTIC-001`.

- Formal candidate: `true`
- Candidate state: `ANALYTIC_REVIEW`
- Source commit: `af41439b609a5dfb863931ed1e56a0598de5f003`
- Source lock: `configs/source_locks/QG-0001-BASE-CHARACTERISTIC.yaml`
- Route-A evaluation:
  `evaluations/route_a/QG-0001/20260806T111927Z.yaml`
- Route-A tuple:
  `(A1_WEAK, A2_FAIL, A3_FAIL, A4_UNITARY_OR_SCATTERING_CANDIDATE)`
- Overall Route A: `ROUTE_A_EXPLORATORY`
- Route-B tuple: `(NOT_INVOKED, NOT_INVOKED, NOT_INVOKED, NOT_INVOKED, NOT_INVOKED)`
- Scoped verdict: `GO_WITH_LIMITATIONS`
- Route B: inactive and not authorized

### Source lock

Only the n=1 component is audited. The 6-by-6 sinc-matching matrix uses
`(u_L,u_R,q_0,q_1,q_2,q_3)` and the raw wavenumber `k`; `sin(k*ell)/k` is
defined as `ell` at zero. Its determinant `C_phys(k)` is entire and even.
The parent bond convention is retained only for the exact comparison

\[
\Delta_{\rm bond}(k)=-\frac43 k^2e^{ikL_0}C_{\rm phys}(k),
\qquad L_0=1+\sqrt2+\sqrt3+\sqrt5.
\]

No tower Euler/Fredholm/relative determinant, heat-zeta promotion, target fit,
prime/zero table, or Route B step is authorized by this local lock.

### Route-A tuple

- `A1_WEAK`: the prior signed primitive/repetition ledger through period six
  is unchanged; no arithmetic orbit law is supplied.
- `A2_FAIL`: exact matching gives

  \[
  C_{\rm phys}(0)=A=\sqrt2+\sqrt3+\sqrt5+\sqrt6+\sqrt{15}+3\sqrt{10}>0.
  \]

  The bond zero at zero is exactly double and spurious. After removing the
  scalar and phase,
  \(\chi_0(k)=1-4.4035597019537134\ldots k^2+O(k^4)\); this is a base
  prerequisite, not a global determinant.
- `A3_FAIL`: no tower divisor, functional equation, correct coefficient, or
  completed-xi identity exists.
- `A4_UNITARY_OR_SCATTERING_CANDIDATE`: the same parent clock and magnetic
  scattering convention are preserved; Route B remains closed.

### Strongest evidence

The sinc matrix is finite at `k=0` and at individual edge-Dirichlet points,
while the exact bond identity is reproduced with maximum residual below
`1.53e-80` at four frozen samples, including `k=pi`. The Dirichlet terminal
proves the positive physical gap independently.

### Strongest failure

The result is local to one finite component. It neither supplies convergence
of a tower product nor a prime-power trace formula, and the parent naive tower
product remains blocked by `OBR-012`.

### New reusable knowledge

Use a sinc-matching determinant as the physical characteristic at zero; do not
use cotangent/cosecant poles or individual sine factors as eigenvalue tests.
The raw normalized bond factor has first nonconstant coefficient `i*L0`; the
explicit counterphase `exp(-i*k*L0/n)` leaves the even component characteristic
`chi_0(k/n)`. This is the precise local ledger for a possible genus-one
relative product.

### Updated files

- `configs/source_locks/QG-0001-BASE-CHARACTERISTIC.yaml`
- `experiments/qg_0001_base_characteristic.py`
- `artifacts/qg_0001/base_characteristic_zero.json`
- `formal/results/qg_0001_base_characteristic_zero.md`
- `tests/test_qg_0001_base_characteristic.py`
- `evaluations/route_a/QG-0001/20260806T111927Z.yaml`
- `docs/candidate_registry.md`
- `docs/research_clues.md`
- `docs/research_log.md`
- `HP_HANDOFF.md`
- `CHANGELOG.md`

`docs/operator_obligations.md` is unchanged because Route B remains closed.

### Tests and reproduction

- Base-characteristic focused suite: `8/8 passed` (`0.899 s`).
- Parent QG focused suite: `8/8 passed`.
- Full repository suite after adding this subaudit: `217/217 passed` (`60.914 s`).
- YAML parse and `git diff --check`: passed.

```bash
python3 experiments/qg_0001_base_characteristic.py \
  --quiet \
  --output artifacts/qg_0001/base_characteristic_zero.json
python3 -m unittest -v tests/test_qg_0001_base_characteristic.py
python3 -m unittest -v tests/test_qg_0001_harmonic_magnetic_tower.py
python3 -c 'import yaml; p="evaluations/route_a/QG-0001/20260806T111927Z.yaml"; d=yaml.safe_load(open(p,encoding="utf-8")); print(d["a2"]["verdict"], d["a2"]["metrics"]["bond_zero_order_at_k0"], d["route_b_invocation_allowed"])'
sha256sum artifacts/qg_0001/base_characteristic_zero.json \
  experiments/qg_0001_base_characteristic.py \
  configs/source_locks/QG-0001-BASE-CHARACTERISTIC.yaml \
  formal/results/qg_0001_base_characteristic_zero.md \
  tests/test_qg_0001_base_characteristic.py
git diff --check
```

### Claim boundary

Established: the exact entire base physical characteristic, positive value at
zero, exact order-two spurious bond zero, leading coefficient, raw linear
phase, and dephased normalized Taylor coefficient.

Not established: a global tower determinant or convergence theorem, arithmetic
trace weights, completed-xi divisor, Route B, Hilbert--Pólya, or RH.

### Next smallest task

Freeze one explicit same-operator genus-one relative component product using
`chi_0(k/n)` and `exp(-i*k*L_0/n)`. Prove convergence and compatibility with
the direct-sum operator before any divisor comparison; keep it separate from
the naive orbit product and heat/spectral zeta.

Recommended verdict: `GO_WITH_LIMITATIONS`.

## Previous checkpoint — QG-0001 harmonic magnetic graph-tower prefilter

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

---

# COPRIME-0001 scalar continuation and endpoint closure (2026-08-10)

## Current clue

`CLUE-A1-009` / `COPRIME-0001` was audited after the exact countable trace
ledger. The original object remains

```text
(L_s)_{mn}=1_{gcd(m,n)=1}(mn)^(-s/2),  n,m>=2,
D_cop(s)=det_F(I-L_s),  Re(s)>1.
```

No prime table, zero table, determinant value, or fitted parameter was used.

## New reusable theorem edge

The squarefree Mobius lift

```text
L_s=V_s M V_s^T,
C_s=V_s^T V_s M=zeta(s)T_s-P_1,
T_s(d,e)=mu(e)[d,e]^(-s)
```

has

```text
||H_s||_{S_2}^2=prod_p(1+3*p^(-2*Re(s))),  H_s(d,e)=[d,e]^(-s).
```

Therefore

```text
D_tilde(s)=det_2(I-C_s)
```

is a holomorphic scalar representation on `Re(s)>1/2, s!=1` and equals the
original Fredholm determinant on `Re(s)>1` because `Tr(C_s)=0` there. This is
an explicitly named continuation representation, not an extension of the
original bounded counting-measure `ell^2` operator.

## Strict endpoint obstruction

For real `s>1`, temporarily add label one and use finite prime-coordinate
compressions. The local rank-two kernel has

```text
alpha_p^+/-=(1 +/- sqrt((1+3*p^(-s))/(1-p^(-s))))/2,
alpha_p^+(s)>=1+p^(-s).
```

Euler divergence and min--max show that every fixed positive eigenvalue index
of the original codimension-one compression eventually exceeds one as
`s downarrow 1`. At `s=3`, the exact trace-class bound gives
`||L_3||<9/16<1`. Spectral continuity therefore produces infinitely many
distinct positive real zeros

```text
s_j downarrow 1,  D_cop(s_j)=0.
```

No zero was searched for or located. The accumulation proves that the scalar
determinant has no holomorphic or meromorphic germ through `s=1`. The
punctured continuation and endpoint obstruction are separate ledgers.

## Route-A checkpoint

```text
analytic tuple:       (A1_WEAK, A2_ANALYTIC_DETERMINANT,
                       A3_CONTROLLED_CONTINUATION, A4_FAIL)
Riemann-target tuple:  (A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
scoped verdict:        STOP_SCOPED
Route B:               not invoked
```

## Updated files

- `configs/source_locks/COPRIME-0001-SCALAR-BOUNDARY.yaml`
- `evaluations/route_a/COPRIME-0001/20260810T034453Z.yaml`
- `experiments/coprime_0001_scalar_boundary.py`
- `artifacts/coprime_0001/scalar_boundary_certificate.json`
- `formal/results/coprime_0001_scalar_boundary.md`
- `formal/obstructions/coprime_scalar_endpoint_accumulation.md`
- `tests/test_coprime_0001_scalar_boundary.py`
- `docs/candidate_registry.md`
- `docs/obstruction_registry.md`
- `docs/research_clues.md`
- `docs/research_log.md`
- `CHANGELOG.md`

## Verification

Focused scalar-boundary suite: `7/7 passed`.

```bash
python3 experiments/coprime_0001_scalar_boundary.py \
  --quiet \
  --output artifacts/coprime_0001/scalar_boundary_certificate.json
python3 -m unittest -v tests/test_coprime_0001_scalar_boundary.py
```

## Claim boundary and next smallest task

Established: a target-free punctured scalar continuation representation and a
strict endpoint zero-accumulation obstruction at `s=1`.

Not established: prime-orbit/von-Mangoldt weights, completed-xi structure,
functional equation, target divisor law, quantization, Route B, Hilbert--Polya,
or RH.

Next smallest task: park COPRIME-0001. Reopen only with a new source-locked
determinant or function space; do not search roots or compare Riemann zeros.

# TH-0001 on-shell caustic incidence audit (2026-08-10)

## Current clue

`CLUE-A4-001`; candidate `TH-0001` remains in `ANALYTIC_REVIEW`.

The source lock is
`configs/source_locks/TH-0001-PHASE-CAUSTIC-REAL.yaml`, and the versioned
Route-A evaluation is
`evaluations/route_a/TH-0001/20260810T074238Z.yaml`.

## Result

For the frozen ordered phase

\[
\Phi=S_{1/2}(q_0,q_1)+S_{3/2}(q_1,q_2)+S_{5/2}(q_2,q_3),
\]

the stationary equations intersect the caustic `15*q1*q2=1` in the exact real
family

\[
q_1=t\ne0,\quad q_2=\frac1{15t},\quad
q_0=1-\frac32t^2-\frac1{15t},\quad
q_3=1-t-\frac1{90t^2}.
\]

The endpoint projection Jacobian is exactly minus the internal Hessian. At
`t=1`, the rational canonical trajectory is

```text
(q0,q1,q2,q3)=(-17/30,1,1/15,-1/90)
(p0,p1,p2,p3)=(-289/1800,-17/30,1,1/15)
```

and all six three-kick residuals vanish. The Hessian has rank one, with null
direction `(-1,3)` and third directional derivative `132 != 0`.

## Route-A checkpoint

```text
analytic tuple:       (A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)
Riemann-target tuple: (A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
scoped verdict:       GO_WITH_LIMITATIONS
Route B:              not invoked and not authorized
```

This is a physical/on-shell strengthening of `OBR-011`, not a new independent
obstruction. It does not construct a multi-chart phase/Maslov ledger and does
not authorize determinant, spectrum, root, or Route-B work.

## Verification

```bash
python3 experiments/th_0001_phase_caustic_real.py --quiet \
  --output artifacts/th_0001/phase_caustic_real_audit.json
python3 -m unittest -v tests/test_th_0001_phase_caustic_real.py
```

Focused audit suite: `7/7 passed`.

## Claim boundary and next smallest task

Established: exact on-shell caustic parameterization, singular endpoint
projection identity, rational canonical witness, rank-one regularity witness,
and the strengthened `OBR-011` scope.

Not established: multi-chart phase/Maslov transitions, arithmetic orbit law,
determinant, spectrum, trace formula, Route B, Hilbert--Pólya, or RH.

Next smallest task: stop this sub-audit. Reopen only with a new source lock
fixing explicit multi-chart phase/Maslov transition rules, or pivot
breadth-first to a structurally different candidate.

# Current checkpoint — CLUE-A4-002 countable bouquet prefilter (2026-08-10)

## Current clue

`CLUE-A4-002`; no formal candidate ID is allocated.  The audit identifier is
`SS-PREFILTER-IRRATIONAL-BOUQUET-001`.

## Source lock and object

`configs/source_locks/SS-PREFILTER-IRRATIONAL-BOUQUET.yaml` freezes the
countable disjoint suspension

\[
\Sigma=\bigsqcup_{n\ge2}\mathbb Z/n\mathbb Z,
\quad \sigma(n,j)=(n,j+1),
\quad \tau_n=1+\sqrt2/n,
\quad \phi_n=-n,
\]

and the single determinant ledger

\[
D_{\rm bouquet}(s)=\det_{\rm F}(I-\mathcal L_s)
=\prod_{n\ge2}(1-e^{-n^2-s(n+\sqrt2)}).
\]

No prime/zero/USTC/GUE data, numerical root search, fitted clock, or affine
rescaling is allowed.  This is deliberately a pre-candidate control and does
not consume `SS-0003`.

## Route-A checkpoint

```text
analytic tuple:       (A1_WEAK, A2_ANALYTIC_DETERMINANT,
                       A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)
Riemann-target tuple: (A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
scoped verdict:       STOP_SCOPED
overall:              ROUTE_A_REJECTED
Route B:              not invoked and not authorized
```

The exact block ledger has one primitive `n`-cycle per component and

\[
\operatorname{tr}(\mathcal L_s^k)
=\sum_{n\mid k,\,n\ge2}n e^{-kn-sk(1+\sqrt2/n)}.
\]

The determinant is entire and its zeros are
\[
s_{n,k}=-(n^2+2\pi i k)/(n+\sqrt2).
\]

The real lines decrease to `-infinity`, so each bounded vertical strip has
`N(T)=O(T)`.  The global period set is incommensurate, but the base is
disconnected and not mixing; this supplies no arithmetic orbit law.

## Strongest evidence and failure

Strongest evidence: exact same-object Fredholm factorization, trace-class
entire family, primitive/repetition ledger, and closed-form divisor theorem.

Strongest failure: `OBR-016` — superexponentially escaping cycle actions force
linear fixed-strip divisor growth, incompatible with the completed-xi
`Theta(T log T)` regime.  The object is a reusable negative structural prior,
not a formal candidate.

## Verification

```bash
python3 experiments/ss_prefilter_irrational_bouquet.py \
  --n-max 12 \
  --output artifacts/ss_prefilter_irrational_bouquet/audit.json
python3 -m unittest -v tests/test_ss_prefilter_irrational_bouquet.py
```

Focused suite: `7/7 passed`.

## Claim boundary and next smallest task

Established: target-free countable object, exact determinant and repetition
ledger, and `O(T)` fixed-strip divisor obstruction.

Not established: prime correspondence, connected/mixing renewal dynamics,
completed-xi equality, quantization, Route B, Hilbert--Pólya, or RH.

Next smallest task: do not promote `SS-0003`.  If `CLUE-A4-002` is reopened,
freeze one connected or renewal non-Selberg object whose cycle actions remain in
a fixed critical strip, then repeat the bounded A1/A2 prefilter without target
data.  Otherwise park this clue and return to breadth selection.
