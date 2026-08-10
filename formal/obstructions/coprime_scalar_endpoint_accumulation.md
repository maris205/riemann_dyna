# OBR-015 — COPRIME scalar determinant has an endpoint zero accumulation at \(s=1\)

Status: `PROVED_OBSTRUCTION` (candidate-local, endpoint-scoped)

Source:
`COPRIME-0001-SCALAR-BOUNDARY-001`

## Statement

For the frozen object

\[
 (L_s)_{mn}=\mathbf 1_{(m,n)=1}(mn)^{-s/2},
 \qquad
 D_{\rm cop}(s)=\det_F(I-L_s),
 \qquad \Re s>1,
\]

there is a sequence of distinct positive real numbers (s_j>1) with

\[
 s_j\downarrow1,
 \qquad D_{\rm cop}(s_j)=0.
\]

The proof uses only a temporary label-one completion for min--max comparison.
Finite prime-coordinate compressions have local eigenvalues

\[
 \alpha_p^\pm(s)=\frac{1\pm\sqrt{(1+3p^{-s})/(1-p^{-s})}}2.
\]

The positive products with an even number of negative local factors become
arbitrarily large as (s\downarrow1), while the codimension-one removal of
the label-one state can remove at most one positive eigenvalue.  At (s=3),

\[
 \|L_3\|<9/16<1,
\]

so continuity of compact self-adjoint eigenvalues forces arbitrarily many
crossings of the level one.  The Fredholm zero criterion then gives the
sequence above.

## Consequence

No holomorphic or meromorphic germ of the same scalar determinant can pass
through (s=1).  A meromorphic germ would have only finitely many zeros in a
punctured neighborhood unless it vanished identically, contradicting the
accumulation and (D_{\rm cop}(3)\ne0).

The obstruction does **not** rule out a punctured scalar continuation at
points (1+it), (t\ne0).  Indeed, a separately named squarefree-divisor
`S_2` representation

\[
 \widetilde D(s)=\det_2(I-[\zeta(s)T_s-P_1])
\]

agrees with (D_{\rm cop}) on \(\Re s>1\) and is holomorphic for
\(\Re s>1/2,\ s\ne1\).  This representation is not the original bounded
`ell^2` operator below \(\Re s=1\), and the two determinant conventions must
remain explicitly separated.

## Scope and reopening condition

This is not a claim about every possible regularization, another function
space, or a new candidate.  Reopening requires a new source lock that names
the altered operator and determinant convention before any target comparison.

Artifacts:

- `configs/source_locks/COPRIME-0001-SCALAR-BOUNDARY.yaml`
- `formal/results/coprime_0001_scalar_boundary.md`
- `experiments/coprime_0001_scalar_boundary.py`
- `artifacts/coprime_0001/scalar_boundary_certificate.json`
- `evaluations/route_a/COPRIME-0001/20260810T030434Z.yaml`
