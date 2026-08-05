# Derivation Package

## Target

Derive an autonomous recurrent Logistic construction in which:

1. the distinguished parameter is the exact band-merging point (U_c), not
   its six-decimal approximation;
2. gap symbols come only from first returns of the static map (f_{U_c}) on
   its physical core (J=[1-U_c,1]) to (L_J=[1-U_c,0));
3. every aging block contains exactly as many updates as its gap length;
4. the terminal fibre update uses (U_c) exactly before renewal;
5. the resulting primitive/repeated orbit grammar and determinant boundary
   can be evaluated honestly under Route A.

The target is a structural derivation and falsification package. It does not
fit or inspect prime gaps or Riemann zeros.

## Status

COHERENT EXPLORATORY MODEL / PHYSICAL BRANCH GRAMMAR PROVED

The legacy globally monotone schedule is not recurrent. It becomes a coherent
periodic-orbit object only after two reframings:

- its endpoint is replaced by the exact algebraic Misiurewicz value (U_c);
- its block lengths are restricted to the exact all-even physical first-return
  branches of (f_{U_c}), rather than an arbitrary parity-unconstrained alphabet.

The renewal reset is part of this new autonomous object. It is not claimed to
leave the legacy trajectory unchanged.

## Invariant Object

The invariant object is the full skew product

\[
F:[-1,1]\times\mathcal B\longrightarrow[-1,1]\times\mathcal B,
\]

where the symbol alphabet of (mathcal B) is supplied by the exact all-even
physical return branches of the (U_c) parent. The full two-sided recurrent
completion and its invariant measure remain modeling choices, although every
finite symbol word has a physical open cylinder. The literal ambient interval
`[-1,1]` has additional transient odd branches; they lie outside the
forward-invariant core and have zero mass for every invariant probability.

The parent map is

\[
f_u(y)=1-u y^2,
\]

Its physical forward-invariant core and event set are

\[
J=[1-U_c,1],
\qquad
L_J=J\cap\{y<0\}=[1-U_c,0).
\]

For (y\in L_J), the event gap is the first-return time

\[
\tau_J(y)=\min\{n\ge1:f_{U_c}^n(y)\in L_J\}
\]

when this set is nonempty, with (\tau_J(-\rho)=\infty). Zero is a non-event.
At (u=U_c), the recurrent symbolic construction has
exactly one interval branch symbol (m\ge1) for the even return label

\[
\tau=2m.
\]

The parent first-return gaps are observables, not primitive periodic orbits.
The primitive grammar below belongs to the newly defined recurrent tower. The
full object is not the legacy occupation matrix, a histogram, the ordinary
countable shift, or the tower zeta alone.

## Assumptions

- (U_c) is the unique real root of
  \[
  p(u)=u^3-2u^2+2u-2.
  \]
- Its frozen binary64 representation is
  \[
  U_c=1.5436890126920764.
  \]
- The legacy value `1.543689` is only a rounded value and is not accepted as
  the exact anchor.
- The exact band-swap theorem proves that physical odd branches are empty and
  every even return label has exactly one nondegenerate interval branch.
- One symbol (m\ge1) represents that certified physical branch (L=2m).
- Ambient `[-1,1]` and physical-core return ledgers are kept separate.
- A block of length (L) has updates labelled (j=1,\ldots,L).
- The (j=L) fibre update is evaluated before the base renews.
- The inherited aging constants are frozen as
  \[
  k=6.764850551029437,
  \qquad a_0=100000.
  \]
- The inherited (k) is target-contaminated legacy provenance. It is not
  retuned and supplies no arithmetic evidence.
- The only determinant initially frozen for the full system is its reciprocal
  Artin--Mazur series.
- Prime tables, prime-gap histograms, zero tables, zeta evaluations, USTC data,
  fitted epsilon, empirical transition spectra, and eigenphase matching are
  forbidden.

## Notation

- (U_c): exact algebraic band-merging parameter.
- (U_c^{(6)}=1.543689): rounded legacy value.
- (W): number of legacy warmup updates.
- (N): number of legacy recorded updates.
- (i): zero-based global update index in the legacy kernel.
- (m\ge1): (U_c) first-return branch symbol.
- (L=2m): even gap length and number of fibre updates in one block.
- (j=1,\ldots,L): one-based block age.
- (h(r)=\log^{-2}(a_0+r)).
- (f_\mu(x)=1-\mu x^2).
- \(\omega\in\{1,2,\ldots\}^{\mathbb Z}\): bi-infinite return-symbol word.
- (G): tower time-one map.
- (W_b=(m_0,\ldots,m_{q-1})): cyclic return word.
- (P(W_b)=2\sum_i m_i): tower-time period.
- \(\Phi_{W_b}\): fibre return composition over one full base period.
- (N_G(n)=\#\operatorname{Fix}(G^n)).
- (N_F(n)=\#\operatorname{Fix}(F^n)).

## Derivation Strategy

The derivation separates four ledgers:

1. the exact algebraic (U_c) parent and its (L)-hit gaps;
2. the legacy finite-window index calculation;
3. the recurrent tower and aged fibre;
4. the tower zeta versus the full skew-product determinant.

The route is

\[
\text{algebraic critical point}
\to
\text{left/center/right gap signature}
\to
\text{even-return tower}
\to
\text{exact terminal anchor}
\to
\text{primitive full-orbit lift}
\to
\text{determinant limitation}.
\]

## Derivation Map

1. The postcritical relation derives the exact polynomial for (U_c).
2. The rounded legacy value is proved to lie on the left side of the
   bifurcation by direct subtraction.
3. The exact band swap proves the physical support (S_top^J=2*N) and one
   interval branch for every even label, while ambient support is all of N.
4. The certified physical branches define the tower alphabet (L=2m), excluding
   transient ambient odd branches and the right-parameter odd-gap channel.
5. A one-based block formula makes the terminal update exactly (U_c).
6. The tower has genuine recurrence, so it escapes the strict-monotone-clock
   obstruction `OBR-007`.
7. Continuity of the fibre return map supplies at least one full periodic lift
   over every primitive base orbit.
8. Finite fixed-count bounds give a locally convergent reciprocal
   Artin--Mazur series.
9. The remaining integer lattice clock blocks a completed-ξ interpretation.

## Main Derivation

### Step 1 — Derive the exact critical point

The critical orbit starts at (0):

\[
x_0=0,
\qquad
x_1=1,
\qquad
x_2=1-u.
\]

At the (RLR^\infty) Misiurewicz point, the next iterate lands on the positive
fixed point (u-1):

\[
f_u(1-u)=u-1.
\]

Substituting (f_u(x)=1-u x^2) gives

\[
1-u(1-u)^2=u-1,
\]

or

\[
\boxed{u^3-2u^2+2u-2=0}.
\]

Its derivative is

\[
p'(u)=3u^2-4u+2.
\]

The discriminant of this quadratic is (16-24=-8<0), and its leading
coefficient is positive, so (p'(u)>0) for all real (u). Hence (p) has a
unique real root. That root is (U_c).

At (u=U_c),

\[
0\mapsto1\mapsto1-U_c\mapsto U_c-1\mapsto U_c-1.
\]

This algebraic identity is the anchor definition; the displayed decimal is
only its binary64 implementation value.

The rounded legacy value satisfies

\[
U_c^{(6)}-U_c
=1.543689-1.5436890126920764
=-1.2692076278852937\times10^{-8}.
\]

It is therefore slightly to the left of the true critical point.

### Step 2 — Define the intrinsic (U_c) gap event

Freeze the physical core

\[
J=[1-U_c,1]=[-\rho,1],
\qquad \rho=U_c-1,
\]

and write (L) whenever (y_n\in[-\rho,0)). Zero is a non-event. If

\[
n_0<n_1<n_2<\cdots
\]

are the (L)-hit positions, define

\[
g_r=n_{r+1}-n_r.
\]

These gaps belong to the autonomous (U_c) parent. They are not the spacings
between parameter samples and do not read a prime table.

The exact relation (U_c\rho^2=1-\rho) gives

\[
f([-\rho,\rho])=[\rho,1],
\qquad
f([\rho,1])=[-\rho,\rho].
\]

Thus the two bands swap and a point starting in (L) cannot return at an odd
time. Let (T=f^2) and define its positive inverse branch

\[
\psi(y)=
\sqrt{\frac{1-\sqrt{(1-y)/U_c}}{U_c}},
\qquad
r_0=0,
\qquad
r_{n+1}=\psi(r_n).
\]

Then (r_n\uparrow\rho), and the complete physical branch ledger is

\[
C_2=(-r_1,0),
\qquad
C_{2n}=(-r_n,-r_{n-1}]\quad(n\ge2),
\qquad
C_{2n+1}=\varnothing.
\]

Hence

\[
S_{\rm top}^{J}=2\mathbb N_{\ge1},
\]

with exactly one nondegenerate interval branch per even label. The unique
nonreturning point is (-\rho), which maps to the repelling fixed point (\rho).

On every branch interior,

\[
f^{2n}:\operatorname{int}C_{2n}\longrightarrow(-\rho,0)
\]

is a real-analytic diffeomorphism. Hence every finite word of positive even
return labels has a nonempty open cylinder. The recurrent tower's finite-word
alphabet therefore has proved physical provenance; realization of every
infinite one- or two-sided sequence, the full recurrent completion, its
invariant measure, and its coupling to the aged fibre remain separate modeling
steps.

Writing (\ell_n=|C_{2n}|), the endpoint recursion and the mean-value theorem
also give the exact asymptotic length ratio

\[
\frac{\ell_{n+1}}{\ell_n}
\longrightarrow
\frac{1}{4U_c^2(U_c-1)^2}
=0.35491084440177\ldots.
\]

The invariant-mass theorem is now closed. Reflecting
$T=f^2|_{[-\rho,\rho]}$ and using $x=\rho\sin\theta$ gives a two-full-branch
Markov map $G$ with

\[
\inf|G'|
=\frac4{U_c^2}
=2U_c(U_c-1)
>1.
\]

The expanding-Markov Ruelle--Perron--Frobenius theorem therefore gives the
unique full-support physical acip and a density $h$ which is finite and
strictly positive at zero. The exact physical inverse-branch ledger then gives

\[
h(-\rho+t)
=\frac{h(0)}{\sqrt2\,U_c}t^{-1/2}+O(1),
\qquad t\downarrow0,
\qquad h(0)>0.
\]

Consequently,

\[
\frac{\mu_{\rm ac}(C_{2n+2})}{\mu_{\rm ac}(C_{2n})}
\longrightarrow
\frac1{2U_c(U_c-1)}
=0.59574394197656\ldots.
\]

This is an asymptotic theorem, not an exact finite-$n$ geometric law. A later
target-free, complete Arb polar-cone certificate proves
$0.20655<h(0)<0.40008$ and tighter selected finite branch masses, but it does
not give a closed form, a narrow high-accuracy value, or a quantitative rate.

The domain qualification is essential. On ambient `[-1,1]`, the transient
interval `[-1,-rho)` supplies all odd return labels, so

\[
S_{\rm top}^{[-1,1]}=\mathbb N_{\ge1}.
\]

Every invariant probability gives this transient interval zero mass. The named
physical acip exists, has support (J), and gives every physical even branch
positive mass. Closed forms for the individual finite branch weights are not
computed here.

The corrected claim boundary is therefore:

- on the physical core, odd branches are topologically empty;
- ambient odd branches exist but have zero mass for every invariant measure;
- every physical even label has one positive-length branch;
- the prior proof of asymptotically geometric branch weights is not valid,
  because the unaccelerated first-return map is not uniformly expanding, but
  its asymptotic mass-ratio conclusion is repaired by the direct density
  theorem above;
- the one-dimensional system does not generate the Hardy--Littlewood mod-(3)
  resonance of actual prime gaps.

Thus “prime-like” here means the coarse parity/geometric skeleton, not equality
of the full arithmetic gap law.

### Step 3 — Left/center/right critical controls

The exact center object uses (u=U_c). Nearby parameters are adversarial
controls, not alternate candidate definitions.

For (u=U_c-\delta), the frozen scans test the left-side behavior: the sampled
gap support remains even and its stable finite-sample maximum lies below the
center value on the frozen cutoff. All scanned points have positive Lyapunov
exponent, so this is not evidence of an attracting periodic window.

At (u=U_c), the center test requires zero observed odd-gap mass while the
even support extends beyond every corresponding frozen left control.

For (u=U_c+\delta), the right-side test requires positive odd-gap mass. The
right-side controls open an odd-gap channel. That support contains both odd
primes and odd composites in general; this audit makes no
composite-preference claim.

This is a finite numerical phase-boundary diagnostic. Raw long-tail support
and its maximum depend on cutoff, seed, precision, and the last bits of the
parameter. Only the exact algebraic critical-orbit relation carries theorem
status here. The exact physical all-even branch grammar is now proved; only
the finite left/right parameter diagnostics retain numerical status.

### Step 4 — Diagnose the legacy finite-window endpoint

The legacy kernel uses

\[
i=0,\ldots,W-1
\]

for warmup and

\[
i=W,\ldots,W+N-1
\]

for the (N) recorded updates. The terminal update index is therefore

\[
i_\star=W+N-1.
\]

The legacy compensation

\[
u_{\mathrm{temp}}^{\mathrm{old}}
=U_c^{(6)}-\frac{k}{\log^2(a_0+N)}
\]

anchors the parameter at (i=N), not at (i=i_\star). With

\[
W=2{,}000{,}000,
\qquad
N=10{,}000{,}000{,}000,
\]

the actual final update uses

\[
1.5436887783759317,
\]

which is below even the rounded target (U_c^{(6)}).

The finite global-window repair would be

\[
u_{\mathrm{temp}}^{\mathrm{global}}
=U_c-\frac{k}{\log^2(a_0+W+N-1)}.
\]

This fixes both defects only if (U_c) is the algebraic root, not the rounded
six-decimal value. It still does not create recurrence.

The legacy counter has a second timing fault: it initializes the source bin
before warmup and does not refresh it during warmup. Its first recorded edge is

\[
b(x_0)\to b(x_{W+1})
\]

instead of

\[
b(x_W)\to b(x_{W+1}).
\]

Only that first edge is stale, so a total-count test cannot detect it.

### Step 5 — Build the exact-(U_c) recurrent tower

Let

\[
\mathcal B=
\{(\omega,j):
\omega\in\mathbb N_{\ge1}^{\mathbb Z},
\ 1\le j\le2\omega_0\}.
\]

The symbol (m=\omega_0) represents the certified physical (U_c) return branch
(L=2m). Define

\[
G(\omega,j)=
\begin{cases}
(\omega,j+1),&j<2\omega_0,\\
(\sigma\omega,1),&j=2\omega_0.
\end{cases}
\]

One tower step is one physical update. A block of symbol (m) contains
exactly

\[
L=2m
\]

updates. The ordinary unweighted shift on the countable symbols is not used:
it has infinitely many fixed points at each shift period. The tower-time map
(G) has finite fixed counts at every physical period.

### Step 6 — Exact terminal aging law

For a block of even length (L=2m), define

\[
\boxed{
\mu(j,L)
=U_c+k\left[
\frac1{\log^2(a_0+j)}
-\frac1{\log^2(a_0+L)}
\right],
\quad j=1,\ldots,L.
}
\]

Then

\[
\mu(L,L)=U_c
\]

identically, and for (j<L),

\[
\mu(j,L)>U_c.
\]

The terminal (U_c) update is applied before (G) renews to the next block.
There is no (j=0) update and no (L+1)-st update.

With the frozen constants,

\[
U_c\le\mu(j,L)
<U_c+\frac{k}{\log^2(a_0+1)}
=1.5947261217303264\ldots<2.
\]

Therefore every fibre map (f_{\mu(j,L)}) preserves `[-1,1]` without a
clamp.

The full autonomous map is

\[
F(x,\omega,j)
=\left(1-\mu(j,2\omega_0)x^2,\ G(\omega,j)\right).
\]

### Step 7 — Primitive tower grammar

A cyclic physical-return word

\[
W_b=(m_0,\ldots,m_{q-1})
\]

has physical tower period

\[
P(W_b)=2\sum_{r=0}^{q-1}m_r.
\]

If (W_b) is not a repetition of a shorter cyclic word, its tower orbit has
exact period (P(W_b)). Every block visits at least one aging-interior state
and one exact terminal (U_c) state.

The one-loop return series is

\[
A(z)=\sum_{m\ge1}z^{2m}=\frac{z^2}{1-z^2}.
\]

The tower Artin--Mazur zeta is

\[
\boxed{
Z_T(z)=\frac1{1-A(z)}
=\frac{1-z^2}{1-2z^2}.
}
\]

Consequently

\[
N_G(n)=0\quad(n\text{ odd}),
\]

and

\[
\boxed{
N_G(2r)=2(2^r-1).
}
\]

Primitive and repeated tower orbits are separated by Möbius inversion:

\[
E_G(n)=\sum_{d\mid n}\mu_{\mathrm M}(d)N_G(n/d),
\qquad
\pi_G(n)=\frac{E_G(n)}n.
\]

### Step 8 — Lift every primitive tower orbit to the full system

Expand (W_b) into the ordered parameter schedule for its complete blocks and
let

\[
\Phi_{W_b}=f_{\mu_P}\circ\cdots\circ f_{\mu_1},
\qquad P=P(W_b).
\]

This is a continuous self-map of `[-1,1]`. Hence

\[
\Phi_{W_b}(-1)+1\ge0,
\qquad
\Phi_{W_b}(1)-1\le0.
\]

The intermediate value theorem gives an (x_\ast\in[-1,1]) with

\[
\Phi_{W_b}(x_\ast)=x_\ast.
\]

The full state over (x_\ast) cannot close earlier than (P), because its
tower projection has exact period (P). Thus every primitive tower orbit has
at least one primitive full-space lift.

The signed fibre multiplier is

\[
M_{W_b}(x_\ast)
=\prod_{t=1}^{P}(-2\mu_t x_{t-1}).
\]

Its sign records orientation and is preserved. For the (r)-fold repetition,

\[
M_{W_b^r}(x_\ast)=M_{W_b}(x_\ast)^r.
\]

No von-Mangoldt weight, phase law, or prime correspondence follows from this
identity.

### Step 9 — Full fixed-count bound and determinant ledger

For each base point fixed by (G^n), the (n)-step fibre return is a
polynomial of degree (2^n) with nonzero leading coefficient. It has at least
one and at most (2^n) real fixed points. Therefore

\[
N_G(n)\le N_F(n)\le2^nN_G(n)<4^n.
\]

The full reciprocal Artin--Mazur series

\[
\boxed{
D_{\mathrm{AM},F}(z)
=\exp\left(-\sum_{n\ge1}\frac{N_F(n)}n z^n\right)
}
\]

is coefficientwise finite and its defining logarithm converges absolutely for

\[
|z|<\frac14.
\]

This is not (1/Z_T), not the ordinary countable-shift zeta, not a Fredholm
determinant, and not the legacy matrix determinant.

### Step 10 — Remaining Route-A obstruction

Every tower period is an even integer. If one only writes (z=e^{-s}), any
single-valued continuation of the form

\[
D(s)=H(e^{-s})
\]

satisfies

\[
D(s+2\pi i)=D(s).
\]

A discrete divisor with finitely many zeros in one fundamental strip then has
only (O(T)) zeros up to height (T), not the completed-zeta
(\Theta(T\log T)) count. The exact-(U_c)-anchored model therefore supplies a
genuine recurrent symbolic orbit grammar, but only `A1_WEAK`: its physical
branch support and asymptotic mass ratio are certified, while closed-form or
certified finite-$n$ branch weights, the modeled tower coupling, an arithmetic
primitive-orbit correspondence, and a non-lattice clock are absent. It does
not supply an A2 Riemann clock.

## Remarks and Interpretation

- The user's left/center/right observation becomes a sharp source-lock test:
  left controls have only a finite sampled even support, the exact center has
  the even critical parity skeleton, and right controls open an odd-gap
  channel.
- Using `1.543689` can falsely look “almost correct” at low gap cutoff while
  changing the low-count long tail. No fixed tail endpoint is claimed.
- The renewal alphabet has exact one-branch-per-even-label and finite-word
  provenance from (f_{U_c}). The unrestricted two-sided recurrent completion
  remains a modeling choice. Ambient transient odd branches are a separate
  zero-invariant-mass ledger and are not tower symbols.
- The current symbolic factor captures parity and a geometric envelope. The
  repository's later correction says it lacks internal mod-(3) resonance.
- The exact terminal equality is a block identity independent of a finite
  experiment cutoff.
- The recurrent object escapes `OBR-007`, because its base has nontrivial
  periodic points that traverse aging interiors.
- The natural unaccelerated first-return map is not uniformly expanding:
  every branch has derivative infimum zero at a critical preimage. A future
  operator requires a weighted/cusp-adapted space or a newly frozen accelerated
  inducing domain before any Fredholm claim.

## Boundaries and Non-Claims

- No prime table or prime-gap histogram is read.
- Any “prime-like” language is restricted to the coarse parity/geometric gap
  skeleton already recorded in prior work; full prime-gap equality and any
  composite-preference claim are explicitly denied.
- No Riemann zero is fitted or evaluated.
- The inherited (k) is not independent evidence.
- No complete census of all fibre fixed points is claimed; the exact result is
  existence of at least one full lift per primitive tower orbit.
- The named physical acip has full support, every physical branch has positive
  mass, and the asymptotic mass ratio is proved. A validated sharp-cone
  interval for $h(0)$ and selected finite branch masses is certified; no
  closed form, quantitative rate, or exact finite-order weight law is known.
- No Fredholm, Ruelle, Koopman, or transfer-operator determinant is defined.
- No analytic continuation, functional equation, Gamma factor, trivial-zero
  ledger, or completed-ξ divisor is established.
- No symplectic, contact, scattering, unitary, or self-adjoint lift is defined.
- Route B is not authorized.
- Nothing here proves the Riemann Hypothesis.

## Open Risks

- The old Paper-2 uniform-expansion and ordinary-BV spectral-gap argument is
  refuted by the exact branch endpoints. The mass-ratio conclusion is repaired
  by a direct density theorem, not by restoring that proof.
- A closed form or narrow high-accuracy enclosure for $h(0)$ remains open. The
  complete Arb sharp-cone audit certifies a substantially tighter safe interval
  and four selected finite branch masses, but no quantitative branch-mass
  convergence rate.
- Full fibre-root multiplicities, tangencies, and completeness remain open.
- Logistic critical fibres are noninvertible and not uniformly expanding, so
  standard nuclear transfer-operator theorems do not apply automatically to
  the full skew product.
- The unit lattice clock forces vertical periodicity after (z=e^{-s}).
- A future non-lattice roof must be derived from the same dynamics; choosing it
  from prime or zero data would invalidate the candidate.
