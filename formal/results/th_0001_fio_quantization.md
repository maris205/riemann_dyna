# TH-0001 same-order Fourier-integral quantization audit

Status: `PROVED` for the frozen unitary propagator and the audited inherited
antiunitary class. This is an A4 theorem edge, not a Route-B realization.

Route-A update:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)
ROUTE_A_EXPLORATORY
GO_WITH_LIMITATIONS
```

## 1. Frozen operator

Keep the classical kick

\[
F_a(q,p)=(1-aq^2-p,q),
\qquad
V_a(q)=-q+\frac a3q^3,
\]

and its type-I generating function

\[
S_a(q,Q)=qQ+V_a(q)=qQ-q+\frac a3q^3.
\]

Fix the target-free normalization \(\hbar=1\), Lebesgue measure on
\(L^2(\mathbb R,dq)\), and the positive-real Fourier normalization

\[
(\mathcal F_+\psi)(Q)=\frac1{\sqrt{2\pi}}
\int_{\mathbb R}e^{+iqQ}\psi(q)\,dq.
\]

Let

\[
(M_a\psi)(q)=e^{iV_a(q)}\psi(q),
\qquad
U_a=\mathcal F_+M_a.
\]

On the Schwartz core this has the oscillatory kernel

\[
K_a(Q,q)=\frac1{\sqrt{2\pi}}e^{iS_a(q,Q)}.
\]

The same-order superstep is frozen as

\[
U_G=U_{5/2}U_{3/2}U_{1/2}.
\]

No extra \(i\)-prefactor or Maslov branch is inserted. Replacing the positive
real prefactor by \((2\pi i)^{-1/2}\) would only multiply each factor by a
fixed unimodular scalar, but that convention is not part of this audit.

## 2. Exact canonical graph

Since

\[
\partial_qS_a=Q-1+aq^2,
\qquad
\partial_QS_a=q,
\qquad
\partial_{qQ}^2S_a=1,
\]

the generating relations \(p=-\partial_qS_a\), \(P=\partial_QS_a\) give

\[
Q=1-aq^2-p,
\qquad P=q.
\]

Thus the canonical relation of the Fourier-integral factor is exactly the
frozen classical kick, with no coordinate rescaling or fitted phase.

## 3. Unitarity

For real \(a\), \(V_a\) is real, so \(|e^{iV_a(q)}|=1\) and \(M_a\) is an
everywhere-defined unitary multiplication operator on \(L^2(\mathbb R)\).
Plancherel gives that \(\mathcal F_+\) is unitary. Hence every factor and the
ordered product are everywhere-defined unitaries:

\[
U_a^*=U_a^{-1}=M_a^*\mathcal F_+^{-1},
\qquad
U_G^*=U_G^{-1}=U_{1/2}^{-1}U_{3/2}^{-1}U_{5/2}^{-1}.
\]

Equivalently, the distributional kernel identities use

\[
\int_{\mathbb R}e^{i(q-q')Q}\,dQ=2\pi\,\delta(q-q'),
\]

and give both \(U_a^*U_a=I\) and \(U_aU_a^*=I\). The three-kick kernel is
understood as an iterated oscillatory integral over the two intermediate
coordinates. No global absolute-convergence or single reduced-phase claim is
made: the intermediate Hessian can vanish (a caustic), while factorization
still proves unitarity.

This is a unitary Floquet propagator, not a self-adjoint Hamiltonian. No
logarithm branch, spectral type, or operator-domain claim for a Hamiltonian is
introduced.

## 4. Natural antiunitary audit

Let \(C\) be pointwise complex conjugation and define

\[
\Theta_R=\mathcal F_+C.
\]

Using \(C\mathcal F_+C=\mathcal F_+^{-1}\), one obtains
\(\Theta_R^2=I\). On the Schwartz core,

\[
\Theta_R\,q\,\Theta_R^{-1}=p,
\qquad
\Theta_R\,p\,\Theta_R^{-1}=q,
\]

so this antiunitary quantizes the parent swap \(R(q,p)=(p,q)\). Also
\(CM_aC=M_a^{-1}\), and therefore each factor obeys the exact reversibility
identity

\[
\Theta_RU_a\Theta_R^{-1}=U_a^{-1}.
\]

For the three-kick product, however,

\[
\Theta_RU_G\Theta_R^{-1}
 =U_{5/2}^{-1}U_{3/2}^{-1}U_{1/2}^{-1}
 \ne
 U_{1/2}^{-1}U_{3/2}^{-1}U_{5/2}^{-1}=U_G^{-1}.
\]

The mismatch is exact, not a numerical spectral observation. The classical
canonical graphs already differ at the origin:

\[
RGR(0,0)=(-1/2,-5/8),
\qquad
G^{-1}(0,0)=(-1/2,-1/8).
\]

The reverse parameter word \((5/2,3/2,1/2)\) is not a cyclic rotation of the
forward word \((1/2,3/2,5/2)\), so the inherited clock-reflection family is
also excluded. Simple affine/metaplectic antiunitaries are covered by the
existing affine anti-symplectic obstruction. This audit does **not** exclude
arbitrary nonlinear, non-geometric, or non-polynomial antiunitaries.

## 5. Exact order control

The factor order is not cosmetic. On the Heisenberg generators, direct
conjugation gives

\[
\operatorname{Ad}_{U_a}(q)=p,
\qquad
\operatorname{Ad}_{U_a}(p)=1-q-ap^2.
\]

Consequently, for \(a=1/2\) and \(b=3/2\),

\[
\operatorname{Ad}_{U_bU_a}(q)=1-q-\frac32p^2,
\qquad
\operatorname{Ad}_{U_aU_b}(q)=1-q-\frac12p^2,
\]

so the two factors do not commute. This supplies an exact operator-order
witness independent of any spectrum or discretization.

## 6. Claim boundary

Established:

- one same-order target-free Fourier-integral factor for each frozen kick;
- exact canonical graph matching and fixed positive-real normalization;
- everywhere-defined unitarity of each factor and of the three-kick product on
  \(L^2(\mathbb R)\);
- the involutive parent-swap antiunitary and its exact one-kick identities;
- failure of that inherited antiunitary and of inherited cyclic clock reflection
  for the non-palindromic superstep.

Not established:

- absence of arbitrary nonlinear or non-geometric antiunitaries;
- self-adjoint Hamiltonian, spectral type, trace formula, determinant, or
  completed-\(\xi\) divisor;
- any spectrum, zero comparison, Route B, Hilbert--Pólya realization, or RH.

The next task is not a spectral calculation. If the candidate is continued,
the next bounded question is whether a separate, explicitly frozen phase/Maslov
ledger is needed for orbit-level quantization; it must not be inferred from
signed classical multipliers.
