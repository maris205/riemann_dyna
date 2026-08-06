# Harmonic Graph-Tower Divisor-Coefficient Obstruction

**Status:** proved obstruction  
**Registry ID:** `OBR-013`  
**Witness:** `QG-0001`

## Theorem

Let \(H_1>0\) be a self-adjoint Laplacian on a compact metric graph of total
length \(L>0\). Let \(H_n\simeq n^2H_1\), and define

\[
H=\bigoplus_{n\geq1}H_n.
\]

In the raw wavenumber variable \(K=\sqrt\lambda\):

1. \(H^{-1}\) is trace class;
2. \(D_H(k)=\det_F(I-k^2H^{-1})\) is an entire relative determinant;
3. its positive-zero count is

   \[
   N_{D_H}(K)=\frac{L}{\pi}K\log K+O(K).
   \]

Consequently, equality of its divisor with the positive completed-xi divisor
up to a zero-free entire factor requires \(L=1/2\).

## Proof

Write the base eigenvalues as \(\lambda_j=\kappa_j^2\), including
multiplicity. The compact-graph Weyl law is

\[
N_1(K)=\#\{j:\kappa_j\leq K\}=\frac{L}{\pi}K+O(1).
\]

Thus \(\lambda_j\asymp j^2\), so

\[
\sum_{n,j}\frac1{n^2\lambda_j}
=\zeta(2)\sum_j\lambda_j^{-1}<\infty.
\]

This proves trace class and the Fredholm determinant claim. Its positive
zeros are \(n\kappa_j\), with coincident multiplicities added. Therefore

\[
\begin{aligned}
N_{D_H}(K)
&=\sum_{n\leq K/\kappa_1}N_1(K/n)\\
&=\frac{L}{\pi}K
  \sum_{n\leq K/\kappa_1}\frac1n+O(K)\\
&=\frac{L}{\pi}K\log K+O(K).
\end{aligned}
\]

The positive Riemann-von Mangoldt count has leading term

\[
\frac1{2\pi}K\log K.
\]

Zero-free entire factors do not change zeros or their multiplicities, hence
matching the two divisors requires \(L/\pi=1/(2\pi)\), or \(L=1/2\).

## QG-0001

For the frozen graph,

\[
L_0=1+\sqrt2+\sqrt3+\sqrt5,
\]

and the ratio to the target coefficient is

\[
2L_0=12.764664694883524\ldots.
\]

The source lock permits no affine spectral rescaling. QG-0001 is therefore
`STOP_SCOPED` as a completed-xi divisor candidate, even though its relative
Fredholm determinant is mathematically valid.

## Scope

The obstruction applies to an exact \(1/n\) metric tower in the raw
wavenumber clock. It does not exclude a new intrinsically normalized graph,
a different component law, or another clock fixed before target data. Those
would be new candidates, not repairs of QG-0001.
