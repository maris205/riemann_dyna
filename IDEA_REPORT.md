# Breadth-pivot idea report: intrinsic recurrent Route-A objects

Generated 2026-08-09. This repository-first report records the search-space
decision that follows the frozen Logistic and finite-state obstructions. No
prime table, zero table, or fitted target data is used.

## Landscape and hard exclusions

The exact-`U_c` Logistic polar family now has a same-object entire Fredholm
determinant, a signed trace ledger, an upper order bound, a cancellation-safe
lower-growth theorem, and the interval `1 <= ord(D_pol) <= 2`. It still has no
arithmetic orbit law or natural quantization, so another fixed-point estimate
is not the next project-level task.

Finite-state finite-roof suspensions have an `O(T)` divisor obstruction;
finite-index Selberg/Mayer variants have an `Omega(T^2)` obstruction; and
strictly monotone clock lifts collapse periodic orbits to the static slice.
The next object should therefore be countable, genuinely recurrent, and
mathematically explicit before any target comparison.

## Generated and filtered ideas

### 1. Coprime renewal suspension — selected

Use the countable shift

`Sigma_cop = {(n_k): n_k >= 2, gcd(n_k,n_{k+1}) = 1}`

with roof `tau(n_k) = log(n_0)` and symmetric kernel

`(L_s)_{mn} = 1_{gcd(m,n)=1} (mn)^(-s/2)`.

The cycle weight telescopes to `prod_i n_i^(-s)`. The gcd rule is intrinsic
and does not read a prime table. The cheapest decisive test is a trace-class
decomposition plus an exact primitive-cycle census for periods 1--3. Risk is
high, but a failure would still give a reusable countable-state obstruction.

### 2. Non-Selberg Lüroth renewal map

Use full branches of lengths `1/[n(n+1)]`, derivative clock
`log(n(n+1))`, and a countable disk-algebra transfer operator. It avoids the
modular/Selberg obstruction, but may collapse to a scalar Dirichlet-series
determinant. Hold until the coprime object is screened.

### 3. Intermittent induced suspension

Use an analytic Pomeau--Manneville/LSV-type recurrent base whose induced
branches have an intrinsic logarithmic return clock. The inverse branches and
nuclear function space are not yet frozen. Hold.

### 4. Irrational-holonomy continued-fraction suspension

Add an intrinsic irrational compact-group holonomy to a countable continued-
fraction shift. It may escape the finite-index Selberg subclass, but the
holonomy and determinant domain are not yet canonical. Hold.

### 5--8. Parked or rejected ideas

Squarefree hereditary suspensions risk losing nontrivial periodic points;
the recurrent Logistic redesign is not yet explicit; the harmonic graph tower
is stop-scoped by its divisor coefficient; and the twisted Hénon cusp lacks a
frozen phase space and same-order lift.

## Ranking and decision

| Rank | Idea | Object explicit | Cheapest decisive test | Decision |
|---:|---|---:|---|---|
| 1 | Coprime renewal suspension | yes | trace class + period 1--3 ledger | SELECT |
| 2 | Non-Selberg Lüroth map | yes | determinant/trace reduction | hold |
| 3 | Intermittent induced map | no | branch/domain freeze | hold |
| 4 | Irrational-holonomy continued fraction | no | canonical holonomy | hold |
| 5--8 | squarefree, Logistic redesign, graph, Hénon cusp | no/blocked | object definition | park |

## Selected task

Create `COPRIME-0001-COUNTABLE-TRACE` source lock, then prove or refute only:

1. `L_s` is trace class for `Re(s) > 1` under the frozen symmetric kernel.
2. Trace powers equal the exact coprime cyclic and primitive-repetition ledger.
3. Primitive cycles of periods 1--3 are enumerated without target data.

Do not search Fredholm roots or compare Riemann zeros during this first audit.
