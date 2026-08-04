# HP-Dynamics Handoff

## Current status — exact-(U_c) first-return support closure

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
