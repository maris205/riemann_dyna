#!/usr/bin/env python3
"""Exact on-shell incidence audit for the TH-0001 caustic.

The preceding phase audit found the internal caustic
``15*q1*q2 - 1 = 0`` for the ordered three-kick FIO.  This follow-up asks the
smallest structural question left open there: is the caustic attained by an
actual real stationary canonical trajectory, or is it only an artifact of
allowing arbitrary internal integration variables?  Exact rational algebra
shows that the whole real caustic is on-shell.

No spectrum, determinant, root list, prime table, or zero table is used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import sympy as sp


CANDIDATE_ID = "TH-0001"
AUDIT_ID = "TH-0001-A4-PHASE-CAUSTIC-REAL-001"
CLUE_ID = "CLUE-A4-001"
SOURCE_LOCK = "configs/source_locks/TH-0001-PHASE-CAUSTIC-REAL.yaml"
PARENT_EVALUATION = "evaluations/route_a/TH-0001/20260806T053410Z.yaml"
GENERATOR = "experiments/th_0001_phase_caustic_real.py"
ARTIFACT = "artifacts/th_0001/phase_caustic_real_audit.json"
FORMAL_RESULT = "formal/results/th_0001_phase_caustic_real.md"
OBSTRUCTION = "formal/obstructions/th_0001_single_phase_caustic.md"

q0, q1, q2, q3 = sp.symbols("q0 q1 q2 q3", real=True)
PARAMETERS = (sp.Rational(1, 2), sp.Rational(3, 2), sp.Rational(5, 2))


def generating_function(x: sp.Expr, y: sp.Expr, parameter: sp.Rational) -> sp.Expr:
    return sp.expand(x * y - x + parameter * x**3 / 3)


def henon_step(q: sp.Expr, p: sp.Expr, parameter: sp.Rational) -> tuple[sp.Expr, sp.Expr]:
    return (sp.expand(1 - parameter * q**2 - p), sp.expand(q))


def file_sha256(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def build_report(root: str | Path | None = None) -> dict[str, Any]:
    base = Path(root) if root is not None else Path(__file__).resolve().parents[1]
    a, b, c = PARAMETERS
    phase = sp.expand(
        generating_function(q0, q1, a)
        + generating_function(q1, q2, b)
        + generating_function(q2, q3, c)
    )
    stationary = [sp.factor(sp.diff(phase, variable)) for variable in (q1, q2)]
    hessian = sp.hessian(phase, (q1, q2))
    hessian_det = sp.factor(hessian.det())
    # Solve the stationary equations and caustic equation with t=q1 free.
    t = sp.symbols("t", real=True, nonzero=True)
    q2_on = sp.Rational(1, 15) / t
    q0_on = sp.factor(1 - sp.Rational(3, 2) * t**2 - q2_on)
    q3_on = sp.factor(1 - t - sp.Rational(5, 2) * q2_on**2)
    p0_on = sp.factor(1 - sp.Rational(1, 2) * q0_on**2 - t)
    p1_on, p2_on, p3_on = q0_on, t, q2_on

    witness = {"t": sp.Rational(1)}
    witness_q = {
        "q0": sp.simplify(q0_on.subs(t, 1)),
        "q1": sp.Integer(1),
        "q2": sp.simplify(q2_on.subs(t, 1)),
        "q3": sp.simplify(q3_on.subs(t, 1)),
    }
    witness_p = {
        "p0": sp.simplify(p0_on.subs(t, 1)),
        "p1": sp.simplify(p1_on.subs(t, 1)),
        "p2": sp.simplify(p2_on.subs(t, 1)),
        "p3": sp.simplify(p3_on.subs(t, 1)),
    }

    # Canonical endpoint projection of the stationary Lagrangian.
    q0_stationary = 1 - sp.Rational(3, 2) * q1**2 - q2
    q3_stationary = 1 - q1 - sp.Rational(5, 2) * q2**2
    endpoint_jacobian = sp.Matrix([q0_stationary, q3_stationary]).jacobian((q1, q2))
    endpoint_relation = sp.simplify(endpoint_jacobian + hessian)

    # The null direction at the rational witness has a nonzero third phase
    # derivative, so this point is a regular rank-one caustic witness.
    hessian_witness = hessian.subs({q1: 1, q2: sp.Rational(1, 15)})
    null_direction = sp.Matrix([-1, 3])
    null_image = hessian_witness * null_direction
    third_tensor = sp.diff(phase, q1, 3) * null_direction[0] ** 3 + sp.diff(phase, q2, 3) * null_direction[1] ** 3
    third_witness = sp.simplify(third_tensor.subs({q1: 1, q2: sp.Rational(1, 15)}))

    trajectory = [(q0_on, p0_on), (t, p1_on), (q2_on, p2_on), (q3_on, p3_on)]
    parameters = [a, b, c]
    residuals: list[sp.Expr] = []
    for (q_in, p_in), parameter, (q_out, p_out) in zip(trajectory, parameters, trajectory[1:]):
        step_q, step_p = henon_step(q_in, p_in, parameter)
        residuals.extend([sp.simplify(step_q - q_out), sp.simplify(step_p - p_out)])

    source_inputs = {
        SOURCE_LOCK: file_sha256(base / SOURCE_LOCK),
        PARENT_EVALUATION: file_sha256(base / PARENT_EVALUATION),
    }
    return {
        "candidate_id": CANDIDATE_ID,
        "audit_id": AUDIT_ID,
        "clue_id": CLUE_ID,
        "parent_audit_id": "TH-0001-A4-PHASE-CAUSTIC-001",
        "formal_candidate": True,
        "target_data_used": {
            "prime_table": False,
            "zero_table": False,
            "spectrum": False,
            "determinant": False,
            "fitting": False,
        },
        "phase": {
            "parameters": [str(value) for value in parameters],
            "ordered_phase": sp.sstr(phase),
            "stationary_equations": [sp.sstr(value) for value in stationary],
            "internal_hessian": [[sp.sstr(hessian[i, j]) for j in range(2)] for i in range(2)],
            "internal_hessian_determinant": sp.sstr(hessian_det),
        },
        "on_shell_caustic": {
            "caustic_equation": "15*q1*q2-1=0",
            "parameter": "t=q1 in R\\{0}",
            "q0": sp.sstr(q0_on),
            "q1": "t",
            "q2": sp.sstr(q2_on),
            "q3": sp.sstr(q3_on),
            "endpoint_projection_jacobian": [[sp.sstr(endpoint_jacobian[i, j]) for j in range(2)] for i in range(2)],
            "endpoint_jacobian_plus_hessian": [[sp.sstr(endpoint_relation[i, j]) for j in range(2)] for i in range(2)],
            "all_real_nonzero_t_are_on_shell": True,
        },
        "canonical_trajectory": {
            "q": {name: sp.sstr(value) for name, value in witness_q.items()},
            "p": {name: sp.sstr(value) for name, value in witness_p.items()},
            "step_residuals": [sp.sstr(value) for value in residuals],
            "all_step_residuals_zero": all(value == 0 for value in residuals),
        },
        "regular_rank_one_witness": {
            "hessian_at_witness": [[sp.sstr(hessian_witness[i, j]) for j in range(2)] for i in range(2)],
            "rank": int(hessian_witness.rank()),
            "null_direction": [sp.sstr(value) for value in null_direction],
            "hessian_times_null": [sp.sstr(value) for value in null_image],
            "third_directional_derivative": sp.sstr(third_witness),
            "nonzero_third_directional_derivative": third_witness != 0,
        },
        "route_effect": {
            "analytic_tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "riemann_target_tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall_verdict": "ROUTE_A_EXPLORATORY",
            "scoped_audit_verdict": "GO_WITH_LIMITATIONS",
            "obstruction_refined": "OBR-011",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "established": [
                "the internal caustic is attained by every real nonzero-t stationary branch",
                "the caustic is a singular endpoint projection of the stationary Lagrangian",
                "the rational witness is an exact real three-kick canonical trajectory",
                "the t=1 witness has rank-one Hessian and nonzero null-direction third derivative",
            ],
            "not_established": [
                "a multi-chart phase or Maslov transition ledger",
                "an orbit phase or arithmetic weight law",
                "a determinant, spectrum, trace formula, Route B, Hilbert-Polya, or RH result",
            ],
        },
        "next_smallest_test": (
            "Stop this incidence audit; reopen only with an explicitly source-locked "
            "multi-chart phase/Maslov transition ledger, or pivot breadth-first."
        ),
        "provenance": {
            "source_inputs_sha256": source_inputs,
            "generator_sha256": file_sha256(base / GENERATOR),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--output", type=Path, default=Path(ARTIFACT))
    args = parser.parse_args()
    report = build_report()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if not args.quiet:
        print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
