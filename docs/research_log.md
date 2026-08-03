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
