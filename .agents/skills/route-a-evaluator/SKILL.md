---
name: route-a-evaluator
description: Evaluate whether a proposed classical dynamical system, transfer operator, symbolic suspension, quantum graph, or Fredholm-determinant construction is a credible Route-A candidate for a Riemann dynamical determinant. Use when assessing primitive-orbit structure, trace formulas, determinant matching, normalization, robustness, falsification tests, or Route-B readiness for a proposed Riemann-dynamics construction.
---

# Skill: Route A Evaluator

**Name:** `route-a-evaluator`  
**Version:** `0.1.0`  
**Purpose:** Evaluate whether a proposed classical dynamical system, transfer operator, symbolic suspension, quantum graph, or Fredholm-determinant construction is a credible Route-A candidate for a Riemann dynamical determinant.

---

## 1. Scope

Route A is a discovery and validation route. It does **not** prove the Riemann Hypothesis and does **not** establish a Hilbert–Pólya operator.

The target is a natural dynamical object whose weighted determinant satisfies, exactly or asymptotically,

\[
D_{\mathrm{dyn}}(s)\approx e^{g(s)}\xi(s),
\]

where \(e^{g(s)}\) introduces no extra zeros.

A successful Route A result may still be a major result even if Route B later fails.

---

## 2. Inputs

Required:

```yaml
candidate_id:
candidate_definition:
family:
phase_space:
dynamics:
parameters:
parameter_provenance:
clock:
normalization:
determinant_convention:
orbit_cutoff:
precision:
training_data:
forbidden_data:
code_commit:
artifact_paths:
```

Optional:

```yaml
symbolic_partition:
transfer_operator:
roof_function:
potential_function:
quantization_hint:
prior_work_links:
legacy_rh_links:
```

Reject the evaluation as `NOT_TESTABLE` if the mathematical object, clock, normalization, determinant convention, or data split is missing.

---

## 3. Evidence hierarchy

Use only these labels:

```text
PROVED
CONDITIONAL_THEOREM
NUMERICALLY_CERTIFIED
NUMERICAL_OBSERVATION
HEURISTIC
MODELING_CHOICE
FITTED_PARAMETER
OPEN
REFUTED
NOT_TESTABLE
STOP_SCOPED
```

Never promote a numerical observation to a theorem.

---

# 4. Route-A layers

## A1 — Primitive-orbit layer

### Question

Does the candidate possess a natural, reproducible primitive-periodic-orbit structure carrying prime-like information?

### Required checks

1. Primitive orbit definition is intrinsic to the dynamics.
2. Orbit enumeration is reproducible.
3. Repeated orbits are distinguished from primitive orbits.
4. Orbit orientation, phase and multiplicity are recorded.
5. Monodromy/stability multipliers are computed.
6. Completeness or missed-orbit risk is reported.
7. Candidate does not directly read a prime table or zero table.

### Target structure

At minimum, seek a non-accidental correspondence

\[
p\longleftrightarrow \gamma_p,
\qquad
T_{\gamma_p}\approx \log p.
\]

The stronger target is

\[
A_{\gamma_p,r}
\approx
\frac{\log p}{p^{r/2}}
\]

with correct repetition, multiplicity and phase structure.

### Mandatory controls

- shuffled periods;
- random weights;
- random phases;
- same-density random lengths;
- neighboring candidate parameters;
- simpler parent candidate.

### A1 verdicts

```text
A1_FAIL
A1_WEAK
A1_PASS_NUMERICAL
A1_PASS_CERTIFIED
A1_PASS_ANALYTIC
```

### A1 fail conditions

- direct prime lookup;
- period matching only after high-dimensional fitting;
- UPO enumeration incomplete without an uncertainty report;
- primitive and repeated cycles mixed;
- signed/complex weights replaced by absolute values;
- result disappears under small parameter or cutoff changes.

---

## A2 — Dynamical-Zeta layer

### Question

Do the primitive orbits define a stable weighted dynamical Zeta function or Fredholm determinant whose zeros/divisor structure matches the target beyond the fitted region?

### Required object

One explicit convention, for example

\[
Z_{\mathrm{dyn}}(s)
=
\prod_{\gamma}
\left(1-w_\gamma e^{-sT_\gamma}\right)^{-1},
\]

or

\[
D_{\mathrm{dyn}}(s)=\det(I-\mathcal L_s).
\]

The report must state whether the target concerns:

```text
Z
1/Z
Z'/Z
det(I-L_s)
another explicitly defined determinant
```

### Required checks

1. Training, validation and sealed test regions are separated.
2. Parameters are frozen before validation.
3. Root count is checked with the argument principle or an equivalent method.
4. Missing and extra zeros are reported.
5. Results are compared across orbit cutoffs.
6. Precision dependence is reported.
7. Two independent implementations are preferred.
8. Signed/complex cancellations are preserved.

### Mandatory outputs

```yaml
zero_error_train:
zero_error_validation:
zero_error_test:
extra_zero_count:
missing_zero_count:
root_count_discrepancy:
cutoff_drift:
precision_drift:
control_margin:
```

### A2 verdicts

```text
A2_FAIL
A2_TRAIN_ONLY
A2_FROZEN_VALIDATION_PASS
A2_ADVERSARIAL_PASS
A2_CERTIFIED_PREFIX
A2_ANALYTIC_DETERMINANT
```

### A2 fail conditions

- test-set refitting;
- changing scale, offset or unfolding after validation;
- reporting only the best seed;
- ignoring extra zeros;
- combining incompatible determinant decompositions;
- using different clocks or normalizations for head, orbit and tail pieces.

---

## A3 — Analytic-structure layer

### Question

Does the candidate reproduce the global analytic structure, not merely a finite list of zeros?

### Required checks

1. Conjugation symmetry:
   \[
   D(\bar s)=\overline{D(s)}.
   \]
2. Functional-equation behavior:
   \[
   D(s)\sim D(1-s)
   \]
   with all normalization factors stated.
3. Correct treatment of:
   - Gamma factor;
   - trivial zeros;
   - pole removal;
   - entire prefactors.
4. Riemann–von Mangoldt counting law.
5. Analytic continuation or a controlled annular/domain theorem.
6. Truncation error or moving-order control.
7. No zero-producing hidden prefactor.

### Strong optional evidence

- nuclear or trace-class transfer operator;
- Fredholm determinant theorem;
- certified annular \(H^\infty\) or \(H^2\) control;
- exact trace identity;
- all-order coefficient theorem.

### A3 verdicts

```text
A3_FAIL
A3_NUMERICAL_GLOBAL_MATCH
A3_PARTIAL_ANALYTIC_STRUCTURE
A3_CONTROLLED_CONTINUATION
A3_EXACT_DIVISOR_CANDIDATE
```

### A3 fail conditions

- finite zero fit presented as analytic continuation;
- separate absolute majorants destroy required cancellation;
- fixed-order data promoted to moving-order asymptotics;
- an abstract algebraic completion presented as a physical dynamical determinant.

---

## A4 — Natural-liftability layer

### Question

Is there a natural, non-post-hoc path from the classical candidate to a unitary, scattering, or Hamiltonian object?

### Required checks

1. Quantization is defined from the candidate, not invented after zero fitting.
2. Candidate has a coherent phase space and symplectic/contact/scattering structure, where applicable.
3. Time-reversal or antiunitary symmetry is explicitly tested.
4. The proposed quantum object preserves the same clock and normalization.
5. The proposed lift retains the relevant orbit phases and weights.
6. A plausible Hilbert space and operator domain can be named.

### A4 verdicts

```text
A4_FAIL
A4_FORMAL_HINT
A4_NATURAL_QUANTIZATION
A4_UNITARY_OR_SCATTERING_CANDIDATE
A4_ROUTE_B_READY
```

A candidate may be a strong Route-A success even if A4 fails.

---

# 5. Overall Route-A decision

Use the tuple

```text
(A1, A2, A3, A4)
```

and one overall status:

```text
ROUTE_A_REJECTED
ROUTE_A_EXPLORATORY
ROUTE_A_NUMERICAL_CANDIDATE
ROUTE_A_STRONG_CANDIDATE
ROUTE_A_ANALYTIC_CANDIDATE
ROUTE_A_SUCCESS_ROUTE_B_NOT_READY
ROUTE_A_SUCCESS_ROUTE_B_READY
```

Recommended interpretation:

```text
A1 + A2 only:
interesting numerical orbit model

A1 + A2 + partial A3:
strong Route-A candidate

A1 + A2 + strong A3:
Route-A success

A1 + A2 + strong A3 + A4:
send to Route-B Evaluator
```

---

# 6. Knowledge sources

Read in this order:

```text
docs/prior_work/README.md
docs/prior_work/claims_matrix.md
docs/prior_work/papers/
docs/related_programs/legacy_rh_program/RH_HANDOFF.md
docs/obstruction_registry.md
docs/candidate_registry.md
```

Interpretation inherited from prior work:

```text
Paper 1: arithmetic-symbolic clue
Paper 2: one-dimensional obstruction and mod-2 ceiling
Paper 3: conditional slow-drift theory
Paper 4: numerical baseline and overfitting warnings
Paper 5: conservative mother template
Legacy RH program: signed-completion and determinant-gluing obstructions
```

---

# 7. Output schema

```yaml
skill: route-a-evaluator
skill_version: 0.1.0
candidate_id:
source_commit:
evaluation_date:

source_lock:
  object:
  clock:
  normalization:
  determinant_convention:
  cutoff:
  precision:
  allowed_data:
  forbidden_data:

a1:
  verdict:
  evidence_status:
  strongest_evidence:
  strongest_failure:
  metrics:
  artifacts:

a2:
  verdict:
  evidence_status:
  strongest_evidence:
  strongest_failure:
  metrics:
  artifacts:

a3:
  verdict:
  evidence_status:
  strongest_evidence:
  strongest_failure:
  metrics:
  artifacts:

a4:
  verdict:
  evidence_status:
  strongest_evidence:
  strongest_failure:
  metrics:
  artifacts:

overall_verdict:
claim_boundary:
blocking_conditions:
next_smallest_test:
route_b_invocation_allowed: false
```

Set `route_b_invocation_allowed: true` only after A4 reaches `A4_ROUTE_B_READY` or the project lead explicitly authorizes a limited Route-B audit.

---

# 8. Accumulation protocol

Every evaluation must be saved under:

```text
evaluations/route_a/<candidate_id>/<timestamp>.yaml
```

Update:

```text
docs/candidate_registry.md
docs/obstruction_registry.md
```

Do not overwrite prior evaluations. New evidence creates a new version.

Reusable knowledge should be extracted as one of:

```text
positive structural prior
negative structural prior
numerical benchmark
proved obstruction
open theorem obligation
reusable implementation pattern
```

---

# 9. Invocation prompt

```text
Apply the Route-A Evaluator skill to candidate <candidate_id>.

Use the repository as the sole source of truth.
Freeze the object, clock, normalization, determinant convention, cutoff,
precision and data split before evaluation.

Evaluate A1 primitive-orbit structure, A2 dynamical Zeta/Fredholm determinant,
A3 global analytic structure and A4 natural liftability.

Preserve signed and complex cancellations.
Do not use test zeros for fitting.
Do not combine incompatible determinant decompositions.
Return the exact YAML output schema and recommend only the next smallest
verifiable step.
```
