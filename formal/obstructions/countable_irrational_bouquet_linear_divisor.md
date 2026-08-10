# OBR-016 — Irrational-roof countable cycle bouquets still have a linear fixed-strip divisor

Status: `PROVED_OBSTRUCTION` (prefilter scope; not a formal candidate)

Source:
`SS-PREFILTER-IRRATIONAL-BOUQUET-001`, following `CLUE-A4-002`

## Statement

Consider the countable suspension

\[
 \Sigma=\bigsqcup_{n\ge 2}\mathbb Z/n\mathbb Z,
 \qquad \sigma(n,j)=(n,j+1\pmod n),
\]

with one-step roof and potential

\[
 \tau_n=1+\frac{\sqrt2}{n},
 \qquad \phi_n=-n.
\]

On \(\ell^2(\Sigma)\), freeze the same-object transfer family

\[
 (\mathcal L_s f)(n,j)
 =e^{-n-s\tau_n}f(n,j-1\pmod n).
\]

The family is trace class and entire in \(s\), because on every compact set
the trace norm is bounded by a constant times

\[
 \sum_{n\ge2}n e^{-n}<\infty.
\]

Its only determinant ledger is

\[
 D_{\mathrm{bouquet}}(s)
 =\det_{\mathrm F}(I-\mathcal L_s)
 =\prod_{n\ge2}\left(1-e^{-n^2-s(n+\sqrt2)}\right).
\]

The primitive orbit \(\gamma_n\) has period \(n\), roof
\(L_n=n+\sqrt2\), and action \(A_n=n^2\).  The exact repetition ledger is

\[
 -\log D_{\mathrm{bouquet}}(s)
 =\sum_{n\ge2}\sum_{r\ge1}
 \frac{e^{-r n^2-sr(n+\sqrt2)}}{r},
\]

initially where the trace series converges and then by the normally convergent
product.  The zeros are exactly

\[
 s_{n,k}= -\frac{n^2+2\pi i k}{n+\sqrt2},
 \qquad n\ge2,\ k\in\mathbb Z.
\]

In particular every zero has negative real part, so the frozen determinant has
no zeros in the usual strip \(0\le\Re s\le1\).

The real parts \(\alpha_n=-n^2/(n+\sqrt2)\) are strictly decreasing and tend
to \(-\infty\).  Therefore every bounded vertical strip contains only finitely
many zero lines, and

\[
 N_{[a,b]}(T)
 =\sum_{\alpha_n\in[a,b]}
 \left(2\left\lfloor\frac{T(n+\sqrt2)}{2\pi}\right\rfloor+1\right)
 =O_{a,b}(T).
\]

This cannot have the completed-\(\xi\) divisor regime \(\Theta(T\log T)\) in
fixed critical strips.

## Proof details

The \(n\)-block is a weighted cyclic permutation.  Its determinant is
\(1-(e^{-n-s\tau_n})^n\), and the sum of the block trace norms is locally
uniformly finite.  Since \(n^2/(n+\sqrt2)\) has positive derivative on
\((0,\infty)\), \(\alpha_n\) is strictly decreasing.  The zero formula follows
by solving one block factor equal to zero; the normal convergence of the tail
prevents any additional zeros.

The period set is globally incommensurate: if all \(n+\sqrt2\) belonged to
one lattice \(h\mathbb Z\), then their difference would give \(1\in h\mathbb Z\),
while \(\sqrt2\) would also be rationally commensurate with \(h\), a
contradiction.  This is only a global incommensurability statement; the base is
disconnected and each component is periodic, so no mixing or prime-orbit law is
being claimed.

## Impact on the search

The example escapes the finite-state/finite-roof obstruction `OBR-005` and is
not a Selberg determinant, but countability plus a non-common roof span is not
enough.  Superexponentially escaping cycle actions move all but finitely many
zero lines out of every fixed strip, forcing the wrong divisor density.

The audit is therefore a reusable negative structural prior, not `SS-0003`.
It rules out this disconnected bouquet subclass only.  It does not exclude a
connected renewal system whose cycle actions remain in a critical strip, nor a
different non-Selberg nuclear object with an independently proved
\(T\log T\) divisor regime.

Artifacts:

- `configs/source_locks/SS-PREFILTER-IRRATIONAL-BOUQUET.yaml`
- `experiments/ss_prefilter_irrational_bouquet.py`
- `artifacts/ss_prefilter_irrational_bouquet/audit.json`
- `evaluations/route_a/SS-PREFILTER-IRRATIONAL-BOUQUET/20260810T162243Z.yaml`
- `tests/test_ss_prefilter_irrational_bouquet.py`
