# Changelog

Repository-backed research status changes are recorded here. Detailed evidence
and reproduction commands remain in `docs/research_log.md` and `HP_HANDOFF.md`.

## 2026-08-06

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
