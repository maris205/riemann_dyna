#!/usr/bin/env python3
"""Structural audit for the exact-U_c physical-acip endpoint theorem."""

from __future__ import annotations

import argparse
from decimal import Decimal, ROUND_FLOOR, localcontext
import hashlib
import json
import platform
from pathlib import Path
from typing import Any


AUDIT_ID = "P4-LOGISTIC-UC-ACIP-ENDPOINT-DENSITY"
PARENT_AUDIT_ID = "P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK"
SOURCE_LOCK = "configs/source_locks/P4-LOGISTIC-UC-ACIP-ENDPOINT-DENSITY.yaml"
FORMAL_RESULT = "formal/results/exact_uc_acip_endpoint_density.md"
LITERATURE_AUDIT = "docs/literature/exact_uc_acip_density_sources.md"

DECIMAL_DIGITS = 180
ROOT_BRACKET_DIGITS = 100
POLAR_GRID_INTERVALS = 1024
T_EXPONENTS = (8, 16, 32, 64)
CHAIN_RULE_FRACTIONS = ((1, 8), (1, 3), (1, 2), (3, 4), (7, 8))
REPRODUCTION_COMMAND = (
    "python3 experiments/p4_logistic_uc_acip_endpoint_density.py --quiet "
    "--output artifacts/p4_logistic_uc_acip_endpoint_density/structural_audit.json"
)


def file_sha256(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def critical_polynomial(value: Decimal) -> Decimal:
    return value**3 - 2 * value**2 + 2 * value - 2


def decimal_root(precision: int = DECIMAL_DIGITS) -> Decimal:
    with localcontext() as context:
        context.prec = precision
        value = Decimal(
            "1.54368901269207636157085597180174798652520329765098393524"
        )
        for _ in range(40):
            polynomial = critical_polynomial(value)
            derivative = 3 * value**2 - 4 * value + 2
            update = polynomial / derivative
            value -= update
            if update == 0:
                break
        return value


def decimal_root_bracket(
    value: Decimal, digits: int = ROOT_BRACKET_DIGITS
) -> tuple[Decimal, Decimal]:
    quantum = Decimal(10) ** (-digits)
    lower_units = (value / quantum).to_integral_value(rounding=ROUND_FLOOR)
    lower = lower_units * quantum
    return lower, lower + quantum


def polar_derivative_squared(x: Decimal, u: Decimal) -> Decimal:
    numerator = Decimal(16) * (Decimal(1) - u * x * x) ** 2
    denominator = (
        u
        * (Decimal(2) - u * x * x)
        * (Decimal(1) - x * x)
    )
    return numerator / denominator


def reflected_map(x: Decimal, u: Decimal, rho: Decimal) -> Decimal:
    return rho - Decimal(2) * u**2 * x**2 + u**3 * x**4


def reflected_derivative(x: Decimal, u: Decimal) -> Decimal:
    return -Decimal(4) * u**2 * x * (Decimal(1) - u * x**2)


def polar_chain_rule_derivative_squared(
    x: Decimal, u: Decimal, rho: Decimal
) -> Decimal:
    sx = reflected_map(x, u, rho)
    derivative = reflected_derivative(x, u)
    return (
        derivative**2
        * (rho**2 - x**2)
        / (rho**2 - sx**2)
    )


def polar_chain_rule_rows(
    u: Decimal, rho: Decimal
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for numerator, denominator in CHAIN_RULE_FRACTIONS:
        fraction = Decimal(numerator) / Decimal(denominator)
        x = rho * fraction
        closed_form = polar_derivative_squared(x, u)
        chain_rule = polar_chain_rule_derivative_squared(x, u, rho)
        rows.append(
            {
                "x_over_rho": f"{numerator}/{denominator}",
                "x": str(x),
                "closed_form_derivative_squared": str(closed_form),
                "independent_chain_rule_derivative_squared": str(chain_rule),
                "relative_error": str(abs(closed_form / chain_rule - Decimal(1))),
            }
        )
    return rows


def positive_t_inverse(y: Decimal, u: Decimal) -> Decimal:
    inner = ((Decimal(1) - y) / u).sqrt()
    return ((Decimal(1) - inner) / u).sqrt()


def inverse_jacobian_rows(u: Decimal, rho: Decimal) -> list[dict[str, str]]:
    target = Decimal(1) / (Decimal(2).sqrt() * u)
    rows: list[dict[str, str]] = []
    for exponent in T_EXPONENTS:
        t = Decimal(10) ** (-exponent)
        y = -rho + t
        x = positive_t_inverse(y, u)
        fx = Decimal(1) - u * x * x
        positive_derivative = Decimal(4) * u * u * x * fx
        negative_derivative = -positive_derivative
        positive_inverse_jacobian = Decimal(1) / abs(positive_derivative)
        negative_inverse_jacobian = Decimal(1) / abs(negative_derivative)
        two_branch_inverse_jacobian = (
            positive_inverse_jacobian + negative_inverse_jacobian
        )
        positive_inverse_residual = -reflected_map(x, u, rho) - y
        negative_inverse_residual = -reflected_map(-x, u, rho) - y
        scaled = t.sqrt() * two_branch_inverse_jacobian
        rows.append(
            {
                "t_exponent": str(exponent),
                "positive_inverse_x": str(x),
                "negative_inverse_x": str(-x),
                "positive_T_inverse_residual": str(positive_inverse_residual),
                "negative_T_inverse_residual": str(negative_inverse_residual),
                "positive_absolute_inverse_jacobian": str(
                    positive_inverse_jacobian
                ),
                "negative_absolute_inverse_jacobian": str(
                    negative_inverse_jacobian
                ),
                "sqrt_t_times_two_branch_inverse_jacobian": str(scaled),
                "target_coefficient_for_unit_density_at_zero": str(target),
                "relative_error": str(abs(scaled / target - Decimal(1))),
            }
        )
    return rows


def build_report() -> dict[str, Any]:
    with localcontext() as context:
        context.prec = DECIMAL_DIGITS
        u = decimal_root(DECIMAL_DIGITS)
        rho = u - 1
        polynomial_residual = critical_polynomial(u)
        root_lower, root_upper = decimal_root_bracket(u)
        root_lower_residual = critical_polynomial(root_lower)
        root_upper_residual = critical_polynomial(root_upper)

        band_identity_residual = u * rho**2 - (Decimal(1) - rho)
        multiplier_identity_residual = u**3 * rho - Decimal(2)

        expansion_lower_bound = Decimal(4) / u**2
        fixed_postcritical_multiplier = Decimal(2) * u * rho
        endpoint_length_ratio = Decimal(1) / (
            Decimal(4) * u**2 * rho**2
        )
        endpoint_mass_ratio = Decimal(1) / (Decimal(2) * u * rho)
        mass_ratio_u_squared = u**2 / Decimal(4)

        sampled_values: list[Decimal] = []
        for index in range(POLAR_GRID_INTERVALS + 1):
            x = rho * Decimal(index) / Decimal(POLAR_GRID_INTERVALS)
            sampled_values.append(polar_derivative_squared(x, u))
        sampled_strictly_decreasing = all(
            right < left
            for left, right in zip(sampled_values, sampled_values[1:])
        )
        sampled_maximum = max(sampled_values).sqrt()
        sampled_minimum = min(sampled_values).sqrt()

        chain_rule_rows = polar_chain_rule_rows(u, rho)
        maximum_chain_rule_relative_error = max(
            Decimal(row["relative_error"]) for row in chain_rule_rows
        )
        endpoint_mapping_residuals = {
            "S_0_minus_rho": reflected_map(Decimal(0), u, rho) - rho,
            "S_rho_plus_rho": reflected_map(rho, u, rho) + rho,
            "S_minus_rho_plus_rho": reflected_map(-rho, u, rho) + rho,
        }

        inverse_rows = inverse_jacobian_rows(u, rho)
        final_inverse_relative_error = Decimal(inverse_rows[-1]["relative_error"])
        maximum_inverse_residual = max(
            abs(Decimal(row[key]))
            for row in inverse_rows
            for key in (
                "positive_T_inverse_residual",
                "negative_T_inverse_residual",
            )
        )

        computed_gates = {
            "critical_polynomial_residual_below_1e_170": abs(polynomial_residual)
            < Decimal("1e-170"),
            "critical_root_has_100_digit_sign_bracket": (
                root_lower_residual < 0 < root_upper_residual
                and root_upper - root_lower == Decimal("1e-100")
            ),
            "band_identity_residual_below_1e_170": abs(band_identity_residual)
            < Decimal("1e-170"),
            "multiplier_identity_residual_below_1e_170": abs(
                multiplier_identity_residual
            )
            < Decimal("1e-170"),
            "reflected_branch_endpoint_mapping_is_exact": all(
                abs(residual) < Decimal("1e-170")
                for residual in endpoint_mapping_residuals.values()
            ),
            "polar_grid_is_strictly_monotone_decreasing": (
                sampled_strictly_decreasing
            ),
            "polar_closed_form_matches_independent_chain_rule": (
                maximum_chain_rule_relative_error < Decimal("1e-170")
            ),
            "polar_sampled_minimum_matches_exact_bound": abs(
                sampled_minimum - expansion_lower_bound
            )
            < Decimal("1e-170"),
            "polar_sampled_maximum_matches_center_value": abs(
                sampled_maximum**2 - Decimal(8) / u
            )
            < Decimal("1e-170"),
            "uniform_expansion_margin_is_positive": expansion_lower_bound > 1,
            "equivalent_mass_ratio_forms_match": abs(
                endpoint_mass_ratio - mass_ratio_u_squared
            )
            < Decimal("1e-170"),
            "inverse_jacobian_coefficient_converges": final_inverse_relative_error
            < Decimal("1e-7"),
            "reported_points_are_two_exact_inverse_branches": (
                maximum_inverse_residual < Decimal("1e-170")
            ),
        }

        return {
            "artifact_schema_version": 2,
            "audit_id": AUDIT_ID,
            "parent_audit_id": PARENT_AUDIT_ID,
            "formal_candidate": False,
            "source_lock": SOURCE_LOCK,
            "provenance": {
                "generator": "experiments/p4_logistic_uc_acip_endpoint_density.py",
                "generator_sha256": file_sha256(__file__),
                "python_implementation": platform.python_implementation(),
                "python_version": platform.python_version(),
                "decimal_context_digits": DECIMAL_DIGITS,
                "source_inputs_sha256": {
                    SOURCE_LOCK: file_sha256(SOURCE_LOCK),
                    FORMAL_RESULT: file_sha256(FORMAL_RESULT),
                    LITERATURE_AUDIT: file_sha256(LITERATURE_AUDIT),
                },
                "reproduction_command": REPRODUCTION_COMMAND,
                "external_target_data_used": False,
            },
            "mathematical_object": {
                "map": "f(x)=1-U_c*x^2",
                "physical_core": "J=[-(U_c-1),1]",
                "parity_reduced_map": "T=f^2 on A=[-rho,rho]",
                "proof_conjugate": (
                    "G=arcsin(S(rho*sin(theta))/rho), S=-T, with two full branches"
                ),
                "measure": "unique f-acip mu_ac on J, normalized by mu_ac(J)=1",
                "density": (
                    "canonical h=d mu_ac/dx, locally Lipschitz and positive at x=0"
                ),
            },
            "constants": {
                "U_c": str(u),
                "rho": str(rho),
                "critical_polynomial_residual": str(polynomial_residual),
                "U_c_100_digit_lower_bound": str(root_lower),
                "U_c_100_digit_upper_bound": str(root_upper),
                "U_c_lower_polynomial_value": str(root_lower_residual),
                "U_c_upper_polynomial_value": str(root_upper_residual),
                "U_c_times_rho_squared_identity_residual": str(
                    band_identity_residual
                ),
                "U_c_cubed_times_rho_identity_residual": str(
                    multiplier_identity_residual
                ),
                "uniform_expansion_lower_bound": str(expansion_lower_bound),
                "fixed_postcritical_multiplier": str(
                    fixed_postcritical_multiplier
                ),
                "endpoint_length_ratio": str(endpoint_length_ratio),
                "endpoint_mass_ratio": str(endpoint_mass_ratio),
                "endpoint_mass_ratio_as_U_c_squared_over_4": str(
                    mass_ratio_u_squared
                ),
                "unit_density_endpoint_coefficient": str(
                    Decimal(1) / (Decimal(2).sqrt() * u)
                ),
            },
            "formal_claims": {
                "polar_full_branch_uniform_expansion": {
                    "status": "PROVED",
                    "source": FORMAL_RESULT,
                    "statement": "inf|G'|=4/U_c^2=2*U_c*rho>1",
                },
                "physical_acip_existence_uniqueness_full_support": {
                    "status": "PROVED",
                    "source": FORMAL_RESULT,
                    "dependency": (
                        "Jiang-Ruelle 2005: Main Theorem setup, Assumption A, "
                        "Markov graph, and Properties of L"
                    ),
                },
                "endpoint_density": {
                    "status": "PROVED",
                    "source": FORMAL_RESULT,
                    "statement": (
                        "h(-rho+t)=h(0)/(sqrt(2)*U_c)*t^(-1/2)+O(1)"
                    ),
                },
                "physical_branch_mass_ratio": {
                    "status": "PROVED",
                    "source": FORMAL_RESULT,
                    "statement": (
                        "mu(C_(2n+2))/mu(C_(2n))->1/(2*U_c*(U_c-1))"
                    ),
                },
                "raw_first_return_uniform_expansion": {
                    "status": "REFUTED",
                    "source": (
                        "formal/obstructions/exact_uc_first_return_nonuniform_expansion.md"
                    ),
                    "unchanged_by_this_audit": True,
                },
            },
            "published_cross_checks": {
                "jiang_ruelle_2005": {
                    "doi": "10.1088/0951-7715/18/6/002",
                    "arxiv": "math/0501161",
                    "location": (
                        "opening Main Theorem, Assumption A, Markovian graph, "
                        "and Properties of L"
                    ),
                    "role": "RPF proof input",
                },
                "ruelle_2009": {
                    "doi": "10.1007/s00220-008-0637-8",
                    "arxiv": "0710.2015",
                    "location": "Theorem 9 and Remark 16(a)",
                },
                "baladi_smania_2021": {
                    "doi": "10.1007/s00220-021-04015-z",
                    "arxiv": "2008.01654v4",
                    "location": (
                        "corrected equation (1.1) in the 2023 supplementary note; "
                        "leading C_k^(0) coefficient unchanged"
                    ),
                },
                "audit": LITERATURE_AUDIT,
            },
            "computed_diagnostics": {
                "decimal_digits": DECIMAL_DIGITS,
                "root_bracket_digits": ROOT_BRACKET_DIGITS,
                "polar_grid_intervals": POLAR_GRID_INTERVALS,
                "sampled_polar_maximum": str(sampled_maximum),
                "sampled_polar_minimum": str(sampled_minimum),
                "polar_chain_rule_rows": chain_rule_rows,
                "maximum_chain_rule_relative_error": str(
                    maximum_chain_rule_relative_error
                ),
                "maximum_T_inverse_residual": str(maximum_inverse_residual),
                "reflected_endpoint_mapping_residuals": {
                    key: str(value)
                    for key, value in endpoint_mapping_residuals.items()
                },
                "inverse_jacobian_rows": inverse_rows,
            },
            "computed_gates": computed_gates,
            "computed_diagnostics_passed": all(computed_gates.values()),
            "route_a_effect": {
                "tuple": "(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)",
                "overall": "ROUTE_A_EXPLORATORY",
                "local_endpoint_audit_verdict": "GO_WITH_LIMITATIONS",
                "candidate_recommended_verdict": "REVISE",
                "formal_candidate_created": False,
                "route_b_invocation_allowed": False,
            },
            "claim_boundary": {
                "established": [
                    "the exact endpoint inverse-square-root density law",
                    "the positive coefficient h(0)/(sqrt(2)*U_c)",
                    "the asymptotic physical even-branch mass ratio",
                    "unconditional positive mass for every physical even branch",
                ],
                "not_established": [
                    "a closed form or rigorous numerical enclosure for h(0)",
                    "an exact finite-n geometric branch-weight law",
                    "an arithmetic primitive-orbit correspondence or von-Mangoldt law",
                    "an s-dependent Fredholm/completed-xi determinant",
                    "natural quantization, Route B, Hilbert-Polya, or RH",
                ],
            },
            "next_smallest_task": (
                "Use the uniformly expanding polar coordinate to obtain a rigorous "
                "numerical enclosure of h(0), hence of the absolute endpoint "
                "coefficient and selected finite branch masses, without target data."
            ),
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default=(
            "artifacts/p4_logistic_uc_acip_endpoint_density/structural_audit.json"
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
