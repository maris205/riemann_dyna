# Exact-​$U_c$ half-open partition ledger for the polar map

## Claim boundary

This checkpoint freezes the geometric endpoint convention for the exact-​$U_c$
polar Markov map. It proves the finite boundary orbit graph and a target-free
half-open coding rule. It does **not** prove the analytic trace multiplicity of
the weighted composition operator on the matching space. That local trace
identity remains an explicit next theorem.

The object is

\[
f(x)=1-U_cx^2,
\qquad
U_c^3-2U_c^2+2U_c-2=0,
\qquad
\rho=U_c-1,
\]

\[
S=-f^2,
\qquad
q(\theta)=\rho\sin\theta,
\qquad
G=q^{-1}\circ S\circ q
\]

on the two full branch intervals

\[
I_L=[-\pi/2,0],
\qquad
I_R=[0,\pi/2].
\]

The exact root $U_c$ is used throughout; the rounded legacy literal
`1.543689` is not part of the object.

## 1. Half-open geometric coding

The analytic doubled space keeps $0_L$ and $0_R$ distinct for branch coding,
but the geometric interval uses the frozen half-open partition

\[
I_L^{\mathrm{ho}}=[-\pi/2,0),
\qquad
I_R^{\mathrm{ho}}=[0,\pi/2].
\]

Thus the geometric partition point belongs to the right branch. Away from
$0$, the projection from the doubled space to the geometric interval is
one-to-one. At $0$, the two coding labels are identified. A geometric
periodic orbit is therefore assigned one half-open cyclic itinerary; cyclic
rotations are collapsed, and an $r$-fold repetition remains a separate
repetition operation.

This is a coding convention, not yet a Fredholm trace theorem. If a doubled
enumerator is used, it must project its words and quotient the explicitly
audited lift fibre before inserting a contribution into a trace ledger. No
unproved universal factor such as $2^h$ for $h$ partition visits is allowed.

## 2. Exact boundary orbit graph

Let

\[
P=-\pi/2,
\qquad Z=0,
\qquad Q=\pi/2.
\]

The critical polynomial identities give

\[
S(\rho)=-\rho,
\qquad
S(-\rho)=-\rho,
\qquad
S(0)=\rho.
\]

Since $q(P)=-\rho$, $q(Z)=0$, and $q(Q)=\rho$, the boundary graph is

\[
P\longmapsto P,
\qquad
Q\longmapsto P,
\qquad
Z\longmapsto Q.
\]

Consequently $P$ is the only periodic state in this exact boundary graph.
The partition point $Z$ is preperiodic and never itself supplies a boundary
periodic orbit. The states $Q$ and $Z$ are endpoint/partition hits in finite
itineraries, not additional periodic cycles.

This distinction matters: a preperiodic endpoint hit cannot be counted as a
primitive periodic orbit merely because it has two doubled labels.

## 3. Matching-space range lemma

At the frozen complex radius, let

\[
\mathcal B_\epsilon
=\{(v_L,v_R):v_\sigma\text{ is holomorphic on }U_\sigma,
\ v_L(0)=v_R(0)\}.
\]

For a fixed $s$, the conditional weighted family is written componentwise as

\[
(\mathcal L_s v)_j(z)
=e^{s\ell(z)}\bigl(v_L(\phi_L(z))+v_R(\phi_R(z))\bigr),
\qquad j\in\{L,R\}.
\]

Both output components are restrictions of the same function

\[
F_s(z)=e^{s\ell(z)}
\bigl(v_L(\phi_L(z))+v_R(\phi_R(z))\bigr).
\]

Therefore

\[
(\mathcal L_sv)_L(0)=(\mathcal L_sv)_R(0),
\]

so the range lies in the matching kernel

\[
\ker\delta,
\qquad
\delta(v)=v_L(0)-v_R(0).
\]

This proves that the two endpoint target labels represent one common output
value after matching. It does **not** by itself prove that a trace computed on
$\mathcal B_\epsilon$ has exactly the half-open geometric multiplicity: that
requires a local analytic trace calculation at the boundary fixed point $P$.

There is one useful conditional algebraic fact. Let $X$ denote the direct sum
of the two component spaces and let $B=\ker\delta$. If a later theorem proves
that the weighted operator is nuclear on $X$ and that its range is contained in
$B$, then relative to a decomposition $X=B\oplus\mathbb C e$ it has block form

\[
\begin{pmatrix}L_B&b\\0&0\end{pmatrix}.
\]

For every $n\geq1$ the powers have top-left block $L_B^n$, so conditionally

\[
\operatorname{Tr}_X L^n=\operatorname{Tr}_B L_B^n.
\]

This does **not** divide the source-branch sum by two. A finite toy matrix
$T(w)=\left(\begin{smallmatrix}w&w\\w&w\end{smallmatrix}\right)$ has trace
$2w$ on the full space and restriction trace $2w$ on the diagonal matching
line. Matching identifies the endpoint value, but it does not erase cyclic
source multiplicity.

## 4. Target-free certificate

The executable certificate checks:

1. the exact $U_c$ polynomial bracket and the three boundary identities;
2. disjoint/exhaustive half-open ownership;
3. the exact boundary graph and the preperiodic status of $0$;
4. cyclic-rotation canonicalization through word length $8$;
5. invariance under swapping the auxiliary endpoint labels $0_L$ and $0_R$;
6. retention of signed branch orientation;
7. the common-output matching lemma.

8. a finite block/toy calculation showing why matching alone cannot justify a
   factor-of-two trace correction.

These checks contain no primes, zeros, $ξ/\zeta$ evaluations, or fitted
parameters. The finite word cutoff is regression-only and is not promoted to
an all-period theorem.

## 5. Status and remaining obligation

The reusable result is a precise quotient-versus-doubled ledger rule:

\[
\boxed{\text{one geometric half-open cyclic lift per partition-hit orbit}}
\]

with signed orientation and repetition kept separate. The Route-A tuple remains

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
```

The remaining local theorem is:

> compute the analytic trace correction at the boundary fixed point $P$ on the
> matching space and prove whether it agrees with the half-open quotient count.

Until that theorem is proved, the audit is `REVISE` / `NOT_TESTABLE` for trace
multiplicity. Nuclearity, a Fredholm determinant, divisor comparison,
quantization, Route B, Hilbert--Pólya, and RH remain closed.

Reproduction:

```bash
python3 experiments/p4_logistic_uc_polar_partition_trace.py \
  --quiet \
  --output artifacts/p4_logistic_uc_polar_partition_trace/partition_trace_certificate.json
python3 -m unittest -v tests/test_p4_logistic_uc_polar_partition_trace.py
```
