# Explicit conformal restriction ratios for the LOG-0001 stadium pair

## Scope

This note keeps the exact-\(U_c\) polar map, the matching space, the intrinsic
roof, and the canonical
Fredholm determinant from the preceding LOG-0001 audits unchanged.  It proves
an explicit upper bound for the two normalized Riemann-map restriction ratios
that previously appeared only as unspecified constants \(r_L,r_R<1\).  It
then inserts that bound into the inherited two-stream determinant majorant and
gives completely numerical constants in the global quadratic exponential
envelope.

The calculation is target-free.  It does not evaluate the Fredholm
determinant, search for its roots, or read prime, Riemann-zero, zeta, xi, or
USTC data.  The absolute-value estimates below are convergence and upper-growth
majorants only; they do not replace the exact signed trace identity.

## 1. Frozen domains and normalization

Let

\[
I_L=[-\pi/2,0],\qquad I_R=[0,\pi/2],
\]

and put

\[
R=\frac1{1000},\qquad r_0=\frac3{5000}.
\]

For \(\sigma\in\{L,R\}\), define the unchanged operator stadium and the
proof-only inner stadium by

\[
U_\sigma=\{z:\operatorname{dist}(z,I_\sigma)<R\},
\qquad
V_\sigma=\{z:\operatorname{dist}(z,I_\sigma)<r_0\}.
\tag{1}
\]

Write

\[
c_L=-\frac\pi4,\qquad c_R=\frac\pi4,
\]

and normalize the Riemann maps

\[
h_\sigma:\mathbb D\longrightarrow U_\sigma,
\qquad
h_\sigma(0)=c_\sigma,
\qquad
h_\sigma'(0)>0.
\tag{2}
\]

The restriction ratios are

\[
r_\sigma=
\max_{z\in\overline V_\sigma}|h_\sigma^{-1}(z)|.
\tag{3}
\]

The maximum exists because
\(\overline V_\sigma\Subset U_\sigma\) and \(h_\sigma^{-1}\) is continuous
there.  These ratios are proof constants and do not alter the transfer
operator or its clock.
Translation by \(\pi/2\) maps the left stadium pair to the right stadium pair.
Uniqueness under the normalization (2) gives

\[
h_R(w)=h_L(w)+\frac\pi2,
\qquad r_L=r_R.
\tag{4}
\]

The equality is convenient but is not needed for the common upper bound.

## 2. Hyperbolic path theorem

Use the Poincare metric convention

\[
\lambda_{\mathbb D}(w)=\frac{2}{1-|w|^2},
\qquad
d_{\mathbb D}(0,w)=2\operatorname{artanh}|w|.
\tag{5}
\]

### Theorem 1

Define

\[
D_*=500\pi+\log4
\tag{6}
\]

and

\[
r_*=\tanh\frac{D_*}{2}
=\frac{4e^{500\pi}-1}{4e^{500\pi}+1}.
\tag{7}
\]

Then

\[
r_L=r_R\le r_*<1.
\tag{8}
\]

#### Proof

Fix \(\sigma\) and \(z\in\overline V_\sigma\).  Let \(p\in I_\sigma\)
be the Euclidean projection of \(z\) onto the closed interval.  Then
\(|z-p|\le r_0\).  Join \(c_\sigma\) to \(p\) inside the interval and then
join \(p\) to \(z\) by the straight segment.

For every \(x\in I_\sigma\), the disk \(B(x,R)\) lies in \(U_\sigma\).
Monotonicity of the hyperbolic density therefore gives

\[
\lambda_{U_\sigma}(x)
\le \lambda_{B(x,R)}(x)=\frac2R.
\]

The length of the branch interval is \(L=\pi/2\), and \(c_\sigma\) is its
midpoint, so \(|c_\sigma-p|\le L/2\).  Hence

\[
d_{U_\sigma}(c_\sigma,p)
\le \frac2R\frac L2=\frac LR=500\pi.
\tag{9}
\]

The second segment lies in \(B(p,R)\subset U_\sigma\).  A second use of
domain monotonicity and the exact disk distance gives

\[
d_{U_\sigma}(p,z)
\le 2\operatorname{artanh}\frac{|z-p|}{R}
\le \log\frac{R+r_0}{R-r_0}=\log4.
\tag{10}
\]

The triangle inequality proves

\[
d_{U_\sigma}(c_\sigma,z)\le D_*.
\]

Since \(h_\sigma\) is a hyperbolic isometry, (5) implies

\[
2\operatorname{artanh}|h_\sigma^{-1}(z)|\le D_*.
\]

Taking the maximum over \(\overline V_\sigma\) proves (8).  The exact
formula (7) makes \(r_*<1\) strict. \(\square\)

### Stable small quantities

Directly subtracting a floating-point approximation of \(r_*\) from one is
unsafe.  Put instead

\[
t=e^{-D_*},\qquad
\delta_*=1-r_*=\frac{2t}{1+t},\qquad
\beta_*=-\log r_*=\log\frac{1+t}{1-t}.
\tag{11}
\]

Both \(\delta_*\) and \(\beta_*\) are strictly positive.  A 4096-bit outward
Arb evaluation gives

\[
\delta_*
=3.2418512480136249798375853005287351\ldots\times10^{-683},
\tag{12}
\]

\[
\beta_*
=3.2418512480136249798375853005287351\ldots\times10^{-683}.
\tag{13}
\]

The displayed leading digits agree because both quantities are asymptotic to
\(2e^{-D_*}\); they are not asserted to be exactly equal.

## 3. Explicit two-stream coefficient bound

Retain the same matching-space expansion and write

\[
W(s)\le e^{L_\ell|s|},
\qquad L_\ell=\frac{103}{125}=0.824.
\tag{14}
\]

For one stream, the exact elementary-symmetric identity contains the
denominator

\[
\prod_{h=1}^k(1-r_\sigma^h).
\]

Because \(r_\sigma\le r_*\), every factor is at least \(1-r_*=\delta_*\).
Splitting an order-\(q\) coefficient as \(q=k+(q-k)\) between the two input
streams and using

\[
\frac{k(k-1)}2+
\frac{(q-k)(q-k-1)}2
\ge \frac{q^2}{4}-\frac q2
\tag{15}
\]

therefore gives

\[
e_q(s)
\le(q+1)
\left(\frac{W(s)}{\delta_*}\right)^q
r_*^{q^2/4-q/2}.
\tag{16}
\]

Combining this with the inherited Hadamard principal-minor factor yields the
same determinant coefficients \(a_q(s)\):

\[
|a_q(s)|
\le q^{q/2}(q+1)
\left(\frac{e^{L_\ell|s|}}{\delta_*}\right)^q
\exp\!\left[-\beta_*\left(\frac{q^2}{4}-\frac q2\right)\right].
\tag{17}
\]

No separately glued determinant or ambient four-stream bound is used.

## 4. Fully numerical quadratic envelope

Fix

\[
\theta=\frac1{4096},
\qquad
\alpha_\theta=\frac{\beta_*(1-2\theta)}4,
\tag{18}
\]

and define

\[
b_\theta=
-\log\delta_*+\frac{\beta_*}{2}
+\frac12\left(\log\frac1{\theta\beta_*}-1\right)
+\log2.
\tag{19}
\]

For every integer \(q\ge1\), maximization of
\(\log x-\theta\beta_*x\) gives

\[
\log q\le
\theta\beta_*q+\log\frac1{\theta\beta_*}-1,
\tag{20}
\]

while \(q+1\le2^q\).  Inserting these two inequalities into (17) gives

\[
|a_q(s)|
\le
\exp\left[-\alpha_\theta q^2+
(L_\ell|s|+b_\theta)q\right].
\tag{21}
\]

For \(\alpha>0\) and real \(c\), the shifted Gaussian lattice bound is

\[
\sum_{q\in\mathbb Z}e^{-\alpha(q-c)^2}
\le1+\sqrt{\frac\pi\alpha}.
\tag{22}
\]

One proof first observes by Poisson summation that the shifted sum is maximal
at an integral shift, and then bounds each decreasing tail term by the
integral over the preceding unit interval.  Extending the determinant
majorant from \(q\ge0\) to \(q\in\mathbb Z\) and completing the square now
gives the explicit master bound

\[
|D_{\rm pol}(s)|
\le
\left(1+
\sqrt{\frac{4\pi}{\beta_*(1-2\theta)}}\right)
\exp\left(
\frac{(L_\ell|s|+b_\theta)^2}
{\beta_*(1-2\theta)}
\right).
\tag{23}
\]

Writing

\[
L_\ell|s|+b_\theta
=L_\ell(1+|s|)+(b_\theta-L_\ell)
\]

and applying \((u+v)^2\le2u^2+2v^2\), valid constants are

\[
C_0=
\log\left(1+
\sqrt{\frac{4\pi}{\beta_*(1-2\theta)}}\right)
+\frac{2(b_\theta-L_\ell)^2}
{\beta_*(1-2\theta)},
\tag{24}
\]

\[
C_1=
\frac{2L_\ell^2}{\beta_*(1-2\theta)}.
\tag{25}
\]

The 4096-bit certificate encloses

\[
b_\theta=2361.58624122710446397702901049\ldots,
\]

\[
C_0=3.4399610288626472207036914777\ldots\times10^{689},
\qquad
C_1=4.1908628202839735397728688340\ldots\times10^{682}.
\tag{26}
\]

Consequently the simple rational decimal ceilings

\[
\widehat C_0=3.45\times10^{689},
\qquad
\widehat C_1=4.20\times10^{682}
\tag{27}
\]

are certified sufficient, and the same determinant obeys

\[
\boxed{
|D_{\rm pol}(s)|
\le
\exp\!\left(
\widehat C_0+
\widehat C_1(1+|s|)^2
\right).
}
\tag{28}
\]

The enormous numerical constants reflect the deliberately elementary path
bound through a very long, thin stadium.  They are finite proof constants,
not evidence of numerical instability and not estimates of the true growth
type.

## 5. Route-A effect and claim boundary

This audit replaces an unspecified compact-containment constant by an
explicit target-free certificate and makes the previous quadratic exponential
bound completely numerical.  It does not change the Route-A tuple:

\[
(A1_{\rm WEAK},A2_{\rm ANALYTIC\ DET},
A3_{\rm PARTIAL},A4_{\rm FAIL}).
\]

In particular, the result does **not** prove:

- exact conformal ratios or a sharp conformal modulus;
- exact order two, a lower growth bound, or the true type;
- a \(T\log T\) divisor law or any determinant root;
- a log-prime or von-Mangoldt primitive-orbit law;
- a functional equation, Gamma/trivial-zero ledger, or completed-\(\xi\)
  divisor;
- a natural quantization, Route B, Hilbert--Polya, or RH.

The next smallest same-object question is whether one explicit nonzero
coefficient or signed trace term can yield any theorem-level lower bound on
the maximum modulus without computing roots or using target data.  If that
object cannot be stated with a cancellation-safe lower-bound mechanism, the
task is `NOT_TESTABLE` rather than an invitation to fit determinant values.
