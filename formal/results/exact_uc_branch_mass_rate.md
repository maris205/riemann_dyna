# Quantitative physical branch-mass-ratio rate at exact $U_c$

## Status

NUMERICALLY_CERTIFIED.

Source: CLUE-A1-004 / P4-LOGISTIC-UC-BRANCH-MASS-RATE.

The only new computer-assisted gate in this audit is directed Arb interval
evaluation of two explicit derivatives on one complete closed interval. The
certified root bracket, endpoint interval, endpoint-coefficient lower bound,
and cusp remainder are inherited inputs from the cited parent certificates.
Every subsequent rate-constant comparison is exact rational arithmetic. No
prime, zero, fitted weight, Ulam, resolvent, or determinant data enters.

## Theorem

Let $u=U_c$ be the unique real root of

\[
u^3-2u^2+2u-2=0,
\qquad
\rho=u-1,
\]

and let $\mu_{\rm ac}$ be the normalized physical acip of
$f(x)=1-ux^2$ on $[-\rho,1]$. Define the exact physical first-return
endpoints and masses by

\[
r_0=0,
\qquad
r_{n+1}=\psi(r_n),
\qquad
\psi(x)=\sqrt{\frac{1-\sqrt{(1-x)/u}}{u}},
\]

\[
\delta_n=\rho-r_n,
\qquad
M_n=\mu_{\rm ac}(C_{2n}),
\qquad
C_{2n}=(-r_n,-r_{n-1}].
\]

Then, for every $n\geq6$,

\[
\boxed{
\left|
\frac{M_{n+1}}{M_n}-\frac{u^2}{4}
\right|
\leq
\frac{36}{5}\sqrt{\delta_{n-1}}
<
\frac{243}{625}\left(\frac35\right)^{n-6}.
}
\]

Thus the already proved ratio limit has an explicit geometric convergence
rate. This is a rate for adjacent physical branch masses, not an exact
finite-order geometric law.

## Frozen cusp-adapted space

Set $\varepsilon=1/200$. Define the local Banach space

\[
\mathcal X_\varepsilon
=
\left\{
v(t)=c\,t^{-1/2}+b(t):
c\in\mathbb R,\ b\in L^\infty(0,\varepsilon]
\right\}
\]

with norm

\[
\|v\|_{\mathcal X_\varepsilon}
=|c|+\|b\|_\infty.
\]

The decomposition is unique because
$c=\lim_{t\downarrow0}\sqrt t\,v(t)$ whenever $b$ is bounded.
The parent endpoint and sharp-cone theorems put the canonical physical density
in this frozen space:

\[
h(-\rho+t)=C_h t^{-1/2}+b(t),
\]

\[
C_h>\frac{9461}{100000},
\qquad
\|b\|_\infty\leq\frac{61}{100}.
\]

This local cusp norm is the only function-space input below. No spectral gap
or resolvent estimate is inferred from it.

## Proof

### 1. Quantitative endpoint geometry

Write

\[
a(x)=\sqrt{\frac{1-x}{u}},
\qquad
\psi(x)=\sqrt{\frac{1-a(x)}u}.
\]

Direct differentiation gives

\[
\psi'(x)=\frac1{4u^2a(x)\psi(x)}
\]

and

\[
\psi''(x)
=\psi'(x)
\left[
\frac1{2(1-x)}
-\frac1{4u\,a(x)(1-a(x))}
\right].
\]

Using the certified 100-digit root ball for $u$, one directed Arb evaluation
on the complete interval

\[
x\in[\rho-1/200,\rho]
\]

proves

\[
\frac7{20}<\psi'(x)<\frac9{25},
\qquad
0<\psi''(x)<\frac4{25}.
\]

There is no point sampling: the input is one closed real ball containing every
point in the interval.

Set

\[
q=\frac{u^2}{4}
=\frac1{2u\rho},
\qquad
\lambda=q^2=\psi'(\rho).
\]

The same root ball gives

\[
\frac{59}{100}<q<\frac35.
\]

For $n\geq1$, put

\[
s_n=\sqrt{\delta_n},
\qquad
q_n=\frac{s_n}{s_{n-1}},
\qquad
A_n=q_n^2=\frac{\delta_n}{\delta_{n-1}}.
\]

Because $\psi(\rho)=\rho$,

\[
A_n
=\frac{\psi(\rho)-\psi(\rho-\delta_{n-1})}{\delta_{n-1}}
\]

is the average of $\psi'$ on
$[\rho-\delta_{n-1},\rho]$. Whenever this interval lies in the frozen cusp
domain,

\[
\frac7{20}<A_n<\frac9{25},
\qquad
\frac{59}{100}<q_n<\frac35.
\]

The bound on $\psi''$ also gives

\[
|A_n-\lambda|
\leq\frac4{25}\delta_{n-1}.
\]

Therefore

\[
|q_n-q|
=\frac{|A_n-\lambda|}{q_n+q}
<
\frac{4/25}{2(59/100)}\delta_{n-1}
=\frac8{59}\delta_{n-1}
<
\frac7{50}\delta_{n-1}.
\]

### 2. The sealed start index

The exact rational endpoint certificate gives

\[
\delta_5
<
\left(\frac{27}{500}\right)^2
<
\frac1{200}.
\]

Hence the preceding bounds apply to every $n\geq6$. They also imply

\[
\delta_n<\frac9{25}\delta_{n-1},
\qquad
s_n<\frac35s_{n-1},
\]

and consequently

\[
s_{n-1}
<
\frac{27}{500}\left(\frac35\right)^{n-6}
\qquad(n\geq6).
\]

### 3. Cusp remainder in each physical mass

Integrating the frozen cusp decomposition over
$[\delta_n,\delta_{n-1})$ gives

\[
M_n
=2C_hs_{n-1}(1-q_n)+E_n,
\]

where

\[
|E_n|
\leq
\frac{61}{100}
s_{n-1}^2(1-q_n^2).
\]

Define the signed relative error $\eta_n$ by

\[
M_n
=2C_hs_{n-1}(1-q_n)(1+\eta_n).
\]

Since the same physical coefficient $C_h$ occurs in every branch,

\[
|\eta_n|
\leq
\frac{61/100}{2C_h}s_{n-1}(1+q_n)
<
\frac{48800}{9461}s_{n-1}
<
\frac{129}{25}s_{n-1}.
\]

At and beyond the sealed start index,

\[
|\eta_n|
<
\frac{129}{25}\frac{27}{500}
=\frac{3483}{12500}
<
\frac7{25}.
\]

In particular, $1+\eta_n>18/25$, so no denominator in the ratio estimate can
vanish. Also

\[
|\eta_{n+1}|
<
\frac{129}{25}s_n
<
\frac{129}{25}\frac35s_{n-1}.
\]

This common-coefficient calculation is stronger than dividing two independent
marginal mass intervals, which would illegally allow $C_h$ to change between
the numerator and denominator.

### 4. The geometric main ratio

The ratio of the two leading cusp integrals is

\[
F(q_n,q_{n+1})
=q_n\frac{1-q_{n+1}}{1-q_n},
\qquad
F(q,q)=q.
\]

On the square $[59/100,3/5]^2$,

\[
\left|\partial_1F\right|
=\frac{1-q_{n+1}}{(1-q_n)^2}
\leq\frac{41}{16},
\]

\[
\left|\partial_2F\right|
=\frac{q_n}{1-q_n}
\leq\frac32,
\qquad
0<F\leq\frac{123}{200}.
\]

The preceding $q_n$ estimate and
$\delta_n\leq(9/25)\delta_{n-1}$ give

\[
|q_n-q|\leq\frac7{50}s_{n-1}^2,
\]

\[
|q_{n+1}-q|
\leq\frac7{50}s_n^2
\leq\frac{63}{1250}s_{n-1}^2.
\]

Thus

\[
|F(q_n,q_{n+1})-q|
\leq
\left(
\frac{41}{16}\frac7{50}
+\frac32\frac{63}{1250}
\right)s_{n-1}^2
=\frac{8687}{20000}s_{n-1}^2
<
\frac{11}{25}s_{n-1}^2.
\]

### 5. Combining geometry and the cusp error

The exact mass ratio is

\[
\frac{M_{n+1}}{M_n}
=
F(q_n,q_{n+1})
\frac{1+\eta_{n+1}}{1+\eta_n}.
\]

The multiplicative correction satisfies

\[
\left|
\frac{1+\eta_{n+1}}{1+\eta_n}-1
\right|
\leq
\frac{|\eta_{n+1}|+|\eta_n|}{1-|\eta_n|}
<
\frac{172}{15}s_{n-1}.
\]

Since $F\leq123/200$,

\[
\left|
\frac{M_{n+1}}{M_n}-F(q_n,q_{n+1})
\right|
<
\frac{1763}{250}s_{n-1}.
\]

Combining this with the geometric error and using
$s_{n-1}<27/500$ yields

\[
\left|\frac{M_{n+1}}{M_n}-q\right|
<
\left(
\frac{1763}{250}
+\frac{11}{25}\frac{27}{500}
\right)s_{n-1}
=\frac{88447}{12500}s_{n-1}
<
\frac{36}{5}s_{n-1}.
\]

Finally,

\[
\frac{36}{5}s_{n-1}
<
\frac{36}{5}\frac{27}{500}
\left(\frac35\right)^{n-6}
=
\frac{243}{625}
\left(\frac35\right)^{n-6}.
\]

This proves both displayed rate bounds. QED.

## Error ledger

- Discretization: none. One directed Arb interval covers the complete local
  derivative domain.
- Truncation: none. The conclusion applies to every branch index $n\geq6$.
- Rounding: Arb uses 100 decimal digits; all rate-combination gates are exact
  Fraction inequalities.
- Normalization: the same full-acip coefficient $C_h$ is retained in adjacent
  masses.
- Iteration stopping: none. No stationary vector or iterative solver enters.
- Resolvent/tail: none. The explicit cusp remainder and analytic endpoint
  recursion control the full tail directly.

## Claim boundary

Established:

- a frozen local cusp-adapted Banach decomposition of the physical density;
- an explicit all-tail rate for adjacent physical branch-mass ratios;
- an explicit geometric upper bound beginning with physical return 12.

Not established:

- an exact finite-$n$ mass formula or a sharp interval for any one ratio;
- the stronger legacy statement in any form not implied by the displayed
  adjacent-ratio estimate;
- an ordinary-BV spectral gap, finite-rank resolvent, or transfer-operator
  determinant;
- an arithmetic primitive-orbit law, analytic completed-xi structure,
  quantization, Route B, Hilbert-Polya, or RH.

The Route-A tuple remains
$(A1_{\rm WEAK},A2_{\rm FAIL},A3_{\rm FAIL},A4_{\rm FAIL})$.
The scoped verdict is GO_WITH_LIMITATIONS and the parent verdict remains
REVISE.
