# HP-Dynamics Handoff

## Current status

The `CLUE-A2-001` synthetic Fredholm/Euler-product evaluator control is
complete.

- Active clue: `CLUE-A2-001`
- Control ID: `CTRL-0001`
- Formal candidate: `false`
- Infrastructure verdict: `GO_WITH_LIMITATIONS`
- Candidate-scope verdict: `STOP_SCOPED`
- Control-context Route-A tuple:
  `(A1_WEAK, A2_ANALYTIC_DETERMINANT,
    A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)`
- Candidate-context Route-A tuple:
  `(A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`
- Overall candidate interpretation: `ROUTE_A_REJECTED`
- Route B: inactive and not authorized

The latest formal candidate remains `SS-0002`, which is `STOP_SCOPED` under
`OBR-006`. `CTRL-0001` is reusable test infrastructure and must not be renamed
or promoted to `SS-0003`.

The legacy Logistic line remains separately `BLOCKED`: its frozen empirical
phase observable is `STOP_SCOPED`, while Route A is `NOT_TESTABLE`. Reopen it
only with an explicit autonomous slow-variable lift or a chronological
transfer-cocycle/Fredholm determinant under a new source lock.

## Current entry files

- `docs/HP_Dynamics_Project_Entry.md`
- `docs/main_agent_rules.md`
- `.agents/skills/route-a-evaluator/SKILL.md`
- `.agents/skills/route-b-evaluator/SKILL.md`
- `docs/research_clues.md`
- `configs/source_locks/CTRL-0001.yaml`
- `experiments/ctrl_0001_qpochhammer.py`
- `tests/test_ctrl_0001_qpochhammer.py`
- `artifacts/ctrl_0001/route_a_positive_control.json`
- `evaluations/route_a/CTRL-0001/20260803T171847Z.yaml`

Source-lock version 2 is an adversarial-audit clarification: it adds explicit
`D_N`/`D_K` formulas, deterministic-holdout wording, and supplemental
precision/ledger diagnostics. It does not change the object, constants,
rectangle, primary cutoffs, match radius, or frozen thresholds.

## Frozen mathematical object

On

\[
\mathcal H=\ell^2(\{A_+,A_-,B,C\}\times\mathbb N_0),
\]

freeze the analytic diagonal trace-class family

\[
\mathcal L_s e_{c,n}=a_cq_c^ne^{-s}e_{c,n},
\qquad
a_c=e^{\alpha_c+i\theta_c},
\qquad
q_c=e^{-\beta_c},
\]

with channels:

| channel | alpha | beta | theta |
|---|---:|---:|---:|
| `A_plus` | `11/20` | `2/5` | `+pi/3` |
| `A_minus` | `11/20` | `2/5` | `-pi/3` |
| `B` | `9/20` | `1/2` | `pi` |
| `C` | `3/10` | `9/20` | `0` |

The sole determinant ledger is

\[
D(s)=\det_{\rm Fr}(I-\mathcal L_s)
=\prod_c\prod_{n=0}^{\infty}(1-a_cq_c^ne^{-s}).
\]

Keep the following separate:

- `1/D`, a pole ledger;
- `D'/D`, a meromorphic logarithmic-derivative ledger;
- the exponential of a truncated log expansion, which is zero-free and cannot
  be used for root discovery;
- the absolute-value ablation, which is a different determinant.

The object uses a unit roof, `z=exp(-s)`, no affine scaling or unfolding, and no
prime, zero, `zeta`, or `xi` data.

## Frozen scoring region

The open rectangle is

\[
-8/25<\Re s<17/25,
\qquad
|\Im s|<34/5.
\]

Exact roots, used only after discovery for scoring, are

\[
s_{c,n,k}=\alpha_c-n\beta_c+i(\theta_c+2\pi k).
\]

The exact count ledger is:

- total: `22`;
- validation core `|Im(s)|<17/5`: `12`;
- upper deterministic holdout strip: `5`;
- lower deterministic holdout strip: `5`;
- minimum boundary clearance: `0.07`.

Training is empty. No target values are fitted or used as root seeds. The
holdout is deterministic rather than cryptographically sealed because the
synthetic formula is public.

## Strongest evidence

Two independent numerical paths pass:

1. q-binomial channel coefficients, independently checked by the
   Newton/Fredholm trace recurrence, discover polynomial roots in `z` and then
   enumerate all logarithm branches in the rectangle;
2. direct finite-mode products compute argument-principle windings without
   reading the polynomial roots.

The coefficient cutoffs deliberately expose unstable prefixes:

| K | roots | strict matches at `1e-4` | missing | extra | max global assignment error |
|---:|---:|---:|---:|---:|---:|
| 16 | 28 | 6 | 16 | 22 | `0.135492` |
| 20 | 22 | 15 | 7 | 7 | `0.00202999` |
| 24 | 22 | 22 | 0 | 0 | `1.25037e-5` |
| 28 | 22 | 22 | 0 | 0 | `8.89663e-9` |
| 32 | 22 | 22 | 0 | 0 | `7.82564e-13` |

The maximum branch drift from `K=24` to `K=28` is `1.24983e-5`.
The independent coefficient constructions have global scaled defect
`5.96946e-13` through degree 24, and the nominal coefficient conjugation defect
through degree 32 is `1.88072e-13`.

Supplemental `K=28` mpmath audits at 50/80/120 dps all find 22 roots. Maximum
drifts are `4.35e-49` from 50 to 80 dps, `8.62e-79` from 80 to 120 dps, and
`5.41e-13` from complex128 to 120 dps. The 120-dps error against the exact
ledger is still `8.89658e-9`, so the primary error is cutoff, not precision.

The frozen contour diagnostics are:

| points/edge | winding | max phase step | accepted |
|---:|---:|---:|---|
| 128 | 22 | `2.00839` | no |
| 256 | 22 | `1.11299` | no |
| 512 | 22 | `0.568995` | yes |
| 1024 | 22 | `0.285756` | yes |

The coarse grids happen to return the correct count but fail the frozen
`pi/3` adjacent-phase gate. The successive 512/1024 grids pass.

These are numerical anti-alias diagnostics, not an interval-arithmetic or
derivative-bound proof. Endpoint sampling cannot rigorously exclude every
possible between-sample winding. This limitation is why the control verdict is
`GO_WITH_LIMITATIONS`, even though the exact analytic divisor is known.

Mode cutoff `N=2` has count 18; every frozen `N>=3` has count 22. The maximum
relative contour-value drift from `N=40` to `N=48` is `8.46440e-7`, showing
that count stability does not imply determinant-value stability.

## Strongest falsification result

The balanced corruption control proves that argument count alone is
insufficient:

- missing-only: counts `18/10/4/4`, matcher `4 missing, 0 extra`;
- extra-only: counts `26/14/6/6`, matcher `0 missing, 4 extra`;
- balanced: counts return to `22/12/5/5`, matcher still reports
  `4 missing, 4 extra`;
- absolute-value ablation: total winding changes to `30` and is rejected as a
  different determinant.

Executable ledger controls keep data types separate:

- `D` winding is `+22`;
- `1/D` winding is `-22`, interpreted as 22 poles and no zeros;
- `D'/D` contour integrals are `22.0000110` and `22.0000028` at 512 and
  1024 points per edge, with local scaled residue approximately 1;
- the order-four truncated-log exponential has winding zero and is
  analytically zero-free.

Every injected contour passes its own phase-step and integer-residual
diagnostics.

Signed cancellation is material. At repetition four,

\[
p_4=-0.33393858995368,
\qquad
\sum_c\left|\frac{a_c^4}{1-q_c^4}\right|
=33.59028440713514,
\]

so the cancellation ratio is `0.00994152`. Separate absolute-value bounds
cannot replace the signed trace.

## Route-A interpretation

```text
A1_WEAK
```

Synthetic factors and repetitions are exact and complete, but they are not
primitive orbits of a natural classical dynamics and have no rational-prime or
von-Mangoldt structure.

```text
A2_ANALYTIC_DETERMINANT
```

The trace-class Fredholm determinant is exact and the frozen evaluation prefix
passes all root, sampled-winding, cutoff, matching, ledger, precision, and
adversarial regression checks. `GO_WITH_LIMITATIONS` applies only to evaluator
infrastructure; the limitation is the non-rigorous sampled winding gate.

```text
A3_PARTIAL_ANALYTIC_STRUCTURE
```

The determinant is entire and conjugation symmetric with an exact divisor, but
it is `2*pi*i` periodic, has linear vertical zero density in a fixed strip, and
has no completed-xi functional equation, Gamma factor, trivial-zero ledger, or
Riemann-von Mangoldt count.

```text
A4_FAIL
```

The analytic family acts on an explicit Hilbert space but is not a natural
quantization of a classical symplectic/contact/scattering system. No
self-adjoint generator, physical domain problem, or Route-B obligation is
defined.

For completed-`xi` candidate interpretation, all four layers fail:

```text
(A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)
```

## Repository updates

Created:

- `configs/source_locks/CTRL-0001.yaml`;
- `experiments/ctrl_0001_qpochhammer.py`;
- `tests/test_ctrl_0001_qpochhammer.py`;
- `artifacts/ctrl_0001/route_a_positive_control.json`;
- `evaluations/route_a/CTRL-0001/20260803T171847Z.yaml`.

Updated:

- `docs/candidate_registry.md` with a separately labeled non-candidate control;
- `docs/research_clues.md`;
- `docs/research_log.md`;
- this handoff.

Unchanged by design:

- `docs/obstruction_registry.md`, because no new family theorem was proved;
- `docs/operator_obligations.md`, because Route B remains closed.

## Reproduction commands

Final verification: `14/14` focused tests and `46/46` full repository tests
passed. The regenerated artifact was byte-identical, both YAML files parsed,
and `git diff --check` passed.

```bash
python3 -m unittest -v tests/test_ctrl_0001_qpochhammer.py
python3 experiments/ctrl_0001_qpochhammer.py \
  --quiet \
  --output artifacts/ctrl_0001/route_a_positive_control.json
python3 -m unittest discover -v
git diff --check
```

Runtime environment for the control: CPython `3.12.3`, NumPy `2.4.4`, SciPy
`1.16.1`.

## Claim boundary

Established:

- an exact analytic trace-class positive-control determinant;
- independent direct-product winding and coefficient-root implementations;
- a frozen 22-root scoring prefix with explicit boundary clearance;
- cutoff-instability, coarse-phase, missing-only, extra-only, balanced, and
  absolute-value falsification behavior;
- a reusable one-to-one matching pattern with dummies and a signed-cancellation
  regression gate;
- executable separation of `D`, `1/D`, `D'/D`, and truncated-log ledgers;
- supplemental 50/80/120-dps root-drift reporting.

Not established:

- a natural classical dynamical system or primitive-orbit census;
- a rational-prime clock or von-Mangoldt repetition weights;
- completed-xi analytic structure or divisor equality;
- a moving-order theorem for another candidate;
- an interval-arithmetic or derivative-bound certificate for the sampled
  winding path;
- physical quantization, self-adjointness, Route B, Hilbert--Polya, or RH.

## Next smallest task

Do not continue tuning `CTRL-0001` and do not create `SS-0003` from it.

The next candidate-side task begins only when one explicit non-Selberg object
is mathematically defined with:

- an intrinsic clock;
- one same-object Fredholm/dynamical determinant convention;
- no prime or zero lookup;
- a frozen train/validation/test split and cutoff policy.

Once such an object exists, its first smallest test is to run the `CTRL-0001`
regression pattern: independent winding, logarithm-branch-complete root
discovery, one-to-one missing/extra matching, cutoff drift, balanced corruption,
and signed-complex cancellation. Until the object is explicit, no new formal
candidate should be allocated and Route B remains closed.
