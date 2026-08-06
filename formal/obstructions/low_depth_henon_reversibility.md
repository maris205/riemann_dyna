# OBR-010 — Low-depth Hénon twists retain hidden reversibility

Status: `PROVED_OBSTRUCTION`

Let

\[
F_a(q,p)=(1-aq^2-p,q),
\qquad
R(q,p)=(p,q).
\]

Then \(RF_aR=F_a^{-1}\). Three common low-complexity mutations do not create
a genuine time-oriented candidate.

## 1. A quadratic post-shear is only a conjugacy

For

\[
S_\kappa(q,p)=(q,p+\kappa q^2),
\]

one has the exact identity

\[
S_\kappa F_a
=S_\kappa F_{a+\kappa}S_\kappa^{-1}.
\]

Thus the apparent twist is conjugate to a single shifted-parameter Hénon map
and inherits the conjugated reversor \(S_\kappa R S_\kappa^{-1}\).

## 2. Static generalized Hénon deformations remain reversible

For any scalar function \(g\) for which the map is defined,

\[
H_g(q,p)=(g(q)-p,q)
\]

satisfies

\[
RH_gR=H_g^{-1}.
\]

Adding a cubic force, including the quartic-potential legacy deformation,
changes the polynomial degree but does not break this time reversal.

## 3. Every two-kick composition has a reversor

For

\[
G_{a,b}=F_bF_a,
\qquad
I_a=F_a^{-1}R,
\]

the map \(I_a\) is an involution and

\[
I_aG_{a,b}I_a=G_{a,b}^{-1}.
\]

Therefore a two-kick non-palindromic-looking product is still reversible.

## Scope and reopening condition

This obstruction covers the displayed single-shear, static generalized-Hénon,
and two-kick classes. It does not state that every three-kick or higher product
breaks time reversal. Reopen only with one explicit frozen product whose
inherited clock reversors are absent and whose relevant affine or nonlinear
anti-symplectic involutions are audited separately.

`TH-0001` lies outside these three subclasses. Its affine reversor class is
excluded, while arbitrary nonlinear reversors remain open.
