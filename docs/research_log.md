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
