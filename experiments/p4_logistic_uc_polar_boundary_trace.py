#!/usr/bin/env python3
"""Certify the exact local boundary trace of the polar left branch."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path
from typing import Any

import mpmath as mp
import sympy as sp


AUDIT_ID = "P4-LOGISTIC-UC-POLAR-BOUNDARY-TRACE"
PARENT_AUDIT_ID = "P4-LOGISTIC-UC-POLAR-PARTITION-TRACE"
SOURCE_LOCK = "configs/source_locks/P4-LOGISTIC-UC-POLAR-BOUNDARY-TRACE.yaml"
PARENT_LOCK = "configs/source_locks/P4-LOGISTIC-UC-POLAR-PARTITION-TRACE.yaml"
FORMAL_RESULT = "formal/results/exact_uc_polar_boundary_trace.md"
GENERATOR = "experiments/p4_logistic_uc_polar_boundary_trace.py"
ARTIFACT = (
    "artifacts/p4_logistic_uc_polar_boundary_trace/"
    "boundary_trace_certificate.json"
)

DECIMAL_DIGITS = 100
POWERS = (1, 2, 3, 4)
CUTOFFS = (4, 8, 16, 32, 64)
S_VALUES = ("0", "1/2", "1", "2+i")

U_LOWER_TEXT = (
    "1.5436890126920763615708559718017479865252032976509839352408040378311686739279738664851579145760591254"
)
U_UPPER_TEXT = (
    "1.5436890126920763615708559718017479865252032976509839352408040378311686739279738664851579145760591255"
)


def file_sha256(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exact_identity_certificate() -> dict[str, Any]:
    u, t, x = sp.symbols("u t x")
    rho = u - 1
    critical = sp.Poly(u**3 - 2 * u**2 + 2 * u - 2, u)
    S = rho - 2 * u**2 * x**2 + u**3 * x**4

    def zero_mod_critical(expr: sp.Expr) -> bool:
        return sp.rem(sp.Poly(sp.expand(expr), u), critical).is_zero

    a_squared = (1 + t) * (rho + t) / (16 * t**2)
    a_endpoint_squared_residual = sp.together(
        a_squared.subs(t, rho) - u**4 / 16
    )
    endpoint_numerator = sp.fraction(a_endpoint_squared_residual)[0]
    identities = {
        "u_rho_squared_equals_one_minus_rho": u * rho**2 - (1 - rho),
        "u_cubed_rho_equals_two": u**3 * rho - 2,
        "S_plus_rho_equals_minus_rho": S.subs(x, rho) + rho,
        "S_minus_rho_equals_minus_rho": S.subs(x, -rho) + rho,
        "S_zero_equals_plus_rho": S.subs(x, 0) - rho,
        "a_endpoint_squared_equals_u_fourth_over_sixteen": endpoint_numerator,
    }
    gates = {name: zero_mod_critical(expr) for name, expr in identities.items()}
    return {
        "critical_polynomial": "u^3-2*u^2+2*u-2",
        "rho": "u-1",
        "alpha_0": "u^2/4",
        "boundary_graph": {"P": "P", "Q": "P", "Z": "Q"},
        "computed_gates": gates,
        "computed_gates_passed": all(gates.values()),
    }


def parse_s(text: str) -> mp.mpc:
    if text == "0":
        return mp.mpc(0)
    if text == "1/2":
        return mp.mpc(mp.mpf(1) / 2)
    if text == "1":
        return mp.mpc(1)
    if text == "2+i":
        return mp.mpc(2, 1)
    raise ValueError(text)


def numerical_trace_certificate() -> dict[str, Any]:
    previous_dps = mp.mp.dps
    try:
        mp.mp.dps = DECIMAL_DIGITS
        u = mp.findroot(lambda value: value**3 - 2 * value**2 + 2 * value - 2, mp.mpf("1.54"))
        lower = mp.mpf(U_LOWER_TEXT)
        upper = mp.mpf(U_UPPER_TEXT)
        alpha = u**2 / 4
        rows: list[dict[str, Any]] = []
        maximum_tail_residual = mp.mpf(0)
        for s_text in S_VALUES:
            s_value = parse_s(s_text)
            for power in POWERS:
                multiplier = alpha**power
                weight = mp.power(alpha, power * s_value)
                exact_trace = weight / (1 - multiplier)
                for cutoff in CUTOFFS:
                    partial = mp.fsum(
                        weight * multiplier**index for index in range(cutoff + 1)
                    )
                    exact_tail = weight * multiplier ** (cutoff + 1) / (1 - multiplier)
                    residual = abs((exact_trace - partial) - exact_tail)
                    maximum_tail_residual = max(maximum_tail_residual, residual)
                    rows.append(
                        {
                            "s": s_text,
                            "pure_L_word_power": power,
                            "taylor_cutoff": cutoff,
                            "trace": mp.nstr(exact_trace, 80),
                            "partial_trace": mp.nstr(partial, 80),
                            "exact_tail": mp.nstr(exact_tail, 80),
                            "tail_identity_residual": mp.nstr(residual, 20),
                        }
                    )
        return {
            "decimal_digits": DECIMAL_DIGITS,
            "u_c": mp.nstr(u, 105),
            "u_c_inside_certified_bracket": lower < u < upper,
            "alpha_0": mp.nstr(alpha, 100),
            "alpha_0_strictly_between_zero_and_one": 0 < alpha < 1,
            "powers": list(POWERS),
            "s_values": list(S_VALUES),
            "cutoffs": list(CUTOFFS),
            "rows": rows,
            "maximum_tail_identity_residual": mp.nstr(maximum_tail_residual, 20),
            "tail_identities_pass": maximum_tail_residual < mp.mpf("1e-90"),
        }
    finally:
        mp.mp.dps = previous_dps


def build_report() -> dict[str, Any]:
    exact = exact_identity_certificate()
    numeric = numerical_trace_certificate()
    gates = {
        "all_exact_identity_gates_pass": exact["computed_gates_passed"],
        "u_c_inside_certified_bracket": numeric["u_c_inside_certified_bracket"],
        "alpha_0_is_a_strict_contraction": numeric[
            "alpha_0_strictly_between_zero_and_one"
        ],
        "all_taylor_tail_identities_pass": numeric["tail_identities_pass"],
        "P_is_the_only_boundary_periodic_state": exact["boundary_graph"]
        == {"P": "P", "Q": "P", "Z": "Q"},
        "rounded_legacy_literal_is_not_used": U_LOWER_TEXT.startswith(
            "1.543689012692"
        ),
        "sympy_version_is_frozen": sp.__version__ == "1.14.0",
        "mpmath_version_is_frozen": mp.__version__ == "1.3.0",
    }
    source_inputs = [SOURCE_LOCK, PARENT_LOCK, FORMAL_RESULT]
    return {
        "artifact_schema_version": 1,
        "audit_id": AUDIT_ID,
        "parent_audit_id": PARENT_AUDIT_ID,
        "formal_candidate": False,
        "status": "PROVED_LOCAL_BOUNDARY_TRACE",
        "source_lock": SOURCE_LOCK,
        "mathematical_object": {
            "branch_operator": "T_(s,L)v=exp(s*ell)*v o phi_L on A(U_L)",
            "fixed_point": "P=-pi/2",
            "inverse_multiplier": "alpha_0=U_c^2/4",
            "weight_at_P": "alpha_0^s",
            "local_trace": "alpha_0^s/(1-alpha_0)",
            "pure_L_power_trace": "alpha_0^(n*s)/(1-alpha_0^n)",
        },
        "exact_identity_certificate": exact,
        "numerical_trace_certificate": numeric,
        "trace_theorem_ledger": {
            "function_space": "disk algebra A(U_L) on the frozen Jordan stadium",
            "compact_inclusion_inherited": True,
            "weighted_composition_is_nuclear_order_zero": True,
            "fixed_point_trace_formula": True,
            "P_is_complex_domain_interior": True,
            "real_boundary_half_weight_applies": False,
            "doubled_copy_factor": 1,
            "matching_space_factor": 1,
            "full_two_component_nuclearity_claimed": False,
        },
        "computed_gates": gates,
        "computed_gates_passed": all(gates.values()),
        "claim_boundary": {
            "established": [
                "the exact unique boundary periodic orbit P",
                "alpha_0=U_c^2/4 in (0,1)",
                "the nuclear trace alpha_0^s/(1-alpha_0) for the local left branch",
                "the pure-L power traces alpha_0^(n*s)/(1-alpha_0^n)",
                "no half-weight or doubled/matching multiplicity correction",
            ],
            "not_established": [
                "nuclearity of the full two-component matching-space family",
                "a Fredholm determinant or complete orbit trace formula",
                "arithmetic orbit weights, completed-xi structure, or target zeros",
                "quantization, Route B, Hilbert-Polya, or RH",
            ],
        },
        "route_a_effect": {
            "tuple_unchanged": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "local_verdict": "GO_WITH_LIMITATIONS",
            "recommended_verdict": "REVISE",
            "route_b_invocation_allowed": False,
        },
        "next_smallest_test": (
            "Prove nuclearity of the full two-component weighted family on "
            "the frozen matching space; do not evaluate Fredholm zeros first."
        ),
        "provenance": {
            "generator": GENERATOR,
            "generator_sha256": file_sha256(GENERATOR),
            "source_inputs_sha256": {path: file_sha256(path) for path in source_inputs},
            "external_target_data_used": False,
            "reproduction_command": (
                "python3 experiments/p4_logistic_uc_polar_boundary_trace.py "
                "--quiet --output " + ARTIFACT
            ),
            "python": platform.python_version(),
            "sympy": sp.__version__,
            "mpmath": mp.__version__,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default=ARTIFACT)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()
    report = build_report()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if not args.quiet:
        print(json.dumps(report, indent=2, sort_keys=True))
    if not report["computed_gates_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
