# Changelog

Repository-backed research status changes are recorded here. Detailed evidence
and reproduction commands remain in `docs/research_log.md` and `HP_HANDOFF.md`.

## 2026-08-09

### COPRIME-0001 countable trace and primitive-cycle ledger

- Applied the breadth pivot after the frozen Logistic order interval and
  selected one explicit recurrent countable shift with the intrinsic rule
  `gcd(n_k,n_{k+1})=1`, roof `log(n)`, and symmetric half-roof kernel.
- Added a source lock, exact theorem note, deterministic certificate generator,
  artifact, focused tests, and a versioned Route-A evaluation.
- Proved the target-free trace-class bound on `Re(s)>1` through the Mobius
  rank-one decomposition, and recorded the exact cyclic trace-power and
  primitive-repetition ledger. Periods 1--3 and the sealed Fraction control
  through `k=6` pass without prime/zero data. The focused suite has 10 tests;
  the full repository suite has 283 passing tests.
- Added the exact operator-domain boundary: the frozen matrix is not even
  bounded on `ell^2` for `Re(s)<=1`, as shown by its `e_2` column. Any scalar
  continuation across the line must be proved separately.
- Kept `(A1_WEAK,A2_ANALYTIC_DETERMINANT,A3_PARTIAL_ANALYTIC_STRUCTURE,A4_FAIL)`
  and `ROUTE_A_EXPLORATORY / GO_WITH_LIMITATIONS`. Route B remains closed.
- The gcd grammar is not promoted to a prime-orbit or von-Mangoldt law. The
  next task is only a target-free scalar continuation or barrier audit across
  the exact operator boundary.

Evaluation source state: `3890e0aa1f5acd8228c22f4ed24db2cdde4c88dd` at lock;
the final research commit will freeze the added artifact and documentation.

### LOG-0001 Phragmen--Lindelof order lower bound

- Froze a separate source lock at the same determinant, clock, normalization,
  and matching space. Used only the inherited uniform bound on Re(s)>=2,
  entire-ness, order-at-most-two theorem, and D_pol'(2)>0.0213.
- Proved by a half-plane Phragmen--Lindelof argument that order below one
  would make the translated determinant bounded on the complementary half-plane;
  Liouville then contradicts nonconstancy.
- Certified the target-free scalar majorant K_2=exp(B_2) at 1024-bit Arb and
  passed a focused 7/7 logical/scalar regression.
- Established 1<=ord(D_pol)<=2 while keeping
  (A1_WEAK,A2_ANALYTIC_DETERMINANT,A3_PARTIAL_ANALYTIC_STRUCTURE,A4_FAIL)
  and the target tuple (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL). Route B remains
  closed.
- Applied the breadth rule: the next task must be a new explicit recurrent
  candidate or a reusable obstruction, not another fixed-point estimate for
  LOG-0001.

Evaluation source state:
9b0b09e305579d9ed0ae755b2e499a3bd05a261b; research commit:
d1cfa20c6b69503af95abb96ded893eb19329371. The theorem is a scoped analytic
audit; the lower-growth standalone mirror remains the active shareable paper
stage.

### LOG-0001 cancellation-safe lower growth

- Kept the exact-U_c polar map, intrinsic roof, signed orientation ledger,
  matching space, stadiums, and Fredholm determinant convention unchanged.
- Proved local-uniform differentiation of the complete signed trace logarithm
  on the safe zero-free half-plane and strict positivity of every real-axis
  derivative summand.
- Retained only the exact n=1 pure-left term after the full-ledger positivity
  proof, certifying D_pol'(2)>0.0213 with 1024-bit outward Arb arithmetic and
  an inherited 100-decimal-digit U_c bracket.
- Applied Cauchy's estimate to obtain M_D(R)>0.0213(R-2) for R>2 and
  M_D(R)>0.01065R for R>=4. Together with D_pol(sigma)->1, this proves
  nonconstant/transcendental-entire status and qualitative super-polynomial
  maximum-modulus growth.
- Kept the analytic tuple at
  (A1_WEAK,A2_ANALYTIC_DETERMINANT,A3_PARTIAL_ANALYTIC_STRUCTURE,A4_FAIL)
  and the Riemann-target tuple at
  (A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL). Route B remains closed.
- Added the lower-growth source lock, Route-A evaluation, theorem note,
  target-free certificate, focused tests, and registry/frontier updates.
- Fixed certificate metadata to distinguish working precision from inherited
  input accuracy and independently rechecked the 1024-bit scalar inequality.
- Selected a separate Phragmen--Lindelöf audit for a possible order lower
  bound as the next smallest task; positive/exact order, divisor asymptotics,
  target matching, completed-xi, quantization, and RH remain outside scope.

Evaluation source state:
8cabec587cf0a796f4f004bf5b1b0611de3305f3; research commit:
726e42a93a9fabcf07c4c543c1c5962aa0fa1569; shared mirror commit:
`8fbe914cf4438a5a792f7e87e0c87e3a88292201`.

## 2026-08-08

### LOG-0001 explicit conformal restriction ratios

- Kept the exact map, roof, stadiums, matching space, two-stream expansion,
  and canonical Fredholm determinant unchanged.
- Used the curvature-`-1` Poincare metric and a center--projection--point path
  inside each frozen stadium to prove
  `r_L=r_R<=tanh((500*pi+log(4))/2)=r_*<1`.
- Evaluated the stable quantities `delta_*=1-r_*` and
  `beta_*=-log(r_*)` at 4096-bit outward Arb precision; both begin
  `3.2418512480136249798...e-683`, while ordinary precision would round
  `r_*` to one.
- Replaced the parameterized geometric-product constant by an explicit
  two-stream coefficient bound and certified
  `|D_pol(s)|<=exp(3.45e689+4.20e682*(1+|s|)^2)` for the same determinant.
- Passed an independent hyperbolic-distance and Gaussian-constant audit and a
  target-free `7/7` focused regression. No numerical conformal map,
  determinant value, prime table, or zero table was used.
- Kept the analytic Route-A tuple at
  `(A1_WEAK,A2_ANALYTIC_DETERMINANT,A3_PARTIAL_ANALYTIC_STRUCTURE,A4_FAIL)`
  and the Riemann-target tuple at
  `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`. Route B remains closed.
- Selected only a cancellation-safe lower-growth precheck as the next task;
  exact ratios, sharp type, target roots, and lower divisor asymptotics remain
  outside this checkpoint.

Evaluation source state: `dbb78f10bb3299415e022ecadb20d65e0aac5436`;
research commit: `80107bc8ec2bcb4b5d0dd7a30447c5bc2d075320`;
shared paper-stage mirror: `ce0e3c88a3daa32ccf79f7fdeb9c0b22695bc6f5`.

### LOG-0001 quadratic growth and zero-free half-plane

- Reused the same frozen matching-space determinant and grouped its Taylor
  expansion into exactly two geometric rank-one streams, one per input branch.
- Proved an all-order principal-minor majorant with negative quadratic rank
  exponent `q^2/4-q/2`, yielding
  `|D_pol(s)| <= exp(C0+C1*(1+|s|)^2)` and classical order at most two.
- Applied Jensen with a proved zero-free anchor to obtain `O(R^2)` disk and
  `O(T^2)` fixed-real-strip divisor upper bounds.
- Proved absolute convergence of the actual `lambda=1` trace logarithm and a
  zero-free half-plane
  `Re(s)>log(2)/log(4/U_c^2)=1.3382657903899534...`; each closed
  sub-half-plane has uniform upper and lower determinant bounds.
- Added a target-free 100-digit constant certificate and exact two-stream
  allocation checks through `q=24`; no determinant or Riemann roots were
  computed.
- Kept
  `(A1_WEAK,A2_ANALYTIC_DETERMINANT,A3_PARTIAL_ANALYTIC_STRUCTURE,A4_FAIL)`
  analytically and `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` against the Riemann
  target. Route B remains closed.
- Selected only an explicit conformal-ratio certificate for `r_L,r_R` as the
  next smallest task; exact order, lower growth, and sharp divisor asymptotics
  remain open.

Evaluation source state:
`33986f9633b7f03f2fcc1f6ab914e5e0d69f7050`; research commit: `ec00bcb`;
shared paper-stage mirror: `d5ab4b42e66b357859f3b4de560ea5d02bdcf86d`.

### LOG-0001 full matching-space nuclear Fredholm determinant

- Promoted the exact-$U_c$ polar transfer family to formal candidate
  `LOG-0001` only after proving full order-zero nuclearity on the frozen
  matching space.
- Factored every weighted pullback through a proof-only inner stadium by an
  explicit Riemann-map/Taylor expansion; the family is locally bounded and
  entire in every $p$-nuclear ideal for `0<p<=1`.
- Proved that matching preserves the ambient traces and determinant, and that
  `Delta(lambda,s)=det_Fr(I-lambda*L_s|_B)` is jointly entire with
  `D_pol(s)=Delta(1,s)` entire.
- Proved the exact all-power based-fixed-point trace with denominator
  `1-epsilon_omega*exp(-T_omega)`, retaining signed orientation and the
  correct primitive/repetition ledger.
- Passed a target-free 100-digit regression over all 510 based words of
  lengths one through eight; no Fredholm or Riemann zeros were computed.
- Recorded analytic tuple
  `(A1_WEAK,A2_ANALYTIC_DETERMINANT,A3_PARTIAL_ANALYTIC_STRUCTURE,A4_FAIL)`
  but kept the Riemann-target tuple at
  `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall
  `ROUTE_A_EXPLORATORY / GO_WITH_LIMITATIONS`, with Route B closed.
- Selected only the intrinsic growth-order or high-imaginary-height
  divisor-count theorem as the next task.

Source state: `e3358c3a90ec67c2f1cf8b883107ad0fcf3cc64a`; shared paper-stage mirror:
`e6cf4f21b5d82adaec40cb542d952cf491a0b909`.

## 2026-08-07

### Exact-U_c polar boundary trace

- Proved that `P=-pi/2` is the unique boundary periodic point and that its
  inverse multiplier is `alpha_0=U_c^2/4`.
- Proved the local nuclear weighted-composition traces
  `alpha_0^s/(1-alpha_0)` and
  `alpha_0^(n*s)/(1-alpha_0^n)` for pure-left powers.
- Certified target-free Taylor tails at 100 digits; no half-weight, seam, or
  doubled-copy factor occurs because `P` lies inside the complex stadium and
  belongs only to the left component.
- Kept full matching-space nuclearity, Fredholm determinant existence, target
  zeros, and Route B closed. Route-A remains
  `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` / `REVISE`.

### Exact-U_c half-open partition ledger

- Froze `I_L=[-pi/2,0)` and `I_R=[0,pi/2]` for geometric coding while retaining
  doubled labels for analytic branch bookkeeping.
- Proved the exact boundary graph `P->P`, `Q->P`, `Z->Q`; the partition point
  is preperiodic rather than a boundary periodic orbit.
- Separated geometric quotient multiplicity, doubled cyclic trace words, and
  matching-space analytic traces; matching at zero does not justify dividing
  source-branch contributions by two.

## 2026-08-06

### QG-0001 same-operator relative Fredholm closure

- Froze
  `configs/source_locks/QG-0001-RELATIVE-FREDHOLM.yaml` with the raw
  wavenumber clock and one determinant convention:
  `D_H(k)=det_F(I-k^2 H^{-1})=det_rel(H-k^2,H)`.
- Proved `H^{-1}` is trace class and
  `D_H(k)=product_{n>=1} chi_0(k/n)` normally on compact sets. The repaired
  bond factor requires the forced factorwise counterphase
  `exp(-i*k*L0/n)`; the failed orbit and bond-block products remain separate.
- Certified the exact trace sum
  `Tr(H^{-1})=7.2435653691436857...`, the complete divisor, genus/order/type,
  and the all-order count `(L0/pi)*K*log(K)+O(K)`.
- Added `OBR-013`: the frozen divisor coefficient exceeds the target by
  `2*L0=12.764664694883524...`, which no zero-free factor can repair.
- Recorded analytic A2/A3 progress but set QG-0001 to
  `ROUTE_A_REJECTED` / `STOP_SCOPED`; Route B remains closed.

Source state: `b5ad4c9ce4305cf055a2e6a3ae957ba4fda7e90b`.

### QG-0001 base-component characteristic at k=0

- Added the local source lock
  `configs/source_locks/QG-0001-BASE-CHARACTERISTIC.yaml` and a 6-by-6
  sinc-matching characteristic for the frozen n=1 graph.
- Proved the exact same-convention identity
  \(\Delta_{\rm bond}(k)=-(4/3)k^2e^{ikL_0}C_{\rm phys}(k)\). The bond
  determinant therefore has an exact double zero at `k=0`, while
  \(C_{\rm phys}(0)=\sqrt2+\sqrt3+\sqrt5+\sqrt6+\sqrt{15}+3\sqrt{10}>0\),
  so the zero is a plane-wave parametrization artifact.
- Recorded both normalization ledgers: the raw post-`k^2` bond factor has
  first nonconstant coefficient `i*L0`, and the dephased even characteristic
  has \(\chi_0(k)=1-4.4035597019537134\,k^2+O(k^4)\).
- Added exact symbolic and 80-digit numerical gates, including an
  edge-Dirichlet sample. This is a local base prerequisite only; the tower
  determinant and Route B remain closed.

Source state: `af41439b609a5dfb863931ed1e56a0598de5f003`.

### QG-0001 harmonic magnetic graph-tower prefilter

- Froze an asymmetric magnetic lollipop-theta base graph with squarefree
  lengths and exact `1/n` metric tower, without prime/zero tables, fitting,
  unfolding, or spectral rescaling.
- Certified the exact signed primitive/repetition prefix through topological
  period six: `10`, `45`, and `330` primitive oriented orbits at periods
  `2`, `4`, and `6`.
- Proved that the natural direct-sum magnetic Laplacian is self-adjoint with
  compact resolvent and has
  \(N_H(K)=(L_0/\pi)K\log K+O(K)\), while recording that its unfitted leading
  coefficient is too large by the multiplicative factor `2*L_0`.
- Added `OBR-012`: the pendant-bounce Euler factors tend to `1/2`, and the
  explicit standard bond blocks have trace norm tending to `8`; hence the
  naive product has no finite nonzero value and the direct-sum bond operator
  is not trace class.
- Kept the heat/spectral-zeta identity separate from a wavenumber secular
  divisor. Narrowed the antiunitary claim to exclusion of the inherited local
  geometric class; an abstract spectral-basis conjugation necessarily exists.
- Registered Route-A tuple
  `(A1_WEAK, A2_FAIL, A3_FAIL, A4_UNITARY_OR_SCATTERING_CANDIDATE)` /
  `ROUTE_A_EXPLORATORY` with `GO_WITH_LIMITATIONS`. Route B remains closed.

Source state: `ce0d4424a95a9392c9e8755a4a11b1cfcabc0e77`.

### TH-0001 internal phase caustic obstruction

- Added `OBR-011`: the ordered three-kick internal Hessian has determinant
  `15*q1*q2-1` and a nonempty exact caustic at `(1,1/15)`, so no global
  single reduced phase or global Maslov index is available in the current chart.
- Preserved the ordered oscillatory-integral and factorized `L^2(R)` unitary
  ledger; this is a phase-reduction obstruction, not a failure of the quantum
  propagator and not a Route-B result.
- Stopped the phase sub-audit; reopening requires an explicit multi-chart
  caustic-transition convention. Signed classical multipliers remain separate
  from Maslov or magnetic phases.

Source state: `a4cb10640c44559f0520386d9c84e65c9b873134`.

### TH-0001 same-order unitary FIO lift

- Froze `hbar=1`, positive-real Fourier normalization, Lebesgue `L^2(R)`,
  Schwartz core, and the exact same-order factors
  `U_a=F_+M_a`, `U=U_(5/2)U_(3/2)U_(1/2)`.
- Proved exact canonical graphs and everywhere-defined unitarity by
  Plancherel plus modulus-one multiplication; retained the multi-kick kernel as
  an iterated oscillatory integral without a false global single-phase claim.
- Audited `A=F_+C`: it is an involutive antiunitary reversing each kick, but
  fails to reverse the non-palindromic superstep; inherited cyclic clock
  reflections fail as well. Arbitrary nonlinear/non-geometric antiunitaries
  remain open.
- Upgraded only A4 to `A4_NATURAL_QUANTIZATION`; retained
  `(A1_WEAK, A2_FAIL, A3_FAIL)` and `ROUTE_A_EXPLORATORY`/
  `GO_WITH_LIMITATIONS`. Route B, self-adjointness, spectra, determinants, and
  RH remain closed.
- Added evaluation
  `evaluations/route_a/TH-0001/20260806T045554Z.yaml`; focused FIO tests are
  `12/12`, full repository tests `196/196`.

Source state: `836f5880fac6abfb29ee031e1136e24504e2b0a9`.

### TH-0001 target-free three-kick Hénon Route-A prefilter

- Promoted `TH-0001` to the first formal Hénon-family candidate after freezing
  the autonomous superstep
  `G=F_(5/2) o F_(3/2) o F_(1/2)` and its exact source lock.
- Certified exact symplecticity, an explicit inverse and generating function,
  failure of the inherited swap reversor, and exclusion of all affine
  anti-symplectic involutions in the audited class.
- Certified the complete global real primitive-orbit prefix through `G`-period
  two: 4 primitive period-one and 8 primitive period-two orbits, 20 phase
  points total, all hyperbolic; recorded `OBR-010` for the reusable low-depth
  reversibility obstruction.
- Kept the Route-A tuple at
  `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` / `ROUTE_A_EXPLORATORY` with
  `GO_WITH_LIMITATIONS`. The determinant convention is `NOT_OPENED`, arbitrary
  nonlinear reversors remain open, and Route B is closed.
- Added versioned evaluation
  `evaluations/route_a/TH-0001/20260806T024238Z.yaml` and byte-reproducible
  artifact/test gates (`10/10` focused, `184/184` full).

Source state: `fb69649afbda27006d56471c5680b590f90ba43b`.

## 2026-08-05

### RH breadth-first portfolio rule

- Distinguished a candidate-local resume task from the project-level next
  task so a weak Route-A branch can be parked without being discarded.
- Added a mandatory breadth pivot after two stable checkpoints leave both the
  Route-A tuple and main blocker unchanged, unless the next bounded test can
  upgrade a layer or prove a reusable family obstruction.
- Parked the Logistic branch after its non-lattice and frozen-complex-domain
  theorem edges; retained partition-hit trace multiplicity as its local
  resume task.
- Activated `CLUE-A4-001` for the next project-level source lock: exactly one
  explicit target-free Twisted Hénon / kicked-symplectic object, initially
  screened only for autonomous definition, symplecticity, time-reversal, and
  reproducible short UPOs.

### Frozen-radius exact-$U_c$ polar complex branches

- Kept `epsilon=1/1000` unchanged and constructed one common holomorphic
  `t`, `a`, and `Log(a)` on the full union stadium rather than selecting
  separate scalar `sqrt/asin/Log` branches.
- Defined both composite inverse branches as primitives of the same `a`,
  preserving `phi_L'=+a` and `phi_R'=-a`, and proved the exact locked
  `q`-coordinate inverse identity.
- Certified `|a|<0.59626`, logarithm variation below `0.000851`, positive
  real part of `a`, and global univalence of both complex branches.
- Proved all four frozen target/source inclusions with common image radius
  below `0.00059626` and compact margin above `0.00040374`.
- Proved the weighted composition formula is well-defined on the matching
  space for each fixed `s`, but kept endpoint trace multiplicity, nuclearity,
  a Fredholm determinant, target divisors, Route B, and RH open.
- Kept `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` / `REVISE`; this is a proved
  complex-domain structural prior, not an A2 determinant pass.

Source state: `3ae5e23508e27129cfa5910473b944026b904ea3`.

### Exact-$U_c$ polar-roof non-lattice theorem

- Evaluated only the sealed primitive words `R` and `LR` with their full roof
  sums and preserved signed multipliers.
- Proved `alpha=4*(U_c-1)` has an irreducible cubic with norm `2^6`, while the
  `LR` multiplier magnitude has an irreducible degree-nine polynomial with
  norm `2^36`.
- Used common-field norms to reduce every possible rational period relation
  to `beta=alpha^2`, then excluded it exactly via
  `H_U_c(alpha^2)=-8192*(U_c-2)*(2*U_c-3) != 0`.
- Concluded `T_LR/T_R` is irrational and the intrinsic roof `tau=log|G'|` is
  non-lattice; no decimal irrationality or arithmetic target data was used.
- Kept `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`: complex branch inclusion,
  endpoint trace multiplicity, nuclearity, a Fredholm determinant, target
  divisor, quantization, Route B, and RH remain open.

Source state: `36a38f0db16652bf0e0c1459be6c69f6bdafec12`.

### Exact-$U_c$ polar intrinsic-roof source lock

- Froze the doubled two-branch polar Markov map
  `G=q^(-1) o (-f^2) o q` and the intrinsic positive roof
  `tau=log|G'|` without using arithmetic target data.
- Separated one `G` step (`2` physical Logistic iterates) from the suspension
  period `sum tau=log|(G^n)'|`; neither clock may replace the other.
- Froze `epsilon=1/1000`, a two-component matching analytic Banach space, the
  weighted family with potential `-s*tau`, and the sole conditional convention
  `D_pol(s)=det_Fr(I-L_s)`.
- Kept the determinant explicitly conditional: complex branch inclusion,
  nuclearity, non-lattice behavior, and all target comparisons remain open.
- Sealed the next audit to primitive words `R` and `LR` only; Fredholm analysis
  is deferred.
- Clarified lock v2 so only the composite inverse branches are intended to be
  holomorphic, froze the exact conjugacy `H o G=f^2 o H`, made the two-witness
  lattice test one-way, and deferred the partition-hit trace ledger.

Source state: `4d5cd7e346445317d2ed19ef90a484cca09c3588`.

### Quantitative exact-$U_c$ physical branch-mass-ratio rate

- Froze the local cusp-adapted space
  $v(t)=c\,t^{-1/2}+b(t)$ with norm $|c|+\|b\|_\infty$ on
  $0<t\leq1/200$.
- Combined the sharp lower bound for the common endpoint coefficient, the
  explicit cusp remainder, exact endpoint recursion, and one complete Arb
  derivative interval to prove, for every $n\geq6$,
  \[
  \left|\frac{\mu(C_{2n+2})}{\mu(C_{2n})}-\frac{U_c^2}{4}\right|
  \leq\frac{36}{5}\sqrt{\delta_{n-1}}
  <\frac{243}{625}\left(\frac35\right)^{n-6}.
  \]
- Kept the common physical coefficient across adjacent masses; independent
  marginal mass intervals were not divided.
- Added an exact Fraction rate ledger, byte-identical artifact reproduction,
  source hashes, focused tests, and a versioned Route-A evaluation.
- Preserved the original `03:53:48Z` evaluation at source commit `02727fc` and
  added a later superseding evaluation for the direct parent-lock provenance
  correction; the mathematical verdict is unchanged.
- Kept (A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL) / REVISE; the theorem gives
  no arithmetic primitive-orbit law, determinant, quantization, Route B, or
  RH consequence.

Source state: `dbcb58d21ff93ef842df869c177a3ec3e8c0a785` (provenance correction).

### Validated sharp exact-$U_c$ polar-cone enclosure

- Replaced the coarse distortion bound by a complete directed Arb cover of
  $2^{18}$ closed cells, proving `0.17013 < D < 0.17014` at the frozen
  `python-flint 0.9.0` / FLINT `3.6.0` environment and 100-digit precision.
- Proved the sharp invariant-cone identity with slope `42535/101064` and
  certified `0.20655<h(0)<0.40008` and `0.09461<C_h<0.18327`.
- Tightened the positive absolute-mass enclosures for physical returns
  `12,14,16,18`, with sealed endpoint-radius, ordering, and label gates.
- Added source-input hashes, byte-identical CLI reproduction, a six-category
  error ledger, and a versioned Route-A evaluation.
- Kept `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`, parent verdict `REVISE`, and
  Route B closed. No arithmetic target data, determinant, or quantization was
  introduced.

Source state: `f34117824702404fe0837f5811a5465d33cc65de`.

## 2026-08-04

### Exact-$U_c$ polar-cone enclosure

- Added a target-free forward-invariant log-Lipschitz cone certificate for the
  polar proof-coordinate transfer operator.
- Certified coarse intervals for `h(0)`, `C_h=h(0)/(sqrt(2)*U_c)`, and absolute
  masses of physical returns `12,14,16,18`.
- Replaced the qualitative local endpoint remainder by the explicit bound
  `|h(-rho+t)-C_h*t^(-1/2)| <= 61/100` on `0<t<=1/200`.
- Added an exact rational Machin-series check for the frozen 100-digit pi
  bracket and retained a separate six-category error ledger.
- Kept the parent Route-A tuple at
  `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` / `REVISE`; Route B remains closed.
- Explicitly excluded sharp Ulam/resolvent certification, arithmetic orbit
  matching, determinant claims, quantization, and RH conclusions.

Source state: `8f270de6546928385b93e1dd0b8b78c7ffd40ea8`.

### Exact-$U_c$ physical-acip endpoint theorem

- Proved existence, uniqueness, full support, and physicality of the exact-$U_c$
  Logistic acip.
- Proved
  \[
  h(-\rho+t)=\frac{h(0)}{\sqrt2U_c}t^{-1/2}+O(1),
  \qquad h(0)>0,
  \]
  and
  \[
  \frac{\mu(C_{2n+2})}{\mu(C_{2n})}
  \longrightarrow\frac1{2U_c(U_c-1)}=\frac{U_c^2}{4}.
  \]
- Upgraded the physical ratio-limit subclaim of P2-C12 to `PROVED` by a direct
  density theorem. The stronger legacy exact finite-order remainder statement
  remains `OPEN`, while the later adjacent-ratio rate is certified separately;
  the legacy ordinary-`BV` proof remains `REFUTED` under
  `OBR-009`.
- Kept the parent Route-A audit at
  `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` / `REVISE`; Route B remains closed.
- Locked the Baladi–Smania cross-check to corrected equation (1.1) in the 2023
  supplement to arXiv:2008.01654v4.
- Hardened the reproducible audit with an independent chain-rule ledger,
  exact inverse-branch residuals, a 100-digit root bracket, input hashes, and
  byte-identical CLI reproduction.

Source state: `84111b3f436ed1e8111c871719e32b70a4def098`.
