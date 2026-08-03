# HP-Dynamics Handoff

## Current status

The second formal Route-A baseline is complete.

- Active clue: `CLUE-A1-002`
- Candidate: `SS-0002`
- Candidate state: `STOP_SCOPED`
- Route A: `ROUTE_A_REJECTED`
- Route B: inactive and not authorized

## Current entry files

- `docs/HP_Dynamics_Project_Entry.md`
- `docs/main_agent_rules.md`
- `docs/research_clues.md`
- `.agents/skills/route-a-evaluator/SKILL.md`
- `.agents/skills/route-b-evaluator/SKILL.md`

## Current frontier

`SS-0002` is the paired-Gauss regular-holonomy Mayer operator for the
six-sheeted commutator cover of the modular surface. With

\[
\Gamma=\operatorname{PSL}_2(\mathbb Z),\qquad
\Gamma_{\rm com}=[\Gamma,\Gamma]
=\ker(\Gamma\to C_6),
\]

its inverse branches and intrinsic cover cocycle are

\[
\phi_{a,b}(z)=\frac{z+a}{b(z+a)+1},
\qquad c(a,b)=a-b\pmod6.
\]

On \(\mathcal A(D_{3/2})\otimes\mathbb C^6\), the frozen determinant is

\[
D_{\rm ab}(s)=\det_{\rm Fr}(I-\mathcal M_s)
=Z_{\Gamma_{\rm com}}(s).
\]

The candidate reads neither prime tables nor Riemann-zero tables. It is
countable-branch, infinite-dimensional, non-locally-constant, and nuclear of
order zero for \(\Re s>1/2\), so it genuinely escapes `OBR-005`.

Route-A tuple:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)
```

Strongest evidence:

- the paired branch matrix, derivative, determinant-one identity, and mod-six
  cocycle pass exact disjoint validation/test checks;
- the regular representation retains nontrivial mod-three character modes and
  correctly handles nonzero-holonomy primitive lifts;
- the Fredholm determinant has a theorem-backed Selberg identity;
- the same geodesic clock has a canonical Laplace--Beltrami quantization.

Strongest failure:

- modular closed-geodesic lengths are not a natural rational-prime `log p`
  clock and do not generate von-Mangoldt weights;
- the inherited modular cusp spectrum alone gives at least
  \(T^2/12+o(T^2)\) positive-height Selberg zeros;
- the full area-\(2\pi\) resonance law has two-sided main term \(T^2\), not
  the completed-\(\xi\) \(\Theta(T\log T)\) count;
- the modular scattering determinant is a separate zero/pole ledger and
  cannot be glued to the Mayer determinant.

The failure is recorded as `OBR-006` in
`formal/obstructions/finite_area_selberg_weyl_mismatch.md`. `OBR-005` remains
valid for the finite-state parent family; SS-0002 demonstrates that escaping
one obstruction is not sufficient when the new same-object determinant has a
different global counting obstruction.

## Source lock and evaluation

- Source lock: `configs/source_locks/SS-0002.yaml`
- Route-A evaluation: `evaluations/route_a/SS-0002/20260803T012711Z.yaml`
- Reproduction artifact: `artifacts/ss_0002/route_a_structural_audit.json`
- Literature ledger: `docs/literature/ss_0002_gauss_mayer_sources.md`

## Reproduction commands

```bash
python3 -m unittest -v tests/test_ss_0002_commutator_mayer.py
python3 experiments/ss_0002_commutator_mayer.py --output artifacts/ss_0002/route_a_structural_audit.json
```

## Next smallest task

No next formal candidate is currently defined. Do not create `SS-0003` until
the repository contains one explicit non-Selberg countable-state or nuclear
object, together with:

- intrinsic clock;
- determinant convention;
- state/phase space;
- proof that the determinant is mathematically defined;
- proof or sharp bound for its own divisor-count regime;
- explanation of how the object avoids direct prime/zero encoding;
- proof that it does not borrow an independent scattering quotient.

Another finite-area modular Selberg cover is already inside `OBR-006` and is
not a new candidate. The smallest next task is object definition and
same-ledger zero-count classification, not zero fitting.

## Claim boundary

No Route-A candidate has passed A2 or A3. No Route-B layer has been opened.
SS-0002 establishes a meaningful countable-state escape and a new scoped
Selberg/Weyl obstruction. Its natural Laplacian is not a Hilbert--Polya
operator, and nothing here is evidence for a proof of the Riemann Hypothesis.
