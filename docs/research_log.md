# HP-Dynamics Research Log

## 2026-08-06 — CLUE-A3-001 same-ledger annular residual audit

### Repository and provenance

- The outer HP repository began this checkpoint clean at
  `e1a2934f506c5d65a1649c0020511ca5e4442eb0`.
- The relevant nested legacy repository was found to have a stale local
  tracking ref at RH-345. It was fast-forwarded cleanly to the actual remote
  endpoint RH-371, commit
  `2d01633de0bcf0ecd1310291e2547cff417e13a0`.
- RH-371 is an independent capacity obstruction. It does not activate the
  direct annular branch; the latest handoff retains
  `actual_same_clock_unnormalized_head_transport_open`.
- Future shareable Logistic/HP work is mirrored through SSH to
  `git@github.com:maris205/hilbert-polya-structure.git` under
  `logistic_dynamics/`, using one self-contained subproject per stage and one
  paper per genuine result edge.

### Current clue and source lock

The only active clue is `CLUE-A3-001`. No formal candidate was created. The
audit ID is `LEGACY-ANNULAR-RESIDUAL-001`, with source lock
`configs/source_locks/LEGACY-ANNULAR-RESIDUAL-001.yaml`.

The object is

\[
g_\sigma(z)
=\sum_{n\ge2}\frac{\tau_{\sigma,n}-a_n}{n}z^n
=\log G_H(z)-\log\det_2(I-zC_\sigma),
\]

where `C_sigma` is the `q=1/2` normal realization of the complementary
algebraic spectrum of `K_sigma/r_H` after Perron/parity removal. It is not a
proved physical invariant compression. The residual is a logarithmic
determinant ratio diagnostic, not a standalone determinant.

The frozen normalization is

```text
r_H = 17/20
q = 1/2
R = 7/5
rho = 141/100
rho_star = 1.426787483864074...
```

The all-order residual uses every `n>=2`. RH-302 alone uses
`m_sigma=ceil(4 log(1/sigma))`; this is not silently identified with the
physical first-alias clock. Any future numerical pre-audit is frozen to
`sigma_k=lambda^(-2k)`.

### Route-A result

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
overall: ROUTE_A_EXPLORATORY as a diagnostic only
scoped verdict: NOT_TESTABLE
standalone candidate verdict: STOP_SCOPED
Route B: not authorized
```

RH-300 proves the strict-radius conditional implication; at `rho=1.41`, the
`H-infinity` and `H2` conversion constants are `139.0070922` and
`8.2924679`. RH-302 proves the noisy and deterministic tails vanish, reducing
the problem exactly to the moving head. RH-309 proves endpoint `H2`
membership, endpoint `H-infinity` failure, and a logarithmic lower-rate
barrier.

### Strongest failure and reusable knowledge

The legacy tree contains earlier fixed-noise finite spectra, but no compatible
physical-clock `q=1/2` complementary spectrum/trace stream with frozen
discretization, cutoff, precision, and stopping controls. Those snapshots,
fixed-order convergence, finite boundary grids, and RH-354's normalized
selected tail cannot activate the raw signed/complex `p=tau-a` theorem.

Reusable rule: an annular residual must freeze the physical complement,
algebraic multiplicity, determinant sign, Hardy norm, noise schedule, trace
order, and proof cutoff separately before any norm plot. Same-map data from an
incompatible clock or spectral selection are not interchangeable.

### Updated files

- `configs/source_locks/LEGACY-ANNULAR-RESIDUAL-001.yaml`
- `evaluations/route_a/LEGACY-ANNULAR-RESIDUAL-001/20260806T140210Z.yaml`
- `docs/research_clues.md`
- `docs/candidate_registry.md`
- `docs/research_log.md`
- `HP_HANDOFF.md`

No obstruction-registry entry is added because no physical nonconvergence
theorem was proved. `docs/operator_obligations.md` remains unchanged because
Route B is closed.

### Tests and reproduction

Legacy focused suites passed `39/39`: RH-300 `4/4`, RH-302 `3/3`, RH-309
`5/5`, RH-311 `3/3`, RH-361 `20/20`, and Volume IV `4/4`. The outer full
suite passed `225/225` in `63.548 s`; all 43 YAML files parse.

```bash
python3 -m pytest -q -p no:cacheprovider docs/related_programs/prime_dynamics_theory/papers/RH-300-annular-analytic-prefix-criteria/tests
python3 -m pytest -q -p no:cacheprovider docs/related_programs/prime_dynamics_theory/papers/RH-302-annular-tail-moving-head-reduction/tests
python3 -m pytest -q -p no:cacheprovider docs/related_programs/prime_dynamics_theory/papers/RH-309-endpoint-hardy-mismatch-barrier/tests
python3 -m pytest -q -p no:cacheprovider docs/related_programs/prime_dynamics_theory/papers/RH-311-ten-layer-annular-mass-frontier-review/tests
python3 -m pytest -q -p no:cacheprovider docs/related_programs/prime_dynamics_theory/papers/RH-361-ten-layer-signed-completion-and-upper-counterloop-review/tests
python3 -m pytest -q -p no:cacheprovider docs/related_programs/prime_dynamics_theory/papers/RH-VOL4-noisy-head-annulus-signed-completion-synthesis/tests
python3 -m unittest discover -v
python3 -c 'from pathlib import Path; import yaml; fs=list(Path("configs/source_locks").glob("*.yaml"))+list(Path("evaluations").rglob("*.yaml")); [yaml.safe_load(p.read_text(encoding="utf-8")) for p in fs]; print(len(fs))'
git diff --check
```

### Claim boundary and next task

Established: the exact residual data type and sign, clock/normalization
separation, strict-radius conditional theorem, vanishing-tail reduction, and
the precise availability boundary.

Not established: actual annular convergence, a physical complement
compression, arithmetic primitive-orbit weights, completed-xi structure,
quantization, Route B, Hilbert--Polya, or RH.

Stop `CLUE-A3-001` as `NOT_TESTABLE`. Reopen only with the compatible actual
`tau_(sigma_k,n)` stream and a complete numerical source lock, or with a proof
of the frozen `H2(1.41)` moving-head limit. Test only that norm first and do
not refit the source lock.

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
w(0) in [0.1668010108790061, 0.5418010108790062]
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

## 2026-08-05 — validated sharp exact-$U_c$ polar-cone enclosure

### Stable checkpoint

Current clue: `CLUE-A1-004`.

Candidate ID: no new formal candidate. Scoped audit:
`P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE`, strengthening parent candidate
`P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK`.

Source lock:
`configs/source_locks/P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE.yaml`.
It freezes the exact algebraic map, physical clock, `w -> g_A -> h -> C_h`
normalization, absent determinant convention, $2^{18}$ closed-cell cover,
100-digit Arb precision, `python-flint 0.9.0`, FLINT `3.6.0`, allowed and
forbidden data, train/validation/test boundaries, and stopping conditions.

Implementation source commit:
`f34117824702404fe0837f5811a5465d33cc65de`.

Route-A tuple:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
overall: ROUTE_A_EXPLORATORY
scoped audit verdict: GO_WITH_LIMITATIONS
parent verdict: REVISE
```

Route-B tuple: not evaluated. Route B remains inactive and unauthorized.

### Strongest evidence

The independently derived distortion identity

\[
R(t,U_c)=
\frac{U_c y(\rho^2-y)(U_c^2y-3U_c+2)^2}
 {16(1-y)(2-U_cy)(1-U_cy)^4},
\qquad y=\rho^2t,
\]

is evaluated by directed Arb balls on a complete cover of `t in [0,1]`.
Every denominator is strictly positive, all $2^{18}$ cells lie below the
upper threshold, and the sealed witness interval lies above the lower
threshold. Therefore

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

Together with the inherited explicit endpoint remainder, they give

```text
C_12: [0.0029623667412445, 0.0090289530684826]
C_14: [0.0020334760261950, 0.0051059183301683]
C_16: [0.0013068364718538, 0.0029454892619841]
C_18: [0.0008124254452971, 0.0017206760060806]
```

### Strongest failure

The safe density interval remains broad, and no quantitative convergence rate
or exponential finite-order remainder is proved. The certified branches are
first-return observables, not arithmetic primitive periodic orbits. There is
no $s$-dependent Fredholm determinant, analytic completion, or quantization;
`OBR-008` and `OBR-009` remain active.

### New reusable knowledge

A complete directed interval cover can sharpen an infinite-dimensional
analytic cone bound without introducing Ulam truncation or pretending that a
finite-rank residual is a resolvent theorem. Closed cells cover every
between-grid point; interval dependency can only widen the enclosure. The
finite-mass certificate must also seal endpoint-radius, interval-order, and
physical-return-label gates.

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

### Tests

Focused sharp-cone audit: `12/12 passed`.

Full repository: `123/123 passed`.

Artifact SHA-256:

```text
dec8f8c1a6a7dc329d3338fc835ac34e538c0555283d2cc968c09c31e5e5e231  artifacts/p4_logistic_uc_acip_sharp_cone_enclosure/interval_certificate.json
```

### Reproduction commands

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

### Claim boundary

Established: the complete full-domain distortion certificate, the sharper
safe density and endpoint-coefficient intervals, and tighter positive absolute
masses for four sealed physical returns.

Not established: a closed form, narrow high-accuracy density enclosure,
quantitative or exponential branch-mass remainder, arithmetic primitive-orbit
law, determinant, analytic completion, quantization, Route B, Hilbert--Polya,
or RH.

### Next smallest task

Prove a quantitative convergence rate for the physical branch-mass ratio in
one explicitly frozen analytic or cusp-adapted norm. Preserve the physical
clock and normalization, and do not compare zeros or define a determinant
before that theorem exists.

Recommended verdict: `REVISE` (`GO_WITH_LIMITATIONS` for this scoped audit).

## 2026-08-05 — quantitative exact-$U_c$ branch-mass-ratio rate

### Stable checkpoint

Current clue: `CLUE-A1-004`.

Candidate ID: no new formal candidate. Scoped audit:
`P4-LOGISTIC-UC-BRANCH-MASS-RATE`, strengthening
`P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE` under parent candidate
`P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK`.

Implementation source commit:
`dbcb58d21ff93ef842df869c177a3ec3e8c0a785`.

The latest evaluation is
`evaluations/route_a/P4-LOGISTIC-UC-BRANCH-MASS-RATE/20260805T083731Z.yaml`.
It supersedes, but does not overwrite, the preserved `03:53:48Z` evaluation;
the change is provenance-only and leaves the theorem and tuple unchanged.

Source lock:
`configs/source_locks/P4-LOGISTIC-UC-BRANCH-MASS-RATE.yaml`.
It freezes the exact map and endpoint recursion, physical clock, full-acip
normalization, absent determinant convention, cusp radius `1/200`, all branch
indices `n>=6`, 100-digit Arb precision, one common endpoint coefficient,
allowed and forbidden data, data boundaries, and stopping conditions.

Route-A tuple:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
overall: ROUTE_A_EXPLORATORY
scoped audit verdict: GO_WITH_LIMITATIONS
parent verdict: REVISE
```

Route-B tuple: not evaluated. Route B remains inactive and unauthorized.

### Strongest evidence

The frozen physical density belongs locally to

\[
\mathcal X_{1/200}
=\{c\,t^{-1/2}+b(t):b\in L^\infty\},
\qquad
\|v\|=|c|+\|b\|_\infty.
\]

A complete directed Arb interval proves `7/20 < psi' < 9/25` and
`0 < psi'' < 4/25` on the whole cusp domain. The sharp coefficient bound,
explicit remainder, sealed endpoint `delta_5`, and exact Fraction ledger then
give, for every `n>=6`,

\[
\left|
\frac{\mu(C_{2n+2})}{\mu(C_{2n})}-\frac{U_c^2}{4}
\right|
\leq\frac{36}{5}\sqrt{\delta_{n-1}}
<\frac{243}{625}\left(\frac35\right)^{n-6}.
\]

No target data enters. The same physical coefficient $C_h$ is retained in
both adjacent masses; independent marginal coefficient intervals are not
divided.

### Strongest failure

The branch masses are physical observables rather than arithmetic primitive
periodic orbits. There is no phase, multiplicity, repetition, von-Mangoldt
weight, $s$-dependent determinant, completed-$\xi$ structure, or natural
quantization. The legacy ordinary-`BV` proof remains refuted, while
`OBR-008` and `OBR-009` remain active.

### New reusable knowledge

An all-tail adjacent-cusp-mass theorem can be obtained from a frozen local
Banach decomposition, one complete derivative interval, and exact endpoint
contraction without claiming a transfer-operator spectral gap. The leading
cusp coefficient must remain common across the adjacent-mass ledger.

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

Artifact SHA-256:

```text
a6baa8ae9603bd4cebe3a26a85ce537c020282b9a2ae0902e26d37c7e15cc9ae  artifacts/p4_logistic_uc_branch_mass_rate/rate_certificate.json
```

### Claim boundary

Established: the cusp space, complete derivative certificate, exact rational
constant ledger, and explicit physical adjacent-ratio rate for all `n>=6`.

Not established: an exact finite-order mass law, ordinary-`BV` spectral gap,
arithmetic orbit law, determinant, analytic completion, quantization, Route B,
Hilbert--Polya, or RH.

### Next smallest task

Freeze the polar suspension object only: the map $G$, its two branches,
intrinsic positive roof $\tau=\log|G'|$, physical clock relation, analytic
function space, determinant convention, data split, and stopping conditions.
Defer the non-lattice and same-object Fredholm audits until this source lock is
complete.

Recommended verdict: `REVISE` (`GO_WITH_LIMITATIONS` for this scoped audit).

## 2026-08-05 — exact-$U_c$ polar intrinsic-roof source lock

### Stable checkpoint

Current clue: `CLUE-A1-004`.

Candidate ID: no new formal candidate. Lock-only audit ID:
`P4-LOGISTIC-UC-POLAR-INTRINSIC-ROOF`.

Source commit: `4d5cd7e346445317d2ed19ef90a484cca09c3588`.

Source lock:
`configs/source_locks/P4-LOGISTIC-UC-POLAR-INTRINSIC-ROOF.yaml`.

The exact object is the doubled two-full-branch polar Markov map

\[
G=q^{-1}\circ(-f^2)\circ q,
\qquad
q(\theta)=\rho\sin\theta,
\]

with intrinsic roof $\tau=\log|G'|$. One base step is exactly two Logistic
iterates; the suspension clock is the roof sum
$T_\gamma=\log|(G^n)'|$. These clocks are separate.

The lock fixes `epsilon=1/1000`, two complex stadium neighborhoods, the
matching two-component analytic Banach space, the weighted family with
potential `-s*tau`, and the sole conditional notation
$D_{\rm pol}(s)=\det_{\rm Fr}(I-\mathcal L_s)$.

Route-A tuple: inherited `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`; no new
Route-A evaluation was performed. Checkpoint status:
`DEFINED_NOT_EVALUATED`.

Route-B tuple: not evaluated; Route B remains inactive and unauthorized.

### Strongest evidence

The exact polar theorem gives `phi_L'=+a`, `phi_R'=-a`,
`inf|G'|=4/U_c^2>1`, and hence the strictly positive endpoint roof values.
Thirteen executable tests verify the real inverse identities and signs, exact
reflected physical conjugacy, outward endpoint positivity, Markov ledger,
frozen complex obligations, one-way witness logic, data firewall, and scoped
status.

### Strongest failure

The frozen composite complex branch continuations, compact inclusion,
analytic-space invariance, partition-hit trace rule, nuclearity, and
determinant existence have not been proved. The roof is not yet certified
non-lattice. No orbit-divisor or target comparison is open.

### New reusable knowledge

A same-object polar determinant audit must retain the doubled Markov ledger,
signed branch orientation, and positive roof magnitude as separate fields. A
conditional Fredholm notation is not an established determinant.

### Updated files

- `CHANGELOG.md`
- `DERIVATION_PACKAGE.md`
- `HP_HANDOFF.md`
- `configs/source_locks/P4-LOGISTIC-UC-POLAR-INTRINSIC-ROOF.yaml`
- `docs/candidate_registry.md`
- `docs/research_clues.md`
- `docs/research_log.md`
- `tests/test_p4_logistic_uc_polar_intrinsic_roof_lock.py`

`docs/obstruction_registry.md` and `docs/operator_obligations.md` are unchanged.

### Tests and reproduction

Focused lock audit: `13/13 passed`.

Full repository: `148/148 passed`.

```bash
python3 -m unittest -v tests/test_p4_logistic_uc_polar_intrinsic_roof_lock.py
python3 -m unittest discover -v
python3 -c 'import yaml; p="configs/source_locks/P4-LOGISTIC-UC-POLAR-INTRINSIC-ROOF.yaml"; d=yaml.safe_load(open(p,encoding="utf-8")); print(d["audit_id"], d["route_status_at_lock"]["checkpoint_status"], d["route_status_at_lock"]["recommended_verdict"])'
git diff --check
```

### Claim boundary

Established: the exact real lock for the polar Markov base, intrinsic positive
roof, two clocks, branch orientations, intended analytic space and conditional
transfer family, determinant convention, data split, and stopping rules.

Not established: non-lattice behavior, nuclearity, an actual Fredholm
determinant, arithmetic orbit law, completed-$\xi$ structure, quantization,
Route B, Hilbert--Polya, or RH.

### Next smallest task

Audit only whether the sealed primitive words `R` and `LR` have
multiplicatively independent positive multipliers and therefore prove the
roof non-lattice. Failure returns `REVISE` or `NOT_TESTABLE` and is not a
lattice theorem. Do not audit Fredholm nuclearity or compare target zeros in
that task.

Recommended verdict: `REVISE`; checkpoint status `DEFINED_NOT_EVALUATED`.

## 2026-08-05 — exact-$U_c$ polar-roof non-lattice theorem

### Stable checkpoint

Current clue: `CLUE-A1-004`.

Candidate ID: no new formal candidate. Scoped audit:
`P4-LOGISTIC-UC-POLAR-NONLATTICE`.

Implementation source commit:
`36a38f0db16652bf0e0c1459be6c69f6bdafec12`.

Route-A evaluation:
`evaluations/route_a/P4-LOGISTIC-UC-POLAR-NONLATTICE/20260805T110654Z.yaml`.

Source lock:
`configs/source_locks/P4-LOGISTIC-UC-POLAR-NONLATTICE.yaml`.

The audit opens only the sealed primitive words `R` and `LR` of the corrected
polar-roof lock. It preserves the signed multipliers

\[
\Lambda_R=-\alpha<0,
\qquad
\Lambda_{LR}=-\beta<0,
\]

and uses the full primitive roof sums

\[
T_R=\log\alpha,
\qquad
T_{LR}=\log\beta.
\]

Exact factorization and polynomial reduction give an irreducible cubic for
$\alpha$ with norm $2^6$ and an irreducible degree-nine polynomial for
$\beta$ with norm $2^{36}$. A hypothetical rational period ratio implies
$\beta^b=\alpha^a$; common-field norms force $a=2b$, leaving only
$\beta=\alpha^2$. The identity

\[
H_{U_c}(\alpha^2)
=-8192(U_c-2)(2U_c-3)\ne0,
\qquad
3/2<U_c<2,
\]

excludes that case. Therefore $T_{LR}/T_R$ is irrational and the intrinsic
roof is non-lattice.

Route-A tuple:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
overall: ROUTE_A_EXPLORATORY
scoped audit verdict: GO_WITH_LIMITATIONS
parent verdict: REVISE
```

Route-B tuple: not evaluated; Route B remains inactive and unauthorized.

### Strongest evidence

This is an exact theorem, not a decimal-ratio observation. The certificate
checks the exact fixed-point factorization, right-orbit multiplier, degree-12
period-two dynatomic quotient, multiplier identity modulo the critical
polynomial, mod-3 and mod-5 irreducibility, both norm ledgers, the common-field
exponent reduction, and the final nonvanishing identity. Twenty exact algebra
gates pass. High-precision orbit coordinates are explicitly diagnostic only.

### Strongest failure

The theorem removes the unit-lattice hypothesis for this roof but supplies no
arithmetic primitive-orbit law or von-Mangoldt weights. The frozen
`epsilon=1/1000` complex inverse branches, common `Log(a)` germ, compact
inclusion, matching-space invariance, partition-hit trace rule, nuclearity,
Fredholm determinant, global completed-$\xi$ structure, and quantization are
still absent. A2 remains failed.

### New reusable knowledge

Two intrinsic primitive periods can prove a roof non-lattice when exact
multiplier algebra establishes multiplicative independence. Algebraic norms
can collapse an infinite rational-relation problem to one exact residual
identity. `OBR-008` remains a proved obstruction for the old unit clock but is
out of scope for this newly proved non-lattice roof; its divisor-count
obligation remains open.

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

Artifact SHA-256:

```text
a05bfa31316281345e3fe7d6645732beaff291298bc928fd8a6156f0f649b832  artifacts/p4_logistic_uc_polar_nonlattice/nonlattice_certificate.json
```

### Claim boundary

Established: exact signed multipliers for `R` and `LR`, their minimal
polynomials and norms, multiplicative independence, irrational full
primitive-period ratio, and the non-lattice intrinsic roof.

Not established: arithmetic orbit weights, complex branch inclusion,
endpoint trace multiplicity, nuclearity, a Fredholm determinant, analytic
completion, quantization, Route B, Hilbert--Polya, or RH.

### Next smallest task

Audit only the frozen `epsilon=1/1000` composite complex inverse branches,
common `Log(a)` germ, and compact branch inclusion. Do not audit nuclearity,
Fredholm zeros, target divisors, or Route B in that task.

Recommended verdict: `REVISE` (`GO_WITH_LIMITATIONS` for this scoped theorem).

## 2026-08-06 — QG-0001 same-operator relative Fredholm closure

### Stable checkpoint

Current clue: `CLUE-A4-003`.

Candidate ID: `QG-0001`; subaudit ID:
`QG-0001-RELATIVE-FREDHOLM-001`.

- Source commit: `b5ad4c9ce4305cf055a2e6a3ae957ba4fda7e90b`
- Source lock: `configs/source_locks/QG-0001-RELATIVE-FREDHOLM.yaml`
- Evaluation: `evaluations/route_a/QG-0001/20260806T123946Z.yaml`
- Analytic Route-A tuple:
  `(A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_UNITARY_OR_SCATTERING_CANDIDATE)`
- Target interpretation:
  `(A1_WEAK, A2_FAIL, A3_FAIL, A4_UNITARY_OR_SCATTERING_CANDIDATE)`
- Overall: `ROUTE_A_REJECTED`
- Candidate state / verdict: `STOP_SCOPED`
- Route B: not invoked and not authorized

### Exact determinant theorem

For the frozen direct sum `H=direct_sum H_n`, exact metric dilation gives
`H_n` unitarily equivalent to `n^2 H_1`. The Dirichlet terminal gives a
positive base gap, and the base Weyl law gives

\[
H^{-1}\in\mathfrak S_1,
\qquad
\operatorname{Tr}(H^{-1})
=\zeta(2)\operatorname{Tr}(H_1^{-1})
=7.24356536914368571711\ldots.
\]

The complete base divisor, its multiplicities, and finite-exponential-type
growth prove

\[
\chi_0(k)=\det_F(I-k^2H_1^{-1}).
\]

Trace-norm direct-sum convergence then proves, normally on compact sets,

\[
\boxed{
D_H(k)=\det_F(I-k^2H^{-1})
=\prod_{n\geq1}\chi_0(k/n).
}
\]

The raw repaired component bond factor contains
`exp(i*k*L0/n)`. Its factorwise genus-one counterphase
`exp(-i*k*L0/n)` is forced; the standalone harmonic phase diverges away from
the physical divisor. This relative determinant is not the naive orbit Euler
product, direct-sum bond determinant, or heat/spectral zeta, so `OBR-012`
remains valid for those ledgers.

### Exact target obstruction

The determinant zeros are `+/-n*sqrt(lambda_j(H_1))`, with all spectral and
coincidence multiplicities. Its positive count is

\[
N_H(K)=\frac{L_0}{\pi}K\log K+O(K),
\]

so its leading-coefficient ratio to Riemann-von Mangoldt is

\[
2L_0=12.764664694883524\ldots.
\]

No zero-free factor changes a divisor count, and the source lock forbids
post-hoc spectral rescaling. `OBR-013` therefore closes QG-0001 as a
completed-xi divisor candidate under the frozen object.

### New reusable knowledge

An exact `1/n` tower over a positive compact graph of total length `L` has a
valid inverse-spectral Fredholm determinant with leading divisor coefficient
`L/pi`; the necessary target coefficient gate is `L=1/2`. Check this before
orbit enumeration for future harmonic graph towers. Determinant existence and
target determinant matching are separate Route-A facts.

### Updated files

- `CHANGELOG.md`
- `HP_HANDOFF.md`
- `artifacts/qg_0001/relative_fredholm.json`
- `configs/source_locks/QG-0001-RELATIVE-FREDHOLM.yaml`
- `docs/candidate_registry.md`
- `docs/obstruction_registry.md`
- `docs/research_clues.md`
- `docs/research_log.md`
- `evaluations/route_a/QG-0001/20260806T123946Z.yaml`
- `experiments/qg_0001_relative_fredholm.py`
- `formal/obstructions/harmonic_graph_tower_divisor_coefficient.md`
- `formal/results/qg_0001_relative_fredholm.md`
- `tests/test_qg_0001_relative_fredholm.py`

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
python3 -m unittest discover -v
python3 -c 'import yaml; p="evaluations/route_a/QG-0001/20260806T123946Z.yaml"; d=yaml.safe_load(open(p,encoding="utf-8")); print(d["a2"]["verdict"], d["a3"]["verdict"], d["overall_verdict"], d["route_b_invocation_allowed"])'
sha256sum artifacts/qg_0001/relative_fredholm.json \
  experiments/qg_0001_relative_fredholm.py \
  configs/source_locks/QG-0001-RELATIVE-FREDHOLM.yaml \
  formal/results/qg_0001_relative_fredholm.md \
  formal/obstructions/harmonic_graph_tower_divisor_coefficient.md \
  tests/test_qg_0001_relative_fredholm.py
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

### Claim boundary and next smallest task

Established: the genuine same-operator determinant, exact component product,
forced counterphase, trace coefficient, divisor, growth, counting law, and
strict coefficient obstruction.

Not established: a primitive-orbit trace identity, arithmetic weights,
completed-xi structure, Route B, Hilbert--Polya, or RH.

QG-0001 is `STOP_SCOPED`. The project-level next task applies the breadth-first
rule to `CLUE-A3-001`: inspect the legacy RH handoff and freeze exactly one
explicit same-ledger annular residual object before creating a candidate.

Recommended verdict: `STOP_SCOPED`.

## 2026-08-06 — QG-0001 base-component characteristic audit

### Stable checkpoint

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
- Scoped verdict: `GO_WITH_LIMITATIONS`
- Route-B tuple: not evaluated; Route B remains inactive and unauthorized

### Source lock and exact result

Only the `n=1` component is audited. A 6-by-6 sinc-matching matrix uses the
unknowns `(u_L,u_R,q_0,q_1,q_2,q_3)`, with `sin(k*ell)/k` interpreted as `ell`
at `k=0`. Its determinant `C_phys(k)` is entire and even, including at
individual edge-Dirichlet points. Exact evaluation gives

\[
A=C_{\rm phys}(0)
=\sqrt2+\sqrt3+\sqrt5+\sqrt6+\sqrt{15}+3\sqrt{10}>0.
\]

For the parent directed-bond convention,

\[
\Delta_{\rm bond}(k)
=-\frac43 k^2e^{ikL_0}C_{\rm phys}(k),
\qquad
L_0=1+\sqrt2+\sqrt3+\sqrt5.
\]

The identity is checked at 80-digit precision for `k=0.11`, `0.731`, `1.2`,
and `pi` (the last sample has an edge sine zero). Consequently the bond
secular zero at `k=0` has exact order two and is not a physical eigenvalue;
the Dirichlet terminal independently rules out a zero mode.

### Normalization ledger

The first nonzero bond coefficient is

\[
[k^2]\Delta_{\rm bond}(k)=-\frac43A
=-28.2555178892499933575\ldots.
\]

After removing the proved `k^2` and scalar, the raw factor is

\[
\beta(k)=e^{ikL_0}\chi_0(k)=1+iL_0k+O(k^2),
\]

where the zero-free phase removal gives

\[
\chi_0(k)=\frac{C_{\rm phys}(k)}A
=1-4.40355970195371342217\ldots k^2+O(k^4).
\]

For component `n`, the local relation is `chi_n(k)=chi_0(k/n)` and the
corresponding phase counterterm is `exp(-i*k*L_0/n)`. This is a local ledger,
not yet an infinite product.

### Strongest evidence and failure

The physical matching characteristic is now defined without cotangent poles or
automatic sine-factor zeros, and the bond/physical relation is exact under one
frozen convention. This resolves the requested representation singularity.

It does not define a global tower Euler, Fredholm, relative, Weierstrass, or
heat-zeta determinant; it adds no arithmetic orbit law, completed-xi divisor,
Route B result, or RH claim. The parent `OBR-012`, wrong raw `K log K`
coefficient, and period accumulation at zero remain unchanged.

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

`docs/operator_obligations.md` remains unchanged because Route B is closed.

### Tests and reproduction

- Base-characteristic focused suite: `8/8 passed` (`0.899 s`).
- Parent QG focused suite: `8/8 passed`.
- Full repository suite after adding this subaudit: `217/217 passed` (`60.914 s`).
- Exact YAML parse and `git diff --check`: passed.

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

Hashes:

```text
3534a95c9940600760e79e72fdfe94c7b0538ece3f8ec04119cc1faccf7d0f88  artifacts/qg_0001/base_characteristic_zero.json
f5c53c1b4104a88e2b49dfeb237f705479eeac47825a1094b511156ffcdd570e  experiments/qg_0001_base_characteristic.py
e95f0184a757dc1754efd48904b101bbed6afadcd1d8530c8433f1785cc36d8b  configs/source_locks/QG-0001-BASE-CHARACTERISTIC.yaml
fcebae639a006d1d284923bba9464b27b7283b2472f50f25fbbeb598eb60de7e  formal/results/qg_0001_base_characteristic_zero.md
50012f5386e3f30bcb3e9138a9f940b065c5b4ff40bc6e515da47e4d2d91ea1d  tests/test_qg_0001_base_characteristic.py
```

### Claim boundary and next smallest task

Established: the exact entire base physical characteristic, positive value at
zero, exact order-two spurious bond zero, its leading coefficient, and the raw
and dephased normalized Taylor ledgers.

Not established: any global tower determinant, convergence/divisor theorem,
arithmetic trace formula, completed-xi identity, Route B, Hilbert--Polya, or RH.

Next smallest task: freeze one explicit same-operator genus-one relative
component product using `chi_0(k/n)` and `exp(-i*k*L_0/n)`, then prove its
convergence and compatibility with the direct-sum operator. Keep it separate
from the naive orbit product and heat/spectral zeta.

Recommended verdict: `GO_WITH_LIMITATIONS`.

## 2026-08-06 — QG-0001 harmonic magnetic graph-tower prefilter

### Stable checkpoint

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
- Scoped verdict: `GO_WITH_LIMITATIONS`
- Route-B tuple: not evaluated; Route B is inactive and not authorized

### Source lock

The base graph has three `L--R` edges and one `L--D` pendant, with

\[
(\ell_0,\ell_1,\ell_2,\ell_3)=(1,\sqrt2,\sqrt3,\sqrt5),
\qquad
(\alpha_0,\alpha_1,\alpha_2,\alpha_3)
=\left(0,\frac\pi3,\frac{2\pi}3,0\right),
\]

where the second tuple is the fixed `L`-outward magnetic line-integral
representative. `L,R` carry covariant Kirchhoff conditions of degrees four
and three, and `D` is Dirichlet. Component `n` scales all metric lengths by
`1/n` without changing these line integrals. The only clocks are raw metric
length and positive wavenumber `K=sqrt(lambda)`. No prime table, zero table,
fit, rescaling, unfolding, or nonlinear clock is permitted.

The determinant convention remains `NOT_OPENED`. The ordinary Euler product,
standard directed-bond direct sum, heat/spectral zeta, and any future
regularized characteristic determinant are distinct ledgers.

### Route-A tuple and strongest evidence

- `A1_WEAK`: exact enumeration gives `10`, `45`, and `330` primitive oriented
  orbits at topological periods `2`, `4`, and `6`. Every exact based-word trace
  agrees with the primitive/repetition ledger through period six, with signed
  rational scattering amplitudes and magnetic phases retained.
- `A2_FAIL`: the pendant bounce has weight `1/2` and period
  `2*sqrt(5)/n`, so the naive Euler factors tend to `1/2`, not `1`. For the
  standard block

  \[
  B_n(s)=S\,\operatorname{diag}_b
  \left(e^{-s\ell_b/n+i\alpha_b}\right),
  \qquad \lVert B_n(s)\rVert_1\longrightarrow8,
  \]

  so the direct sum is not compact or trace class. This is `OBR-012`.
- `A3_FAIL`: the natural operator has the exact all-order count

  \[
  N_H(K)=\frac{L_0}{\pi}K\log K+O(K),
  \qquad L_0=1+\sqrt2+\sqrt3+\sqrt5,
  \]

  but this is an operator count, not a determinant theorem. Its coefficient
  is larger than the positive Riemann-zero coefficient by the unfitted factor
  `2*L_0 = 12.764664694883523`.
- `A4_UNITARY_OR_SCATTERING_CANDIDATE`: closed magnetic forms give
  self-adjoint components with \(H_n\simeq n^2H_1\). The positive base gap
  and exact scaling make the direct-sum resolvent compact. The asymmetric
  decoration and flux class exclude the inherited local geometric
  antiunitary class.

### Strongest failure and reusable knowledge

The primitive metric periods accumulate at zero, no log-prime or
von-Mangoldt law is present, and neither a same-object regularized determinant
nor a prime-power trace formula exists. The heat/spectral identity

\[
\zeta_H(z)=\zeta(2z)\zeta_{H_1}(z)
\]

is in the exponent variable and is not a wavenumber secular divisor.

Reusable structural knowledge: a harmonic `1/n` graph tower can naturally
produce compact resolvent and a `K log K` count, escaping the fixed finite-graph
`O(K)` obstruction, while simultaneously destroying its naive short-orbit
Euler/Fredholm construction. Counting order and determinant existence must be
audited separately. Also, every self-adjoint compact-resolvent operator admits
an abstract spectral-basis conjugation; excluding the local geometric class
does not exclude that abstract antiunitary or give it an orbit interpretation.

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

### Tests and reproduction

- Focused QG-0001 suite: `8/8 passed` (`0.234 s`).
- Full repository suite: `209/209 passed` (`61.312 s`).
- Source lock and evaluation YAML parse successfully.
- Saved artifact is byte reproducible.

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

Hashes:

```text
ff0d55a1d42a3e0eeb6e1e9efa0b62bc09ab7aa864ee1d2d126c96d0d0650915  artifacts/qg_0001/route_a_prefilter.json
dbc44342748104cf445d87c71340576a61a233b31b8cc754b01f316de7febd43  experiments/qg_0001_harmonic_magnetic_tower.py
3d9593c0f69a958109460e51b2ea6d6e88e869fe05ec7bcc12912082258dab4a  configs/source_locks/QG-0001.yaml
e57dab9366eb01fa2a642f46b71bf70d9b5717342514696bb30adab2ae850c43  formal/results/qg_0001_harmonic_magnetic_tower.md
c94da645af34705d9393d8b34fd5a63fc0c541fba7441f77f1c0de027050687b  formal/obstructions/harmonic_graph_tower_naive_determinant.md
9ce664235ee49c944b17b4ec542309f92171ad6b6b7cdda1714498f006e5d8bf  tests/test_qg_0001_harmonic_magnetic_tower.py
```

### Claim boundary and next smallest task

Established: one explicit target-free harmonic magnetic graph tower; its exact
signed primitive/repetition prefix through period six; exclusion of the
inherited local geometric antiunitary class; a natural self-adjoint
compact-resolvent operator; the intrinsic `K log K` counting exponent; and
failure of both the naive unregularized Euler product and trace class for the
standard direct-sum bond operator.

Not established: an arithmetic orbit law, a same-object regularized
determinant, the correct leading coefficient, a prime-power trace formula,
completed-ξ structure, Route B, Hilbert–Pólya, or RH.

Next smallest task: derive the entire physical base-component characteristic
function at `k=0`, prove the order and removal of every spurious bond-secular
zero, and identify the first nonzero normalized Taylor coefficient. Only then
may one explicit genus-one relative component product be frozen. Do not borrow
zeros from `zeta_H(z)` and do not invoke Route B.

Recommended verdict: `GO_WITH_LIMITATIONS`.

## 2026-08-06 — TH-0001 internal phase caustic obstruction

### Stable checkpoint

Current clue: `CLUE-A4-001`.

Candidate ID: `TH-0001`.

Source lock: `configs/source_locks/TH-0001-FIO.yaml` (phase ledger extension).

Implementation/source commit:
`a4cb10640c44559f0520386d9c84e65c9b873134`.

Route-A evaluation:
`evaluations/route_a/TH-0001/20260806T053410Z.yaml`.

Route-A tuple remains:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)
overall: ROUTE_A_EXPLORATORY
scoped verdict: GO_WITH_LIMITATIONS
Route B: not invoked and not authorized
```

### Exact obstruction

For the ordered three-kick phase

\[
\Phi=S_{1/2}(q_0,q_1)+S_{3/2}(q_1,q_2)+S_{5/2}(q_2,q_3),
\]

the internal Hessian is

\[
H_{\mathrm{int}}=\begin{pmatrix}3q_1&1\\1&5q_2\end{pmatrix},
\qquad
\det H_{\mathrm{int}}=15q_1q_2-1.
\]

The exact point \((q_1,q_2)=(1,1/15)\) lies on the nonempty caustic set.
Thus a global single nondegenerate reduced phase chart and global Maslov index
cannot be silently assigned. The ordered iterated oscillatory integral and the
factorized `L^2(R)` unitary are unaffected.

### New reusable knowledge and boundary

This yields `OBR-011`: for composed kicked maps, factorized Plancherel
unitarity can remain exact even when stationary-phase elimination crosses an
internal caustic. Keep the positive-real per-factor convention and retain the
ordered phase; signed classical multipliers are not a substitute for a Maslov
ledger. A future reopening requires an explicit multi-chart transition calculus.

No spectrum, determinant, trace formula, orbit phase law, Route B, or RH claim
was made.

### Updated files

- `configs/source_locks/TH-0001-FIO.yaml`
- `experiments/th_0001_phase_caustic_audit.py`
- `artifacts/th_0001/phase_caustic_audit.json`
- `formal/obstructions/th_0001_single_phase_caustic.md`
- `evaluations/route_a/TH-0001/20260806T053410Z.yaml`
- `docs/obstruction_registry.md`
- `docs/candidate_registry.md`
- `docs/research_clues.md`
- `docs/research_log.md`
- `HP_HANDOFF.md`
- `CHANGELOG.md`
- `tests/test_th_0001_phase_caustic_audit.py`

### Tests and reproduction

Focused phase-caustic suite: `5/5 passed`.

```bash
python3 experiments/th_0001_phase_caustic_audit.py \
  --quiet \
  --output artifacts/th_0001/phase_caustic_audit.json
python3 -m unittest -v tests/test_th_0001_phase_caustic_audit.py
sha256sum artifacts/th_0001/phase_caustic_audit.json \
  experiments/th_0001_phase_caustic_audit.py \
  configs/source_locks/TH-0001-FIO.yaml \
  evaluations/route_a/TH-0001/20260806T053410Z.yaml
git diff --check
```

Hashes:

```text
a5b8ed95b6832ed47b2da7f1a4a00878c9e64bde0b513cc96a39049ef4a17912  artifacts/th_0001/phase_caustic_audit.json
37734c27d05b75c4f2f3c5aad0e6e7c1edfb17cfa838e96539eea8604c88c593  experiments/th_0001_phase_caustic_audit.py
ac71bc10ed3066910b78a429e56beaf39db0378d10522f482ad6a7e60ba47605  configs/source_locks/TH-0001-FIO.yaml
6ead339b8fb951ddb649fd05e92515b273f4e434b1779646caaf283f7e84d311  formal/obstructions/th_0001_single_phase_caustic.md
737a133f2245a3d06e896218d4ada43ccdf0407de222fae7df7501d428372c2e  tests/test_th_0001_phase_caustic_audit.py
```

### Next smallest task

Stop the phase sub-audit at `OBR-011`. Reopen only with an explicit multi-chart
phase/Maslov ledger and caustic transition rules; do not infer one from signed
multipliers or compute a spectrum/determinant.

Recommended verdict: `GO_WITH_LIMITATIONS` for this scoped obstruction.

## 2026-08-06 — TH-0001 same-order unitary Fourier-integral lift

### Stable checkpoint

Current clue: `CLUE-A4-001`.

Candidate ID: `TH-0001`.

Source lock: `configs/source_locks/TH-0001-FIO.yaml`.

Implementation/source commit:
`836f5880fac6abfb29ee031e1136e24504e2b0a9`.

Route-A evaluation:
`evaluations/route_a/TH-0001/20260806T045554Z.yaml`.

Route-A tuple:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)
overall: ROUTE_A_EXPLORATORY
scoped verdict: GO_WITH_LIMITATIONS
Route B: not invoked and not authorized
```

### Source lock and strongest evidence

The classical generating function is kept exactly,

\[
S_a(q,Q)=qQ-q+\frac a3q^3,
\]

and the frozen quantization uses \(\hbar=1\), Lebesgue `L^2(R,dq)`,

\[
U_a=\mathcal F_+M_a,
\qquad
(\mathcal F_+\psi)(Q)=\frac1{\sqrt{2\pi}}
\int e^{iqQ}\psi(q)dq,
\qquad
(M_a\psi)(q)=e^{i(-q+aq^3/3)}\psi(q).
\]

The mixed generating-function Hessian is one, so each factor has the exact
frozen canonical graph. Modulus-one multiplication and Plancherel prove every
factor and
`U_G=U_(5/2)U_(3/2)U_(1/2)` are everywhere-defined unitaries on `L^2(R)`.
The inverse order is explicitly reversed. The composed kernel remains an
iterated oscillatory integral; possible caustics mean no global single-phase or
absolute-convergence claim is made.

### Antiunitary result and strongest failure

`A=F_+ C` is an involutive antiunitary implementing the parent swap and obeys
`A U_a A^{-1}=U_a^{-1}` for each kick. For the superstep,

```text
A U_G A^{-1}=U_(5/2)^(-1)U_(3/2)^(-1)U_(1/2)^(-1)
U_G^(-1)=U_(1/2)^(-1)U_(3/2)^(-1)U_(5/2)^(-1)
```

The words differ; the reverse parameter word is not a cyclic rotation. The
exact classical witness
`RGR(0,0)=(-1/2,-5/8) != G^(-1)(0,0)=(-1/2,-1/8)` confirms the same-clock
failure. This only audits the inherited affine/metaplectic class; arbitrary
nonlinear/non-geometric antiunitaries remain open. The unitary propagator is
not a self-adjoint Hamiltonian, and no spectrum, determinant, trace formula, or
Route-B object is defined.

### New reusable knowledge

For a kick generated by a type-I phase with constant mixed Hessian, the safest
natural lift is `F_+` followed by modulus-one potential multiplication. Prove
unitarity by factorization rather than trying to reduce a multi-kick oscillatory
kernel through caustics. A shared parent antiunitary can reverse every factor
while failing the superstep solely from a non-palindromic order; this is an
exact word-level obstruction, not a spectral statistic.

### Updated files

- `configs/source_locks/TH-0001-FIO.yaml`
- `experiments/th_0001_fio_quantization.py`
- `artifacts/th_0001/fio_quantization_audit.json`
- `formal/results/th_0001_fio_quantization.md`
- `tests/test_th_0001_fio_quantization.py`
- `evaluations/route_a/TH-0001/20260806T045554Z.yaml`
- `docs/candidate_registry.md`
- `docs/research_clues.md`
- `docs/research_log.md`
- `HP_HANDOFF.md`
- `CHANGELOG.md`

`docs/operator_obligations.md` and `docs/obstruction_registry.md` are unchanged
because no new obstruction was proved and Route B remains closed.

### Tests and reproduction

Focused FIO suite: `12/12 passed`.

Full repository suite: `196/196 passed` (`59.535 s`).

```bash
python3 experiments/th_0001_fio_quantization.py \
  --quiet \
  --output artifacts/th_0001/fio_quantization_audit.json
python3 -m unittest -v tests/test_th_0001_fio_quantization.py
python3 -m unittest discover -v
sha256sum artifacts/th_0001/fio_quantization_audit.json \
  experiments/th_0001_fio_quantization.py \
  configs/source_locks/TH-0001-FIO.yaml \
  evaluations/route_a/TH-0001/20260806T045554Z.yaml
git diff --check
```

Hashes:

```text
0eb583e54b69d3372b582a204c871f7b5f446143353cd6831fea3c27a893fc3e  artifacts/th_0001/fio_quantization_audit.json
9cff63faf27f56e48f89caf1eab45e07e092c61b6c78e3a9b07beb1836c77bfb  experiments/th_0001_fio_quantization.py
888ae90ac95cebcd2c852b655d231da2a73133afd6b6a249e30362fd65838688  configs/source_locks/TH-0001-FIO.yaml
87f4152841bdde4b6129944647ab7dce0f8c7bc13b3d0f372fea7fe532300c04  formal/results/th_0001_fio_quantization.md
4a7c594edc2c6dac076decd8b1d9ba73098134ec5882620446a49f58ecf7898d  tests/test_th_0001_fio_quantization.py
```

### Claim boundary and next smallest task

Established: same-order exact unitary FIO on `L^2(R)`, exact canonical graph,
inherited antiunitary one-kick identities, and failure of inherited antiunitary
and cyclic clock reflection for the non-palindromic product.

Not established: arbitrary antiunitary exclusion, self-adjoint Hamiltonian,
spectral type, determinant, trace formula, Route B, Hilbert--Pólya, or RH.

Next smallest task: preserve the FIO and antiunitary ledgers. Only add an
explicit orbit-phase/Maslov convention if needed; do not compute a spectrum or
determinant.

Recommended verdict: `GO_WITH_LIMITATIONS` for this scoped A4 audit.

## 2026-08-06 — TH-0001 target-free non-palindromic three-kick Hénon prefilter

### Stable checkpoint

Current clue: `CLUE-A4-001`.

Candidate ID: `TH-0001` — target-free non-palindromic three-kick Hénon ratchet.

Source lock: `configs/source_locks/TH-0001.yaml`.

Implementation/source commit:
`fb69649afbda27006d56471c5680b590f90ba43b`.

Route-A evaluation:
`evaluations/route_a/TH-0001/20260806T024238Z.yaml`.

Route-A tuple:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
overall: ROUTE_A_EXPLORATORY
scoped verdict: GO_WITH_LIMITATIONS
Route B: not invoked and not authorized
```

### Source lock and strongest evidence

The only clock is one complete autonomous superstep

\[
G=F_{5/2}\circ F_{3/2}\circ F_{1/2},
\qquad F_a(q,p)=(1-aq^2-p,q).
\]

The half-integer ramp is a declared target-free modeling choice. Exact
generating functions prove exact symplecticity and an explicit inverse. The
inherited swap reversor fails at an exact origin witness; all affine
anti-symplectic involutions are excluded by leading-term comparison. Exact
Groebner/Sturm elimination gives four primitive real period-one orbits and
eight primitive real period-two orbits, with 20 phase points total, globally on
the full plane and without random seeds or a search box. Every certified short
orbit is hyperbolic, with minimum margin
`|tr(M)|-2 > 1.65120565439421041`.

### Strongest failure and reusable knowledge

The result stops at a complete short-orbit structural prefix. There is no
prime-like period law, von-Mangoldt repetition weight, higher-period census,
determinant convention, analytic continuation, or target-zero ledger. The
three-kick order escapes the audited inherited one-/two-kick and affine
reversor classes (`OBR-010`), but arbitrary nonlinear/non-polynomial
anti-symplectic reversors remain open. Exact triangular elimination plus a
primitive dynatomic quotient is a reusable pattern for global low-period UPO
certificates; signed traces, multipliers, and `det(I-M)` must remain distinct
data fields.

### Updated files

- `configs/source_locks/TH-0001.yaml`
- `experiments/th_0001_three_kick_henon.py`
- `tests/test_th_0001_three_kick_henon.py`
- `artifacts/th_0001/route_a_prefilter.json`
- `formal/results/th_0001_three_kick_prefilter.md`
- `formal/obstructions/low_depth_henon_reversibility.md`
- `evaluations/route_a/TH-0001/20260806T024238Z.yaml`
- `docs/candidate_registry.md`
- `docs/obstruction_registry.md`
- `docs/research_clues.md`
- `docs/research_log.md`
- `HP_HANDOFF.md`
- `CHANGELOG.md`

`docs/operator_obligations.md` is unchanged because Route B remains closed.

### Tests and reproduction

Focused TH-0001 suite: `10/10 passed` (31.593 s).

Full repository suite: `184/184 passed` (60.083 s).

```bash
python3 experiments/th_0001_three_kick_henon.py \
  --quiet \
  --output artifacts/th_0001/route_a_prefilter.json
python3 -m unittest -v tests/test_th_0001_three_kick_henon.py
python3 -m unittest discover -v
tmpdir=$(mktemp -d)
python3 experiments/th_0001_three_kick_henon.py --quiet --output "$tmpdir/route_a_prefilter.json"
cmp "$tmpdir/route_a_prefilter.json" artifacts/th_0001/route_a_prefilter.json
sha256sum "$tmpdir/route_a_prefilter.json" artifacts/th_0001/route_a_prefilter.json
sha256sum experiments/th_0001_three_kick_henon.py configs/source_locks/TH-0001.yaml evaluations/route_a/TH-0001/20260806T024238Z.yaml
git diff --check
```

Reproduced hashes:

```text
f50e806512b45a49223dd1ee7fac2689858949a7172a02e73e82d1a03a5e104a  artifacts/th_0001/route_a_prefilter.json
f3da9e8d1ce5690a0ae96350c0392c53bf7e42cf6bb71fc108dddbbc056745a4  experiments/th_0001_three_kick_henon.py
0b8606c3ec470d071465a8335293dc064b339bd9a0cce29a389fc00a44de1633  configs/source_locks/TH-0001.yaml
f12660372b1b23317f8d8dec77bc793b995d8c9f7949104f43d219543d69e175  evaluations/route_a/TH-0001/20260806T024238Z.yaml
```

### Claim boundary and next smallest task

Established: one explicit autonomous exact-symplectic target-free map, the
frozen superstep clock and signed normalization, low-depth reversibility
obstruction, and complete real primitive-orbit data through `G`-period two.

Not established: arbitrary nonlinear time-reversal breaking, arithmetic orbit
correspondence, any dynamical determinant or global analytic structure,
quantization/operator domain, Route B, Hilbert--Pólya, or RH.

Next smallest task: freeze the same-order Fourier-integral quantization on
`L^2(R)`, prove normalization and unitarity, and audit natural antiunitary
symmetry. Do not compute a spectrum, fit zeros, define a determinant, or invoke
Route B.

Recommended verdict: `GO_WITH_LIMITATIONS` for this scoped prefilter;
candidate-level status remains `UPO_PASSED` only through the frozen cutoff.

## 2026-08-05 — frozen-radius exact-$U_c$ polar complex branches

### Stable checkpoint

Current clue: `CLUE-A1-004`.

Candidate ID: no new formal candidate. Scoped audit:
`P4-LOGISTIC-UC-POLAR-COMPLEX-BRANCH`.

Implementation source commit:
`3ae5e23508e27129cfa5910473b944026b904ea3`.

Source lock:
`configs/source_locks/P4-LOGISTIC-UC-POLAR-COMPLEX-BRANCH.yaml`.

Route-A evaluation:
`evaluations/route_a/P4-LOGISTIC-UC-POLAR-COMPLEX-BRANCH/20260805T125236Z.yaml`.

The audit keeps `epsilon=1/1000` and works on the single convex union of the
two frozen branch stadiums. It first constructs

\[
t(z)=\sqrt{\frac{1+\rho\sin z}{U_c}},
\qquad
\ell(z)=-\log4+\frac12\Log(1+t)
+\frac12\Log(\rho+t)-\Log t,
\qquad
a=e^\ell,
\]

with each principal root or logarithm applied separately to a
right-half-plane function. The branches are then defined by

\[
\phi_L(z)=\int_{\pi/2}^{z}a(w)\,dw,
\qquad
\phi_R(z)=-\int_{\pi/2}^{z}a(w)\,dw.
\]

This preserves `phi_L'=+a` and `phi_R'=-a` and proves the locked coordinate
identity

\[
S(\rho\sin\phi_\sigma(z))=\rho\sin z.
\]

No independently defined holomorphic forward $G$ is claimed on the
noninjective endpoint caps.

The exact analytic ledger and 100-digit outward Arb certificate prove

\[
\begin{aligned}
\operatorname{Re}g&>0.29559,\\
d&<0.000324,\\
|\ell(z)-\ell(x)|&<0.000851,\\
M:=\sup_{\overline U}|a|&<0.59626<1.
\end{aligned}
\]

The logarithm variation forces $\operatorname{Re}a>0$, so both branches are
globally univalent. For all four `LL`, `LR`, `RL`, and `RR` pairs, the common
image radius is below `0.00059626` and the compact margin exceeds
`0.00040374`.

Route-A tuple:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
overall: ROUTE_A_EXPLORATORY
scoped audit verdict: GO_WITH_LIMITATIONS
parent verdict: REVISE
```

Route-B tuple: not evaluated; Route B remains inactive and unauthorized.

### Strongest evidence

This is a full-domain analytic theorem, not a complex-grid observation. One
common functional calculus handles the overlap and both endpoint
cancellations; one contraction bound handles every target/source pair; and a
separate logarithm-variation bound proves global univalence. Exact source
identities, environment gates, source hashes, and byte-identical artifact
reproduction all pass. Independent proof and interval audits found no
blocking issue.

### Strongest failure

No target-copy or multiplicity rule is frozen for partition-hit orbits in the
doubled matching space. Nuclearity, a Fredholm determinant, trace formula,
root count, target divisor, functional equation, and quantization remain
absent. A2 remains failed.

### New reusable knowledge

At polar endpoints, construct the common nonzero inverse derivative and its
holomorphic logarithm before constructing inverse branches. Defining the
branches as primitives avoids incompatible scalar `sqrt/asin` endpoint
choices. A small complex logarithm variation can then prove positive real
derivative and global univalence, while the same derivative bound supplies a
uniform compact-inclusion margin.

Portfolio knowledge: RH exploration should not turn every `A1_WEAK/A2_FAIL`
object into an indefinite bridge-building program. After this stable theorem
edge, the Logistic line keeps an explicit local resume task but yields the
project-level slot to the structurally different Hénon family.

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

### Claim boundary

Established: one common holomorphic $t$, $a$, and $\Log(a)$ on the frozen
complex domain; two globally univalent signed composite inverse branches;
all four compact inclusions; and matching-space invariance for each fixed
$s$.

Not established: partition-hit trace multiplicity, nuclearity, a Fredholm
determinant, arithmetic orbit weights, completed-$\xi$ global structure,
quantization, Route B, Hilbert--Polya, or RH.

### Next smallest task

Candidate-local resume task: freeze only the doubled-partition target-copy
and multiplicity rule for partition-hit traces on the matching space.

Project-level next task: park the Logistic branch and apply the RH
breadth-first rule to `CLUE-A4-001`. Freeze exactly one explicit target-free
Twisted Hénon / kicked-symplectic object, then prefilter only its autonomous
definition, symplecticity, antiunitary/time-reversal symmetry, and
reproducible short primitive UPOs. Do not fit zeros or define a determinant in
that first task.

Recommended verdict: `REVISE` (`GO_WITH_LIMITATIONS` for this scoped theorem).
## 2026-08-07 — exact-U_c polar half-open partition trace ledger

### Stable checkpoint

Current clue: `CLUE-A1-004`.

Audit ID: `P4-LOGISTIC-UC-POLAR-PARTITION-TRACE`.

Source lock:
`configs/source_locks/P4-LOGISTIC-UC-POLAR-PARTITION-TRACE.yaml`.

Route-A evaluation:
`evaluations/route_a/P4-LOGISTIC-UC-POLAR-PARTITION-TRACE/20260807T032000Z.yaml`.

The exact root is the unique real solution of

\[
U_c^3-2U_c^2+2U_c-2=0,
\]

and no rounded legacy literal is used. The geometric coding is frozen as

\[
I_L^{\rm ho}=[-\pi/2,0),
\qquad
I_R^{\rm ho}=[0,\pi/2].
\]

The exact endpoint graph is

\[
P=-\pi/2\mapsto P,
\qquad
Q=\pi/2\mapsto P,
\qquad
Z=0\mapsto Q.
\]

Thus the partition point is preperiodic, not a boundary periodic orbit. The
finite symbolic certificate through word length eight confirms cyclic-rotation
canonicalization, endpoint-copy swap invariance, signed branch orientation,
and separation of repetitions from endpoint coding.

### Strongest evidence

The boundary graph follows exactly from the critical identities
`S(+rho)=S(-rho)=-rho` and `S(0)=rho`; no numerical orbit search is needed.
The matching-space family has a common output expression, so its range lies in
the kernel of `delta(v)=v_L(0)-v_R(0)`.

### Strongest failure

The geometric half-open quotient convention is not yet an analytic trace
identity. Even when a doubled operator has common output at zero, the raw
branch-source sum can retain its cyclic multiplicity; a local trace calculation
at the boundary fixed point `P` is still required. No nuclearity or Fredholm
determinant is opened.

### New reusable knowledge

Keep three ledgers separate:

1. geometric half-open orbit coding (one canonical lift per geometric orbit);
2. doubled branch-source/cyclic trace words (which may retain source
   multiplicity); and
3. matching-space analytic traces (requiring a local endpoint calculation).

Matching at a partition point alone cannot be used to divide a trace by two.
No universal `2^h` endpoint factor is allowed without a transition census.

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

`docs/obstruction_registry.md` and `docs/operator_obligations.md` remain
unchanged; this is a scoped ledger audit and Route B is not authorized.

### Tests and reproduction

```bash
python3 experiments/p4_logistic_uc_polar_partition_trace.py \
  --quiet \
  --output artifacts/p4_logistic_uc_polar_partition_trace/partition_trace_certificate.json
python3 -m unittest -v tests/test_p4_logistic_uc_polar_partition_trace.py
```

### Claim boundary and next smallest task

Established: exact-U_c endpoint graph, half-open quotient coding, finite cyclic
word regression, signed orientation bookkeeping, and matching-range inclusion.

Not established: local matching-space trace multiplicity, nuclearity, a
Fredholm determinant, arithmetic orbit weights, completed-xi structure,
quantization, Route B, Hilbert--Polya, or RH.

Next smallest task: derive the local matching-space trace correction at the
boundary fixed point `P=-pi/2` under this lock, or stop the Logistic branch.

## 2026-08-07 — exact-U_c local polar boundary trace

### Stable checkpoint

Audit ID: `P4-LOGISTIC-UC-POLAR-BOUNDARY-TRACE`.

The audited operator is only the left weighted composition branch

\[
T_{s,L}v=e^{s\ell}\,v\circ\phi_L
\]

on the disk algebra of the frozen complex stadium `U_L`. At the unique
boundary periodic point `P=-pi/2`, set

\[
\alpha_0=\phi_L'(P)=\frac{U_c^2}{4}.
\]

The exact endpoint identities and the inherited compact inclusion prove

\[
\operatorname{Tr}T_{s,L}
=\frac{\alpha_0^s}{1-\alpha_0},
\qquad
\operatorname{Tr}_P T_{s,L}^n
=\frac{\alpha_0^{ns}}{1-\alpha_0^n}.
\]

### Strongest evidence

The point `P` is a real endpoint but an interior point of `U_L`. The right
inverse branch maps target `P` to `+pi/2`, so it is not a diagonal fixed germ.
The disk-coordinate weighted-composition matrix is triangular with diagonal
`alpha_0^(n*s)*(alpha_0^n)^k`; its geometric sum gives the formula. A
100-digit certificate checks every frozen Taylor tail for powers 1--4,
`s=0,1/2,1,2+i`, and cutoffs 4--64, with maximum residual below `2e-101`.

### Strongest failure

This is a local branch theorem. Nuclearity of the full two-component operator
on the matching space, the complete trace formula, and the Fredholm
determinant remain unproved. No zero calculation is authorized.

### New reusable knowledge

An interval endpoint that lies in the interior of the complex transfer domain
does not receive a half-trace weight. Endpoint topology, doubled symbolic
coding, and analytic fixed-germ multiplicity must be audited separately.

### Claim boundary

Route-A remains `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` / `REVISE`. Route B is
inactive. The next smallest task is the full matching-space nuclearity theorem,
not Fredholm-zero evaluation.

## 2026-08-08 — LOG-0001 full matching-space nuclear Fredholm theorem

### Stable checkpoint

Current clue: `CLUE-A1-004`.

Candidate ID: `LOG-0001` (formal candidate).

Source lock:
`configs/source_locks/LOG-0001-NUCLEAR-FREDHOLM.yaml`.

Provenance: HP-Dynamics research commit
`e3358c3a90ec67c2f1cf8b883107ad0fcf3cc64a`; shared standalone paper-stage
mirror commit `e6cf4f21b5d82adaec40cb542d952cf491a0b909`.

The frozen Banach spaces are

\[
X=A(U_L)\oplus A(U_R),
\qquad
B=\ker[v_L(0)-v_R(0)],
\]

where the unchanged outer stadiums have radius `1/1000`. The radius
`3/5000` stadiums are proof-only intermediate domains. Every weighted block
factors as

\[
A(U_\sigma)\xrightarrow{R_\sigma}A(V_\sigma)
\xrightarrow{Q_{j\sigma}(s)}A(U_j).
\]

A Riemann-map Taylor expansion of $R_\sigma$ has coefficient norms bounded
by $r_\sigma^m$ for one $r_\sigma<1$. Hence every restriction, weighted
block, the finite block family $\mathcal L_s$ on $X$, and its restriction to
$B$ are $p$-nuclear for every $0<p\le1$. The same expansion and
$\partial_s^k e^{s\ell}=\ell^ke^{s\ell}$ prove locally bounded entire
dependence in each $p$-nuclear ideal.

With $e=(1,0)$, $X=B\oplus\mathbb Ce$ and the common-output identity gives

\[
\mathcal L_s=
\begin{pmatrix}\mathcal L_{s,B}&b_s\\0&0\end{pmatrix}.
\]

Therefore matching preserves, rather than halves, the ambient traces and
determinant. The canonical Grothendieck determinant

\[
\Delta(\lambda,s)=\det_{\rm Fr}(I-\lambda\mathcal L_{s,B})
\]

is jointly entire, and $D_{\rm pol}(s)=\Delta(1,s)$ is entire. For every
$n\ge1$,

\[
\operatorname{Tr}\mathcal L_s^n
=\sum_{\omega\in\{L,R\}^n}
\frac{e^{-sT_\omega}}
     {1-\varepsilon_\omega e^{-T_\omega}},
\qquad
\varepsilon_\omega=(-1)^{\#R(\omega)}.
\]

The word index is the explicit reverse-order relabelling of the diagonal
block path. Distinct cyclic rotations remain when distinct; a least-period
$d$ orbit repeated to $n=rd$ contributes $d$ based points, and the `1/n`
log-determinant factor supplies `1/r`. The pure-left term remains
$\alpha_0^{ns}/(1-\alpha_0^n)$ with no seam or doubled factor.

### Route evaluation

Route-A analytic tuple:

```text
(A1_WEAK, A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)
```

Riemann-target tuple:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
```

Route-B tuple: `(NOT_INVOKED, NOT_INVOKED, NOT_INVOKED, NOT_INVOKED,
NOT_INVOKED)`; invocation is not authorized.

### Strongest evidence

The order-zero expansion is explicit rather than inferred from compactness;
the complemented matching identity is exact; and the same frozen operator now
has a canonical jointly entire Fredholm determinant and exact signed all-power
trace. An adversarial functional-analysis review passed after correcting the
block-word indexing. The target-free 100-digit implementation enumerates all
`2^1+...+2^8=510` based words and passes fixed-point residual, strict itinerary,
contraction, cyclic transport, orientation, signed denominator, and pure-left
boundary gates.

### Strongest failure

No primitive orbit is related to a prime or von-Mangoldt prime-power weight.
No growth-order or high-height divisor theorem, functional equation,
Gamma/trivial-zero ledger, target zero count, completed-$\xi$ equality, or
natural quantization is known. Determinant and Riemann zeros were not
computed under this lock.

### New reusable knowledge

1. A fixed compact inclusion between Jordan-domain disk algebras becomes an
   order-zero nuclear map by an explicit Riemann-map/Taylor expansion.
2. A codimension-one matching condition does not alter a determinant when the
   ambient nuclear operator maps into the matching kernel; the block identity
   decides the multiplicity.
3. A genuine analytic Fredholm determinant is only an A2/A3 structural gate.
   Arithmetic orbit weights and the determinant's own divisor regime must be
   established separately before any target interpretation.

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

`docs/operator_obligations.md` remains unchanged because A4 fails and Route B
is not authorized.

### Tests

- LOG-0001 focused suite: `6/6 passed` (`29.359 s`).
- Full repository suite: `244/244 passed` (`93.940 s`).
- `git diff --check`: passed.

### Reproduction commands

```bash
python3 experiments/log_0001_nuclear_fredholm.py \
  --quiet \
  --output artifacts/log_0001_nuclear_fredholm/nuclear_fredholm_certificate.json
python3 -m unittest -v tests/test_log_0001_nuclear_fredholm.py
python3 -m unittest discover -s tests -p 'test_*.py'
git diff --check
sha256sum \
  artifacts/log_0001_nuclear_fredholm/nuclear_fredholm_certificate.json \
  experiments/log_0001_nuclear_fredholm.py \
  formal/results/log_0001_nuclear_fredholm.md \
  configs/source_locks/LOG-0001-NUCLEAR-FREDHOLM.yaml \
  evaluations/route_a/LOG-0001/20260808T051519Z.yaml \
  tests/test_log_0001_nuclear_fredholm.py
```

The hashes at this checkpoint are:

```text
1ca6a3fa7c8c1367a3560e1ad6441980822ce9e0ae3105f9c0edcf220f714c74  artifacts/log_0001_nuclear_fredholm/nuclear_fredholm_certificate.json
df9dd590dea0334d5fa110992ae013a042539264777898dc6b863de733304e3f  experiments/log_0001_nuclear_fredholm.py
0645972215211d95c191c9f2e166e6592e21b6db625e69a07a06ea3209ab0c7d  formal/results/log_0001_nuclear_fredholm.md
3c67edbcb0eca1ccbb786b7c3321b4af307a35e07c7e2f7467a29f029d27b6e3  configs/source_locks/LOG-0001-NUCLEAR-FREDHOLM.yaml
5bfa1502fb430fbd146a865add904cd91111667d643ef42e647aac427f3a4dfa  evaluations/route_a/LOG-0001/20260808T051519Z.yaml
5b2396e235ac6b34ef2eaae88db5783cb9991c75b1f4937d047a86055f59b35e  tests/test_log_0001_nuclear_fredholm.py
```

### Claim boundary and next task

Established: full matching-space order-zero nuclearity, locally entire
$p$-nuclear dependence, the canonical jointly entire same-object determinant,
conjugation symmetry, and the exact signed all-power trace ledger.

Not established: log-prime/von-Mangoldt orbit data, determinant divisor growth,
functional equation, completed-$\xi$, target zeros, quantization, Route B,
Hilbert--Pólya, or RH.

Next smallest task: prove an intrinsic high-imaginary-height divisor-count
regime or a strict growth-order bound for $D_{\rm pol}(s)$ without computing or
comparing target zeros.

Recommended verdict: `GO_WITH_LIMITATIONS`; overall
`ROUTE_A_EXPLORATORY`.

## 2026-08-10 — COPRIME-0001 scalar continuation and endpoint barrier

### Current clue and candidate

`CLUE-A1-009` / `COPRIME-0001` remained the sole active object after the
countable trace ledger. The source lock froze the original
`D_cop(s)=det_F(I-L_s)` on `Re(s)>1`; no target data, determinant values, or
root locations were allowed.

### New theorem edge

On the squarefree divisor space, the Mobius factorization is

```text
L_s=V_s M V_s^T,
C_s=V_s^T V_s M=zeta(s)T_s-P_1,
T_s(d,e)=mu(e)[d,e]^(-s).
```

The exact Hilbert--Schmidt ledger is

```text
||H_s||_{S_2}^2 = prod_p(1+3*p^(-2*Re(s))),  H_s(d,e)=[d,e]^(-s).
```

Thus `D_tilde(s)=det_2(I-C_s)` is holomorphic on
`Re(s)>1/2, s!=1` and agrees with `D_cop` on `Re(s)>1` because
`Tr(C_s)=0` there. This is a scalar continuation representation only; the
original counting-measure `ell^2` matrix remains undefined as a bounded
operator on `Re(s)<=1`.

### Endpoint obstruction

Adding label one only for a min--max comparison gives local rank-two prime
coordinate kernels with

```text
alpha_p^+/-=(1 +/- sqrt((1+3*p^(-s))/(1-p^(-s))))/2.
```

The positive finite-coordinate products diverge in count as `s downarrow 1`.
After the codimension-one compression back to labels `n>=2`, every fixed
positive eigenvalue index eventually exceeds one, while `||L_3||<9/16<1`.
Continuity therefore yields infinitely many distinct positive real zeros
`s_j downarrow 1` of `D_cop`. This proves that no holomorphic or meromorphic
germ of the same scalar determinant passes through `s=1`.

No root was searched for or numerically located; the zeros are an existence
consequence of the spectral-flow theorem. The punctured `det_2` continuation
and the endpoint barrier are kept as separate ledgers.

### Route-A update

```text
(A1_WEAK, A2_ANALYTIC_DETERMINANT,
 A3_CONTROLLED_CONTINUATION, A4_FAIL)
```

The Riemann-target interpretation remains
`(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`. The scoped audit is `STOP_SCOPED`; no
Route-B invocation is authorized. Any reopening requires a new source lock
with a new determinant or function space, and must not search roots or compare
Riemann zeros.

### Updated files

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
- `HP_HANDOFF.md`
- `CHANGELOG.md`

### Tests and reproduction

Focused scalar-boundary suite: `7/7 passed`.

```bash
python3 experiments/coprime_0001_scalar_boundary.py \
  --quiet \
  --output artifacts/coprime_0001/scalar_boundary_certificate.json
python3 -m unittest -v tests/test_coprime_0001_scalar_boundary.py
```

Recommended verdict: `STOP_SCOPED`; overall Route-A status remains
`ROUTE_A_EXPLORATORY` for the analytic representation, with the completed-xi
target tuple still failed.

## 2026-08-09 — COPRIME-0001 countable trace and primitive-cycle ledger

### Stable checkpoint

The breadth pivot selected exactly one new mathematically explicit object:

```text
Candidate: COPRIME-0001
Clue: CLUE-A1-009
Source lock: configs/source_locks/COPRIME-0001-COUNTABLE-TRACE.yaml
Evaluation: evaluations/route_a/COPRIME-0001/20260809T134933Z.yaml
```

The phase space is the coprime countable shift on labels `n>=2`, with roof
`tau(n)=log(n)`, and the symmetric kernel
`K_s(m,n)=1_{gcd(m,n)=1}(mn)^(-s/2)` on `ell^2({2,3,...})`.
The sole determinant convention is `D_cop(s)=det_F(I-L_s)` on `Re(s)>1`.

### Route-A result

```text
(A1_WEAK, A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)
overall: ROUTE_A_EXPLORATORY
scoped verdict: GO_WITH_LIMITATIONS
Route B: not authorized
```

For `sigma=Re(s)>1`, the Mobius rank-one decomposition has trace-norm sum

```text
sum_d |mu(d)| S_d = zeta(sigma)^2/zeta(2 sigma)-1 < infinity.
```

Hence `L_s` is a locally uniformly holomorphic trace-class family. Absolute
cycle summability gives

```text
Tr(L_s^k) = sum over cyclic coprime words (prod_i n_i)^(-s),
```

and the exact primitive/repetition ledger
`Tr(L_s^k)=sum_{|gamma||k}|gamma| w_gamma^(k/|gamma|)`.
There are no period-one cycles. Period-two and period-three orientation
factors and finite inclusion-exclusion formulas pass exactly; the sealed
Fraction ledger reproduces powers `k=1..6`.

The operator boundary is exact: for the coordinate vector `e_2`,
`||L_s e_2||_2^2 = 2^(-sigma) sum_{m>=3,m odd} m^(-sigma)`, which diverges
for `sigma<=1`. Any continuation across `Re(s)=1` would therefore be a
scalar determinant theorem beyond the original bounded ell-squared operator,
not a silent extension of the same transfer operator.

### Strongest failure

The gcd rule has not produced a prime-to-orbit correspondence or
von-Mangoldt amplitudes. No continuation, global divisor-count theorem,
functional equation, completed-xi identity, or quantization is established.
The determinant was not evaluated and no roots were searched.

### New reusable knowledge

1. A genuinely recurrent countable shift can be screened by an exact nuclear
   decomposition before any target comparison.
2. Symmetric half-roof kernels telescope to a single, unambiguous cycle clock;
   period and repetition factors can be audited independently with exact
   rational arithmetic.
3. Trace class alone is an A2 theorem edge, not evidence of a prime-orbit law
   or a completed-xi divisor.

### Updated files

- `IDEA_REPORT.md`
- `configs/source_locks/COPRIME-0001-COUNTABLE-TRACE.yaml`
- `experiments/coprime_0001_countable_trace.py`
- `artifacts/coprime_0001/countable_trace_certificate.json`
- `tests/test_coprime_0001_countable_trace.py`
- `formal/results/coprime_0001_countable_trace.md`
- `formal/obstructions/coprime_ell2_operator_boundary.md` (`OBR-014`)
- `evaluations/route_a/COPRIME-0001/20260809T134933Z.yaml`
- `docs/candidate_registry.md`
- `docs/research_clues.md`
- `docs/research_log.md`
- `HP_HANDOFF.md`
- `CHANGELOG.md`

### Tests and reproduction

Focused suite: `10/10 passed`; full repository suite after integration:
`283/283 passed`.

```bash
python3 experiments/coprime_0001_countable_trace.py --quiet \
  --output artifacts/coprime_0001/countable_trace_certificate.json
python3 -m unittest -v tests/test_coprime_0001_countable_trace.py
python3 -m unittest discover -s tests -p 'test_*.py'
git diff --check
```

### Claim boundary and next task

Established: exact trace class, holomorphic half-plane determinant, and exact
period/repetition ledger. Not established: prime correspondence, global
divisor law, completed xi, Route B, Hilbert--Pólya, or RH.

Next smallest task: audit whether the scalar `D_cop(s)` continues across
`Re(s)=1` despite the exact ell-squared operator boundary, or prove an
intrinsic barrier, preserving this source lock and determinant convention.

## 2026-08-09 — LOG-0001 Phragmen--Lindelof order lower bound

### Stable checkpoint

Current clue: CLUE-A1-004.

Candidate ID: LOG-0001 (formal candidate).

Source lock:
configs/source_locks/LOG-0001-ORDER-LOWER.yaml.

Evaluation:
evaluations/route_a/LOG-0001/20260809T110000Z.yaml at source state
9b0b09e305579d9ed0ae755b2e499a3bd05a261b.

Provenance: HP-Dynamics research commit
d1cfa20c6b69503af95abb96ded893eb19329371.  This bounded analytic audit is
kept in the main repository; the lower-growth standalone mirror remains the
active shareable paper stage.

The unchanged determinant is entire, has the inherited uniform bound
|D_pol(s)|<=K_2=exp(B_2) on Re(s)>=2, and has the inherited
nonconstancy witness D_pol'(2)>0.0213. Suppose its order were rho<1 and
choose rho<eta<mu<1. With g(z)=D_pol(2-z) on Re(z)>0, the principal branch
satisfies Re(z^mu)>=cos(mu*pi/2)|z|^mu. The damped function
g(z)exp(-epsilon*z^mu) vanishes on large semicircles because eta<mu.
The half-disk maximum principle, epsilon->0, and Liouville then contradict
the derivative witness. Therefore

\[
1\le\operatorname{ord}(D_{\rm pol})\le2.
\]

### Route evaluation

Analytic Route-A tuple:

~~~
(A1_WEAK, A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)
~~~

Riemann-target tuple:

~~~
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
~~~

Overall/scoped verdict: ROUTE_A_EXPLORATORY / GO_WITH_LIMITATIONS.
Route B remains unauthorized.

### Strongest evidence

- The half-plane bound is uniform in imaginary height on the full line
  Re(s)=2; a real-axis limit alone is not substituted.
- The translated half-plane orientation, principal branch, damping exponent,
  and Liouville contradiction were independently audited.
- Focused PL suite: 7/7 passed; the 1024-bit scalar certificate is
  byte-reproducible and target-free.

### Strongest failure

The theorem does not decide order one versus two, type, divisor asymptotics,
a T log T law, arithmetic orbit weights, completed-xi, quantization, Route B,
Hilbert--Polya, or RH.

### New reusable knowledge

A nonconstant entire function bounded on one closed half-plane has order at
least one. The threshold is sharp: an order-one exponential perturbation is
bounded on such a half-plane. Uniform vertical control and entire-ness are
essential hypotheses.

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

No obstruction-registry or operator-obligation entry is added; Route B remains
closed.

### Tests and reproduction

~~~
python3 experiments/log_0001_order_lower.py --quiet \
  --output artifacts/log_0001_order_lower/order_lower_certificate.json
python3 -m unittest -v tests/test_log_0001_order_lower.py
python3 -m unittest discover -s tests -p 'test_*.py'
git diff --check
~~~

Hashes at this checkpoint:

~~~text
3f58a6a3ca8ae2ac0812db36c25b7bbc011313b2ab2fd9c2af698137e51f99f2  artifacts/log_0001_order_lower/order_lower_certificate.json
2595fae21c5eb4c71c814c3e030d674bd907d3fd28ffb437ab3ea73a0bc5e23f  experiments/log_0001_order_lower.py
97d9121f0a6c6f982305ed6e9cfe6ba84afa50d8fc6318a9821062351be62fd5  formal/results/log_0001_order_lower.md
aac9829fb404533ce7a0e44831867a3f1a2fc93eeb07fc06cd9f5e087acb303f  configs/source_locks/LOG-0001-ORDER-LOWER.yaml
e586da1cde78a7a285be5980c649ee95d7998df12ed37f0283d0e412bbc32692  evaluations/route_a/LOG-0001/20260809T110000Z.yaml
ac8c69dba4a8208a51dd0373a998c0d13ac2587cadf32d184aee8a9764fa1e8e  tests/test_log_0001_order_lower.py
~~~

### Claim boundary and next task

Established: 1<=ord(D_pol)<=2 for the same frozen determinant.

Not established: exact order, type, sharp divisor counts, target zeros,
arithmetic orbit law, completed-xi, quantization, Route B, Hilbert--Polya, or
RH.

Next smallest task: apply the breadth pivot and define one new intrinsic
recurrent candidate with an explicit phase space, clock, determinant
convention, and plausible arithmetic orbit law, or register a reusable
structural obstruction.

Recommended verdict: GO_WITH_LIMITATIONS; overall ROUTE_A_EXPLORATORY.

## 2026-08-09 — LOG-0001 cancellation-safe lower-growth theorem

### Stable checkpoint

Current clue: CLUE-A1-004.

Candidate ID: LOG-0001 (formal candidate).

Source lock:
configs/source_locks/LOG-0001-LOWER-GROWTH.yaml.

Evaluation:
evaluations/route_a/LOG-0001/20260809T073000Z.yaml at source state
8cabec587cf0a796f4f004bf5b1b0611de3305f3.

Provenance: HP-Dynamics research commit
726e42a93a9fabcf07c4c543c1c5962aa0fa1569; shared standalone paper-stage
mirror commit 8fbe914cf4438a5a792f7e87e0c87e3a88292201.

The frozen object remains

\[
D_{\rm pol}(s)=\det_{\rm Fr}(I-\mathcal L_s|_B),
\qquad B=\ker[v_L(0)-v_R(0)],
\]

with the inherited exact-U_c polar map, intrinsic roof
T_gamma=sum log|G'|, signed orientation denominator, matching condition,
stadiums, and lambda=1 determinant convention. Only the real anchor s=2
is opened by this lock.

Set

\[
\alpha_0=U_c^2/4,\quad \tau_*=-\log\alpha_0,\quad
B_2=\frac{-\log(1-2\alpha_0^2)}{1-\alpha_0}.
\]

The complete signed trace logarithm is locally uniformly differentiable on
the inherited zero-free half-plane. On the real axis every exact summand in
the differentiated ledger is positive because
1-epsilon_omega exp(-T_omega)>0. The exact n=1 pure-left word therefore
gives the same-determinant lower bound

\[
D_{\rm pol}'(2)\ge
c_2=e^{-B_2}\frac{\tau_*\alpha_0^2}{1-\alpha_0}
>0.0213.
\]

The target-free 1024-bit outward-Arb certificate uses the inherited
100-decimal-digit root bracket and reports 327 relative accuracy bits. It
then gives

\[
M_D(R)>0.0213(R-2)\quad(R>2),
\qquad M_D(R)>0.01065R\quad(R\ge4).
\]

Together with D_pol(sigma)->1 on the positive real axis, this proves that
the same determinant is nonconstant and transcendental entire, with qualitative
maximum-modulus growth beyond every fixed power.

### Route evaluation

Analytic Route-A tuple:

~~~
(A1_WEAK, A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)
~~~

Riemann-target tuple:

~~~
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
~~~

Overall/scoped verdict: ROUTE_A_EXPLORATORY / GO_WITH_LIMITATIONS.
Route B remains unauthorized.

### Strongest evidence

- Signed denominators, repetitions, and matching multiplicities remain on the
  complete ledger; no auxiliary-lambda coefficient or determinant truncation
  is used.
- Two independent audits verified local-uniform differentiation, strict
  real-axis positivity, the pure-left multiplier alpha_0, and the Cauchy
  disk geometry.
- Focused suite: 8/8 passed; generator output is byte-identical to the
  committed certificate under CPython 3.12.3, python-flint 0.9.0, and
  FLINT 3.6.0.

### Strongest failure

No positive or exact order, exponential lower type, zero-count lower bound,
sharp divisor asymptotic, T log T law, arithmetic orbit law, functional
equation, completed-xi divisor, quantization, Route B, Hilbert-Polya, or RH
has been established.

### New reusable knowledge

1. A safe-real-axis positivity proof can retain one exact signed trace term as
   a rigorous lower bound for the same Fredholm determinant without evaluating
   determinant values or roots.
2. A nonzero derivative together with convergence to one on a ray proves
   transcendental-entire status, but does not by itself prove positive order.
3. Certificate metadata must distinguish 1024-bit working precision from the
   effective accuracy inherited from a 100-digit root interval.

### Updated files

- configs/source_locks/LOG-0001-LOWER-GROWTH.yaml
- evaluations/route_a/LOG-0001/20260809T073000Z.yaml
- formal/results/log_0001_lower_growth.md
- experiments/log_0001_lower_growth.py
- artifacts/log_0001_lower_growth/lower_growth_certificate.json
- tests/test_log_0001_lower_growth.py
- docs/candidate_registry.md
- docs/research_clues.md
- docs/research_log.md
- HP_HANDOFF.md
- CHANGELOG.md

docs/obstruction_registry.md and docs/operator_obligations.md are unchanged
because no obstruction was proved and Route B is closed.

### Tests and reproduction

~~~
python3 experiments/log_0001_lower_growth.py --quiet \
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
~~~

Hashes at this checkpoint:

~~~
c11878ebdf6b44c241dcfdbe3dffb663bdc47dea2f47aa553c8f6c2c79aafbbc  artifacts/log_0001_lower_growth/lower_growth_certificate.json
e8df1b54cb8acd3d2b03194cd7e904f9fe0907d5d6e7a571055ab5c73594d44d  experiments/log_0001_lower_growth.py
769900b52ec05e2abdea038c1f19c9285e04ad847bdb45b0177cb3904a57a3cc  formal/results/log_0001_lower_growth.md
f209fd14d2fa4f90f8a8cd840520f300967be2ee123f87fa72ad187aa93b27b9  configs/source_locks/LOG-0001-LOWER-GROWTH.yaml
299252af08dcea038e1399287203268aff05f0a3bdea7656d525352836e7ebde  evaluations/route_a/LOG-0001/20260809T073000Z.yaml
a8e9c48523765a78b6d664f69265c3762b9f74b9862979bc9cf4f2f39cc3b524  tests/test_log_0001_lower_growth.py
~~~

### Claim boundary and next task

Established: D_pol'(2)>0.0213, the two displayed linear maximum-modulus
lower bounds, nonconstant/transcendental-entire status, and qualitative
super-polynomial maximum-modulus growth for the frozen same determinant.

Not established: positive or exact order, exponential lower growth, zero-count
lower bounds, sharp divisor asymptotics, target zeros, functional equation,
completed-xi, quantization, Route B, Hilbert-Polya, or RH.

Next smallest task: create a separate source lock and audit whether finite
order, boundedness on the proved right half-plane, and nonconstancy force
ord(D_pol)>=1 by Phragmen-Lindelöf; then apply the breadth pivot.

Recommended verdict: GO_WITH_LIMITATIONS; overall ROUTE_A_EXPLORATORY.

## 2026-08-08 — LOG-0001 explicit conformal restriction ratios

### Stable checkpoint

Current clue: `CLUE-A1-004`.

Candidate ID: `LOG-0001` (formal candidate).

Source lock:
`configs/source_locks/LOG-0001-CONFORMAL-RATIO.yaml`.

Evaluation:
`evaluations/route_a/LOG-0001/20260808T151232Z.yaml` at source state
`dbb78f10bb3299415e022ecadb20d65e0aac5436`.

Provenance: HP-Dynamics research commit
`80107bc8ec2bcb4b5d0dd7a30447c5bc2d075320`; shared standalone paper-stage
mirror commit `ce0e3c88a3daa32ccf79f7fdeb9c0b22695bc6f5`.

The frozen map, intrinsic roof, radius-`1/1000` operator stadiums,
radius-`3/5000` proof stadiums, matching space, two-stream expansion, and
canonical determinant remain unchanged.  Normalize
`h_sigma:D->U_sigma` at the branch midpoint with positive derivative and set

\[
r_\sigma=
\max_{z\in\overline V_\sigma}|h_\sigma^{-1}(z)|.
\]

With the curvature-`-1` Poincare convention, a midpoint-to-projection path
costs at most `500*pi`, and the projection-to-point disk path costs at most
`log(4)`.  Hence

\[
r_L=r_R\le
\tanh\!\left(\frac{500\pi+\log4}{2}\right)=:r_*<1.
\]

The stable formulas through `t=exp(-(500*pi+log(4)))` give

\[
\delta_*=1-r_*,\qquad \beta_*=-\log r_*.
\]

At 4096-bit outward Arb precision, both begin
`3.2418512480136249798375853005287351e-683`; the certificate retains
positive lower bounds and does not round `r_*` to one.

Using `delta_*` in the inherited two-stream elementary-symmetric bound,
keeping `||ell||<103/125`, choosing `theta=1/4096`, and summing a shifted
Gaussian gives the same determinant the fully numerical envelope

\[
|D_{\rm pol}(s)|\le
\exp\!\left(3.45\times10^{689}
+4.20\times10^{682}(1+|s|)^2\right).
\]

### Route evaluation

Analytic Route-A tuple:

```text
(A1_WEAK, A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)
```

Riemann-target tuple:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
```

Overall/scoped verdict:
`ROUTE_A_EXPLORATORY / GO_WITH_LIMITATIONS`.

Route-B tuple: `(NOT_INVOKED, NOT_INVOKED, NOT_INVOKED, NOT_INVOKED,
NOT_INVOKED)`; invocation remains unauthorized.

### Strongest evidence

- The proof uses only domain monotonicity, exact disk distance, and normalized
  Riemann-map isometry on the frozen stadium pair.
- Translation by `pi/2` proves `r_L=r_R`; the theorem correctly retains the
  non-strict upper comparison `r_sigma<=r_*`.
- An independent adversarial audit verified the Poincare factor, branch
  interval length, boundary path containment, translation normalization,
  shifted-Gaussian constant, and claim boundary.
- The target-free Arb certificate resolves the exponentially small gap with
  more than 1000 relative accuracy bits and certifies both decimal ceilings.

### Strongest failure

The stadium path bound is extremely coarse as a conformal estimate.  It gives
finite proof constants, not the exact ratios or the true determinant type.
There is still no lower growth theorem, sharp divisor asymptotic, arithmetic
orbit law, functional equation, completed-`xi` identity, quantization, or
Route-B object.  No determinant or Riemann roots were computed.

### New reusable knowledge

1. A compact restriction between explicit planar domains can be quantified
   without a numerical conformal solver by bounding hyperbolic distance in the
   outer domain and transporting the result through a normalized Riemann map.
2. For extremely thin domains, compute `1-r` and `-log(r)` through
   `t=exp(-D)`, not by subtracting an ordinary-precision value of
   `tanh(D/2)` from one.
3. The product constant in a geometric elementary-symmetric bound can be
   replaced by the cruder but fully explicit factor `(1-r_*)^(-q)`, which is
   enough for a numerical quadratic envelope.

No obstruction-registry entry is added because no impossibility theorem was
proved. `docs/operator_obligations.md` remains unchanged because A4 fails and
Route B is closed.

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

The standalone paper stage is mirrored under
`logistic_dynamics/projects/exact_uc_polar_conformal_ratio/` in the shared
Hilbert--Polya structure repository.

### Tests

- Focused conformal-ratio suite: `7/7 passed` (`0.123 s`).
- Full repository suite: `258/258 passed` (`93.355 s`).
- Standalone mirror suite: `7/7 passed` (`0.111 s`).
- Standalone manuscript: 5 pages, two clean `pdflatex` passes, zero undefined
  references/citations, zero overfull/underfull boxes, and all fonts embedded.

### Reproduction commands

```bash
python3 experiments/log_0001_conformal_ratio.py \
  --quiet \
  --output artifacts/log_0001_conformal_ratio/conformal_ratio_certificate.json
python3 -m unittest -v tests/test_log_0001_conformal_ratio.py
python3 -m unittest discover -s tests -p 'test_*.py'
python3 -c 'from pathlib import Path; import yaml; fs=list(Path("configs/source_locks").glob("*.yaml"))+list(Path("evaluations").rglob("*.yaml")); [yaml.safe_load(p.read_text(encoding="utf-8")) for p in fs]; print(len(fs))'
git diff --check
sha256sum \
  artifacts/log_0001_conformal_ratio/conformal_ratio_certificate.json \
  experiments/log_0001_conformal_ratio.py \
  formal/results/log_0001_conformal_ratio.md \
  configs/source_locks/LOG-0001-CONFORMAL-RATIO.yaml \
  evaluations/route_a/LOG-0001/20260808T151232Z.yaml \
  tests/test_log_0001_conformal_ratio.py
```

The hashes at this checkpoint are:

```text
005fedd097a054adba0ea303341dee3007e3ad2bdcaf417b7786fc45854babf3  artifacts/log_0001_conformal_ratio/conformal_ratio_certificate.json
d88b6de1691f529eeac82cb51ce67de7a1fe11d9f0adc3daad32b6399470e096  experiments/log_0001_conformal_ratio.py
a731f53d154526befa2b22f1cec6945e4d2c779e80258241a1a216c656d19c75  formal/results/log_0001_conformal_ratio.md
50a615cb60911df144b33804ca4c935aacbeafb6c6541474f3eb39a9fa4cbdcd  configs/source_locks/LOG-0001-CONFORMAL-RATIO.yaml
529a9f2a921180427b8af9642328497461dd409ce8fe05b33fe2802f9310a6d4  evaluations/route_a/LOG-0001/20260808T151232Z.yaml
6d7a8c435de6772845c9e3a3a93302881d7be198fc45e3382ca01cdbc37de984  tests/test_log_0001_conformal_ratio.py
```

### Claim boundary and next task

Established: explicit common conformal-ratio upper bound, positive 4096-bit
gap and logarithmic-rate certificates, and fully numerical constants in the
same determinant's quadratic exponential upper envelope.

Not established: exact conformal ratios, true growth type, lower growth,
sharp divisor asymptotics, arithmetic orbit weights, determinant roots,
functional equation, completed-`xi`, quantization, Route B,
Hilbert--P\'olya, or RH.

Next smallest task: audit whether one explicit nonzero coefficient or signed
trace term supports a cancellation-safe theorem-level lower bound on the same
determinant's maximum modulus.  If no such mechanism is mathematically
explicit, return `NOT_TESTABLE` rather than computing or fitting roots.

Recommended verdict: `GO_WITH_LIMITATIONS`; overall
`ROUTE_A_EXPLORATORY`.

## 2026-08-08 — LOG-0001 quadratic growth and zero-free half-plane

### Stable checkpoint

Current clue: `CLUE-A1-004`.

Candidate ID: `LOG-0001` (formal candidate).

Source lock:
`configs/source_locks/LOG-0001-GROWTH-ORDER.yaml`.

Provenance: HP-Dynamics research commit `ec00bcb`; shared standalone
paper-stage mirror commit `d5ab4b42e66b357859f3b4de560ea5d02bdcf86d`.

The frozen determinant remains

\[
D_{\rm pol}(s)=\det_{\rm Fr}(I-\mathcal L_s|_B).
\]

Normalized Riemann-map Taylor expansions group directly on the matching space
into two geometric rank-one streams. If
`r=max(r_L,r_R)<1`, `W(s)<=exp(0.824*|s|)`, and
`C_r=product_(h>=1)(1-r^h)^(-1)`, then the order-`q` determinant coefficient
is bounded by

\[
q^{q/2}C_r^2(q+1)W(s)^q r^{q^2/4-q/2}.
\]

The negative quadratic rank exponent dominates the `q log q` minor factor.
Continuity of the canonical Grothendieck determinant under the inherited
`p`-nuclear convergence for any `p<2/3` proves

\[
|D_{\rm pol}(s)|
\leq\exp\!\bigl(C_0+C_1(1+|s|)^2\bigr).
\]

Thus the classical entire-function order is at most two. Jensen's formula on
an outer circle of radius `2R` gives `O(R^2)` zeros in the inner radius-`R`
disk and hence `O(T^2)` zeros in every fixed real strip through height `T`.

With

\[
\alpha_0=\frac{U_c^2}{4},
\qquad
\tau_*=\log\frac4{U_c^2},
\]

the exact signed trace ledger gives an absolutely convergent `lambda=1`
trace logarithm for

\[
\Re s>
\frac{\log2}{\log(4/U_c^2)}
=1.3382657903899534315\ldots.
\]

The determinant is zero-free in this open half-plane. Every closed
sub-half-plane above the threshold has uniform upper and lower modulus bounds;
there is no single uniform bound asserted all the way down to the open
boundary.

### Route evaluation

Analytic Route-A tuple:

```text
(A1_WEAK, A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)
```

Riemann-target tuple:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
```

Route-B tuple: `(NOT_INVOKED, NOT_INVOKED, NOT_INVOKED, NOT_INVOKED,
NOT_INVOKED)`; invocation is not authorized.

### Strongest evidence

The proof stays on the same determinant and preserves the signed trace
ledger. An adversarial audit verified the two-stream count, the
`q^2/4-q/2` exponent, Hadamard minor factor, `p<2/3` determinant limit,
`lambda`-disk continuation, nonnegative-real-part trace bound, closed
sub-half-plane wording, and Jensen outer radius. The target-free 100-digit
certificate checks `alpha_0`, `tau_*`, the zero-free threshold, the safe line
`Re(s)=2`, `||ell||<0.824`, and all two-stream allocations through `q=24`.

### Strongest failure

No exact order, lower growth bound, sharp fixed-strip asymptotic, or
`T log T` theorem is known. The `O(T^2)` upper bound neither establishes nor
excludes Riemann--von Mangoldt growth. No log-prime/von-Mangoldt orbit law,
functional equation, completed-`xi` identity, quantization, Route B, or root
comparison exists.

### New reusable knowledge

1. Two geometric nuclear streams with `exp(O(|s|))` parameter weights yield
   Gaussian determinant-coefficient decay and an `exp(O(|s|^2))` envelope.
2. A positive roof lower bound can push the exact signed trace logarithm to
   `lambda=1` in a right half-plane and prove zero-freeness there.
3. Finite order and an upper zero-count bound do not supply a sharp divisor
   law; a lower/asymptotic theorem is a separate obligation.

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

`docs/operator_obligations.md` is unchanged because A4 fails and Route B is
not authorized.

### Tests

- LOG-0001 growth focused suite: `7/7 passed` (`0.099 s`).
- Full repository suite: `251/251 passed` (`93.385 s`).
- YAML load and `git diff --check`: passed.

### Reproduction commands

```bash
python3 experiments/log_0001_growth_order.py \
  --quiet \
  --output artifacts/log_0001_growth_order/growth_order_certificate.json
python3 -m unittest -v tests/test_log_0001_growth_order.py
python3 -m unittest discover -s tests -p 'test_*.py'
git diff --check
sha256sum \
  artifacts/log_0001_growth_order/growth_order_certificate.json \
  experiments/log_0001_growth_order.py \
  formal/results/log_0001_growth_order.md \
  configs/source_locks/LOG-0001-GROWTH-ORDER.yaml \
  evaluations/route_a/LOG-0001/20260808T104049Z.yaml \
  tests/test_log_0001_growth_order.py
```

The hashes at this checkpoint are:

```text
9e28833c0b68aabc5e9fc2d771d7e7d2c7a6ffca8e2cd6abdbb3a7dd430120ec  artifacts/log_0001_growth_order/growth_order_certificate.json
5e2a9ef910371a7992734b70fd4f4465696932403361d53992c89f1f72bd0620  experiments/log_0001_growth_order.py
b005e0d0c43f31af638c9ae91c12db03a0ab450d0cb25616682a234931cc3efc  formal/results/log_0001_growth_order.md
4a2493ae51ebce6812e05f48330ab71b161c8cad68d540f9bd3416f63b29181e  configs/source_locks/LOG-0001-GROWTH-ORDER.yaml
3101db5692fffe06eed65abc7cce0adf47f72b49bce5a5a61257aaa68bf4848c  evaluations/route_a/LOG-0001/20260808T104049Z.yaml
350b70508baf8362422b95944908ec3a2dcf0f7d8faee43ad2d2f33b273e437c  tests/test_log_0001_growth_order.py
```

### Claim boundary and next task

Established: same-object classical order at most two, `O(T^2)` disk and
fixed-strip divisor upper bounds, and a zero-free right half-plane with
uniform bounds on every closed sub-half-plane above its threshold.

Not established: arithmetic orbit weights, determinant roots, exact order,
lower or sharp divisor asymptotics, functional equation, completed-`xi`,
target zeros, quantization, Route B, Hilbert--P\'olya, or RH.

Next smallest task: certify explicit numerical upper bounds for the normalized
conformal restriction ratios `r_L,r_R` of the frozen stadium pair, turning the
parameterized quadratic-type constant into a numerical certificate without
computing determinant roots.

Recommended verdict: `GO_WITH_LIMITATIONS`; overall
`ROUTE_A_EXPLORATORY`.
## 2026-08-10 — TH-0001 on-shell caustic incidence audit

- Candidate/clue: `TH-0001` / `CLUE-A4-001`.
- Source lock: `configs/source_locks/TH-0001-PHASE-CAUSTIC-REAL.yaml`.
- Evaluation: `evaluations/route_a/TH-0001/20260810T074238Z.yaml`.
- Result: the exact caustic `15*q1*q2=1` is attained by every real nonzero-
  `t` stationary branch. The endpoint projection Jacobian is `-H_int`.
- Witness: `t=1` gives `(q0,q1,q2,q3)=(-17/30,1,1/15,-1/90)` and
  `(p0,p1,p2,p3)=(-289/1800,-17/30,1,1/15)`, with all six kick residuals zero;
  the Hessian rank is one and the null-direction third derivative is `132`.
- Route-A tuple remains `(A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`;
  target tuple remains `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`.
- Interpretation: this is a scoped strengthening of `OBR-011`, not a new
  independent obstruction. No determinant, spectrum, zero, or Route-B work is
  authorized.
- Reproduction:

  ```bash
  python3 experiments/th_0001_phase_caustic_real.py --quiet \
    --output artifacts/th_0001/phase_caustic_real_audit.json
  python3 -m unittest -v tests/test_th_0001_phase_caustic_real.py
  ```

- Next smallest task: stop this sub-audit; reopen only with an explicit
  multi-chart phase/Maslov transition source lock, or pivot breadth-first.

## 2026-08-10 — CLUE-A4-002 irrational-roof bouquet prefilter

The project-level breadth pivot selected one explicit, target-free,
non-Selberg countable suspension before allocating `SS-0003`:

\[
\Sigma=\bigsqcup_{n\ge2}\mathbb Z/n\mathbb Z,
\quad \sigma(n,j)=(n,j+1),
\quad \tau_n=1+\sqrt2/n,
\quad \phi_n=-n.
\]

The transfer family is the weighted cyclic block shift on counting-measure
`ell^2(Sigma)`, and its only determinant ledger is

\[
D_{\rm bouquet}(s)=\det_{\rm F}(I-\mathcal L_s)
=\prod_{n\ge2}(1-e^{-n^2-s(n+\sqrt2)}).
\]

This is an audit (`formal_candidate: false`), not `SS-0003`.  The exact
primitive/repetition ledger has one primitive `n`-cycle per component and

\[
\operatorname{tr}(\mathcal L_s^k)
=\sum_{n\mid k,\,n\ge2}n e^{-kn-sk(1+\sqrt2/n)}.
\]

The determinant is entire and its zeros are
\(s_{n,k}=-(n^2+2\pi i k)/(n+\sqrt2)\).  Their real parts decrease to
`-infinity`, so every bounded vertical strip has `O(T)` zeros.  The period set
has no common lattice, but the base is disconnected and not mixing; this is
not an arithmetic or thermodynamic positive result.

Route-A result:

```text
(A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)
Riemann target: (A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
verdict: STOP_SCOPED; overall ROUTE_A_REJECTED; Route B not authorized
```

The reusable obstruction is `OBR-016`: countability, entire nuclearity, and
global roof incommensurability do not force a `T log T` divisor when cycle
actions escape each fixed strip.  The next smallest task, if this clue is
reopened, is a connected/renewal object with a fresh source lock and an
intrinsic same-ledger divisor theorem; no root search is allowed.

Artifacts:

- `configs/source_locks/SS-PREFILTER-IRRATIONAL-BOUQUET.yaml`
- `evaluations/route_a/SS-PREFILTER-IRRATIONAL-BOUQUET/20260810T162243Z.yaml`
- `experiments/ss_prefilter_irrational_bouquet.py`
- `artifacts/ss_prefilter_irrational_bouquet/audit.json`
- `formal/results/ss_prefilter_irrational_bouquet.md`
- `formal/obstructions/countable_irrational_bouquet_linear_divisor.md`
- `tests/test_ss_prefilter_irrational_bouquet.py`
