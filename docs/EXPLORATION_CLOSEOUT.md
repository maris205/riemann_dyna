# Exploration close-out: clues, obstructions, and handoff

The project now treats the exact-(U_c) Logistic polar family as the primary
stable line.  Other families remain valuable, but their reusable content is
organized as structural clues and obstructions rather than as competing main
narratives.

## Reusable clues

### CLUE-A4-002 — signed/complex connected renewal

The next structurally meaningful object should be a connected, non-Selberg,
countable multi-channel renewal grammar.  Its roof must be target-free and its
signed/complex weights must come from an intrinsic finite-group or unitary
cocycle, not fitted phases.  Before any divisor comparison, prove a
right-half-plane zero-free theorem and a same-ledger continuation theorem.

This clue is motivated by the sequence:

- finite-state suspensions: wrong (O(T)) divisor count (`OBR-005`);
- finite-index Selberg/Mayer objects: wrong \(\Omega(T^2)\) count (`OBR-006`);
- positive connected renewal: an extra real zero in `(1,2)` (`OBR-017`).

It is a design constraint, not yet a mathematical candidate.  Do not allocate
an identifier until grammar, cocycle, function space, clock, normalization, and
determinant convention are explicit.

### CLUE-A4-001 — multi-chart Hénon/FIO phase calculus

TH-0001 demonstrates exact symplecticity, a same-order unitary FIO lift, and a
real on-shell caustic.  The next legitimate reopening is a source-locked
multi-chart phase/Maslov transition ledger.  Until that exists, do not compute
spectra or determinants.  The low-depth reversibility obstruction remains
scoped to the audited subclasses.

### CLUE-A4-003 — intrinsically normalized magnetic graph

QG-0001 proves that a harmonic tower can produce the (K\log K) exponent and a
natural compact-resolvent operator, but its exact coefficient is fixed by the
base total length and is wrong.  Reopen only with a new graph grammar or
component law whose normalization is fixed before target data; never rescale
the existing tower after seeing the mismatch.

### CLUE-A1-009 — coprime renewal boundary

COPRIME-0001 supplies a useful trace-class and cycle-ledger pattern, together
with a punctured \(\det_2\) scalar representation.  Its original counting-
measure \(\ell^2\) operator boundary and endpoint zero accumulation are strict
obstructions.  Reopening requires a genuinely new function space or determinant
with its own source lock.

## Reusable obstructions

The authoritative registry remains `docs/obstruction_registry.md`.  The most
important close-out boundaries are:

| ID | Structural lesson |
|---|---|
| OBR-005 | Finite-state, finite-roof determinants have only `O(T)` fixed-strip zeros. |
| OBR-006 | Direct Selberg determinants from finite-area modular covers have at least `Omega(T^2)` zeros. |
| OBR-007 | Strictly monotone autonomous clocks collapse periodic orbits to the static boundary. |
| OBR-008 | Unit-lattice clocks impose vertical periodicity incompatible with completed-ξ structure. |
| OBR-009 | Exact-(U_c) induced branches are not uniformly expanding in ordinary BV. |
| OBR-011 | The frozen three-kick FIO has a genuine on-shell internal caustic for global single-phase reduction. |
| OBR-012 | Harmonic graph towers do not have the naive ordinary orbit determinant. |
| OBR-013 | The QG exact relative divisor coefficient is immutably wrong under its lock. |
| OBR-014 | The frozen COPRIME \(\ell^2\) kernel is unbounded for `Re(s)<=1`. |
| OBR-015 | The COPRIME scalar determinant has infinitely many positive zeros accumulating at `s=1`. |
| OBR-016 | Incommensurate disconnected bouquets can still have only `O(T)` fixed-strip zeros. |
| OBR-017 | Positive integer-renewal determinants force an extra real zero in `(1,2)`. |

These are scoped results.  They do not prove that every related family fails.

## Handoff

### Primary line: LOG-0001

Status: `ANALYTIC_REVIEW / GO_WITH_LIMITATIONS`; park at the stable theorem
boundary summarized in `docs/LOG0001_STABLE_RESULTS.md`.

Do not:

- search Fredholm roots or compare Riemann zeros;
- infer a prime law from the return grammar;
- turn `1<=ord(D_pol)<=2` into an exact-order or `T log T` theorem;
- invoke Route B.

### Exploration line

The only project-level reopening worth considering is the signed/complex
connected renewal clue above.  The smallest admissible first gate is:

```text
explicit grammar + intrinsic cocycle
 -> same-space nuclear/trace-class determinant
 -> zero-free right half-plane
 -> same-ledger continuation
```

If the object is not explicit or requires fitted phases/target data, classify it
as `NOT_TESTABLE` and stop.  A formal candidate ID is not created at the clue
stage.

### Route-B boundary

No candidate has entered Route B.  Self-adjointness, PT symmetry, GUE
statistics, or a real finite spectrum are not substitutes for B1--B5.

### Source of truth

The source repository remains `riemann_dyna`; the shareable mirror is
`hilbert-polya-structure/logistic_dynamics`.  Historical evidence is preserved,
and the independent `docs/related_programs/prime_dynamics_theory` repository is
not vendored.
