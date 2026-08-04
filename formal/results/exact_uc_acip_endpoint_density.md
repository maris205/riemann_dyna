# Exact endpoint density and physical branch-mass ratio at $U_c$

## Status

`PROVED`

Source: `CLUE-A1-004` / `P4-LOGISTIC-UC-ACIP-ENDPOINT-DENSITY`

External theorem input: Jiang–Ruelle (2005), the opening Main Theorem setup,
Assumption A, and `Properties of L`, for an analytically expanding Markovian
unimodal interval map. The spike coefficient is independently cross-checked by
Ruelle (2009), Theorem 9 and Remark 16(a), and by the corrected equation (1.1)
in the 2023 supplementary note to Baladi–Smania, arXiv:2008.01654v4. See
`docs/literature/exact_uc_acip_density_sources.md`.

## Theorem

Let $u=U_c$ be the unique real root of

\[
u^3-2u^2+2u-2=0,
\]

set

\[
\rho=u-1,
\qquad
f(x)=1-ux^2,
\qquad
J=[-\rho,1],
\]

and let $\mu_{\rm ac}$ be the physical absolutely continuous invariant
probability of $f$ on $J$. Then $\mu_{\rm ac}$ exists, is unique, and has full
support $J$.

There is a canonical density representative

\[
h=\frac{d\mu_{\rm ac}}{dx}
\]

which is locally Lipschitz in a neighborhood of $0$ and satisfies

\[
0<h(0)<\infty.
\]

At the left endpoint of the physical core,

\[
\boxed{
h(-\rho+t)
=\frac{h(0)}{\sqrt2\,u}\,t^{-1/2}+O(1)
\qquad(t\downarrow0).
}
\]

In particular,

\[
h(-\rho+t)=C t^{-1/2}(1+o(1)),
\qquad
C=\frac{h(0)}{\sqrt2\,U_c}>0.
\]

For the physical first-return branches from the exact support theorem,

\[
C_2=(-r_1,0),
\qquad
C_{2n}=(-r_n,-r_{n-1}]
\quad(n\ge2),
\]

one consequently has

\[
\boxed{
\frac{\mu_{\rm ac}(C_{2n+2})}
     {\mu_{\rm ac}(C_{2n})}
\longrightarrow
\frac{1}{2U_c(U_c-1)}
=\frac{U_c^2}{4}
}
\]

and the common value is

\[
0.5957439419765593735\ldots.
\]

## Proof

### Step 1 — Algebraic identities and the two-band map

Substituting $u=1+\rho$ into the defining polynomial gives

\[
\rho^3+\rho^2+\rho-1=0.
\]

It follows that

\[
u\rho^2=1-\rho.
\]

The same polynomial also gives

\[
u^3\rho=u^3(u-1)=u^4-u^3=2.
\]

The exact band swap is

\[
A=[-\rho,\rho],
\qquad
B=[\rho,1],
\qquad
f(A)=B,
\qquad
f(B)=A.
\]

On $A$, define

\[
T=f^2|_A.
\]

Direct expansion yields

\[
T(x)=-\rho+2u^2x^2-u^3x^4.
\]

Both monotone branches of $T$ map onto $A$, but $T'(0)=0$. The next step
removes this quadratic cusp without changing the invariant-measure problem.

### Step 2 — A uniformly expanding full-branch coordinate

Let $R(x)=-x$ and set

\[
S=R\circ T\circ R=-T
=\rho-2u^2x^2+u^3x^4.
\]

Thus $S$ has two full branches on $A$, with

\[
S(0)=\rho,
\qquad
S(\pm\rho)=-\rho.
\]

Use the increasing coordinate

\[
q(\theta)=\rho\sin\theta,
\qquad
-\frac\pi2\leq\theta\leq\frac\pi2,
\]

and define, branchwise,

\[
G=q^{-1}\circ S\circ q.
\]

Each of the intervals $[-\pi/2,0]$ and $[0,\pi/2]$ is mapped
monotonically onto the full interval $[-\pi/2,\pi/2]$.

Two exact factorizations control the endpoint coordinates:

\[
\rho-S(x)=u^2x^2(2-ux^2),
\]

\[
\rho+S(x)=u^3(1-x^2)(\rho^2-x^2).
\]

They show that the square-root singularities of $q^{-1}=\arcsin(x/\rho)$
cancel the quadratic contacts of $S$ at the branch endpoints. Consequently
each branch of $G$ extends real-analytically to its closed branch interval.

Since $q'(\theta)^2=\rho^2-x^2$ for $x=q(\theta)$,

\[
|G'(\theta)|^2
=\frac{S'(x)^2(\rho^2-x^2)}{\rho^2-S(x)^2}.
\]

Using the two factorizations and

\[
S'(x)=-4u^2x(1-ux^2),
\]

this becomes

\[
|G'(\theta)|^2
=\frac{16}{u}
\frac{(1-ux^2)^2}{(2-ux^2)(1-x^2)}.
\]

Put $y=x^2$. Apart from a positive denominator, the derivative with respect
to $y$ of the last rational factor has numerator

\[
-(uy-1)(u^2y-3u+2).
\]

For $0\leq y\leq\rho^2$, one has

\[
uy\leq u\rho^2=1-\rho<1,
\]

and

\[
u^2y-3u+2
\leq u^2\rho^2-3u+2
=2-u-u^2<0.
\]

Therefore $|G'|^2$ decreases with $x^2$, and its minimum occurs at
$|x|=\rho$. Substitution gives

\[
\inf|G'|
=\frac4{u^2}
=2u\rho
>1.
\]

The equality uses $u^3\rho=2$, and the strict inequality follows from
$u<2$.

Here are the Jiang–Ruelle hypotheses explicitly. The polynomial $S$ is real
analytic, and

\[
S'(x)=-4u^2x(1-ux^2).
\]

Since $ux^2\leq u\rho^2=1-\rho<1$ on $A$, its unique critical point is
$0$, and it is nondegenerate because $S''(0)=-4u^2\ne0$. Moreover,

\[
S(0)=\rho,
\qquad
S^2(0)=S(\rho)=-\rho,
\]

so $A=[S^2(0),S(0)]$, and the postcritical orbit is the finite orbit

\[
0\longmapsto\rho\longmapsto-\rho\longmapsto-\rho.
\]

The endpoints $\pm\rho$ are polar and the common branch endpoint $0$ is
nonpolar. The coordinate $q(\theta)=\rho\sin\theta$ has the required
quadratic contact at the polar endpoints and a nonzero derivative at the
nonpolar endpoint. The two exact factorizations above show directly that the
two branches of $G$ extend real-analytically through every doubled endpoint.
Each branch covers the full coordinate interval, hence both Markov intervals;
the Markov adjacency matrix has every entry equal to one and is primitive.

Finally, the displayed bound $\inf|G'|>1$ makes every inverse branch strictly
contracting on the real Markov intervals. Its real-analytic extension is
holomorphic on a complex neighborhood. By continuity and the strict
contraction margin, sufficiently thin bounded complex neighborhoods can be
chosen so that each inverse branch maps the closure of its target
neighborhood compactly inside its source neighborhood. This is precisely
Assumption A of Jiang–Ruelle (2005).

The opening Main Theorem setup and `Properties of L` in that paper therefore
give a unique **absolutely continuous** $G$-invariant probability $\nu_G$.
Its density $w$ is strictly positive and branchwise real analytic. Membership
in the paper's space $H_1$ makes the two values agree at the nonpolar partition
point $0$. Consequently

\[
w(\theta)=w(0)+O(|\theta|)
\qquad(\theta\to0),
\]

and

\[
0<w(0)<\infty.
\]

Push $\nu_G$ forward by $q$ and then by $R$. This gives the unique
$T$-invariant absolutely continuous probability $\mu_A$ on $A$. Its density
is locally Lipschitz and strictly positive near $x=0$ because
$q'(0)=\rho>0$.

Finally define

\[
\mu_{\rm ac}
=\frac12\bigl(\mu_A+f_*\mu_A\bigr).
\]

Since $f_*^2\mu_A=T_*\mu_A=\mu_A$, this measure is $f$-invariant. Its two
terms have supports $A$ and $B$, respectively, so its support is $J$ and its
density is locally Lipschitz and strictly positive near $0$. On $A$, if
$g_A=d\mu_A/dx$, the normalization ledger is

\[
h=\frac12g_A,
\qquad
g_A=2h.
\]

Uniqueness follows in the other direction. Any absolutely continuous
$f$-invariant probability gives equal mass to the two bands, and its
normalized restriction to $A$ is a $T$-invariant absolutely continuous
probability. The uniqueness of $\mu_A$ therefore forces the displayed
$\mu_{\rm ac}$.

Jiang–Ruelle also gives ergodicity of $\nu_G$. Its strictly positive density
is equivalent to Lebesgue measure, so its basin has full Lebesgue measure.
Conjugacy and reflection give the same statement for $\mu_A$ under $T$;
alternating the two bands then gives a full-Lebesgue basin for $\mu_{\rm ac}$
under $f$. Thus the named acip is physical, not merely invariant.

### Step 3 — Exact Perron–Frobenius endpoint coefficient

For $y<1$, write

\[
a(y)=\sqrt{\frac{1-y}{u}}.
\]

The physical preimages of $y$ are selected by the core $J$. For
$-\rho<y<\rho$, only $a(y)$ lies in $J$; the negative preimage is less than
$-\rho$. For $\rho<y<1$, both $a(y)$ and $-a(y)$ lie in $J$. Hence the
Perron–Frobenius equation is

\[
h(y)=\frac{h(a(y))}{2u\,a(y)}
\qquad(-\rho<y<\rho),
\]

and

\[
h(y)=\frac{h(a(y))+h(-a(y))}{2u\,a(y)}
\qquad(\rho<y<1).
\]

Let $s\downarrow0$. Since $a(1-s)=\sqrt{s/u}$ and $h$ is locally Lipschitz
near zero,

\[
h(1-s)
=\frac{2h(0)+O(\sqrt{s})}{2\sqrt{us}}
=\frac{h(0)}{\sqrt u}s^{-1/2}+O(1).
\]

Now let $t\downarrow0$ and put

\[
a_t=a(-\rho+t)=\sqrt{1-\frac tu}.
\]

There is only one physical preimage, and

\[
1-a_t=\frac{t}{u(1+a_t)}
=\frac{t}{2u}(1+O(t)).
\]

Applying the preceding asymptotic at $1$ gives

\[
h(a_t)
=\frac{h(0)}{\sqrt u}(1-a_t)^{-1/2}+O(1)
=h(0)\sqrt2\,t^{-1/2}+O(1).
\]

Dividing by $2ua_t=2u+O(t)$ yields

\[
h(-\rho+t)
=\frac{h(0)}{\sqrt2\,u}t^{-1/2}+O(1).
\]

The leading coefficient is strictly positive. The point $-\rho$ occurs only
once in the postcritical orbit, so no second spike is present there to alter
or cancel this coefficient.

### Step 4 — Physical branch-mass ratio

This step depends only on the independently proved branch geometry and
endpoint-length-ratio corollary in
`formal/results/exact_uc_first_return_support.md`. It does not use that
document's later acip or mass statements, so the documentation dependency is
not circular.

Let

\[
\delta_n=\rho-r_n.
\]

The exact first-return support theorem already proves

\[
\frac{\delta_{n+1}}{\delta_n}
\longrightarrow
\lambda
=\frac{1}{4u^2\rho^2}.
\]

The coordinate $t=x+\rho$ sends $C_{2n}$ to
$[\delta_n,\delta_{n-1})$ up to the immaterial endpoint convention. With

\[
C=\frac{h(0)}{\sqrt2\,u},
\]

the endpoint asymptotic gives

\[
\mu_{\rm ac}(C_{2n})
=2C\bigl(\sqrt{\delta_{n-1}}-\sqrt{\delta_n}\bigr)
+O(\delta_{n-1}).
\]

Because $0<\lambda<1$, the error is lower order than the displayed main
term. Therefore

\[
\frac{\mu_{\rm ac}(C_{2n+2})}
     {\mu_{\rm ac}(C_{2n})}
\longrightarrow
\sqrt\lambda
=\frac{1}{2u\rho}.
\]

Finally, $u^3\rho=2$ implies

\[
\frac{1}{2u\rho}=\frac{u^2}{4}.
\]

This proves the theorem. ∎

## Published spike-theorem cross-check

Under the linear conjugacy $y=ux$, the map becomes

\[
F(y)=u-y^2.
\]

Its critical orbit is

\[
0\mapsto u\mapsto-u\rho\mapsto u\rho\mapsto u\rho,
\]

and the fixed postcritical multiplier has magnitude

\[
2u\rho>1.
\]

Thus it is a Misiurewicz–Thurston map. Ruelle's spike formula and the corrected
equation (1.1) in the 2023 supplementary note to Baladi–Smania give, at the
second postcritical point,

\[
\varrho(-u\rho+s)
=\frac{\varrho(0)}{\sqrt{2u}}s^{-1/2}+O(1).
\]

Transforming densities by $h(x)=u\varrho(ux)$ gives exactly

\[
h(-\rho+t)
=\frac{h(0)}{\sqrt2\,u}t^{-1/2}+O(1).
\]

This agrees with the repository-specific proof above.

## Consequences for prior work

- The old global-`BV` description of the raw physical density is false: the
  density has postcritical inverse-square-root spikes.
- The asymptotic even-branch mass ratio is nevertheless true, by the direct
  density argument above.
- The old ordinary-`BV` spectral-gap proof for the unaccelerated first-return
  map remains refuted. This theorem does not restore uniform expansion of that
  map and does not remove `OBR-009`.
- Every physical even branch has positive $\mu_{\rm ac}$ mass
  unconditionally; the earlier full-support-acip hypothesis is now discharged.

## Claim boundary

Established:

- existence, uniqueness, and full support of the exact-$U_c$ physical acip;
- finite positive density at the critical point;
- the exact leading endpoint singularity and its positive coefficient;
- the asymptotic physical branch-mass ratio.

Not established:

- a closed form for $h(0)$ or for the absolute branch masses;
- an exact finite-$n$ geometric law;
- a prime-orbit correspondence or von-Mangoldt repetition weight;
- an $s$-dependent Fredholm determinant or completed-$\xi$ structure;
- natural quantization, Route B, Hilbert–Pólya, RH, or a physical spectral
  realization.
