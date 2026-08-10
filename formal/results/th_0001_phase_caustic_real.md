# TH-0001 on-shell caustic incidence

This scoped audit keeps the frozen ordered three-kick Fourier-integral object
unchanged:

\[
\Phi=S_{1/2}(q_0,q_1)+S_{3/2}(q_1,q_2)+S_{5/2}(q_2,q_3),
\qquad S_a(x,y)=xy-x+\frac a3x^3.
\]

The previous audit found the internal Hessian

\[
H_{\rm int}=\begin{pmatrix}3q_1&1\\1&5q_2\end{pmatrix},
\qquad \det H_{\rm int}=15q_1q_2-1.
\]

The present question is only whether this caustic is reached by the actual
stationary canonical relation.

## Exact incidence

The stationary equations are

\[
q_0+\frac32q_1^2+q_2-1=0,
\qquad
q_1+\frac52q_2^2+q_3-1=0.
\]

On the caustic, put `t=q1` with `t` real and nonzero. Solving the three
exact equations gives

\[
q_2=\frac1{15t},\qquad
q_0=1-\frac32t^2-\frac1{15t},\qquad
q_3=1-t-\frac1{90t^2}.
\]

Thus every real nonzero-`t` point of the internal caustic has stationary
endpoint data. The endpoint map on the stationary Lagrangian is

\[
(q_1,q_2)\longmapsto
\left(1-\frac32q_1^2-q_2,\,1-q_1-\frac52q_2^2\right),
\]

whose Jacobian is `-H_int`. The caustic is therefore an actual
singular projection of the stationary Lagrangian, not an artifact of arbitrary
off-shell integration coordinates.

## Rational canonical witness

At `t=1`,

\[
(q_0,q_1,q_2,q_3)=\left(-\frac{17}{30},1,\frac1{15},-\frac1{90}\right),
\]

and the canonical momenta are

\[
(p_0,p_1,p_2,p_3)=\left(-\frac{289}{1800},-\frac{17}{30},1,\frac1{15}\right).
\]

Direct substitution gives zero residual for each of the six coordinate
equations of the three frozen kicks. At this witness,

\[
H_{\rm int}=\begin{pmatrix}3&1\\1&1/3\end{pmatrix}
\]

has rank one. The null direction `(-1,3)` is annihilated by the Hessian,
while the third directional derivative of `Phi` is `132 != 0`. This is a
regular rank-one caustic witness in the frozen chart.

## Route-A scope

The result strengthens `OBR-011`: a global single nondegenerate phase/Maslov
chart is obstructed on the physically attained stationary relation. It does
not construct the required multi-chart transition ledger. The factorized
unitary FIO remains valid, but no determinant, spectrum, trace formula, Route B,
Hilbert--Pólya realization, or Riemann-Hypothesis claim is made.

Recommended verdict: `GO_WITH_LIMITATIONS` for this scoped A4 audit; stop the
sub-audit and reopen only under an explicit multi-chart phase/Maslov source
lock, or pivot breadth-first to another candidate.
