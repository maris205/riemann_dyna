# Finite-State Finite-Roof Zero-Count Obstruction

**Status:** proved in the project under the assumptions below
**Active clue:** `CLUE-A1-002`
**Triggering baseline:** `SS-0001`
**Route-A layers:** A2, A3

## 1. Theorem

Let \(G=(V,E)\) be a finite directed multigraph. Assign to every edge
\(e\in E\):

- a fixed complex weight \(w_e\in\mathbb C\);
- a positive roof value \(\tau_e>0\).

Define the finite transfer matrix

\[
(L_s)_{ij}
=
\sum_{e:i\to j} w_e e^{-s\tau_e},
\qquad s\in\mathbb C,
\]

and the determinant

\[
D(s)=\det(I-L_s).
\]

Assume \(D\not\equiv0\). For every bounded real interval
\([a,b]\subset\mathbb R\), the number of zeros of \(D\), counted with
multiplicity, in

\[
\{s\in\mathbb C:a\leq\Re s\leq b,
\ |\Im s|\leq T\}
\]

is \(O(T)\) as \(T\to\infty\).

Consequently, no determinant in this class can have the same global divisor
as the completed Riemann function \(\xi(s)\), even after multiplication by a
zero-free entire factor or after a fixed nondegenerate affine change of the
spectral variable.

The same counting obstruction applies to zeros or poles obtained from
\(1/D\), \(D'/D\), or another convention whose divisor is supported on the
zeros of this same finite determinant. The conventions must still be reported
separately.

## 2. Proof

Because \(G\) has finitely many edges, every entry of \(L_s\) is a finite
exponential sum. Expanding the determinant over permutations and then
expanding the finite edge sums gives

\[
D(s)=\sum_{k=0}^{M} c_k e^{-\lambda_k s},
\]

where \(M<\infty\), \(c_k\in\mathbb C\), and every \(\lambda_k\geq0\) is a
finite sum of edge roofs. Thus \(D\) is an entire exponential polynomial.

Set

\[
\Lambda=\max_k\lambda_k,
\qquad
C=\sum_k |c_k|.
\]

For every \(s\in\mathbb C\),

\[
|D(s)|
\leq
\sum_k |c_k|e^{-\lambda_k\Re s}
\leq
C e^{\Lambda|s|}.
\]

Since \(D\not\equiv0\), choose \(s_0\in\mathbb C\) with \(D(s_0)\neq0\).
Apply Jensen's formula to \(z\mapsto D(s_0+z)\). The growth estimate gives

\[
\frac1{2\pi}\int_0^{2\pi}
\log^+|D(s_0+Re^{i\theta})|\,d\theta
\leq
\log C+\Lambda(|s_0|+R).
\]

Jensen's formula therefore bounds the number of zeros in
\(|s-s_0|\leq R/2\) by \(O(R)\), with multiplicity. A rectangle with
\(a\leq\Re s\leq b\) and \(|\Im s|\leq T\) lies in a disk centered at
\(s_0\) of radius \(T+O(1)\). Hence its zero count is \(O(T)\).

On the other hand, the Riemann-von Mangoldt formula gives

\[
N_\xi(T)
=
\frac{T}{2\pi}\log\frac{T}{2\pi}
-\frac{T}{2\pi}
+O(\log T)
=\Theta(T\log T)
\]

for the nontrivial zeros in the critical strip with positive imaginary part.
A zero-free entire factor does not change a divisor. A fixed affine spectral
change \(s\mapsto\alpha s+\beta\), \(\alpha\neq0\), changes heights only by a
constant factor and preserves the \(O(T)\) versus \(\Theta(T\log T)\)
incompatibility. Therefore no determinant in the stated finite-dimensional
class can equal \(e^{g(s)}\xi(s)\) globally or share its divisor. ∎

## 3. Corollary for finite-memory symbolic suspensions

A finite-state subshift with a roof and potential depending on only finitely
many symbols can be recoded as a finite higher-block graph. If its proposed
determinant is the determinant of the resulting finite transfer matrix, the
theorem applies.

Therefore, adding only finite residue memory, a finite number of sheets, or a
finite locally constant phase decoration cannot by itself produce the
completed-\(\xi\) divisor through a finite-dimensional determinant.

## 4. Scope boundary

The theorem does **not** cover:

- countable-state shifts;
- infinitely many edges or roof values;
- unbounded roofs;
- non-locally-constant Hölder potentials represented by an
  infinite-dimensional Ruelle operator;
- nuclear or trace-class transfer operators on infinite-dimensional spaces;
- Selberg-type or scattering determinants whose symbolic coding does not
  reduce the determinant to a finite matrix;
- parameter-dependent weights with additional uncontrolled analytic factors.

These are reopening directions, not established candidates.

## 5. Relation to SS-0001

For `SS-0001`, the adjacency spectrum is

\[
\{2,1,1,-1,-1,-2\},
\]

and the theorem specializes to the exact factorization

\[
D(s)
=(1-4e^{-2s})(1-e^{-2s})^2.
\]

The explicit orbit census and determinant computation are reproduced by:

```bash
python3 -m unittest -v tests/test_ss_0001_mod6_cayley.py
python3 experiments/ss_0001_mod6_cayley.py --max-period 24 --output artifacts/ss_0001/route_a_baseline.json
```

## 6. Claim boundary

This is a scoped family obstruction for finite-dimensional transfer
determinants. It does not rule out symbolic dynamics as a whole and does not
establish any result about the truth or falsity of the Riemann Hypothesis.
