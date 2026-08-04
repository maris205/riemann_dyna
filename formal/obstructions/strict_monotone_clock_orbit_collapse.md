# Strict-monotone clock lifts collapse periodic orbits to the clock fixed set

## Status

`PROVED_OBSTRUCTION`

Source: `CLUE-A1-004` / `P4-LOGISTIC-MONOTONE-CLOCK-LIFT`

## General skew-product identity

Let \(Y\) and \(B\) be sets, let \(g:B\to B\), and let
\(f_b:Y\to Y\) be a fibre map for every \(b\in B\). Define

\[
F(y,b)=(f_b(y),g(b)).
\]

For every \(m\geq1\), direct iteration gives

\[
F^m(y,b)=
\left(
f_{g^{m-1}b}\circ\cdots\circ f_{gb}\circ f_b(y),
g^m(b)
\right).
\]

Consequently,

\[
\operatorname{Fix}(F^m)
=
\bigcup_{b\in\operatorname{Fix}(g^m)}
\left\{
(y,b):
f_{g^{m-1}b}\circ\cdots\circ f_b(y)=y
\right\}.
\]

In particular, if the base has no periodic points, the skew product has no
periodic points. More generally, every full-space periodic orbit projects to a
periodic orbit of the base. A return in the fibre coordinate alone is not a
periodic orbit of the autonomous lift.

If there is a strict Lyapunov coordinate \(L:B\to\mathbb R\) with
\(L(gb)<L(b)\) away from a fixed set \(B_0\), every periodic orbit is confined
to \(B_0\).

## Compact Logistic clock

Freeze the legacy schedule

\[
\mu_n=u_c+\frac{k}{\log^2(n+10)},
\qquad n\geq1,
\]

and set

\[
v_n=\frac1{\log(n+10)}.
\]

On

\[
X=[-1,1]\times[0,1/\log 11],
\]

define

\[
F(x,v)=
\left(1-(u_c+kv^2)x^2,G(v)\right),
\]

where

\[
G(v)=
\begin{cases}
\displaystyle
\frac1{\log(e^{1/v}+1)}
=
\frac{v}{1+v\log(1+e^{-1/v})},&v>0,\\[6pt]
0,&v=0.
\end{cases}
\]

For \(v>0\), induction yields the exact identity

\[
G^m(v)
=
\frac1{\log(e^{1/v}+m)}
=
\frac{v}{1+v\log(1+me^{-1/v})}.
\]

Thus \(G^m(v)<v\) for every \(v>0\) and \(m\geq1\), while \(G^m(0)=0\).
Therefore

\[
\operatorname{Fix}(G^m)=\{0\}.
\]

The fibre map at \(v=0\) is the static limit map

\[
f_{u_c}(x)=1-u_cx^2.
\]

The general skew-product identity now gives

\[
\boxed{
\operatorname{Fix}(F^m)
=
\operatorname{Fix}(f_{u_c}^m)\times\{0\}
}
\qquad(m\geq1).
\]

Primitive full-space orbits therefore satisfy

\[
\operatorname{Prim}(F)
=
\operatorname{Prim}(f_{u_c})\times\{0\}.
\]

No periodic orbit visits the interior \(v>0\), so no periodic orbit samples
the aging part of the schedule.

The frozen endpoint formulas give

\[
0<u_c\leq u_c+kv^2\leq1.5637<2.
\]

Hence the fibre maps send \([-1,1]\) into itself and \(F:X\to X\) is a
well-defined autonomous map.

## Neutral clock multiplier

Since

\[
\frac{G(v)}v
=
\frac1{1+v\log(1+e^{-1/v})}
\longrightarrow1
\qquad(v\downarrow0),
\]

we have \(G'(0)=1\). Along every boundary periodic orbit the derivative is
triangular and contains the clock multiplier \(1\). Thus a standard
hyperbolic stability factor involving

\[
\det(I-DF^m)
\]

is degenerate in the clock direction. Removing this neutral multiplier by
hand would define a different determinant ledger.

## Formal Artin--Mazur consequence

Define only the formal series

\[
Z_{\rm AM,F}(z)
=
\exp\left(
\sum_{m\geq1}\frac{\#\operatorname{Fix}(F^m)}m z^m
\right),
\qquad
D_{\rm AM,F}(z)=Z_{\rm AM,F}(z)^{-1}.
\]

The fixed-set identity proves coefficient by coefficient that

\[
D_{\rm AM,F}(z)=D_{\rm AM,f_{u_c}}(z)
\]

as formal power series. The autonomous slow-clock lift contributes no new
periodic-orbit data beyond the static limit parent.

This statement does not assert convergence, analytic continuation, a Ruelle
or Fredholm determinant, or a completed-\xi divisor identity.

## Invalid repairs

1. **Modulo clock.** Replacing the clock by a period-\(P\) counter makes step
   \(P+1\) reuse \(\mu_1\), rather than the original \(\mu_{P+1}\). It is a
   different schedule.
2. **Clamped clock.** Freezing at a cutoff \(N\) creates a static boundary map
   with parameter \(\mu_N\). Changing \(N\) changes the orbit ledger.
3. **Projected return.** A point may return in \(x\) while \(v\) changes; this
   is not a full-state periodic point.
4. **Aggregate-matrix cycle.** A graph cycle of an occupation-conditioned
   matrix need not be a chronological orbit of the skew product.
5. **Silent neutral-mode removal.** Dropping the clock multiplier from a
   stability weight changes the determinant convention.

## Scope and reopening condition

This obstruction applies to skew-product lifts whose base has no nontrivial
periodic orbit, or whose strict Lyapunov coordinate confines all recurrence to
a fixed subset. It does not exclude every autonomous lift.

Reopening requires one of:

- an intrinsic recurrent base with nontrivial periodic orbits that leave the
  static-limit slice and reproduce logarithmic aging without a reset or
  finite-cutoff periodization; or
- a chronological transfer-cocycle determinant with a frozen function space,
  start time, horizon, clock, normalization, repetition law, and same-object
  trace theorem.
