# The exact-U_c first-return map is not uniformly expanding

## Status

`PROVED_OBSTRUCTION`

Source: `CLUE-A1-004` / `P4-LOGISTIC-UC-FIRST-RETURN-SUPPORT`

## Statement

Let

\[
f(x)=1-U_cx^2,
\qquad
\rho=U_c-1,
\qquad
L=[-\rho,0),
\]

and let

\[
R(x)=f^{\tau_L(x)}(x)
\]

be the first-return map to $L$ on the physical invariant core. For every
return branch

\[
C_{2n}=\{x\in L:\tau_L(x)=2n\},
\]

one has

\[
\boxed{
\inf_{x\in C_{2n}} |R'(x)|=0.
}
\]

In particular, there is no constant $\lambda>1$ for which

\[
|R'(x)|\geq\lambda
\]

throughout the union of the natural open first-return branches. For any named
full-support physical acip, the subintervals where $|R'|<1$ also have positive
measure. The ordinary piecewise-uniformly-expanding `BV` argument asserted in
legacy Paper 2 therefore does not apply to this map.

## Proof

On the first branch

\[
C_2=(-r_1,0),
\]

the return map is $R=f^2$. Direct expansion gives

\[
f^2(x)=-\rho+2U_c^2x^2-U_c^3x^4
\]

and

\[
(f^2)'(x)=4U_c^2x f(x).
\]

Therefore

\[
\lim_{x\uparrow0}|(f^2)'(x)|=0,
\]

which already rules out uniform expansion. The explicit interior point

\[
x=-0.01\in C_2
\]

gives

\[
|(f^2)'(-0.01)|
\approx0.0953043164<1.
\]

The failure occurs on every higher branch as well. With the endpoint sequence
from the exact support theorem,

\[
C_{2n}=(-r_n,-r_{n-1}]
\quad(n\geq2),
\]

the right endpoint satisfies

\[
(f^2)^{n-1}(-r_{n-1})=0.
\]

Thus the derivative of $(f^2)^n=f^{2n}$ vanishes at that endpoint and tends
to zero along branch-interior points approaching it. Hence every branch has
derivative infimum zero. ∎

## Inverse-Jacobian singularity

Near $x=0$,

\[
y+\rho
=2U_c^2x^2-U_c^3x^4
\sim2U_c^2x^2.
\]

Consequently the inverse Jacobian on the first branch obeys

\[
\left|\frac{dx}{dy}\right|
\sim
\frac{1}{2\sqrt2\,U_c}
(y+\rho)^{-1/2}
\qquad(y\downarrow-\rho).
\]

This square-root singularity has unbounded variation at the image endpoint.
In particular, the unweighted Perron--Frobenius operator for the unaccelerated
first-return map does not map the constant function into ordinary `BV(L)` in
the manner required by the legacy proof.

## Prior-work correction

Legacy Paper 2 asserted that the first-return branches avoid a fixed
neighborhood of the critical point and hence satisfy a uniform Mañé expansion
bound. The exact branch endpoints show the opposite: every branch accumulates
on a preimage of the critical point, and the first branch accumulates directly
at the critical point itself.

Therefore the following downstream claims are not presently established by
the legacy Paper-2 argument:

- the stated ordinary-`BV` Lasota--Yorke inequality for this induced map;
- the claimed ordinary-`BV` spectral gap derived from that inequality;
- the resulting proof of geometric convergence of the branch probabilities;
- the stated asymptotic even-gap mass theorem insofar as it relies on those
  spectral lemmas.

This correction does not refute existence of the physical acip, the exact
even topological support on the invariant core, or the empirical gap-mass
ratio. It refutes the specific unaccelerated uniform-expansion proof.

## Scope and reopening condition

The obstruction applies to the first-return map to the full negative event
interval $L=[-\rho,0)$ with its natural branches. It does not rule out:

- a further accelerated inducing scheme whose branches avoid critical
  preimages;
- a weighted-BV, cusp-adapted, anisotropic, or other singularity-compatible
  function space;
- a direct analysis of a rigorously specified physical density.

Reopening requires one explicitly frozen replacement: its inducing domain,
return convention, branch endpoints, function space, norm, distortion bounds,
and operator action on the square-root singularity must all be proved before a
spectral-gap or Fredholm claim is restored.
