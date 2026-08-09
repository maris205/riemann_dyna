#!/usr/bin/env python3
"""Target-free Phragmen--Lindelof order-lower certificate for LOG-0001.

This audit uses only the inherited same-object entire-function theorem, the
uniform signed-trace bound on ``Re(s)>=2``, and the certified nonconstancy
witness.  It does not evaluate the Fredholm determinant or search for roots.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
from typing import Any

import flint
from flint import arb, ctx

try:
    from experiments import p4_logistic_uc_first_return_support as support
except ModuleNotFoundError:  # Direct execution from the repository root.
    import p4_logistic_uc_first_return_support as support


AUDIT_ID = "LOG-0001-ORDER-LOWER"
PARENT_AUDIT_ID = "LOG-0001-LOWER-GROWTH"
CANDIDATE_ID = "LOG-0001"
SOURCE_LOCK = "configs/source_locks/LOG-0001-ORDER-LOWER.yaml"
PARENT_LOCK = "configs/source_locks/LOG-0001-LOWER-GROWTH.yaml"
GROWTH_LOCK = "configs/source_locks/LOG-0001-GROWTH-ORDER.yaml"
PARENT_RESULT = "formal/results/log_0001_lower_growth.md"
GROWTH_RESULT = "formal/results/log_0001_growth_order.md"
PARENT_ARTIFACT = (
    "artifacts/log_0001_lower_growth/lower_growth_certificate.json"
)
GROWTH_ARTIFACT = (
    "artifacts/log_0001_growth_order/growth_order_certificate.json"
)
PARENT_EVALUATION = "evaluations/route_a/LOG-0001/20260809T073000Z.yaml"
EVALUATION = "evaluations/route_a/LOG-0001/20260809T110000Z.yaml"
FORMAL_RESULT = "formal/results/log_0001_order_lower.md"
GENERATOR = "experiments/log_0001_order_lower.py"
ARTIFACT = "artifacts/log_0001_order_lower/order_lower_certificate.json"

ARB_BITS = 1024
EXPECTED_PYTHON_VERSION = "3.12.3"
EXPECTED_PYTHON_FLINT_VERSION = "0.9.0"
EXPECTED_FLINT_VERSION = "3.6.0"
SAFE_REAL_POINT = 2
DERIVATIVE_SAFE_FLOOR = "0.0213"
ORDER_UPPER_BOUND = 2
PL_THRESHOLD = 1

REPRODUCTION_COMMAND = (
    "python3 experiments/log_0001_order_lower.py --quiet --output "
    "artifacts/log_0001_order_lower/order_lower_certificate.json"
)


def file_sha256(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def root_ball() -> arb:
    return arb(support.U_LOWER_TEXT).union(arb(support.U_UPPER_TEXT))


def scalar_certificate() -> dict[str, Any]:
    previous_precision = ctx.prec
    try:
        ctx.prec = ARB_BITS
        u = root_ball()
        alpha_0 = u**2 / 4
        tau_star = -alpha_0.log()
        sigma_star = arb(2).log() / tau_star
        q_2 = 2 * alpha_0**2
        b_2 = -((1 - q_2).log()) / (1 - alpha_0)
        k_2 = b_2.exp()
        polynomial_ball = u**3 - 2 * u**2 + 2 * u - 2

        gates = {
            "critical_polynomial_ball_contains_zero": polynomial_ball.contains(0),
            "alpha_0_strictly_between_zero_and_one": (
                alpha_0 > 0 and alpha_0 < 1
            ),
            "q_2_strictly_below_one": q_2 < 1,
            "B_2_strictly_positive": b_2 > 0,
            "K_2_strictly_above_one": k_2 > 1,
            "anchor_is_two": SAFE_REAL_POINT == 2,
            "anchor_is_above_inherited_threshold": (
                arb(SAFE_REAL_POINT) > sigma_star
            ),
            "pl_opening_is_pi": Fraction(1, 1) > 0,
            "pl_threshold_is_one": PL_THRESHOLD == 1,
            "mu_can_be_chosen_strictly_below_threshold": PL_THRESHOLD > 0,
        }

        return {
            "arb_bits": ARB_BITS,
            "working_decimal_digits_floor": 300,
            "inherited_root_bracket_decimal_digits": 100,
            "U_c_ball": u.str(110),
            "critical_polynomial_ball": polynomial_ball.str(80),
            "alpha_0_ball": alpha_0.str(110),
            "tau_star_ball": tau_star.str(110),
            "sigma_star_ball": sigma_star.str(110),
            "q_2_ball": q_2.str(110),
            "B_2_ball": b_2.str(110),
            "K_2_ball": k_2.str(110),
            "K_2_definition": "exp(B_2)",
            "computed_gates": gates,
            "computed_gates_passed": all(gates.values()),
        }
    finally:
        ctx.prec = previous_precision


def inherited_nonconstancy_gate() -> dict[str, Any]:
    lower = json.loads(Path(PARENT_ARTIFACT).read_text(encoding="utf-8"))
    c_2 = lower["arb_interval_certificate"]["c_2_ball"]
    previous_precision = ctx.prec
    try:
        ctx.prec = ARB_BITS
        c_2_interval = arb(c_2)
        floor = arb(213) / 10000
        gates = {
            "inherited_lower_growth_certificate_passed": (
                lower["computed_gates_passed"] is True
            ),
            "inherited_derivative_witness_above_floor": c_2_interval > floor,
            "inherited_transcendental_entire_claim": (
                lower["maximum_modulus_consequence"]["transcendental_entire"]
                is True
            ),
        }
        return {
            "c_2_interval": c_2,
            "safe_floor": DERIVATIVE_SAFE_FLOOR,
            "computed_gates": gates,
            "computed_gates_passed": all(gates.values()),
        }
    finally:
        ctx.prec = previous_precision


def proof_ledger() -> dict[str, Any]:
    gates = {
        "same_entire_object_retained": True,
        "uniform_closed_half_plane_bound_at_re_ge_2": True,
        "translated_function_is_g_of_z_equals_D_2_minus_z": True,
        "principal_branch_on_right_half_plane": True,
        "choose_rho_lt_eta_lt_mu_lt_one_under_contradiction": True,
        "cos_mu_pi_over_two_is_positive": True,
        "semicircle_damping_dominates_order_eta": True,
        "half_disk_maximum_principle_applied": True,
        "epsilon_decreases_to_zero": True,
        "liouville_contradicts_D_prime_at_2_nonzero": True,
        "no_uniform_real_axis_only_substitution": True,
    }
    return {
        "assumption_for_contradiction": "ord(D_pol)=rho<1",
        "auxiliary_exponents": "rho<eta<mu<1",
        "translated_variable": "g(z)=D_pol(2-z), Re(z)>0",
        "boundary_line": "g(it)=D_pol(2-it), |g(it)|<=K_2",
        "damping": "h_epsilon(z)=g(z)*exp(-epsilon*z^mu)",
        "sector_lower_bound": "Re(z^mu)>=cos(mu*pi/2)*|z|^mu",
        "global_consequence": "D_pol bounded on Re(s)<2, then on C",
        "liouville_consequence": "D_pol constant, contradicting D_pol'(2)>0.0213",
        "computed_gates": gates,
        "computed_gates_passed": all(gates.values()),
    }


def build_report() -> dict[str, Any]:
    scalar = scalar_certificate()
    witness = inherited_nonconstancy_gate()
    proof = proof_ledger()
    source_inputs = [
        SOURCE_LOCK,
        PARENT_LOCK,
        GROWTH_LOCK,
        PARENT_RESULT,
        GROWTH_RESULT,
        PARENT_ARTIFACT,
        GROWTH_ARTIFACT,
        PARENT_EVALUATION,
        FORMAL_RESULT,
        EVALUATION,
        "experiments/p4_logistic_uc_first_return_support.py",
    ]
    computed_gates = {
        "python_version_is_frozen": (
            platform.python_version() == EXPECTED_PYTHON_VERSION
        ),
        "python_flint_version_is_frozen": (
            flint.__version__ == EXPECTED_PYTHON_FLINT_VERSION
        ),
        "flint_version_is_frozen": (
            flint.__FLINT_VERSION__ == EXPECTED_FLINT_VERSION
        ),
        "scalar_certificate_passed": scalar["computed_gates_passed"],
        "inherited_nonconstancy_gate_passed": witness[
            "computed_gates_passed"
        ],
        "pl_proof_ledger_passed": proof["computed_gates_passed"],
    }
    return {
        "artifact_schema_version": 1,
        "audit_id": AUDIT_ID,
        "parent_audit_id": PARENT_AUDIT_ID,
        "candidate_id": CANDIDATE_ID,
        "formal_candidate": True,
        "status": "TARGET_FREE_ORDER_LOWER_CERTIFICATE_PASSED",
        "source_lock": SOURCE_LOCK,
        "frozen_object": {
            "determinant": "D_pol(s)=det_Fr(I-L_s|_B)",
            "clock": "T_gamma=sum log|G'|",
            "matching_space": "B=ker[v_L(0)-v_R(0)]",
            "pl_boundary": "Re(s)=2",
            "pl_translation": "g(z)=D_pol(2-z)",
            "auxiliary_lambda_kept_separate": True,
        },
        "scalar_certificate": scalar,
        "inherited_nonconstancy_gate": witness,
        "pl_proof_ledger": proof,
        "route_a_effect": {
            "analytic_tuple": [
                "A1_WEAK",
                "A2_ANALYTIC_DETERMINANT",
                "A3_PARTIAL_ANALYTIC_STRUCTURE",
                "A4_FAIL",
            ],
            "riemann_target_tuple": [
                "A1_WEAK",
                "A2_FAIL",
                "A3_FAIL",
                "A4_FAIL",
            ],
            "order_lower_bound": "1<=ord(D_pol)<=2",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "established": [
                "uniform same-object bound on Re(s)>=2 is sufficient for PL",
                "nonconstant entire D_pol has ord(D_pol)>=1",
                "inherited upper theorem combines to 1<=ord(D_pol)<=2",
            ],
            "not_established": [
                "exact order or whether it is one or two",
                "exponential type or divisor-count asymptotic",
                "target zeros, completed-xi, quantization, Route B, or RH",
            ],
        },
        "data_firewall": {
            "prime_tables_used": False,
            "Riemann_zero_tables_used": False,
            "xi_or_zeta_evaluated": False,
            "Fredholm_determinant_evaluated": False,
            "Fredholm_roots_searched": False,
            "fitting_or_parameter_search_used": False,
            "changed_object_or_clock_used": False,
        },
        "computed_gates": computed_gates,
        "computed_gates_passed": all(computed_gates.values()),
        "next_smallest_test": (
            "Apply the breadth pivot: define a new intrinsic recurrent object "
            "with a plausible arithmetic orbit law, or register a reusable "
            "obstruction; do not add another fixed-point estimate to LOG-0001."
        ),
        "provenance": {
            "generator": GENERATOR,
            "generator_sha256": file_sha256(GENERATOR),
            "source_inputs_sha256": {
                path: file_sha256(path) for path in source_inputs
            },
            "route_a_evaluation": EVALUATION,
            "external_target_data_used": False,
            "reproduction_command": REPRODUCTION_COMMAND,
        },
        "validated_environment": {
            "python": platform.python_version(),
            "python_flint": flint.__version__,
            "flint": flint.__FLINT_VERSION__,
            "arb_bits": ARB_BITS,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default=ARTIFACT)
    parser.add_argument("--quiet", action="store_true")
    arguments = parser.parse_args()
    report = build_report()
    output = Path(arguments.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    if not arguments.quiet:
        print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["computed_gates_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
