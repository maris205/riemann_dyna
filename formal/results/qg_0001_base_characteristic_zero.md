# QG-0001 Base Characteristic at Zero

**Status:** proved base-component characteristic theorem
**Candidate:** `QG-0001`
**Subaudit:** `QG-0001-BASE-CHARACTERISTIC-001`
**Active clue:** `CLUE-A4-003`
**Route-A layer:** A2 local prerequisite; the tower determinant remains unopened

## 1. Frozen convention

Let

\[
(\ell_0,\ell_1,\ell_2,\ell_3)
=(1,\sqrt2,\sqrt3,\sqrt5),
\qquad
(\alpha_0,\alpha_1,\alpha_2,\alpha_3)
=\left(0,\frac\pi3,\frac{2\pi}3,0\right).
\]

Edges (e_0,e_1,e_2) run from (L) to (R), and the pendant (e_3) runs
from (L) to the Dirichlet terminal (D). Vertices (L,R) have covariant
Kirchhoff conditions of degrees four and three. This audit concerns only the
base component and the raw wavenumber (k). It does not define an infinite
tower product.

## 2. Entire physical matching matrix

Gauge away the constant magnetic potential on each oriented edge and write

\[
f_e(x)=u_L\cos(kx)+q_e\frac{\sin(kx)}{k},
\qquad
\frac{\sin(k\ell_e)}{k}\bigg|_{k=0}=\ell_e.
\]

Set (s_e=\sin(k\ell_e)) and (c_e=\cos(k\ell_e)). Endpoint matching,
the Dirichlet condition, and both Kirchhoff conditions give a homogeneous
system with columns ((u_L,u_R,q_0,q_1,q_2,q_3)):

\[
\mathcal M(k)=
\begin{pmatrix}
c_0&-e^{-i\alpha_0}&s_0/k&0&0&0\\
c_1&-e^{-i\alpha_1}&0&s_1/k&0&0\\
c_2&-e^{-i\alpha_2}&0&0&s_2/k&0\\
c_3&0&0&0&0&s_3/k\\
0&0&1&1&1&1\\
k\sum_{e=0}^2e^{i\alpha_e}s_e&0&
-e^{i\alpha_0}c_0&-e^{i\alpha_1}c_1&-e^{i\alpha_2}c_2&0
\end{pmatrix}.
\]

Define

\[
\mathcal C_{\rm phys}(k)=\det\mathcal M(k).
\]

Every matrix entry is an even entire function of (k): (c_e), (s_e/k), and
(k s_e) are all even and entire. Hence (\mathcal C_{\rm phys}) is even and
entire. The cosine/sinc basis is a fundamental solution basis at every (k),
including (k=0), so the kernel of (\mathcal M(k)) is exactly the physical
matching space. This formulation neither loses nor inserts eigenvalues when
one individual (s_e) vanishes.

## 3. Exact value at zero

Direct exact evaluation gives

\[
\begin{aligned}
A:=\mathcal C_{\rm phys}(0)
&=\sqrt2+\sqrt3+\sqrt5+\sqrt6+\sqrt{15}+3\sqrt{10}\\
&=\sqrt2+\sqrt3+\sqrt6
+\sqrt5(1+\sqrt3+3\sqrt2)\\
&\approx21.1916384169374950181>0.
\end{aligned}
\]

Thus (k=0) is not a physical eigen-wavenumber. Independently, a zero-form
state would be covariantly constant on every edge. Its value at (D) is zero,
and continuity then forces the state to vanish on the connected graph.

## 4. Bond determinant and the spurious zero

Use the parent directed-bond order

```text
e0+, e1+, e2+, e3+, e0-, e1-, e2-, e3-
```

and propagation convention

\[
P_b(k)=e^{i(k\ell_b+\alpha_b)},
\qquad
U(k)=S P(k),
\qquad
\Delta_{\rm bond}(k)=\det(I_8-U(k)),
\]

with (\alpha_{\bar b}=-\alpha_b). Direct block-determinant and row-reduction
algebra gives the exact same-convention identity

\[
\boxed{
\Delta_{\rm bond}(k)
=-\frac43 k^2e^{ikL_0}\mathcal C_{\rm phys}(k),
}
\qquad
L_0=1+\sqrt2+\sqrt3+\sqrt5.
\]

Equivalently, with (F(k)=k^2\mathcal C_{\rm phys}(k)), the poles in the
cotangent/cosecant representation cancel to the entire expression

\[
\begin{aligned}
F(k)={}&s_3\left[-3s_0s_1s_2
+2\sum_{0\leq i<j\leq2}s_{\ell(i,j)}
\left(c_ic_j-\cos(\alpha_i-\alpha_j)\right)\right]\\
&+c_3\sum_{i=0}^2c_i s_j s_m,
\end{aligned}
\]

where (\ell(i,j)) is the remaining theta-edge index and
(\{i,j,m\}=\{0,1,2\}) in the second sum.

Since (A>0), the bond determinant has exact order two at zero:

\[
\operatorname{ord}_{k=0}\Delta_{\rm bond}=2,
\]

and

\[
\Delta_{\rm bond}(k)
=-\frac43A k^2-\frac{4i}{3}L_0A k^3+O(k^4).
\]

The first nonzero coefficient is

\[
-\frac43A
\approx-28.2555178892499933575.
\]

The double zero is therefore a singularity of the bond plane-wave
parametrization, not a physical zero mode.

## 5. Normalized Taylor ledger

Write

\[
F(k)=A k^2+g_4k^4+O(k^6),
\]

where

\[
g_4=-\frac16\left(
27\sqrt2+25\sqrt3+23\sqrt6+36\sqrt5
+18\sqrt{30}+26\sqrt{15}+45\sqrt{10}
\right).
\]

The normalized physical characteristic is

\[
\boxed{
\chi_0(k)=\frac{\mathcal C_{\rm phys}(k)}{A}
=-\frac{3}{4A}e^{-ikL_0}
\frac{\Delta_{\rm bond}(k)}{k^2}.
}
\]

It is even and entire, with

\[
\chi_0(k)=1+a_2k^2+O(k^4),
\]

\[
\boxed{
a_2=\frac{g_4}{A}
\approx-4.40355970195371342217.
}
\]

If only the proved double zero and scalar coefficient are removed from the
bond determinant, then

\[
\beta(k):=-\frac{3}{4Ak^2}\Delta_{\rm bond}(k)
=e^{ikL_0}\chi_0(k)
=1+iL_0k+O(k^2).
\]

Thus the first nonconstant coefficient of the raw normalized bond factor is
(iL_0). The zero-free counterphase (e^{-ikL_0}) is not optional bookkeeping:
it is precisely what returns the even physical characteristic. For component
(n), exact metric scaling gives (\chi_n(k)=\chi_0(k/n)) and the corresponding
local counterphase is (e^{-ikL_0/n}). This identifies the local genus-one
counterterm but does not yet define or validate an infinite product.

## 6. Claim boundary

Established:

- one entire physical base-component characteristic valid at (k=0) and at
  individual edge-Dirichlet points;
- (\mathcal C_{\rm phys}(0)=A>0), hence no physical zero mode;
- the exact bond/physical identity and the spurious bond-zero order two;
- the exact leading bond coefficient, raw linear phase (iL_0), and dephased
  normalized coefficient (a_2).

Not established:

- convergence or divisor control of a component product;
- a relative, Weierstrass, Fredholm, or zeta-regularized tower determinant;
- an arithmetic orbit law, completed-xi identity, Route B, Hilbert--Polya, or RH.

Reproduction:

```bash
python3 experiments/qg_0001_base_characteristic.py \
  --quiet \
  --output artifacts/qg_0001/base_characteristic_zero.json
python3 -m unittest -v tests/test_qg_0001_base_characteristic.py
```
