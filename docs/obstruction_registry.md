# RH Obstruction Registry

## OBR-001 — Cross-determinant ledger gluing is invalid

Status:
PROVED_OBSTRUCTION

Source:
RH-341

Statement:
Coordinatewise maxima from the noisy modulus spectrum and graded
counterloop cannot be used as a legal determinant certificate.

Impact on HP-Dynamics:
Metrics from different determinant conventions may not be combined.

---

## OBR-002 — Wrong-clock comparison

Status:
PROVED_OBSTRUCTION

Source:
RH-337

Statement:
The RH-329 rational clock develops unbounded phase relative to the
physical algebraic clock.

Impact:
Every Route-A validation must use one frozen clock and normalization.

---

## OBR-003 — Separate absolute majorization fails

Status:
PROVED_OBSTRUCTION

Source:
RH-338–RH-340

Statement:
Separately taking absolute values of orbit, diffuse, and head terms
produces a divergent two-atom submajorant.

Impact:
The Zeta engine must retain signed/complex cancellation.

---

## OBR-004 — Abstract completion is not physical completion

Status:
INFORMATION_CLASS_UNDERDETERMINATION

Source:
RH-341

Impact:
Finite algebraic or matrix completions are not accepted as candidate
dynamical systems.

---

## OBR-005 — Constant-roof finite-state determinants have the wrong divisor growth

Status:
PROVED_OBSTRUCTION

Source:
CLUE-A1-002 / SS-0001 Route-A evaluation /
`formal/obstructions/finite_state_finite_roof_zero_count.md`

Statement:
For the mod-6 Cayley suspension SS-0001 with constant roof one,

\[
D(s)=\det(I-e^{-s}A)
     =(1-4e^{-2s})(1-e^{-2s})^2.
\]

Its zeros form finitely many vertical arithmetic progressions and therefore
have counting function \(N_D(T)=O(T)\). This cannot equal the completed-\(\xi\)
divisor, whose nontrivial-zero count is \(\Theta(T\log T)\), even after
multiplication by a zero-free entire factor.

Scope:
Every nonzero determinant `det(I-L_s)` where `L_s` is a finite matrix whose
entries are finite sums of fixed weights times `exp(-s*tau)` with positive
roof values. Finite-memory symbolic systems recoded as finite higher-block
graphs are included.

Invalid shortcut:
Adding finite residue memory or a finite graph quantization does not by itself
create a log-prime orbit clock or the required global zero density.

Reopening condition:
Use a structurally different object, such as a countable-state system,
unbounded/non-locally-constant roof, or infinite-dimensional nuclear transfer
operator, and prove that it escapes the finite-exponential-type count.

Artifacts:

- `evaluations/route_a/SS-0001/20260802T160435Z.yaml`
- `evaluations/route_a/SS-0001/20260802T163302Z.yaml`
- `artifacts/ss_0001/route_a_baseline.json`
- `tests/test_ss_0001_mod6_cayley.py`
- `formal/obstructions/finite_state_finite_roof_zero_count.md`
