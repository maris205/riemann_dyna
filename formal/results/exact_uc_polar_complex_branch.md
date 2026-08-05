# Frozen-radius complex branches for the exact-$U_c$ polar roof

## Claim boundary

This note proves the complex-domain obligation opened by the corrected polar
source lock. At the unchanged radius

\[
\epsilon=\frac1{1000},
\]

the two composite inverse branches exist as single-valued holomorphic maps,
their signed derivatives come from one common nonvanishing function $a$, one
common holomorphic $\Log(a)$ exists, and all four target/source branch pairs
map compactly into the frozen source stadiums.

This result does **not** define the target-copy or multiplicity rule for an
orbit that hits the doubled partition point. It does not prove nuclearity, a
Fredholm determinant, a trace formula, a completed-$\xi$ divisor,
quantization, Route B, the Hilbert--Pólya conjecture, or RH.

## 1. Frozen object and one complex stadium

Let $u=U_c$ be the unique real root of

\[
P(u)=u^3-2u^2+2u-2,
\qquad
\rho=u-1,
\]

and write

\[
I_L=[-\pi/2,0],
\qquad
I_R=[0,\pi/2],
\qquad
I=I_L\cup I_R.
\]

The frozen complex domains are

\[
U_j=\{z:\operatorname{dist}(z,I_j)<\epsilon\},
\qquad j\in\{L,R\}.
\]

Their union is exactly

\[
U=U_L\cup U_R
=\{z:\operatorname{dist}(z,I)<\epsilon\}.
\]

Thus $U$ is the Minkowski sum of a real interval and an open disk. In
particular, it is convex and simply connected. This observation is important:
the two branch components will be restrictions of objects first constructed
on the single domain $U$, rather than independently chosen germs.

The reflected polynomial map is

\[
S(x)=\rho-2u^2x^2+u^3x^4.
\]

The exact identities inherited from the real theorem are

\[
u\rho^2=1-\rho,
\qquad
u^3\rho=2,
\qquad
1+S(x)=u(1-ux^2)^2.
\]

## 2. One holomorphic $t$, $a$, and logarithm

Put

\[
g(z)=\frac{1+\rho\sin z}{u}.
\]

For $z\in\overline U$, one has $|\operatorname{Im}z|\leq\epsilon$ and

\[
\operatorname{Re}(\sin z)
=\sin(\operatorname{Re}z)\cosh(\operatorname{Im}z)
\geq-\cosh\epsilon.
\]

Consequently

\[
\operatorname{Re}g(z)
\geq B
:=\frac{1-\rho\cosh\epsilon}{u}
>0.29559>0.
\]

The strict inequality is certified with the 100-digit root enclosure for
$U_c$. It also shows that a neighborhood of the compact set $\overline U$ is
mapped into the open right half-plane. Hence the principal square root

\[
t(z)=\sqrt{g(z)}
\]

is holomorphic on such a neighborhood and has $\operatorname{Re}t(z)>0$.
The functions $t$, $1+t$, and $\rho+t$ therefore all take values in the open
right half-plane. Define, using the principal logarithm separately on each of
these three right-half-plane functions,

\[
\ell(z)
=-\log4
+\frac12\Log(1+t(z))
+\frac12\Log(\rho+t(z))
-\Log t(z),
\]

and

\[
a(z)=e^{\ell(z)}
=\frac{\sqrt{1+t(z)}\sqrt{\rho+t(z)}}{4t(z)}.
\]

This uses separate principal square roots; no principal square root of an
uncontrolled product is being assumed. The function $a$ is holomorphic and
nonzero on a neighborhood of $\overline U$, and $\ell$ is one explicit
single-valued holomorphic logarithm of $a$.

On the real interval, $t\in[\rho,1]$ and $a$ is positive. Moreover the real
function

\[
a_0(t)=\frac{\sqrt{(1+t)(\rho+t)}}{4t}
\]

has

\[
\frac{d}{dt}\log a_0(t)
=-\frac{ut+2\rho}{2t(1+t)(\rho+t)}<0.
\]

Its maximum is therefore

\[
a_0(\rho)=\frac{u^2}{4}<1,
\]

where the displayed equality uses $u^3\rho=2$. Hence $\ell=\log a<0$ on
$I$, and the real roof is $\tau=-\ell>0$ on inverse images.

## 3. Composite inverse branches without scalar endpoint branches

The right-half-plane bound is strict on the compact set $\overline U$.
Therefore some slightly larger convex stadium is still contained in the
holomorphy domain of $t$, $a$, and $\ell$. This auxiliary neighborhood is
used only to justify extension to $\overline U$; it does not change the
frozen radius $\epsilon$. On that neighborhood define, and then restrict to
$U$,

\[
\phi_R(z)=-\int_{\pi/2}^{z}a(w)\,dw,
\qquad
\phi_L(z)=+\int_{\pi/2}^{z}a(w)\,dw.
\]

The integrals are path independent. They give

\[
\phi_L'=+a,
\qquad
\phi_R'=-a,
\qquad
\phi_L=-\phi_R.
\]

On the open real target interval, the previously proved real inverse formulas
have these derivatives and the same endpoint value
$\phi_L(\pi/2)=\phi_R(\pi/2)=0$. Thus the primitive-defined functions agree
with the real composite inverse branches. This is the promised endpoint
continuation: no separate holomorphic `asin` through $1$, and no separate
square root through $0$, is required.

Both sides of

\[
S\!\left(\rho\sin(\phi_\sigma(z))\right)=\rho\sin z
\]

are holomorphic on $U$ and agree on the real interval. The identity theorem
therefore proves this $q$-level inverse identity throughout $U$ for
$\sigma=L,R$. It is the locked coordinate identity corresponding to the real
inverse relation. No separate holomorphic forward $G$ is asserted on the
endpoint caps, where $q(\theta)=\rho\sin\theta$ itself is not injective.

## 4. Certified complex contraction bound

Fix $z\in\overline U$ and choose $x\in I$ with
$|z-x|\leq\epsilon$. The segment $[x,z]$ stays in $\overline U$. Along it,

\[
|\cos w|^2
=\cos^2(\operatorname{Re}w)+\sinh^2(\operatorname{Im}w)
\leq\cosh^2\epsilon.
\]

Therefore

\[
|g(z)-g(x)|
\leq \Delta
:=\frac{\rho}{u}\epsilon\cosh\epsilon.
\]

Let $t_0=t(x)\in[\rho,1]$ and $m=\sqrt B$. For the principal square root,
$\operatorname{Re}\sqrt w\geq\sqrt{\operatorname{Re}w}$ whenever
$\operatorname{Re}w>0$. Hence

\[
|t(z)-t_0|
=\frac{|g(z)-g(x)|}{|t(z)+t_0|}
\leq\frac{\Delta}{m+\rho}
=:d.
\]

The certified scalar values are

\[
\begin{aligned}
B&=0.2955975664215057\ldots,\\
m&=0.5436888507423209\ldots,\\
\Delta&=0.0003522013048395366\ldots,\\
d&=0.0003238996458205766\ldots<0.000324<\rho.
\end{aligned}
\]

Using $|t-t_0|\leq d$ in the three factors of $a$ gives

\[
\begin{aligned}
|a(z)|
&\leq a_0(t_0)
\frac{
\sqrt{(1+d/(1+t_0))(1+d/(\rho+t_0))}
}{1-d/t_0}\\
&\leq\frac{u^2}{4}
\frac{\sqrt{(1+d/u)(1+d/(2\rho))}}{1-d/\rho}
=:M.
\end{aligned}
\]

The 100-digit Arb certificate proves

\[
\boxed{
M=0.5962503819920866\ldots<0.59626<1.
}
\]

No finite complex grid is used in this bound.

The same perturbation estimate also proves global univalence. Regard $\ell$
as a holomorphic function of $t$. Along the straight segment from
$t_0=t(x)$ to $t=t(z)$, the three denominators in $d\ell/dt$ are bounded
below by $u-d$, $2\rho-d$, and $\rho-d$. Hence

\[
|\ell(z)-\ell(x)|
\leq d\left(
\frac1{2(u-d)}
+\frac1{2(2\rho-d)}
+\frac1{\rho-d}
\right)
=:L.
\]

The Arb certificate gives

\[
L=0.0008500128404207560\ldots<0.000851.
\]

Since $\ell(x)$ is real, $|\operatorname{Im}\ell(z)|<0.000851<\pi/2$.
Thus

\[
\operatorname{Re}a(z)>0
\qquad(z\in U).
\]

For distinct $z_1,z_2\in U$, convexity gives

\[
\frac{\phi_L(z_2)-\phi_L(z_1)}{z_2-z_1}
=\int_0^1 a(z_1+s(z_2-z_1))\,ds.
\]

The integral has positive real part and is nonzero. Hence $\phi_L$ is
injective on $U$, and so is $\phi_R=-\phi_L$. The primitive-defined maps are
therefore genuine globally univalent complex inverse branches, not merely
local analytic continuations.

## 5. All four compact inclusions

Now take $z\in\overline{U_j}$ and choose the nearest real point
$x\in I_j$. The segment $[x,z]$ remains in the convex closed stadium
$\overline{U_j}$. Since $\phi_\sigma(x)\in I_\sigma$,

\[
\begin{aligned}
\operatorname{dist}(\phi_\sigma(z),I_\sigma)
&\leq|\phi_\sigma(z)-\phi_\sigma(x)|\\
&\leq M|z-x|\\
&\leq M\epsilon
<0.00059626.
\end{aligned}
\]

Thus, for all $j,\sigma\in\{L,R\}$,

\[
\boxed{
\phi_\sigma(\overline{U_j})
\subset
\{w:\operatorname{dist}(w,I_\sigma)\leq M\epsilon\}
\Subset U_\sigma.
}
\]

The certified distance from this closed image stadium to the boundary of the
frozen source stadium is at least

\[
\epsilon(1-M)
=0.0004037496180079133\ldots
>0.00040374.
\]

This one estimate proves the `LL`, `LR`, `RL`, and `RR` inclusions without
changing the radius.

## 6. Matching-space corollary and Route-A boundary

For a fixed $s\in\mathbb C$ and
$v=(v_L,v_R)$ in the frozen matching space, define on the single domain $U$

\[
F_s(z)=e^{s\ell(z)}
\left[v_L(\phi_L(z))+v_R(\phi_R(z))\right].
\]

The compact inclusions make both compositions holomorphic and continuous to
the relevant closures. The two proposed output components are simply
$F_s|_{U_L}$ and $F_s|_{U_R}$, so they agree on the whole overlap and in
particular at $0$. Compactness of the closures also gives boundedness for each
fixed $s$.

This is only well-definedness and matching-space invariance of the weighted
composition formula. It is not a nuclearity theorem and does not establish
$\det_{\rm Fr}(I-\mathcal L_s)$.

The reusable Route-A fact is therefore a proved complex-domain structural
prior. The inherited tuple remains

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
```

because the doubled partition-hit trace ledger, nuclearity, determinant,
arithmetic orbit law, global analytic structure, and quantization remain
open.
