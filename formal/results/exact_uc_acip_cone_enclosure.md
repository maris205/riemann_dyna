# Coarse certified ACIP enclosure at exact $U_c$

## Status

`PROVED` (coarse enclosure)

Source: `CLUE-A1-004` / `P4-LOGISTIC-UC-ACIP-CONE-ENCLOSURE`.

This result depends on the expanding-Markov RPF theorem already audited in
`formal/results/exact_uc_acip_endpoint_density.md`. It does not use a finite
Ulam matrix, a fitted orbit histogram, prime data, or zero data.

## Theorem

Let

\[
u=U_c,
\qquad
u^3-2u^2+2u-2=0,
\qquad
\rho=u-1,
\]

and let $h$ be the full physical invariant density of
$f(x)=1-ux^2$ on $[-\rho,1]$, normalized by $\int h=1$. Then the conditional
$f^2$ density on $A=[-\rho,\rho]$ obeys

\[
0.3067948900660891
<g_A(0)<
0.9965274232713996,
\qquad g_A(0)=2h(0).
\]

\[
0.1533974450330445
<h(0)<
0.4982637116356999.
\]

For the endpoint coefficient

\[
C_h=\frac{h(0)}{\sqrt2\,u},
\]

one has

\[
0.0702656899853137
<C_h<
0.2282361579437252.
\]

Moreover, the qualitative remainder in the endpoint theorem can be made
explicit on a fixed interval:

\[
\boxed{
\left|h(-\rho+t)-C_h t^{-1/2}\right|
\leq \frac{61}{100}
\qquad
\left(0<t\leq\frac1{200}\right).
}
\]

Consequently, if

\[
\delta_n=\rho-r_n,
\qquad
C_{2n}=(-r_n,-r_{n-1}],
\]

then every $n$ with $\delta_{n-1}\leq1/200$ satisfies

\[
2C_-\left(\sqrt{\delta_{n-1}}-\sqrt{\delta_n}\right)
-\frac{61}{100}(\delta_{n-1}-\delta_n)
\leq \mu_{\rm ac}(C_{2n})
\]

and

\[
\mu_{\rm ac}(C_{2n})
\leq
2C_+\left(\sqrt{\delta_{n-1}}-\sqrt{\delta_n}\right)
+\frac{61}{100}(\delta_{n-1}-\delta_n),
\]

where the lower bound is replaced by zero if its displayed expression is
negative, and $C_-,C_+$ are the certified endpoint-coefficient bounds above.
The accompanying artifact applies these inequalities to $C_{12}$,
$C_{14}$, $C_{16}$, and $C_{18}$ using exact rational endpoint intervals.

## Proof

### 1. Frozen polar transfer operator

Put

\[
I=[-\pi/2,\pi/2],
\qquad
q(\theta)=\rho\sin\theta,
\]

and use the reflected two-iterate map from the endpoint theorem,

\[
G=q^{-1}\circ(-f^2)\circ q.
\]

It has two full inverse branches $\phi_\pm$. If

\[
a_\pm(\eta)=|\phi_\pm'(\eta)|,
\]

its Perron-Frobenius operator is

\[
(\mathcal L v)(\eta)
=\sum_{\sigma\in\{+,-\}}
a_\sigma(\eta)v(\phi_\sigma(\eta)).
\]

The operator preserves Lebesgue integral. Its unique invariant probability
density $w$ therefore satisfies

\[
\int_I w(\theta)\,d\theta=1.
\]

The normalization ledger is

\[
g_A(0)=\frac{w(0)}{\rho},
\qquad
h(0)=\frac{g_A(0)}2=\frac{w(0)}{2\rho}.
\]

### 2. Explicit contraction and distortion bounds

For a target angle $\eta$, define

\[
t=t(\eta)
=\sqrt{\frac{1+\rho\sin\eta}{u}}.
\]

Then $\rho\leq t\leq1$, and direct simplification of the inverse-branch
Jacobian gives

\[
a_+(\eta)=a_-(\eta)
=\frac14\frac{\sqrt{(1+t)(\rho+t)}}{t}.
\]

Its logarithmic derivative with respect to $t$ has magnitude

\[
E(t)
=\frac1t-\frac1{2(1+t)}-\frac1{2(\rho+t)}.
\]

The numerator after putting this over the positive denominator
$2t(1+t)(\rho+t)$ is $2\rho+(1+\rho)t$, so $E(t)>0$ on the whole
interval.

Since

\[
E'(t)
=-\frac1{t^2}
+\frac1{2(1+t)^2}
+\frac1{2(\rho+t)^2}<0,
\]

the inequality follows directly from $t>0$: each positive term satisfies
$t^2/[2(1+t)^2]<1/2$ and $t^2/[2(\rho+t)^2]<1/2$. Therefore one has

\[
E(t)\leq E(\rho)
=\frac3{4\rho}-\frac1{2u}<\frac{11}{10}.
\]

Also

\[
|t'(\eta)|^2
=\frac{(1-z)(u(1+z)-2)}{4uz},
\qquad z=t^2.
\]

The derivative of the numerator quotient before the factor $1/(4u)$ is

\[
-\frac{uz^2+u-2}{z^2}.
\]

Using $u\rho^2=2-u$, its unique maximum on
$z\in[\rho^2,1]$ occurs at $z=\rho$. Hence

\[
\max|t'|^2
=\frac{\rho(u^2-2)}4<\frac1{16}.
\]

It follows that

\[
D:=\sup_\eta|\partial_\eta\log a_\pm(\eta)|
<\frac{11}{40}<\frac3{10}.
\]

The exact inverse-branch contraction from the endpoint theorem is

\[
\kappa=\sup|\phi_\pm'|=\frac{u^2}{4}<\frac35.
\]

All strict algebraic inequalities in this step are certified using the
100-digit sign bracket for $u$ in the audit artifact.

### 3. A forward-invariant log-Lipschitz cone

For $A>0$, let

\[
\mathcal C_A
=\left\{v>0:
|\partial_\theta\log v|\leq A
\right\}.
\]

If $v\in\mathcal C_A$, every positive summand in $\mathcal Lv$ has
logarithmic derivative bounded by

\[
D+\kappa A.
\]

The logarithmic derivative of a positive sum is a pointwise convex
combination of the logarithmic derivatives of its summands. Therefore

\[
\mathcal L(\mathcal C_A)
\subseteq \mathcal C_{D+\kappa A}.
\]

With the frozen rational bounds

\[
D_* =\frac3{10},
\qquad
\kappa_* =\frac35,
\qquad
A_* =\frac34,
\]

one has

\[
D_*+\kappa_*A_*=A_*.
\]

Thus $\mathcal C_{3/4}$ is forward invariant. A positive constant density
belongs to this cone. The primitive expanding-Markov RPF convergence already
proved for $G$ implies that its normalized iterates converge to $w$; closure
of the cone gives

\[
|\partial_\theta\log w|\leq\frac34.
\]

This step is the infinite-dimensional error control. It does not infer an
infinite-dimensional bound from a finite stationary-vector residual.

### 4. Pointwise density enclosure

Let $L=\pi/2$ and $A=3/4$. The cone inequality gives

\[
w(0)e^{-A|\theta|}
\leq w(\theta)
\leq w(0)e^{A|\theta|}.
\]

Integrating and using $\int_Iw=1$ yields

\[
\frac{A}{2(e^{AL}-1)}
\leq w(0)
\leq
\frac{A}{2(1-e^{-AL})}.
\]

The 100-digit bracket for $\pi$, outward decimal rounding, and the certified
algebraic bracket for $\rho$ then give the stated intervals for $w(0)$,
$g_A(0)$, $h(0)$, and $C_h$. In particular, the conditional and full
normalizations are never interchanged.

### 5. Explicit endpoint remainder

The cone bound and normalization also give

\[
\sup_I w<\frac95.
\]

For $|x|\leq x_0=1/20$, put

\[
d(x)=\sqrt{\rho^2-x^2}.
\]

The root bracket gives $d(x)>27/50$. Up to the harmless reflection used in
the polar proof,

\[
h(x)=\frac{w(\arcsin(x/\rho))}{2d(x)}.
\]

Consequently

\[
|h'(x)|
\leq
\frac{(3/4)(9/5)}{2d(x)^2}
+\frac{|x|(9/5)}{2d(x)^3}
<\frac{27}{10}.
\]

Now let $0<t\leq1/200$ and write

\[
a_t=\sqrt{1-\frac tu},
\qquad
s=1-a_t,
\qquad
z=\sqrt{\frac su}.
\]

The frozen inequalities imply $a_t>499/500$ and $z<1/20$. The two-preimage
Perron-Frobenius equation near $1$ therefore gives

\[
\left|
h(1-s)-\frac{h(0)}{\sqrt{us}}
\right|
\leq\frac{27}{10u}.
\]

At the left endpoint there is one physical preimage, so

\[
h(-\rho+t)=\frac{h(a_t)}{2ua_t}.
\]

Using

\[
s=\frac{t}{u(1+a_t)}
\]

shows that the leading factor before $t^{-1/2}$ is

\[
\frac{h(0)}{2u}
\frac{\sqrt{1+a_t}}{a_t}.
\]

For $H(a)=\sqrt{1+a}/a$,

\[
|H'(a)|
=\frac{a+2}{2a^2\sqrt{1+a}}<\frac{11}{10}
\qquad(a\geq499/500).
\]

Together with $h(0)<1/2$, $u>3/2$, and
$\sqrt t<71/1000$, the two remainder terms obey

\[
\frac{27/10}{2u^2a_t}
+\frac{h(0)(11/10)\sqrt t}{2u^2(1+a_t)}
<\frac{61}{100}.
\]

This proves the explicit endpoint remainder.

### 6. Finite branch masses

The coordinate $t=x+\rho$ identifies $C_{2n}$ with
$[\delta_n,\delta_{n-1})$. Integrating the preceding pointwise remainder
gives

\[
\left|
\mu_{\rm ac}(C_{2n})
-2C_h(\sqrt{\delta_{n-1}}-\sqrt{\delta_n})
\right|
\leq
\frac{61}{100}(\delta_{n-1}-\delta_n)
\]

whenever $\delta_{n-1}\leq1/200$. Substitution of the exact rational
endpoint intervals from the first-return support audit proves the displayed
finite-mass enclosures in the artifact. ∎

## Error ledger

The six required numerical categories are frozen explicitly:

1. **Discretization:** not used; the cone argument covers the full closed
   theta interval.
2. **Truncation:** not used; no finite branch or operator truncation enters the
   density enclosure.
3. **Rounding:** algebraic gates use exact rational arithmetic; displayed
   transcendental intervals are computed at 180 digits and widened outward to
   40 decimal places. The 100-digit pi bracket is independently certified by
   Machin's identity and alternating series.
4. **Normalization:** $w$, $g_A$, and $h$ are converted explicitly, with
   $g_A=2h$ on the physical band.
5. **Iteration stopping:** not used; no stationary-vector iteration or residual
   is used as evidence.
6. **Resolvent/tail:** not used; the forward-invariant log-Lipschitz cone gives
   a direct global bound instead of a truncated resolvent estimate.

The inverse-branch formula, the 100-digit root interval, and the exact
endpoint recursion are separately checked. Finally, the pointwise $61/100$
remainder is integrated over each sealed branch length to obtain the finite
mass rows.

## Claim boundary

Established:

- a coarse, target-free, rigorous enclosure of $h(0)$ and $C_h$;
- an explicit endpoint remainder on $0<t\leq1/200$;
- rigorous absolute-mass intervals for four finite physical branches.

Not established:

- a sharp interval-Ulam enclosure or a certified finite-rank resolvent;
- an exact finite-order geometric mass law or exponential remainder;
- a primitive-prime orbit law, an $s$-dependent Fredholm determinant,
  quantization, Route B, Hilbert-Pólya, or RH.
