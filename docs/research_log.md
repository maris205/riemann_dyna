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

---

## 2026-08-04 — Exact-(U_c) recurrent Logistic clock Route-A audit

### Current clue and candidate state

Current clue: `CLUE-A1-004`, autonomous higher-dimensional realization of the
Logistic slow schedule.

Candidate ID: none. The audit ID is

```text
P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK
```

and `formal_candidate: false`. The object is explicit enough for a versioned
Route-A audit but is not promoted to `SS-0003`, because its physical
first-return branch system and weights remain uncertified.

Evaluation source commit:

```text
95e72606c75e039ba3457a727e2d05377e35daf0
```

### Source lock

The exact parent is

\[
f_u(x)=1-ux^2,
\]

with (U_c) the unique real root of

\[
u^3-2u^2+2u-2=0.
\]

The frozen binary64 value and its critical orbit are

\[
U_c=1.5436890126920764,
\qquad
0\to1\to1-U_c\to U_c-1\to U_c-1.
\]

The rounded legacy literal lies on the left:

\[
1.543689-U_c
=-1.2692076278852937\times10^{-8}.
\]

The physical observable uses (L=\{x<0\}) and the first-return gap

\[
\tau_u(y)=\min\{n\geq1:f_u^n(y)<0\},\qquad y<0.
\]

First-return gaps are not primitive periodic orbits. The recurrent object is
an additional modeled tower

\[
\mathcal B
=\{(\omega,j):\omega\in\mathbb N_{\geq1}^{\mathbb Z},
1\leq j\leq2\omega_0\},
\]

with one symbol (m\geq1) for each modeled even label (L=2m). Equality of
this all-even envelope with the complete physical exact-(U_c) induced branch
system is an open interval/kneading obligation.

The fibre parameter is

\[
\mu(j,L)=U_c+k\left[
\frac1{\log^2(a_0+j)}-\frac1{\log^2(a_0+L)}
\right],
\]

with

```text
k = 6.764850551029437
offset = 100000
```

and exactly (j=1,\ldots,L) updates per block. The terminal branch returns
the frozen `U_C` directly, so

\[
\mu(L,L)=U_c
\]

bitwise before renewal. The inherited (k) has target-contaminated legacy
provenance and supplies no arithmetic evidence.

Training is empty. Validation uses frozen gaps `2,4,6,8,12,16`, periods 1--8,
and deltas (10^{-5},10^{-6}). The sealed tests use gaps
`10,14,18,24,32,64`, periods 9--16, delta (10^{-7}), rounded-(U_c), legacy
indexing, terminal-order, repetition, reorder, and source-scan controls. Prime
tables, primality predicates, prime-gap tables, Riemann zeros, xi/zeta target
evaluations, USTC data, and target-driven tuning are forbidden.

### Exact anchor and legacy timing correction

The old Model-4 compensation used `steps` as its endpoint, while the actual
last recorded update index is

\[
i_\star=W+N-1.
\]

For the production values (W=2{,}000{,}000) and
(N=10{,}000{,}000{,}000), the old terminal parameter is

```text
1.5436887783759317
```

and therefore reaches neither the rounded target nor the algebraic (U_c).
The legacy transition counter also keeps the pre-warmup source bin for the
first recorded edge. These are finite-window indexing defects; correcting
them does not by itself create recurrence.

### Left / center / right gap boundary

The frozen scan uses four initial states, burn-in `20000`, and `300000`
recorded updates for each parameter. Across every initial state and every
registered delta:

- the exact center has zero odd-gap count;
- every left control has zero odd-gap count;
- every right control has positive odd-gap count;
- the rounded `1.543689` control remains on the even left side.

The robust interpretation is an odd-gap channel opening to the right of
(U_c). It is not a composite-only mechanism: the new odd support generally
contains both primes and composites. All scanned Lyapunov exponents are
positive. Raw long-tail maxima and rare support pixels vary with seed, cutoff,
precision, and last-bit parameter changes, so they remain
`NUMERICAL_OBSERVATION` rather than a candidate definition.

The exact algebraic critical seed (x_0=0) is a degeneration control: its
postcritical orbit has one (L)-hit and no gap sequence. Gap statistics require
a frozen generic initial condition or a separately defined invariant measure.

### Recurrent tower and full-fibre lift

For one loop of every modeled even length,

\[
A(z)=\sum_{m\geq1}z^{2m}=\frac{z^2}{1-z^2},
\]

so the tower zeta and fixed counts are

\[
Z_T(z)=\frac{1-z^2}{1-2z^2},
\]

\[
\#\operatorname{Fix}(G^n)=0\quad(n\text{ odd}),
\qquad
\#\operatorname{Fix}(G^{2r})=2(2^r-1).
\]

Möbius inversion and direct cyclic-word enumeration agree through period 16,
giving 70 primitive tower orbits in the prefix. Repetitions are excluded and
cyclic rotations share one oriented orbit.

Every scheduled fibre map preserves `[-1,1]`, because

\[
U_c\leq\mu(j,L)<1.5947261217303264<2.
\]

For each primitive base orbit, the fibre return is a continuous self-map of
`[-1,1]`; it therefore has a fixed point. Base projection proves that each
witness is a primitive full-space orbit of the same physical period. All 70
prefix witnesses close with maximum residual

```text
3.7761460625063137e-14
```

and preserve signed multipliers and the repetition relation. This is one
witness per base orbit, not a complete fibre-root or multiplicity census.

### Determinant convention and new obstruction

The tower zeta is kept separate from the full reciprocal Artin--Mazur series

\[
D_{\rm AM,F}(z)
=\exp\left(-\sum_{n\geq1}\frac{\#\operatorname{Fix}(F^n)}n z^n\right).
\]

For every (n),

\[
N_G(n)\leq N_F(n)\leq2^nN_G(n)<4^n,
\]

so the full logarithmic series converges at least for (|z|<1/4). It is not a
Fredholm determinant, and no continuation is asserted.

`OBR-008` proves that any single-valued meromorphic continuation still of the
form (H(e^{-s})) is (2\pi i)-periodic and has only (O(T)) divisor count in
a bounded real strip. This is incompatible with the completed-ξ
(Theta(T\log T)) count. A zero-free prefactor cannot change the divisor.

### Route-A result

```text
Route-A tuple: (A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
Overall: ROUTE_A_EXPLORATORY
Recommended verdict: REVISE
Formal candidate: false
Route B: inactive and not authorized
```

- `A1_WEAK / CONDITIONAL_THEOREM`: exact primitive grammar and full lifts for
  the modeled tower, but no certified physical one-branch-per-even induced
  system, branch weights, log-prime clock, or von-Mangoldt amplitude.
- `A2_FAIL / PROVED`: exact tower zeta and local full Artin--Mazur ledger, but
  no same-object Fredholm determinant; the unit lattice divisor is obstructed.
- `A3_FAIL / PROVED`: `OBR-008` rules out completed-ξ growth for the frozen
  clock, while all other global analytic obligations remain absent.
- `A4_FAIL / NOT_TESTABLE`: no natural invertible/symplectic/scattering lift,
  Hilbert space, domain, or quantization is defined.

### Updated files

- `DERIVATION_PACKAGE.md`;
- `configs/source_locks/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK.yaml`;
- `experiments/p4_logistic_recurrent_uc_anchored_clock.py`;
- `tests/test_p4_logistic_recurrent_uc_anchored_clock.py`;
- `artifacts/p4_logistic_recurrent_uc_anchored_clock/structural_audit.json`;
- `formal/obstructions/unit_lattice_clock_vertical_periodicity.md`;
- `evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T080528Z.yaml`;
- `docs/research_clues.md`;
- `docs/candidate_registry.md`;
- `docs/obstruction_registry.md`;
- `docs/research_log.md`;
- `HP_HANDOFF.md`.

`docs/operator_obligations.md` remains unchanged because Route B is closed.

### Tests and reproduction commands

Focused result at this checkpoint:

```text
16/16 passed
```

Full repository result:

```text
73/73 passed
```

The regenerated structural artifact is byte-identical with SHA-256

```text
16fc53e17a56eb84e491abd12d927cb0644fae9e3a543b8a9b25ca06d77f41cf
```

Reproduction commands:

```bash
python3 -m unittest -v tests/test_p4_logistic_recurrent_uc_anchored_clock.py
python3 experiments/p4_logistic_recurrent_uc_anchored_clock.py \
  --quiet \
  --output artifacts/p4_logistic_recurrent_uc_anchored_clock/structural_audit.json
python3 -m unittest discover -v
python3 -c 'import yaml; paths=["configs/source_locks/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK.yaml","evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T080528Z.yaml"]; [yaml.safe_load(open(p,encoding="utf-8")) for p in paths]'
git diff --check
```

### Claim boundary and next smallest task

Established: exact algebraic (U_c), terminal-before-renewal anchoring,
target-free left/center/right odd-channel diagnostic, exact tower primitive
grammar, finite full-fibre witnesses, local full Artin--Mazur convergence, and
the unit-lattice vertical-periodicity obstruction.

Not established: complete physical return support, interval branches,
invariant weights, full fibre multiplicities, arithmetic prime correspondence,
von-Mangoldt trace law, Fredholm determinant, completed-ξ structure, natural
quantization, Route B, Hilbert--Pólya, or RH.

Next smallest task:

\[
S_{\rm top}=\{m:C_m\ne\varnothing\},
\qquad
C_m=L\cap\bigcap_{j=1}^{m-1}f^{-j}(I\setminus L)\cap f^{-m}(L).
\]

Prove or refute (S_{\rm top}=2\mathbb N) for exact (U_c) by interval or
kneading methods, and determine which branches have positive invariant weight.
Do not introduce a non-lattice roof until the same dynamics derives it without
prime or zero data.

---

## 2026-08-04 — Exact-(U_c) first-return support closure

### Current clue and candidate state

Current clue: `CLUE-A1-004`.

Candidate ID: none. The parent audit remains

```text
P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK
```

and the scoped support audit is

```text
P4-LOGISTIC-UC-FIRST-RETURN-SUPPORT
```

Both have `formal_candidate: false`. The versioned Route-A result is

```text
evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T105010Z.yaml
```

with source commit

```text
cd2ba4e7fabbcb5ace2466427a57e4d500eeaa27
```

### Source lock

Let

\[
f(x)=1-U_cx^2,
\qquad
U_c^3-2U_c^2+2U_c-2=0,
\qquad
\rho=U_c-1.
\]

The two return ledgers are frozen separately:

\[
X=[-1,1],
\qquad
J=f(X)=[-\rho,1],
\]

\[
L_X=[-1,0),
\qquad
L_J=[-\rho,0).
\]

For (D\in\{X,J\}), zero is a non-event and

\[
C_m(D)=L_D\cap
\bigcap_{j=1}^{m-1}f^{-j}(D\setminus L_D)
\cap f^{-m}(L_D).
\]

One (f)-iterate is one clock tick. The use of (T=f^2) in the proof does not
change the clock or the return labels. No determinant is added by this support
audit. Prime data, zero data, target arithmetic, USTC data, fitted weights, and
empirical transition matrices are forbidden.

The exact-rational reproduction certificate freezes a 100-decimal enclosure
of (U_c), 130-digit outward square-root bounds, the first 154 endpoint
intervals, and physical returns through 308. The independent midpoint
diagnostic uses 180 decimal digits through branch 64.

### Exact support theorem

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

Then (r_n\uparrow\rho) and the complete physical ledger is

\[
C_2(J)=(-r_1,0),
\]

\[
C_{2n}(J)=(-r_n,-r_{n-1}]\quad(n\ge2),
\qquad
C_{2n+1}(J)=\varnothing.
\]

Therefore

\[
S_{\rm top}^{J}=2\mathbb N_{\ge1},
\]

with exactly one nondegenerate interval branch for every even label. The only
nonreturning point of (L_J) is (-\rho).

For every (n),

\[
f^{2n}:\operatorname{int}C_{2n}(J)\longrightarrow(-\rho,0)
\]

is a real-analytic diffeomorphism. Therefore every finite word of positive
even return labels has a nonempty open cylinder. This proves the recurrent
tower's finite-word alphabet provenance, while leaving realization of every
infinite sequence, the full two-sided completion, its invariant measure, and
its aged fibre coupling as separate modeling choices.

On the literal ambient interval, define (q_n=-h(r_n)). Then

\[
C_1(X)=[-1,q_0),
\qquad
C_{2n+1}(X)=[q_{n-1},q_n)\quad(n\ge1),
\]

and these branches fill `[-1,-rho)`. Thus

\[
S_{\rm top}^{X}=\mathbb N_{\ge1}.
\]

This ambient/core distinction is mandatory. Since (f(X)\subset J), every
invariant probability gives (X\setminus J) zero mass. Hence every ambient odd
branch has zero invariant weight. Conditionally on the named physical acip
having support (J), every physical even branch has positive weight, but this
audit does not reprove that support theorem. The exact values are not computed,
and positivity is not measure-independent.

### Prior-work correction and obstruction

The old Paper-2 MSS proof interpreted its admissibility inequality in the
wrong direction. The parity conclusion is retained and strengthened by the
band-swap proof above.

The claimed uniformly expanding induced map is refuted. On the first branch,

\[
(f^2)'(x)=4U_c^2x f(x)\longrightarrow0
\qquad(x\uparrow0),
\]

and `x=-0.01` gives

```text
|(f^2)'(x)| = 0.0953043164222... < 1.
```

Every branch has derivative infimum zero, and the inverse Jacobian has a
square-root singularity at (-\rho). This creates `OBR-009`: the legacy Paper-2
ordinary-`BV` Lasota--Yorke/spectral-gap route does not establish the claimed
geometric branch-weight theorem. A weighted space, further acceleration, or a
direct physical-density theorem is required.

The endpoint-length ratio nevertheless has the proved limit

\[
\lambda=\frac{1}{4U_c^2(U_c-1)^2}
=0.35491084440177\ldots.
\]

If the physical density satisfies the explicit open hypothesis

\[
\frac{d\mu_{\rm ac}}{dx}(-\rho+t)
=C\,t^{-1/2}(1+o(1)),
\qquad C>0,
\qquad t\downarrow0,
\]

the branch-mass ratio would conditionally tend to

\[
\sqrt\lambda
=\frac{1}{2U_c(U_c-1)}
=0.59574394197656\ldots.
\]

This is recorded only as `OPEN_CONDITIONAL_CLUE`.

### Route-A result

```text
Route-A tuple: (A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
Overall: ROUTE_A_EXPLORATORY
Recommended verdict: REVISE
Formal candidate: false
Route B: inactive and not authorized
```

- `A1_WEAK / PROVED`: the physical one-even-label/one-full-interval grammar and
  full finite-word language are exact, and the recurrent tower retains its
  exact primitive combinatorics. The signed full-fibre residual ledger is a
  separately labeled finite numerical prefix. Exact acip weights, an
  arithmetic orbit correspondence, log-prime clock, and von-Mangoldt law are
  absent.
- `A2_FAIL / PROVED`: no first-return Fredholm operator is defined; `OBR-009`
  blocks the old ordinary-`BV` construction and `OBR-008` blocks every
  unit-lattice continuation as a completed-ξ divisor.
- `A3_FAIL / PROVED`: the unit-clock global count is incompatible with the
  completed-ξ count, while all positive analytic-structure obligations remain
  absent.
- `A4_FAIL / NOT_TESTABLE`: no natural quantization, Hilbert space, domain, or
  self-adjoint/scattering object is defined.

### Updated files

- `DERIVATION_PACKAGE.md`;
- `configs/source_locks/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK.yaml`;
- `configs/source_locks/P4-LOGISTIC-UC-FIRST-RETURN-SUPPORT.yaml`;
- `experiments/p4_logistic_recurrent_uc_anchored_clock.py`;
- `experiments/p4_logistic_uc_first_return_support.py`;
- `tests/test_p4_logistic_recurrent_uc_anchored_clock.py`;
- `tests/test_p4_logistic_uc_first_return_support.py`;
- `artifacts/p4_logistic_recurrent_uc_anchored_clock/structural_audit.json`;
- `artifacts/p4_logistic_uc_first_return_support/structural_audit.json`;
- `formal/results/exact_uc_first_return_support.md`;
- `formal/obstructions/exact_uc_first_return_nonuniform_expansion.md`;
- `evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T105010Z.yaml`;
- `docs/prior_work/README.md`;
- `docs/prior_work/claims_matrix.md`;
- `docs/research_clues.md`;
- `docs/candidate_registry.md`;
- `docs/obstruction_registry.md`;
- `docs/research_log.md`;
- `HP_HANDOFF.md`.

`docs/operator_obligations.md` remains unchanged because Route B is closed.

### Tests and reproduction commands

Focused support audit:

```text
16/16 passed
```

Focused recurrent audit:

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

Reproduction commands:

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

### Claim boundary and next smallest task

Established: exact physical and ambient return support, one full physical
branch per even label, the full finite-word return language, invariant-measure
annihilation of ambient odd branches, conditional physical branch positivity
under the named full-support-acip hypothesis, rational endpoint certification
through return 308, the recurrent tower's prior exact grammar, and `OBR-009`.

Not established: realization of every infinite return-label sequence or a
complete full-shift conjugacy, exact acip branch weights, their asymptotic
ratio, a repaired transfer-operator theorem, complete fibre multiplicities, an
arithmetic prime-orbit law, a non-lattice clock, Fredholm/completed-ξ structure,
natural quantization, Route B, Hilbert--Pólya, or RH.

Next smallest task: prove or refute the displayed physical-acip endpoint
density asymptotic and whether

\[
\frac{\mu(C_{2n+2})}{\mu(C_{2n})}
\longrightarrow
\frac{1}{2U_c(U_c-1)}.
\]

Freeze one of: a direct Misiurewicz density argument, a weighted/cusp-adapted
function space, or an accelerated inducing domain. Do not fit weights or add a
non-lattice roof before that choice is explicit.

## 2026-08-04 — exact-($U_c$) physical-acip endpoint theorem

### Stable checkpoint

Current clue: `CLUE-A1-004`.

Candidate ID: none. Parent audit and scoped theorem audit:

```text
P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK
P4-LOGISTIC-UC-ACIP-ENDPOINT-DENSITY
```

Source lock:
`configs/source_locks/P4-LOGISTIC-UC-ACIP-ENDPOINT-DENSITY.yaml`.
The physical map is `f(x)=1-U_c*x^2` on `J=[-(U_c-1),1]`, one `f`
iterate is one clock tick, `mu_ac(J)=1`, and `h=d mu_ac/dx`. The
conditional `T=f^2` density on `A=[-rho,rho]` is `g_A=2h`. The reflected
map and polar coordinate are proof objects only. No determinant or target
arithmetic data is admitted.

Route-A tuple:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
overall: ROUTE_A_EXPLORATORY
scoped endpoint verdict: GO_WITH_LIMITATIONS
parent audit verdict: REVISE
formal candidate: false
Route B: inactive and not authorized
```

Evaluation:
`evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T162511Z.yaml`.
Evaluation source commit:
`84111b3f436ed1e8111c871719e32b70a4def098`.

### Strongest evidence

For `T=f^2|_A` and `S=-T`, the coordinate `x=rho*sin(theta)` yields two
analytic full branches and

\[
\inf|G'|=\frac4{U_c^2}=2U_c(U_c-1)>1.
\]

All Jiang–Ruelle Markov/RPF hypotheses are checked, including the unique
nondegenerate critical point, finite postcritical orbit, primitive Markov
graph, polar/nonpolar endpoints, holomorphic inverse branches, and compact
containment. The resulting density is strictly positive and locally Lipschitz
at zero. Reflection and the two-band lift give the unique full-support
physical acip of `f`.

The physical Perron–Frobenius inverse branches prove

\[
h(-\rho+t)
=\frac{h(0)}{\sqrt2U_c}t^{-1/2}+O(1),
\qquad h(0)>0.
\]

The independently proved endpoint-length geometry then gives

\[
\frac{\mu_{\rm ac}(C_{2n+2})}{\mu_{\rm ac}(C_{2n})}
\longrightarrow
\frac1{2U_c(U_c-1)}
=\frac{U_c^2}{4}
=0.5957439419765593735\ldots.
\]

The structural audit independently compares the simplified polar derivative
with the raw chain rule, verifies both exact inverse branches at sealed
endpoint scales, certifies a 100-digit sign bracket for `U_c`, records input
hashes and environment metadata, and reproduces byte-identically through the
CLI. The Baladi–Smania cross-check uses corrected equation (1.1) in the 2023
supplement to arXiv:2008.01654v4.

### Strongest failure

No rigorous numerical enclosure for `h(0)` or exact finite-order physical
branch masses is available. The branch-mass theorem proves a ratio limit, not
the stronger legacy exponential-remainder formula. Return branches are not
arithmetic primitive periodic orbits, and no von-Mangoldt trace, intrinsic
non-lattice roof, s-dependent Fredholm determinant, global completed-xi
structure, or natural quantization exists.

`OBR-009` remains valid for the raw unaccelerated first-return operator. The
new density proof repairs the legacy mass-ratio conclusion but does not restore
the refuted ordinary-`BV` spectral gap. `OBR-008` still blocks the unit-lattice
determinant route.

### New reusable knowledge

A postcritical quadratic cusp at an exact Misiurewicz anchor can be removed by
a polar coordinate to obtain a uniformly expanding analytic Markov proof
object. This can certify local physical-density spikes and branch-mass
asymptotics while keeping the physical clock, normalization, and determinant
ledgers separate.

### Updated files

- `CHANGELOG.md`;
- `DERIVATION_PACKAGE.md`;
- `configs/source_locks/P4-LOGISTIC-UC-ACIP-ENDPOINT-DENSITY.yaml`;
- `docs/literature/exact_uc_acip_density_sources.md`;
- `docs/prior_work/README.md`;
- `docs/prior_work/claims_matrix.md`;
- `docs/research_clues.md`;
- `docs/candidate_registry.md`;
- `docs/obstruction_registry.md`;
- `docs/research_log.md`;
- `HP_HANDOFF.md`;
- `experiments/p4_logistic_uc_acip_endpoint_density.py`;
- `formal/results/exact_uc_acip_endpoint_density.md`;
- `formal/results/exact_uc_first_return_support.md`;
- `tests/test_p4_logistic_uc_acip_endpoint_density.py`;
- `tests/test_p4_logistic_uc_first_return_support.py`;
- `artifacts/p4_logistic_uc_acip_endpoint_density/structural_audit.json`;
- `evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T162511Z.yaml`.

`docs/operator_obligations.md` is unchanged because Route B remains closed.

### Tests

Focused endpoint audit: `10/10 passed`.

Endpoint plus first-return support audits: `26/26 passed`.

Full repository: `99/99 passed`.

Artifact SHA-256:

```text
ef015a2f1f4fc475c7daf8b87c1a2fedc75f35b8e76e151eb588b279eca53a8e  artifacts/p4_logistic_uc_acip_endpoint_density/structural_audit.json
```

### Reproduction commands

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

### Claim boundary

Established: the exact physical-acip endpoint spike, positivity and local
regularity at zero, physical full support, every physical even branch having
positive mass, and the asymptotic physical mass ratio.

Not established: an enclosure for `h(0)`, exact finite-order weights, an
exponential remainder/rate, an arithmetic primitive-orbit law, a viable
Riemann determinant, global analytic structure, quantization, Route B,
Hilbert–Pólya, or RH.

### Next smallest task

Use the uniformly expanding polar coordinate with a rigorously validated
finite-rank approximation to enclose `h(0)`, the absolute endpoint
coefficient, and selected finite branch masses. Freeze and separately report
discretization, truncation, rounding, normalization, and stopping errors. Use
no prime or zero data.

Recommended verdict: `REVISE`.

## 2026-08-04 — exact-$U_c$ polar-cone enclosure

Current clue: `CLUE-A1-004`.

The next smallest obligation after the endpoint theorem was to obtain an
absolute, target-free enclosure rather than quote the approximate collocation
value `h(0) ~= 0.2813`. The proof-coordinate Perron--Frobenius operator has
inverse contraction below `3/5` and logarithmic weight distortion below `3/10`.
Consequently the positive log-Lipschitz cone with slope `3/4` is invariant,
because

```text
3/10 + (3/5)*(3/4) = 3/4.
```

Normalization on `[-pi/2,pi/2]`, followed by the explicit `g_A=2h` ledger,
gives the following coarse certified intervals:

```text
w(0) in [0.1668010108790061, 0.5418010108790061]
h(0) in [0.1533974450330445, 0.4982637116356998]
C_h=h(0)/(sqrt(2)*U_c) in [0.0702656899853137, 0.2282361579437252]
```

The endpoint calculation is strengthened from an unspecified `O(1)` to

```text
|h(-rho+t)-C_h*t^(-1/2)| <= 61/100,  0 < t <= 1/200.
```

Integrating this bound over exact rational endpoint intervals certifies
positive absolute masses for returns `12,14,16,18`. The pi bracket is checked
by the exact rational Machin identity and alternating-series remainder bounds;
the root bracket and branch endpoint recursion are inherited from the sealed
support audit.

The six required categories are explicit: discretization (not used),
truncation (not used), rounding, normalization, iteration stopping (not used),
and resolvent/tail (not used because the cone is a direct bound). Auxiliary
rows separately record inverse-branch evaluation, the absent finite-rank
projection and invariant-vector residual, and the integrated endpoint
remainder. This is a local density theorem only. It does not certify a sharp
Ulam value, a finite-rank resolvent, an exponential branch-mass remainder, a
primitive-prime orbit law, or any determinant.

Route-A result remains `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`, scoped verdict
`GO_WITH_LIMITATIONS`, parent verdict `REVISE`; Route B remains inactive.

Artifacts:

- `configs/source_locks/P4-LOGISTIC-UC-ACIP-CONE-ENCLOSURE.yaml`
- `formal/results/exact_uc_acip_cone_enclosure.md`
- `experiments/p4_logistic_uc_acip_cone_enclosure.py`
- `tests/test_p4_logistic_uc_acip_cone_enclosure.py`
- `artifacts/p4_logistic_uc_acip_cone_enclosure/certified_bounds.json`
- `evaluations/route_a/P4-LOGISTIC-UC-ACIP-CONE-ENCLOSURE/20260804T233200Z.yaml`

Reproduction:

```bash
python3 experiments/p4_logistic_uc_acip_cone_enclosure.py \
  --quiet \
  --output artifacts/p4_logistic_uc_acip_cone_enclosure/certified_bounds.json
python3 -m unittest -v tests/test_p4_logistic_uc_acip_cone_enclosure.py
```

The focused audit passes `12/12`; the full repository passes `111/111`.
Artifact SHA-256:

```text
c0933c7a9df45f38fb403541aab7643e4e1f771bf7c277e4d144b80cb63f635d  artifacts/p4_logistic_uc_acip_cone_enclosure/certified_bounds.json
```

Next smallest task: prove a quantitative branch-mass remainder or a frozen
cusp-adapted finite-rank/resolvent tail bound. Do not compare zeros or add a
non-lattice roof before that object is defined.
