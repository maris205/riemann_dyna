# Exact local boundary trace for the exact-$U_c$ polar branch

## Claim boundary

This note proves the local weighted-composition trace carried by the unique
boundary periodic orbit of the exact-$U_c$ polar Markov map. It does not yet
prove nuclearity of the full two-component family or establish its Fredholm
determinant.

Let

\[
P=-\frac{\pi}{2},
\qquad
\alpha_0=\frac{U_c^2}{4}.
\]

For the left inverse branch and its frozen weight,

\[
T_{s,L}v(z)=e^{s\ell(z)}v(\phi_L(z)),
\]

the local trace is

\[
\boxed{
\operatorname{Tr}T_{s,L}
=\frac{\alpha_0^s}{1-\alpha_0}.
}
\]

For the pure-left word of length $n$,

\[
\boxed{
\operatorname{Tr}_P T_{s,L}^n
=\frac{\alpha_0^{ns}}{1-\alpha_0^n}.
}
\]

There is no half-weight and no doubled-copy factor.

## 1. Exact endpoint data

Write $u=U_c$, $ho=u-1$, and

\[
S(x)=\rho-2u^2x^2+u^3x^4.
\]

Modulo the critical relation

\[
u^3-2u^2+2u-2=0,
\]

one has

\[
S(-\rho)=-\rho,
\qquad
S(\rho)=-\rho,
\qquad
S(0)=\rho.
\]

Therefore the exact boundary graph is

\[
-\frac\pi2\mapsto-\frac\pi2,
\qquad
+\frac\pi2\mapsto-\frac\pi2,
\qquad
0\mapsto+\frac\pi2.
\]

Thus $P=-\pi/2$ is the only boundary periodic point. The partition point and
$+\pi/2$ are preperiodic and contribute no separate boundary cycle.

At target $P$, the common auxiliary variable in the inverse-branch formula is

\[
t(P)=\sqrt{\frac{1-\rho}{u}}=\rho,
\]

where $u\rho^2=1-\rho$. Hence

\[
a(P)^2
=\frac{(1+\rho)(\rho+\rho)}{16\rho^2}
=\frac{u}{8\rho}
=\frac{u^4}{16},
\]

using $u^3\rho=2$. Positivity of the inherited real branch gives

\[
a(P)=\frac{u^2}{4}=\alpha_0.
\]

Since $3/2<u<2$, one has $0<\alpha_0<1$.

The endpoint continuation proved earlier gives

\[
\phi_L(P)=P,
\qquad
\phi_L'(P)=\alpha_0,
\qquad
e^{s\ell(P)}=\alpha_0^s.
\]

Although $P$ is a real interval endpoint, it is an interior point of the open
complex stadium $U_L$. No real-boundary half-trace convention applies.

## 2. Weighted-composition trace lemma

Let $U$ be a bounded Jordan domain, let
$\phi(\overline U)\Subset U$, and let $w$ be holomorphic on a neighborhood of
$\overline U$. Suppose $phi$ has the unique fixed point $z_*$ in $U$.
The weighted composition

\[
Cv=w\,(v\circ\phi)
\]

on the disk algebra $A(U)$ is nuclear of order zero. Its nuclear trace is

\[
\operatorname{Tr}C
=\frac{w(z_*)}{1-\phi'(z_*)}.
\]

For completeness, conjugate by a Riemann map sending $z_*$ to $0$. In disk
coordinates,

\[
\psi(z)=\lambda z+O(z^2),
\qquad
\widetilde w(z)=w_0+O(z).
\]

The matrix of $C$ in the monomial expansion is triangular, and its $k$th
diagonal coefficient is $w_0\lambda^k$. Compact containment gives the nuclear
summability required to take the trace, hence

\[
\sum_{k\ge0}w_0\lambda^k=\frac{w_0}{1-\lambda}.
\]

The radius-$1/1000$ complex theorem supplies precisely the compact containment
and holomorphic weight required for $U=U_L$, $\phi=\phi_L$, and
$w=e^{s\ell}$.

Substitution of the exact endpoint data proves

\[
\operatorname{Tr}T_{s,L}
=\frac{\alpha_0^s}{1-\alpha_0}.
\]

For the $n$th power, the fixed point remains $P$, the derivative is
$\alpha_0^n$, and the product weight is $\alpha_0^{ns}$. This proves the
power formula.

## 3. Why there is no doubled-copy factor

The point $P$ belongs only to the left component. The right inverse branch at
target $P$ lands at $+\pi/2$ and is not a diagonal fixed germ. The doubled
partition labels $0_L,0_R$ are irrelevant to this local orbit because the
fixed cycle never visits $0$.

The matching-space condition also introduces no half-weight. If a later
theorem proves the full operator nuclear on an ambient direct sum $X$ and its
range lies in the matching subspace $B$, then in a decomposition
$X=B\oplus\mathbb C e$ it has block form

\[
\begin{pmatrix}L_B&b\\0&0\end{pmatrix}.
\]

Trace additivity gives

\[
\operatorname{Tr}_X L^n=\operatorname{Tr}_B L_B^n.
\]

This equality preserves rather than halves the source-branch cyclic trace.

## 4. Reproducible certificate

The target-free certificate verifies the exact endpoint identities,
$\alpha_0=U_c^2/4\in(0,1)$, and Taylor partial traces at

```text
s = 0, 1/2, 1, 2+i
n = 1, 2, 3, 4
N = 4, 8, 16, 32, 64.
```

Every partial trace satisfies the exact tail identity

\[
\frac{\alpha_0^{ns}}{1-\alpha_0^n}
-\sum_{k=0}^{N}\alpha_0^{ns}(\alpha_0^n)^k
=\frac{\alpha_0^{ns}(\alpha_0^n)^{N+1}}{1-\alpha_0^n}.
\]

No arithmetic target data enters.

## 5. Route-A boundary

This closes the local boundary-trace obligation but not A2. The inherited
Route-A tuple remains

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
```

The next smallest task is the full two-component nuclearity theorem on the
frozen matching space. Only after that theorem may the conditional notation
$\det_{\rm Fr}(I-\mathcal L_s)$ be promoted to an actual Fredholm determinant.
