# SS-PREFILTER-IRRATIONAL-BOUQUET-001 — Route-A prefilter result

This is a non-candidate audit for `CLUE-A4-002`; no formal `SS-0003` ID is
allocated.

## Frozen object

\[
\Sigma=\bigsqcup_{n\ge2}\mathbb Z/n\mathbb Z,
\qquad \sigma(n,j)=(n,j+1\pmod n),
\]

with one-step roof \(\tau_n=1+\sqrt2/n\) and per-step potential
\(\phi_n=-n\).  On \(\ell^2(\Sigma)\),

\[
(\mathcal L_s f)(n,j)=e^{-n-s\tau_n}f(n,j-1\pmod n).
\]

The sole determinant ledger is

\[
D_{\rm bouquet}(s)=\det_{\rm F}(I-\mathcal L_s)
=\prod_{n\ge2}\bigl(1-e^{-n^2-s(n+\sqrt2)}\bigr).
\]

## Exact evidence

There is one primitive \(n\)-cycle \(\gamma_n\), with period \(n\), roof
\(L_n=n+\sqrt2\), action \(A_n=n^2\), and repeat weight
\(e^{-r n^2-srL_n}\).  The block trace identity is

\[
\operatorname{tr}(\mathcal L_s^k)
=\sum_{n\mid k,\,n\ge2}n\,e^{-kn-sk(1+\sqrt2/n)}.
\]

The family is entire and trace class in \(s\), since the local trace norm is
bounded by a constant times \(\sum_{n\ge2}ne^{-n}\).  The divisor is explicit:

\[
s_{n,k}= -\frac{n^2+2\pi i k}{n+\sqrt2}.
\]

The real parts \(-n^2/(n+\sqrt2)\) decrease to \(-\infty\).  Hence every
bounded vertical strip contains finitely many zero lines and has
\(N_{[a,b]}(T)=O(T)\), incompatible with a \(T\log T\) divisor law.
Indeed, all zeros lie in \(\Re s<0\), so the usual strip \(0\le\Re s\le1\)
is already zero-free.

The two primitive lengths \(2+\sqrt2\) and \(3+\sqrt2\) have irrational ratio,
so the global period set has no common lattice.  This does not imply mixing:
the phase space is intentionally disconnected, and each component is periodic.

## Route-A decision

```text
analytic tuple:       (A1_WEAK, A2_ANALYTIC_DETERMINANT,
                       A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)
Riemann-target tuple: (A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
scoped verdict:       STOP_SCOPED
formal candidate:     false
Route B:              not authorized
```

The reusable conclusion is narrow: a countable, globally incommensurate roof
and an entire Fredholm determinant do not by themselves supply the critical
divisor.  The negative result applies only to this disconnected bouquet with
escaping cycle actions.  A connected renewal object would require a fresh
source lock and a separate prefilter.
