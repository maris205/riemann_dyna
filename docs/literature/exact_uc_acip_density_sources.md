# Exact-$U_c$ acip endpoint-density source audit

## Scope

This note freezes the external results used for the endpoint-density theorem
for

\[
f(x)=1-U_cx^2,
\qquad
U_c^3-2U_c^2+2U_c-2=0.
\]

It does not import a prime table, a Riemann-zero table, a fitted gap weight, or
an $s$-dependent determinant.

## RPF proof input

Yunping Jiang and David Ruelle, “Analyticity of the Susceptibility Function
for Unimodal Markovian Maps of the Interval,” *Nonlinearity* 18 (2005),
2447–2453.

- DOI: `10.1088/0951-7715/18/6/002`
- arXiv: `math/0501161`
- Relevant locations: the opening unnumbered Main Theorem, `Assumption A`,
  the Markovian graph discussion, and `Properties of L`.

For the reflected map $S=-f^2|_{[-\rho,\rho]}$, the critical orbit is finite,
the two full branches give a primitive Markov graph, and the repository proof
establishes strict expansion after the polar coordinate. The branch inverses
extend holomorphically and strictly contract on sufficiently thin complex
neighborhoods, which verifies Assumption A. `Properties of L` then supplies a
simple eigenvalue $1$, a strictly positive density, uniqueness among
absolutely continuous invariant probabilities, and ergodicity. The density is
branchwise analytic and its two values agree at the nonpolar partition point
$0$, hence it is locally Lipschitz there.

## Primary spike source

David Ruelle, “Structure and $f$-Dependence of the A.C.I.M. for a Unimodal
Map $f$ of Misiurewicz Type,” *Communications in Mathematical Physics* 287
(2009), 1039–1070.

- DOI: `10.1007/s00220-008-0637-8`
- arXiv: `0710.2015`
- Relevant result: Theorem 9 and Remark 16(a).

Ruelle proves that the acip density of a nondegenerate Misiurewicz unimodal
map is a continuous background plus one-sided inverse-square-root spikes along
the postcritical orbit. In his notation the leading coefficient at the
$n$-th postcritical image is the density at the critical point multiplied by
the inverse square root of the appropriate critical-orbit derivative.

For the present map the postcritical orbit is

\[
0\mapsto1\mapsto-\rho\mapsto\rho\mapsto\rho,
\qquad \rho=U_c-1,
\]

and $-\rho$ occurs only once. Its leading one-sided spike therefore cannot be
cancelled by another postcritical contribution.

## Corrected independent formula cross-check

Viviane Baladi and Daniel Smania, “Fractional Susceptibility Functions for the
Quadratic Family: Misiurewicz–Thurston Parameters,” *Communications in
Mathematical Physics* 385 (2021), 1957–2007, together with the 2023
supplementary note included in arXiv:2008.01654v4.

- DOI: `10.1007/s00220-021-04015-z`
- arXiv: `2008.01654v4`
- Relevant result: corrected equation (1.1) in the supplementary note.

The supplement states that the cutoffs $w_0,w_1$ in the published equation
(50) were incorrect and replaces that display by equation (1.1). The leading
coefficient $C_k^{(0)}$ used below is unchanged. The repository therefore does
not cite the uncorrected published display as its formula ledger.

The linear change of coordinates $y=U_cx$ sends the repository map to

\[
F(y)=U_c-y^2.
\]

Its postcritical orbit is

\[
c_1=U_c,
\qquad
c_2=-U_c\rho,
\qquad
c_3=U_c\rho,
\qquad
F(c_3)=c_3,
\]

and

\[
|F'(c_3)|=2U_c\rho>1.
\]

Thus this is a Misiurewicz–Thurston parameter with preperiod $3$ and period
$1$. Corrected equation (1.1) gives at $c_2$, from the allowed side,

\[
\varrho(c_2+s)
=\frac{\varrho(0)}{\sqrt{2U_c}}s^{-1/2}+O(1).
\]

Since $h(x)=U_c\varrho(U_cx)$, this becomes

\[
h(-\rho+t)
=\frac{h(0)}{\sqrt2\,U_c}t^{-1/2}+O(1).
\]

## Repository-specific proof route

The formal repository proof does not rely on an unchecked appeal to the
published spike formula. It independently removes the critical cusp from
$T=f^2|_{[-\rho,\rho]}$ by the coordinate $x=\rho\sin\theta$ and verifies
that the resulting two-full-branch Markov map is uniformly expanding with

\[
\inf|G'|=\frac4{U_c^2}=2U_c\rho>1.
\]

The locked Jiang–Ruelle theorem then supplies a unique positive, branchwise
analytic invariant density in the desingularized coordinate, with matching
traces and hence local Lipschitz regularity at the nonpolar point zero.
The exact Perron–Frobenius inverse branches recover the displayed endpoint
coefficient. Ruelle 2009 and Baladi–Smania 2021 are therefore independent
published checks of the same singularity ledger.

## Corrected legacy interpretation

The raw density is not globally of bounded variation: it has
$t^{-1/2}$ postcritical spikes. The statements in the legacy Paper-2 and
Paper-3 sources that call the raw acip density globally `BV` are not the
theorem supplied by Misiurewicz. This correction does not restore the old
ordinary-`BV` spectral-gap proof for the unaccelerated first-return map.

## Claim boundary

The cited results establish the invariant-density structure used here. They
do not establish a Riemann dynamical determinant, a prime-orbit law, a
von-Mangoldt trace formula, a natural quantization, Route B, Hilbert–Pólya, or
the Riemann Hypothesis.
