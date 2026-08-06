# Harmonic Graph-Tower Naive-Determinant Obstruction

**Status:** proved obstruction
**Triggering candidate:** `QG-0001`
**Active clue:** `CLUE-A4-003`
**Route-A layer:** A2

## 1. Statement

Suppose a graph or symbolic component has a primitive orbit with fixed
nonzero weight (w\neq0) and positive period (L). Form an infinite tower in
which component (n) reproduces that orbit with the same weight and period
(L/n). Then the ordinary componentwise Euler product contains

\[
P(s)=\prod_{n\geq1}\left(1-we^{-sL/n}\right).
\]

For every fixed (s\in\mathbb C), its factors satisfy

\[
1-we^{-sL/n}\longrightarrow1-w\neq1.
\]

A necessary condition for convergence of an infinite product to a finite
nonzero limit is that its factors tend to one. Therefore (P(s)) cannot
define a finite nonzero ordinary Euler product on any domain.

The same issue prevents the standard Fredholm determinant of a direct sum of
finite bond-transfer blocks whenever those blocks fail to approach zero in
trace norm.

## 2. QG-0001 witness

In `QG-0001`, the pendant bounce (e_3^+e_3^-) is primitive. Dirichlet
reflection contributes (-1), Kirchhoff backscatter at the degree-four
vertex contributes (-1/2), and the magnetic phase is zero. Hence

\[
w=\frac12,
\qquad
L=2\sqrt5.
\]

The frozen tower therefore contains the subproduct

\[
\prod_{n\geq1}
\left(1-\frac12e^{-2\sqrt5s/n}\right),
\]

whose factors tend to (1/2). For real (s\geq0), the partial products tend
to zero exponentially after a finite index. Thus no nonzero unregularized
orbit determinant exists.

## 3. Impact

The correct (K\log K) eigenvalue count of the natural graph Laplacian does
not automatically supply a Route-A determinant. Any continuation must first
freeze one explicit regularization, its counterterms, its primitive/repetition
trace identity, its divisor, and its relation to the same quantum operator.

The heat/spectral zeta

\[
\zeta_H(z)=\zeta(2z)\zeta_{H_1}(z)
\]

is a separate data type. It cannot be substituted for a wavenumber secular
determinant merely because it contains a Riemann-zeta factor.

## 4. Scope boundary

This obstruction applies only to the naive unregularized Euler product and
the standard trace-class Fredholm determinant for a harmonic short-orbit
tower with a repeated nonzero weight.

It does not exclude:

- a canonically derived Weierstrass or relative determinant;
- a renormalized trace formula with explicit local counterterms;
- another infinite graph whose component weights decay sufficiently fast;
- a connected infinite graph with a different primitive-orbit law.

Those are reopening directions, not established successes.
