# HP-Dynamics Handoff

## Current status — exact-(U_c) recurrent Logistic audit

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
