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
