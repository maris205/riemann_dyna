# Prior Work Guide

This directory contains the five papers and corresponding legacy code that form the starting point of the **HP-Dynamics** project.

These materials are **not** a single final theory. They form a chronological research chain in which later papers refine, limit, or correct earlier claims. Codex and all human contributors must therefore read them in order and use `claims_matrix.md` as the authoritative interpretation layer.

---

## 1. Purpose

The prior work serves four roles:

1. **Search priors** — symbolic dynamics, the band-merging/Misiurewicz regime, slow logarithmic drift, conservative lifting, transfer operators, Floquet spectra, and candidate periodic-orbit structure.
2. **Negative constraints** — finite-stage MSS defects, the expressive ceiling of the one-dimensional unimodal projection, and the limits of finite-dimensional spectral fitting.
3. **Regression baselines** — the legacy experiments must be reproduced before the new UPO–Zeta stack is trusted.
4. **Claim provenance** — every reused statement must be labeled as a theorem, conditional theorem, numerical observation, heuristic, modeling choice, fitted result, correction, or open problem.

This directory must not be treated as unquestionable ground truth.

---

## 2. Recommended layout

```text
docs/prior_work/
├── README.md
├── claims_matrix.md
├── papers/
│   ├── 01_prime_chaos.pdf
│   ├── 02_transient_chaos_topological_bounds.pdf
│   ├── 03_sequential_birkhoff.pdf
│   ├── 04_non_autonomous_riemann_spectrum.pdf
│   └── 05_area_preserving_henon.pdf
└── summaries/
    ├── 01_prime_chaos.md
    ├── 02_transient_chaos.md
    ├── 03_sequential_birkhoff.md
    ├── 04_non_autonomous_riemann_spectrum.md
    └── 05_area_preserving_henon.md
```

Historical code should remain outside `docs/`:

```text
legacy/
├── paper1_prime_chaos/
├── paper2_transient_chaos/
├── paper3_sequential_birkhoff/
├── paper4_riemann_logistic/
└── paper5_henon/
```

New reusable code belongs under `src/hpdyn/`. Do not patch legacy scripts indefinitely: reproduce them, test them, then reimplement reusable pieces in the new package.

---

## 3. Required reading order

### Paper 1 — Prime–Chaos framework

**File:** `papers/01_prime_chaos.pdf`

**Role**

- Introduces the symbolic-sieve viewpoint.
- Proposes a correspondence between the Eratosthenes sieve and the Logistic map near the first band-merging point.
- Introduces parity rigidity, weak chaos, and non-autonomous aging.
- Reports numerical recovery of the twin-prime constant.

**Use as**

- arithmetic-symbolic search prior;
- band-merging/Misiurewicz baseline;
- source of candidate observables and regression tests;
- historical motivation.

**Do not assume**

- every finite sieve stage is an admissible unimodal itinerary;
- the one-dimensional Logistic map is the final Hilbert–Pólya host;
- numerical agreement proves spectral identity.

Paper 2 explicitly revises part of this framework.

---

### Paper 2 — Transient chaos and topological bounds

**File:** `papers/02_transient_chaos_topological_bounds.pdf`

**Role**

- Re-examines finite-stage MSS admissibility.
- Gives explicit defects at `Q3` and `Q5`.
- Proves the Parity-Gap Lemma.
- Separates microscopic topological failure from macroscopic statistical usefulness.
- Identifies a mod-2/abelian expressive ceiling of the one-dimensional model.

**Use as**

- the main negative-constraint document;
- the source of MSS regression tests;
- the argument for higher-dimensional or higher-rank lifting;
- a model for the workflow “computation finds the pivot, proof establishes the structure.”

**Precedence rule**

Where Paper 2 conflicts with Paper 1 on finite-stage admissibility, Paper 2 takes precedence.

**Later correction — 2026-08-04**

The parity conclusion is retained only after replacing the legacy Paper-2 MSS
argument by an exact band-swap proof on the physical core
(J=[1-U_c,1]). On that core the first-return support is exactly
(2\mathbb N), with one interval branch per even label. On ambient
`[-1,1]`, transient odd branches exist but have zero mass for every invariant
probability.

The Paper-2 claim that the unaccelerated first-return map is uniformly
expanding on its countable branches is false: the derivative infimum is zero
on every branch because the endpoints accumulate on critical preimages. Its
ordinary-`BV` spectral-gap proof remains refuted. The neighboring-mass-ratio
limit is now repaired independently by the direct physical-density theorem

\[
h(-\rho+t)
=\frac{h(0)}{\sqrt2U_c}t^{-1/2}+O(1),
\qquad h(0)>0,
\]

which gives

\[
\frac{\mu(C_{2n+2})}{\mu(C_{2n})}
\longrightarrow\frac1{2U_c(U_c-1)}.
\]

This does not restore the stronger Paper-2 formula or its ordinary-BV
spectral proof. A later target-free sharp polar-cone theorem gives the
validated interval $0.20655<h(0)<0.40008$ and tighter selected finite branch
masses. The subsequent cusp-adapted audit proves the adjacent-mass-ratio rate

\[
\left|
\frac{\mu(C_{2n+2})}{\mu(C_{2n})}-\frac{U_c^2}{4}
\right|
<
\frac{243}{625}\left(\frac35\right)^{n-6},
\qquad n\geq6.
\]

A closed form, a narrow high-accuracy value, and an exact finite-order weight
law remain open. See:

- `formal/results/exact_uc_first_return_support.md`;
- `formal/results/exact_uc_acip_endpoint_density.md`;
- `formal/results/exact_uc_acip_cone_enclosure.md`;
- `formal/results/exact_uc_acip_sharp_cone_enclosure.md`;
- `formal/results/exact_uc_branch_mass_rate.md`;
- `formal/obstructions/exact_uc_first_return_nonuniform_expansion.md`.

---

### Paper 3 — Sequential Birkhoff theorem

**File:** `papers/03_sequential_birkhoff.pdf`

**Role**

- Gives a conditional non-autonomous ergodic theorem for slowly drifting unimodal maps.
- Makes the required assumptions explicit: uniform inducing, expansion, distortion control, Young-tower tails, Lasota–Yorke bounds, spectral gap, Keller–Liverani stability, and raw-operator stability.
- Separates mean/`L2` convergence from almost-everywhere convergence.
- States that the theorem does **not** itself generate a non-stationary `1/log n` prime-density envelope.

**Use as**

An admissibility filter for non-autonomous candidates. A schedule such as

```math
u_n=u_c-c(\log n)^{-\beta}
```

must not be accepted only because it fits data. The surrounding operator family must support the stated assumptions or a justified replacement.

---

### Paper 4 — Non-autonomous Logistic spectral experiments

**File:** `papers/04_non_autonomous_riemann_spectrum.pdf`

**Role**

- Explores finite-dimensional transfer matrices, Gaussian smoothing, time averaging, eigenphase extraction, conjugate-spectrum completion, and low-order zero matching.
- Provides useful numerical experiments and failure modes.

**Use as**

- a reproducibility target;
- a numerical baseline;
- a source of ablation tests;
- a case study in finite-precision sensitivity and overfitting risk.

**Important limitation**

The strongest spectral and physical language must not be imported as established fact. Smoothing scales, mappings, schedules, and other quantities were optimized or selected; the reported spectral agreement is numerical.

Treat this paper as an **anti-overclaim benchmark**.

---

### Paper 5 — Area-preserving Hénon model

**File:** `papers/05_area_preserving_henon.pdf`

**Role**

- Lifts the search from a one-dimensional dissipative map to a two-dimensional area-preserving map.
- Introduces conservative dynamics, homoclinic structure, quartic confinement, unitary and Markovian solvers, and GUE diagnostics.
- Explicitly distinguishes structural facts, numerical observations, heuristic consistency checks, fitted parameters, and conjectural interpretation.

**Use as**

- the principal conservative-lifting baseline;
- the mother template for twisted Hénon and kicked symplectic candidates;
- a regression target for UPO and Floquet tooling;
- evidence that a sharp fitted optimum must be distinguished from robust performance.

**Do not assume**

- the current Hénon model is the Hilbert–Pólya operator;
- GUE-like statistics uniquely identify a Riemann system;
- `a ≈ 1.02`, the quartic coefficient, or the schedules are first-principles constants;
- the reported zero match is already a strict blind test.

---

## 4. Research-chain interpretation

```text
Paper 1
Prime sieve → symbolic chaos hypothesis
        │
        ▼
Paper 2
Finite-stage obstruction + mod-2 expressive ceiling
        │
        ▼
Paper 3
Conditional analytic control of slow non-autonomous drift
        │
        ▼
Paper 4
Finite-dimensional spectral experiments and sensitivity lessons
        │
        ▼
Paper 5
Conservative lifting and quantization-oriented numerical model
        │
        ▼
HP-Dynamics
UPO → weighted dynamical Zeta/Fredholm determinant → blind validation
        │
        ▼
Possible Hilbert–Pólya operator program
```

The new project therefore performs a **theory-guided inverse trace-formula search**, not a blind search over arbitrary dynamical systems.

---

## 5. Evidence and precedence rules

### Rule 1 — Later correction overrides earlier claim

Example:

```text
Paper 1: finite-stage topological admissibility is assumed.
Paper 2: explicit counterexamples occur at Q3 and Q5.
Project status: the universal finite-stage claim is refuted.
```

### Rule 2 — A theorem is only as strong as its assumptions

Do not summarize Paper 3 as “every logarithmically drifting Logistic map satisfies Birkhoff convergence.” Its result is conditional on a uniform inducing/spectral framework and has different conclusions for different values of `beta`.

### Rule 3 — Numerical matching is not operator identity

Finite matrix, eigenphase, zero-coordinate, or GUE agreement does not prove:

- self-adjointness;
- equality of spectral determinants;
- analytic continuation;
- uniqueness;
- the Riemann Hypothesis.

### Rule 4 — Modeling choices are not derived constants

Regularizers, schedules, fitted scales, anchors, and numerical cutoffs must be labeled as such.

### Rule 5 — GUE is a consistency check, not a unique fingerprint

The new project prioritizes:

1. primitive-orbit lengths;
2. orbit weights, repetitions, multiplicities, and phases;
3. determinant convergence;
4. blind zero locations;
5. global counting function and functional equation;
6. then local GUE statistics.

### Rule 6 — Legacy code is not proof

A successful script establishes only that a particular procedure produced a result under a particular configuration.

---

## 6. Claim-status vocabulary

| Label | Meaning |
|---|---|
| `ESTABLISHED_EXTERNAL` | Standard result proved in cited literature |
| `PROVED_IN_PAPER` | The paper presents a proof of the claim |
| `CONDITIONAL_THEOREM` | Proved subject to explicit assumptions/conjectures |
| `NUMERICALLY_CERTIFIED` | Rigorous numerical enclosure with controlled error |
| `NUMERICAL_OBSERVATION` | Finite reproducible computation without proof-level certification |
| `HEURISTIC` | Structural analogy or physical argument |
| `CONJECTURE` | Explicit unproved mathematical statement |
| `MODELING_CHOICE` | Chosen ansatz, schedule, regularizer, or boundary condition |
| `FITTED_PARAMETER` | Optimized against target data |
| `SUPERSEDED` | Replaced by a later, more precise formulation |
| `REFUTED` | Disproved by counterexample or contradiction |
| `PROJECT_DECISION` | Policy adopted by HP-Dynamics |
| `OPEN` | Important unresolved statement |

Do not create new labels without updating this table and `claims_matrix.md`.

---

## 7. Required Codex workflow

Before implementing new search code, Codex must:

1. Read this file.
2. Read all five papers in order.
3. Read `claims_matrix.md`.
4. Inspect corresponding legacy code.
5. Create or update:
   - `docs/prior_work/summaries/*.md`;
   - `docs/reproduction_plan.md`;
   - `docs/architecture.md`;
   - `docs/issues/`.
6. Reproduce the baseline claims marked as regression tests.
7. Record every mismatch between paper, legacy code, and new implementation.

Codex must not silently fix discrepancies. Use this template:

```text
Expected from paper:
Observed from legacy code:
Observed from new implementation:
Likely reason:
Status:
Next smallest test:
```

---

## 8. Mandatory reproduction targets

### Paper 1

- Logistic band-merging baseline;
- symbolic partition and parity statistics;
- twin-constant numerical experiment;
- aging-schedule behavior.

### Paper 2

- `Q3` and `Q5` MSS defects;
- Parity-Gap test cases;
- defect scan through a feasible range;
- even-gap rigidity;
- absence of internal mod-3 resonance in the 1D model.

### Paper 3

- density-stability experiment;
- sequential Birkhoff convergence;
- dependence on `beta`;
- one-sided schedule behavior.

### Paper 4

- smoothing-scale scan;
- low-order eigenphase matching;
- parameter sensitivity;
- conjugate-spectrum ablation;
- shuffled/random controls.

### Paper 5

- area preservation;
- short periodic orbits;
- phase portraits;
- homoclinic-tangency calculation;
- unitary and Markovian baselines;
- 100-level sensitivity;
- unfolded GUE diagnostics.

---

## 9. Project-level conclusions

These are **project decisions**, not theorems proved by the five papers.

1. The one-dimensional Logistic model is retained as a baseline and symbolic prior, not the default final Hilbert–Pólya host.
2. Principal candidate families include twisted Hénon/kicked symplectic maps, higher-memory symbolic suspensions, and low-complexity magnetic quantum graphs.
3. The primary target is the completed function `xi(s)`, not a finite fit to raw zeta zeros.
4. A strong Route-A candidate must pass orbit, weight, determinant, blind-zero, counting-function, functional-equation, robustness, leakage, and complexity checks.
5. Route B begins only after a natural quantization, Hilbert space, operator domain, and self-adjointness path are identified.

---

## 10. Maintenance

Update this directory whenever:

- a new paper version is added;
- a claim is corrected;
- a reproduction succeeds or fails;
- a theorem assumption changes;
- a legacy parameter is found to be fitted or hard-coded;
- a project decision changes the interpretation of prior work.

Any major claim-status change must also update:

```text
docs/prior_work/claims_matrix.md
docs/research_log.md
CHANGELOG.md
```
