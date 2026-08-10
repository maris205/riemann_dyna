# COPRIME-0001: scalar continuation and the (s=1) endpoint barrier

## Scope and convention

This audit keeps the original candidate fixed:

\[
I=\{2,3,\ldots\},\qquad
(L_s)_{mn}=\mathbf 1_{(m,n)=1}(mn)^{-s/2},
\qquad
D_{\rm cop}(s)=\det_F(I-L_s),
\]

with defining domain \(\Re s>1\).  No determinant roots are computed and no
prime or zero table is used.  The result has two parts:

1. a target-free scalar continuation representation on
   \(\Omega=\{\Re s>1/2\}\setminus\{1\}\); and
2. a same-object endpoint obstruction: infinitely many positive real zeros
   of \(D_{\rm cop}\) approach \(s=1\) from the right.

The auxiliary \(\det_2\) formula below is a representation of the scalar
continuation, not an assertion that the original counting-measure \(\ell^2\)
operator remains bounded below its defining half-plane.

## 1. Squarefree Möbius lift

Let \(\mathcal S=\{d\ge1:d\text{ is squarefree}\}\), and define

\[
 V_s(m,d)=\mathbf 1_{d\mid m}m^{-s/2},
 \qquad M(d,d)=\mu(d).
\]

For \(\Re s>1\), the original kernel has the factorization

\[
 L_s=V_s M V_s^{\mathsf T}.
\]

The transpose is the analytic matrix transpose; the formula is not a change
to the frozen symmetric half-roof convention.  Since \(V_s\) is
Hilbert--Schmidt on this half-plane, Sylvester's trace-class determinant
identity gives

\[
 D_{\rm cop}(s)=\det_F(I-C_s),
 \qquad C_s=V_s^{\mathsf T}V_sM.
\]

For \(d,e\in\mathcal S\),

\[
 (V_s^{\mathsf T}V_s)_{de}
 =\sum_{\substack{m\ge2\\[d,e]\mid m}}m^{-s}
 =\zeta(s)[d,e]^{-s}-\delta_{d=e=1}.
\]

Consequently

\[
 C_s=\zeta(s)T_s-P_1,
 \qquad
 (T_s)_{de}=\mu(e)[d,e]^{-s},
 \qquad
 P_1=e_1\otimes e_1.
\]

## 2. Hilbert--Schmidt continuation representation

Put \(H_s(d,e)=[d,e]^{-s}\).  Squarefree factorization gives the exact
Hilbert--Schmidt ledger

\[
 \|H_s\|_{S_2}^2
 =\sum_{d,e\in\mathcal S}[d,e]^{-2\Re s}
 =\prod_p\bigl(1+3p^{-2\Re s}\bigr).
\]

The product converges locally uniformly for \(\Re s>1/2\), so \(T_s=H_sM\)
is a holomorphic \(S_2\)-valued family there.  Therefore

\[
 C_s=\zeta(s)T_s-P_1
\]

is holomorphic as an \(S_2\)-valued family on

\[
 \Omega=\{\Re s>1/2\}\setminus\{1\}.
\]

Define the explicit continuation representation

\[
 \widetilde D(s)=\det_2(I-C_s),
 \qquad s\in\Omega.
\]

On \(\Re s>1\), \(C_s\) is trace class and

\[
 \operatorname{Tr}C_s
 =\zeta(s)\sum_{d\in\mathcal S}\mu(d)d^{-s}-1
 =\zeta(s)\frac1{\zeta(s)}-1=0.
\]

The relation \(\det_2(I-C)=\det_F(I-C)e^{\operatorname{Tr}C}\) therefore
reduces to

\[
 \widetilde D(s)=D_{\rm cop}(s),
 \qquad \Re s>1.
\]

Thus \(\widetilde D\) is a target-free scalar continuation of the original
determinant to every point of the half-plane \(\Re s>1/2\) except the
endpoint \(s=1\).  The auxiliary expression must not be relabeled as the
original bounded \(\ell^2\) operator or mixed with another determinant ledger.

## 3. Endpoint spectral obstruction

To audit the missing point, temporarily add label one:

\[
 (K_s)_{mn}=\mathbf 1_{(m,n)=1}(mn)^{-s/2},
 \qquad m,n\ge1.
\]

For real \(s>1\), \(K_s\) is compact self-adjoint and \(L_s\) is its
codimension-one compression to \(e_1^\perp\).  In the exponent coordinate of
a formal prime \(p\), write \(q=p^{-s}\).  The local compressed kernel is

\[
 (M_p(q))_{ab}=\mathbf 1_{\min(a,b)=0}q^{(a+b)/2},
 \qquad a,b\ge0.
\]

Its nonzero part is two-dimensional and has eigenvalues

\[
 \alpha_p^\pm(s)
 =\frac{1\pm\sqrt{(1+3q)/(1-q)}}2,
 \qquad \alpha_p^+>0>\alpha_p^-.
\]

For any finite set \(P\) of prime coordinates, the principal compression to
the \(P\)-smooth labels has nonzero eigenvalues

\[
 \Lambda_{S,P}(s)
 =\left(\prod_{p\in P}\alpha_p^+(s)\right)
   \prod_{p\in S}\rho_p(s),
 \qquad
 \rho_p=\alpha_p^-/\alpha_p^+,
 \qquad S\subseteq P.
\]

Even-cardinality \(S\) give positive eigenvalues.  The elementary identity

\[
 \frac{1+3q}{1-q}-(1+2q)^2=\frac{4q^3}{1-q}\ge0
\]

implies \(\alpha_p^+(s)\ge1+p^{-s}\) for real \(s>1\).  Euler's product
therefore gives

\[
 \prod_p\alpha_p^+(s)\longrightarrow\infty
 \qquad (s\downarrow1).
\]

Fix \(M\).  Choose \(M+1\) distinct even-cardinality finite sets \(S_j\).
Their finitely many \(|\rho_p(1)|\) are nonzero.  For \(s\) sufficiently
close to one, a finite prime set \(P\) can be chosen so that every one of the
corresponding positive \(P\)-smooth eigenvalues exceeds one.  The min--max
principle and the codimension-one compression then imply

\[
 \lambda_M^+(L_s)>1
 \quad\text{for all sufficiently small }s-1>0.
\]

At the fixed safe point \(s=3\), the trace-class bound from the first audit
gives

\[
 \|L_3\|
 \le \frac{\zeta(3)^2}{\zeta(6)}-1
 <\left(\frac54\right)^2-1
 =\frac9{16}<1,
\]

where \(\zeta(3)<5/4\) follows from the elementary integral bound.  Since
the ordered positive eigenvalues vary continuously in \(s>1\), each fixed
\(M\) produces a point \(s_M\in(1,3)\) with

\[
 \lambda_M^+(L_{s_M})=1,
 \qquad D_{\rm cop}(s_M)=0.
\]

The number of such crossings is unbounded with \(M\).  More sharply, for any
\(\varepsilon>0\), compactness of the fixed operator \(L_{1+\varepsilon}\)
gives \(\lambda_M^+(L_{1+\varepsilon})\to0\) as \(M\to\infty\).  Choosing
\(M\) large first and then moving \(s\) toward one confines a crossing to
\((1,1+\varepsilon)\).  A compact self-adjoint operator has finite
multiplicity at the nonzero eigenvalue one, so the crossings cannot all occur
at finitely many points.  Hence there is a sequence of distinct positive real
zeros

\[
 s_j\downarrow1,
 \qquad D_{\rm cop}(s_j)=0.
\]

If a holomorphic or meromorphic germ through \(s=1\) existed, multiplying by
a finite power of \(s-1\) would produce a holomorphic germ with zeros
accumulating at an interior point.  The identity theorem would force it to be
identically zero, contradicting \(D_{\rm cop}(3)\ne0\).  Therefore

\[
 \boxed{D_{\rm cop}\text{ has no holomorphic or meromorphic continuation
 through }s=1.}
\]

This is a pointwise endpoint obstruction.  The punctured continuation above
does not assert a barrier at every \(1+it\) with \(t\ne0\), and no root
locations have been computed.

## Route-A boundary

The continuation audit updates the analytic tuple to

```text
(A1_WEAK, A2_ANALYTIC_DETERMINANT,
 A3_CONTROLLED_CONTINUATION, A4_FAIL)
```

For the completed-Riemann target, the tuple remains

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL).
```

Established: a target-free punctured scalar continuation representation and a
strict same-object endpoint obstruction at \(s=1\).  Not established: a
prime-orbit law, von-Mangoldt weights, a functional equation, a completed-xi
divisor, natural quantization, Route B, Hilbert--Pólya, or RH.

The scoped audit is `STOP_SCOPED`; any reopening must freeze a new object or a
new regularization convention explicitly.

Reproduction:

```bash
python3 experiments/coprime_0001_scalar_boundary.py \
  --quiet \
  --output artifacts/coprime_0001/scalar_boundary_certificate.json
python3 -m unittest -v tests/test_coprime_0001_scalar_boundary.py
```
