# OBR-017 — Positive integer-renewal determinants force a right-half-plane zero

Status: PROVED_OBSTRUCTION (connected-renewal scope)

Source: SS-0003 / formal/results/ss_0003_connected_renewal.md

## Statement

Consider the target-free hub-and-spoke renewal graph with labels n>=2,
two directed edges per excursion, roof (1/2)log(n) on each edge, and zero
potential.  On

\[
\mathcal H=\mathbb C e_h\oplus\ell^2(\{2,3,\ldots\}),
\]

the holomorphic finite-rank transfer family on Re(s)>1 is

\[
\mathcal L_s(c,x)=\left(\sum_{n\ge2}n^{-s/2}x_n,
                     c(n^{-s/2})_{n\ge2}\right).
\]

Its same-object Fredholm determinant is

\[
D(s)=\det_F(I-\mathcal L_s)
    =1-\sum_{n\ge2}n^{-s}=2-\zeta(s).
\]

For real sigma>1, S(sigma)=sum_{n>=2} n^(-sigma) is continuous, strictly
decreasing, tends to +infinity as sigma decreases to 1, and obeys

\[
S(2)<\frac14+\int_2^\infty x^{-2}\,dx=\frac34<1.
\]

Therefore there is a unique sigma_star in (1,2) with S(sigma_star)=1, and

\[
D(\sigma_*)=0.
\]

The completed Riemann xi-function is zero-free for Re(s)>1, so no zero-free
prefactor can turn this frozen determinant into a completed-xi divisor under
the same clock and normalization.

## Scope and invalid shortcuts

This obstruction applies to positive one-hub renewal sums with the frozen
integer-label rule.  It does not rule out every connected renewal system or
signed/complex weight system.  It does rule out silently fixing the failure by
an affine shift, a fitted phase, a separate reciprocal determinant, or a
post-hoc zero-producing correction.

The same candidate also has a scalar continuation 2-zeta(s) on
C minus {1}, but that continuation is not the Fredholm determinant of the
original ell2 operator outside Re(s)>1.

## Reopening condition

Freeze a structurally different connected grammar and its signed/complex
weight ledger before target data.  Prove a zero-free right half-plane and a
same-object determinant/continuation theorem before any divisor comparison.
