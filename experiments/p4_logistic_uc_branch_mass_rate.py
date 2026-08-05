#!/usr/bin/env python3
"""Certify a quantitative exact-U_c physical branch-mass-ratio rate."""

from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction
import hashlib
import json
import platform
from pathlib import Path
from typing import Any

import flint
from flint import arb, ctx

try:
    from experiments import p4_logistic_uc_first_return_support as support
except ModuleNotFoundError:  # Direct execution from the repository root.
    import p4_logistic_uc_first_return_support as support


AUDIT_ID = "P4-LOGISTIC-UC-BRANCH-MASS-RATE"
PARENT_AUDIT_ID = "P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE"
SOURCE_LOCK = "configs/source_locks/P4-LOGISTIC-UC-BRANCH-MASS-RATE.yaml"
FORMAL_RESULT = "formal/results/exact_uc_branch_mass_rate.md"
GENERATOR = "experiments/p4_logistic_uc_branch_mass_rate.py"

ARB_DECIMAL_DIGITS = 100
EXPECTED_PYTHON_FLINT_VERSION = "0.9.0"
EXPECTED_FLINT_VERSION = "3.6.0"

CUSP_RADIUS = Fraction(1, 200)
MINIMUM_BRANCH_INDEX = 6
PSI_DERIVATIVE_LOWER = Fraction(7, 20)
PSI_DERIVATIVE_UPPER = Fraction(9, 25)
PSI_SECOND_DERIVATIVE_UPPER = Fraction(4, 25)
Q_LOWER = Fraction(59, 100)
Q_UPPER = Fraction(3, 5)
C_LOWER = Fraction(9461, 100000)
ENDPOINT_REMAINDER = Fraction(61, 100)
SQRT_DELTA_5_UPPER = Fraction(27, 500)
Q_ERROR_COEFFICIENT = Fraction(7, 50)
RELATIVE_ERROR_COEFFICIENT = Fraction(129, 25)
RELATIVE_ERROR_BASE_UPPER = Fraction(7, 25)
GEOMETRY_ERROR_COEFFICIENT = Fraction(11, 25)
MAIN_RATIO_UPPER = Fraction(123, 200)
LOCAL_RATE_CONSTANT = Fraction(36, 5)
EXPONENTIAL_RATE_PREFACTOR = Fraction(243, 625)

REPRODUCTION_COMMAND = (
    "python3 experiments/p4_logistic_uc_branch_mass_rate.py --quiet "
    "--output artifacts/p4_logistic_uc_branch_mass_rate/"
    "rate_certificate.json"
)


def file_sha256(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def arb_fraction(value: Fraction) -> arb:
    return arb(value.numerator) / value.denominator


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def fraction_decimal(value: Fraction, digits: int = 60) -> str:
    with localcontext() as decimal_context:
        decimal_context.prec = digits
        return str(Decimal(value.numerator) / Decimal(value.denominator))


def root_ball() -> arb:
    return arb(support.U_LOWER_TEXT).union(arb(support.U_UPPER_TEXT))


def derivative_certificate(u: arb, rho: arb) -> dict[str, Any]:
    x = (rho - arb_fraction(CUSP_RADIUS)).union(rho)
    first_inverse = ((1 - x) / u).sqrt()
    psi = ((1 - first_inverse) / u).sqrt()
    psi_prime = 1 / (4 * u**2 * first_inverse * psi)
    psi_second = psi_prime * (
        1 / (2 * (1 - x))
        - 1 / (4 * u * first_inverse * (1 - first_inverse))
    )

    gates = {
        "psi_prime_above_7_over_20": (
            psi_prime > arb_fraction(PSI_DERIVATIVE_LOWER)
        ),
        "psi_prime_below_9_over_25": (
            psi_prime < arb_fraction(PSI_DERIVATIVE_UPPER)
        ),
        "psi_second_is_positive": psi_second > 0,
        "psi_second_below_4_over_25": (
            psi_second < arb_fraction(PSI_SECOND_DERIVATIVE_UPPER)
        ),
    }
    return {
        "x_domain": ["rho-1/200", "rho"],
        "psi_prime_ball": psi_prime.str(60),
        "psi_prime_lower": str(psi_prime.lower()),
        "psi_prime_upper": str(psi_prime.upper()),
        "psi_second_ball": psi_second.str(60),
        "psi_second_lower": str(psi_second.lower()),
        "psi_second_upper": str(psi_second.upper()),
        "gates": gates,
    }


def base_endpoint_certificate() -> dict[str, Any]:
    r_lower, r_upper = support.certified_endpoint_intervals(5)[5]
    delta_lower = support.U_LOWER - 1 - r_upper
    delta_upper = support.U_UPPER - 1 - r_lower
    sqrt_bound_squared = SQRT_DELTA_5_UPPER**2
    return {
        "branch_index": 5,
        "delta_5_exact_interval": {
            "lower": fraction_text(delta_lower),
            "upper": fraction_text(delta_upper),
        },
        "delta_5_decimal_approximation": {
            "lower": fraction_decimal(delta_lower),
            "upper": fraction_decimal(delta_upper),
        },
        "sqrt_delta_5_safe_upper": fraction_text(SQRT_DELTA_5_UPPER),
        "delta_5_below_cusp_radius": delta_upper < CUSP_RADIUS,
        "sqrt_delta_5_below_27_over_500": (
            delta_upper < sqrt_bound_squared
        ),
    }


def exact_rate_ledger() -> dict[str, Any]:
    q_error_raw = PSI_SECOND_DERIVATIVE_UPPER / (2 * Q_LOWER)
    relative_error_raw = (
        ENDPOINT_REMAINDER
        * (1 + Q_UPPER)
        / (2 * C_LOWER)
    )
    relative_error_at_base = (
        RELATIVE_ERROR_COEFFICIENT * SQRT_DELTA_5_UPPER
    )
    next_q_error_coefficient = (
        Q_ERROR_COEFFICIENT * PSI_DERIVATIVE_UPPER
    )
    geometry_raw = (
        Fraction(41, 16) * Q_ERROR_COEFFICIENT
        + Fraction(3, 2) * next_q_error_coefficient
    )
    quotient_factor_coefficient = (
        RELATIVE_ERROR_COEFFICIENT
        * (1 + Q_UPPER)
        / (1 - RELATIVE_ERROR_BASE_UPPER)
    )
    mass_error_coefficient = MAIN_RATIO_UPPER * quotient_factor_coefficient
    combined_rate_coefficient = (
        mass_error_coefficient
        + GEOMETRY_ERROR_COEFFICIENT * SQRT_DELTA_5_UPPER
    )
    exponential_prefactor = (
        LOCAL_RATE_CONSTANT * SQRT_DELTA_5_UPPER
    )

    gates = {
        "q_lower_squared_is_below_psi_derivative_lower": (
            Q_LOWER**2 < PSI_DERIVATIVE_LOWER
        ),
        "psi_derivative_upper_equals_q_upper_squared": (
            PSI_DERIVATIVE_UPPER == Q_UPPER**2
        ),
        "q_error_coefficient_is_safe": (
            q_error_raw < Q_ERROR_COEFFICIENT
        ),
        "relative_mass_error_coefficient_is_safe": (
            relative_error_raw < RELATIVE_ERROR_COEFFICIENT
        ),
        "base_relative_error_is_below_7_over_25": (
            relative_error_at_base < RELATIVE_ERROR_BASE_UPPER
        ),
        "geometry_error_coefficient_is_safe": (
            geometry_raw < GEOMETRY_ERROR_COEFFICIENT
        ),
        "relative_error_denominator_is_positive": (
            1 - RELATIVE_ERROR_BASE_UPPER > 0
        ),
        "combined_rate_coefficient_is_below_36_over_5": (
            combined_rate_coefficient < LOCAL_RATE_CONSTANT
        ),
        "exponential_prefactor_is_exact": (
            exponential_prefactor == EXPONENTIAL_RATE_PREFACTOR
        ),
    }

    return {
        "q_error_raw": fraction_text(q_error_raw),
        "q_error_safe": fraction_text(Q_ERROR_COEFFICIENT),
        "relative_mass_error_raw": fraction_text(relative_error_raw),
        "relative_mass_error_safe": fraction_text(
            RELATIVE_ERROR_COEFFICIENT
        ),
        "relative_error_at_base": fraction_text(relative_error_at_base),
        "relative_error_base_safe": fraction_text(
            RELATIVE_ERROR_BASE_UPPER
        ),
        "next_q_error_coefficient": fraction_text(
            next_q_error_coefficient
        ),
        "geometry_error_raw": fraction_text(geometry_raw),
        "geometry_error_safe": fraction_text(
            GEOMETRY_ERROR_COEFFICIENT
        ),
        "main_ratio_upper": fraction_text(MAIN_RATIO_UPPER),
        "quotient_factor_coefficient": fraction_text(
            quotient_factor_coefficient
        ),
        "mass_error_coefficient": fraction_text(mass_error_coefficient),
        "combined_rate_coefficient": fraction_text(
            combined_rate_coefficient
        ),
        "local_rate_constant": fraction_text(LOCAL_RATE_CONSTANT),
        "exponential_rate_prefactor": fraction_text(
            EXPONENTIAL_RATE_PREFACTOR
        ),
        "exponential_rate_base": fraction_text(Q_UPPER),
        "gates": gates,
    }


def build_report() -> dict[str, Any]:
    previous_precision = ctx.prec
    try:
        ctx.dps = ARB_DECIMAL_DIGITS
        u = root_ball()
        rho = u - 1
        derivatives = derivative_certificate(u, rho)
        base_endpoint = base_endpoint_certificate()
        rate_ledger = exact_rate_ledger()
        target_ratio = u**2 / 4

        computed_gates = {
            "python_flint_version_is_frozen": (
                flint.__version__ == EXPECTED_PYTHON_FLINT_VERSION
            ),
            "flint_version_is_frozen": (
                flint.__FLINT_VERSION__ == EXPECTED_FLINT_VERSION
            ),
            "critical_root_has_certified_sign_bracket": (
                support.critical_polynomial(support.U_LOWER) < 0
                < support.critical_polynomial(support.U_UPPER)
            ),
            "target_ratio_is_between_59_over_100_and_3_over_5": (
                target_ratio > arb_fraction(Q_LOWER)
                and target_ratio < arb_fraction(Q_UPPER)
            ),
            **derivatives["gates"],
            "delta_5_below_cusp_radius": base_endpoint[
                "delta_5_below_cusp_radius"
            ],
            "sqrt_delta_5_below_27_over_500": base_endpoint[
                "sqrt_delta_5_below_27_over_500"
            ],
            **rate_ledger["gates"],
        }

        source_inputs = [
            SOURCE_LOCK,
            FORMAL_RESULT,
            "configs/source_locks/P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE.yaml",
            "formal/results/exact_uc_acip_sharp_cone_enclosure.md",
            "formal/results/exact_uc_acip_cone_enclosure.md",
            "formal/results/exact_uc_first_return_support.md",
            "artifacts/p4_logistic_uc_acip_sharp_cone_enclosure/interval_certificate.json",
            "experiments/p4_logistic_uc_first_return_support.py",
        ]

        return {
            "artifact_schema_version": 1,
            "audit_id": AUDIT_ID,
            "parent_audit_id": PARENT_AUDIT_ID,
            "formal_candidate": False,
            "status": "NUMERICALLY_CERTIFIED_BRANCH_MASS_RATIO_RATE",
            "source_lock": SOURCE_LOCK,
            "mathematical_object": {
                "map": "f(x)=1-U_c*x^2 on J=[-(U_c-1),1]",
                "endpoint_recursion": (
                    "psi(x)=sqrt((1-sqrt((1-x)/U_c))/U_c)"
                ),
                "branch_mass": "M_n=mu_ac(C_(2n))",
                "target_ratio": "q=U_c^2/4=1/(2*U_c*(U_c-1))",
            },
            "cusp_adapted_space": {
                "radius": "1/200",
                "definition": "v(t)=c*t^(-1/2)+b(t), b in L-infinity",
                "norm": "|c|+||b||_infinity",
                "physical_coefficient_lower": "0.09461",
                "physical_remainder_upper": "0.61",
            },
            "validated_environment": {
                "python": platform.python_version(),
                "python_flint": flint.__version__,
                "flint": flint.__FLINT_VERSION__,
                "arb_decimal_digits": ARB_DECIMAL_DIGITS,
            },
            "certified_root_ball": u.str(110),
            "target_ratio_ball": target_ratio.str(60),
            "derivative_certificate": derivatives,
            "base_endpoint_certificate": base_endpoint,
            "exact_rate_ledger": rate_ledger,
            "certified_statement": {
                "local": (
                    "|M_(n+1)/M_n-U_c^2/4| "
                    "<= (36/5)*sqrt(delta_(n-1)), n>=6"
                ),
                "exponential": (
                    "|M_(n+1)/M_n-U_c^2/4| "
                    "< (243/625)*(3/5)^(n-6), n>=6"
                ),
            },
            "computed_gates": computed_gates,
            "computed_gates_passed": all(computed_gates.values()),
            "error_budget": {
                "discretization": (
                    "none; one Arb interval covers the full local x-domain"
                ),
                "truncation": "none; every branch n>=6 is covered",
                "rounding": (
                    "100-digit Arb balls and exact Fraction inequalities"
                ),
                "normalization": (
                    "one common full-acip coefficient C_h is retained"
                ),
                "iteration_stopping": "none; no stationary iteration enters",
                "resolvent_tail": (
                    "none; the cusp remainder and endpoint recursion control the tail"
                ),
            },
            "claim_boundary": {
                "established": [
                    "an explicit cusp-adapted local Banach decomposition",
                    "a certified all-tail physical branch-mass-ratio rate",
                    "an explicit geometric upper bound from branch index n=6",
                ],
                "not_established": [
                    "an exact finite-n mass law or sharp ratio interval",
                    "an ordinary-BV spectral gap or transfer-operator resolvent",
                    "an arithmetic orbit law, determinant, quantization, Route B, or RH",
                ],
            },
            "route_a_effect": {
                "tuple_unchanged": [
                    "A1_WEAK",
                    "A2_FAIL",
                    "A3_FAIL",
                    "A4_FAIL",
                ],
                "local_verdict": "GO_WITH_LIMITATIONS",
                "parent_candidate_verdict": "REVISE",
            },
            "provenance": {
                "generator": GENERATOR,
                "generator_sha256": file_sha256(GENERATOR),
                "source_inputs_sha256": {
                    path: file_sha256(path) for path in source_inputs
                },
                "external_target_data_used": False,
                "reproduction_command": REPRODUCTION_COMMAND,
            },
        }
    finally:
        ctx.prec = previous_precision


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        default=(
            "artifacts/p4_logistic_uc_branch_mass_rate/"
            "rate_certificate.json"
        ),
    )
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    report = build_report()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    if not args.quiet:
        print(json.dumps(report, indent=2, sort_keys=True))
    if not report["computed_gates_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
