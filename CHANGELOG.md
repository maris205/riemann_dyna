# Changelog

Repository-backed research status changes are recorded here. Detailed evidence
and reproduction commands remain in `docs/research_log.md` and `HP_HANDOFF.md`.

## 2026-08-04

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
  density theorem. The stronger exponential-remainder statement remains
  `OPEN`, and the legacy ordinary-`BV` proof remains `REFUTED` under
  `OBR-009`.
- Kept the parent Route-A audit at
  `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` / `REVISE`; Route B remains closed.
- Locked the Baladi–Smania cross-check to corrected equation (1.1) in the 2023
  supplement to arXiv:2008.01654v4.
- Hardened the reproducible audit with an independent chain-rule ledger,
  exact inverse-branch residuals, a 100-digit root bracket, input hashes, and
  byte-identical CLI reproduction.

Source state: `84111b3f436ed1e8111c871719e32b70a4def098`.
