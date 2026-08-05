# Exact non-lattice theorem for the intrinsic exact-$U_c$ polar roof

## Claim boundary

This note proves one structural fact about the frozen polar object

\[
G=q^{-1}\circ(-f^2)\circ q,
\qquad
q(\theta)=\rho\sin\theta,
\qquad
\tau(\theta)=\log|G'(\theta)|,
\]

where $u=U_c$ is the unique real root of

\[
P(u)=u^3-2u^2+2u-2,
\qquad
\rho=u-1.
\]

For the sealed primitive words $R$ and $LR$, their full roof periods satisfy

\[
\frac{T_{LR}}{T_R}\notin\mathbb Q.
\]

Consequently the roof $\tau$ is non-lattice. This does **not** prove the
frozen complex inverse branches exist on the entire radius-$1/1000$ stadiums,
does not prove compact inclusion or nuclearity, and does not establish a
Fredholm determinant, a Riemann divisor, quantization, Route B, the
Hilbert--Pólya conjecture, or RH.

## 1. The sealed periodic words

Write the reflected polynomial map in the $x$ coordinate as

\[
S(x)=u-1-2u^2x^2+u^3x^4.
\]

The exact polar theorem proves that $G$ has two full real-analytic branches,
that every inverse branch is strictly contracting, and that

\[
\inf |G'|=\frac4{u^2}>1.
\]

Therefore every periodic word has a unique periodic point. The word $R$ is
the unique fixed point in the open right branch. The word $LR$ is the unique
open-branch primitive two-cycle

\[
\theta_L\in(-\pi/2,0),
\quad
G(\theta_L)=\theta_R\in(0,\pi/2),
\quad
G(\theta_R)=\theta_L.
\]

The word $RL$ is only a cyclic rotation of this same orbit. Neither witness
hits a doubled endpoint or the partition point. Because $q'$ is nonzero at
both interior periodic points, the periodic multipliers of $G$ and $S$ agree.

The branch signs are retained:

\[
\Lambda_R=G'(\theta_R)<0,
\qquad
\Lambda_{LR}=G'(\theta_L)G'(\theta_R)<0.
\]

Define their positive roof multipliers by

\[
\alpha=-\Lambda_R>1,
\qquad
\beta=-\Lambda_{LR}>1.
\]

The full primitive periods are

\[
T_R=\log\alpha,
\qquad
T_{LR}=\log\beta.
\]

In particular, $T_{LR}$ is not divided by the symbolic length two.

## 2. Exact multiplier of the $R$ orbit

Direct factorization in $\mathbb Z[u,x]$ gives

\[
S(x)-x
=(ux^2-x-1)(u^2x^2+ux-u+1).
\]

The open right fixed point is the positive root of the second quadratic,

\[
x_R=\frac{\sqrt{4u-3}-1}{2u}.
\]

Since

\[
S'(x)=-4u^2x(1-ux^2),
\]

the fixed-point equation reduces its positive multiplier magnitude to

\[
\alpha=-S'(x_R)=4(u-1).
\]

Substituting $u=1+\alpha/4$ into $P(u)=0$ gives

\[
A(\alpha)=0,
\qquad
A(z)=z^3+4z^2+16z-64.
\]

Modulo $3$, the cubic $A$ has values $2,2,1$ at $0,1,2$, respectively.
Hence it has no root and is irreducible. Therefore

\[
[\mathbb Q(\alpha):\mathbb Q]=3,
\qquad
N_{\mathbb Q(\alpha)/\mathbb Q}(\alpha)=2^6.
\]

## 3. Exact multiplier polynomial of the $LR$ orbit

Let

\[
D_2(X)=\frac{S(S(X))-X}{S(X)-X}.
\]

The division is exact in $\mathbb Q(u)[X]$ and gives the period-two
dynatomic quotient for the polynomial map $S$. The primitive open-branch
$LR$ orbit is supplied independently by the parent full-branch coding theorem,
not by the quotient alone. Put

\[
M(X)=S'(X)S'(S(X)).
\]

Exact polynomial reduction in
$\mathbb Q[u,X]/(P(u),D_2(X))$ gives

\[
H_u(-M(X))=0,
\]

where

\[
H_u(m)
=m^3+(48-16u^2)m^2+256(1+u^2)m-4096.
\]

For the sealed $LR$ orbit, $-M(x_L)=\beta$, hence

\[
H_u(\beta)=0.
\]

Write

\[
A_0(m)=m^3+48m^2+256m-4096,
\qquad
B_0(m)=-16m^2+256m.
\]

Thus $H_u(m)=A_0(m)+B_0(m)u^2$. The critical polynomial also implies

\[
(u^2)^3-4u^2-4=0.
\]

Consequently every root of $H_u$ satisfies

\[
F(m)=A_0(m)^3-4A_0(m)B_0(m)^2+4B_0(m)^3=0.
\]

Expansion gives the monic degree-nine polynomial

\[
\begin{aligned}
F(m)={}&m^9+144m^8+6656m^7+139264m^6+2621440m^5\\
&-37748736m^4-369098752m^3+2684354560m^2\\
&+12884901888m-68719476736.
\end{aligned}
\]

Its reduction modulo $5$ is

\[
g(m)=m^9-m^8+m^7-m^6-m^4-2m^3-2m-1.
\]

The exact Rabin certificate is

\[
m^{5^9}-m\equiv0\pmod g,
\qquad
\gcd\bigl(g,m^{5^3}-m\bigr)=1.
\]

Since $3$ is the only prime divisor of $9$, this proves $g$ irreducible over
$\mathbb F_5$. Hence $F$ is irreducible over $\mathbb Q$ and is the minimal
polynomial of $\beta$. Therefore

\[
[\mathbb Q(\beta):\mathbb Q]=9,
\qquad
N_{\mathbb Q(\beta)/\mathbb Q}(\beta)=2^{36}.
\]

## 4. Multiplicative independence

Assume for contradiction that the roof-period ratio is rational. For coprime
positive integers $a,b$,

\[
\frac{T_{LR}}{T_R}=\frac ab
\quad\Longrightarrow\quad
\beta^b=\alpha^a.
\]

Let $K=\mathbb Q(\alpha,\beta)$ and $d=[K:\mathbb Q]$. The tower law for
norms gives

\[
N_{K/\mathbb Q}(\alpha)=2^{6d/3}=2^{2d},
\qquad
N_{K/\mathbb Q}(\beta)=2^{36d/9}=2^{4d}.
\]

Taking norms in $\beta^b=\alpha^a$ therefore gives

\[
4bd=2ad,
\qquad
a=2b.
\]

Since $(a,b)=1$, the only possible relation is

\[
\beta=\alpha^2.
\]

This last possibility is excluded in the same exact field. Reduction modulo
$P(u)$ gives

\[
H_u(\alpha^2)
=-8192(u-2)(2u-3).
\]

The polynomial $P$ is strictly increasing on $\mathbb R$, with
$P(3/2)=-1/8<0<P(2)=2$. Hence

\[
\frac32<u<2,
\]

so the displayed value is nonzero. Thus $\beta\ne\alpha^2$, contradicting
the only possible multiplicative relation.

We conclude

\[
\boxed{\frac{T_{LR}}{T_R}\notin\mathbb Q}.
\]

## 5. Non-lattice conclusion and Route-A effect

If a roof is lattice, all primitive periodic sums lie in one discrete group
$h\mathbb Z$. Any two nonzero primitive periods then have rational ratio.
The two sealed periods above have irrational ratio, so the intrinsic polar
roof is non-lattice.

This is a `PROVED` positive structural prior. It removes the unit-lattice
obstruction for this exact roof, but it does not create an arithmetic
prime-orbit law and does not establish the conditional Fredholm determinant.
The Route-A tuple therefore remains

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
```

with scoped verdict `GO_WITH_LIMITATIONS`, parent verdict `REVISE`, and Route
B closed.
