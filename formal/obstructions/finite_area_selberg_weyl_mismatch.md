# Finite-Area Selberg/Weyl Divisor Obstruction

**Status:** project corollary from established external theorems
**Active clue:** CLUE-A1-002
**Triggering candidate:** SS-0002
**Route-A layers:** A2, A3

## 1. Statement

Let

\[
\Gamma_0=\operatorname{PSL}_2(\mathbb Z)
\]

and let \(\Gamma\leq\Gamma_0\) be a finite-index subgroup. Suppose a proposed
dynamical Fredholm determinant \(D_\Gamma(s)\) has, under one fixed
determinant convention, the Selberg-zeta divisor of \(Z_\Gamma(s)\).

Then the zero divisor of \(D_\Gamma\) has at least \(\Omega(T^2)\) zeros of
height at most \(T\), counted with multiplicity. Consequently it cannot equal

\[
e^{g(s)}\xi(\alpha s+\beta),\qquad \alpha\ne0,
\]

globally, where \(e^{g(s)}\) is entire and zero-free. It also cannot have the
same global divisor as that function.

## 2. Proof

The modular surface has hyperbolic area \(\pi/3\). The cuspidal Weyl law for
the modular Laplacian gives, for positive spectral height,

\[
N_{\rm cusp,\Gamma_0}(T)
=\frac{\operatorname{area}(\Gamma_0\backslash\mathbb H)}{4\pi}T^2
+o(T^2)
=\frac{T^2}{12}+o(T^2).
\]

Every \(\Gamma_0\)-automorphic cusp eigenfunction is also
\(\Gamma\)-automorphic. Its squared norm on the finite cover is multiplied by
the finite index, so it remains an \(L^2\) eigenfunction. Hence the modular
cuspidal spectrum injects into the discrete spectrum of the cover.

The Selberg-zeta divisor contains zeros at

\[
s=\frac12\pm i r_j
\]

for these Laplace eigenvalues \(1/4+r_j^2\), with their spectral
multiplicities. Therefore

\[
N_{Z_\Gamma}^{+}(T)
\geq \frac{T^2}{12}+o(T^2)
=\Omega(T^2).
\]

By contrast, the Riemann--von Mangoldt formula gives

\[
N_\xi^{+}(T)
=\frac{T}{2\pi}\log\frac{T}{2\pi}
-\frac{T}{2\pi}
+O(\log T)
=\Theta(T\log T).
\]

A zero-free entire factor does not change a divisor. A fixed nondegenerate
affine change of variable rescales disk radii by a constant and does not
change the growth exponent of the zero count. Thus an \(\Omega(T^2)\)
Selberg divisor cannot equal a \(\Theta(T\log T)\) completed-xi divisor. ∎

## 3. SS-0002 corollary

For SS-0002,

\[
\Gamma_{\rm com}=[\Gamma_0,\Gamma_0]
=\ker\!\left(\Gamma_0\to C_6\right)
\]

has index six. It is torsion-free, has one cusp of width six, genus one, and
area

\[
6\cdot\frac{\pi}{3}=2\pi.
\]

The paired-Gauss regular-holonomy operator is countable-branch,
infinite-dimensional, non-locally-constant, and nuclear of order zero for
\(\Re s>1/2\). It therefore genuinely lies outside OBR-005.

However, the frozen identity

\[
D_{\rm ab}(s)
=\det_{\rm Fr}(I-\mathcal M_s)
=Z_{\Gamma_{\rm com}}(s)
\]

puts it inside the present obstruction. The full finite-area resonance Weyl
law is even stronger: with area \(2\pi\), the two-sided resonance main term is
\(T^2\). The proof above uses only the safer inherited modular cusp-spectrum
lower bound.

## 4. Determinant-ledger boundary

The modular scattering determinant is a different object. In common
normalizations it contains a completed-zeta ratio schematically of the form

\[
\varphi(s)\sim\frac{\Lambda(2s-1)}{\Lambda(2s)},
\]

with convention-dependent elementary factors and with both zeros and poles.
It is not \(D_{\rm ab}\), \(1/D_{\rm ab}\), or
\(D'_{\rm ab}/D_{\rm ab}\). Multiplying its numerator into the Mayer
determinant, or using its denominator to cancel Selberg zeros, is forbidden
cross-determinant gluing unless a single same-object physical determinant
identity is first proved.

## 5. Scope

This obstruction covers direct Selberg-zeta/Fredholm determinants for
finite-index modular covers and, more generally, any candidate whose same
determinant divisor contains the inherited modular cuspidal spectrum.

It does not by itself rule out:

- infinite-area hyperbolic systems with a different rigorously counted divisor;
- non-Selberg nuclear transfer determinants;
- a single physical determinant with a proved internal cancellation law;
- operators whose intrinsic divisor has the \(T\log T\) scale from the start.

Any reopening must keep the clock, normalization, and determinant data type
fixed and must prove the new divisor count without borrowing a separate
scattering ledger.

## 6. Sources

- E. Balslev and A. Venkov, *The Weyl Law for Subgroups of the Modular Group*,
  DOI 10.1007/s000390050063.
- David Borthwick, *Distribution of resonances for hyperbolic surfaces*,
  arXiv:1305.4850v2.
- A. B. Venkov and P. G. Zograf, Artin factorization for induced
  representations of Fuchsian groups, DOI 10.1070/IM1983v021n03ABEH001800.

## 7. Claim boundary

This is a structural Route-A obstruction for one determinant class. It is not
a statement about the truth or falsity of the Riemann Hypothesis, and it does
not convert the natural modular Laplacian into a Hilbert--Polya operator.
