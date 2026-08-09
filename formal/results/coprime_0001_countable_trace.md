# COPRIME-0001: exact countable trace and primitive-cycle ledger

## Scope

This note freezes one target-free countable-state object and records the first
theorem edge.  It does not evaluate determinant roots and does not compare the
object with a Riemann-zero list.

Let

\[
 I=\{2,3,\ldots\},\qquad
 \Sigma_{\rm cop}=\{(n_k)_{k\in\mathbb Z}:\gcd(n_k,n_{k+1})=1\},
\]

with shift and roof \(\tau(n_k)=\log n_0\).  On \(\ell^2(I)\), freeze the
symmetric transfer kernel

\[
 (L_s)_{mn}=\mathbf 1_{(m,n)=1}(mn)^{-s/2},
 \qquad \Re s>1.
\]

The determinant convention is the single object

\[
 D_{\rm cop}(s)=\det_{\!F}(I-L_s).
\]

No reciprocal determinant, logarithmic derivative, scattering quotient, or
completed-xi factor is part of this ledger.

## Trace-class theorem

Write \(\sigma=\Re s>1\).  The standard divisor identity gives

\[
 \mathbf 1_{(m,n)=1}=\sum_{d\mid m,n}\mu(d).
\]

Define

\[
 a_d(m)=\mathbf 1_{d\mid m}m^{-s/2},\qquad
 c_d(m)=\mathbf 1_{d\mid m}m^{-\bar s/2}.
\]

Then, as a matrix identity,

\[
 L_s=\sum_{d\ge1}\mu(d)\,a_d c_d^*.
\]

Each summand is rank one and has trace norm

\[
 S_d=\|a_dc_d^*\|_1
     =\sum_{\substack{m\ge2\\d\mid m}}m^{-\sigma}.
\]

Consequently,

\[
 \sum_{d\ge1}|\mu(d)|S_d
 =\frac{\zeta(\sigma)^2}{\zeta(2\sigma)}-1<\infty.
\]

The series converges locally uniformly in trace norm on \(\Re s>1\).  Thus
\(L_s\) is a holomorphic trace-class family there and \(D_{\rm cop}\) is a
well-defined holomorphic Fredholm determinant on that half-plane.

This is an intrinsic analytic object, but it is only a half-plane theorem;
continuation and global divisor growth remain open.

The threshold is exact for this \(\ell^2\) realization.  Let \(e_2\) be the
second coordinate vector.  For \(\sigma=\Re s\le1\),

\[
 \|L_se_2\|_2^2
 =2^{-\sigma}\sum_{\substack{m\ge3\\m\ \mathrm{odd}}}m^{-\sigma}
 =\infty.
\]

Hence the frozen matrix does not define a bounded operator on this Hilbert
space for \(\Re s\le1\).  A continuation of the scalar Fredholm determinant,
if one exists, would therefore require a theorem beyond the original
trace-class operator definition; it cannot be obtained by silently extending
the same bounded operator.

## Exact trace powers and cycle weights

Let \(P_N\) project onto labels \(2,\ldots,N\).  The trace-norm convergence
\(P_NL_sP_N\to L_s\), together with the finite-matrix cyclic expansion and
continuity of traces of fixed powers, passes the finite formula to the limit.
Equivalently, the absolute bound

\[
 \sum_{\mathrm{cyclic\ words}}|\mathrm{weight}|
 \leq\bigl(\zeta(\sigma)-1\bigr)^k
\]

justifies every rearrangement.  Thus, for every \(k\ge1\),

\[
 \operatorname{Tr}L_s^k
 =\sum_{\substack{n_0,\ldots,n_{k-1}\ge2\\
          (n_j,n_{j+1})=1\;(\mathrm{cyclic})}}
       \prod_{j=0}^{k-1}(n_jn_{j+1})^{-s/2}
 =\sum_{\substack{n_0,\ldots,n_{k-1}\ge2\\
          (n_j,n_{j+1})=1\;(\mathrm{cyclic})}}
       \left(\prod_{j=0}^{k-1}n_j\right)^{-s},
\]

where \(n_k=n_0\).  The second equality is the exact cyclic telescoping
identity, and is the only repetition convention used here.

If \(\gamma\) ranges over primitive directed cycles, with period
\(|\gamma|\) and weight \(w_\gamma=\prod_i n_i^{-s}\), then

\[
 \operatorname{Tr}L_s^k
 =\sum_{\substack{\gamma\ {\mathrm{primitive}}\\|\gamma|\mid k}}
      |\gamma|\,w_\gamma^{k/|\gamma|}.
\]

The finite exact certificate checks this identity at \(s=2\) through \(k=6\)
on a sealed label cutoff, using rational arithmetic.

## Periods one through three

There are no period-one cycles: a self-loop would require
\(\gcd(n,n)=n=1\), excluded by \(I\).

For period two, primitive cycles are represented by \(2\le a<b\) with
\((a,b)=1\), and

\[
 C_2(s)=2\sum_{\substack{2\le a<b\\(a,b)=1}}(ab)^{-s}
       =\frac{\zeta(s)^2}{\zeta(2s)}-2\zeta(s)+1.
\]

For period three, the cyclic condition is pairwise coprimality.  With

\[
 F_3(s)=\prod_p\frac{1+2p^{-s}}{1-p^{-s}},
\]

inclusion-exclusion of the forbidden label one gives

\[
 C_3(s)=F_3(s)-3\frac{\zeta(s)^2}{\zeta(2s)}+3\zeta(s)-1.
\]

All valid triples have distinct labels and are primitive.  Each unordered
pairwise-coprime triple has two directed cyclic orientations, hence the trace
contains six ordered representatives while the primitive-cycle sum contains
two cycles and each cycle contributes three rotations.

These identities establish the cycle ledger; they do not establish that
primitive cycles correspond to primes or that the amplitudes are
von-Mangoldt weighted.

## Route-A boundary

The first audit yields

```text
(A1_WEAK, A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)
```

Established:

- an explicit recurrent countable shift and a trace-class transfer family on
  \(\Re s>1\);
- exact trace-power, repetition, and period-1--3 primitive-cycle ledgers;
- a target-free, reproducible finite certificate.

Not established:

- a rational-prime orbit law or von-Mangoldt trace formula;
- analytic continuation, functional equation, or a \(T\log T\) divisor law;
- completed-xi equality, natural quantization, Route B, Hilbert--Pólya, or RH.

The next smallest task is a target-free continuation or growth audit for this
same determinant.  Since the frozen ell^2 matrix is unbounded for Re(s)<=1,
the task is specifically to prove or refute a scalar continuation across that
boundary without calling it the same bounded operator. Root searches and
Riemann-zero comparisons remain outside the source lock.

Reproduction:

```bash
python3 experiments/coprime_0001_countable_trace.py \
  --quiet \
  --output artifacts/coprime_0001/countable_trace_certificate.json
python3 -m unittest -v tests/test_coprime_0001_countable_trace.py
```
