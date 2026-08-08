# LOG-0001: quadratic Fredholm growth and a zero-free half-plane

## Claim boundary

This note proves a global growth upper bound for the same frozen determinant

\[
D_{\rm pol}(s)=\det_{\rm Fr}(I-\mathcal L_{s,B})
\]

constructed in the preceding nuclearity theorem.  It also proves an explicit
right half-plane in which the trace logarithm converges at the actual
Fredholm value \(\lambda=1\), uniformly in imaginary height.  The conclusions
are:

\[
|D_{\rm pol}(s)|\leq \exp\!\bigl(C_0+C_1(1+|s|)^2\bigr),
\tag{1}
\]

so the classical entire-function order is at most two; the number of zeros in
a disk, and hence in a fixed real strip through height \(T\), is \(O(T^2)\);
and \(D_{\rm pol}\) is zero-free when

\[
\Re s>
\sigma_*:=\frac{\log2}{\log(4/U_c^2)}
=1.3382657903899534\ldots.
\tag{2}
\]

with uniform upper and lower modulus bounds on every closed sub-half-plane
\(\Re s\geq\sigma_0>\sigma_*\).

This is an upper theorem only.  It does **not** prove that the order equals
two, give a lower growth bound, determine the divisor asymptotic in a critical
strip, establish a \(T\log T\) law, or compare a Fredholm zero with a Riemann
zero.  It does not supply a functional equation, completed-\(\xi\) identity,
quantization, Route B result, Hilbert--P\'olya realization, or RH claim.

## 1. Frozen determinant and proof constants

Retain the outer and proof-only inner stadiums

\[
U_\sigma=\{z:\operatorname{dist}(z,I_\sigma)<10^{-3}\},
\qquad
V_\sigma=\{z:\operatorname{dist}(z,I_\sigma)<6\cdot10^{-4}\},
\]

and the matching space

\[
B=\ker[v_L(0)-v_R(0)]
\subset A(U_L)\oplus A(U_R).
\]

The parent theorem proves that

\[
(\mathcal L_s v)_j(z)
=e^{s\ell(z)}
 \left[v_L(\phi_L(z))+v_R(\phi_R(z))\right]
\tag{3}
\]

is nuclear of order zero on \(B\), depends entirely on \(s\) in every
\(p\)-nuclear ideal, and has the canonical determinant in the claim boundary.
The function \(\ell=\operatorname{Log}a\) is the unchanged common logarithm.
The inherited complex certificate gives the convenient numerical envelope

\[
L_\ell:=\|\ell\|_{A(U_L\cup U_R)}<0.824.
\tag{4}
\]

Indeed, on the real interval

\[
\log\frac{\sqrt{2U_c}}4
\leq \ell(x)
\leq \log\frac{U_c^2}4<0,
\]

and the certified variation from a nearest real point is below \(0.000851\).

Normalize Riemann maps \(h_\sigma:\mathbb D\to U_\sigma\) by

\[
h_L(0)=-\frac\pi4,
\qquad
h_R(0)=\frac\pi4,
\qquad
h_\sigma'(0)>0.
\]

Carath\'eodory extension and \(\overline V_\sigma\Subset U_\sigma\) give

\[
r_\sigma:=
\max_{z\in\overline V_\sigma}|h_\sigma^{-1}(z)|<1,
\qquad
r:=\max(r_L,r_R)<1,
\qquad
\beta:=-\log r>0.
\tag{5}
\]

These conformal quantities are fixed proof constants.  They do not alter the
operator, roof, clock, normalization, or determinant.

## 2. Two geometric rank-one streams on the matching space

For \(f\in A(U_\sigma)\), write

\[
f\circ h_\sigma(\zeta)
=\sum_{m\geq0}\lambda_{\sigma,m}(f)\zeta^m,
\qquad
\|\lambda_{\sigma,m}\|\leq1.
\tag{6}
\]

For \(v=(v_L,v_R)\in B\), define

\[
u_{\sigma,m}(v)=\lambda_{\sigma,m}(v_\sigma).
\]

Define the \(B\)-valued vector \(x_{\sigma,m}(s)\) by its two components,

\[
\bigl(x_{\sigma,m}(s)\bigr)_j(z)
=e^{s\ell(z)}
 \bigl(h_\sigma^{-1}(\phi_\sigma(z))\bigr)^m,
\qquad z\in U_j.
\tag{7}
\]

The two components in (7) are restrictions of one holomorphic function, so
\(x_{\sigma,m}(s)\in B\).  The full operator has the two-stream expansion

\[
\mathcal L_{s,B}
=\sum_{\sigma\in\{L,R\}}\sum_{m\geq0}
 x_{\sigma,m}(s)\otimes u_{\sigma,m}.
\tag{8}
\]

Put

\[
W(s)=\max_{j\in\{L,R\}}\|e^{s\ell}\|_{A(U_j)}.
\]

Then

\[
W(s)\leq e^{L_\ell|s|},
\qquad
\|u_{\sigma,m}\|\leq1,
\qquad
\|x_{\sigma,m}(s)\|_B\leq W(s)r_\sigma^m.
\tag{9}
\]

It matters that (8) has two streams, one for each **input** branch.  Splitting
the two output components into four ambient blocks gives a valid weaker
majorant, but an individual output-supported vector need not lie in \(B\).

## 3. A determinant-coefficient majorant

Truncate (8) at a finite Taylor index and write the resulting finite-rank
operator as \(T=X\Phi\).  Sylvester's identity gives

\[
\det_B(I-T)=\det_{\mathbb C^N}(I-\Phi X).
\]

For a subset \(I\) of \(q\) rank-one terms, the corresponding principal
minor is the determinant of

\[
\bigl[u_i(x_j)\bigr]_{i,j\in I}.
\]

After factoring \(\|u_i\|\) from row \(i\) and \(\|x_j\|\) from column
\(j\), every remaining entry has modulus at most one.  Hadamard's inequality
therefore gives

\[
\left|\det\bigl[u_i(x_j)\bigr]_{i,j\in I}\right|
\leq q^{q/2}\prod_{i\in I}\|u_i\|\|x_i\|.
\tag{10}
\]

Let \(e_q\) denote the \(q\)-th elementary symmetric sum of the two geometric
sequences

\[
\{W(s)r_L^m:m\geq0\}
\quad\hbox{and}\quad
\{W(s)r_R^m:m\geq0\}.
\]

For one sequence, the elementary \(q\)-binomial identity is

\[
\sum_{0\leq m_1<\cdots<m_k}
r^{m_1+\cdots+m_k}
=\frac{r^{k(k-1)/2}}{\prod_{h=1}^k(1-r^h)}.
\tag{11}
\]

With

\[
C_r:=\prod_{h\geq1}(1-r^h)^{-1}<\infty,
\]

split \(q=k+(q-k)\) between the two streams.  Since

\[
\frac{k(k-1)}2+\frac{(q-k)(q-k-1)}2
\geq\frac{q^2}4-\frac q2,
\tag{12}
\]

one obtains

\[
e_q
\leq C_r^2(q+1)W(s)^q
r^{q^2/4-q/2}.
\tag{13}
\]

Combining (10) and (13) gives, for every finite truncation,

\[
|\det_B(I-T)|
\leq
1+C_r^2\sum_{q\geq1}
q^{q/2}(q+1)W(s)^q r^{q^2/4-q/2}.
\tag{14}
\]

Choose any \(p<2/3\).  The Taylor truncations converge to
\(\mathcal L_{s,B}\) in the \(p\)-nuclear quasi-norm, locally uniformly in
\(s\).  Continuity of the canonical Grothendieck determinant in that ideal
passes (14) to the same determinant \(D_{\rm pol}\).  No new determinant
convention is introduced.

## 4. Quadratic exponential growth

The series on the right of (14) converges for every \(s\).  To make its
growth explicit, insert \(W(s)\leq e^{L_\ell|s|}\) and write
\(\beta=-\log r\).  The logarithm of its \(q\)-th summand is at most

\[
-\frac\beta4q^2
+\left(L_\ell|s|+\frac\beta2\right)q
+\frac q2\log q+\log(q+1)+O_r(1).
\tag{15}
\]

For fixed \(\beta>0\), the last two terms can be absorbed into
\((\beta/8)q^2+c_\beta q\).  Completing the square in the remaining Gaussian
sum proves that constants \(C_0,C_1<\infty\), depending only on the frozen
stadium pair and \(\ell\), satisfy (1).  Equivalently,

\[
\log M_D(R)=O(R^2),
\qquad
M_D(R)=\max_{|s|\leq R}|D_{\rm pol}(s)|.
\tag{16}
\]

Thus

\[
\operatorname{ord}(D_{\rm pol})
=\limsup_{R\to\infty}
\frac{\log\log M_D(R)}{\log R}
\leq2.
\tag{17}
\]

Equation (17) is not an equality claim.  The present proof does not exclude a
smaller order or a much smaller vertical-strip count.

## 5. Absolute trace logarithm and a zero-free half-plane

Let

\[
\alpha_0=\frac{U_c^2}{4},
\qquad
\tau_*=-\log\alpha_0=\log\frac4{U_c^2}>0.
\tag{18}
\]

The exact real theorem gives \(\tau\geq\tau_*\) at every branch point.  Hence
for every based word \(\omega\) of length \(n\),

\[
T_\omega\geq n\tau_*,
\qquad
e^{-T_\omega}\leq\alpha_0^n.
\tag{19}
\]

Retain the exact signed trace identity

\[
\operatorname{Tr}\mathcal L_s^n
=\sum_{\omega\in\{L,R\}^n}
\frac{e^{-sT_\omega}}
     {1-\varepsilon_\omega e^{-T_\omega}}.
\tag{20}
\]

For \(\sigma=\Re s\geq0\), (19)--(20) imply

\[
|\operatorname{Tr}\mathcal L_s^n|
\leq
\frac{(2\alpha_0^\sigma)^n}{1-\alpha_0^n}.
\tag{21}
\]

The signed denominator in (20) has not been changed in the determinant
ledger; (21) is used only as an absolute convergence majorant.

If

\[
\sigma>\sigma_*:=\frac{\log2}{-\log\alpha_0},
\qquad
q_\sigma:=2\alpha_0^\sigma<1,
\tag{22}
\]

then

\[
\sum_{n\geq1}
\frac{|\operatorname{Tr}\mathcal L_s^n|}{n}
\leq
\sum_{n\geq1}\frac{q_\sigma^n}{n(1-\alpha_0^n)}
\leq
\frac{-\log(1-q_\sigma)}{1-\alpha_0}
=:B(\sigma).
\tag{23}
\]

For fixed \(s\) in this half-plane, the same estimate with
\(q_\sigma\) replaced by \(|\lambda|q_\sigma\) proves convergence on a
\(\lambda\)-disk of radius \(q_\sigma^{-1}>1\).  The trace exponential agrees
with \(\Delta(\lambda,s)\) near \(\lambda=0\); the identity theorem therefore
extends the equality to \(\lambda=1\):

\[
D_{\rm pol}(s)
=\exp\left(-\sum_{n\geq1}
 \frac{\operatorname{Tr}\mathcal L_s^n}{n}\right).
\tag{24}
\]

Consequently

\[
e^{-B(\sigma)}
\leq |D_{\rm pol}(\sigma+it)|
\leq e^{B(\sigma)}
\qquad(t\in\mathbb R),
\tag{25}
\]

and the determinant has no zeros in (2).  On every closed half-plane
\(\Re s\geq\sigma_0>\sigma_*\), the bounds are uniform in imaginary height.
Moreover \(B(\sigma)\to0\), so

\[
D_{\rm pol}(\sigma+it)\longrightarrow1
\]

uniformly in \(t\) as \(\sigma\to+\infty\).

At the sealed diagnostic line \(\sigma=2\),

\[
q_2=0.7098216888035402\ldots,
\qquad
B(2)=3.0605841377099549\ldots.
\tag{26}
\]

These numbers certify a convergence margin; they are not fitted spectral
parameters.

## 6. Divisor upper bounds

Equation (25) gives a nonzero anchor, for example \(D_{\rm pol}(2)\ne0\).
Apply Jensen's formula to \(z\mapsto D_{\rm pol}(2+z)\) on the outer circle
\(|z|=2R\), and use (1) to count the inner disk \(|z|\leq R\).  The number
of zeros, counted with multiplicity, in \(|s-2|\leq R\) satisfies

\[
N_D(2;R)=O(R^2).
\tag{27}
\]

For every fixed bounded real interval \([a,b]\), the rectangle

\[
\{s:a\leq\Re s\leq b,\ |\Im s|\leq T\}
\]

lies in a disk centered at \(2\) of radius \(T+O_{a,b}(1)\).  Therefore its
zero count is

\[
N_D([a,b];T)=O_{a,b}(T^2).
\tag{28}
\]

The upper bound (28) neither proves nor refutes a \(T\log T\) law.  A target
divisor conclusion would require a substantially sharper same-object
asymptotic and a lower bound, neither of which follows from nuclearity or
finite order alone.

## 7. Reusable conclusion

The proof isolates a general mechanism.  A finite number of geometric
rank-one streams whose parameter weights grow like \(e^{O(|s|)}\) produce a
Fredholm determinant with a Gaussian-in-rank coefficient majorant and hence
quadratic exponential growth in \(s\).  Separately, a positive roof lower
bound gives a zero-free half-plane, with uniform modulus bounds on every
closed sub-half-plane, through the exact signed trace ledger.

For LOG-0001 this advances A3, but only within
`A3_PARTIAL_ANALYTIC_STRUCTURE`.  The analytic Route-A tuple remains

```text
(A1_WEAK, A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL),
```

and the Riemann-target tuple remains

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL).
```

The next smallest target-free task is to certify numerical upper bounds for
the normalized conformal restriction ratios \(r_L,r_R\).  That would turn the
existential constant in (1) into a fully numerical quadratic-type bound.  It
would still not authorize determinant-root computation or Route B.
