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

---

## OBR-006 — Finite-area modular Selberg determinants have the wrong divisor growth

Status:
PROVED_OBSTRUCTION

Source:
CLUE-A1-002 / SS-0002 Route-A evaluation /
`formal/obstructions/finite_area_selberg_weyl_mismatch.md`

Statement:
Let \(\Gamma\) be a finite-index subgroup of
\(\operatorname{PSL}_2(\mathbb Z)\). If one frozen dynamical Fredholm
determinant has the Selberg-zeta divisor \(Z_\Gamma(s)\), then it contains at
least the modular cuspidal spectrum lifted to the cover. Hence its
positive-height zero count is

\[
N_{Z_\Gamma}^{+}(T)
\geq \frac{T^2}{12}+o(T^2)
=\Omega(T^2).
\]

This cannot equal the completed-\(\xi\) divisor, whose count is
\(\Theta(T\log T)\), even after multiplication by a zero-free entire factor
or a fixed nondegenerate affine spectral change.

SS-0002 corollary:
The regular-`C6` paired-Gauss operator for the index-six commutator cover is
nuclear and genuinely escapes `OBR-005`, but

\[
\det_{\rm Fr}(I-\mathcal M_s)
=Z_{[\Gamma,\Gamma]}(s)
\]

puts the same determinant inside this obstruction. Its area is \(2\pi\), and
the full two-sided finite-area resonance Weyl main term is \(T^2\).

Invalid shortcut:
The modular scattering determinant, which contains a convention-dependent
ratio related to \(\Lambda(2s-1)/\Lambda(2s)\), is a different data type. It
cannot be multiplied into or used to cancel the Mayer/Selberg determinant
without a single proved same-object identity.

Scope:
Direct Selberg-zeta/Fredholm determinants for finite-index modular covers and
any same determinant divisor containing the inherited modular cuspidal
spectrum.

Reopening condition:
Give one explicit non-Selberg determinant whose intrinsic, same-ledger divisor
has a proved \(T\log T\) regime, with no prime/zero lookup and no borrowed
scattering quotient.

Artifacts:

- `configs/source_locks/SS-0002.yaml`
- `evaluations/route_a/SS-0002/20260803T012711Z.yaml`
- `artifacts/ss_0002/route_a_structural_audit.json`
- `docs/literature/ss_0002_gauss_mayer_sources.md`
- `formal/obstructions/finite_area_selberg_weyl_mismatch.md`
- `tests/test_ss_0002_commutator_mayer.py`
