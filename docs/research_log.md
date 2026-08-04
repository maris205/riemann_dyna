# HP-Dynamics Research Log

## 2026-08-02 — First Route-A run

### Repository audit

- The repository was synchronized with `origin/main` at commit
  `278f707eeaa12a7836a4621d5d1cd5aa2f24df1c` before research changes.
- The two project skills are installed under `.agents/skills/`, while several
  core documents still referenced the obsolete `skills/` path.
- Required first-run storage was missing: `configs/source_locks/`,
  `evaluations/route_a/`, `experiments/`, `artifacts/`, `tests/`, and this log.
  The directories needed for the active evaluation were created.
- Recommended but non-blocking files/directories remain absent or inconsistent:
  `AGENTS.md`, `CHANGELOG.md`, `src/`, `formal/`, `reports/`, and the archived
  plan filename described in the README. These were not fabricated during the
  clue evaluation.
- `docs/related_programs/prime_dynamics_theory/` and
  `docs/prior_work/legacy/` remain separate Git repositories and were preserved.

### Current clue

`CLUE-A1-002` — the one-dimensional model is a mod-2 projection rather than a
complete host; test the smallest extension with mod-3 residue memory.

### Candidate and source lock

`SS-0001` is the constant-roof suspension over the edge shift of
`Cay(Z/6Z,{+1,-1})`, with zero potential and determinant convention

\[
D(s)=\det(I-e^{-s}A).
\]

The complete source lock is `configs/source_locks/SS-0001.yaml`.

### Route-A result

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
overall: ROUTE_A_REJECTED
candidate state: STOP_SCOPED
Route B: not authorized
```

Strongest positive result: the finite-state lift contains nontrivial mod-3
character modes without reading a prime table, and its primitive-orbit census
is exact.

Strongest failure: the exact determinant

\[
(1-4e^{-2s})(1-e^{-2s})^2
\]

has a divisor consisting of finitely many vertical arithmetic progressions,
with `O(T)` zero counting rather than the required `Theta(T log T)` behavior.

### Reproduction commands

Final verification passed `14/14` focused control tests and `46/46` repository
tests. Regenerating the JSON artifact produced a byte-identical file; both YAML
files parsed successfully and `git diff --check` passed.

```bash
git status --short --branch
git pull --rebase origin main
python3 -m unittest -v tests/test_ss_0001_mod6_cayley.py
python3 experiments/ss_0001_mod6_cayley.py --max-period 24 --output artifacts/ss_0001/route_a_baseline.json
```

### Claim boundary

Established only for `SS-0001`: finite residue memory is present, while the
constant integer clock and finite determinant have the wrong divisor geometry
and counting law. No result about countable-state shifts, unbounded roofs,
nuclear transfer operators, Route B, or the Riemann Hypothesis is claimed.

### Next smallest task

Prove the finite-state, finitely-valued locally constant positive-roof
generalization of the `O(T)` zero-count obstruction, including explicit scope
and reopening conditions.

### Same-day theorem closure

The next smallest task was completed in
`formal/obstructions/finite_state_finite_roof_zero_count.md`.

For a finite directed graph with fixed edge weights and positive locally
constant roofs, every entry of the finite transfer matrix is a finite
exponential sum. Expanding `det(I-L_s)` makes the determinant an entire
exponential polynomial of finite type. Jensen's formula gives `O(T)` zeros in
every bounded vertical strip, whereas the completed-`xi` divisor has
`Theta(T log T)` counting. A zero-free factor or fixed affine spectral map
cannot remove this mismatch.

The family-level obstruction is now recorded as `OBR-005`. `CLUE-A1-002` is
`BLOCKED` until an explicit countable-state, unbounded-roof,
non-locally-constant, or infinite-dimensional nuclear object is defined.
No new candidate ID is allowed before that object, clock, and determinant
convention are explicit.

---

## 2026-08-03 — SS-0002 countable-state reopening

### Repository synchronization

- `main` was synchronized with `origin/main` at source commit
  `934d85c82a8aae61ea9ac648f3d0241122cdb78e` before research edits.
- The active clue remained `CLUE-A1-002`; its exact reopening condition was an
  explicit countable-state or infinite-dimensional nuclear object outside
  `OBR-005`.
- Broken inline Markdown math delimiters in the existing
  `finite_state_finite_roof_zero_count.md` theorem were repaired without
  changing the theorem or its scope.

### Candidate and source lock

`SS-0002` is the paired-Gauss regular-holonomy Mayer operator for the
commutator cover

\[
\Gamma_{\rm com}
=[\operatorname{PSL}_2(\mathbb Z),
  \operatorname{PSL}_2(\mathbb Z)].
\]

Its paired inverse branches and frozen mod-six cocycle are

\[
\phi_{a,b}(z)=\frac{z+a}{b(z+a)+1},
\qquad
c(a,b)=a-b\pmod6.
\]

On \(\mathcal A(D_{3/2})\otimes\mathbb C^6\), the only determinant ledger is

\[
D_{\rm ab}(s)=\det_{\rm Fr}(I-\mathcal M_s)
=Z_{\Gamma_{\rm com}}(s).
\]

The full source lock is `configs/source_locks/SS-0002.yaml`. No prime table,
primality predicate, Riemann-zero table, fitted phase, or fitted normalization
is allowed.

### Route-A result

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)
overall: ROUTE_A_REJECTED
candidate state: STOP_SCOPED
Route B: not authorized
```

Strongest positive result: this is a genuine escape from `OBR-005`. It has
countably many branches, an infinite-dimensional nuclear operator, exact
regular-`C6` holonomy, nontrivial mod-three character modes, and a canonical
Laplace--Beltrami quantization.

Strongest failure: the same Fredholm determinant is a finite-area Selberg
zeta. The modular cuspidal spectrum lifts to the cover, giving at least

\[
N^+_{D_{\rm ab}}(T)\geq T^2/12+o(T^2),
\]

whereas completed `xi` has `Theta(T log T)` nontrivial-zero counting. The
area-`2*pi` cover has the stronger full two-sided resonance main term `T^2`.
This yields family obstruction `OBR-006`.

### Determinant-ledger audit

The modular scattering determinant is separate from the Mayer/Selberg
Fredholm determinant. Its completed-zeta ratio has zeros and poles and was not
used to cancel, complete, or modify `D_ab`. Such a gluing would violate
`OBR-001`.

### Reproduction commands

```bash
git status --short --branch
git pull --rebase origin main
python3 -m unittest -v tests/test_ss_0002_commutator_mayer.py
python3 experiments/ss_0002_commutator_mayer.py --output artifacts/ss_0002/route_a_structural_audit.json
```

### Claim boundary

Established: the countable-state/nuclear reopening is mathematically explicit,
and the direct finite-area modular Selberg subclass has the wrong divisor
growth. Not established: a rational-prime orbit clock, von-Mangoldt weights,
completed-xi determinant, Route-B result, Hilbert--Polya realization, or RH.

### Next smallest task

Do not create `SS-0003` from another finite-area Selberg cover. First define
one explicit non-Selberg countable-state or nuclear transfer object and prove
the zero-count regime permitted by its own Fredholm determinant, with no
separate scattering quotient or arithmetic-table lookup.

---

## 2026-08-03 — Legacy Logistic pre-candidate reopening

### Current clue

`CLUE-A2-005` — deterministic branch audit for the empirical spectrum of the
legacy non-autonomous Logistic construction.

No formal candidate ID was created. The legacy notebooks define only a fitted
finite-matrix eigenphase observable, not a primitive-orbit Zeta or Fredholm
determinant. The Route-A skill therefore classifies the present object as
`NOT_TESTABLE` rather than promoting it to `SS-0003`.

### Read-only legacy audit

The following separate-repository files were inspected without modification:

- `docs/prior_work/legacy/4-riemann_logistic/ablation_test.ipynb`;
- `docs/prior_work/legacy/4-riemann_logistic/micro_ustc_data_match.ipynb`;
- the epsilon-scan and macro-optimizer notebooks needed for parameter
  provenance.

The micro object is the occupation-weighted aggregate

\[
T_{ij}=\sum_n V_n(i)K_n(i,j)
\]

for a noisy, non-autonomous quadratic map. It erases the chronological order of
the transfer cocycle. The notebook then discards eigenvalue moduli, sorts
principal phases, and anchors the scale with the first Riemann zero.

Saved target-use audit:

- zero 1 fixes scale;
- zeros 2--6 select `epsilon=0.001916` and the displayed eigensolver trial;
- zero 20 is explicitly rewarded in the trial score;
- the macro schedule family uses the first 100 zeros;
- there is no honest legacy validation or sealed test.

The selected saved result has MAE `0.3494` on fitted zeros 2--6, retrospective
MAE `7.4162` on zeros 7--20, and `61.7317` on zeros 21--85.

### Normalization result

The legacy CSR line computes (B=TD^{-1}), while correct row normalization is
(Q=D^{-1}T). The exact identity

\[
B=DQD^{-1}
\]

shows that both matrices have the same exact eigenvalue multiset. The bug is
real for the Markov/eigenvector interpretation and numerical conditioning, but
it does not by itself create the reported phases.

### Target-free deterministic smoke profile

A reduced `128 bins x 1000 steps` profile preserved the legacy
`epsilon/dx=5.748` ratio and used no prime, zero or USTC data.

- fixed-start ARPACK at tolerance `1e-10` matched the dense top-40 spectrum to
  below `3.7e-10` and produced residuals below `3.8e-15`;
- five of the first six phase-ranked modes had modulus below `1e-3`;
- a half-bin partition shift moved the 13 resolved modes by median complex
  distance `0.00943`, 90th percentile `0.0883`, and maximum `0.15275`.

The solver can be deterministic on the reduced profile, but the legacy
low-phase level ordering is not yet a stable spectral observable.

### Route-A preassessment

```text
Candidate ID: none
Source locks: P4-LOGISTIC-LEGACY-AUDIT and P4-LOGISTIC-DETERMINISTIC-SMOKE
Route A: NOT_TESTABLE
Diagnostic tuple: (A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)
Route B: inactive and not authorized
Recommended verdict: REVISE
```

### Reusable knowledge

- destination-index normalization and row normalization are diagonally
  similar for the same occupation diagonal;
- repeated sparse eigensolver starts are not a physical ensemble;
- phase ranking must report modulus, residual and mode identity;
- occupation-aggregated cycles need not be chronological dynamical cycles;
- a fitted finite prefix is a regression benchmark, not determinant evidence.

### Reproduction commands

```bash
python3 -m unittest -v \
  tests/test_p4_logistic_legacy_audit.py \
  tests/test_p4_logistic_deterministic_smoke.py
python3 experiments/p4_logistic_legacy_audit.py \
  --output artifacts/p4_logistic_legacy/route_a_pre_candidate_audit.json
python3 experiments/p4_logistic_deterministic_smoke.py \
  --output artifacts/p4_logistic_legacy/deterministic_smoke_profile.json
```

### Claim boundary

Established only: a fitted low-prefix numerical observation, its data leakage
and solver-selection provenance, the exact normalization similarity identity,
and a reduced target-free partition/solver smoke test. Not established: a
blind zero match, primitive orbit structure, prime clock, dynamical determinant,
analytic continuation, natural quantization, Route B, Hilbert--Polya, or RH.

### Next smallest task

Run a medium-fidelity target-free profile with physical epsilon fixed. Save the
raw (T) matrix, freeze every eigensolver parameter, and track only
residual-certified eigenbranches across bins, steps and a half-bin partition
shift. Do not inspect new zero-match metrics until branch identities are frozen.

---

## 2026-08-03 — Logistic physical-epsilon medium checkpoint

### Current clue

`CLUE-A2-005` — frozen strong-layer eigenbranch robustness of the legacy
occupation-conditioned Logistic matrix.

Candidate ID: none. No formal candidate, Route-A evaluation YAML, obstruction
number, or operator obligation was created.

### Source lock

`P4-LOGISTIC-MEDIUM-PHYSICAL-EPSILON`, version 2:

- one frozen million-step schedule with
  `k=0.1185699450083701`, `u_c=1.543078787606443`;
- historically target-fitted physical `epsilon=0.001916`, used without reading
  a target table or reoptimizing it;
- `2048 bins x 100000 steps` reference;
- time prefixes `50000/100000/200000` from the same schedule;
- bin controls `1536/2048/3072` and a half-bin translated-domain stress
  control;
- mean-matched static `mu=1.544195814880148`, both schedule endpoints, and the
  legacy regression static control, all using their own density evolution;
- ARPACK `k=450`, `ncv=1200`, tolerance `1e-11`, maximum iterations `100000`,
  fixed ones and seed-17 starts;
- signed-complex matching with explicit unmatched support before phase ranking;
- no phase-to-height scale and no prime, zero, or USTC table access.

The lock revision from version 1 to 2 was documentation-only: it recorded the
already frozen initial state, kernel boundary rule, imaginary-part threshold,
matching cutoff, translated-domain geometry, runtime, and historical epsilon
provenance. No computational value or acceptance threshold changed.

### Route-A evaluation

```text
Route A status: NOT_TESTABLE
Diagnostic tuple: (A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)
Route B: inactive and not authorized
Empirical phase-observable verdict: STOP_SCOPED
```

There is still no chronological primitive-orbit ledger, dynamical Zeta,
Fredholm determinant, global analytic object, or natural lift. The scoped
verdict applies only to the frozen finite empirical-matrix phase observable.

### Numerical result

All mechanics gates passed:

- every sparse profile converged and returned all `450/450` requested Ritz
  values;
- mass, row-sum, residual, static-kernel identity, strong/moderate conjugacy,
  all-profile edge, `k=300/450`, fixed-start, (Q/B), raw round-trip, and
  repeat-hash gates passed;
- dense and sparse eigensolvers matched all 23 strong upper-half branches on
  the separate `256 bins x 5000 steps` anchor matrix; this does not compare
  those anchor branches with the four reference branches;
- the reference edge modulus at `k=450` was `0.00225768`;
- dynamic and mean-matched static raw hashes reproduced exactly as
  `1d739153...d6270` and `5b6e20f7...65f950`.

The reference had only 4 upper-half strong branches, below the frozen minimum
20. All four matched stably in each time and bin control, with median drifts:

- bins 1536: `0.003231`;
- bins 3072: `0.001999`;
- steps 50000: `0.006023`;
- steps 200000: `0.004890`.

The half-bin translated grid produced five strong branches. Four matched, only
three passed every stability gate, median/p90/max drift was
`0.028783/0.046071/0.051659`, maximum phase drift was `0.033001`, and
phase-rank median/max displacement was `1/1`. The all-profile stable survival
fraction was `0.75`, but the frozen phase-rank gate failed.

The median nearest-static normalized distance was `0.0009477`. The
dynamic/static margin median was `0.03789`, and none of the four branches
reached margin `1.5`. The strong branches therefore cannot be distinguished
from the preregistered static-parent spectra at the internal numerical scale.

### Reusable knowledge

- strong empirical branches can be cutoff- and solver-reproducible yet fail as
  a phase-level observable under a translated-domain stress control;
- identical-estimator static controls are essential: here they explain the
  dynamic strong spectrum more closely than the internal perturbation radius;
- weak ARPACK-edge truncation must not be promoted to a strong/moderate
  conjugacy failure;
- branch matching with dummies must enforce the distance cutoff inside the
  assignment objective, not discard over-cutoff pairs only after assignment;
- “target-free run” does not mean “target-independent model” when a frozen
  hyperparameter was historically fitted to target zeros.

This is a single-source-lock numerical failure, not a family theorem, so no new
entry was added to `docs/obstruction_registry.md`.

### Updated files

- `configs/source_locks/P4-LOGISTIC-MEDIUM-PHYSICAL-EPSILON.yaml`;
- `experiments/p4_logistic_medium_branch_audit.py`;
- `tests/test_p4_logistic_medium_branch_audit.py`;
- `artifacts/p4_logistic_medium/branch_audit.json`;
- `artifacts/p4_logistic_medium/raw/dynamic_reference_T.npz`;
- `artifacts/p4_logistic_medium/raw/static_mean_matched_T.npz`;
- `docs/prior_work/logistic_legacy_pre_audit.md`;
- `docs/research_clues.md`;
- `docs/research_log.md`;
- `HP_HANDOFF.md`.

### Tests and reproduction commands

Reference runtime: CPython `3.12.3`, NumPy `2.4.4`, SciPy `1.16.1`, Numba
`0.66.0`, llvmlite `0.48.0`.

```bash
python3 -m unittest -v tests/test_p4_logistic_medium_branch_audit.py
python3 experiments/p4_logistic_medium_branch_audit.py \
  --output artifacts/p4_logistic_medium/branch_audit.json \
  --raw-directory artifacts/p4_logistic_medium/raw \
  > /tmp/p4_logistic_medium_stdout.json
python3 -m unittest discover -v
git diff --check
```

### Claim boundary

Established: reproducible finite-matrix mechanics and a scoped negative result
for the frozen strong-layer phase observable at the registered cutoffs.

Not established: blind zero prediction, rejection of Logistic dynamics,
behavior of a future autonomous lift or chronological cocycle, primitive-orbit
structure, a dynamical determinant, analytic continuation, completed-`xi`
divisor equality, natural quantization, Route B, Hilbert--Polya, or RH.

### Next smallest task

The active observable is `STOP_SCOPED`, so no further task is authorized inside
`CLUE-A2-005`. Reopening requires a newly explicit autonomous lift or
chronological transfer-cocycle/Fredholm object with its own source lock.
Otherwise the next queued project task is the `CLUE-A2-001` synthetic
Euler-product positive control.

---

## 2026-08-03 — CTRL-0001 Route-A A2 positive control

### Current clue

`CLUE-A2-001` — validate the weighted dynamical-Zeta/Fredholm evaluator before
using numerical zero evidence from a new candidate.

`CTRL-0001` is an explicitly non-candidate control. It does not consume
`SS-0003`, does not read primes or Riemann zeros, and does not authorize Route B.

### Source lock and exact object

The source lock `configs/source_locks/CTRL-0001.yaml` was written before the
implementation and freezes

\[
\mathcal H=\ell^2(\{A_+,A_-,B,C\}\times\mathbb N_0),
\qquad
\mathcal L_s e_{c,n}=a_cq_c^ne^{-s}e_{c,n},
\]

with four rationally parameterized channels. The sole determinant convention is

\[
D(s)=\det_{\rm Fr}(I-\mathcal L_s)
=\prod_c\prod_{n\ge0}(1-a_cq_c^ne^{-s}).
\]

The reciprocal `1/D`, logarithmic derivative `D'/D`, exponential of a
truncated log series, and absolute-value ablation are separate ledgers.

After adversarial review, lock version 2 added only explicit formulas for
`D_N` and `D_K`, deterministic-holdout wording, and supplemental precision and
ledger audits. No mathematical object, channel constant, rectangle, primary
cutoff, match radius, or acceptance threshold changed.

The frozen open rectangle is

\[
-8/25<\Re s<17/25,
\qquad
|\Im s|<34/5,
\]

with exact post-discovery scoring counts total/core/upper/lower
`22/12/5/5` and minimum boundary clearance `0.07`.

### Route-A result

```text
control tuple:
(A1_WEAK, A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)
candidate interpretation:
(A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)
overall as a candidate: ROUTE_A_REJECTED
infrastructure control verdict: GO_WITH_LIMITATIONS
candidate-scope verdict: STOP_SCOPED
Route B: inactive and not authorized
```

The analytic trace-class statement and entire Fredholm determinant are exact.
The A2 numerical pipeline passes every frozen gate, but the object is engineered
and has no natural prime orbit or completed-xi target structure.

### Independent numerical paths

Root discovery uses q-binomial Fredholm coefficients in `z=exp(-s)` and then
enumerates every logarithm branch in the rectangle. Exact formula roots are
opened only afterward for one-to-one scoring. An independent Newton/trace
recurrence agrees through degree 24 with global scaled defect
`5.97e-13`; the coefficient conjugation defect through degree 32 is
`1.88e-13`.

Supplemental `K=28` mpmath recomputations at 50, 80, and 120 decimal digits
all find 22 roots. Maximum root drift is `4.35e-49` from 50 to 80 dps,
`8.62e-79` from 80 to 120 dps, and `5.41e-13` from complex128 to 120 dps.
The 120-dps truncation error against the exact scoring ledger remains
`8.89658e-9`, showing that the primary error is coefficient cutoff rather than
floating precision.

Argument-principle counting uses only the direct finite-mode product. Frozen
grid results are:

| points/edge | winding | max adjacent phase step |
|---:|---:|---:|
| 128 | 22 | 2.00839 |
| 256 | 22 | 1.11299 |
| 512 | 22 | 0.568995 |
| 1024 | 22 | 0.285756 |

The first two grids have the correct count but fail the `pi/3` phase-step gate;
only the successive 512/1024 pair is accepted.

This is a sampled numerical winding diagnostic, not a rigorous
interval-arithmetic certificate: endpoint phase increments and successive
refinement cannot exclude every possible between-sample loop. The exact root
ledger establishes the control truth; the sampler tests whether the numerical
pipeline reproduces it independently.

Coefficient cutoffs expose both count and identity failures:

| K | roots found | strict matches at `1e-4` | missing | extra | global max assignment error |
|---:|---:|---:|---:|---:|---:|
| 16 | 28 | 6 | 16 | 22 | `1.35492e-1` |
| 20 | 22 | 15 | 7 | 7 | `2.02999e-3` |
| 24 | 22 | 22 | 0 | 0 | `1.25037e-5` |
| 28 | 22 | 22 | 0 | 0 | `8.89663e-9` |
| 32 | 22 | 22 | 0 | 0 | `7.82564e-13` |

Mode cutoff `N=2` has winding 18; every frozen `N>=3` has winding 22. The
maximum relative contour-value drift from `N=40` to `N=48` remains
`8.46440e-7`, so root-count stability and determinant-value stability are
reported separately.

### Mandatory falsification controls

- deleting the conjugate `A_plus/A_minus, n=1` modes gives counts
  `18/10/4/4` and exactly `4 missing, 0 extra`;
- adding the frozen conjugate extra factors gives `26/14/6/6` and exactly
  `0 missing, 4 extra`;
- balanced deletion plus addition restores all counts to `22/12/5/5`, while
  the matcher still reports `4 missing, 4 extra`;
- replacing all complex channel weights by absolute values changes total
  winding to 30 and is rejected as a different determinant;
- at repetition four, the signed trace is `-0.33393858995368`, while the sum
  of absolute channel terms is `33.59028440713514`, for cancellation ratio
  `0.00994152`.

Executable determinant-ledger controls additionally give:

- `D` winding `+22`;
- `1/D` winding `-22`, recorded as 22 poles and no zeros;
- `D'/D` trapezoidal contour integrals `22.0000110` and `22.0000028` at
  512 and 1024 points per edge, plus local scaled residue approximately 1;
- winding zero for the order-four truncated-log exponential, which is
  analytically zero-free.

Every missing/extra/balanced/absolute injection contour also passes its own
frozen phase-step and integer-residual diagnostics.

The balanced control is the main reusable result: regional argument count is
necessary but cannot certify divisor identity without explicit missing/extra
matching.

### Updated files

- `configs/source_locks/CTRL-0001.yaml`;
- `experiments/ctrl_0001_qpochhammer.py`;
- `tests/test_ctrl_0001_qpochhammer.py`;
- `artifacts/ctrl_0001/route_a_positive_control.json`;
- `evaluations/route_a/CTRL-0001/20260803T171847Z.yaml`;
- `docs/candidate_registry.md`;
- `docs/research_clues.md`;
- `docs/research_log.md`;
- `HP_HANDOFF.md`.

No obstruction or operator-obligation entry was created. This control proves no
new candidate-family impossibility and opens no Route-B operator.

### Reproduction commands

```bash
python3 -m unittest -v tests/test_ctrl_0001_qpochhammer.py
python3 experiments/ctrl_0001_qpochhammer.py \
  --quiet \
  --output artifacts/ctrl_0001/route_a_positive_control.json
python3 -m unittest discover -v
git diff --check
```

### Claim boundary

Established: a deterministic, table-free A2 evaluator benchmark with exact
analytic determinant, independent root and winding implementations, explicit
cutoff failures, one-to-one missing/extra reporting, and signed-cancellation
falsification.

Not established: natural primitive dynamics, rational-prime correspondence,
von-Mangoldt weights, completed-xi functional equation or divisor, physical
quantization, self-adjointness, Route B, Hilbert--Polya, or RH.

Also not established: a rigorous interval or derivative-bound certificate for
the sampled winding path. This is the limitation attached to the control
verdict.

### Next smallest task

Before allocating `SS-0003`, define one explicit non-Selberg mathematical
object with its own intrinsic clock and same-object Fredholm determinant. Then
apply the `CTRL-0001` independent winding, cutoff, one-to-one matching, balanced
corruption, and signed-cancellation gates before interpreting any zero match.

---

## 2026-08-04 — Compact monotone-clock Logistic lift obstruction

### Active clue and source lock

The active clue was `CLUE-A1-004`, the proposed autonomous higher-dimensional
lift of the legacy non-autonomous Logistic schedule. No formal candidate ID was
allocated. The audit ID is

```text
P4-LOGISTIC-MONOTONE-CLOCK-LIFT
```

The source lock was written before the implementation at
`configs/source_locks/P4-LOGISTIC-MONOTONE-CLOCK-LIFT.yaml`. It excludes the
historically zero-fitted epsilon, empirical transition matrices, eigenphases,
best-of-seed selection, Riemann-zero and prime tables, USTC data, artificial
clock resets, and determinant-ledger mixing.

The legacy schedule constants are frozen solely as object provenance:

\[
k=0.1185699450083701,
\qquad
u_c=1.543078787606443,
\]

with

\[
\mu_1=1.5637,
\qquad
\mu_{10^6}=1.5437.
\]

No arithmetic target was scored.

### Frozen autonomous object

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

Starting at \(v_1=1/\log11\), the exact identity

\[
G^{n-1}(v_1)=\frac1{\log(n+10)}
\]

reproduces the frozen schedule. Since

\[
0<u_c\le u_c+kv^2\le1.5637<2,
\]

the fibre maps preserve `[-1,1]` and the lift is a well-defined autonomous
map on the declared compact phase space.

### Proved obstruction

For a general skew product

\[
F(y,b)=(f_b(y),g(b)),
\]

full-space periodic points must project to base periodic points. For the compact
clock,

\[
G^m(v)=\frac1{\log(e^{1/v}+m)}<v
\]

for every \(v>0\) and \(m\ge1\), while \(G^m(0)=0\). Therefore

\[
\operatorname{Fix}(F^m)
=
\operatorname{Fix}(f_{u_c}^m)\times\{0\},
\]

and likewise

\[
\operatorname{Prim}(F)
=
\operatorname{Prim}(f_{u_c})\times\{0\}.
\]

No periodic orbit visits the aging interior. The autonomous clock lift adds no
primitive-orbit data beyond the static limiting Logistic map.

Moreover,

\[
G'(0)=1,
\]

so every boundary orbit carries a neutral clock multiplier. A standard
hyperbolic stability factor containing `det(I-DF^m)` is degenerate in the clock
direction; silently removing that factor would change the determinant ledger.

This reusable theorem is registered as `OBR-007` and proved in
`formal/obstructions/strict_monotone_clock_orbit_collapse.md`.

### Determinant convention

The sole ledger is the reciprocal formal Artin--Mazur series

\[
Z_{\rm AM,F}(z)
=
\exp\left(
\sum_{m\ge1}\frac{\#\operatorname{Fix}(F^m)}m z^m
\right),
\qquad
D_{\rm AM,F}=Z_{\rm AM,F}^{-1}.
\]

The fixed-set theorem gives the exact formal identity

\[
D_{\rm AM,F}=D_{\rm AM,f_{u_c}}.
\]

This is not called a Fredholm determinant. No convergence, analytic
continuation, functional equation, root ledger, or completed-xi divisor is
asserted.

### Adversarial controls

- a point fixed by the first fibre map returns in `x` but not in the full
  `(x,v)` state;
- periodizing the clock at `P=8,32,64` makes step `P+1` reuse `mu_1`, so it no
  longer follows the frozen schedule;
- clamping at those cutoffs creates three different static parent parameters;
- the boundary parent is `u_c`, not the finite-window endpoint `1.5437` or the
  separate legacy regression value `1.543689`;
- all schedule, phase-space, fixed-set, ledger, modulo, clamp, and target-free
  gates passed.

The direct-versus-closed clock regression maximum error was
`1.1102230246251565e-16`; the short direct-versus-lifted trajectory regression
maximum error was zero in binary64. These are implementation checks, not the
proof basis.

### Route-A result

```text
(A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)
overall: ROUTE_A_REJECTED
audit verdict: STOP_SCOPED
formal candidate: false
Route B: inactive and not authorized
```

- `A1_FAIL / PROVED`: all primitive orbits are static boundary orbits;
- `A2_FAIL / PROVED`: the formal determinant reduces exactly to the static
  parent and the neutral multiplier blocks the usual hyperbolic weight;
- `A3_FAIL / NOT_TESTABLE`: no analytic determinant or global divisor exists;
- `A4_FAIL / NOT_TESTABLE`: no same-clock natural quantization, Hilbert space,
  or operator domain is defined, and the map is noninvertible.

### Updated files

- `configs/source_locks/P4-LOGISTIC-MONOTONE-CLOCK-LIFT.yaml`;
- `experiments/p4_logistic_monotone_clock_lift.py`;
- `tests/test_p4_logistic_monotone_clock_lift.py`;
- `artifacts/p4_logistic_monotone_clock_lift/structural_audit.json`;
- `formal/obstructions/strict_monotone_clock_orbit_collapse.md`;
- `evaluations/route_a/P4-LOGISTIC-MONOTONE-CLOCK-LIFT/20260804T025047Z.yaml`;
- `docs/candidate_registry.md` with an explicit non-candidate summary note;
- `docs/obstruction_registry.md`;
- `docs/research_clues.md`;
- `docs/research_log.md`;
- `HP_HANDOFF.md`.

The formal-candidate registry and operator-obligation ledger remain unchanged:
the object failed before candidate promotion and Route B was not authorized.

### Reproduction commands

```bash
python3 -m unittest -v tests/test_p4_logistic_monotone_clock_lift.py
python3 experiments/p4_logistic_monotone_clock_lift.py \
  --quiet \
  --output artifacts/p4_logistic_monotone_clock_lift/structural_audit.json
python3 -m unittest discover -v
git diff --check
```

### Claim boundary and next task

Established: exact schedule embedding, compact phase-space invariance,
full fixed-set and primitive-orbit collapse to the static limit slice, neutral
clock multiplier, formal determinant reduction, and failure of modulo/clamped
clock repairs.

Not established: an analytic/Fredholm determinant, intrinsic prime clock,
completed-xi structure, natural quantization, Route B, Hilbert--Polya, RH, or a
no-go theorem for every autonomous lift.

Next smallest task: define one intrinsic recurrent base with a nontrivial
periodic orbit that leaves the static-limit slice while genuinely reproducing
logarithmic aging, and freeze a nondegenerate same-object determinant before
any numerical zero comparison. No such object is presently defined, so this
branch stops at the scoped obstruction.
