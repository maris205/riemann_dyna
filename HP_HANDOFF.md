# HP-Dynamics Handoff

## Current status

The legacy non-autonomous Logistic direction has been reopened as a
pre-candidate numerical audit.

- Active clue: `CLUE-A2-005`
- Formal candidate: none
- Pre-candidate status: `NOT_TESTABLE`
- Diagnostic Route-A tuple:
  `(A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`
- Recommended verdict: `REVISE`
- Route B: inactive and not authorized

The latest formal candidate remains `SS-0002`, which is `STOP_SCOPED` under
`OBR-006`. Do not reuse `SS-0003` for the Logistic line until an explicit
mathematical determinant, clock and moving-cutoff object have been defined.

## Current entry files

- `docs/HP_Dynamics_Project_Entry.md`
- `docs/main_agent_rules.md`
- `docs/research_clues.md`
- `.agents/skills/route-a-evaluator/SKILL.md`
- `.agents/skills/route-b-evaluator/SKILL.md`
- `docs/prior_work/logistic_legacy_pre_audit.md`

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

## Strongest evidence

The stored selected micro run has a real finite-prefix numerical alignment:

- fitted zeros 2--6: MAE `0.3494`, mean relative error `1.34%`;
- zero 1 fixes the scale.

A target-free reduced deterministic profile also showed that, with fixed
starts and tolerance `1e-10`, ARPACK can reproduce the dense top-40 spectrum
with matching error below `3.7e-10` and eigen-residuals below `3.8e-15`.

This preserves the Logistic line as a useful numerical benchmark and a search
prior for a later autonomous slow-variable lift.

## Strongest failure

The saved prefix is training-only:

- zeros 2--6 select `epsilon=0.001916` and the displayed eigensolver run;
- zero 20 enters the selection score through a reward for a large error;
- the macro schedule family was optimized against the first 100 zeros;
- repeated `eigs` calls on one matrix are solver restarts, not a physical
  ensemble.

Retrospective errors grow immediately:

- zeros 7--20: MAE `7.4162`, mean relative error `11.49%`;
- zeros 21--85: MAE `61.7317`, mean relative error `39.84%`.

In the target-free `128 bins x 1000 steps` smoke profile, five of the first six
phase-ranked modes had

\[
|\lambda|<10^{-3}.
\]

Only four of fourteen selected upper-half top-40 modes exceeded that threshold.
A half-bin partition shift moved the 13 resolved modes by median complex
distance `0.00943`, 90th percentile `0.0883`, and maximum `0.15275`.

The current “small phase equals low energy” rule is therefore not a frozen,
stable spectral observable.

## Source locks and artifacts

- Legacy audit lock:
  `configs/source_locks/P4-LOGISTIC-LEGACY-AUDIT.yaml`
- Deterministic smoke lock:
  `configs/source_locks/P4-LOGISTIC-DETERMINISTIC-SMOKE.yaml`
- Saved-evidence audit:
  `artifacts/p4_logistic_legacy/route_a_pre_candidate_audit.json`
- Target-free smoke profile:
  `artifacts/p4_logistic_legacy/deterministic_smoke_profile.json`
- Detailed audit:
  `docs/prior_work/logistic_legacy_pre_audit.md`

No entry was added to `docs/candidate_registry.md`, no Route-A candidate YAML
was created, and `docs/operator_obligations.md` remains unchanged.

## Reproduction commands

```bash
python3 -m unittest -v \
  tests/test_p4_logistic_legacy_audit.py \
  tests/test_p4_logistic_deterministic_smoke.py
python3 experiments/p4_logistic_legacy_audit.py \
  --output artifacts/p4_logistic_legacy/route_a_pre_candidate_audit.json
python3 experiments/p4_logistic_deterministic_smoke.py \
  --output artifacts/p4_logistic_legacy/deterministic_smoke_profile.json
```

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
- numerical failure of the current phase-ranking rule under modulus and
  partition diagnostics.

Not established:

- an honest validation or sealed zero test;
- intrinsic primitive periodic orbits of the non-autonomous object;
- a rational-prime or von-Mangoldt clock;
- a dynamical Zeta or Fredholm determinant;
- a moving-cutoff infinite-operator limit;
- analytic continuation or completed-`xi` divisor equality;
- natural quantization, Route B, Hilbert--Polya, or RH.

## Next smallest task

Implement one medium-fidelity, target-free branch audit with physical epsilon
fixed rather than `epsilon/dx` fixed:

1. save and hash the raw (T) matrix;
2. construct (Q=D^{-1}T) and (B=TD^{-1});
3. freeze `v0`, `k`, `ncv`, tolerance and maximum iterations;
4. report all requested eigenvalue moduli and residuals;
5. track residual-certified branches by complex-plane matching across bins,
   steps and a half-bin partition shift;
6. compare a static Logistic control using the identical estimator;
7. do not inspect new zero-match metrics until mode identities are frozen.

If no stable branch identity survives, record a reusable numerical
mode-selection/occupation-aggregation obstruction and stop this scoped phase
route. If stable branches survive, define the autonomous slow-variable lift or
the transfer-cocycle determinant before creating a formal candidate.
