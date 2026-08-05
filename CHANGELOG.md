# Changelog

Repository-backed research status changes are recorded here. Detailed evidence
and reproduction commands remain in `docs/research_log.md` and `HP_HANDOFF.md`.

## 2026-08-05

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
