#!/usr/bin/env python3
"""Exact-U_c physical-core and ambient first-return support audit."""

from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
from fractions import Fraction
from math import isqrt
import json
from pathlib import Path
from typing import Any


AUDIT_ID = "P4-LOGISTIC-UC-FIRST-RETURN-SUPPORT"
PARENT_AUDIT_ID = "P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK"
SOURCE_LOCK = "configs/source_locks/P4-LOGISTIC-UC-FIRST-RETURN-SUPPORT.yaml"

U_LOWER_TEXT = (
    "1.5436890126920763615708559718017479865252032976509839352408040378311686739279738664851579145760591254"
)
U_UPPER_TEXT = (
    "1.5436890126920763615708559718017479865252032976509839352408040378311686739279738664851579145760591255"
)

RATIONAL_SQRT_SCALE_DIGITS = 130
RATIONAL_CERTIFIED_BRANCHES = 154
HIGH_PRECISION_DIGITS = 180
HIGH_PRECISION_DIAGNOSTIC_BRANCHES = 64
REPORTED_ENDPOINT_ROWS = 16
DERIVATIVE_COUNTEREXAMPLE_X = Decimal("-0.01")


def fraction_from_decimal(text: str) -> Fraction:
    whole, fractional = text.split(".")
    return Fraction(int(whole + fractional), 10 ** len(fractional))


U_LOWER = fraction_from_decimal(U_LOWER_TEXT)
U_UPPER = fraction_from_decimal(U_UPPER_TEXT)
SQRT_SCALE = 10**RATIONAL_SQRT_SCALE_DIGITS


def critical_polynomial(value: Fraction) -> Fraction:
    return value**3 - 2 * value**2 + 2 * value - 2


def sqrt_floor_fraction(value: Fraction, scale: int = SQRT_SCALE) -> Fraction:
    if value < 0:
        raise ValueError("square-root argument must be nonnegative")
    scaled_floor = (value.numerator * scale * scale) // value.denominator
    return Fraction(isqrt(scaled_floor), scale)


def sqrt_ceil_fraction(value: Fraction, scale: int = SQRT_SCALE) -> Fraction:
    lower = sqrt_floor_fraction(value, scale)
    if lower * lower == value:
        return lower
    return lower + Fraction(1, scale)


def sqrt_interval(
    lower: Fraction, upper: Fraction, scale: int = SQRT_SCALE
) -> tuple[Fraction, Fraction]:
    if lower > upper:
        raise ValueError("invalid interval")
    return sqrt_floor_fraction(lower, scale), sqrt_ceil_fraction(upper, scale)


def h_interval(
    y_lower: Fraction,
    y_upper: Fraction,
    *,
    u_lower: Fraction = U_LOWER,
    u_upper: Fraction = U_UPPER,
) -> tuple[Fraction, Fraction]:
    """Outward interval for h(y)=sqrt((1-y)/u), decreasing in y and u."""

    quotient_lower = (1 - y_upper) / u_upper
    quotient_upper = (1 - y_lower) / u_lower
    return sqrt_interval(quotient_lower, quotient_upper)


def positive_t_inverse_interval(
    y_lower: Fraction, y_upper: Fraction
) -> tuple[Fraction, Fraction]:
    """Outward interval for psi=h composed with h, the positive inverse of T=f^2."""

    inner_lower, inner_upper = h_interval(y_lower, y_upper)
    return h_interval(inner_lower, inner_upper)


def certified_endpoint_intervals(
    count: int = RATIONAL_CERTIFIED_BRANCHES,
) -> list[tuple[Fraction, Fraction]]:
    rows = [(Fraction(0), Fraction(0))]
    for _ in range(count):
        rows.append(positive_t_inverse_interval(*rows[-1]))
    return rows


def scaled_integer(value: Fraction, scale: int = SQRT_SCALE) -> int:
    scaled = value * scale
    if scaled.denominator != 1:
        raise ArithmeticError("endpoint bound is not on the frozen rational scale")
    return scaled.numerator


def decimal_root(precision: int = HIGH_PRECISION_DIGITS) -> Decimal:
    with localcontext() as context:
        context.prec = precision
        value = Decimal("1.54368901269207636")
        for _ in range(32):
            polynomial = value**3 - 2 * value**2 + 2 * value - 2
            derivative = 3 * value**2 - 4 * value + 2
            update = polynomial / derivative
            value -= update
            if update == 0:
                break
        return value


def decimal_f(x: Decimal, u: Decimal) -> Decimal:
    return Decimal(1) - u * x * x


def decimal_t(x: Decimal, u: Decimal) -> Decimal:
    return decimal_f(decimal_f(x, u), u)


def decimal_h(y: Decimal, u: Decimal) -> Decimal:
    return ((Decimal(1) - y) / u).sqrt()


def decimal_positive_t_inverse(y: Decimal, u: Decimal) -> Decimal:
    return decimal_h(decimal_h(y, u), u)


def first_negative_return(
    initial_x: Decimal, u: Decimal, maximum_steps: int
) -> int | None:
    if initial_x >= 0:
        raise ValueError("initial state must lie in the strict negative event set")
    x = initial_x
    for step in range(1, maximum_steps + 1):
        x = decimal_f(x, u)
        if x < 0:
            return step
    return None


def high_precision_diagnostics(
    branch_count: int = HIGH_PRECISION_DIAGNOSTIC_BRANCHES,
) -> dict[str, Any]:
    with localcontext() as context:
        context.prec = HIGH_PRECISION_DIGITS
        u = decimal_root(HIGH_PRECISION_DIGITS)
        rho = u - 1
        threshold = Decimal(1) / u.sqrt()

        endpoints = [Decimal(0)]
        for _ in range(max(branch_count, REPORTED_ENDPOINT_ROWS)):
            endpoints.append(decimal_positive_t_inverse(endpoints[-1], u))

        core_rows: list[dict[str, Any]] = []
        core_midpoint_returns_pass = True
        for index in range(1, branch_count + 1):
            lower = -endpoints[index]
            upper = -endpoints[index - 1]
            midpoint = (lower + upper) / 2
            observed = first_negative_return(midpoint, u, 2 * index + 2)
            core_midpoint_returns_pass &= observed == 2 * index
            if index <= REPORTED_ENDPOINT_ROWS:
                core_rows.append(
                    {
                        "branch_index": index,
                        "return_time": 2 * index,
                        "lower_open": str(lower),
                        "upper": str(upper),
                        "upper_closed": index >= 2,
                        "midpoint_first_return": observed,
                        "length": str(upper - lower),
                    }
                )

        outer_endpoints = [-decimal_h(value, u) for value in endpoints]
        ambient_rows: list[dict[str, Any]] = []

        c1_midpoint = (Decimal(-1) + outer_endpoints[0]) / 2
        c1_return = first_negative_return(c1_midpoint, u, 3)
        ambient_midpoint_returns_pass = c1_return == 1
        ambient_rows.append(
            {
                "return_time": 1,
                "lower": "-1",
                "lower_closed": True,
                "upper_open": str(outer_endpoints[0]),
                "midpoint_first_return": c1_return,
            }
        )

        for index in range(1, min(branch_count, REPORTED_ENDPOINT_ROWS) + 1):
            lower = outer_endpoints[index - 1]
            upper = outer_endpoints[index]
            midpoint = (lower + upper) / 2
            observed = first_negative_return(midpoint, u, 2 * index + 3)
            ambient_midpoint_returns_pass &= observed == 2 * index + 1
            ambient_rows.append(
                {
                    "return_time": 2 * index + 1,
                    "lower_closed": str(lower),
                    "upper_open": str(upper),
                    "midpoint_first_return": observed,
                }
            )

        x = DERIVATIVE_COUNTEREXAMPLE_X
        derivative_value = abs(4 * u**2 * x * decimal_f(x, u))
        derivative_first_return = first_negative_return(x, u, 4)
        t_prime_rho = 4 * u**2 * rho**2
        endpoint_length_ratio = Decimal(1) / t_prime_rho
        conditional_mass_ratio = Decimal(1) / (2 * u * rho)

        band_residuals = {
            "f_minus_rho_minus_rho": str(abs(decimal_f(-rho, u) - rho)),
            "f_rho_minus_rho": str(abs(decimal_f(rho, u) - rho)),
            "f_zero_minus_one": str(abs(decimal_f(Decimal(0), u) - 1)),
            "f_one_plus_rho": str(abs(decimal_f(Decimal(1), u) + rho)),
        }

        period_two_discriminant = (4 * u - 3).sqrt()
        period_two_negative = (1 - period_two_discriminant) / (2 * u)
        period_two_positive = (1 + period_two_discriminant) / (2 * u)

        return {
            "precision_digits": HIGH_PRECISION_DIGITS,
            "u_c": str(u),
            "rho": str(rho),
            "negative_threshold": str(threshold),
            "band_identity_residuals": band_residuals,
            "core_branch_rows": core_rows,
            "ambient_odd_branch_rows": ambient_rows,
            "core_midpoint_first_returns_pass": core_midpoint_returns_pass,
            "ambient_midpoint_first_returns_pass": ambient_midpoint_returns_pass,
            "derivative_counterexample": {
                "x": str(x),
                "first_negative_return": derivative_first_return,
                "absolute_first_return_derivative": str(derivative_value),
                "strictly_below_one": (
                    derivative_first_return == 2 and derivative_value < 1
                ),
            },
            "asymptotic_endpoint_length_ratio": str(endpoint_length_ratio),
            "conditional_square_root_mass_ratio": str(conditional_mass_ratio),
            "period_two_measure_witness": {
                "negative_point": str(period_two_negative),
                "positive_point": str(period_two_positive),
                "f_negative_to_positive_residual": str(
                    abs(decimal_f(period_two_negative, u) - period_two_positive)
                ),
                "f_positive_to_negative_residual": str(
                    abs(decimal_f(period_two_positive, u) - period_two_negative)
                ),
            },
        }


def rational_certificate() -> dict[str, Any]:
    endpoint_intervals = certified_endpoint_intervals()
    rho_lower = U_LOWER - 1
    rho_upper = U_UPPER - 1

    rows = []
    for index, (lower, upper) in enumerate(endpoint_intervals[1:], start=1):
        rows.append(
            {
                "branch_index": index,
                "return_time": 2 * index,
                "lower_scaled_integer": str(scaled_integer(lower)),
                "upper_scaled_integer": str(scaled_integer(upper)),
                "strictly_above_previous": endpoint_intervals[index - 1][1] < lower,
                "strictly_below_rho": upper < rho_lower,
            }
        )

    return {
        "u_lower": U_LOWER_TEXT,
        "u_upper": U_UPPER_TEXT,
        "polynomial_negative_at_lower": critical_polynomial(U_LOWER) < 0,
        "polynomial_positive_at_upper": critical_polynomial(U_UPPER) > 0,
        "root_uniqueness_basis": "p'(u)=3*u^2-4*u+2>0 because its discriminant is -8",
        "sqrt_scale_digits": RATIONAL_SQRT_SCALE_DIGITS,
        "certified_branch_count": RATIONAL_CERTIFIED_BRANCHES,
        "maximum_certified_physical_return": 2 * RATIONAL_CERTIFIED_BRANCHES,
        "all_endpoint_intervals_strictly_separated": all(
            bool(row["strictly_above_previous"]) for row in rows
        ),
        "all_endpoint_intervals_below_rho": all(
            bool(row["strictly_below_rho"]) for row in rows
        ),
        "rho_lower_scaled_floor": str((rho_lower * SQRT_SCALE).numerator // (rho_lower * SQRT_SCALE).denominator),
        "rho_upper_scaled_ceil": str(
            -((-rho_upper * SQRT_SCALE).numerator // (-rho_upper * SQRT_SCALE).denominator)
        ),
        "endpoint_rows": rows,
    }


def build_report() -> dict[str, Any]:
    rational = rational_certificate()
    diagnostic = high_precision_diagnostics()
    derivative_value = Decimal(
        diagnostic["derivative_counterexample"]["absolute_first_return_derivative"]
    )
    identity_residuals = [
        Decimal(value) for value in diagnostic["band_identity_residuals"].values()
    ]

    computational_gates = {
        "critical_polynomial_changes_sign_on_rational_bracket": rational[
            "polynomial_negative_at_lower"
        ]
        and rational["polynomial_positive_at_upper"],
        "rational_root_enclosure_lies_between_three_halves_and_two": (
            U_LOWER > Fraction(3, 2) and U_UPPER < Fraction(2)
        ),
        "band_swap_identities_pass": max(identity_residuals) < Decimal("1e-170"),
        "physical_endpoint_prefix_is_rationally_certified": rational[
            "all_endpoint_intervals_strictly_separated"
        ]
        and rational["all_endpoint_intervals_below_rho"],
        "physical_midpoint_return_diagnostics_pass": diagnostic[
            "core_midpoint_first_returns_pass"
        ],
        "ambient_support_contains_odd_transient_branches": diagnostic[
            "ambient_midpoint_first_returns_pass"
        ],
        "old_uniform_expansion_claim_is_refuted": (
            diagnostic["derivative_counterexample"]["first_negative_return"] == 2
            and derivative_value < 1
        ),
        "period_two_witness_closes": max(
            Decimal(
                diagnostic["period_two_measure_witness"][
                    "f_negative_to_positive_residual"
                ]
            ),
            Decimal(
                diagnostic["period_two_measure_witness"][
                    "f_positive_to_negative_residual"
                ]
            ),
        )
        < Decimal("1e-170"),
    }

    formal_evidence = {
        "root_uniqueness_and_location": {
            "status": "PROVED",
            "basis": "p'(u)>0 with p(3/2)<0<p(2)",
            "executable_gate": False,
        },
        "physical_support_and_unique_branches": {
            "status": "PROVED",
            "basis": "exact band swap plus forced inverse-branch formula in formal/results/exact_uc_first_return_support.md",
            "executable_gate": False,
        },
        "full_branch_and_finite_word_language": {
            "status": "PROVED",
            "basis": "f^(2n) maps every branch interior diffeomorphically onto (-rho,0)",
            "executable_gate": False,
        },
        "ambient_transient_support": {
            "status": "PROVED",
            "basis": "outer inverse branch ell(y)=-sqrt((1-y)/U_c)",
            "executable_gate": False,
        },
        "ambient_invariant_measure_scope": {
            "status": "PROVED",
            "basis": "f(X) is contained in J, so every invariant probability gives X minus J zero mass",
            "executable_gate": False,
        },
        "physical_acip_branch_positivity": {
            "status": "CONDITIONAL_THEOREM",
            "basis": "conditional on the named physical acip having topological support J; then every nonempty branch interior has positive mass",
            "executable_gate": False,
        },
        "endpoint_length_ratio_limit": {
            "status": "PROVED",
            "basis": "mean-value theorem applied to r_(n+1)=psi(r_n), with psi'(rho)=1/T'(rho)",
            "executable_gate": False,
        },
        "paper_2_uniform_expansion_obstruction": {
            "status": "PROVED",
            "basis": "derivative tends to zero at a critical-preimage endpoint on every branch",
            "executable_gate": False,
        },
    }

    return {
        "audit_id": AUDIT_ID,
        "parent_audit_id": PARENT_AUDIT_ID,
        "formal_candidate": False,
        "source_lock": SOURCE_LOCK,
        "mathematical_object": {
            "map": "f(x)=1-U_c*x^2",
            "ambient_interval": "X=[-1,1]",
            "physical_invariant_core": "J=[1-U_c,1]=[-rho,1]",
            "physical_event": "L_J=[-rho,0)",
            "ambient_event": "L_X=[-1,0)",
            "zero_convention": "x=0 is not an L event",
            "clock": "one f iterate; T=f^2 is proof notation only",
        },
        "exact_theorem": {
            "rho": "U_c-1",
            "band_swap": ["f([-rho,rho])=[rho,1]", "f([rho,1])=[-rho,rho]"],
            "t_formula": "T(x)=-rho+2*U_c^2*x^2-U_c^3*x^4",
            "t_derivative": "T'(x)=4*U_c^2*x*f(x)",
            "positive_inverse_branch": (
                "psi(y)=sqrt((1-sqrt((1-y)/U_c))/U_c)"
            ),
            "endpoint_recursion": "r_0=0; r_(n+1)=psi(r_n); r_n increases to rho",
            "physical_branches": {
                "C_2": "(-r_1,0)",
                "C_2n_for_n_at_least_2": "(-r_n,-r_(n-1)]",
                "C_odd": "empty",
                "nonreturning_point": "-rho",
                "topological_support": "2*N_{>=1}",
                "branch_multiplicity": "exactly one nondegenerate interval per even label",
                "full_branch_map": "f^(2n): int(C_(2n)) -> (-rho,0) is a real-analytic diffeomorphism",
                "finite_return_word_cylinders": "nonempty open for every finite word of positive even labels",
            },
            "ambient_branches": {
                "q_n": "-sqrt((1-r_n)/U_c)",
                "C_1": "[-1,q_0)",
                "C_(2n+1)_for_n_at_least_1": "[q_(n-1),q_n)",
                "even_branches": "the physical-core C_(2n)",
                "topological_support": "N_{>=1}",
                "transient_odd_union": "[-1,-rho)",
            },
        },
        "rational_interval_certificate": rational,
        "high_precision_diagnostics": diagnostic,
        "invariant_weight_ledger": {
            "measure_free_topology": {
                "physical_support": "2*N_{>=1}",
                "ambient_support": "N_{>=1}",
            },
            "all_invariant_probabilities": {
                "mass_of_X_minus_J": 0,
                "mass_of_every_ambient_odd_branch": 0,
                "proof": "f(X) is a subset of J, so f^{-1}(X minus J) is empty",
            },
            "physical_acip_with_support_J": {
                "mass_of_every_physical_even_branch": "strictly_positive",
                "basis": "each branch contains an open interval and every open subset of the support has positive mass",
                "exact_weight_values": "open",
            },
            "measure_independence": False,
            "counterexamples": {
                "fixed_point_measure": "delta_rho assigns no mass to L",
                "period_two_orbit_measure": {
                    "mass_of_C_2": "1/2",
                    "mass_of_C_2n_for_n_at_least_2": 0,
                    "conditional_return_support_on_L": "C_2 only",
                },
            },
        },
        "prior_work_correction": {
            "paper_2_parity_lemma": {
                "conclusion": "repaired and strengthened on J",
                "old_proof_status": "REFUTED",
                "reason": "LR^(2j)L... < K satisfies, rather than violates, the stated MSS admissibility inequality",
                "replacement": "exact band-swap proof",
            },
            "paper_2_induced_uniform_expansion": {
                "status": "REFUTED",
                "counterexample": diagnostic["derivative_counterexample"],
                "all_branch_infimum": "inf_(C_2n) |(f^(2n))'| = 0 for every n>=1",
                "inverse_jacobian_singularity": "constant*(y+rho)^(-1/2) at the left image endpoint",
                "ordinary_bv_markov_argument_ready": False,
            },
        },
        "open_weight_clue": {
            "endpoint_length_ratio_limit": diagnostic[
                "asymptotic_endpoint_length_ratio"
            ],
            "endpoint_length_ratio_status": "PROVED",
            "conditional_square_root_mass_ratio": diagnostic[
                "conditional_square_root_mass_ratio"
            ],
            "mass_ratio_status": "OPEN_CONDITIONAL_CLUE",
            "status": "OPEN_CONDITIONAL_CLUE",
            "required_density_hypothesis": (
                "d mu_ac/dx(-rho+t)=C*t^(-1/2)*(1+o(1)), C>0, as t decreases to zero"
            ),
            "interpretation": (
                "the value near 0.595744 follows only under the explicitly frozen endpoint-density asymptotic"
            ),
        },
        "route_a_update": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall_verdict": "ROUTE_A_EXPLORATORY",
            "recommended_audit_verdict": "REVISE",
            "a1_evidence_upgrade": (
                "the one-even-label/one-full-interval physical branch grammar and every finite return-word cylinder are PROVED rather than modeling choices"
            ),
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "established": [
                "physical-core topological support equals all positive even return times",
                "ambient topological support equals all positive return times because of transient odd branches",
                "each physical even label has exactly one nondegenerate interval branch",
                "each branch maps diffeomorphically onto the event interior and every finite even-label word has a nonempty open cylinder",
                "all invariant probabilities assign zero mass to ambient transient odd branches",
                "conditional on the named physical acip having support J, all physical even branches have positive mass",
                "the asymptotic branch-length ratio equals 1/(4*U_c^2*(U_c-1)^2)",
                "the unaccelerated first-return map is not uniformly expanding and the old ordinary-BV argument fails",
            ],
            "not_established": [
                "closed-form or certified numerical physical-acip branch weights",
                "the asymptotic branch-mass ratio or its square-root-density mechanism",
                "a repaired weighted-space or accelerated transfer-operator theorem",
                "a Fredholm determinant, prime correspondence, completed-xi structure, Route B, or RH",
            ],
        },
        "next_smallest_task": (
            "Prove or refute d mu_ac/dx(-rho+t)=C*t^(-1/2)*(1+o(1)), C>0, and the resulting conditional branch-mass ratio, using a direct density argument, a weighted function space, or a newly frozen accelerated inducing domain."
        ),
        "formal_evidence": formal_evidence,
        "computational_gates": computational_gates,
        "audit_passed": all(computational_gates.values()),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "artifacts/p4_logistic_uc_first_return_support/structural_audit.json"
        ),
    )
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    report = build_report()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    if not args.quiet:
        print(json.dumps(report, indent=2, sort_keys=True))
    if not report["audit_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
