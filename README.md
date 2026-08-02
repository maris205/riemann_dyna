# HP-Dynamics

**Theory-Guided AI Search for a Riemann Dynamical Determinant**

HP-Dynamics is a research project for exploring possible dynamical-system routes toward the Hilbert–Pólya program.

The project does **not** assume that a numerical spectral match proves the Riemann Hypothesis. Instead, it separates the research into two explicit routes:

```text
Route A — discover and validate a dynamical determinant
Route B — promote a strong Route-A candidate to a rigorous operator realization
```

The repository is designed for long-running AI-assisted research, reproducible numerical experiments, theorem-oriented auditing, and cumulative knowledge reuse.

---

## 1. Project objective

### Route A

Search for a natural classical dynamical system, symbolic system, transfer operator, quantum graph, or Fredholm determinant satisfying

\[
D_{\mathrm{dyn}}(s)
\approx
e^{g(s)}\xi(s),
\]

where \(e^{g(s)}\) introduces no extra zeros.

Route A is evaluated at four levels:

```text
A1 — primitive orbit structure
A2 — dynamical Zeta / Fredholm determinant
A3 — global analytic structure
A4 — natural quantization and liftability
```

A successful Route A result may already be a major result even if Route B fails.

### Route B

For the strongest Route-A candidates, construct a rigorous operator

\[
H:\mathcal D(H)\subset\mathcal H\to\mathcal H
\]

and investigate:

```text
B1 — complete operator definition
B2 — self-adjointness
B3 — target spectral type
B4 — exact prime-power trace formula
B5 — completed-xi determinant or divisor equality
```

The ultimate target is

\[
\det_{\zeta}(E-H)
=
e^{q(E)}
\xi\!\left(\frac12+iE\right).
\]

Only a construction that closes B1–B5 in one compatible framework may be called a complete Hilbert–Pólya realization.

---

## 2. Core workflow

The project is intentionally simple:

```text
research clue or candidate
        ↓
Route-A Evaluator
        ↓
reject / refine / freeze / validate
        ↓
Route-B Evaluator, only when authorized
        ↓
knowledge accumulation
```

The main Agent performs only four tasks:

```text
1. Read and classify new clues or candidates
2. Invoke the Route-A Evaluator
3. Invoke the Route-B Evaluator only after Route A authorizes it
4. Update the shared knowledge base and choose the next smallest verifiable task
```

The repository, not chat memory, is the source of truth.

---

## 3. Start here

Read these files in order:

```text
1. docs/HP_Dynamics_Project_Entry.md
2. docs/main_agent_rules.md
3. skills/route-a-evaluator/SKILL.md
4. skills/route-b-evaluator/SKILL.md
5. docs/research_clues.md
6. docs/prior_work/README.md
7. docs/prior_work/claims_matrix.md
8. HP_HANDOFF.md
```

The full historical research plan is archived for reference:

```text
docs/archive/HP_Dynamics_Research_Plan_v0.1_full.md
```

Daily operation should use the shorter entry document and the two Skills.

---

## 4. Repository structure

Recommended layout:

```text
HP-Dynamics/
├── README.md
├── HP_HANDOFF.md
├── AGENTS.md
├── CHANGELOG.md
│
├── skills/
│   ├── route-a-evaluator/
│   │   └── SKILL.md
│   └── route-b-evaluator/
│       └── SKILL.md
│
├── docs/
│   ├── HP_Dynamics_Project_Entry.md
│   ├── main_agent_rules.md
│   ├── research_clues.md
│   ├── candidate_registry.md
│   ├── obstruction_registry.md
│   ├── operator_obligations.md
│   ├── research_log.md
│   │
│   ├── prior_work/
│   │   ├── README.md
│   │   ├── claims_matrix.md
│   │   ├── papers/
│   │   └── summaries/
│   │
│   ├── related_programs/
│   │   └── legacy_rh_program/
│   │
│   └── archive/
│       └── HP_Dynamics_Research_Plan_v0.1_full.md
│
├── evaluations/
│   ├── route_a/
│   └── route_b/
│
├── configs/
├── src/
├── tests/
├── experiments/
├── artifacts/
├── reports/
├── formal/
└── legacy/
```

---

## 5. Core Skills

### Route-A Evaluator

Location:

```text
skills/route-a-evaluator/SKILL.md
```

It evaluates:

```text
A1 — primitive periods, repetitions, weights, phases and orbit completeness
A2 — dynamical Zeta or Fredholm determinant and blind spectral validation
A3 — functional equation, counting law, analytic continuation and moving-order control
A4 — natural unitary, scattering or Hamiltonian lift
```

Typical outputs:

```text
ROUTE_A_REJECTED
ROUTE_A_EXPLORATORY
ROUTE_A_NUMERICAL_CANDIDATE
ROUTE_A_STRONG_CANDIDATE
ROUTE_A_ANALYTIC_CANDIDATE
ROUTE_A_SUCCESS_ROUTE_B_NOT_READY
ROUTE_A_SUCCESS_ROUTE_B_READY
```

### Route-B Evaluator

Location:

```text
skills/route-b-evaluator/SKILL.md
```

It evaluates:

```text
B1 — Hilbert space, domain, boundary conditions and operator action
B2 — self-adjointness
B3 — discrete or otherwise correct target spectral type
B4 — rigorous von Mangoldt-weighted prime-power trace formula
B5 — global completed-xi spectral determinant equality
```

Typical outputs:

```text
ROUTE_B_REJECTED
ROUTE_B_NOT_TESTABLE
ROUTE_B_FORMAL_ONLY
ROUTE_B_OPERATOR_CANDIDATE
ROUTE_B_SELF_ADJOINT_CANDIDATE
ROUTE_B_TRACE_FORMULA_CANDIDATE
ROUTE_B_PARTIAL_REALIZATION
HILBERT_POLYA_REALIZATION
```

---

## 6. Shared knowledge base

The project accumulates knowledge in four forms.

### Candidate registry

```text
docs/candidate_registry.md
```

Tracks:

- candidate family;
- current status;
- latest Route-A tuple;
- latest Route-B tuple;
- positive evidence;
- failed controls;
- open obligations;
- next test.

### Obstruction registry

```text
docs/obstruction_registry.md
```

Stores reusable negative results such as:

- incompatible determinant decompositions cannot be glued;
- different clocks or normalizations cannot be mixed;
- signed cancellation cannot be replaced by separate absolute-value estimates;
- fixed-order fits do not imply moving-order theorems;
- abstract completions are not physical operators;
- GUE statistics are not a unique Riemann fingerprint.

### Operator obligations

```text
docs/operator_obligations.md
```

Tracks unresolved B1–B5 requirements for each candidate.

### Research clues

```text
docs/research_clues.md
```

Stores only:

- reusable structural priors;
- proved constraints;
- testable conjectures;
- exact reopening conditions;
- smallest next tests.

---

## 7. Prior work

The project begins from five foundational papers.

Their correct interpretation is:

```text
Paper 1 — arithmetic-symbolic clue
Paper 2 — one-dimensional obstruction and mod-2 ceiling
Paper 3 — conditional slow-drift theory
Paper 4 — numerical baseline and overfitting warnings
Paper 5 — conservative Hénon mother template
```

Read:

```text
docs/prior_work/README.md
docs/prior_work/claims_matrix.md
```

Later corrections override earlier incompatible claims.

The older RH research program is kept as a separate vertical branch:

```text
docs/related_programs/legacy_rh_program/
```

It contributes determinant-gluing obstructions, signed-completion lessons, wrong-clock exclusions, sideband analysis, and moving-order requirements.

---

## 8. Current priority directions

The main Route-A search directions are:

```text
1. Twisted Hénon and kicked symplectic maps
2. Higher-memory symbolic suspensions
3. Low-complexity magnetic quantum graphs
4. Legacy Hardy signed-completion and annular-norm route
```

The three central open questions are:

### OQ-1

Can a low-complexity dynamical rule naturally generate

\[
T_{\gamma_p}=\log p
\]

without directly encoding primes?

### OQ-2

Can the system naturally generate

\[
A_{\gamma_p,r}
\sim
\frac{\log p}{p^{r/2}}?
\]

### OQ-3

Can a strong Route-A determinant admit a natural self-adjoint lift?

---

## 9. Non-negotiable rules

No candidate may:

1. use validation or test zeros for optimization;
2. directly read prime or zero tables in its definition;
3. mix \(Z\), \(1/Z\), \(Z'/Z\), and \(\det(I-\mathcal L_s)\) without an explicit convention;
4. combine incompatible clocks or normalizations;
5. replace required signed or complex cancellation with separate absolute-value estimates;
6. treat an abstract algebraic completion as a physical dynamical system;
7. treat GUE statistics as a unique Riemann-spectrum signature;
8. infer self-adjointness from a finite real spectrum;
9. promote a fixed truncation to an all-order theorem;
10. hide extra zeros, failed seeds, precision drift, or numerical instability.

---

## 10. Evaluation storage

Every evaluation is versioned:

```text
evaluations/
├── route_a/<candidate_id>/<timestamp>.yaml
└── route_b/<candidate_id>/<timestamp>.yaml
```

Do not overwrite earlier evaluations.

Each evaluation must record:

```text
source commit
mathematical object
clock
normalization
determinant convention
cutoff
precision
allowed and forbidden data
metrics
strongest evidence
strongest failure
claim boundary
next smallest test
```

---

## 11. Project status levels

```text
S0 — reproducible infrastructure
S1 — frozen-parameter blind-validation success
S2 — strong Route-A candidate
S3 — partial Route-B realization
S4 — complete Hilbert–Pólya realization
```

The near-term objective is not to claim RH.

It is to:

```text
find a genuine strong Route-A path
or
prove a meaningful structural obstruction for a candidate family
```

---

## 12. First run

At project initialization:

```text
1. Create the repository structure
2. Add the two Skills
3. Add the entry and main-Agent rules
4. Add the prior-work documents
5. Create an initial HP_HANDOFF.md
6. Select one clue from research_clues.md
7. Freeze a source lock
8. Run the Route-A Evaluator
9. Save the evaluation
10. Update the registries
```

The initial `HP_HANDOFF.md` may state:

```text
Project initialized.
No candidate has yet passed Route A or Route B.
The next task is to select the first clue and create a source lock.
```

---

## 13. Claim boundary

This repository may contain:

- exploratory candidates;
- numerical evidence;
- certified numerical results;
- conditional theorems;
- local obstructions;
- operator programs.

None of these should be described as a proof of the Riemann Hypothesis unless one compatible construction rigorously closes Route A and B1–B5.

---

## 14. One-line summary

\[
\boxed{
\text{Clue}
\rightarrow
\text{Route A discovery and validation}
\rightarrow
\text{Route B operator proof}
\rightarrow
\text{shared knowledge}
}
\]

The goal is not to maximize paper count. The goal is to find and preserve a real path, however narrow, toward a dynamical Hilbert–Pólya realization.

注意，可以使用科研工具skills，如果外网访问有问题，可以用clash代理。已经开了。
