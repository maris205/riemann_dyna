# QG-0001 Harmonic Magnetic Graph-Tower Prefilter

**Status:** proved structural prefilter under the frozen source lock
**Candidate:** `QG-0001`
**Active clue:** `CLUE-A4-003`
**Route-A layers:** A1, A3, A4

## 1. Frozen object

Let the base metric graph have vertices (L,R,D). Three edges join (L) to
(R), and one pendant edge joins (L) to (D). Their lengths and magnetic
line integrals in the (L)-outward orientation are

\[
(\ell_0,\ell_1,\ell_2,\ell_3)
=(1,\sqrt2,\sqrt3,\sqrt5),
\qquad
(\alpha_0,\alpha_1,\alpha_2,\alpha_3)
=\left(0,\frac\pi3,\frac{2\pi}3,0\right).
\]

The vertices (L) and (R) carry covariant Kirchhoff conditions, while the
degree-one terminal (D) is Dirichlet. The (n)-th component is the exact
(1/n) metric scaling of this base graph, with every magnetic line integral
held fixed. The full graph is the disjoint union over (n\geq1).

This definition uses no prime table, zero table, scale fit, unfolding, or
spectral anchoring.

## 2. Exact primitive-orbit ledger

At a Kirchhoff vertex of degree (d), the directed-bond scattering amplitude
from an incoming bond (b) to an outgoing bond (b') is

\[
\sigma_{b'b}=\frac2d-\delta_{b',\bar b}.
\]

At (D), the reflection amplitude is (-1). The resulting eight-by-eight
directed-bond scattering matrix is exactly orthogonal. A closed oriented word
(p=(b_0,\ldots,b_{m-1})), taken modulo cyclic rotation but not orientation
reversal, has weight

\[
w_p=
\prod_{j=0}^{m-1}\sigma_{b_{j+1},b_j}
\exp\!\left(i\sum_{j=0}^{m-1}\alpha_{b_j}\right),
\qquad b_m=b_0.
\]

Its component-(n) metric period is

\[
T_{p,n}=\frac1n\sum_{j=0}^{m-1}\ell_{b_j},
\]

while (w_p) is independent of (n). Exact exhaustive enumeration through
topological period six gives

```text
period 1:   0 primitive oriented orbits
period 2:  10 primitive oriented orbits
period 3:   0 primitive oriented orbits
period 4:  45 primitive oriented orbits
period 5:   0 primitive oriented orbits
period 6: 330 primitive oriented orbits
```

For every (m\leq6), the direct based-word trace ledger agrees exactly with
the primitive/repetition identity

\[
\operatorname{tr}U_s^m
=
\sum_{p:\,|p|\mid m}|p|\,
\left(w_p e^{-sT_{p,1}}\right)^{m/|p|}.
\]

All amplitudes remain signed rational numbers and all magnetic phases remain
sixth-root phase units. No absolute-value replacement is used.

## 3. Geometric antiunitary audit

The decorated vertex signatures are

```text
L: Kirchhoff, degree 4
R: Kirchhoff, degree 3
D: Dirichlet, degree 1
```

so every boundary- and length-preserving graph automorphism fixes every
vertex and edge. The only such automorphism is the identity. The two
independent theta-cycle fluxes contain (pi/3) and (2pi/3); their doubles
are not zero modulo (2pi). Hence the magnetic cohomology class is not gauge
equivalent to its negative.

Therefore the inherited local geometric class consisting of edge-coordinate
complex conjugation, graph isometries, and gauge transformations supplies no
antiunitary symmetry for the frozen graph. This is only a geometric statement.
The self-adjoint compact-resolvent operator proved below admits coefficientwise
complex conjugation in any chosen orthonormal eigenbasis. That abstract
antiunitary commutes with the operator and preserves its domain, but it has no
asserted locality, graph-isometry origin, or primitive-orbit reversal meaning.

## 4. Natural operator theorem

For component (n), let

\[
\mathcal H_n=\bigoplus_{e=0}^3L^2(0,\ell_e/n),
\]

and define the nonnegative closed quadratic form

\[
q_n[\psi]
=
\sum_{e=0}^3\int_0^{\ell_e/n}
\left|\left(-i\frac d{dx}-A_{n,e}\right)\psi_e(x)\right|^2dx
\]

on edgewise (H^1) functions continuous at (L,R) and vanishing at (D),
where (A_{n,e}\ell_e/n=\alpha_e). Its associated operator (H_n) is the
self-adjoint magnetic Laplacian with the frozen vertex conditions.

The Dirichlet terminal forces a positive base gap. Indeed, a zero-form vector
would be covariantly constant on every edge; vanishing at (D) and continuity
then force it to vanish everywhere. Thus

\[
\lambda_1(H_1)>0.
\]

Metric dilation gives the exact unitary equivalence

\[
H_n\simeq n^2H_1.
\]

On

\[
\mathcal H=\bigoplus_{n\geq1}\mathcal H_n,
\qquad
H=\bigoplus_{n\geq1}H_n,
\]

take the standard graph-norm direct-sum domain. The direct sum is
self-adjoint. Each component resolvent is compact and

\[
\|(H_n+1)^{-1}\|
\leq\frac1{n^2\lambda_1(H_1)+1}\longrightarrow0,
\]

so ((H+1)^{-1}) is compact.

## 5. Intrinsic (K\log K) counting law

Let (N_1(K)) count base-graph eigenvalues (lambda_j(H_1)\leq K^2), with
multiplicity. The compact metric-graph Weyl law gives

\[
N_1(K)=\frac{L_0}{\pi}K+O(1),
\qquad
L_0=1+\sqrt2+\sqrt3+\sqrt5.
\]

By exact component scaling,

\[
N_H(K)=\sum_{n\geq1}N_1(K/n).
\]

Only (n\leq K/\sqrt{\lambda_1(H_1)}) contribute. Summing the Weyl law and
using the harmonic-number asymptotic yields

\[
\boxed{
N_H(K)=\frac{L_0}{\pi}K\log K+O(K).
}
\]

Thus a low-complexity, target-free quantum-graph grammar produces the correct
(K\log K) *order* and compact resolvent. The raw leading coefficient is
(L_0/\pi), whereas the positive Riemann-zero coefficient is (1/(2\pi)).
Their ratio is

\[
2L_0=2(1+\sqrt2+\sqrt3+\sqrt5)\approx12.7646646949.
\]

No rescaling is allowed in this prefilter, so the coefficient does not match.

## 6. Determinant boundary

The preceding operator theorem does not define a Route-A dynamical
determinant. Primitive periods accumulate at zero. The pendant bounce is the
exact primitive word (e_3^+e_3^-), with

\[
w_{\rm pend}=(-1)(-1/2)=1/2,
\qquad
T_{{\rm pend},n}=\frac{2\sqrt5}{n}.
\]

Hence an ordinary orbit product would contain

\[
\prod_{n\geq1}
\left(1-\frac12e^{-2\sqrt5s/n}\right),
\]

whose factors tend to (1/2), not (1). It cannot be a nonzero ordinary
Euler product. For the usual directed-bond convention, write

\[
B_n(s)=S\,\operatorname{diag}_{b}
\left(e^{-s\ell_b/n+i\alpha_b}\right),
\]

where (S) is the exact eight-dimensional vertex-scattering matrix. At each
fixed (s), finite-dimensional trace-norm convergence gives

\[
B_n(s)\longrightarrow
B_\infty=S\,\operatorname{diag}_{b}(e^{i\alpha_b}),
\qquad
\lVert B_n(s)\rVert_1\longrightarrow\lVert B_\infty\rVert_1=8.
\]

Both factors in (B_\infty) are unitary. Hence (\bigoplus_nB_n(s)) is not
compact and therefore is not trace class, so its standard Fredholm determinant
is unavailable. This is recorded as `OBR-012`.

There is a separate exact identity, initially for (Re z>1/2),

\[
\zeta_H(z)
=\sum_{n,j}(n^2\lambda_j(H_1))^{-z}
=\zeta(2z)\,\zeta_{H_1}(z).
\]

This is a heat/spectral-zeta identity in the exponent variable (z). Its
(zeta(2z)) factor is not a characteristic determinant in the wavenumber
(K), and its zeros are not operator eigenvalues. Promoting it across data
types would violate the determinant ledger.

## 7. Claim boundary

Established:

- one explicit target-free infinite magnetic quantum graph;
- an exact primitive/repetition prefix with signed and oriented phases;
- failure of the inherited local geometric antiunitary class;
- a natural self-adjoint direct-sum magnetic Laplacian with compact resolvent;
- the all-order wavenumber count (N_H(K)=(L_0/\pi)K\log K+O(K));
- strict failure of the naive ordinary orbit/Fredholm determinant.

Not established:

- a prime-like primitive-orbit law or von-Mangoldt repetition weight;
- any regularized same-object dynamical/secular determinant;
- a completed-ξ divisor, functional equation, or correct leading coefficient;
- a canonical local or orbit-reversal interpretation for the unavoidable
  abstract spectral-basis conjugation;
- Route B, Hilbert–Pólya, or RH.

Reproduction:

```bash
python3 experiments/qg_0001_harmonic_magnetic_tower.py \
  --quiet \
  --output artifacts/qg_0001/route_a_prefilter.json
python3 -m unittest -v tests/test_qg_0001_harmonic_magnetic_tower.py
```
