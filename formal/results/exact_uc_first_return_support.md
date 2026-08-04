# Exact first-return support at the Logistic band-merging parameter

## Status

`PROVED`

Source: `CLUE-A1-004` / `P4-LOGISTIC-UC-FIRST-RETURN-SUPPORT`

## Definitions

Let $u=U_c$ be the unique real root of

\[
p(u)=u^3-2u^2+2u-2,
\]

let

\[
\rho=u-1,
\qquad
f(x)=1-ux^2,
\]

and distinguish two domains:

\[
X=[-1,1],
\qquad
J=f(X)=[-\rho,1].
\]

The ambient and physical event sets are

\[
L_X=[-1,0),
\qquad
L_J=[-\rho,0).
\]

For $D\in\{X,J\}$ and $x\in L_D$, define

\[
\tau_D(x)=\min\{m\geq1:f^m(x)\in L_D\},
\]

with value $\infty$ if no return occurs, and

\[
C_m(D)
=L_D\cap
\bigcap_{j=1}^{m-1}f^{-j}(D\setminus L_D)
\cap f^{-m}(L_D).
\]

Thus zero is a non-event state. This convention fixes the half-open branch
endpoints below.

The root location used below is also elementary. Since

\[
p(3/2)=-1/8<0,
\qquad
p(2)=2>0,
\]

and

\[
p'(u)=3u^2-4u+2
=3\left(u-\frac23\right)^2+\frac23>0
\]

for every real $u$, one has

\[
\frac32<U_c<2,
\qquad
\frac12<\rho<1.
\]

## Theorem

### Physical invariant core

On $J$,

\[
\boxed{
S_{\rm top}^{J}
=\{m:C_m(J)\ne\varnothing\}
=2\mathbb N_{\geq1}.
}
\]

Every even return label has exactly one nondegenerate interval branch. More
precisely, define

\[
h(y)=\sqrt{\frac{1-y}{u}},
\qquad
\psi(y)=h(h(y)),
\]

and

\[
r_0=0,
\qquad
r_{n+1}=\psi(r_n).
\]

Then

\[
0<r_1<r_2<\cdots<\rho,
\qquad
r_n\longrightarrow\rho,
\]

and

\[
C_2(J)=(-r_1,0),
\]

\[
\boxed{
C_{2n}(J)=(-r_n,-r_{n-1}]
\quad(n\geq2),
}
\]

while

\[
C_{2n+1}(J)=\varnothing
\quad(n\geq0).
\]

The only point of $L_J$ that never returns is $-\rho$.

Moreover, on every branch interior,

\[
f^{2n}:\operatorname{int}C_{2n}(J)\longrightarrow(-\rho,0)
\]

is a real-analytic diffeomorphism onto the full event interior. Consequently,
every finite word of positive even return labels has a nonempty open cylinder.
The induced map therefore has the full finite-word language used by the
recurrent tower. This does not by itself prove realization of every infinite
one- or two-sided sequence, choose an invariant tower measure, or settle
endpoint codings.

### Ambient interval

On the literal ambient domain $X=[-1,1]$,

\[
\boxed{
S_{\rm top}^{X}=\mathbb N_{\geq1}.
}
\]

Let

\[
q_n=-h(r_n).
\]

Then $q_0=-u^{-1/2}$, $q_n\uparrow-\rho$, the even branches are the
physical branches above, and the transient odd branches are

\[
C_1(X)=[-1,q_0),
\]

\[
\boxed{
C_{2n+1}(X)=[q_{n-1},q_n)
\quad(n\geq1).
}
\]

Their union is exactly the transient interval $[-1,-\rho)$.

### Invariant weights

Every $f$-invariant probability measure on $X$ assigns zero mass to every
ambient odd branch. If $\mu_{\rm ac}$ is the standard physical absolutely
continuous invariant probability with support $J$, then

\[
\mu_{\rm ac}(C_{2n}(J))>0
\quad(n\geq1).
\]

Both assertions are now unconditional. Existence, uniqueness, and full support
of the named physical acip are proved in
`formal/results/exact_uc_acip_endpoint_density.md`. The positivity statement
is still false for arbitrary invariant measures.

## Proof

Substituting $u=\rho+1$ in $p(u)=0$ gives

\[
\rho^3+\rho^2+\rho-1=0,
\]

hence

\[
u\rho^2=1-\rho
\quad\text{and}\quad
f(\pm\rho)=\rho.
\]

Set

\[
A=[-\rho,\rho],
\qquad
B=[\rho,1].
\]

Evenness and monotonicity of $f$ on its two sides give the exact band swap

\[
f(A)=B,
\qquad
f(B)=A.
\]

Since $L_J\subset A$, every odd iterate of a point starting in $L_J$ lies in
$B\subset[0,1]$. Therefore no physical odd return exists.

Now write

\[
T=f^2|_A.
\]

Direct expansion gives

\[
T(x)=-\rho+2u^2x^2-u^3x^4,
\qquad
T'(x)=4u^2x f(x).
\]

Consequently, $T$ is strictly decreasing from $\rho$ to $-\rho$ on
$[-\rho,0]$ and strictly increasing from $-\rho$ to $\rho$ on
$[0,\rho]$. Both branches cover all of $A$. The inverse of the positive
branch is exactly $\psi=h\circ h$.

The positive branch satisfies $T(x)<x$ for $0\leq x<\rho$. One direct
factorization is

\[
T(x)-x
=-(ux^2+x-1)(u^2x^2-ux-u+1).
\]

The first factor is negative on $[0,\rho)$, and the second is negative on
$[0,\rho]$: it is convex, has value $1-u<0$ at zero, and at $\rho$ has
value $1-2\rho-2\rho^2<0$ because $\rho>1/2$. Thus $T(x)-x<0$.
Equivalently, $\psi(y)>y$ for $0\leq y<\rho$. The sequence $r_n$ is
therefore strictly increasing and bounded above by $\rho$. Its limit is a
fixed point of $\psi$, hence of $T$; the only such point in $[0,\rho]$ is
$\rho$.

To prove both inclusion and exhaustiveness, let

\[
P(y)=\psi(y),
\qquad
N(y)=-\psi(y)
\]

be the positive and negative inverse branches of $T$ on $A$. Thus

\[
T\circ P=T\circ N=\operatorname{id}_A,
\qquad
P(A)=[0,\rho],
\qquad
N(A)=[-\rho,0].
\]

Write $C_n^T$ for first return to $L_J$ after $n$ iterates of $T$. If
$x\in C_n^T$ and $y=T^n(x)\in L_J$, then every intermediate point
$T^j(x)$, $1\leq j<n$, must lie in $[0,\rho]$. Backward iteration is therefore
forced: the last $n-1$ inverse choices are $P$, while the initial choice is
$N$. Conversely, every point obtained by those forced inverse choices has
exactly that itinerary. Hence

\[
C_n^T=L_J\cap N\circ P^{n-1}(L_J).
\]

Since $\psi$ is increasing and

\[
\psi(-\rho)=0,
\qquad
\psi^n(L_J)=[r_{n-1},r_n),
\]

one obtains

\[
C_1^T=(-r_1,0)
\]

and, for $n\geq2$,

\[
C_n^T=(-r_n,-r_{n-1}].
\]

The band swap already excludes odd returns under $f$, so
$C_{2n}(J)=C_n^T$. This proves that the displayed list is exhaustive and that
there is exactly one branch for each even label. The left endpoint $-r_n$ hits
zero at the nominal return and therefore belongs to the next branch; the right
endpoint $-r_{n-1}$ hits zero one $T$ iterate earlier and then returns to
$-\rho$, explaining the half-open convention. The point $-\rho$ maps to the
fixed point $\rho$ and never returns.

On each branch interior, the forced itinerary avoids every critical preimage,
so $(T^n)'$ never vanishes there. The endpoint images are $0$ and $-\rho$;
monotonicity therefore gives a real-analytic diffeomorphism

\[
T^n:\operatorname{int}C_{2n}(J)\longrightarrow(-\rho,0).
\]

Let $\phi_n$ be its inverse branch. For any finite word of positive branch
indices $(n_0,\ldots,n_{k-1})$, corresponding to original return labels
$(2n_0,\ldots,2n_{k-1})$, the interval

\[
\phi_{n_0}\circ\phi_{n_1}\circ\cdots\circ\phi_{n_{k-1}}
\bigl((-\rho,0)\bigr)
\]

is a nonempty open cylinder with those successive return labels. This proves
the full-branch consequence.

For the ambient statement, $f$ maps the outer negative interval
$[-1,-\rho]$ monotonically onto $A$. Its inverse branch is

\[
\ell(y)=-h(y).
\]

Points mapping immediately into $L_J$ give

\[
\ell(L_J)=[-1,q_0)=C_1(X).
\]

For $n\geq1$, first return at time $2n+1$ is equivalent to the first image
lying in the forced positive cylinder $P^n(L_J)=[r_{n-1},r_n)$. Therefore,
in both directions,

\[
C_{2n+1}(X)
=\ell(P^n(L_J))
=[q_{n-1},q_n).
\]

Since $q_n\uparrow-\rho$, these intervals and $C_1(X)$ exhaust exactly
$[-1,-\rho)$. This proves the ambient statement without relying on a finite
itinerary scan.

Finally, $f(X)\subset J$, so

\[
f^{-1}(X\setminus J)=\varnothing.
\]

For any invariant probability $\nu$,

\[
\nu(X\setminus J)
=\nu(f^{-1}(X\setminus J))
=0.
\]

All ambient odd branches lie in $X\setminus J$ and therefore have zero
invariant mass. The separate exact endpoint-density theorem proves that the
physical acip exists and has full support $J$. Each physical even branch
contains a nonempty open interval, so it has positive physical-acip mass. ∎

## Corollary: endpoint-length ratio

Let

\[
\delta_n=\rho-r_n.
\]

Because $r_{n+1}=\psi(r_n)$, $\psi(\rho)=\rho$, and $r_n\to\rho$, the mean
value theorem gives points $\xi_n\in(r_n,\rho)$ such that

\[
\frac{\delta_{n+1}}{\delta_n}=\psi'(\xi_n)
\longrightarrow\psi'(\rho).
\]

The map $\psi$ is the inverse of the positive branch of $T$, so

\[
\psi'(\rho)
=\frac{1}{T'(\rho)}
=\frac{1}{4U_c^2\rho^2}
=:\lambda.
\]

Here $0<\lambda<1$. If

\[
\ell_n=|C_{2n}(J)|=r_n-r_{n-1}
=\delta_{n-1}-\delta_n,
\]

then

\[
\frac{\ell_{n+1}}{\ell_n}
=\frac{\delta_n}{\delta_{n-1}}
\frac{1-\delta_{n+1}/\delta_n}
     {1-\delta_n/\delta_{n-1}}
\longrightarrow\lambda.
\]

Therefore

\[
\boxed{
\frac{|C_{2n+2}(J)|}{|C_{2n}(J)|}
\longrightarrow
\frac{1}{4U_c^2(U_c-1)^2}
}.
\]

This is a Lebesgue-length statement. The additional density theorem needed to
convert it into an invariant-mass ratio is now available.

## Physical branch-mass ratio

The proof below imports only the separate endpoint-density theorem. Conversely,
that theorem imports from this file only the independently proved branch
geometry and endpoint-length-ratio corollary above, not this mass section.
Thus the dependency is non-circular.

The exact endpoint-density theorem proves

\[
\frac{d\mu_{\rm ac}}{dx}(-\rho+t)
=\frac{h(0)}{\sqrt2\,U_c}t^{-1/2}+O(1),
\qquad t\downarrow0,
\qquad h(0)>0.
\]

Writing $C=h(0)/(\sqrt2\,U_c)$, one has

\[
\mu_{\rm ac}(C_{2n}(J))
=\int_{\delta_n}^{\delta_{n-1}}
\bigl(Ct^{-1/2}+O(1)\bigr)\,dt
=2C\bigl(\sqrt{\delta_{n-1}}-\sqrt{\delta_n}\bigr)
+O(\delta_{n-1}).
\]

Since $\delta_{n+1}/\delta_n\to\lambda$, it follows that

\[
\frac{\mu_{\rm ac}(C_{2n+2}(J))}
     {\mu_{\rm ac}(C_{2n}(J))}
\longrightarrow
\sqrt\lambda
=\frac{1}{2U_c(U_c-1)}.
\]

Thus the legacy value near $0.596$ is a proved asymptotic physical-mass ratio,
not merely a conditional clue. This does not assert an exact finite-order
geometric law.

## Certified finite prefix

The accompanying implementation uses an exact rational enclosure of $U_c$,
outward rational square-root bounds based on integer `isqrt`, and proves strict
separation of the first 154 endpoint intervals. This certifies the branch
prefix through original return time 308. It is a reproduction check for the
all-order proof, not its logical basis.

The first branches are approximately

| Return | Physical interval |
|---:|---|
| 2 | `(-0.355544333229579, 0)` |
| 4 | `(-0.478789887576554, -0.355544333229579]` |
| 6 | `(-0.520945357858511, -0.478789887576554]` |
| 8 | `(-0.535655847272196, -0.520945357858511]` |
| 10 | `(-0.540842944634170, -0.535655847272196]` |
| 12 | `(-0.542679545272854, -0.540842944634170]` |

## Claim boundary

This theorem certifies the physical branch alphabet, its full finite-word
language, the asymptotic length geometry of the physical branch partition, and
the mass-ratio corollary supplied by the separate exact endpoint-density
theorem. It does not assert realization of every infinite symbolic sequence,
give a closed form for the finite branch masses or $h(0)$, choose the modeled
tower weights, define an $s$-dependent Fredholm determinant, or create an
arithmetic prime correspondence.
