# LOG-0001: order-zero nuclearity and the exact polar Fredholm ledger

## Claim boundary

This note promotes the frozen exact-$U_c$ polar transfer family from a
conditional formula to a genuine holomorphic Fredholm determinant.  It proves
order-zero nuclearity on the full two-component matching space, the exact
all-power based-fixed-point trace formula, entire dependence on the Fredholm
and roof variables, and conjugation symmetry.

It does **not** prove that this determinant has a prime Euler product, the
completed-$\xi$ divisor, a Riemann--von Mangoldt counting law, a functional
equation, or a natural quantization.  No prime table, zero table, $\zeta$ or
$\xi$ evaluation, or Fredholm-zero computation is used.

## 1. Frozen object

Let $u=U_c$ be the unique real root of

\[
u^3-2u^2+2u-2=0,
\qquad \rho=u-1,
\]

and retain the exact polar map and inverse branches proved in the preceding
complex-branch audit.  The outer and proof-only inner stadiums are

\[
U_\sigma=\{z:\operatorname{dist}(z,I_\sigma)<10^{-3}\},
\qquad
V_\sigma=\{z:\operatorname{dist}(z,I_\sigma)<6\cdot10^{-4}\},
\]

for $\sigma\in\{L,R\}$.  The $U_\sigma$ are the unchanged operator domains;
the $V_\sigma$ are used only in a nuclear factorization.  The inherited
certificate gives

\[
\phi_\sigma(\overline U_j)\subset V_\sigma\Subset U_\sigma,
\qquad
\sup_{U_L\cup U_R}|\phi_\sigma'|\le M<0.59626<\frac35
\tag{1}
\]

for every $j,\sigma\in\{L,R\}$.  It also gives one bounded holomorphic germ
$\ell=\operatorname{Log}a$, real on the real intervals, such that

\[
\phi_L'=a,
\qquad
\phi_R'=-a,
\qquad
w_s=e^{s\ell}.
\tag{2}
\]

For a bounded Jordan domain $U$, write

\[
A(U)=\mathcal O(U)\cap C(\overline U),
\qquad
\|f\|_{A(U)}=\sup_{\overline U}|f|.
\]

Define

\[
X=A(U_L)\oplus A(U_R),
\qquad
\|(v_L,v_R)\|_X=\max(\|v_L\|,\|v_R\|),
\]

and

\[
\delta(v)=v_L(0)-v_R(0),
\qquad
B=\ker\delta.
\tag{3}
\]

The ambient transfer family is

\[
(\mathcal L_s v)_j(z)
=e^{s\ell(z)}
 \bigl[v_L(\phi_L(z))+v_R(\phi_R(z))\bigr],
\qquad z\in U_j.
\tag{4}
\]

The determinant clock is the intrinsic roof
$\tau=\log|G'|$; equivalently, a closed inverse word has
$T=-\log|\Phi'|$.  This is not the physical return-label clock.

## 2. Main theorem

**Theorem (full matching-space nuclear Fredholm family).**  For every
$s\in\mathbb C$, the operator $\mathcal L_s$ on $X$ and its restriction
$\mathcal L_{s,B}=\mathcal L_s|_B$ are nuclear of order zero: they are
$p$-nuclear for every $0<p\le1$.  For every such $p$, the map

\[
s\longmapsto\mathcal L_s
\]

is a locally bounded entire map with values in the $p$-nuclear ideal.
Consequently the canonical Grothendieck Fredholm determinant

\[
\Delta(\lambda,s)
=\det_{\mathrm{Fr}}(I-\lambda\mathcal L_{s,B})
\tag{5}
\]

is jointly entire on $\mathbb C^2$, and

\[
D_{\mathrm{pol}}(s)=\Delta(1,s)
\tag{6}
\]

is an entire function.  Moreover,

\[
\Delta(\lambda,\overline s)
=\overline{\Delta(\overline\lambda,s)}.
\tag{7}
\]

For every $n\ge1$,

\[
\operatorname{Tr}_B\mathcal L_{s,B}^n
=\operatorname{Tr}_X\mathcal L_s^n
=\sum_{\omega\in\{L,R\}^n}
\frac{e^{-sT_\omega}}
     {1-\varepsilon_\omega e^{-T_\omega}},
\qquad
\varepsilon_\omega=(-1)^{\#R(\omega)}.
\tag{8}
\]

Here $\omega$ indexes the diagonal block cycles, or equivalently the based
fixed points, and $T_\omega$ is defined in Section 5.  Formula (8) retains the
signed orientation in the denominator.

## 3. Explicit order-zero expansion

Fix $\sigma\in\{L,R\}$ and a Riemann map
$h_\sigma:\mathbb D\to U_\sigma$.  Because
$\overline V_\sigma\Subset U_\sigma$, there is $r_\sigma<1$ such that

\[
\sup_{z\in\overline V_\sigma}
|h_\sigma^{-1}(z)|\le r_\sigma.
\tag{9}
\]

For $f\in A(U_\sigma)$ write

\[
f\circ h_\sigma(\zeta)
=\sum_{m\ge0}\lambda_{\sigma,m}(f)\zeta^m.
\]

Cauchy's estimate on circles inside $\mathbb D$ gives
$\|\lambda_{\sigma,m}\|\le1$.  The restriction

\[
R_\sigma:A(U_\sigma)\longrightarrow A(V_\sigma)
\]

therefore has the uniformly convergent nuclear expansion

\[
R_\sigma
=\sum_{m\ge0}\lambda_{\sigma,m}\otimes
 \left.(h_\sigma^{-1})^m\right|_{V_\sigma}.
\tag{10}
\]

For every $0<p\le1$,

\[
\sum_{m\ge0}\|\lambda_{\sigma,m}\|^p
 \left\|(h_\sigma^{-1})^m\right\|_{A(V_\sigma)}^p
\le\sum_{m\ge0}r_\sigma^{mp}<\infty.
\tag{11}
\]

Thus $R_\sigma$ is nuclear of order zero, not merely compact.

For $j,\sigma\in\{L,R\}$ define the bounded map

\[
Q_{j\sigma}(s):A(V_\sigma)\longrightarrow A(U_j),
\qquad
Q_{j\sigma}(s)g=w_s\,(g\circ\phi_\sigma).
\tag{12}
\]

By (1),

\[
\|Q_{j\sigma}(s)\|
\le\|e^{s\ell}\|_{A(U_j)}.
\]

Every block of (4) is exactly $Q_{j\sigma}(s)R_\sigma$.  The ideal property
of $p$-nuclear operators and the finite $2\times2$ block sum now prove
order-zero nuclearity of $\mathcal L_s$ on $X$.

For $k\ge0$,

\[
\partial_s^k e^{s\ell}=\ell^k e^{s\ell}.
\tag{13}
\]

The function $\ell$ is bounded on the frozen closures.  Hence (10)--(12),
with $e^{s\ell}$ replaced by every derivative in (13), satisfy the same
$\ell^p$ summability uniformly for $s$ in a compact set.  Equivalently, the
Taylor series at every $s_0$ converges locally in each $p$-nuclear
quasi-norm.  This proves the asserted ideal-valued entire dependence without
invoking an undefined ``nuclear-order-zero topology.''

## 4. Matching introduces no trace factor

Let $e=(1,0)\in X$.  Since $\delta(e)=1$,

\[
P_B=I-e\delta,
\qquad
X=B\oplus\mathbb C e
\tag{14}
\]

is a bounded complemented decomposition.  Both components in (4) are
restrictions of the same holomorphic function.  In particular,

\[
(\mathcal L_s v)_L(0)=(\mathcal L_s v)_R(0),
\]

so $\mathcal L_s(X)\subset B$.  Relative to (14),

\[
\mathcal L_s=
\begin{pmatrix}
\mathcal L_{s,B}&b_s\\
0&0
\end{pmatrix}.
\tag{15}
\]

The restriction to $B$ remains order-zero nuclear by the ideal property.
For every $n\ge1$, (15) and the canonical nuclear trace give

\[
\operatorname{Tr}_X\mathcal L_s^n
=\operatorname{Tr}_B\mathcal L_{s,B}^n.
\tag{16}
\]

The two Fredholm determinants agree as well:

\[
\det_X(I-\lambda\mathcal L_s)
=\det_B(I-\lambda\mathcal L_{s,B}).
\tag{17}
\]

For example, (17) follows first near $\lambda=0$ from (16) and the trace-log
identity, then everywhere from entire continuation.  Matching therefore
preserves the ambient source-branch trace; it neither halves it nor doubles it.

## 5. Exact based-fixed-point trace

Fix a word $\omega=(\omega_0,\ldots,\omega_{n-1})$ and use the composition
convention

\[
\Phi_\omega
=\phi_{\omega_0}\circ\phi_{\omega_1}\circ\cdots
 \circ\phi_{\omega_{n-1}}.
\tag{18}
\]

For a diagonal block path $(j_0,j_1,\ldots,j_{n-1})$, use the bijective
reverse-order relabelling

\[
\omega=(j_0,j_{n-1},j_{n-2},\ldots,j_1).
\]

(A based orbit may subsequently be cyclically relabelled.)  With this
convention, $\Phi_\omega$ is exactly the inverse composition generated by the
block product and is a self-map of $U_{\omega_0}$.  The stadium is convex, (1)
gives

\[
\|\Phi_\omega'\|\le M^n<1,
\]

and $\Phi_\omega(\overline U_{\omega_0})$ is compactly contained in
$U_{\omega_0}$.  The contraction theorem supplies one fixed point $p_\omega$.
Iteration from the real branch interval shows that $p_\omega$ is real.

Define

\[
T_\omega=-\log|\Phi_\omega'(p_\omega)|
=\sum_{k=0}^{n-1}\tau(G^k p_\omega)>0.
\tag{19}
\]

Equations (1)--(2) imply

\[
\Phi_\omega'(p_\omega)
=\varepsilon_\omega e^{-T_\omega},
\qquad
W_{\omega,s}(p_\omega)=e^{-sT_\omega},
\tag{20}
\]

where $W_{\omega,s}$ is the product of the $n$ weights along the inverse
cycle.  The standard one-variable nuclear weighted-composition trace formula
on $A(U_{\omega_0})$ is

\[
\operatorname{Tr}C_{\omega,s}
=\frac{W_{\omega,s}(p_\omega)}
       {1-\Phi_\omega'(p_\omega)}.
\tag{21}
\]

Expanding the diagonal blocks of $\mathcal L_s^n$, applying (21), and then
using (16) proves (8).

This is a based-fixed-point ledger.  Distinct cyclic rotations are retained
when they are distinct.  If a primitive orbit has least period $d$ and is
repeated to length $n=rd$, its $d$ based points occur in
$\operatorname{Tr}\mathcal L_s^n$; the factor $1/n$ in

\[
\log\Delta(\lambda,s)
=-\sum_{n\ge1}\frac{\lambda^n}{n}
  \operatorname{Tr}\mathcal L_s^n
\tag{22}
\]

therefore produces the expected $1/r$ repetition coefficient.  Formula (22)
is asserted only near $\lambda=0$; no convergence of this raw logarithmic
series at $\lambda=1$ is needed for (5)--(6).

The partition point $0$ is preperiodic, not periodic.  The only boundary
periodic point is $P=-\pi/2$, and it has one left label.  For the pure-left
word,

\[
\alpha_0=\frac{U_c^2}{4},
\qquad
\frac{e^{-sT_{L^n}}}{1-e^{-T_{L^n}}}
=\frac{\alpha_0^{ns}}{1-\alpha_0^n},
\tag{23}
\]

in agreement with the preceding local theorem.  There is no seam, half, or
doubled-copy correction.

## 6. Fredholm convention and analyticity

For the order-zero nuclear family, $\det_{\mathrm{Fr}}$ in (5) denotes the
canonical Grothendieck determinant

\[
\det_{\mathrm{Fr}}(I-T)
=\sum_{q\ge0}(-1)^q
  \operatorname{Tr}(\wedge^q T).
\tag{24}
\]

It is not a zeta-regularized determinant or a separately glued Euler product.
The standard order-zero nuclear determinant theorem, together with the
locally uniform ideal-valued holomorphy proved in Section 3, makes (24)
locally uniformly convergent and holomorphic in $(\lambda,s)$.  This proves
joint entireness of (5).

All frozen domains, branches, and $\ell$ are invariant under complex
conjugation.  Conjugating (4) sends $\mathcal L_s$ to
$\mathcal L_{\overline s}$.  Applying (24) proves (7).

## 7. Route-A interpretation

For the same frozen holomorphic object, the analytic tuple is

```text
(A1_WEAK, A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL).
```

The $A2$ and $A3$ entries mean only that an actual same-object entire
Fredholm determinant, conjugation symmetry, and an exact trace ledger now
exist.  Relative to the Riemann target, the tuple remains

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL).
```

There is no arithmetic primitive-orbit law, functional equation,
Gamma/trivial-zero ledger, target counting law, growth-order theorem,
completed-$\xi$ divisor, Hilbert space lift, or self-adjoint operator.  Route B
is not authorized.

The next smallest target-free task is to prove an intrinsic growth-order bound
or a high-imaginary-height divisor-count regime for $D_{\mathrm{pol}}$ before
computing or comparing any target zeros.
