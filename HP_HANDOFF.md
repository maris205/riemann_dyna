# HP-Dynamics Handoff

## Current status

The first formal Route-A baseline is complete.

- Active clue: `CLUE-A1-002`
- Candidate: `SS-0001`
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

`SS-0001` is the constant-roof suspension over the edge shift of
`Cay(Z/6Z,{+1,-1})`. It is an explicit, parameter-free mod-6 residue-memory
baseline that reads neither prime tables nor Riemann-zero tables.

The exact determinant is

\[
D(s)=\det(I-e^{-s}A)=(1-4e^{-2s})(1-e^{-2s})^2.
\]

Route-A tuple:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
```

Strongest evidence:

- primitive and repeated orbit counts are exact and reproducible;
- the graph contains nontrivial mod-3 character modes;
- the determinant has exact all-order factorization.

Strongest failure:

- the primitive clock is integral rather than an intrinsic `log p` clock;
- zeros form finitely many vertical arithmetic progressions;
- divisor counting is `O(T)`, not Riemann-von Mangoldt `Theta(T log T)`;
- the canonical finite graph quantization has only six eigenvalues.

The failure has been generalized in
`formal/obstructions/finite_state_finite_roof_zero_count.md`: every nonzero
finite-state finite-dimensional transfer determinant with finitely many
locally constant positive roof values has only `O(T)` zeros in a bounded
vertical strip. This is now family-level obstruction `OBR-005`.

## Source lock and evaluation

- Source lock: `configs/source_locks/SS-0001.yaml`
- Initial Route-A evaluation: `evaluations/route_a/SS-0001/20260802T160435Z.yaml`
- Latest Route-A evaluation: `evaluations/route_a/SS-0001/20260802T163302Z.yaml`
- Reproduction artifact: `artifacts/ss_0001/route_a_baseline.json`

## Reproduction commands

```bash
python3 -m unittest -v tests/test_ss_0001_mod6_cayley.py
python3 experiments/ss_0001_mod6_cayley.py --max-period 24 --output artifacts/ss_0001/route_a_baseline.json
```

## Next smallest task

No next formal candidate is currently defined. Do not create `SS-0002` until
the repository contains an explicit object outside `OBR-005`, together with:

- intrinsic clock;
- determinant convention;
- state/phase space;
- proof that the determinant is mathematically defined;
- explanation of how the object avoids direct prime encoding.

Permitted reopening classes include countable-state systems, unbounded or
non-locally-constant roofs, and infinite-dimensional nuclear transfer
operators. Merely adding more finite residue states does not reopen the clue.

## Claim boundary

No Route-A candidate has passed A2 or A3. No Route-B layer has been opened.
The current result is a meaningful scoped family obstruction, not a
Hilbert-Pólya operator and not evidence for a proof of the Riemann Hypothesis.
