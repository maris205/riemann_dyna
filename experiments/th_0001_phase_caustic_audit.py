#!/usr/bin/env python3
"""Exact internal-phase caustic audit for the TH-0001 three-kick FIO."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


CANDIDATE_ID = "TH-0001"
AUDIT_ID = "TH-0001-A4-PHASE-CAUSTIC-001"
PARAMETERS = (sp.Rational(1, 2), sp.Rational(3, 2), sp.Rational(5, 2))
q0, q1, q2, q3 = sp.symbols("q0 q1 q2 q3", real=True)


def generating_function(x: sp.Expr, y: sp.Expr, parameter: sp.Rational) -> sp.Expr:
    return sp.expand(x * y - x + parameter * x**3 / 3)


def build_report() -> dict[str, object]:
    a, b, c = PARAMETERS
    phase = sp.expand(
        generating_function(q0, q1, a)
        + generating_function(q1, q2, b)
        + generating_function(q2, q3, c)
    )
    hessian = sp.hessian(phase, (q1, q2))
    determinant = sp.factor(hessian.det())
    stationary = [sp.expand(sp.diff(phase, variable)) for variable in (q1, q2)]
    return {
        "candidate_id": CANDIDATE_ID,
        "audit_id": AUDIT_ID,
        "source_lock": "configs/source_locks/TH-0001-FIO.yaml",
        "phase_variables": ["q0", "q1", "q2", "q3"],
        "parameter_order": ["1/2", "3/2", "5/2"],
        "ordered_phase": sp.sstr(phase),
        "stationary_equations": [sp.sstr(value) for value in stationary],
        "internal_hessian_variables": ["q1", "q2"],
        "internal_hessian": [[sp.sstr(hessian[i, j]) for j in range(2)] for i in range(2)],
        "internal_hessian_determinant": sp.sstr(determinant),
        "caustic_equation": "15*q1*q2-1=0",
        "caustic_nonempty_witness": {"q1": "1", "q2": "1/15"},
        "global_single_phase_reduction": False,
        "ordered_oscillatory_integral_remains_defined": True,
        "factorized_unitarity_unaffected": True,
        "phase_convention": {
            "factor_amplitude": "positive real (2*pi)^(-1/2)",
            "factor_phase": "exp(+i*S_a)",
            "global_maslov_index": "NOT_ASSIGNED",
            "reason": "single reduced phase is not globally nondegenerate",
        },
        "route_a_a4": {
            "verdict": "A4_NATURAL_QUANTIZATION",
            "new_obstruction": "OBR-011",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "established": [
                "exact ordered three-kick phase",
                "internal Hessian determinant 15*q1*q2-1",
                "nonempty caustic set and failure of a global single-phase reduction",
                "factorized unitary product remains unaffected",
            ],
            "not_established": [
                "a global reduced generating function across caustics",
                "any orbit Maslov assignment or signed-multiplier phase law",
                "spectrum, determinant, trace formula, Route B, or RH",
            ],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()
    payload = json.dumps(build_report(), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    if not args.quiet:
        print(payload, end="")


if __name__ == "__main__":
    main()
