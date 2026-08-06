# QG-0001 Same-Operator Relative Fredholm Determinant

**Status:** proved determinant-existence theorem and scoped target obstruction  
**Candidate:** `QG-0001`  
**Subaudit:** `QG-0001-RELATIVE-FREDHOLM-001`  
**Active clue:** `CLUE-A4-003`  
**Route-A layers:** A2/A3 analytic audit; Route B remains closed

## 1. Frozen object and convention

Let \(H_1\) be the positive magnetic Laplacian on the frozen base
lollipop-theta graph. Its edge lengths and L-outward magnetic line integrals
are

\[
(\ell_0,\ell_1,\ell_2,\ell_3)
=(1,\sqrt2,\sqrt3,\sqrt5),
\qquad
(\alpha_0,\alpha_1,\alpha_2,\alpha_3)
=\left(0,\frac\pi3,\frac{2\pi}3,0\right).
\]

The vertices \(L,R\) carry covariant Kirchhoff conditions and the terminal
\(D\) is Dirichlet. Component \(n\) is the exact \(1/n\) metric scaling of
the base component, with the magnetic line integrals fixed. Denote its
magnetic Laplacian by \(H_n\). Metric dilation gives

\[
H_n\simeq n^2H_1.
\]

On the orthogonal direct sum of component spaces, define

\[
\mathcal H=\bigoplus_{n\geq1}\mathcal H_n,
\qquad
H=\bigoplus_{n\geq1}H_n,
\]

with

\[
\operatorname{Dom}(H)=
\left\{u=(u_n):u_n\in\operatorname{Dom}(H_n),\ 
\sum_{n\geq1}\lVert H_nu_n\rVert^2<\infty\right\}.
\]

This audit freezes the relative/Fredholm characteristic

\[
\boxed{
D_H(k)=\det_F(I-k^2H^{-1})
=\det_{\rm rel}(H-k^2,H).
}
\]

It is not the naive primitive-orbit Euler product, the standard direct sum of
bond-scattering blocks, a heat or spectral zeta function, or a completed-xi
determinant.

## 2. Positivity and trace class

The Dirichlet terminal excludes a zero mode, so \(H_1\geq cI\) for some
\(c>0\). Every \(H_n\) is positive and self-adjoint, and the direct-sum
operator above is positive and self-adjoint. Write the base eigenvalues as

\[
0<\lambda_1\leq\lambda_2\leq\cdots,
\qquad \kappa_j=\sqrt{\lambda_j}.
\]

The compact metric-graph Weyl law gives

\[
N_1(K)=\#\{j:\kappa_j\leq K\}
=\frac{L_0}{\pi}K+O(1),
\qquad
L_0=1+\sqrt2+\sqrt3+\sqrt5.
\]

Consequently \(\lambda_j\asymp j^2\) and

\[
\operatorname{Tr}(H_1^{-1})
=\sum_{j\geq1}\lambda_j^{-1}<\infty.
\]

Because \(H_n^{-1}\simeq n^{-2}H_1^{-1}\),

\[
\boxed{
\lVert H^{-1}\rVert_1
=\sum_{n\geq1}\lVert H_n^{-1}\rVert_1
=\zeta(2)\operatorname{Tr}(H_1^{-1})<\infty.
}
\]

Thus \(H^{-1}\) is trace class. More sharply,

\[
H^{-1}\in\mathfrak S_p\quad\Longleftrightarrow\quad p>\frac12,
\]

because the relevant double sum is
\(\sum_{n,j}(n^2\lambda_j)^{-p}\). In contrast,

\[
H^{-1/2}\in\mathfrak S_p\quad\Longleftrightarrow\quad p>1.
\]

This distinction explains why the determinant is genus zero in the variable
\(z=k^2\), while its symmetric canonical product in \(k\) has genus one.

## 3. The normalized base factor is a Fredholm determinant

The preceding base audit constructed the even entire physical characteristic

\[
\chi_0(k)=\frac{\mathcal C_{\rm phys}(k)}{A},
\qquad
A=\mathcal C_{\rm phys}(0)>0,
\qquad
\chi_0(0)=1.
\]

Its nonzero zeros, including spectral multiplicity, are exactly
\(\{\pm\kappa_j\}\). The sinc matching determinant is an even entire
function of finite exponential type and order at most one. Consequently there
is an entire function \(\Phi\) of order at most \(1/2\) such that
\(\chi_0(k)=\Phi(k^2)\). On the other hand, trace class gives

\[
\det_F(I-k^2H_1^{-1})
=\prod_{j\geq1}\left(1-\frac{k^2}{\kappa_j^2}\right),
\]

which is also even, entire of order at most one, equals one at zero, and has
the same divisor. In the \(z=k^2\) variable, \(\Phi(z)\) and
\(\det_F(I-zH_1^{-1})\) are genus-zero canonical products of order at most
\(1/2<1\). Their zero-free quotient must therefore be constant; the value at
zero fixes that constant to one. This growth step is essential: shared zero
locations and evenness alone would not exclude an unproved factor
\(e^{ck^2}\). Therefore

\[
\boxed{
\chi_0(k)=\det_F(I-k^2H_1^{-1}).
}
\]

In particular, if

\[
\chi_0(k)=1+a_2k^2+O(k^4),
\]

then

\[
a_2=-\operatorname{Tr}(H_1^{-1}).
\]

For the frozen graph,

\[
\operatorname{Tr}(H_1^{-1})
=\frac{
27\sqrt2+25\sqrt3+23\sqrt6+36\sqrt5+18\sqrt{30}
+26\sqrt{15}+45\sqrt{10}
}{
6(\sqrt2+\sqrt3+\sqrt5+\sqrt6+\sqrt{15}+3\sqrt{10})
}
\]

\[
=4.40355970195371342217\ldots.
\]

## 4. The same-operator component product

For finite \(N\), orthogonal block multiplicativity gives

\[
\det_F\left(I-k^2\bigoplus_{n=1}^NH_n^{-1}\right)
=\prod_{n=1}^N\det_F(I-k^2H_n^{-1})
=\prod_{n=1}^N\chi_0(k/n).
\]

The finite direct sums converge to \(H^{-1}\) in trace norm. Continuity of
the Fredholm determinant in trace norm therefore proves, locally uniformly
in \(k\),

\[
\boxed{
D_H(k)=\det_F(I-k^2H^{-1})
=\prod_{n\geq1}\chi_0(k/n).
}
\]

There is also a direct normal-convergence proof. Uniformly for \(k\) in a
compact set,

\[
\chi_0(k/n)=1+O(n^{-2}),
\]

and \(\sum_n n^{-2}<\infty\). No cutoff, analytic continuation, or external
regularization is part of the determinant definition.

The first tower coefficient is fixed exactly:

\[
D_H(k)=1-\operatorname{Tr}(H^{-1})k^2+O(k^4),
\]

\[
\boxed{
\operatorname{Tr}(H^{-1})
=\zeta(2)\operatorname{Tr}(H_1^{-1})
=7.24356536914368571711\ldots.
}
\]

## 5. Bond counterphase and genus-one ledger

Let \(\Delta_{{\rm bond},n}(k)\) be the bond determinant of component \(n\)
in the frozen convention. Exact scaling and the base identity give

\[
\Delta_{{\rm bond},n}(k)
=-\frac43\left(\frac{k}{n}\right)^2
e^{ikL_0/n}\mathcal C_{\rm phys}(k/n).
\]

After removing the proved spurious quadratic factor and scalar, define

\[
\beta_n(k)
:=-\frac{3n^2}{4Ak^2}\Delta_{{\rm bond},n}(k)
=e^{ikL_0/n}\chi_0(k/n).
\]

It has the component asymptotic

\[
\beta_n(k)=1+\frac{ikL_0}{n}+O(n^{-2}).
\]

Hence the raw product contains the harmonic phase

\[
\prod_{n=1}^N\beta_n(k)
=e^{ikL_0H_N}\prod_{n=1}^N\chi_0(k/n),
\qquad
H_N=\sum_{n=1}^N\frac1n.
\]

For nonzero real \(k\) away from the divisor of \(D_H\), the second factor
has a nonzero limit while \(e^{ikL_0H_N}\) has no limit. Since
\(H_N=\log N+\gamma+o(1)\), subsequences can be chosen whose unwrapped phases
approach values differing by \(\pi\). Thus the raw bond product diverges.

The forced factorwise genus-one repair is

\[
\boxed{
e^{-ikL_0/n}\beta_n(k)=\chi_0(k/n).
}
\]

The standalone product of counterphases also diverges and must not be split
off. The evenness condition, \(D_H(0)=1\), and the Fredholm convention fix
the possible residual factor \(e^{ick}\) to \(c=0\).

This does not contradict `OBR-012`. That obstruction concerns the ordinary
primitive-orbit product and the direct sum of bond transfer blocks, whose
trace norms tend to eight. Here the inverse-Laplacian block trace norms decay
as \(n^{-2}\).

## 6. Exact divisor and counting obstruction

The determinant zeros are

\[
\boxed{
k=\pm n\kappa_j,
\qquad n,j\geq1,
}
\]

with base multiplicities; coincidences from different pairs \((n,j)\) add.
The origin is not a zero. The positive-root count is

\[
N_H(K)=\sum_{n\leq K/\kappa_1}N_1(K/n).
\]

Using the base Weyl law and the harmonic-sum asymptotic gives

\[
\boxed{
N_H(K)=\frac{L_0}{\pi}K\log K+O(K).
}
\]

The positive Riemann-zero count has leading coefficient \(1/(2\pi)\). The
candidate-to-target ratio is therefore

\[
\boxed{
2L_0=2+2\sqrt2+2\sqrt3+2\sqrt5
=12.764664694883524\ldots\neq1.
}
\]

The raw wavenumber clock and metric normalization are frozen, so rescaling is
not allowed. A zero-free entire prefactor cannot alter a divisor count. Thus
this genuine Fredholm determinant cannot equal completed xi up to a zero-free
factor under the QG-0001 source lock.

The zero exponent of convergence is one. Consequently \(D_H\), viewed as a
function of \(k\), has order one and infinite type; more precisely,

\[
\log D_H(iR)=L_0R\log R+O(R).
\]

Viewed as a function of \(z=k^2\), it has order \(1/2\). This global analytic
ledger is exact, but it is the wrong target ledger.

## 7. Trace expansion is not an orbit formula

Only for \(|k|<\sqrt{\lambda_1(H)}\), the Fredholm logarithm expands as

\[
\log D_H(k)
=-\sum_{r\geq1}\frac{k^{2r}}r\operatorname{Tr}(H^{-r}).
\]

These are inverse spectral moments. No identity has been proved between them
and the frozen primitive directed-bond orbits, their metric periods, or their
signed magnetic weights. The formula must not be relabeled as a
von-Mangoldt-weighted prime-power trace formula.

## 8. Claim boundary

Established:

- \(H^{-1}\) is trace class and defines a genuine same-operator Fredholm
  determinant;
- the normalized base physical characteristic equals the base Fredholm
  determinant;
- the component product converges normally and has the exact operator
  divisor, multiplicities, Taylor coefficient, order, and counting law;
- the factorwise bond counterphase is forced and `OBR-012` remains valid for
  the distinct naive products;
- the fixed QG-0001 divisor has the wrong immutable leading coefficient.

Not established:

- a primitive-orbit trace identity or von-Mangoldt weight law;
- a completed-xi functional equation, Gamma/trivial-zero ledger, or divisor;
- Route B, a Hilbert--Polya realization, or RH.

The fixed QG-0001 target-matching route is therefore `STOP_SCOPED`. A
different graph normalization or tower law would be a new source-locked
candidate, not a repair within this audit.

Reproduction:

```bash
python3 experiments/qg_0001_relative_fredholm.py \
  --quiet \
  --output artifacts/qg_0001/relative_fredholm.json
python3 -m unittest -v tests/test_qg_0001_relative_fredholm.py
```
