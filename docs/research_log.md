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
