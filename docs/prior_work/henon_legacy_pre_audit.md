# Legacy Hénon pre-candidate audit

Date: 2026-08-06

Active clue: `CLUE-A4-001`

Formal candidate produced from legacy fitted code: no.

## Clean classical parent

The only autonomous target-free map shared by the early legacy notebooks is

\[
F_a(x,y)=(1-ax^2-y,x),
\qquad
\det DF_a=1.
\]

It is exactly reversible:

\[
F_a^{-1}(x,y)=(y,1-ay^2-x),
\qquad
R(x,y)=(y,x),
\qquad
RF_aR=F_a^{-1}.
\]

The target-free parent control used by the new prefilter is \(F_1\). Its two
fixed points are \(-1\pm\sqrt2\), one elliptic and one hyperbolic.

## Apparent alternatives that are not twists

The kick--drift map from the cubic continuum potential,

\[
p'=p+1-2q-aq^2,
\qquad
q'=q+p',
\]

is linearly conjugate to \(F_a\) under \(q=x, p=x-y\).

Adding the legacy quartic confinement gives

\[
p'=p+1-2q-aq^2-4\lambda q^3,
\qquad
q'=q+p',
\]

or the generalized Hénon map

\[
(x,y)\mapsto(1-ax^2-4\lambda x^3-y,x).
\]

This is a genuine degree change when \(\lambda\ne0\), but it still satisfies
the same swap reversibility. The value \(\lambda=0.05\) is a chosen spectral
regularizer, not a classical first-principles constant.

## Parameters and data firewall

- \(a_c\approx1.00561\) is a finite numerical manifold-distance observation,
  not an intrinsic exact constant.
- \(a=1.02\) is a finite-resolution modeling choice.
- In notebook 4, \(\kappa=35.5499\) was chosen from the fitted
  \(\hbar=0.061387\) so that the displayed crossing returns 1.02; it is not an
  independent derivation.
- Legacy schedules, \(\hbar\), smoothing widths, spectral scales, and
  quartic coefficients in scripts 5--9 use zero, GUE, or USTC targets and are
  forbidden as candidate-definition inputs.

The new candidate therefore imports only the exact parent formula and its
symplectic/reversibility facts. It imports none of the displayed transition
parameters or spectral schedules.

## Markov normalization warning

Several legacy CSR scripts divide entries by

```python
sums[P_sparse.indices]
```

where `indices` are destination columns. If \(T\) is the accumulated matrix
and \(D=\operatorname{diag}(T\mathbf1)\), this produces \(TD^{-1}\), not the
row-stochastic matrix \(D^{-1}T\). When \(D\) is invertible the two matrices
are exactly similar,

\[
TD^{-1}=D(D^{-1}T)D^{-1},
\]

so the bug alone does not manufacture exact eigenvalues. It does invalidate
the Markov/eigenvector interpretation and can worsen finite-precision
nonnormal conditioning. No legacy Markov eigenphase is used as evidence for
`TH-0001`.

## Result of the inventory

The legacy directory contains no explicit magnetic or topological twist.
Static generalized Hénon and two-kick variants retain exact reversors; this is
registered as `OBR-010`. The first accepted new object is instead the frozen
three-kick non-palindromic superstep `TH-0001`.
