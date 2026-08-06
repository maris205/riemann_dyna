# TH-0001 exact three-kick Hénon prefilter

Status: `PROVED` within the stated period and symmetry classes.

Route-A boundary:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
ROUTE_A_EXPLORATORY
GO_WITH_LIMITATIONS
```

## 1. Frozen object

Let

\[
F_a(q,p)=(1-aq^2-p,q)
\]

on \((\mathbb R^2,dq\wedge dp)\), and freeze

\[
G=F_{5/2}\circ F_{3/2}\circ F_{1/2}.
\]

Equivalently,

\[
u=1-\frac12q^2-p,
\qquad
v=1-\frac32u^2-q,
\qquad
G(q,p)=\left(1-\frac52v^2-u,v\right).
\]

The candidate clock is one complete application of \(G\). The three
micro-kicks are construction substeps and are not separate primitive periods.
The half-integer ramp is a target-free modeling choice, not a derived
arithmetic constant.

## 2. Exact symplecticity and inverse

For every \(a\),

\[
DF_a(q,p)=
\begin{pmatrix}-2aq&-1\\1&0\end{pmatrix},
\qquad
\det DF_a=1,
\]

and

\[
F_a^{-1}(q,p)=(p,1-ap^2-q).
\]

In dimension two, determinant one is equivalent to preservation of
\(dq\wedge dp\). More strongly, each kick has the type-one generating
function

\[
S_a(q,Q)=qQ-q+\frac a3q^3,
\qquad
p=-\partial_qS_a,
\qquad
P=\partial_QS_a.
\]

Thus \(G\) is an exact-symplectic polynomial automorphism. Its algebraic
dynamical degree is \(2^3=8\), rather than the degree two of a single legacy
Hénon map.

## 3. Time-reversal audit

The parent reversor is

\[
R(q,p)=(p,q),
\qquad
RF_aR=F_a^{-1}.
\]

It is not a reversor of \(G\). At the origin,

\[
RGR(0,0)=\left(-\frac12,-\frac58\right),
\qquad
G^{-1}(0,0)=\left(-\frac12,-\frac18\right).
\]

The reverse schedule \((5/2,3/2,1/2)\) is not a cyclic rotation of
\((1/2,3/2,5/2)\), so no reversor inherited from the common parent swap and a
clock-origin shift exists.

Every affine anti-symplectic involution satisfying \(IGI=G^{-1}\) would, by
comparison of the highest homogeneous terms, have off-diagonal linear part

\[
\begin{pmatrix}0&\lambda\\\lambda^{-1}&0\end{pmatrix}
\]

and would have to satisfy, with first and last kick parameters \(a,c\),

\[
a^2\lambda^5=c^2,
\qquad
a^3\lambda^7=c^3.
\]

These equations imply \(\lambda=1\) and \(a=c\), contradicting
\(1/2\ne5/2\). Hence no affine anti-symplectic involutory reversor exists.
This does not exclude an arbitrary nonlinear or non-polynomial reversor.

## 4. Complete real UPO prefix

For \(n=1,2\), exact lexicographic Gröbner elimination of

\[
G^n(q,p)=(q,p)
\]

over \(\mathbb Q\) gives a triangular basis consisting of one equation linear
in \(p\) and one eliminant \(R_n(q)\). The basis degree shapes are

```text
n=1: (1,7), (0,8)
n=2: (1,63), (0,64)
```

The period-one eliminant is

\[
\begin{aligned}
R_1(q)={}&225q^8-1800q^6+1920q^5+2760q^4\\
&-3840q^3-736q^2+1536q-48.
\end{aligned}
\]

It has exactly four real simple roots. The period-two eliminant has degree 64
and exactly 20 real simple roots. The exact quotient

\[
D_2(q)=R_2(q)/R_1(q)
\]

has degree 56, is square-free, is coprime to \(R_1\), and has exactly 16 real
roots. These roots form eight two-cycles under forward \(G\).

The primitive integer coefficient hashes are

```text
R1  a0ed76ae20ec9a1300785e86109dd145039c50eb44879be7d9e2202a3acbbc7a
R2  eee0ae04452a9ff02da3c2eadbb8bba4b05787e0392978c029b2c131288d2d0a
D2  60dd88608e229e19708948f239bc7e4f8f80f536a3c54a763dbe59ee924c46dc
```

Exact Sturm isolation and outward rational interval propagation of the
six-micro-kick monodromy prove that all 12 primitive real orbits in this prefix
are hyperbolic. The smallest certified margin is

\[
\min_\gamma\bigl(|\operatorname{tr}M_\gamma|-2\bigr)
>1.65120565439421041.
\]

The census is global on \(\mathbb R^2\) for real \(G\)-period at most two:
there is no search box, random seed, or numerical residual filter. Nothing is
claimed about period three or higher.

## 5. Claim boundary

Established:

- one explicit autonomous target-free exact-symplectic candidate;
- failure of the inherited reversor and absence of affine anti-symplectic
  involutory reversors;
- non-conjugacy to a single legacy \(F_a\), by degree and by four versus at
  most two real fixed points;
- a complete signed real primitive-orbit and monodromy ledger through
  \(G\)-period two.

Not established:

- absence of arbitrary nonlinear reversors;
- any prime-like clock, arithmetic labeling, von-Mangoldt weight, phase law,
  or higher-period completeness;
- a Zeta, reciprocal Zeta, logarithmic derivative, Fredholm determinant, or
  global analytic structure;
- a rigorously defined quantum operator, Route B, Hilbert--Pólya, or RH.

The next bounded task is to freeze the same-order Fourier-integral
quantization on \(L^2(\mathbb R)\), prove normalization and unitarity, and
audit its natural antiunitary symmetry without computing a spectrum.
