# HP-Dynamics Handoff

## Current status

The legacy non-autonomous Logistic strong-layer empirical phase observable has
completed its target-free-computation, physical-epsilon robustness audit.

- Active clue: `CLUE-A2-005`
- Clue state: `BLOCKED`
- Formal candidate: none
- Route-A status: `NOT_TESTABLE`
- Diagnostic Route-A tuple:
  `(A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`
- Empirical phase-observable verdict: `STOP_SCOPED`
- Route B: inactive and not authorized

The latest formal candidate remains `SS-0002`, which is `STOP_SCOPED` under
`OBR-006`. Do not reuse `SS-0003` for the Logistic line until an explicit
mathematical determinant, clock and moving-cutoff object have been defined.

The `STOP_SCOPED` verdict is narrower than the Route-A status. It retires only
the frozen occupation-aggregated strong-layer phase observable. Route A remains
`NOT_TESTABLE` because no primitive-orbit Zeta or Fredholm determinant exists.

## Current entry files

- `docs/HP_Dynamics_Project_Entry.md`
- `docs/main_agent_rules.md`
- `docs/research_clues.md`
- `.agents/skills/route-a-evaluator/SKILL.md`
- `.agents/skills/route-b-evaluator/SKILL.md`
- `docs/prior_work/logistic_legacy_pre_audit.md`
- `configs/source_locks/P4-LOGISTIC-MEDIUM-PHYSICAL-EPSILON.yaml`
- `artifacts/p4_logistic_medium/branch_audit.json`

## Current clue

The legacy micro notebook evolves

\[
x_{n+1}=1-\mu_nx_n^2,
\qquad
\mu_n=u_c+\frac{k}{\log^2(n+10)},
\]

and accumulates an occupation-conditioned empirical flux matrix

\[
T_{ij}=\sum_n V_n(i)K_n(i,j).
\]

The correct Markov surrogate is (Q=D^{-1}T), where
(D=\operatorname{diag}(T\mathbf1)). The legacy CSR code instead computes

\[
B=TD^{-1}=DQD^{-1}.
\]

Thus the normalization is wrong for Markov interpretation but does not alter
the exact eigenvalue multiset. Its practical danger is the conditioning and
nonnormality induced by a highly nonuniform occupation diagonal.

The reported legacy observable is not a dynamical determinant. It retains
upper-half-plane matrix eigenvalues, discards their moduli, sorts principal
phases, and fixes a phase-to-height scale with the first Riemann zero. The
occupation aggregate also erases chronological cocycle order.

The completed medium audit removed the phase-to-height scale and read no zero,
prime, or USTC table. It nevertheless inherits `epsilon=0.001916`, which was
historically selected using zeros 2--6. This is therefore a robustness audit,
not blind arithmetic validation.

## Strongest evidence

The frozen `2048 bins x 100000 steps` reference contains four
residual-certified upper-half strong branches. They reproduce across:

- time prefixes `50000/100000/200000` from one schedule;
- bin counts `1536/2048/3072`;
- `k=300/450`;
- fixed ones and seed-17 ARPACK starts;
- the correct (Q) and diagonally similar legacy (B) matrices;
- raw-matrix reconstruction and save/load content hashes.

Separately, dense and sparse eigensolvers agree on all 23 strong upper-half
branches of the `256 bins x 5000 steps` physical-epsilon anchor. That anchor is
a solver check on its own matrix, not a match to the four reference branches.

Every mechanics gate passes, including convergence with all `450/450` Ritz
values, residuals, mass, row sums, static-kernel identity, strong/moderate
conjugacy, and all-profile edge saturation. The reference `k=450` edge modulus
is `0.00225768`.

## Strongest failure

Only four reference strong branches exist, below the preregistered minimum 20.
Across every internal profile, only three of the four pass all stability gates,
for stable survival `0.75`.

The half-bin translated-domain control produces five strong branches. Its
matched branches have median/p90/max normalized drift
`0.028783/0.046071/0.051659`, maximum phase drift `0.033001`, and phase-rank
median/max displacement `1/1`; the frozen phase/rank gate fails.

The same four dynamic branches are much closer to preregistered static-parent
spectra than to internal perturbation uncertainty:

- median nearest-static normalized distance: `0.0009477`;
- median dynamic/static margin: `0.03789`;
- fraction with margin at least `1.5`: `0`.

Thus reproducible finite-matrix modes do not provide a distinct, stable phase
observable under this source lock.

## Source locks and artifacts

- Legacy audit lock:
  `configs/source_locks/P4-LOGISTIC-LEGACY-AUDIT.yaml`
- Deterministic smoke lock:
  `configs/source_locks/P4-LOGISTIC-DETERMINISTIC-SMOKE.yaml`
- Physical-epsilon medium lock, version 2:
  `configs/source_locks/P4-LOGISTIC-MEDIUM-PHYSICAL-EPSILON.yaml`
- Saved-evidence audit:
  `artifacts/p4_logistic_legacy/route_a_pre_candidate_audit.json`
- Target-free smoke profile:
  `artifacts/p4_logistic_legacy/deterministic_smoke_profile.json`
- Medium branch audit:
  `artifacts/p4_logistic_medium/branch_audit.json`
- Raw reference matrices:
  `artifacts/p4_logistic_medium/raw/dynamic_reference_T.npz` and
  `artifacts/p4_logistic_medium/raw/static_mean_matched_T.npz`
- Detailed audit:
  `docs/prior_work/logistic_legacy_pre_audit.md`

No entry was added to `docs/candidate_registry.md`, no Route-A candidate YAML
was created, and `docs/operator_obligations.md` remains unchanged. No new
obstruction number was minted because this is one source lock's numerical
failure, not a family-level theorem.

## Reproduction commands

```bash
python3 -m unittest -v \
  tests/test_p4_logistic_legacy_audit.py \
  tests/test_p4_logistic_deterministic_smoke.py
python3 experiments/p4_logistic_legacy_audit.py \
  --output artifacts/p4_logistic_legacy/route_a_pre_candidate_audit.json
python3 experiments/p4_logistic_deterministic_smoke.py \
  --output artifacts/p4_logistic_legacy/deterministic_smoke_profile.json
python3 -m unittest -v tests/test_p4_logistic_medium_branch_audit.py
python3 experiments/p4_logistic_medium_branch_audit.py \
  --output artifacts/p4_logistic_medium/branch_audit.json \
  --raw-directory artifacts/p4_logistic_medium/raw \
  > /tmp/p4_logistic_medium_stdout.json
python3 -m unittest discover -v
git diff --check
```

Medium-audit reference runtime: CPython `3.12.3`, NumPy `2.4.4`, SciPy
`1.16.1`, Numba `0.66.0`, llvmlite `0.48.0`.

The earlier formal-candidate commands remain:

```bash
python3 -m unittest -v tests/test_ss_0001_mod6_cayley.py
python3 -m unittest -v tests/test_ss_0002_commutator_mayer.py
```

## Claim boundary

Established:

- exact source and target-use provenance for the two proposed legacy notebooks;
- the fitted-prefix and retrospective-error metrics;
- the diagonal-similarity normalization identity;
- deterministic dense/ARPACK agreement on a reduced target-free profile;
- exact raw-matrix repeat hashes and expanded solver/mechanics controls at the
  medium physical-epsilon cutoff;
- four reproducible strong branches across time and bin cutoffs;
- scoped failure of the current strong-layer phase observable under branch
  count, translated-grid phase ranking, and identical-estimator static-parent
  separation.

Not established:

- an honest validation or sealed zero test;
- a target-independent choice of `epsilon`;
- intrinsic primitive periodic orbits of the non-autonomous object;
- a rational-prime or von-Mangoldt clock;
- a dynamical Zeta or Fredholm determinant;
- a moving-cutoff infinite-operator limit;
- analytic continuation or completed-`xi` divisor equality;
- natural quantization, Route B, Hilbert--Polya, or RH.

## Next smallest task

The active empirical observable is `STOP_SCOPED`, so there is no further task
inside `CLUE-A2-005`. Do not inspect new zero-match metrics.

The Logistic direction may reopen only when an explicit new object is supplied:

1. an autonomous slow-variable lift with chronological primitive orbits; or
2. a chronological transfer-cocycle/Fredholm determinant with a frozen clock,
   normalization, cutoff, and determinant convention.

Absent such an object, the next queued repository-backed task is the
`CLUE-A2-001` synthetic Euler-product positive control. Because the active
observable is `STOP_SCOPED`, this handoff is a stable stopping checkpoint rather
than authorization to continue the Logistic phase fit.
