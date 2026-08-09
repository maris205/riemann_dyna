# LOG-0001: a cancellation-safe derivative and lower-growth certificate

## Claim boundary

This note proves a lower bound for the maximum modulus of the same frozen
Fredholm determinant

\[
D_{\rm pol}(s)=\det_{\rm Fr}(I-\mathcal L_{s,B})
\]

constructed in the preceding LOG-0001 audits.  At the already certified safe
real point \(s=2\), the exact signed trace logarithm gives

\[
D_{\rm pol}'(2)\ge c_2>0.0213,
\]

and hence, with

\[
M_D(R)=\max_{|s|\le R}|D_{\rm pol}(s)|,
\]

\[
M_D(R)>0.0213(R-2)\quad(R>2),
\qquad
M_D(R)>0.01065R\quad(R\ge4).
\]

The proof preserves every signed denominator in the same all-power trace
ledger.  It does not substitute an auxiliary Fredholm coefficient, a
truncated determinant, or a separately majorized determinant.

The result proves that \(D_{\rm pol}\) is nonconstant and transcendental
entire.  It does **not** prove positive or exact entire-function order, an
exponential lower bound, a zero-count lower bound, a \(T\log T\) divisor law,
a functional equation, a completed-\(\xi\) identity, quantization, Route B,
Hilbert--P\'olya, or RH.

## 1. Frozen determinant and safe half-plane

Let \(U_c\) be the unique real root of

\[
u^3-2u^2+2u-2=0,
\]

and put

\[
\alpha_0=\frac{U_c^2}{4},
\qquad
\tau_*=-\log\alpha_0=\log\frac4{U_c^2}.
\tag{1}
\]

The source lock keeps the same exact two-full-branch polar map, intrinsic roof
\(\tau=\log|G'|\), radius-\(1/1000\) operator stadiums, matching space

\[
B=\ker[v_L(0)-v_R(0)],
\]

and canonical determinant.  No clock, normalization, branch sign, or
determinant convention changes.

The parent growth theorem proved that, whenever

\[
\Re s>\sigma_*:=\frac{\log2}{-\log\alpha_0},
\tag{2}
\]

the actual \(\lambda=1\) trace logarithm converges absolutely and equals the
same determinant:

\[
D_{\rm pol}(s)
=\exp\!\left(
-\sum_{n\ge1}\frac1n
 \sum_{\omega\in\{L,R\}^n}
 \frac{e^{-sT_\omega}}
      {1-\varepsilon_\omega e^{-T_\omega}}
\right),
\qquad
\varepsilon_\omega=(-1)^{\#R(\omega)}.
\tag{3}
\]

For real \(\sigma>\sigma_*\), define

\[
B(\sigma)
=\frac{-\log(1-2\alpha_0^\sigma)}{1-\alpha_0}.
\tag{4}
\]

The same theorem gives

\[
0<D_{\rm pol}(\sigma),
\qquad
D_{\rm pol}(\sigma)\ge e^{-B(\sigma)}.
\tag{5}
\]

The point \(\sigma=2\) lies strictly in (2), because
\(2\alpha_0^2<1\).

## 2. Differentiating the complete signed ledger

The logarithm in (3) may be differentiated locally uniformly throughout the
half-plane (2).  To see this without assuming an upper bound for the roof,
fix a compact set \(K\) in that half-plane.  Choose

\[
\sigma_*<\sigma_1<\inf_{s\in K}\Re s.
\]

If \(a=\inf_K\Re s-\sigma_1>0\), then

\[
T e^{-\Re(s)T}
\le \frac1{ea}e^{-\sigma_1T}
\qquad(T>0,\ s\in K).
\tag{6}
\]

The right-hand side is controlled by the already convergent trace-log
majorant at \(\sigma_1\).  The Weierstrass test therefore justifies termwise
differentiation of (3), giving

\[
\frac{d}{d\sigma}\log D_{\rm pol}(\sigma)
=\sum_{n\ge1}\frac1n
 \sum_{\omega\in\{L,R\}^n}
 \frac{T_\omega e^{-\sigma T_\omega}}
      {1-\varepsilon_\omega e^{-T_\omega}}.
\tag{7}
\]

Because (3) is holomorphic in the half-plane, the displayed real derivative
is the restriction of the ordinary complex derivative of
\(D_{\rm pol}\).

Equation (7) is cancellation-safe on the real axis.  Indeed,
\(T_\omega>0\), while

\[
1-\varepsilon_\omega e^{-T_\omega}
=
\begin{cases}
1-e^{-T_\omega},&\varepsilon_\omega=+1,\\
1+e^{-T_\omega},&\varepsilon_\omega=-1,
\end{cases}
\]

is strictly positive.  Thus every complete-ledger summand in (7) is positive.
No orientation sign has been erased.

The one-letter pure-left word is the already certified boundary orbit.  Its
exact ledger is

\[
T_L=\tau_*,
\qquad
e^{-T_L}=\alpha_0,
\qquad
\varepsilon_L=+1.
\tag{8}
\]

Retaining this one term only after proving positivity of the full remainder
gives

\[
\frac{d}{d\sigma}\log D_{\rm pol}(\sigma)
\ge
\frac{\tau_*\alpha_0^\sigma}{1-\alpha_0}.
\tag{9}
\]

Combining (5) and (9) proves the following theorem.

## 3. Explicit derivative theorem

**Theorem (safe-point derivative lower bound).**  For every real
\(\sigma>\sigma_*\),

\[
D_{\rm pol}'(\sigma)
\ge
e^{-B(\sigma)}
\frac{\tau_*\alpha_0^\sigma}{1-\alpha_0}>0.
\tag{10}
\]

At \(\sigma=2\), put

\[
c_2
:=
(1-2\alpha_0^2)^{1/(1-\alpha_0)}
\frac{(-\log\alpha_0)\alpha_0^2}{1-\alpha_0}.
\tag{11}
\]

Then

\[
D_{\rm pol}'(2)\ge c_2>0.0213.
\tag{12}
\]

The first factor in (11) is exactly \(e^{-B(2)}\); it is not a numerical
value of the Fredholm determinant.  In particular, the theorem does not
evaluate \(D_{\rm pol}(2)\) or any Fredholm zero.

## 4. Maximum-modulus consequence

Let \(R>2\) and set \(r=R-2\).  Cauchy's derivative estimate on the circle
\(|s-2|=r\) gives

\[
|D_{\rm pol}'(2)|
\le \frac1r\max_{|s-2|=r}|D_{\rm pol}(s)|.
\tag{13}
\]

The circle in (13) lies in \(|s|\le R\), so (12) yields

\[
\boxed{M_D(R)>0.0213(R-2)}
\qquad(R>2).
\tag{14}
\]

For \(R\ge4\), \(R-2\ge R/2\), and therefore

\[
\boxed{M_D(R)>0.01065R}.
\tag{15}
\]

More generally, if an entire function \(F\) satisfies
\(|F^{(m)}(s_0)|\ge\eta>0\), then the same argument gives

\[
\max_{|s|\le R}|F(s)|
\ge \frac{\eta}{m!}(R-|s_0|)^m
\qquad(R>|s_0|).
\tag{16}
\]

The derivative in (12) proves that \(D_{\rm pol}\) is nonconstant.  The
parent trace-log theorem also proves

\[
D_{\rm pol}(\sigma)\longrightarrow1
\qquad(\sigma\to+\infty).
\tag{17}
\]

A nonconstant polynomial cannot satisfy (17), hence \(D_{\rm pol}\) is
transcendental entire.  If

\[
D_{\rm pol}(s)=\sum_{m\ge0}a_ms^m,
\]

then infinitely many \(a_m\) are nonzero.  For each fixed \(N\ge0\), choose
\(m>N\) with \(a_m\ne0\).  Cauchy's coefficient estimate gives

\[
M_D(R)\ge |a_m|R^m,
\]

and consequently

\[
\frac{M_D(R)}{R^N}\longrightarrow\infty.
\tag{18}
\]

Equation (18) is qualitative and supplies no effective coefficient sequence,
positive order, exponential lower bound, or zero-count lower bound.

## 5. Certified scalar ledger

The companion program uses the inherited 100-decimal-digit rational bracket
for \(U_c\) and 1024-bit outward Arb working precision.  The resulting
\(c_2\) interval has 327 relative accuracy bits; this is not a claim of 300
correct decimal digits.  It certifies

\[
\begin{aligned}
\alpha_0
&=0.5957439419765593735306771341137586\ldots,\\
B(2)
&=3.060584137709954924895913061954579\ldots,\\
e^{-B(2)}
&=0.04686031434695642308253249627898457\ldots,\\
\frac{\tau_*\alpha_0^2}{1-\alpha_0}
&=0.4547218439897233929513721764983679\ldots,\\
c_2
&=0.02130840854978611545501449299646329\ldots.
\end{aligned}
\tag{19}
\]

All published decimal inequalities use the outward interval endpoints, not
the displayed midpoints.  The certificate also checks the exact polynomial
bracket signs, the frozen python-flint/FLINT versions, source hashes, and
byte-identical reproduction.  It reads no prime, zero, \(\zeta\), \(\xi\),
or USTC data and does not evaluate the Fredholm determinant.

## 6. Route-A interpretation

The result makes a lower-growth statement available for the same analytic
determinant, but it does not change the Route-A levels.  The analytic tuple
remains

```text
(A1_WEAK, A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL),
```

and the Riemann-target tuple remains

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL).
```

Route B is not authorized.  Under the project's breadth-first rule, LOG-0001
should now be parked at this bounded analytic checkpoint.  Its candidate-local
reopening requires a same-object theorem with a realistic chance of changing
a Route-A layer or proving a reusable family obstruction; another isolated
fixed-point derivative bound is not sufficient.
