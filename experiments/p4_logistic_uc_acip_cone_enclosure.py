#!/usr/bin/env python3
"""Certified coarse ACIP bounds from the polar inverse-branch cone."""

from __future__ import annotations

import argparse
from decimal import (
    Decimal,
    ROUND_CEILING,
    ROUND_FLOOR,
    ROUND_HALF_EVEN,
    localcontext,
)
from fractions import Fraction
import hashlib
import json
import platform
from pathlib import Path
from typing import Any

try:
    from experiments import p4_logistic_uc_first_return_support as support
except ModuleNotFoundError:  # Direct execution from the repository root.
    import p4_logistic_uc_first_return_support as support


AUDIT_ID = "P4-LOGISTIC-UC-ACIP-CONE-ENCLOSURE"
PARENT_AUDIT_ID = "P4-LOGISTIC-UC-ACIP-ENDPOINT-DENSITY"
SOURCE_LOCK = "configs/source_locks/P4-LOGISTIC-UC-ACIP-CONE-ENCLOSURE.yaml"
FORMAL_RESULT = "formal/results/exact_uc_acip_cone_enclosure.md"

DECIMAL_DIGITS = 180
OUTPUT_PLACES = 40
REPORTED_BRANCH_INDICES = (6, 7, 8, 9)

KAPPA_STAR = Fraction(3, 5)
DISTORTION_STAR = Fraction(3, 10)
CONE_SLOPE = Fraction(3, 4)
LOCAL_X_RADIUS = Fraction(1, 20)
ENDPOINT_T_RADIUS = Fraction(1, 200)
W_GLOBAL_STAR = Fraction(9, 5)
H_LIPSCHITZ_STAR = Fraction(27, 10)
ENDPOINT_REMAINDER_STAR = Fraction(61, 100)

PI_PREFIX_DIGITS = (
    "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
)
PI_LOWER = Decimal("3." + PI_PREFIX_DIGITS)
with localcontext() as _pi_context:
    _pi_context.prec = len(PI_PREFIX_DIGITS) + 10
    PI_UPPER = PI_LOWER + Decimal(1).scaleb(-len(PI_PREFIX_DIGITS))


def alternating_atan_interval(x: Fraction, terms: int) -> tuple[Fraction, Fraction]:
    """Exact alternating-series enclosure for atan(x), 0 < x < 1."""

    partial = Fraction(0)
    for index in range(terms):
        partial += (-1) ** index * x ** (2 * index + 1) / (2 * index + 1)
    next_term = (-1) ** terms * x ** (2 * terms + 1) / (2 * terms + 1)
    endpoint = partial + next_term
    return (partial, endpoint) if partial <= endpoint else (endpoint, partial)


def machin_pi_interval() -> tuple[Fraction, Fraction]:
    """Certify pi with Machin's identity and alternating rational series."""

    atan_one_fifth = alternating_atan_interval(Fraction(1, 5), 100)
    atan_one_239 = alternating_atan_interval(Fraction(1, 239), 30)
    # pi = 16 atan(1/5) - 4 atan(1/239); the negative coefficient reverses
    # the second interval's endpoints.
    lower = 16 * atan_one_fifth[0] - 4 * atan_one_239[1]
    upper = 16 * atan_one_fifth[1] - 4 * atan_one_239[0]
    return lower, upper


PI_MACHIN_LOWER, PI_MACHIN_UPPER = machin_pi_interval()


def fraction_from_decimal(value: Decimal) -> Fraction:
    numerator, denominator = value.as_integer_ratio()
    return Fraction(numerator, denominator)

REPRODUCTION_COMMAND = (
    "python3 experiments/p4_logistic_uc_acip_cone_enclosure.py --quiet "
    "--output artifacts/p4_logistic_uc_acip_cone_enclosure/certified_bounds.json"
)


def file_sha256(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def decimal_from_fraction(
    value: Fraction, rounding: str = ROUND_HALF_EVEN
) -> Decimal:
    with localcontext() as context:
        context.prec = DECIMAL_DIGITS
        context.rounding = rounding
        return Decimal(value.numerator) / Decimal(value.denominator)


def outward(value: Decimal, direction: str) -> Decimal:
    quantum = Decimal(1).scaleb(-OUTPUT_PLACES)
    rounding = ROUND_FLOOR if direction == "lower" else ROUND_CEILING
    return value.quantize(quantum, rounding=rounding)


def interval_text(lower: Decimal, upper: Decimal) -> dict[str, str]:
    return {
        "lower": str(outward(lower, "lower")),
        "upper": str(outward(upper, "upper")),
    }


def fraction_interval_to_decimals(
    lower: Fraction, upper: Fraction
) -> tuple[Decimal, Decimal]:
    return (
        decimal_from_fraction(lower, ROUND_FLOOR),
        decimal_from_fraction(upper, ROUND_CEILING),
    )


def endpoint_delta_intervals(
    count: int,
) -> tuple[list[tuple[Fraction, Fraction]], list[tuple[Fraction, Fraction]]]:
    r_intervals = support.certified_endpoint_intervals(count)
    rho_lower = support.U_LOWER - 1
    rho_upper = support.U_UPPER - 1
    delta_intervals = [
        (rho_lower - r_upper, rho_upper - r_lower)
        for r_lower, r_upper in r_intervals
    ]
    return r_intervals, delta_intervals


def finite_branch_mass_rows(
    c_lower: Decimal, c_upper: Decimal
) -> list[dict[str, Any]]:
    max_index = max(REPORTED_BRANCH_INDICES)
    r_intervals, delta_intervals = endpoint_delta_intervals(max_index)
    remainder = decimal_from_fraction(ENDPOINT_REMAINDER_STAR)
    t_radius = decimal_from_fraction(ENDPOINT_T_RADIUS)
    rows: list[dict[str, Any]] = []

    for index in REPORTED_BRANCH_INDICES:
        previous_delta_lower, previous_delta_upper = delta_intervals[index - 1]
        delta_lower, delta_upper = delta_intervals[index]
        branch_length_lower = r_intervals[index][0] - r_intervals[index - 1][1]
        branch_length_upper = r_intervals[index][1] - r_intervals[index - 1][0]

        previous_lower_d, previous_upper_d = fraction_interval_to_decimals(
            previous_delta_lower, previous_delta_upper
        )
        delta_lower_d, delta_upper_d = fraction_interval_to_decimals(
            delta_lower, delta_upper
        )
        length_lower_d, length_upper_d = fraction_interval_to_decimals(
            branch_length_lower, branch_length_upper
        )

        previous_sqrt_lower, previous_sqrt_upper = support.sqrt_interval(
            previous_delta_lower, previous_delta_upper
        )
        delta_sqrt_lower, delta_sqrt_upper = support.sqrt_interval(
            delta_lower, delta_upper
        )
        sqrt_difference_lower = (
            decimal_from_fraction(previous_sqrt_lower, ROUND_FLOOR)
            - decimal_from_fraction(delta_sqrt_upper, ROUND_CEILING)
        )
        sqrt_difference_upper = (
            decimal_from_fraction(previous_sqrt_upper, ROUND_CEILING)
            - decimal_from_fraction(delta_sqrt_lower, ROUND_FLOOR)
        )
        mass_lower = (
            Decimal(2) * c_lower * sqrt_difference_lower
            - remainder * length_upper_d
        )
        mass_upper = (
            Decimal(2) * c_upper * sqrt_difference_upper
            + remainder * length_upper_d
        )
        mass_lower = max(Decimal(0), mass_lower)

        rows.append(
            {
                "n": index,
                "physical_return_label": 2 * index,
                "delta_n_minus_1": interval_text(
                    previous_lower_d, previous_upper_d
                ),
                "delta_n": interval_text(delta_lower_d, delta_upper_d),
                "branch_length": interval_text(length_lower_d, length_upper_d),
                "sqrt_delta_difference": interval_text(
                    sqrt_difference_lower, sqrt_difference_upper
                ),
                "endpoint_radius_gate_passed": previous_upper_d <= t_radius,
                "certified_mass": interval_text(mass_lower, mass_upper),
            }
        )
    return rows


def build_report() -> dict[str, Any]:
    with localcontext() as context:
        context.prec = DECIMAL_DIGITS

        u_lower = support.U_LOWER
        u_upper = support.U_UPPER
        rho_lower = u_lower - 1
        rho_upper = u_upper - 1

        e_rho_upper = Fraction(3, 4) / rho_lower - Fraction(1, 2) / u_upper
        t_speed_squared_upper = rho_upper * (u_upper**2 - 2) / 4

        exact_gates = {
            "pi_has_100_digit_outward_bracket": (
                PI_LOWER < PI_UPPER
                and PI_UPPER - PI_LOWER
                == Decimal(1).scaleb(-len(PI_PREFIX_DIGITS))
            ),
            "pi_bracket_is_certified_by_machin_series": (
                fraction_from_decimal(PI_LOWER) <= PI_MACHIN_LOWER
                and PI_MACHIN_UPPER <= fraction_from_decimal(PI_UPPER)
            ),
            "critical_root_has_certified_sign_bracket": (
                support.critical_polynomial(u_lower) < 0
                < support.critical_polynomial(u_upper)
            ),
            "inverse_contraction_below_three_fifths": (
                u_upper**2 / 4 < KAPPA_STAR
            ),
            "E_rho_below_eleven_tenths": e_rho_upper < Fraction(11, 10),
            "t_speed_below_one_quarter": (
                t_speed_squared_upper < Fraction(1, 16)
            ),
            "log_weight_distortion_below_three_tenths": (
                Fraction(11, 10) * Fraction(1, 4) < DISTORTION_STAR
            ),
            "cone_is_forward_invariant": (
                DISTORTION_STAR + KAPPA_STAR * CONE_SLOPE
                <= CONE_SLOPE
            ),
            "local_coordinate_derivative_exceeds_0_54": (
                rho_lower**2 - LOCAL_X_RADIUS**2 > Fraction(27, 50) ** 2
            ),
            "endpoint_preimage_stays_inside_local_radius": (
                1 - ENDPOINT_T_RADIUS / u_lower > Fraction(499, 500) ** 2
                and ENDPOINT_T_RADIUS / Fraction(3, 2) ** 2
                < LOCAL_X_RADIUS**2
            ),
        }

        a = decimal_from_fraction(CONE_SLOPE)
        half_length_lower = PI_LOWER / 2
        half_length_upper = PI_UPPER / 2
        exp_upper = (a * half_length_upper).exp()
        exp_negative_lower = (-a * half_length_lower).exp()

        w_zero_lower = a / (2 * (exp_upper - 1))
        w_zero_upper = a / (2 * (1 - exp_negative_lower))

        u_lower_d, u_upper_d = fraction_interval_to_decimals(u_lower, u_upper)
        rho_lower_d, rho_upper_d = fraction_interval_to_decimals(
            rho_lower, rho_upper
        )
        sqrt_two_lower, sqrt_two_upper = support.sqrt_interval(
            Fraction(2), Fraction(2)
        )
        sqrt_two_lower_d = decimal_from_fraction(sqrt_two_lower, ROUND_FLOOR)
        sqrt_two_upper_d = decimal_from_fraction(sqrt_two_upper, ROUND_CEILING)

        g_zero_lower = w_zero_lower / rho_upper_d
        g_zero_upper = w_zero_upper / rho_lower_d
        h_zero_lower = g_zero_lower / 2
        h_zero_upper = g_zero_upper / 2
        coefficient_lower = w_zero_lower / (
            2 * rho_upper_d * sqrt_two_upper_d * u_upper_d
        )
        coefficient_upper = w_zero_upper / (
            2 * rho_lower_d * sqrt_two_lower_d * u_lower_d
        )

        w_global_upper = w_zero_upper * exp_upper
        d_star = Fraction(27, 50)
        derived_lipschitz_bound = W_GLOBAL_STAR * (
            CONE_SLOPE / (2 * d_star**2)
            + LOCAL_X_RADIUS / (2 * d_star**3)
        )
        h_derivative_bound = Fraction(27, 10)
        a_min = Fraction(499, 500)
        h_factor_derivative_bound = Fraction(11, 10)
        sqrt_t_bound = Fraction(71, 1000)
        endpoint_remainder_derived = (
            h_derivative_bound
            / (2 * Fraction(3, 2) ** 2 * a_min)
            + Fraction(1, 2)
            * h_factor_derivative_bound
            * sqrt_t_bound
            / (
                2
                * Fraction(3, 2) ** 2
                * (1 + a_min)
            )
        )

        exact_gates.update(
            {
                "global_theta_density_below_nine_fifths": (
                    w_global_upper < decimal_from_fraction(W_GLOBAL_STAR)
                ),
                "full_density_at_zero_below_one_half": h_zero_upper
                < Decimal("0.5"),
                "local_h_lipschitz_bound_below_2_7": (
                    derived_lipschitz_bound < h_derivative_bound
                ),
                "endpoint_factor_derivative_below_1_1": (
                    Fraction(3, 1)
                    / (
                        2
                        * a_min**2
                        * Fraction(7, 5)
                    )
                    < h_factor_derivative_bound
                ),
                "sqrt_t_radius_below_0_071": (
                    ENDPOINT_T_RADIUS < sqrt_t_bound**2
                ),
                "endpoint_remainder_below_0_61": (
                    endpoint_remainder_derived < ENDPOINT_REMAINDER_STAR
                ),
            }
        )

        mass_rows = finite_branch_mass_rows(
            outward(coefficient_lower, "lower"),
            outward(coefficient_upper, "upper"),
        )
        exact_gates["all_reported_branch_masses_inside_endpoint_radius"] = all(
            row["endpoint_radius_gate_passed"] for row in mass_rows
        )

        source_inputs = [
            SOURCE_LOCK,
            FORMAL_RESULT,
            "formal/results/exact_uc_acip_endpoint_density.md",
            "formal/results/exact_uc_first_return_support.md",
            "experiments/p4_logistic_uc_first_return_support.py",
        ]

        return {
            "artifact_schema_version": 1,
            "audit_id": AUDIT_ID,
            "parent_audit_id": PARENT_AUDIT_ID,
            "formal_candidate": False,
            "status": "CERTIFIED_COARSE_ENCLOSURE",
            "source_lock": SOURCE_LOCK,
            "mathematical_object": {
                "map": "f(x)=1-U_c*x^2 on J=[-(U_c-1),1]",
                "polar_map": (
                    "G=q^(-1) o (-f^2) o q, q(theta)=(U_c-1)*sin(theta)"
                ),
                "invariant_density": (
                    "w(theta) dtheta is the conditional f^2-acip on A; "
                    "g_A(0)=w(0)/rho and the full f-acip has h(0)=g_A(0)/2"
                ),
                "target": (
                    "coarse certified bounds for w(0), g_A(0), h(0), "
                    "the endpoint coefficient, and selected finite physical branch masses"
                ),
            },
            "certified_root_bracket": {
                "U_c_lower": support.U_LOWER_TEXT,
                "U_c_upper": support.U_UPPER_TEXT,
                "pi_lower": str(PI_LOWER),
                "pi_upper": str(PI_UPPER),
                "pi_certificate": {
                    "identity": "pi=16*atan(1/5)-4*atan(1/239)",
                    "atan_1_over_5_terms": 100,
                    "atan_1_over_239_terms": 30,
                    "series_interval_width_upper_decimal": str(
                        decimal_from_fraction(
                            PI_MACHIN_UPPER - PI_MACHIN_LOWER,
                            ROUND_CEILING,
                        )
                    ),
                },
            },
            "cone_ledger": {
                "inverse_branch_contraction_upper": "3/5",
                "log_inverse_weight_derivative_upper": "3/10",
                "log_lipschitz_cone_slope": "3/4",
                "invariance_inequality": "3/10 + (3/5)*(3/4) = 3/4",
                "exact_inverse_contraction": "U_c^2/4",
                "distortion_parameter": (
                    "t=sqrt((1+rho*sin(eta))/U_c), "
                    "a=(1/4)*sqrt((1+t)*(rho+t))/t"
                ),
                "distortion_bound": (
                    "|d_eta log(a)| <= E(rho)*max|t'| < "
                    "(11/10)*(1/4) < 3/10"
                ),
            },
            "certified_enclosures": {
                "conditional_theta_density_w_0": interval_text(
                    w_zero_lower, w_zero_upper
                ),
                "conditional_x_density_g_A_0": interval_text(
                    g_zero_lower, g_zero_upper
                ),
                "full_physical_density_h_0": interval_text(
                    h_zero_lower, h_zero_upper
                ),
                "endpoint_coefficient_C_h": interval_text(
                    coefficient_lower, coefficient_upper
                ),
                "normalization_identity": "g_A(0)=2*h(0)",
            },
            "explicit_endpoint_remainder": {
                "t_range": "0 < t <= 1/200",
                "statement": (
                    "|h(-rho+t)-C_h*t^(-1/2)| <= 61/100"
                ),
                "local_x_radius": "1/20",
                "global_w_upper": "9/5",
                "local_h_lipschitz_upper": "27/10",
            },
            "finite_branch_mass_enclosures": mass_rows,
            "computed_gates": exact_gates,
            "computed_gates_passed": all(exact_gates.values()),
            "error_budget": {
                "discretization": (
                    "not used; the cone proof covers the full closed theta interval"
                ),
                "truncation": (
                    "not used; no finite branch or operator truncation is used in the density bound"
                ),
                "rounding": (
                    "algebraic gates use exact Fraction arithmetic; Decimal values are computed at 180 digits and widened outward at 40 places"
                ),
                "normalization": (
                    "w is normalized on I, then g_A(0)=w(0)/rho and h(0)=g_A(0)/2"
                ),
                "iteration_stopping": (
                    "not used; no iterative stationary-vector solve enters the certificate"
                ),
                "resolvent_tail": (
                    "not used; the forward-invariant log-Lipschitz cone supplies the global bound"
                ),
                "interval_rounding": (
                    "all displayed bounds are widened outward to 40 decimal places; "
                    "algebraic gates use exact Fraction arithmetic"
                ),
                "inverse_branch_evaluation": (
                    "closed-form inverse weights plus the certified 100-digit U_c bracket"
                ),
                "finite_rank_projection_or_quadrature": (
                    "not used by the certified enclosure; any Ulam value is numerical evidence only"
                ),
                "invariant_vector_residual": (
                    "not used; the existing expanding-Markov RPF theorem supplies the unique fixed density"
                ),
                "truncation_or_resolvent_tail": (
                    "not used; the forward-invariant log-Lipschitz cone gives direct global bounds"
                ),
                "normalization_conversion": (
                    "w(0) -> g_A(0)=w(0)/rho -> h(0)=g_A(0)/2; "
                    "C_h=h(0)/(sqrt(2)*U_c)"
                ),
                "finite_branch_remainder": (
                    "the explicit 61/100 density remainder is integrated over each branch length"
                ),
            },
            "claim_boundary": {
                "established": [
                    "a coarse target-free certified enclosure of h(0)",
                    "an explicit endpoint O(1) constant on 0<t<=1/200",
                    "certified absolute-mass intervals for C_12, C_14, C_16, and C_18",
                ],
                "not_established": [
                    "a sharp validated Ulam enclosure or a validated finite-rank resolvent bound",
                    "an exact finite-order geometric mass law",
                    "a prime-orbit law, s-dependent determinant, quantization, Route B, or RH",
                ],
            },
            "route_a_effect": {
                "tuple_unchanged": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                "local_verdict": "GO_WITH_LIMITATIONS",
                "parent_candidate_verdict": "REVISE",
            },
            "provenance": {
                "python": platform.python_version(),
                "generator": __file__,
                "generator_sha256": file_sha256(__file__),
                "source_inputs_sha256": {
                    path: file_sha256(path) for path in source_inputs
                },
                "external_target_data_used": False,
                "reproduction_command": REPRODUCTION_COMMAND,
            },
        }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        default=(
            "artifacts/p4_logistic_uc_acip_cone_enclosure/certified_bounds.json"
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


if __name__ == "__main__":
    main()
