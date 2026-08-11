# SS-0003 — Connected integer-renewal Dirichlet transfer

This is a formal Route-A candidate created from CLUE-A4-002 only after its
bounded prefilter showed that it is connected, non-Selberg, and not subject to
the disconnected-bouquet OBR-016 escape.  It is not a Hilbert-Pólya
construction and it uses no prime or zero table.

## Frozen object

Let V={h} union {v_n:n>=2}, with directed edges

\[
h\longrightarrow v_n,\qquad v_n\longrightarrow h,\qquad n\ge2.
\]

Each edge in the n-excursion has roof (1/2)log(n), and the potential is zero.
The graph is strongly connected and has discrete edge period two.  The
first-return system at h is the full countable renewal shift on labels n>=2.
Its roof is non-arithmetic because log(2)/log(3) is irrational.

On H=C e_h direct_sum ell2({2,3,...}), for Re(s)>1, put
q_s=(n^(-s/2))_{n>=2} and use the holomorphic bilinear coordinate functional
ell_s(x)=sum_{n>=2}n^(-s/2)x_n.  Define

\[
\mathcal L_s(c,x)=\bigl(\ell_s(x),c q_s\bigr).
\]

The bilinear notation is deliberate: writing a conjugated Hilbert inner
product would obscure holomorphic dependence on s.  Since

\[
\|q_s\|_2^2=\sum_{n\ge2}n^{-\Re s}<\infty,
\]

L_s is a rank-at-most-two trace-class family, holomorphic in trace norm on
Re(s)>1.  With the stated bilinear coordinate convention its two nonzero
singular values are both \(\|q_s\|_2\), so

\[
\|\mathcal L_s\|_1=2\|q_s\|_2
 =2\left(\sum_{n\ge2}n^{-\Re s}\right)^{1/2}.
\]

Its nonzero eigenvalues satisfy

\[
\lambda^2=S(s),\qquad S(s)=\sum_{n\ge2}n^{-s},
\]

and hence the one frozen Fredholm ledger is

\[
D_{\rm ren}(s)=\det_F(I-\mathcal L_s)=1-S(s)=2-\zeta(s).
\]

The primitive cycles are cyclically primitive words [n_1,...,n_k].  Their
roof is

\[
T_{[n_1,\ldots,n_k]}=\sum_i\log n_i
                     =\log\prod_i n_i,
\]

and an r-fold repetition has weight (product_i n_i)^(-r*s).  For the edge
clock,

\[
\operatorname{Tr}\mathcal L_s^{2k}=2S(s)^k,
\qquad
\operatorname{Tr}\mathcal L_s^{2k+1}=0.
\]

The exact primitive/repetition trace-log is therefore

\[
-\log D_{\rm ren}(s)=\sum_{k\ge1}\frac{S(s)^k}{k}
\]

only on the subdomain |S(s)|<1.  It must not be silently asserted on the
whole Fredholm half-plane Re(s)>1.  The scalar function 2-zeta(s) has a
meromorphic continuation to C minus {1}, but this is not a Fredholm
continuation of the same ell2 operator.

## Divisor prefilter

For Re(s)>=2,

\[
|\zeta(s)-1|\le\sum_{n\ge2}n^{-\Re s}
\le\frac14+\int_2^\infty x^{-2}\,dx=\frac34<1,
\]

so all a=2 points with positive real part lie in the fixed strip
0<Re(s)<2.  The classical Bohr-Landau a-point theorem (Landau 1913; see
Titchmarsh-Heath-Brown, 2nd ed., section 9.4, and the modern summary by Hang
and Luo, arXiv:2411.13255v2) gives

\[
N_2(T)=\frac{T}{2\pi}\log\frac{T}{2\pi e}+O(\log T),
\qquad T\longrightarrow\infty,
\]

for the nontrivial a=2 points with positive ordinate.  Thus the frozen
scalar continuation has a Theta(T log T) divisor regime in a fixed strip,
without any numerical root search.  This only matches the order of the target
count; it says nothing about the xi functional equation or zero locations.

## Strict failure

For real sigma>1, S(sigma) is strictly decreasing, diverges at 1+, and
satisfies S(2)<3/4.  There is therefore a unique sigma_star in (1,2) with
D_ren(sigma_star)=0.  This extra right-half-plane zero is incompatible with
the completed xi-divisor and is recorded as OBR-017.  No root was located
numerically.

The primitive alphabet is all integers, not primes.  Primitive cycles are
ordered-factorization necklaces, and their amplitudes are unit weights rather
than derived von-Mangoldt weights.  The finite-rank collapse to the single
Dirichlet sum is an explicit A1/A4 weakness, not evidence of a natural
arithmetic host.

## Route-A decision

    analytic tuple:       (A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)
    Riemann-target tuple: (A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
    overall:              ROUTE_A_REJECTED / STOP_SCOPED
    Route B:              not invoked and not authorized

Established: a connected countable renewal graph, exact primitive/repetition
ledger, finite-rank Fredholm determinant on its defining half-plane, a
target-free fixed-strip Theta(T log T) a-point count, and the strict
right-half-plane obstruction.

Not established: prime correspondence, von-Mangoldt trace weights, same-
operator Fredholm continuation into the critical strip, functional equation,
completed-xi equality, quantization, Route B, Hilbert-Pólya, or RH.

The next smallest task is not to tune this object.  Any reopening must freeze
a new connected grammar with a signed/complex weight mechanism that avoids the
positive right-half-plane zero without importing target data.
