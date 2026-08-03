# Legacy non-autonomous Logistic pre-candidate audit

Date: 2026-08-03

Audit IDs: `P4-LOGISTIC-LEGACY-AUDIT`, `P4-LOGISTIC-DETERMINISTIC-SMOKE`

Formal candidate created: no

## Scope

This audit covers the two legacy entry notebooks proposed for reopening the
Logistic direction:

- `docs/prior_work/legacy/4-riemann_logistic/ablation_test.ipynb`
- `docs/prior_work/legacy/4-riemann_logistic/micro_ustc_data_match.ipynb`

The legacy directory is a separate, dirty Git repository and was treated as
read-only. The audit extracted notebook source and saved textual outputs; it did
not rerun the (10^6)- to (10^{10})-step jobs.

## Object actually computed by the micro notebook

The time-dependent quadratic map is

\[
x_{n+1}=1-\mu_nx_n^2,
\qquad
\mu_n=u_c+\frac{k}{\log^2(n+10)},
\]

with endpoint anchoring from (1.5637) to (1.5437), (10^6) steps,
6000 bins and fitted Gaussian width

\[
\epsilon=0.001916.
\]

If (K_n(i,j)) is the discretized Gaussian transition kernel and (V_n) is
the evolving density, the accumulated matrix is

\[
T_{ij}=\sum_n V_n(i)K_n(i,j).
\]

Thus the numerical object is an occupation-conditioned empirical transition
matrix. It is not the chronological non-autonomous cocycle

\[
K_1K_2\cdots K_N,
\]

not a simple average of the (K_n), and not the Perron--Frobenius operator of
one autonomous Logistic map. Aggregation erases time order and can create graph
cycles that do not correspond to chronological periodic trajectories.

The reported observable is obtained by retaining upper-half-plane matrix
eigenvalues, discarding their moduli, sorting their principal phases, and using

\[
\widehat\gamma_j
=\frac{\gamma_1}{\theta_1}\theta_j.
\]

No (s)-plane dynamical Zeta or Fredholm determinant is defined.

## Normalization audit

Let

\[
D=\operatorname{diag}(T\mathbf1).
\]

Correct row normalization gives

\[
Q=D^{-1}T.
\]

The CSR code instead uses destination indices and therefore computes

\[
B=TD^{-1}.
\]

This is a Markov-normalization error, but it has a crucial exact qualification:

\[
B=DQD^{-1}.
\]

Consequently (B) and (Q) have the same exact eigenvalue multiset. The bug
does not by itself manufacture the eigenphases. It does invalidate the Markov
and eigenvector interpretation, and a badly conditioned occupation diagonal
(D) can worsen nonnormal finite-precision eigensolver behavior.

The target-free deterministic smoke profile found occupation condition number
approximately

\[
1.13\times10^9
\]

for the unshifted reduced partition, while the similarity residual remained at
`2.22e-16`.

## Saved numerical evidence and data boundary

The fitted micro result has:

| Region | Status | MAE | Mean relative error |
|---|---|---:|---:|
| zero 1 | fixes scale | 0 | 0% |
| zeros 2--6 | fitted epsilon and selected trial | 0.3494 | 1.34% |
| zeros 7--20 | retrospective only | 7.4162 | 11.49% |
| zeros 21--85 | retrospective only | 61.7317 | 39.84% |

There is no honest validation or sealed test in the saved legacy result:

- zero 1 fixes the phase scale;
- zeros 2--6 select `epsilon=0.001916` and the displayed eigensolver run;
- zero 20 enters the selection score through a reward for a large error;
- the macro schedule family was optimized against the first 100 zeros.

The same fixed sparse matrix is passed to `eigs` 20 times with no fixed `v0`.
The saved error sum over zeros 2--6 ranges from `1.7470` to `5.3630`. These are
randomized solver starts and Ritz-subspace choices, not repeated physical
measurements.

The N=20 USTC overlay is not independent validation. The selected model error
is `+16.485`, whereas the three plotted embedded experimental deviations are
approximately `+0.265`, `-0.345`, and `-0.325`, with N=20 error bars no larger
than `0.83`. The notebook also rewards a large N=20 model error before making
the overlay.

## Ablation interpretation

The saved ablation reports:

| Model | MSE | Mean relative error |
|---|---:|---:|
| all-100-point linear fit | 28.67 | 6.68% |
| dense random row-stochastic matrix | 655375.10 | 459.84% |
| static Logistic | 305.10 | 7.92% |
| asymptotic non-autonomous schedule | 3818.01 | 32.90% |
| anchored non-autonomous schedule | 78.08 | 5.66% |

The random control is not GUE. Static and dynamic models do not use the same
estimator or bin-index convention. The so-called method-5 “2D” model still has
one state variable; “2D” refers only to two schedule coefficients, and its
scoring lines are commented out.

The anchored schedule parameter belongs to an optimization family using the
same first 100 zeros. A related optimizer saved (k=6.76123) with MSE `21.8491`,
whereas the ablation uses (k=6.764850551\ldots) and reports MSE `78.08`. This
is direct evidence of parameter sensitivity or code/output version drift.

## Target-free deterministic smoke result

A reduced `128 bins x 1000 steps` profile preserved the legacy smoothing width
in bin units, (epsilon/dx=5.748), and used no prime, zero or USTC data.

Positive result:

- fixed ARPACK starts and tolerance `1e-10` reproduced the dense top-40
  eigenvalue set with worst matching distance below `3.7e-10`;
- relative eigen-residuals were below `3.8e-15`.

Failure of the present level rule:

- among the first six phase-ranked upper-half modes, five had
  (|\lambda|<10^{-3});
- only four of the fourteen selected upper-half top-40 modes exceeded that
  modulus threshold;
- after a half-bin partition shift, the 13 residual-resolved dense modes had
  median complex-plane drift `0.00943`, 90th-percentile drift `0.0883`, and
  maximum drift `0.15275`.

This reduced profile is a numerical-mechanics test, not a physical-epsilon or
full-cutoff reproduction. It shows that deterministic eigensolving can work,
while the legacy “lowest phase equals lowest energy” rule is not yet a stable
observable.

## Route-A preassessment

```text
formal candidate: none
status: NOT_TESTABLE
diagnostic tuple: (A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)
Route B: not authorized
```

Strongest evidence: the target-fitted prefix is a genuine stored numerical
observation and can serve as a regression benchmark.

Strongest failure: there is no primitive-orbit ledger, intrinsic prime-like
clock, explicit dynamical determinant, blind validation, global divisor law,
or natural lift. A fixed finite matrix determinant would also remain inside
`OBR-005`; a moving-cutoff infinite-operator limit would need a separate
definition and theorem.

## Next smallest task

Run a medium-fidelity, target-free branch audit with physical epsilon fixed:

1. save and hash the raw (T) matrix;
2. construct both (Q=D^{-1}T) and (B=TD^{-1});
3. fix `v0`, `k`, `ncv`, tolerance and maximum iterations;
4. report every eigenvalue modulus and residual;
5. track residual-certified branches by complex-plane matching across bins,
   steps and a half-bin partition shift;
6. do not inspect Riemann-zero agreement until the branch identities are
   frozen.

Only if stable branches survive should the project define either an autonomous
slow-variable lift or a genuine transfer-cocycle/Fredholm determinant.

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
