# Prior-Work Claims Matrix

This document is the authoritative claim ledger for the five papers preceding the HP-Dynamics project.

Its purpose is to prevent:

- reuse of superseded claims;
- confusion between theorem, conditional theorem, numerical experiment, heuristic, modeling choice, and fitted result;
- inflation of finite spectral agreement into a Hilbert–Pólya realization;
- loss of provenance when legacy code is refactored.

---

## 1. Status legend

| Status | Definition |
|---|---|
| `ESTABLISHED_EXTERNAL` | Standard result proved in cited literature |
| `PROVED_IN_PAPER` | The paper presents a proof intended to establish the claim |
| `CONDITIONAL_THEOREM` | Proved only under explicit hypotheses or conjectures |
| `NUMERICALLY_CERTIFIED` | Rigorous numerical enclosure with controlled error |
| `NUMERICAL_OBSERVATION` | Finite numerical evidence without proof-level certification |
| `HEURISTIC` | Motivated analogy or structural/physical interpretation |
| `CONJECTURE` | Explicit unproved mathematical claim |
| `MODELING_CHOICE` | Chosen system, schedule, regularizer, or parameterization |
| `FITTED_PARAMETER` | Chosen by optimization against target data |
| `SUPERSEDED` | Replaced by a later, more precise formulation |
| `REFUTED` | Disproved by a later counterexample or contradiction |
| `PROJECT_DECISION` | Rule adopted by HP-Dynamics |
| `OPEN` | Unresolved problem |

---

## 2. Authority rules

1. A later correction overrides an earlier incompatible claim.
2. The paper text overrides informal summaries.
3. A proof claim must still be checked for assumptions and gaps.
4. Very small numerical error remains numerical evidence.
5. A fitted parameter must not be described as emergent or predicted.
6. Similar error curves do not establish a shared physical mechanism.
7. GUE-like statistics do not identify a unique Riemann system.
8. This matrix may be updated after proof audit or failed reproduction.

---

# 3. Paper 1 — Prime–Chaos framework

**Source**

```text
papers/01_prime_chaos.pdf
legacy/paper1_prime_chaos/
```

**Role:** arithmetic-symbolic prior and historical starting point.

| ID | Claim | Paper status | Current status | Use in HP-Dynamics | Required action |
|---|---|---:|---:|---|---|
| P1-C01 | The sieve is represented by symbolic operators `S_p = R L^(p-1)` with a destruction-priority composition rule. | `MODELING_CHOICE` with exact definition | Accepted definition | Symbolic baseline | Unit-test sieve words |
| P1-C02 | The limiting sieve sequence is topologically isomorphic to the Logistic kneading sequence at `u_c ≈ 1.543689`. | `CONJECTURE` | `CONJECTURE`, weakened by Paper 2 | Search prior only | Do not use as theorem |
| P1-C03 | Every finite sieve stage is kneading-admissible inside `N < p_(k+1)^2`. | Hypothesis/conjecture | `REFUTED` by Paper 2 | Negative regression test | Reproduce `Q3`, `Q5` defects |
| P1-C04 | The selected band-merging skeleton exhibits parity rigidity. | Analytic/numerical model claim | Retained with model scope | Baseline invariant | Reproduce symbolic/orbit tests |
| P1-C05 | The relevant topological entropy is `log(2)/2`. | Presented analytically | Proof audit required | Baseline invariant | Derive independently |
| P1-C06 | The Lyapunov exponent near the selected parameter is about `0.34`. | `NUMERICAL_OBSERVATION` | `NUMERICAL_OBSERVATION` | Regression metric | Recompute with precision report |
| P1-C07 | Logarithmic aging can reconcile stationary dynamics with decreasing prime density. | `HEURISTIC` / `MODELING_CHOICE` | `HEURISTIC`, constrained by Paper 3 | Candidate schedule prior | Separate density mechanism from Birkhoff convergence |
| P1-C08 | The twin-prime constant is numerically recovered to high precision. | `NUMERICAL_OBSERVATION` | `NUMERICAL_OBSERVATION` | Regression observable | Reproduce frozen configuration |
| P1-C09 | Prime randomness belongs to a weak-chaos universality class. | `HEURISTIC` | `HEURISTIC` | Motivation | No proof-level wording |
| P1-C10 | The 1D Logistic map is a complete host for prime arithmetic. | Strong interpretation | `SUPERSEDED` by Paper 2 | None | Replace by “low-dimensional projection” |

**Compressed interpretation**

```text
Keep: symbolic sieve, critical-dynamics prior, parity observable, aging hypothesis.
Reject: universal finite-stage admissibility and complete 1D realization.
```

---

# 4. Paper 2 — Transient chaos and topological bounds

**Source**

```text
papers/02_transient_chaos_topological_bounds.pdf
legacy/paper2_transient_chaos/
```

**Role:** self-correction, finite-stage obstruction, and dimensional-limit analysis.

| ID | Claim | Paper status | Current status | Use | Required action |
|---|---|---:|---:|---|---|
| P2-C01 | `Q3` violates MSS admissibility at the defect associated with `n = 31`. | `PROVED_IN_PAPER` | Retained, audit/reproduce | Core regression | Exact symbolic test |
| P2-C02 | `Q5` violates MSS admissibility near the `113–127` prime gap. | `PROVED_IN_PAPER` | Retained, audit/reproduce | Core regression | Exact symbolic test |
| P2-C03 | Paper 1's universal finite-stage admissibility hypothesis is false. | `PROVED_IN_PAPER` | `REFUTED` status for P1-C03 | Precedence rule | Encode in tests/docs |
| P2-C04 | Tightening generic classical prime-gap bounds does not repair the explicit parity-lex defects. | Structural proof | Retained subject to audit | Negative constraint | Add counterexample tests |
| P2-C05 | The Parity-Gap Lemma links a defective shift to a gap of at least `p_(k+1)-1`. | `PROVED_IN_PAPER` | Retained subject to audit | Structural lemma | Independently verify proof |
| P2-C06 | `G(p_(k+1)^2) < p_(k+1)-1` is sufficient for admissibility of the finite sieve word. | `PROVED_IN_PAPER` corollary | Retained | Conditional filter | Unit-test finite cases |
| P2-C07 | A Cramér-type polylog gap bound implies eventual admissibility. | `CONDITIONAL_THEOREM` | `CONDITIONAL_THEOREM` | Context | Preserve hypothesis |
| P2-C08 | The observed threshold is `k0 = 6` through `k <= 5000`. | `NUMERICAL_OBSERVATION` | `NUMERICAL_OBSERVATION` | Regression benchmark | Re-run independently |
| P2-C09 | Topological-defect density vanishes asymptotically. | Presented as asymptotic result | Proof audit required | Macroscopic prior | Separate theorem from finite scan |
| P2-C10 | Only `Q3` and `Q5` are defective for `k <= 5000`. | `NUMERICAL_OBSERVATION` | `NUMERICAL_OBSERVATION` | Regression benchmark | Reproduce dataset |
| P2-C11 | Odd gaps have zero invariant measure in the stated 1D model. | `PROVED_IN_PAPER` under model assumptions | `PROVED` on the physical core, with a corrected band-swap proof; ambient odd branches exist but have zero invariant mass | Parity baseline | Preserve the ambient/core domain distinction |
| P2-C12 | Even-gap measures decay asymptotically geometrically. | `CONDITIONAL_THEOREM` using spectral ingredients | Ratio-limit subclaim `PROVED` for the physical exact-$U_c$ acip; a coarse cone enclosure now certifies selected absolute masses, while the stronger geometric asymptotic with exponential remainder remains `OPEN` and the legacy ordinary-`BV` proof is `REFUTED` | Corrected physical mass-ratio theorem only | Cite the direct density and cone proofs; do not claim the old exponential remainder, sharp finite-$n$ weights, or a determinant |
| P2-C13 | The 1D model has no internal mechanism for full Hardy–Littlewood mod-3 resonance. | Structural conclusion | `HEURISTIC`; repairing P2-C12 does not prove the stronger mod-3 impossibility claim | Higher-rank motivation only | Do not cite as a theorem; test the actual weighted residue modes directly |
| P2-C14 | The Logistic construction is an abelian/mod-2 holographic projection. | `HEURISTIC` supported by structure | Project prior | Candidate guidance | Do not call theorem |
| P2-C15 | A higher-dimensional/higher-mode lift is the main next problem. | `OPEN` | `PROJECT_DECISION` | Defines project direction | Implement Track A/B/C |

**Interpretation change**

```text
from: candidate complete arithmetic realization
to:   low-dimensional symbolic projection and search prior
```

**2026-08-04 later correction**

- The physical core (J=[1-U_c,1]) has exact first-return support
  (2\mathbb N), with one nondegenerate interval branch per even label.
- The literal ambient interval `[-1,1]` has topological support
  ℕ because transient odd branches fill `[-1,1-U_c)`; every invariant
  probability gives them zero mass.
- The MSS proof of the old parity lemma had its inequality interpretation
  reversed; the conclusion is repaired by the exact band swap.
- The unaccelerated first-return map has derivative infimum zero on every
  branch. Consequently the stated ordinary-`BV` uniform-expansion and spectral
  argument does not prove P2-C12.
- The ratio-limit portion of P2-C12 is nevertheless repaired by the direct
  physical-density theorem
  \(h(-\rho+t)=h(0)(\sqrt2U_c)^{-1}t^{-1/2}+O(1)\), which gives
  \(\mu(C_{2n+2})/\mu(C_{2n})\to1/[2U_c(U_c-1)]\). This does not restore the
  refuted ordinary-`BV` spectral gap or prove the stronger exponential
  remainder/full P2-C12 statement.

---

# 5. Paper 3 — Sequential Birkhoff theorem

**Source**

```text
papers/03_sequential_birkhoff.pdf
legacy/paper3_sequential_birkhoff/
```

**Role:** conditional analytic control of slow non-autonomous drift.

| ID | Claim | Paper status | Current status | Use | Required action |
|---|---|---:|---:|---|---|
| P3-C01 | Under Assumption 1.1 and `u_n -> u_c`, time averages converge in mean and `L2` to the `u_c` invariant average. | `CONDITIONAL_THEOREM` | `CONDITIONAL_THEOREM` | Candidate filter | Audit every assumption |
| P3-C02 | For logarithmic drift with `beta > 1`, convergence holds almost everywhere by the stated argument. | `CONDITIONAL_THEOREM` | `CONDITIONAL_THEOREM` | Strong schedule filter | Preserve `beta > 1` |
| P3-C03 | For `0 < beta <= 1`, almost-everywhere convergence is not proved by the paper. | Explicit limitation | Accepted limitation | Prevent overstatement | Add docs/test warning |
| P3-C04 | Uniform inducing, expansion, bounded distortion, exponential tails, spectral gap, Keller–Liverani stability, and raw-operator stability are required. | Explicit assumptions | Required checklist | Hard filter | Build diagnostics |
| P3-C05 | The application is on a one-sided/tower-supporting parameter set, not an arbitrary two-sided neighborhood. | Explicit limitation | Accepted limitation | Domain rule | Reject unjustified scans |
| P3-C06 | Density stability is numerically consistent with an exponent near `1/2`. | `NUMERICAL_OBSERVATION` | `NUMERICAL_OBSERVATION` | Regression metric | Reproduce with uncertainty |
| P3-C07 | Sequential convergence is observed numerically for tested schedules. | `NUMERICAL_OBSERVATION` | `NUMERICAL_OBSERVATION` | Regression metric | Re-run across precision/seeds |
| P3-C08 | The theorem itself produces a `1/log n` prime-density envelope. | Explicitly denied | Refuted interpretation | None | Warning in schedule API |
| P3-C09 | A shrinking-target, weighted/thinned estimator, or external aging mechanism is still required for a non-stationary envelope. | Scope/open statement | `OPEN` | New research task | Track separately |

**Required candidate checklist**

```text
[ ] Reference domain and induced map defined
[ ] Uniform expansion
[ ] Uniform distortion bound
[ ] Controlled return-time tails
[ ] Banach space specified
[ ] Uniform spectral gap
[ ] Keller–Liverani stability
[ ] Raw-map stability
[ ] Valid parameter set identified
[ ] Exact convergence mode stated
```

---

# 6. Paper 4 — Non-autonomous Logistic spectral experiments

**Source**

```text
papers/04_non_autonomous_riemann_spectrum.pdf
legacy/paper4_riemann_logistic/
```

**Role:** historical numerical baseline, ablation source, and cautionary example.

| ID | Claim | Paper status | Current status | Use | Required action |
|---|---|---:|---:|---|---|
| P4-C01 | A logarithmically cooled quadratic map is converted into a finite empirical transfer matrix. | `MODELING_CHOICE` | `MODELING_CHOICE` | Baseline | Reproduce exactly |
| P4-C02 | Gaussian kernel splatting with scale `epsilon` regularizes grid transport. | `MODELING_CHOICE` | `MODELING_CHOICE` | Numerical baseline | Compare with alternatives |
| P4-C03 | The smoothing scale is optimized on the first six zeros. | `FITTED_PARAMETER` | `FITTED_PARAMETER` | Overfitting case study | Enforce split firewall |
| P4-C04 | A zero is used to set a global phase-to-energy scale in part of the analysis. | Anchoring choice | `MODELING_CHOICE` | Baseline only | Record all anchors |
| P4-C05 | Several low predicted levels align closely with low Riemann zeros. | `NUMERICAL_OBSERVATION` | `NUMERICAL_OBSERVATION` | Reproduction target | Evaluate out of sample |
| P4-C06 | A residual near `N ≈ 20` resembles a reported experimental anomaly. | `NUMERICAL_OBSERVATION` | Qualitative observation | Null-test target | Statistical comparison |
| P4-C07 | The resemblance proves a shared topological mechanism. | Strong interpretation | Unsupported | None | Must not repeat |
| P4-C08 | Full conjugate-spectrum fitting yields an intercept near zero. | Fitted numerical result | `NUMERICAL_OBSERVATION` / fitted result | Symmetry ablation | Test on held-out data |
| P4-C09 | The intercept proves a physical negative-energy completion. | `HEURISTIC` | Unsupported heuristic | Inspiration only | No proof-level use |
| P4-C10 | The model globally reproduces the Riemann spectrum. | Strong interpretation | Not established | Research hypothesis | Require blind UPO–Zeta validation |
| P4-C11 | The finite matrix is a Hilbert–Pólya operator. | Not proved | Refuted interpretation | None | Keep spectral objects separate |
| P4-C12 | The logarithmic schedules and higher-order terms are unique first-principles laws. | Strong wording vs optimized construction | `MODELING_CHOICE` / `FITTED_PARAMETER` | Search ansatz only | Complexity/ablation tests |

**Project question for Paper 4**

```text
Which observations survive strict train/test separation,
shuffled-period controls, random weights, precision scaling,
and replacement of finite-matrix eigenphases by a UPO determinant?
```

---

# 7. Paper 5 — Area-preserving Hénon model

**Source**

```text
papers/05_area_preserving_henon.pdf
legacy/paper5_henon/
```

**Role:** conservative-lifting baseline and mother template for Route A.

| ID | Claim | Paper status | Current status | Use | Required action |
|---|---|---:|---:|---|---|
| P5-C01 | The chosen Hénon form with `b = -1` is area-preserving, `det J = 1`. | Direct structural calculation | Accepted fact | Hard regression | Symbolic/numeric determinant test |
| P5-C02 | The 1D Logistic model is dissipative and is not used as the final unitary spectral host. | Structural argument | Project prior | Justifies lift | Keep in architecture |
| P5-C03 | The Hénon map is a 2D conservative candidate. | `MODELING_CHOICE` | `MODELING_CHOICE` | Track A baseline | Extend with twists |
| P5-C04 | First homoclinic tangency occurs near `a_c ≈ 1.00561`. | `NUMERICAL_OBSERVATION` | `NUMERICAL_OBSERVATION` | Regression target | Recompute with interval tools |
| P5-C05 | The transition near `a ≈ 1.02` is heuristically connected to finite resolution. | `HEURISTIC` | `HEURISTIC` | Candidate hint | Do not call derivation |
| P5-C06 | The cubic continuum potential needs confinement for a discrete numerical spectrum. | Structural/modeling observation | Accepted modeling need | Quantization baseline | Test alternatives |
| P5-C07 | Quartic coefficient `0.05` is first-principles. | Explicitly denied | Refuted interpretation | None | Label as regularizer |
| P5-C08 | Static/log schedules and constants are modeling choices or fitted quantities. | Explicit statement | `MODELING_CHOICE` / `FITTED_PARAMETER` | Search ansatz | Freeze before validation |
| P5-C09 | Two independent solvers show comparable low-order agreement. | `NUMERICAL_OBSERVATION` | `NUMERICAL_OBSERVATION` | Cross-solver regression | Reproduce independently |
| P5-C10 | Best 100-level quantum error is about `2.3%`. | Sharp optimized numerical result | `NUMERICAL_OBSERVATION` | Best-case baseline | Report sensitivity |
| P5-C11 | Robust error across grids/regularizers is closer to `10–20%`. | `NUMERICAL_OBSERVATION` | `NUMERICAL_OBSERVATION` | Honest baseline | Use in comparisons |
| P5-C12 | Markovian solver obtains a larger independent 100-level error. | `NUMERICAL_OBSERVATION` | `NUMERICAL_OBSERVATION` | Cross-method baseline | Reproduce |
| P5-C13 | Floquet eigenphases show GUE-like local statistics. | `NUMERICAL_OBSERVATION` | `NUMERICAL_OBSERVATION` | Consistency check | Audit unfolding |
| P5-C14 | GUE-like statistics uniquely identify a Riemann system. | Explicitly qualified/denied | Refuted interpretation | None | Add chaotic controls |
| P5-C15 | Reconstructed energies and Floquet phases have identical local statistics. | Not observed | Refuted interpretation | Pipeline warning | Keep objects separate |
| P5-C16 | Similarity to hardware error profiles proves a common mechanism. | Explicitly not established | Unsupported | None | Qualitative only |
| P5-C17 | The paper identifies the Hilbert–Pólya operator. | Explicitly denied | Refuted interpretation | None | Route B remains open |
| P5-C18 | Hénon is a useful mother template for twisted symplectic search. | New-project inference | `PROJECT_DECISION` | Track A | Implement DSL variants |

---

# 8. Cross-paper reconciliation

| Topic | Earlier position | Later refinement | Current project position |
|---|---|---|---|
| Finite-stage admissibility | Paper 1 assumes it | Paper 2 gives `Q3`, `Q5` counterexamples | Universal claim is refuted |
| 1D completeness | Paper 1 uses strong isomorphism language | Paper 2 finds mod-2 expressive ceiling | Logistic is a projection/prior, not final host |
| Aging and density | Paper 1 uses logarithmic aging | Paper 3 proves conditional stationary-average convergence and denies that this alone creates the envelope | Separate ergodic theorem from density mechanism |
| Logistic spectral matching | Paper 4 reports finite-matrix alignment | Paper 5 adopts more cautious claim separation and conservative lifting | Numerical baseline only |
| Conservative dynamics | Implicit earlier | Paper 5 makes area preservation explicit | Search symplectic/contact/quantizable systems |
| GUE evidence | Used as spectral diagnostic | Paper 5 states it is generic and requires unfolding | Secondary consistency metric |
| Hilbert–Pólya realization | Motivational | Paper 5 explicitly denies having identified it | Route B remains open |

---

# 9. HP-Dynamics project decisions

These are not theorems of the five papers.

| ID | Decision | Status | Reason |
|---|---|---|---|
| D-C01 | Route A searches a weighted dynamical Zeta/Fredholm determinant before a self-adjoint operator. | `PROJECT_DECISION` | Separates discovery from proof |
| D-C02 | Primary analytic target is completed `xi(s)` up to a zero-free entire factor. | `PROJECT_DECISION` | Includes Gamma/trivial factors and functional equation |
| D-C03 | Periods alone are insufficient; weights, repetitions, multiplicities, and phases are mandatory. | `PROJECT_DECISION` | Required by trace-formula structure |
| D-C04 | Train, validation, test, and sealed high-zero windows are separated. | `PROJECT_DECISION` | Prevents overfitting |
| D-C05 | Candidate definitions may not query prime or zero tables. | `PROJECT_DECISION` | Prevents direct encoding |
| D-C06 | GUE metrics receive lower weight than orbit, determinant, zero, and counting metrics. | `PROJECT_DECISION` | GUE is not unique |
| D-C07 | Main tracks are twisted symplectic maps, higher-memory symbolic suspensions, and low-complexity magnetic quantum graphs. | `PROJECT_DECISION` | Combines Papers 2, 3, 5 |
| D-C08 | Route B starts only after a natural Hilbert space, domain, quantization, and self-adjointness path exist. | `PROJECT_DECISION` | Prevents premature claims |

---

# 10. Mandatory regression tests

## Symbolic and arithmetic

```text
test_sieve_operator_definition
test_q3_mss_defect
test_q5_mss_defect
test_parity_gap_examples
test_defect_scan_small_k
test_even_gap_rigidity
test_mod3_resonance_absence_in_1d_model
```

## Non-autonomous

```text
test_one_sided_schedule
test_density_stability_reproduction
test_sequential_mean_convergence
test_sequential_l2_convergence
test_beta_greater_than_one_ae_scope
test_density_envelope_not_implied_by_birkhoff
```

## Spectral baseline

```text
test_gaussian_smoothing_sensitivity
test_anchor_dependence
test_shuffled_period_control
test_random_weight_control
test_conjugate_spectrum_ablation
```

## Hénon

```text
test_henon_area_preservation
test_henon_fixed_points
test_henon_short_period_orbits
test_homoclinic_tangency_baseline
test_quartic_regularization_label
test_schedule_parameters_are_fitted
test_quantum_solver_baseline
test_markov_solver_baseline
test_gue_unfolding_pipeline
test_reconstructed_energy_not_equal_to_floquet_phase_statistics
```

---

# 11. Claim update template

```markdown
## Claim update: <CLAIM_ID>

- Date:
- Commit:
- Previous status:
- New status:
- Trigger:
- Evidence:
- Reproduction command:
- Artifact paths:
- Reviewer:
- Consequences for current search:
```

Never change a major status without a change record.

---

# 12. Immediate open questions

| ID | Question | Origin | Priority |
|---|---|---|---:|
| OQ-01 | Can the mod-2 Logistic skeleton be lifted to a system carrying mod-3 and higher residue memory without directly encoding primes? | Paper 2 | Highest |
| OQ-02 | Can the lift remain symplectic or admit a natural suspension/contact flow? | Papers 2, 5 | Highest |
| OQ-03 | Can primitive orbit lengths emerge as `log p` from a low-complexity rule? | Route A | Highest |
| OQ-04 | Can orbit stability weights generate `p^(-r/2)` naturally? | Route A | Highest |
| OQ-05 | Which candidates admit nuclear/trace-class transfer operators and controlled Fredholm determinants? | Papers 3, 5 | High |
| OQ-06 | Can a non-autonomous schedule be replaced by an autonomous higher-dimensional extension? | Papers 1, 3, 5 | High |
| OQ-07 | Which twist breaks antiunitary time reversal while preserving natural quantization? | Paper 5 | High |
| OQ-08 | Are Paper 4's low-order matches robust under blind tests and null controls? | Paper 4 | High |
| OQ-09 | Can a strong Route-A determinant be linked to a self-adjoint operator by an exact trace formula? | Route B | Long-term |
| OQ-10 | Can the final spectral determinant be proved equal to `exp(q(E)) xi(1/2+iE)`? | Route B | Ultimate |

---

# 13. Summary for Codex

```text
Paper 1 gives the clue.
Paper 2 finds the one-dimensional obstruction.
Paper 3 supplies conditional drift theory.
Paper 4 supplies numerical experiments and warnings.
Paper 5 supplies the conservative mother template.

The new project must not merely improve the old fit.
It must search primitive orbits, construct a weighted determinant,
validate it blindly, and only then investigate quantization.
```
