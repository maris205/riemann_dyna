# LOG-0001: Phragmen--Lindelof lower bound for the determinant order

## Claim boundary

This note audits one bounded analytic implication for the already frozen

\[
D_{\rm pol}(s)=\det_{\rm Fr}(I-\mathcal L_s|_B).
\]

The object, clock, normalization, matching space, and determinant convention
are unchanged.  The inherited growth theorem gives classical order at most
two, while the inherited lower-growth theorem gives
\(D_{\rm pol}'(2)>0.0213\).  The present lock asks only whether the uniform
bound on the closed half-plane \(\Re s\ge2\) rules out order below one.

The answer is yes:

\[
\boxed{1\le \operatorname{ord}(D_{\rm pol})\le2.}
\]

The lower inequality is qualitative.  It does not identify the order, the
type, a divisor count, a zero, a functional equation, a completed-
\(\xi\) identity, a quantization, Route B, Hilbert--Pólya, or RH.

## 1. Frozen half-plane bound

Put

\[
\alpha_0=\frac{U_c^2}{4},\qquad
B_2=\frac{-\log(1-2\alpha_0^2)}{1-\alpha_0},qquad
K_2=e^{B_2}.
\tag{1}
\]

The inherited signed trace-log theorem applies uniformly in imaginary height
on every closed sub-half-plane above its threshold.  Since \(2\) is strictly
above that threshold, it gives

\[
|D_{\rm pol}(s)|\le K_2
\qquad (\Re s\ge2).
\tag{2}
\]

This is a bound for the same determinant, not a numerical evaluation of it.
The source lock also inherits that \(D_{\rm pol}\) is entire and that

\[
D_{\rm pol}'(2)>0.0213,
\tag{3}
\]

so the function is nonconstant.

## 2. Half-plane Phragmen--Lindelof lemma

**Lemma.**  Let \(F\) be entire, nonconstant, and of finite classical order.
If \(|F(s)|\le K\) on \(\Re s\ge a\) for some real \(a\), then
\(\operatorname{ord}(F)\ge1\).

**Proof.**  Suppose instead that \(\rho=\operatorname{ord}(F)<1\).  Choose

\[
\rho<\eta<\mu<1.
\tag{4}
\]

By the definition of order, after increasing a constant if necessary,

\[
|F(w)|\le \exp\!\bigl(C(1+|w|)^\eta\bigr)
\qquad (w\in\mathbb C).
\tag{5}
\]

Translate the left half-plane by setting

\[
g(z)=F(a-z),\qquad \Re z>0.
\tag{6}
\]

Translation preserves order, and the boundary values satisfy
\(|g(it)|\le K\).  Use the principal branch of \(z^\mu\) on
\(\Re z>0\).  For \(|\arg z|\le\pi/2\),

\[
\Re(z^\mu)\ge c_\mu |z|^\mu,
\qquad c_\mu=\cos(\mu\pi/2)>0.
\tag{7}
\]

For \(\varepsilon>0\), define

\[
h_\varepsilon(z)=g(z)\exp(-\varepsilon z^\mu).
\tag{8}
\]

On the diameter of a right half-disk, \(|h_\varepsilon|\le K\).  On its
semicircle, (5) and (7) give

\[
\log|h_\varepsilon(z)|
\le C(1+R)^\eta-\varepsilon c_\mu R^\mu\longrightarrow-infty
\qquad(R\to\infty),
\tag{9}
\]
because \(\eta<\mu\).  The maximum principle on the half-disk, with a
vanishing indentation at the origin if desired, yields

\[
|g(z)|\le K\exp\!\bigl(\varepsilon\Re(z^\mu)\bigr).
\tag{10}
\]

Letting \(\varepsilon\downarrow0\) gives \(|g(z)|\le K\) throughout
\(\Re z>0\).  Hence \(|F(s)|\le K\) also on \(\Re s<a\).  Together with
the original bound on \(\Re s\ge a\), this makes \(F\) bounded on the
whole plane.  Liouville's theorem forces it to be constant, a contradiction.
\(\square\)

The strict threshold \(\mu<1\) is essential: the opening angle of a half
plane is \(\pi\), and order one is not excluded.

## 3. Application to LOG-0001

Apply the lemma with \(F=D_{\rm pol}\), \(a=2\), and \(K=K_2\).  The
entire-function theorem and (2) supply its hypotheses, while (3) supplies
nonconstancy.  Therefore

\[
\operatorname{ord}(D_{\rm pol})\ge1.
\tag{11}
\]

Combining (11) with the inherited quadratic upper bound proves

\[
1\le\operatorname{ord}(D_{\rm pol})\le2.
\tag{12}
\]

The example \(F(s)=1+e^{-(s-a)}\) has order one, is bounded on
\(\Re s\ge a\), and tends uniformly to one as \(\Re s\to+\infty\).  Thus
the present hypotheses cannot be sharpened to order strictly larger than
one without new information.

## 4. Route-A interpretation

The theorem adds a reusable global analytic implication but does not alter the
Route-A tuple:

```text
(A1_WEAK, A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)
```

The Riemann-target tuple remains

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL).
```

Route B is not authorized.  The breadth-first pivot is now due: the next
object must be a new explicit recurrent candidate or a reusable obstruction,
not another fixed-point estimate for LOG-0001.

## 5. Strict limitations

Not proved here: exact order, order one versus two, finite/infinite type,
critical-strip zero counts, a \(T\log T\) law, arithmetic orbit weights,
completed-\(\xi\), target-zero comparison, quantization, self-adjointness,
Route B, Hilbert--Pólya, or RH.
