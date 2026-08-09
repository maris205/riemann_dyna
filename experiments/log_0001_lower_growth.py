#!/usr/bin/env python3
"""Target-free lower-growth certificate for the LOG-0001 determinant.

The companion theorem is ``formal/results/log_0001_lower_growth.md``.  This
program evaluates only the exact scalar lower bound obtained from the already
proved real trace logarithm at ``s=2``.  It never evaluates the Fredholm
determinant, searches for roots, or reads arithmetic target data.
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


AUDIT_ID = "LOG-0001-LOWER-GROWTH"
PARENT_AUDIT_ID = "LOG-0001-CONFORMAL-RATIO"
SOURCE_LOCK = "configs/source_locks/LOG-0001-LOWER-GROWTH.yaml"
PARENT_LOCK = "configs/source_locks/LOG-0001-CONFORMAL-RATIO.yaml"
GROWTH_LOCK = "configs/source_locks/LOG-0001-GROWTH-ORDER.yaml"
PARENT_RESULT = "formal/results/log_0001_conformal_ratio.md"
GROWTH_RESULT = "formal/results/log_0001_growth_order.md"
BOUNDARY_RESULT = "formal/results/exact_uc_polar_boundary_trace.md"
PARENT_ARTIFACT = (
    "artifacts/log_0001_conformal_ratio/conformal_ratio_certificate.json"
)
GROWTH_ARTIFACT = (
    "artifacts/log_0001_growth_order/growth_order_certificate.json"
)
FORMAL_RESULT = "formal/results/log_0001_lower_growth.md"
GENERATOR = "experiments/log_0001_lower_growth.py"
ARTIFACT = (
    "artifacts/log_0001_lower_growth/lower_growth_certificate.json"
)
EVALUATION = "evaluations/route_a/LOG-0001/20260809T073000Z.yaml"

ARB_BITS = 1024
EXPECTED_PYTHON_VERSION = "3.12.3"
EXPECTED_PYTHON_FLINT_VERSION = "0.9.0"
EXPECTED_FLINT_VERSION = "3.6.0"
SAFE_REAL_POINT = 2
DERIVATIVE_SAFE_FLOOR = "0.0213"
LINEAR_RADIAL_SAFE_FLOOR = "0.01065"
SIMPLIFIED_RADIUS_MINIMUM = 4

REPRODUCTION_COMMAND = (
    "python3 experiments/log_0001_lower_growth.py --quiet --output "
    "artifacts/log_0001_lower_growth/lower_growth_certificate.json"
)


def file_sha256(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def exact_bracket_certificate() -> dict[str, Any]:
    """Check the inherited exact rational bracket and Cauchy geometry."""
    lower_value = support.critical_polynomial(support.U_LOWER)
    upper_value = support.critical_polynomial(support.U_UPPER)
    radial_factor = Fraction(1, 2)
    gates = {
        "critical_polynomial_is_negative_at_lower_endpoint": lower_value < 0,
        "critical_polynomial_is_positive_at_upper_endpoint": upper_value > 0,
        "critical_polynomial_derivative_is_globally_positive": (
            (-4) ** 2 - 4 * 3 * 2 < 0 and 3 > 0
        ),
        "safe_real_point_is_two": SAFE_REAL_POINT == 2,
        "simplified_radius_is_at_least_twice_the_center": (
            SIMPLIFIED_RADIUS_MINIMUM >= 2 * SAFE_REAL_POINT
        ),
        "radial_factor_is_one_half": radial_factor == Fraction(1, 2),
        "published_linear_floor_is_half_the_derivative_floor": (
            Fraction(LINEAR_RADIAL_SAFE_FLOOR)
            == Fraction(DERIVATIVE_SAFE_FLOOR) * radial_factor
        ),
    }
    return {
        "critical_polynomial": "u^3-2*u^2+2*u-2",
        "critical_polynomial_derivative": "3*u^2-4*u+2>0 on R (discriminant -8)",
        "lower_endpoint_polynomial_sign": -1 if lower_value < 0 else 0,
        "upper_endpoint_polynomial_sign": 1 if upper_value > 0 else 0,
        "safe_real_point": SAFE_REAL_POINT,
        "Cauchy_center": SAFE_REAL_POINT,
        "Cauchy_radius": "R-2",
        "simplified_radius_minimum": SIMPLIFIED_RADIUS_MINIMUM,
        "radial_factor": fraction_text(radial_factor),
        "computed_gates": gates,
        "computed_gates_passed": all(gates.values()),
    }


def root_ball() -> arb:
    return arb(support.U_LOWER_TEXT).union(arb(support.U_UPPER_TEXT))


def arb_interval_certificate() -> dict[str, Any]:
    previous_precision = ctx.prec
    try:
        ctx.prec = ARB_BITS
        u = root_ball()
        alpha_0 = u**2 / 4
        tau_star = -alpha_0.log()
        sigma_star = arb(2).log() / tau_star
        alpha_square = alpha_0**2
        trace_ratio = 2 * alpha_square
        trace_gap = 1 - trace_ratio
        b_2 = -trace_gap.log() / (1 - alpha_0)
        determinant_lower_factor = (-b_2).exp()
        pure_left_log_derivative = (
            tau_star * alpha_square / (1 - alpha_0)
        )
        c_2 = determinant_lower_factor * pure_left_log_derivative
        c_2_half = c_2 / 2

        derivative_floor = arb(213) / 10000
        radial_floor = arb(213) / 20000
        polynomial_ball = u**3 - 2 * u**2 + 2 * u - 2

        gates = {
            "critical_polynomial_ball_contains_zero": polynomial_ball.contains(0),
            "alpha_0_is_strictly_between_zero_and_one": (
                alpha_0 > 0 and alpha_0 < 1
            ),
            "tau_star_is_strictly_positive": tau_star > 0,
            "safe_point_is_inside_trace_log_half_plane": (
                arb(SAFE_REAL_POINT) > sigma_star
            ),
            "trace_ratio_two_alpha_squared_is_below_one": trace_ratio < 1,
            "trace_gap_is_strictly_positive": trace_gap > 0,
            "B_2_is_strictly_positive": b_2 > 0,
            "determinant_lower_factor_is_between_zero_and_one": (
                determinant_lower_factor > 0
                and determinant_lower_factor < 1
            ),
            "pure_left_log_derivative_is_positive": (
                pure_left_log_derivative > 0
            ),
            "c_2_is_above_published_derivative_floor": c_2 > derivative_floor,
            "half_c_2_is_above_published_radial_floor": c_2_half > radial_floor,
            "c_2_has_at_least_three_hundred_relative_bits": (
                c_2.rel_accuracy_bits() >= 300
            ),
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
            "alpha_0_squared_ball": alpha_square.str(110),
            "trace_ratio_2_alpha_0_squared_ball": trace_ratio.str(110),
            "trace_gap_1_minus_2_alpha_0_squared_ball": trace_gap.str(110),
            "B_2_ball": b_2.str(110),
            "determinant_lower_factor_ball": determinant_lower_factor.str(110),
            "pure_left_log_derivative_ball": pure_left_log_derivative.str(110),
            "c_2_ball": c_2.str(120),
            "c_2_relative_accuracy_bits": c_2.rel_accuracy_bits(),
            "c_2_half_ball": c_2_half.str(110),
            "derivative_safe_floor": DERIVATIVE_SAFE_FLOOR,
            "linear_radial_safe_floor": LINEAR_RADIAL_SAFE_FLOOR,
            "computed_gates": gates,
            "computed_gates_passed": all(gates.values()),
        }
    finally:
        ctx.prec = previous_precision


def build_report() -> dict[str, Any]:
    exact = exact_bracket_certificate()
    intervals = arb_interval_certificate()
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
        "all_exact_bracket_and_geometry_gates_pass": exact[
            "computed_gates_passed"
        ],
        "all_arb_interval_gates_pass": intervals[
            "computed_gates_passed"
        ],
    }

    source_inputs = [
        SOURCE_LOCK,
        PARENT_LOCK,
        GROWTH_LOCK,
        PARENT_RESULT,
        GROWTH_RESULT,
        BOUNDARY_RESULT,
        PARENT_ARTIFACT,
        GROWTH_ARTIFACT,
        FORMAL_RESULT,
        "experiments/p4_logistic_uc_first_return_support.py",
    ]

    return {
        "artifact_schema_version": 1,
        "audit_id": AUDIT_ID,
        "parent_audit_id": PARENT_AUDIT_ID,
        "candidate_id": "LOG-0001",
        "formal_candidate": True,
        "status": "TARGET_FREE_LOWER_GROWTH_CERTIFICATE_PASSED",
        "source_lock": SOURCE_LOCK,
        "frozen_object": {
            "operator": "same LOG-0001 matching-space family L_s|_B",
            "determinant": "D_pol(s)=det_Fr(I-L_s|_B)",
            "clock": "T_gamma=sum log|G'|",
            "signed_trace_denominator": "1-epsilon_omega*exp(-T_omega)",
            "matching_space": "B=ker[v_L(0)-v_R(0)]",
            "safe_real_point": SAFE_REAL_POINT,
            "auxiliary_fredholm_variable_kept_separate": True,
        },
        "exact_bracket_and_cauchy_certificate": exact,
        "arb_interval_certificate": intervals,
        "analytic_ledger": {
            "trace_log_domain": "Re(s)>log(2)/log(4/U_c^2)",
            "trace_log_identity": (
                "log D_pol(s)=-sum_(n>=1) sum_omega "
                "exp(-s*T_omega)/(n*(1-epsilon_omega*exp(-T_omega)))"
            ),
            "differentiated_trace_log": (
                "(log D_pol)'(sigma)=sum_(n>=1) sum_omega "
                "T_omega*exp(-sigma*T_omega)/"
                "(n*(1-epsilon_omega*exp(-T_omega)))"
            ),
            "local_uniform_differentiation": (
                "T*exp(-sigma*T)<=exp(-sigma_1*T)/(e*(sigma-sigma_1))"
            ),
            "all_real_derivative_summands_strictly_positive": True,
            "orientation_signs_preserved": True,
            "retained_term": "n=1 pure-left word L",
            "retained_term_is_a_proof_lower_bound_not_a_truncation": True,
            "pure_left_ledger": {
                "epsilon_L": 1,
                "exp_minus_T_L": "alpha_0=U_c^2/4",
                "T_L": "tau_*=-log(alpha_0)",
                "matching_factor": 1,
            },
            "D_2_lower": "exp(-B_2)",
            "B_2": "-log(1-2*alpha_0^2)/(1-alpha_0)",
            "D_prime_2_lower": (
                "c_2=(1-2*alpha_0^2)^(1/(1-alpha_0))*"
                "(-log(alpha_0))*alpha_0^2/(1-alpha_0)>0.0213"
            ),
        },
        "maximum_modulus_consequence": {
            "definition": "M_D(R)=max_(|s|<=R)|D_pol(s)|",
            "Cauchy_disk": "center 2, radius R-2, contained in |s|<=R",
            "all_R_greater_than_2": "M_D(R)>0.0213*(R-2)",
            "all_R_at_least_4": "M_D(R)>0.01065*R",
            "nonconstant": True,
            "transcendental_entire": True,
            "qualitative_super_polynomial_growth": (
                "M_D(R)/R^N -> infinity for every fixed N>=0"
            ),
        },
        "computed_gates": computed_gates,
        "computed_gates_passed": all(computed_gates.values()),
        "error_budget": {
            "operator_truncation": "none",
            "word_truncation": (
                "none; one positive term is retained only after the full "
                "derivative remainder is proved positive"
            ),
            "rounding": "1024-bit outward Arb scalar intervals",
            "normalization": "unchanged exact polar and matching ledgers",
            "cancellation": (
                "signed denominators retained; positivity is proved only "
                "on the safe real axis"
            ),
            "root_finding": "only the inherited certified U_c bracket; no determinant root",
        },
        "data_firewall": {
            "prime_tables_used": False,
            "primality_predicates_used": False,
            "Riemann_zero_tables_used": False,
            "xi_or_zeta_evaluated": False,
            "Fredholm_determinant_evaluated": False,
            "Fredholm_roots_searched": False,
            "auxiliary_lambda_coefficient_substituted": False,
            "USTC_data_used": False,
            "fitting_or_parameter_search_used": False,
        },
        "claim_boundary": {
            "route_a_effect": (
                "same-object lower-growth theorem added; tuple unchanged"
            ),
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
            "not_established": [
                "positive or exact entire-function order",
                "exponential lower growth or any zero-count lower bound",
                "sharp critical-strip divisor asymptotic or T*log(T) law",
                "Fredholm or Riemann zero locations",
                "completed-xi, quantization, Route B, Hilbert-Polya, or RH",
            ],
            "route_b_invocation_allowed": False,
        },
        "next_smallest_test": (
            "Under a separate lock, test whether boundedness on the proved "
            "right half-plane plus nonconstancy and finite order force "
            "ord(D_pol)>=1 by Phragmen-Lindelof; then apply the breadth rule."
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
