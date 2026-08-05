# Validated sharp polar-cone enclosure at exact $U_c$

## Status

`NUMERICALLY_CERTIFIED` as a scoped strengthening of
`formal/results/exact_uc_acip_cone_enclosure.md`.

Source: `CLUE-A1-004` /
`P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE`.

The certificate uses Arb directed real-ball arithmetic from
`python-flint 0.9.0` with FLINT `3.6.0` at 100 decimal digits. It is a
complete closed-interval cover, not a point-sampling maximum. No prime, zero,
Ulam, or determinant data enters.

## Theorem

Let $u=U_c$, $\rho=u-1$, and let $a(\eta)=|r'(\eta)|$ be the common inverse
branch weight of the polar proof map from the coarse cone theorem. Define

\[
y=x^2=\rho^2 t,
\qquad 0\leq t\leq1.
\]

The exact squared logarithmic distortion is

\[
R(t,u)=D(t,u)^2
=
\frac{u y(\rho^2-y)(u^2y-3u+2)^2}
 {16(1-y)(2-u y)(1-u y)^4}.
\]

For completeness, this formula is not inferred from the interval run. The
parent polar derivative identity gives

\[
M(y):=|G'|
=\frac4{\sqrt u}
\frac{1-u y}{\sqrt{(2-u y)(1-y)}},
\]

and direct logarithmic differentiation gives

\[
\partial_y\log M
=\frac{u^2y-3u+2}
 {2(1-y)(2-u y)(1-u y)}.
\]

Since $a=1/M$ on an inverse branch, while the exact output-angle Jacobian
satisfies

\[
\left|\frac{dy}{d\eta}\right|^2
=\frac{u y(\rho^2-y)(1-y)(2-u y)}
 {4(1-u y)^2},
\]

the chain rule
$|\partial_\eta\log a|^2=
|\partial_y\log M|^2|dy/d\eta|^2$ gives the displayed $R(t,u)$ identically.
Thus the interval program certifies an independently derived analytic
quantity.

Using the 100-digit rational sign bracket for $u$ and a cover of $[0,1]$ by
$2^{18}=262144$ closed intervals, Arb proves

\[
\boxed{0.17013<D:=\sup_\eta|\partial_\eta\log a(\eta)<0.17014.}
\]

The lower inequality is independently witnessed on the sealed interval
$t\in[0.75575,0.75576]$; every cover cell has a strictly positive denominator
and its full Arb enclosure lies below $(0.17014)^2$.

The exact inverse contraction bound from the parent theorem satisfies

\[
\kappa=\sup|r'|=\frac{u^2}{4}<0.595744.
\]

Set

\[
A=\frac{42535}{101064}=0.4208719227420248555\ldots.
\]

Then

\[
0.17014+0.595744 A=A,
\]

so the log-Lipschitz cone $|\partial_\theta\log v|\le A$ is forward
invariant under the inverse-branch Perron--Frobenius operator. The parent RPF
theorem supplies the unique fixed density $w$ in this cone. With
$\int_{-\pi/2}^{\pi/2}w=1$ and the physical normalization ledger
$g_A(0)=w(0)/\rho=2h(0)$, Arb-directed evaluation gives the safe rational
enclosures

\[
\begin{aligned}
0.22460&<w(0)<0.43504,\\
0.41310&<g_A(0)<0.80016,\\
0.20655&<h(0)<0.40008,\\
0.09461&<C_h=\frac{h(0)}{\sqrt2\,u}<0.18327.
\end{aligned}
\]

The endpoint remainder from the parent cone theorem remains valid:

\[
\left|h(-\rho+t)-C_h t^{-1/2}\right|
\leq\frac{61}{100},
\qquad 0<t\leq\frac1{200}.
\]

Integrating it over the exact rational endpoint intervals gives the tightened
safe absolute masses below (the displayed intervals are rounded outward):

\[
\begin{array}{c|c}
\text{return label} & \text{certified mass interval}\\\hline
12 &[0.0029623667412445,\;0.0090289530684826]\\
14 &[0.0020334760261950,\;0.0051059183301683]\\
16 &[0.0013068364718538,\;0.0029454892619841]\\
18 &[0.0008124254452971,\;0.0017206760060806]
\end{array}
\]

## Error ledger

- **Discretization:** the $2^{18}$ closed intervals cover the full distortion
  domain; interval dependency widens the enclosure and omits no point.
- **Truncation:** not used; no operator or orbit truncation enters.
- **Rounding:** Arb directed real balls at 100 decimal digits; safe decimal
  thresholds are checked as strict interval inequalities.
- **Normalization:** $w\to g_A\to h\to C_h$ is explicit and keeps the
  conditional and full measures separate.
- **Iteration stopping:** not used; no stationary-vector iteration enters.
- **Resolvent/tail:** not used; the analytic cone controls the invariant
  density directly.

## Claim boundary

Established:

- a complete target-free interval certificate for the distortion upper bound;
- sharper safe enclosures for $w(0)$, $g_A(0)$, $h(0)$, and $C_h$;
- tighter positive absolute-mass intervals for returns 12, 14, 16, and 18.

Not established:

- a narrow Ulam or finite-rank resolvent enclosure;
- the legacy exponential finite-order remainder;
- an arithmetic primitive-orbit correspondence, any $s$-dependent determinant,
  global analytic completion, quantization, Route B, Hilbert--Pólya, or RH.

The Route-A tuple therefore remains
$(A1_{\rm WEAK},A2_{\rm FAIL},A3_{\rm FAIL},A4_{\rm FAIL})$, with scoped
verdict `GO_WITH_LIMITATIONS` and parent verdict `REVISE`.
