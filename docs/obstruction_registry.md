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

---

## OBR-007 — Strict-monotone clock lifts collapse periodic orbits to the clock fixed set

Status:
PROVED_OBSTRUCTION

Source:
CLUE-A1-004 / P4-LOGISTIC-MONOTONE-CLOCK-LIFT /
`formal/obstructions/strict_monotone_clock_orbit_collapse.md`

Statement:
For a skew product

\[
F(y,b)=(f_b(y),g(b)),
\]

every full-space periodic point projects to a periodic point of the base:

\[
\operatorname{Fix}(F^m)
=
\bigcup_{b\in\operatorname{Fix}(g^m)}
\left\{
(y,b):
f_{g^{m-1}b}\circ\cdots\circ f_b(y)=y
\right\}.
\]

Hence an aperiodic base gives no periodic orbits, and a strict Lyapunov clock
confines every periodic orbit to its base fixed set.

Logistic corollary:
For the exact compact clock

\[
v_n=\frac1{\log(n+10)},
\qquad
G(v)=\frac1{\log(e^{1/v}+1)},
\qquad G(0)=0,
\]

the autonomous lift

\[
F(x,v)=\left(1-(u_c+kv^2)x^2,G(v)\right)
\]

reproduces the frozen legacy schedule, but

\[
\operatorname{Fix}(F^m)
=
\operatorname{Fix}(f_{u_c}^m)\times\{0\}
\]

for every \(m\geq1\). Thus no primitive orbit visits the aging interior, and
the reciprocal Artin--Mazur formal series is exactly that of the static limit
parent. Moreover \(G'(0)=1\), so every boundary orbit has a neutral clock
multiplier and the usual hyperbolic monodromy denominator is degenerate.

Invalid shortcuts:

- periodizing the clock changes the schedule after the chosen period;
- clamping at a finite cutoff creates a cutoff-dependent static parent;
- a projected fibre return is not a full-state periodic point;
- graph cycles of an occupation-aggregated matrix are not chronological UPOs;
- silently deleting the neutral multiplier changes the determinant ledger.

Scope:
Autonomous skew-product lifts with an aperiodic base, or with a strict
Lyapunov clock whose recurrence is confined to a fixed subset. The result does
not exclude autonomous lifts with an intrinsic nontrivial recurrent base.

Reopening condition:
Give a new recurrent base whose nontrivial periodic orbits leave the
static-limit slice while genuinely reproducing logarithmic aging, together
with a nondegenerate same-object determinant; or define a chronological
transfer-cocycle determinant with a frozen function space, horizon, clock,
normalization, repetition law, and trace theorem.

Artifacts:

- `configs/source_locks/P4-LOGISTIC-MONOTONE-CLOCK-LIFT.yaml`
- `evaluations/route_a/P4-LOGISTIC-MONOTONE-CLOCK-LIFT/20260804T025047Z.yaml`
- `artifacts/p4_logistic_monotone_clock_lift/structural_audit.json`
- `formal/obstructions/strict_monotone_clock_orbit_collapse.md`
- `tests/test_p4_logistic_monotone_clock_lift.py`

---

## OBR-008 — Unit-lattice clocks force a vertically periodic divisor

Status:
PROVED_OBSTRUCTION

Source:
CLUE-A1-004 / P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK /
`formal/obstructions/unit_lattice_clock_vertical_periodicity.md`

Statement:
Let $H$ be a nonzero single-valued meromorphic function on
$\mathbb C\setminus\{0\}$. Then

\[
D(s)=H(e^{-s})
\]

satisfies

\[
D(s+2\pi i)=D(s).
\]

For every bounded real interval $[a,b]$, the image of one vertical
fundamental rectangle is the compact annulus

\[
\{z:e^{-b}\leq|z|\leq e^{-a}\}\subset\mathbb C^\ast.
\]

Meromorphicity gives only finitely many zeros and poles in that annulus, so
periodicity implies $O(T)$ divisor count in
$a\leq\Re s\leq b$, $0<\Im s\leq T$. This cannot equal the
completed-ξ nontrivial-zero count $\Theta(T\log T)$. A zero-free entire
prefactor changes neither conclusion nor the divisor.

Logistic recurrent-clock corollary:
The exact tower zeta

\[
Z_T(z)=\frac{1-z^2}{1-2z^2}
\]

and any continuation of the full reciprocal Artin--Mazur series that still
depends on $s$ only through $z=e^{-s}$ fail the completed-ξ divisor-count
requirement. The tower zeta and full determinant remain distinct ledgers.

Scope:
Single-valued meromorphic same-object determinants that factor through a unit
lattice clock, possibly times a zero-free factor. The result does not exclude
an intrinsically derived non-lattice roof or an operator family with genuine
nonperiodic $s$-dependence.

Reopening condition:
Derive a non-lattice clock or same-object operator dependence from the frozen
target-free dynamics, and prove its divisor-count regime. Adding a
zero-producing correction by hand changes the ledger and does not reopen this
case.

Artifacts:

- `configs/source_locks/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK.yaml`
- `evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T080528Z.yaml`
- `artifacts/p4_logistic_recurrent_uc_anchored_clock/structural_audit.json`
- `formal/obstructions/unit_lattice_clock_vertical_periodicity.md`
- `tests/test_p4_logistic_recurrent_uc_anchored_clock.py`

---

## OBR-009 — Exact-(U_c) first-return branches are not uniformly expanding

Status:
PROVED_OBSTRUCTION

Source:
CLUE-A1-004 / P4-LOGISTIC-UC-FIRST-RETURN-SUPPORT /
`formal/obstructions/exact_uc_first_return_nonuniform_expansion.md`

Statement:
Let

\[
f(x)=1-U_cx^2,
\qquad
J=[1-U_c,1],
\qquad
L=J\cap\{x<0\},
\]

and let (R(x)=f^{\tau_L(x)}(x)) be the unaccelerated first-return map to
(L). For every physical return branch (C_{2n}),

\[
\inf_{x\in C_{2n}}|R'(x)|=0.
\]

Already on (C_2=(-r_1,0)),

\[
(f^2)'(x)=4U_c^2x f(x)\longrightarrow0
\qquad(x\uparrow0),
\]

and the interior witness `x=-0.01` has

```text
|(f^2)'(x)| = 0.0953043164222... < 1.
```

Every higher branch similarly accumulates on a critical preimage. The inverse
Jacobian has a square-root endpoint singularity,

\[
\left|\frac{dx}{dy}\right|
\sim
\frac{1}{2\sqrt2\,U_c}(y+\rho)^{-1/2},
\qquad \rho=U_c-1.
\]

Consequence:
The ordinary piecewise-uniformly-expanding `BV` / Lasota--Yorke argument in
legacy Paper 2 does not apply to this unaccelerated induced map. In particular,
that argument does not establish its claimed ordinary-`BV` spectral gap or the
downstream asymptotically geometric branch-weight theorem. A later direct
physical-density theorem independently proves the mass-ratio conclusion,

\[
\frac{\mu_{\rm ac}(C_{2n+2})}{\mu_{\rm ac}(C_{2n})}
\longrightarrow\frac1{2U_c(U_c-1)},
\]

without restoring the failed ordinary-`BV` proof. Thus `OBR-009` remains an
operator obstruction, while its direct-density reopening has successfully
closed the narrower neighboring-mass-ratio obligation. The stronger legacy
exponential-remainder statement remains open.

Scope:
The full negative-event first-return map on the exact physical core, with its
natural unaccelerated branches. The obstruction does not exclude a further
accelerated inducing scheme, a weighted/cusp-adapted or anisotropic function
space, or a direct theorem for the Misiurewicz physical density.

Reopening condition:
Freeze one replacement domain and operator ledger, including its return
convention, branch endpoints, function space, norm, distortion estimates, and
action on the square-root singularity. Prove those properties before restoring
any spectral-gap or Fredholm claim. The branch-weight ratio limit no longer
needs this reopening because it has a separate direct proof; an exponential
remainder still requires additional control.

Artifacts:

- `configs/source_locks/P4-LOGISTIC-UC-FIRST-RETURN-SUPPORT.yaml`
- `evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T105010Z.yaml`
- `artifacts/p4_logistic_uc_first_return_support/structural_audit.json`
- `formal/results/exact_uc_first_return_support.md`
- `formal/results/exact_uc_acip_endpoint_density.md`
- `formal/results/exact_uc_acip_cone_enclosure.md`
- `formal/obstructions/exact_uc_first_return_nonuniform_expansion.md`
- `artifacts/p4_logistic_uc_acip_endpoint_density/structural_audit.json`
- `artifacts/p4_logistic_uc_acip_cone_enclosure/certified_bounds.json`
- `evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T162511Z.yaml`
- `tests/test_p4_logistic_uc_first_return_support.py`
- `tests/test_p4_logistic_uc_acip_endpoint_density.py`
