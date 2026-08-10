# OBR-011 — Three-kick FIO has an internal caustic for single-phase reduction

Status: `PROVED_OBSTRUCTION` for a global single reduced phase chart.

Scope: this does **not** obstruct the factorized unitary operator
\(U_{5/2}U_{3/2}U_{1/2}\). It only obstructs replacing its ordered iterated
oscillatory kernel by one globally nondegenerate type-I phase without changing
charts or adding a separate caustic calculus.

## Exact phase

For input \(q_0\), intermediate variables \(q_1,q_2\), and output \(q_3\),

\[
\Phi=S_{1/2}(q_0,q_1)+S_{3/2}(q_1,q_2)+S_{5/2}(q_2,q_3),
\]

where \(S_a(x,y)=xy-x+(a/3)x^3\). The Hessian in the internal variables is

\[
H_{\rm int}=\begin{pmatrix}3q_1&1\\1&5q_2\end{pmatrix},
\qquad
\det H_{\rm int}=15q_1q_2-1.
\]

The caustic set

\[
15q_1q_2-1=0
\]

is nonempty; \((q_1,q_2)=(1,1/15)\) is an exact rational witness. Therefore
the stationary-phase elimination of both internal variables is not globally
nondegenerate.

## On-shell strengthening

The follow-up audit `TH-0001-A4-PHASE-CAUSTIC-REAL-001` shows that the caustic
is attained by the stationary canonical relation. The stationary equations
are

\[
q_0+\frac32q_1^2+q_2-1=0,
\qquad
q_1+\frac52q_2^2+q_3-1=0.
\]

Writing `t=q1` with `t` nonzero and imposing `15*q1*q2=1` gives

\[
q_2=\frac1{15t},\quad
q_0=1-\frac32t^2-\frac1{15t},\quad
q_3=1-t-\frac1{90t^2}.
\]

The endpoint projection of this stationary Lagrangian has Jacobian

\[
\frac{\partial(q_0,q_3)}{\partial(q_1,q_2)}
=-\begin{pmatrix}3q_1&1\\1&5q_2\end{pmatrix},
\]

so its singular set is exactly the same caustic. At `t=1`, the exact real
trajectory has

\[
(q_0,q_1,q_2,q_3)=\left(-\frac{17}{30},1,\frac1{15},-\frac1{90}\right),
\]

\[
(p_0,p_1,p_2,p_3)=\left(-\frac{289}{1800},-\frac{17}{30},1,\frac1{15}\right).
\]

The Hessian has rank one there, with null direction `(-1,3)`, and the third
directional derivative is `132 != 0`. Hence the obstruction is not merely an
off-shell internal-coordinate warning: it is present on a real stationary
Lagrangian branch. This is a strengthening of `OBR-011`, not a new independent
obstruction.

## Consequence

The source lock must retain the product as an ordered oscillatory integral and
the operator as the factorization \(U_a=\mathcal F_+M_a\). A single global
reduced generating function, a global determinant of the internal Hessian, or a
global orbit Maslov index cannot be silently inferred. The positive-real
per-factor normalization remains valid, and factorized Plancherel unitarity is
unchanged.

This is a reusable warning for composed kicked maps: a natural unitary lift can
exist even when its multi-step kernel crosses caustics. Any later orbit-phase
ledger must be charted and explicitly signed; negative classical multipliers
must not be relabeled as Maslov or magnetic phases.

Artifacts:

- `configs/source_locks/TH-0001-FIO.yaml`
- `experiments/th_0001_phase_caustic_audit.py`
- `artifacts/th_0001/phase_caustic_audit.json`
- `formal/results/th_0001_fio_quantization.md`
- `tests/test_th_0001_phase_caustic_audit.py`
- `configs/source_locks/TH-0001-PHASE-CAUSTIC-REAL.yaml`
- `experiments/th_0001_phase_caustic_real.py`
- `artifacts/th_0001/phase_caustic_real_audit.json`
- `formal/results/th_0001_phase_caustic_real.md`
- `evaluations/route_a/TH-0001/20260810T074238Z.yaml`
- `tests/test_th_0001_phase_caustic_real.py`
