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

Current reopening status (2026-08-08):
`P4-LOGISTIC-UC-POLAR-NONLATTICE` proves that the same exact polar dynamics
has an intrinsic roof $\tau=\log|G'|$ with two primitive periods satisfying
$T_{LR}/T_R\notin\mathbb Q$. Therefore this new roof is outside the unit-
lattice hypothesis of `OBR-008`; the obstruction remains fully active for the
old return-label clock and every determinant that factors only through
$e^{-s}$. `P4-LOGISTIC-UC-POLAR-COMPLEX-BRANCH` subsequently proves the
same-object frozen-radius complex branches, common logarithm germ, compact
inclusion, and matching-space invariance. The partition and boundary audits
then close the target-copy and endpoint-trace ledgers. Finally, formal
candidate `LOG-0001` proves full matching-space order-zero nuclearity and the
genuine same-object determinant

\[
\Delta(\lambda,s)=\det_{\rm Fr}(I-\lambda\mathcal L_s|_B),
\qquad
D_{\rm pol}(s)=\Delta(1,s),
\]

with nonperiodic $s$-dependence and an exact signed trace formula. Thus
LOG-0001 lies completely outside the hypothesis of `OBR-008`; this does not
refute or weaken the obstruction for the old unit-clock object. The remaining
reopening obligation was to prove the intrinsic high-height divisor count or
growth regime of $D_{\rm pol}$.

Growth update (2026-08-08): `LOG-0001-GROWTH-ORDER` proves

\[
|D_{\rm pol}(s)|\leq
\exp\!\bigl(C_0+C_1(1+|s|)^2\bigr),
\]

so the same-object determinant has classical order at most two and at most
`O(T^2)` zeros in every fixed real strip. It is also zero-free for
`Re(s)>log(2)/log(4/U_c^2)`, with uniform upper and lower modulus bounds on
each closed sub-half-plane above that threshold. This upper theorem neither
extends `OBR-008` to the non-lattice determinant nor proves a divisor mismatch:
`O(T^2)` is compatible with a smaller `T log T` regime. The remaining open
obligation is a sharp/lower same-object divisor theorem.

Artifacts:

- `configs/source_locks/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK.yaml`
- `evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T080528Z.yaml`
- `artifacts/p4_logistic_recurrent_uc_anchored_clock/structural_audit.json`
- `formal/obstructions/unit_lattice_clock_vertical_periodicity.md`
- `tests/test_p4_logistic_recurrent_uc_anchored_clock.py`
- `configs/source_locks/P4-LOGISTIC-UC-POLAR-NONLATTICE.yaml`
- `formal/results/exact_uc_polar_nonlattice.md`
- `artifacts/p4_logistic_uc_polar_nonlattice/nonlattice_certificate.json`
- `evaluations/route_a/P4-LOGISTIC-UC-POLAR-NONLATTICE/20260805T110654Z.yaml`
- `tests/test_p4_logistic_uc_polar_nonlattice.py`
- `configs/source_locks/P4-LOGISTIC-UC-POLAR-COMPLEX-BRANCH.yaml`
- `formal/results/exact_uc_polar_complex_branch.md`
- `artifacts/p4_logistic_uc_polar_complex_branch/complex_branch_certificate.json`
- `evaluations/route_a/P4-LOGISTIC-UC-POLAR-COMPLEX-BRANCH/20260805T125236Z.yaml`
- `tests/test_p4_logistic_uc_polar_complex_branch.py`
- `configs/source_locks/P4-LOGISTIC-UC-POLAR-PARTITION-TRACE.yaml`
- `formal/results/exact_uc_polar_partition_trace.md`
- `configs/source_locks/P4-LOGISTIC-UC-POLAR-BOUNDARY-TRACE.yaml`
- `formal/results/exact_uc_polar_boundary_trace.md`
- `configs/source_locks/LOG-0001-NUCLEAR-FREDHOLM.yaml`
- `configs/source_locks/LOG-0001-GROWTH-ORDER.yaml`
- `formal/results/log_0001_nuclear_fredholm.md`
- `formal/results/log_0001_growth_order.md`
- `artifacts/log_0001_nuclear_fredholm/nuclear_fredholm_certificate.json`
- `artifacts/log_0001_growth_order/growth_order_certificate.json`
- `evaluations/route_a/LOG-0001/20260808T051519Z.yaml`
- `evaluations/route_a/LOG-0001/20260808T104049Z.yaml`
- `tests/test_log_0001_nuclear_fredholm.py`
- `tests/test_log_0001_growth_order.py`

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
closed the neighboring-mass-ratio limit. A later complete Arb cone audit
certifies sharper absolute density and finite-mass intervals. The subsequent
cusp-adapted audit also proves an explicit geometric rate for adjacent mass
ratios, without supplying a spectral gap. Any stronger legacy finite-order
mass formula not implied by this ratio rate remains open, and none of these
direct density results removes this operator obstruction.

Scope:
The full negative-event first-return map on the exact physical core, with its
natural unaccelerated branches. The obstruction does not exclude a further
accelerated inducing scheme, a weighted/cusp-adapted or anisotropic function
space, or a direct theorem for the Misiurewicz physical density.

Reopening condition:
Freeze one replacement domain and operator ledger, including its return
convention, branch endpoints, function space, norm, distortion estimates, and
action on the square-root singularity. Prove those properties before restoring
any spectral-gap or Fredholm claim. The branch-weight ratio limit and its
explicit convergence rate no longer need this reopening because they have a
separate cusp-adapted proof; an exact finite-order mass law or operator theorem
still requires additional control.

Artifacts:

- `configs/source_locks/P4-LOGISTIC-UC-FIRST-RETURN-SUPPORT.yaml`
- `evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T105010Z.yaml`
- `artifacts/p4_logistic_uc_first_return_support/structural_audit.json`
- `formal/results/exact_uc_first_return_support.md`
- `formal/results/exact_uc_acip_endpoint_density.md`
- `formal/results/exact_uc_acip_cone_enclosure.md`
- `formal/results/exact_uc_acip_sharp_cone_enclosure.md`
- `formal/results/exact_uc_branch_mass_rate.md`
- `formal/obstructions/exact_uc_first_return_nonuniform_expansion.md`
- `artifacts/p4_logistic_uc_acip_endpoint_density/structural_audit.json`
- `artifacts/p4_logistic_uc_acip_cone_enclosure/certified_bounds.json`
- `artifacts/p4_logistic_uc_acip_sharp_cone_enclosure/interval_certificate.json`
- `artifacts/p4_logistic_uc_branch_mass_rate/rate_certificate.json`
- `evaluations/route_a/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK/20260804T162511Z.yaml`
- `evaluations/route_a/P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE/20260805T012200Z.yaml`
- `evaluations/route_a/P4-LOGISTIC-UC-BRANCH-MASS-RATE/20260805T035348Z.yaml`
- `tests/test_p4_logistic_uc_first_return_support.py`
- `tests/test_p4_logistic_uc_acip_endpoint_density.py`
- `tests/test_p4_logistic_uc_acip_sharp_cone_enclosure.py`
- `tests/test_p4_logistic_uc_branch_mass_rate.py`

---

## OBR-010 — Low-depth Hénon reversibility classes do not supply a twist

Status:
PROVED_OBSTRUCTION

Source:
`CLUE-A4-001` / `formal/obstructions/low_depth_henon_reversibility.md`

Statement:
The target-free legacy Hénon parent

\[
F_a(q,p)=(1-aq^2-p,q)
\]

has the exact swap reversor \(R(q,p)=(p,q)\), and the audited one-kick
quadratic shears, static generalized-Hénon deformations, and arbitrary
two-kick products retain an explicit reversor (possibly after a coordinate
conjugacy or clock-origin shift). Therefore those low-complexity subclasses
cannot by themselves provide a time-reversal-breaking twisted candidate.

For the frozen non-palindromic three-kick product

\[
G=F_{5/2}\circ F_{3/2}\circ F_{1/2},
\]

the inherited swap and all affine anti-symplectic involutions are excluded by
exact witnesses and leading-term comparison. This is a positive escape from
the audited low-depth classes, not a proof that every nonlinear or
non-polynomial anti-symplectic reversor is absent.

Impact:
Do not promote the legacy one-/two-kick Hénon or quartic/schedule proxies to a
Route-A twist on the basis of area preservation, PT language, or a finite real
spectrum. Keep the three-kick candidate's residual nonlinear-reversor question
explicitly open.

Scope:
Only the listed low-depth polynomial classes and the affine reversor class
audited in the TH-0001 prefilter. Arbitrary nonlinear reversors, determinants,
quantization, and spectral claims are outside this obstruction.

Reopening condition:
Provide one explicit frozen product outside the audited classes, then either
certify a new reversor or prove a separate symmetry theorem. Changing the kick
order, parameter rule, clock, or normalization reopens the source lock.

Artifacts:

- `configs/source_locks/TH-0001.yaml`
- `formal/obstructions/low_depth_henon_reversibility.md`
- `formal/results/th_0001_three_kick_prefilter.md`
- `evaluations/route_a/TH-0001/20260806T024238Z.yaml`
- `tests/test_th_0001_three_kick_henon.py`

---

## OBR-011 — Three-kick FIO has an internal caustic for global single-phase reduction

Status:
PROVED_OBSTRUCTION

Source:
`CLUE-A4-001` / `formal/obstructions/th_0001_single_phase_caustic.md`

Statement:
For the ordered internal phase of the frozen three-kick FIO,

\[
\Phi=S_{1/2}(q_0,q_1)+S_{3/2}(q_1,q_2)+S_{5/2}(q_2,q_3),
\]

the Hessian in \((q_1,q_2)\) is

\[
\begin{pmatrix}3q_1&1\\1&5q_2\end{pmatrix},
\qquad
\det=15q_1q_2-1.
\]

The exact rational point \((q_1,q_2)=(1,1/15)\) lies on the nonempty caustic
set. Hence the two internal variables cannot be globally eliminated into one
nondegenerate type-I phase chart. The ordered oscillatory integral and the
factorized `L^2(R)` unitary remain well-defined.

Impact:
Do not silently assign a global reduced generating function, global Hessian
determinant, or global orbit Maslov index to this product. Keep the positive-
real per-factor phase convention and preserve chart/caustic information.

Scope:
Only global single-phase reduction of the frozen three-kick kernel. This does
not obstruct the unitary factorization, and it does not exclude a future
explicit multi-chart phase calculus.

On-shell strengthening (2026-08-10):
The exact stationary equations intersect the caustic in the full real family

\[
q_1=t\ne0,\quad q_2=(15t)^{-1},\quad
q_0=1-\frac32t^2-(15t)^{-1},\quad
q_3=1-t-(90t^2)^{-1}.
\]

The endpoint projection Jacobian is `-H_int`, so the caustic is the actual
singular set of the stationary-Lagrangian projection. At `t=1`, the exact
canonical witness has
`(q0,q1,q2,q3)=(-17/30,1,1/15,-1/90)` and
`(p0,p1,p2,p3)=(-289/1800,-17/30,1,1/15)`. The Hessian has rank one and the
null-direction third derivative is `132 != 0`. This strengthens OBR-011 but is
not a new independent obstruction.

Reopening condition:
Freeze a multi-chart phase/Maslov ledger with caustic transition rules and
prove its compatibility with the ordered FIO. Signed classical multipliers
cannot be used as a substitute.

Artifacts:

- `configs/source_locks/TH-0001-FIO.yaml`
- `experiments/th_0001_phase_caustic_audit.py`
- `artifacts/th_0001/phase_caustic_audit.json`
- `formal/obstructions/th_0001_single_phase_caustic.md`
- `evaluations/route_a/TH-0001/20260806T053410Z.yaml`
- `tests/test_th_0001_phase_caustic_audit.py`
- `configs/source_locks/TH-0001-PHASE-CAUSTIC-REAL.yaml`
- `experiments/th_0001_phase_caustic_real.py`
- `artifacts/th_0001/phase_caustic_real_audit.json`
- `formal/results/th_0001_phase_caustic_real.md`
- `evaluations/route_a/TH-0001/20260810T074238Z.yaml`
- `tests/test_th_0001_phase_caustic_real.py`

---

## OBR-012 — Harmonic short-orbit towers have no naive ordinary determinant

Status:
PROVED_OBSTRUCTION

Source:
`CLUE-A4-003` / `QG-0001` /
`formal/obstructions/harmonic_graph_tower_naive_determinant.md`

Statement:
Suppose a tower repeats a primitive orbit of fixed nonzero weight \(w\) with
component-\(n\) period \(L/n\). Its ordinary Euler product contains

\[
\prod_{n\geq1}\left(1-we^{-sL/n}\right).
\]

The factors tend to \(1-w\ne1\), so the product cannot converge to a finite
nonzero ordinary determinant. For the standard directed-bond convention,

\[
B_n(s)=S\,\operatorname{diag}_b
\left(e^{-s\ell_b/n+i\alpha_b}\right)
\longrightarrow
S\,\operatorname{diag}_b(e^{i\alpha_b})
\]

in finite-dimensional trace norm. The limiting QG-0001 block is unitary on
eight directed bonds, so \(\lVert B_n(s)\rVert_1\to8\). Its direct sum is not
compact or trace class and therefore has no standard Fredholm determinant.

QG-0001 witness:
The pendant bounce has exact signed scattering weight \(w=1/2\), phase zero,
and period \(2\sqrt5/n\). Therefore its subproduct factors tend exactly to
\(1/2\).

Impact:
An intrinsic \(K\log K\) operator counting law does not by itself provide a
Route-A determinant. Do not silently turn the divergent component product
into a Weierstrass, relative, or zeta-regularized determinant, and do not
promote the separate heat/spectral-zeta identity to a secular divisor.

Scope:
Naive unregularized Euler products and standard trace-class Fredholm
determinants for towers with repeated nonzero orbit weights and periods
scaling as \(L/n\).

Reopening condition:
Freeze one explicit same-object regularization, its local counterterms,
primitive/repetition trace identity, characteristic variable, and divisor.
Prove normal convergence and compatibility with the natural graph operator.

2026-08-06 resolution boundary:
QG-0001 now has a valid same-operator inverse-spectral relative determinant,
`det_F(I-k^2 H^{-1})`. This satisfies the convergence, counterterm, variable,
and operator-compatibility parts, but it does not reopen the ordinary orbit or
bond-block products: no primitive/repetition trace identity relates them to
the inverse spectral moments. `OBR-012` therefore remains in force for its
stated determinant types.

Artifacts:

- `configs/source_locks/QG-0001.yaml`
- `experiments/qg_0001_harmonic_magnetic_tower.py`
- `artifacts/qg_0001/route_a_prefilter.json`
- `formal/results/qg_0001_harmonic_magnetic_tower.md`
- `formal/obstructions/harmonic_graph_tower_naive_determinant.md`
- `evaluations/route_a/QG-0001/20260806T090351Z.yaml`
- `tests/test_qg_0001_harmonic_magnetic_tower.py`

---

## OBR-013 — A harmonic graph tower has an immutable total-length divisor coefficient

Status:
PROVED_OBSTRUCTION

Source:
`CLUE-A4-003` / `QG-0001` /
`formal/results/qg_0001_relative_fredholm.md` /
`formal/obstructions/harmonic_graph_tower_divisor_coefficient.md`

Statement:
Let a positive compact metric-graph Laplacian (H_1) have total metric
length (L), and form the exact harmonic tower

\[
H=\bigoplus_{n\geq1}n^2H_1
\]

in the raw wavenumber clock. Then (H^{-1}) is trace class and

\[
D_H(k)=\det_F(I-k^2H^{-1})
\]

is a genuine entire relative determinant. Its positive divisor count is

\[
N_{D_H}(K)=\frac{L}{\pi}K\log K+O(K).
\]

Therefore equality with the completed-xi divisor up to a zero-free factor
requires the necessary coefficient condition (L=1/2). A zero-free factor
cannot alter this count.

QG-0001 witness:

\[
L=L_0=1+\sqrt2+\sqrt3+\sqrt5,
\]

so the candidate-to-target leading ratio is

\[
2L_0=12.764664694883524\ldots\neq1.
\]

The source lock forbids a post-hoc spectral rescaling. Hence the exact
QG-0001 relative determinant cannot be a completed-xi divisor up to a
zero-free factor.

Impact:
Obtaining the (K\log K) exponent from a harmonic component tower is
insufficient. The base total length fixes the leading coefficient before any
zero comparison. This gate should be checked before orbit enumeration or
determinant numerics for every exact (1/n) graph tower.

Scope:
Positive compact metric-graph bases, exact (1/n) metric scaling, and the raw
wavenumber clock. The result does not exclude a different intrinsically
normalized base, a non-harmonic component law, or another spectral clock that
is fixed independently of target data.

Reopening condition:
Supply a new source-locked graph grammar or component scaling whose clock and
normalization are intrinsic and whose divisor coefficient is proved before
using prime or zero data. Merely rescaling QG-0001 after seeing the mismatch
is forbidden.

Artifacts:

- `configs/source_locks/QG-0001-RELATIVE-FREDHOLM.yaml`
- `experiments/qg_0001_relative_fredholm.py`
- `artifacts/qg_0001/relative_fredholm.json`
- `formal/results/qg_0001_relative_fredholm.md`
- `formal/obstructions/harmonic_graph_tower_divisor_coefficient.md`
- `evaluations/route_a/QG-0001/20260806T123946Z.yaml`
- `tests/test_qg_0001_relative_fredholm.py`

---

## OBR-014 — Frozen COPRIME ell² kernel stops being bounded at Re(s)=1

Status:
PROVED_OBSTRUCTION (candidate-local, scope-limited)

Source:
`COPRIME-0001` / `formal/obstructions/coprime_ell2_operator_boundary.md`

Statement:
For

```text
(L_s)_{mn}=1_{gcd(m,n)=1}(mn)^(-s/2)
```

on `ell²({2,3,...})`, the Mobius trace-class proof works for
`sigma=Re(s)>1`. The same matrix is not even a bounded operator for
`sigma<=1`, because

```text
||L_s e_2||² = 2^(-sigma) sum_{m>=3, m odd} m^(-sigma) = infinity.
```

Impact:
The original Fredholm determinant is source-locked to its defining half-plane.
Any scalar continuation across `Re(s)=1` requires a separate theorem or a
different function-space/regularization construction. It cannot be called a
silent extension of the same bounded `ell²` operator.

Scope:
Only the frozen coprime kernel on counting-measure `ell²`; this does not rule
out scalar continuation, another Banach space, or a different determinant.

Reopening condition:
Freeze the alternate object and prove its operator/determinant identity while
keeping its clock and determinant ledger separate from `D_cop`.

Artifacts:

- `configs/source_locks/COPRIME-0001-COUNTABLE-TRACE.yaml`
- `formal/results/coprime_0001_countable_trace.md`
- `formal/obstructions/coprime_ell2_operator_boundary.md`
- `experiments/coprime_0001_countable_trace.py`
- `artifacts/coprime_0001/countable_trace_certificate.json`
- `evaluations/route_a/COPRIME-0001/20260809T134933Z.yaml`
- `tests/test_coprime_0001_countable_trace.py`

---

## OBR-015 — COPRIME scalar determinant has an endpoint zero accumulation at s=1

Status:
`PROVED_OBSTRUCTION` (candidate-local, endpoint-scoped)

Source:
`COPRIME-0001-SCALAR-BOUNDARY-001`

Statement:
For the frozen

```text
(L_s)_{mn}=1_{gcd(m,n)=1}(mn)^(-s/2),   D_cop(s)=det_F(I-L_s),   Re(s)>1,
```

there is a sequence of distinct positive real zeros `s_j downarrow 1`.
The proof temporarily adds label one, factorizes finite prime-coordinate
compressions into local rank-two kernels with eigenvalues

```text
alpha_p^+/-=(1 +/- sqrt((1+3*p^(-s))/(1-p^(-s))))/2,
```

and applies min--max after the codimension-one compression back to labels
`n>=2`.  The top positive products diverge as `s downarrow 1`, whereas
`||L_3||<9/16<1`; continuity forces arbitrarily many crossings of eigenvalue
one and hence Fredholm zeros.

Impact:
`D_cop` has no holomorphic or meromorphic germ through `s=1`.  Thus no
same-object continuation to a half-plane containing that point is available.
This is stronger than the operator-boundary statement `OBR-014`.

Related positive result:
The squarefree-divisor lift

```text
C_s=zeta(s)T_s-P_1,   ||T_s||_{S_2}^2=prod_p(1+3*p^(-2*Re(s))),
```

defines the explicitly named scalar representation
`D_tilde(s)=det_2(I-C_s)` on `Re(s)>1/2, s!=1`, and it equals `D_cop` on
`Re(s)>1`.  This punctured continuation does not extend the original bounded
`ell^2` operator and does not remove the endpoint obstruction.

Scope:
Only the frozen COPRIME determinant and the stated endpoint.  No claim is
made about continuation at every `1+it` with `t!=0`, another function space,
or a new candidate.

Reopening condition:
Freeze a new determinant or function space and its convention explicitly;
do not search roots or compare Riemann zeros.

Artifacts:

- `configs/source_locks/COPRIME-0001-SCALAR-BOUNDARY.yaml`
- `formal/results/coprime_0001_scalar_boundary.md`
- `formal/obstructions/coprime_scalar_endpoint_accumulation.md`
- `experiments/coprime_0001_scalar_boundary.py`
- `artifacts/coprime_0001/scalar_boundary_certificate.json`
- `evaluations/route_a/COPRIME-0001/20260810T034453Z.yaml`

---

## OBR-016 — Countable irrational-roof bouquets can still have only a linear fixed-strip divisor

Status:
`PROVED_OBSTRUCTION` (prefilter scope; no formal candidate)

Source:
`CLUE-A4-002` / `SS-PREFILTER-IRRATIONAL-BOUQUET-001`

Statement:
For the target-free countable suspension

```text
Sigma = disjoint_union_{n>=2} Z/nZ,
sigma(n,j) = (n,j+1 mod n),
tau_n = 1 + sqrt(2)/n,
phi_n = -n,
```

the block-diagonal transfer family on `ell^2(Sigma)` is entire and trace class,
and its one frozen determinant is

```text
D_bouquet(s) = det_Fr(I-L_s)
             = product_{n>=2} (1-exp(-n^2-s*(n+sqrt(2)))) .
```

Its zeros are exactly

```text
s_{n,k}=-(n^2+2*pi*i*k)/(n+sqrt(2)),   n>=2, k in Z.
```

The real parts `-n^2/(n+sqrt(2))` decrease to `-infinity`.  Therefore any
bounded vertical strip contains only finitely many zero lines and has
`N(T)=O(T)`, not the completed-xi `Theta(T log T)` regime.  The two primitive
lengths `2+sqrt(2)` and `3+sqrt(2)` are incommensurate, but the base is
disconnected and not mixing; this is not a thermodynamic non-lattice theorem.

Impact:
Countability, an entire Fredholm determinant, and global incommensurability
alone do not produce a critical divisor.  Superexponentially escaping cycle
actions can force the wrong density even outside the finite-state and Selberg
subclasses.

Scope:
Only disconnected direct-sum cycle bouquets with the stated action/roof
escape.  This does not exclude connected renewal systems, chronological
cocycles, or other non-Selberg nuclear objects whose same-ledger cycle actions
remain in a fixed critical strip.

Invalid shortcuts:

- post-hoc affine shifts or rescaling of the frozen clock;
- replacing the direct Fredholm determinant by a reciprocal or a scattering
  quotient;
- treating the global incommensurability as evidence of mixing or prime-like
  orbit statistics;
- promoting the fixed-strip `O(T)` theorem to a global count over an unbounded
  real half-plane.

Reopening condition:
Freeze a connected or renewal countable-state object with its own intrinsic
clock and determinant, and first prove a same-ledger divisor-count regime before
allocating `SS-0003`.  No Route-B or root work is authorized.

Artifacts:

- `configs/source_locks/SS-PREFILTER-IRRATIONAL-BOUQUET.yaml`
- `experiments/ss_prefilter_irrational_bouquet.py`
- `artifacts/ss_prefilter_irrational_bouquet/audit.json`
- `formal/results/ss_prefilter_irrational_bouquet.md`
- `formal/obstructions/countable_irrational_bouquet_linear_divisor.md`
- `evaluations/route_a/SS-PREFILTER-IRRATIONAL-BOUQUET/20260810T162243Z.yaml`
- `tests/test_ss_prefilter_irrational_bouquet.py`

---

## OBR-017 — Positive integer-renewal determinants force a right-half-plane zero

Status:
`PROVED_OBSTRUCTION` (connected one-hub renewal scope)

Source:
`CLUE-A4-002` / `SS-0003` /
`formal/obstructions/positive_renewal_right_half_plane_zero.md`

Statement:
For the connected graph \(h\leftrightarrow v_n\), \(n\ge2\), with zero
potential and roof \(\frac12\log n\) on each edge, the holomorphic rank-two
family on

\[
\mathbb C e_h\oplus\ell^2(\{2,3,\ldots\}),\qquad \Re s>1,
\]

has the same-object Fredholm determinant

\[
D_{\rm ren}(s)=\det_F(I-\mathcal L_s)
=1-\sum_{n\ge2}n^{-s}=2-\zeta(s).
\]

For real \(\sigma>1\), the positive mass

\[
S(\sigma)=\sum_{n\ge2}n^{-\sigma}
\]

is continuous and strictly decreasing, diverges as \(\sigma\downarrow1\),
and satisfies \(S(2)<3/4<1\).  Hence there is a unique
\(\sigma_*\in(1,2)\) with \(D_{\rm ren}(\sigma_*)=0\).  Completed \(\xi\) is
zero-free for \(\Re s>1\), so no zero-free prefactor can make the two
divisors equal under the frozen clock and normalization.

Impact:
SS-0003 is a genuine connected non-Selberg object whose scalar continuation
has the desired \(\Theta(T\log T)\) fixed-strip divisor order, yet it still
fails before zero-location comparison.  Correct growth order is therefore
not enough: a positive renewal determinant must first pass a real-axis
zero-free-half-plane gate.

Scope:
The proved statement covers SS-0003 and positive one-hub renewal masses with
the same crossing behavior.  It does not exclude every connected renewal
system, signed/complex potentials, or multi-channel cancellations.

Invalid shortcuts:

- shifting or rescaling the frozen clock after seeing the zero;
- inserting a fitted phase or zero-producing completion;
- replacing \(D\) by \(1/D\), \(D'/D\), or a separate scattering quotient;
- calling the scalar continuation a Fredholm continuation of the original
  \(\ell^2\) operator outside \(\Re s>1\);
- inferring target compatibility from \(T\log T\) divisor order alone.

Reopening condition:
Freeze a structurally different connected grammar with an intrinsic
signed/complex weight mechanism.  Prove both a target-free zero-free right
half-plane and a same-ledger determinant/continuation theorem before any
target divisor comparison or numerical root search.

Artifacts:

- `configs/source_locks/SS-0003-CONNECTED-RENEWAL.yaml`
- `evaluations/route_a/SS-0003/20260811T112250Z.yaml`
- `experiments/ss_0003_connected_renewal.py`
- `artifacts/ss_0003/connected_renewal_audit.json`
- `formal/results/ss_0003_connected_renewal.md`
- `formal/obstructions/positive_renewal_right_half_plane_zero.md`
- `docs/literature/ss_0003_a_points_sources.md`
- `tests/test_ss_0003_connected_renewal.py`
