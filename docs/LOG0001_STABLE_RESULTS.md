# LOG-0001 stable results

## Scope

This is the canonical close-out summary for the Logistic-origin line.  It
collects the frozen exact-(U_c) polar Logistic results without replacing the
versioned source locks, Route-A evaluations, certificates, tests, or papers.

The complete evidence remains in the source repository and in the synchronized
mirror:

- `riemann_dyna`: source history and full laboratory;
- `hilbert-polya-structure/logistic_dynamics`: shareable stage archive.

The Logistic numerical notebooks are historical diagnostics.  Their finite
zero matches, fitted schedules, USTC/GUE comparisons, and smoothing choices
are not part of the stable candidate definition.

## Frozen mathematical chain

```text
exact algebraic U_c
  -> physical first-return support and ACIP
  -> polar return map and intrinsic roof tau=log|G'|
  -> non-lattice and complex inverse-branch certificates
  -> half-open partition and boundary trace ledgers
  -> LOG-0001 matching-space nuclear Fredholm determinant
  -> same-object analytic growth and order bounds
```

The anchor is the unique real root

\[
U_c^3-2U_c^2+2U_c-2=0,
\qquad U_c=1.5436890126920764\ldots,
\]

with physical core (J=[1-U_c,1]).  The physical first-return branches have
one nondegenerate interval branch for each positive even return label and no
odd physical branch.  The endpoint/ACIP chain proves the square-root endpoint
density law, positivity and full support of the physical invariant measure,
and the asymptotic physical branch-mass ratio

\[
\frac{\mu(C_{2n+2})}{\mu(C_{2n})}
\longrightarrow
\frac{1}{2U_c(U_c-1)}=\frac{U_c^2}{4}.
\]

These are physical-measure and return-grammar results; they are not prime
weights.

## Stable LOG-0001 theorem package

The frozen polar transfer family acts on the matching space

\[
X=A(U_L)\oplus A(U_R),
\qquad B=\ker[v_L(0)-v_R(0)],
\]

with the intrinsic roof \(\tau=\log|G'|\), signed branch orientation, and
one determinant convention:

\[
D_{\mathrm{pol}}(s)=\det_{\mathrm{Fr}}(I-\mathcal L_s|_B).
\]

The nuclear stage proves order-zero nuclearity, matching-space invariance,
and a jointly entire family

\[
\Delta(\lambda,s)=\det_{\mathrm{Fr}}(I-\lambda\mathcal L_s|_B).
\]

Its exact based-word trace ledger is

\[
\operatorname{Tr}(\mathcal L_s^n)
=\sum_{\omega\in\{L,R\}^n}
\frac{e^{-sT_\omega}}
     {1-\varepsilon_\omega e^{-T_\omega}},
\qquad
\varepsilon_\omega=(-1)^{\#R(\omega)}.
\]

The subsequent same-object analytic results establish:

- a target-free zero-free half-plane
  \(\Re s>\log 2/\log(4/U_c^2)=1.3382657903\ldots\);
- a global quadratic exponential upper bound, hence
  \(\operatorname{ord}(D_{\mathrm{pol}})\le2\);
- an explicit cancellation-safe lower witness
  \(D_{\mathrm{pol}}'(2)>0.0213\), proving nonconstancy and
  transcendental-entire status;
- a half-plane Phragmén--Lindelöf argument giving
  \(1\le\operatorname{ord}(D_{\mathrm{pol}})\le2\).

The relevant shareable stages are:

1. `LOG-0001-NUCLEAR-FREDHOLM`
2. `LOG-0001-GROWTH-ORDER`
3. `LOG-0001-CONFORMAL-RATIO`
4. `LOG-0001-LOWER-GROWTH`
5. `LOG-0001-ORDER-LOWER`

The partition and boundary-trace audits are integrated prerequisites rather
than separate determinant claims.

## Route-A boundary

Analytic tuple:

```text
(A1_WEAK, A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)
```

Riemann-target tuple:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
```

Recommended status: `ROUTE_A_EXPLORATORY / GO_WITH_LIMITATIONS`, parked at a
stable analytic checkpoint.

Established:

- explicit exact-(U_c) physical return and ACIP structure;
- intrinsic non-lattice polar roof and certified complex branch domain;
- same-object entire Fredholm determinant;
- exact signed periodic-word trace ledger;
- target-free growth, zero-free, and order bounds.

Not established:

- a rational-prime primitive-orbit correspondence;
- von-Mangoldt-weighted prime-power traces;
- exact order or sharp (T\log T) divisor asymptotics;
- functional equation, Gamma/trivial-zero completion, or completed-ξ identity;
- natural self-adjoint quantization, Route B, Hilbert--Pólya, or RH.

No Fredholm roots or Riemann zeros should be computed in the close-out stage.

## Reproduction

From the main repository:

```bash
python3 experiments/log_0001_nuclear_fredholm.py --quiet \
  --output artifacts/log_0001_nuclear_fredholm/nuclear_fredholm_certificate.json
python3 -m unittest -v tests/test_log_0001_nuclear_fredholm.py
python3 experiments/log_0001_growth_order.py --quiet \
  --output artifacts/log_0001_growth_order/growth_order_certificate.json
python3 -m unittest -v tests/test_log_0001_growth_order.py
python3 experiments/log_0001_conformal_ratio.py --quiet \
  --output artifacts/log_0001_conformal_ratio/conformal_ratio_certificate.json
python3 -m unittest -v tests/test_log_0001_conformal_ratio.py
python3 experiments/log_0001_lower_growth.py --quiet \
  --output artifacts/log_0001_lower_growth/lower_growth_certificate.json
python3 -m unittest -v tests/test_log_0001_lower_growth.py
python3 experiments/log_0001_order_lower.py --quiet \
  --output artifacts/log_0001_order_lower/order_lower_certificate.json
python3 -m unittest -v tests/test_log_0001_order_lower.py
```

The standalone mirror has the same source-locked project tests and hashes;
source-bound historical tests are explicitly marked in its manifest.

## Next smallest task

Park LOG-0001 at this stable theorem boundary.  Any reopening must define a
structurally new intrinsic signed/complex recurrent object; do not append more
fixed-point estimates or fit determinant roots.
