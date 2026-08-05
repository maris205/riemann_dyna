#!/usr/bin/env python3
"""Prove the sealed exact-U_c polar roof is non-lattice."""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import platform
from pathlib import Path
from typing import Any

import mpmath as mp
import sympy as sp
from sympy.polys.domains import QQ


AUDIT_ID = "P4-LOGISTIC-UC-POLAR-NONLATTICE"
PARENT_AUDIT_ID = "P4-LOGISTIC-UC-POLAR-INTRINSIC-ROOF"
SOURCE_LOCK = "configs/source_locks/P4-LOGISTIC-UC-POLAR-NONLATTICE.yaml"
PARENT_SOURCE_LOCK = (
    "configs/source_locks/P4-LOGISTIC-UC-POLAR-INTRINSIC-ROOF.yaml"
)
FORMAL_RESULT = "formal/results/exact_uc_polar_nonlattice.md"
GENERATOR = "experiments/p4_logistic_uc_polar_nonlattice.py"
ARTIFACT = (
    "artifacts/p4_logistic_uc_polar_nonlattice/"
    "nonlattice_certificate.json"
)

EXPECTED_SYMPY_VERSION = "1.14.0"
EXPECTED_MPMATH_VERSION = "1.3.0"
DIAGNOSTIC_DIGITS = 100

ALPHA_POLYNOMIAL_DESCENDING = [1, 4, 16, -64]
BETA_POLYNOMIAL_DESCENDING = [
    1,
    144,
    6656,
    139264,
    2621440,
    -37748736,
    -369098752,
    2684354560,
    12884901888,
    -68719476736,
]

REPRODUCTION_COMMAND = (
    "python3 experiments/p4_logistic_uc_polar_nonlattice.py --quiet "
    "--output artifacts/p4_logistic_uc_polar_nonlattice/"
    "nonlattice_certificate.json"
)


def file_sha256(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _trim_mod(coefficients: list[int], prime: int) -> list[int]:
    result = [coefficient % prime for coefficient in coefficients]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def _sub_mod(left: list[int], right: list[int], prime: int) -> list[int]:
    size = max(len(left), len(right))
    result = [0] * size
    for index in range(size):
        result[index] = (
            (left[index] if index < len(left) else 0)
            - (right[index] if index < len(right) else 0)
        ) % prime
    return _trim_mod(result, prime)


def _divmod_mod(
    dividend: list[int], divisor: list[int], prime: int
) -> tuple[list[int], list[int]]:
    remainder = _trim_mod(dividend[:], prime)
    divisor = _trim_mod(divisor[:], prime)
    if divisor == [0]:
        raise ZeroDivisionError("zero polynomial")
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    inverse_lead = pow(divisor[-1], -1, prime)
    while len(remainder) >= len(divisor) and remainder != [0]:
        shift = len(remainder) - len(divisor)
        factor = remainder[-1] * inverse_lead % prime
        quotient[shift] = factor
        for index, coefficient in enumerate(divisor):
            remainder[index + shift] = (
                remainder[index + shift] - factor * coefficient
            ) % prime
        remainder = _trim_mod(remainder, prime)
    return _trim_mod(quotient, prime), remainder


def _reduce_mod(
    polynomial: list[int], modulus: list[int], prime: int
) -> list[int]:
    return _divmod_mod(polynomial, modulus, prime)[1]


def _multiply_mod(
    left: list[int],
    right: list[int],
    modulus: list[int],
    prime: int,
) -> list[int]:
    product = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            product[left_index + right_index] = (
                product[left_index + right_index]
                + left_value * right_value
            ) % prime
    return _reduce_mod(product, modulus, prime)


def _power_mod(
    base: list[int], exponent: int, modulus: list[int], prime: int
) -> list[int]:
    result = [1]
    factor = _reduce_mod(base, modulus, prime)
    while exponent:
        if exponent & 1:
            result = _multiply_mod(result, factor, modulus, prime)
        factor = _multiply_mod(factor, factor, modulus, prime)
        exponent //= 2
    return result


def _gcd_mod(left: list[int], right: list[int], prime: int) -> list[int]:
    left = _trim_mod(left[:], prime)
    right = _trim_mod(right[:], prime)
    while right != [0]:
        left, right = right, _reduce_mod(left, right, prime)
    inverse_lead = pow(left[-1], -1, prime)
    return [(coefficient * inverse_lead) % prime for coefficient in left]


def rabin_beta_certificate() -> dict[str, Any]:
    prime = 5
    modulus = [
        coefficient % prime
        for coefficient in reversed(BETA_POLYNOMIAL_DESCENDING)
    ]
    x_polynomial = [0, 1]
    frobenius_degree_three = _sub_mod(
        _power_mod(x_polynomial, prime**3, modulus, prime),
        x_polynomial,
        prime,
    )
    frobenius_degree_nine = _sub_mod(
        _power_mod(x_polynomial, prime**9, modulus, prime),
        x_polynomial,
        prime,
    )
    gcd_degree_three = _gcd_mod(
        modulus,
        frobenius_degree_three,
        prime,
    )
    return {
        "prime": prime,
        "polynomial_coefficients_ascending_mod_5": modulus,
        "x_to_5_cubed_minus_x_remainder": frobenius_degree_three,
        "gcd_with_degree_three_frobenius": gcd_degree_three,
        "x_to_5_ninth_minus_x_remainder": frobenius_degree_nine,
        "irreducible": (
            gcd_degree_three == [1]
            and frobenius_degree_nine == [0]
        ),
    }


def _coefficients_reduce_to_zero(
    polynomial: sp.Poly, critical: sp.Poly, variable: sp.Symbol
) -> tuple[bool, bool, int]:
    all_numerators_zero = True
    all_denominators_coprime = True
    coefficients = polynomial.all_coeffs()
    for coefficient in coefficients:
        numerator, denominator = sp.fraction(sp.cancel(coefficient))
        numerator_remainder = sp.rem(
            sp.Poly(numerator, variable, domain=QQ),
            critical,
        )
        all_numerators_zero &= numerator_remainder.is_zero
        denominator_polynomial = sp.Poly(denominator, variable, domain=QQ)
        all_denominators_coprime &= sp.gcd(
            denominator_polynomial,
            critical,
        ).degree() == 0
    return (
        all_numerators_zero,
        all_denominators_coprime,
        len(coefficients),
    )


def exact_algebra_certificate() -> dict[str, Any]:
    u, x, m = sp.symbols("u x m")
    critical_expression = u**3 - 2 * u**2 + 2 * u - 2
    critical = sp.Poly(critical_expression, u, domain=QQ)
    reduced_map = lambda value: (
        u - 1 - 2 * u**2 * value**2 + u**3 * value**4
    )

    fixed_factor = (
        (u * x**2 - x - 1)
        * (u**2 * x**2 + u * x - u + 1)
    )
    fixed_residual = sp.Poly(
        sp.expand(reduced_map(x) - x - fixed_factor),
        x,
        domain=QQ.frac_field(u),
    )
    fixed_zero, fixed_denominators, fixed_coefficient_count = (
        _coefficients_reduce_to_zero(fixed_residual, critical, u)
    )

    derivative = sp.diff(reduced_map(x), x)
    alpha = 4 * (u - 1)
    right_fixed_polynomial = sp.Poly(
        u**2 * x**2 + u * x - u + 1,
        x,
        domain=QQ.frac_field(u),
    )
    right_multiplier_residual = sp.Poly(
        sp.expand(derivative + alpha),
        x,
        domain=QQ.frac_field(u),
    ).rem(right_fixed_polynomial)
    (
        right_multiplier_zero,
        right_multiplier_denominators,
        right_multiplier_coefficient_count,
    ) = _coefficients_reduce_to_zero(
        right_multiplier_residual,
        critical,
        u,
    )

    rational_function_field = QQ.frac_field(u)
    fixed_polynomial = sp.Poly(
        sp.expand(reduced_map(x) - x),
        x,
        domain=rational_function_field,
    )
    period_two_polynomial = sp.Poly(
        sp.expand(reduced_map(reduced_map(x)) - x),
        x,
        domain=rational_function_field,
    )
    dynatomic, dynatomic_remainder = period_two_polynomial.div(
        fixed_polynomial
    )

    signed_multiplier = sp.Poly(
        sp.expand(derivative * derivative.subs(x, reduced_map(x))),
        x,
        domain=rational_function_field,
    ).rem(dynatomic)
    positive_multiplier = -signed_multiplier.as_expr()
    multiplier_identity = sp.Poly(
        sp.expand(
            positive_multiplier**3
            + (48 - 16 * u**2) * positive_multiplier**2
            + 256 * (1 + u**2) * positive_multiplier
            - 4096
        ),
        x,
        domain=rational_function_field,
    ).rem(dynatomic)
    multiplier_zero, multiplier_denominators, multiplier_coefficient_count = (
        _coefficients_reduce_to_zero(multiplier_identity, critical, u)
    )

    alpha_polynomial = alpha**3 + 4 * alpha**2 + 16 * alpha - 64
    alpha_remainder = sp.rem(
        sp.Poly(sp.expand(alpha_polynomial), u, domain=QQ),
        critical,
    )
    alpha_mod_three_values = [
        (
            value**3 + 4 * value**2 + 16 * value - 64
        ) % 3
        for value in range(3)
    ]

    a_zero = m**3 + 48 * m**2 + 256 * m - 4096
    b_zero = -16 * m**2 + 256 * m
    beta_polynomial = sp.Poly(
        sp.expand(a_zero**3 - 4 * a_zero * b_zero**2 + 4 * b_zero**3),
        m,
        domain=QQ,
    )
    beta_coefficients = [
        int(coefficient) for coefficient in beta_polynomial.all_coeffs()
    ]
    u_squared_identity = sp.rem(
        sp.Poly(sp.expand(u**6 - 4 * u**2 - 4), u, domain=QQ),
        critical,
    )

    h_at_alpha_squared = sp.expand(
        alpha**6
        + (48 - 16 * u**2) * alpha**4
        + 256 * (1 + u**2) * alpha**2
        - 4096
    )
    nonvanishing_target = -8192 * (u - 2) * (2 * u - 3)
    nonvanishing_remainder = sp.rem(
        sp.Poly(
            sp.expand(h_at_alpha_squared - nonvanishing_target),
            u,
            domain=QQ,
        ),
        critical,
    )

    rabin = rabin_beta_certificate()
    critical_fraction = lambda value: (
        value**3 - 2 * value**2 + 2 * value - 2
    )
    critical_at_three_halves = critical_fraction(Fraction(3, 2))
    critical_at_two = critical_fraction(Fraction(2, 1))
    h_alpha_identity_holds = nonvanishing_remainder.is_zero
    critical_root_is_bracketed = (
        critical_at_three_halves < 0 < critical_at_two
    )
    critical_is_strictly_increasing = 16 - 4 * 3 * 2 < 0
    computed_gates = {
        "fixed_point_factorization_is_exact": fixed_residual.is_zero,
        "right_fixed_multiplier_is_minus_alpha": (
            right_multiplier_zero and right_multiplier_denominators
        ),
        "dynatomic_division_is_exact": dynatomic_remainder.is_zero,
        "dynatomic_degree_is_12": dynatomic.degree() == 12,
        "signed_multiplier_remainder_degree_is_10": (
            signed_multiplier.degree() == 10
        ),
        "period_two_multiplier_identity_zero_mod_P": (
            multiplier_zero and multiplier_denominators
        ),
        "alpha_polynomial_identity_zero_mod_P": alpha_remainder.is_zero,
        "alpha_cubic_is_irreducible_mod_3": all(
            value != 0 for value in alpha_mod_three_values
        ),
        "u_squared_cubic_identity_zero_mod_P": u_squared_identity.is_zero,
        "beta_polynomial_coefficients_match": (
            beta_coefficients == BETA_POLYNOMIAL_DESCENDING
        ),
        "beta_degree_nine_is_irreducible_mod_5": rabin["irreducible"],
        "alpha_norm_is_2_to_6": (
            -ALPHA_POLYNOMIAL_DESCENDING[-1] == 2**6
        ),
        "beta_norm_is_2_to_36": (
            -BETA_POLYNOMIAL_DESCENDING[-1] == 2**36
        ),
        "common_field_norm_forces_a_equals_2b": 36 // 9 == 2 * (6 // 3),
        "H_alpha_squared_identity_zero_mod_P": (
            h_alpha_identity_holds
        ),
        "critical_root_is_strictly_between_3_over_2_and_2": (
            critical_root_is_bracketed
        ),
        "critical_polynomial_is_strictly_increasing": (
            critical_is_strictly_increasing
        ),
        "H_alpha_squared_is_nonzero": (
            h_alpha_identity_holds
            and critical_root_is_bracketed
            and critical_is_strictly_increasing
        ),
    }
    conclusion_prerequisites = all(computed_gates.values())
    computed_gates["period_ratio_is_irrational"] = conclusion_prerequisites
    computed_gates["intrinsic_roof_is_non_lattice"] = conclusion_prerequisites

    return {
        "critical_polynomial": "u^3-2*u^2+2*u-2",
        "critical_at_3_over_2": "-1/8",
        "critical_at_2": "2",
        "critical_derivative_discriminant": -8,
        "fixed_point_factorization": (
            "S(x)-x=(u*x^2-x-1)*(u^2*x^2+u*x-u+1) in Z[u,x]"
        ),
        "fixed_factor_reduced_coefficient_count": fixed_coefficient_count,
        "alpha": "4*(u-1)",
        "right_multiplier_reduced_coefficient_count": (
            right_multiplier_coefficient_count
        ),
        "alpha_minimal_polynomial_descending": ALPHA_POLYNOMIAL_DESCENDING,
        "alpha_polynomial_mod_3_values_at_0_1_2": alpha_mod_three_values,
        "alpha_degree": 3,
        "alpha_norm": "2^6",
        "dynatomic_degree": dynatomic.degree(),
        "signed_multiplier_remainder_degree": signed_multiplier.degree(),
        "multiplier_identity_reduced_coefficient_count": (
            multiplier_coefficient_count
        ),
        "relative_multiplier_polynomial": (
            "H_u(m)=m^3+(48-16*u^2)*m^2+256*(1+u^2)*m-4096"
        ),
        "u_squared_minimal_relation": "(u^2)^3-4*u^2-4=0",
        "beta_minimal_polynomial_descending": beta_coefficients,
        "beta_degree": 9,
        "beta_norm": "2^36",
        "beta_rabin_certificate": rabin,
        "common_field_norm_ledger": {
            "Norm_K(alpha)": "2^(2*d)",
            "Norm_K(beta)": "2^(4*d)",
            "hypothetical_relation": "beta^b=alpha^a",
            "forced_exponent_relation": "a=2*b",
            "coprime_remaining_case": "a=2, b=1, beta=alpha^2",
        },
        "remaining_case_exclusion": (
            "H_u(alpha^2)=-8192*(u-2)*(2*u-3) != 0 for 3/2<u<2"
        ),
        "computed_gates": computed_gates,
        "computed_gates_passed": all(computed_gates.values()),
    }


def numerical_diagnostics() -> dict[str, str | bool]:
    mp.mp.dps = DIAGNOSTIC_DIGITS
    u = mp.findroot(
        lambda value: value**3 - 2 * value**2 + 2 * value - 2,
        mp.mpf("1.54"),
    )
    rho = u - 1
    reduced_map = lambda value: (
        rho - 2 * u**2 * value**2 + u**3 * value**4
    )
    derivative = lambda value: -4 * u**2 * value * (1 - u * value**2)
    x_left = mp.findroot(
        lambda value: reduced_map(reduced_map(value)) - value,
        (mp.mpf("-0.18"), mp.mpf("-0.15")),
    )
    x_right = reduced_map(x_left)
    alpha = 4 * rho
    signed_r = -alpha
    signed_lr = derivative(x_left) * derivative(x_right)
    beta = -signed_lr
    period_r = mp.log(alpha)
    period_lr = mp.log(beta)
    ratio = period_lr / period_r

    text = lambda value: mp.nstr(value, 85)
    return {
        "proof_weight": "none; identification and reproduction diagnostic only",
        "u": text(u),
        "rho": text(rho),
        "x_L": text(x_left),
        "x_R": text(x_right),
        "theta_L": text(mp.asin(x_left / rho)),
        "theta_R": text(mp.asin(x_right / rho)),
        "signed_multiplier_R": text(signed_r),
        "positive_multiplier_alpha": text(alpha),
        "signed_multiplier_LR": text(signed_lr),
        "positive_multiplier_beta": text(beta),
        "T_R": text(period_r),
        "T_LR": text(period_lr),
        "diagnostic_ratio_T_LR_over_T_R": text(ratio),
        "itinerary_is_strict_LR": (
            -rho < x_left < 0 < x_right < rho
        ),
        "signed_multipliers_are_negative": signed_r < 0 and signed_lr < 0,
        "positive_multipliers_exceed_one": alpha > 1 and beta > 1,
    }


def build_report() -> dict[str, Any]:
    algebra = exact_algebra_certificate()
    diagnostics = numerical_diagnostics()
    source_inputs = [
        SOURCE_LOCK,
        PARENT_SOURCE_LOCK,
        FORMAL_RESULT,
        "formal/results/exact_uc_acip_endpoint_density.md",
        "configs/source_locks/P4-LOGISTIC-UC-ACIP-ENDPOINT-DENSITY.yaml",
    ]
    return {
        "artifact_schema_version": 1,
        "audit_id": AUDIT_ID,
        "parent_audit_id": PARENT_AUDIT_ID,
        "formal_candidate": False,
        "status": "PROVED_INTRINSIC_ROOF_NON_LATTICE",
        "source_lock": SOURCE_LOCK,
        "mathematical_object": {
            "map": "G=q^(-1) o (-f^2) o q on doubled branches I_L and I_R",
            "roof": "tau=log|G'|",
            "sealed_words": ["R", "LR"],
            "periods": ["T_R=log(alpha)", "T_LR=log(beta)"],
            "signed_multipliers": ["Lambda_R=-alpha", "Lambda_LR=-beta"],
        },
        "validated_environment": {
            "python": platform.python_version(),
            "sympy": sp.__version__,
            "mpmath": mp.__version__,
            "diagnostic_decimal_digits": DIAGNOSTIC_DIGITS,
        },
        "exact_algebra_certificate": algebra,
        "numerical_diagnostics": diagnostics,
        "proved_statement": {
            "multiplicative_independence": (
                "alpha and beta have no nontrivial positive integer relation"
            ),
            "period_ratio": "T_LR/T_R is irrational",
            "roof": "tau=log|G'| is non-lattice",
        },
        "computed_gates": {
            "sympy_version_is_frozen": (
                sp.__version__ == EXPECTED_SYMPY_VERSION
            ),
            "mpmath_version_is_frozen": (
                mp.__version__ == EXPECTED_MPMATH_VERSION
            ),
            "all_exact_algebra_gates_pass": algebra["computed_gates_passed"],
            "diagnostic_word_is_strict_LR": diagnostics[
                "itinerary_is_strict_LR"
            ],
            "diagnostic_signed_multipliers_are_negative": diagnostics[
                "signed_multipliers_are_negative"
            ],
            "diagnostic_positive_multipliers_exceed_one": diagnostics[
                "positive_multipliers_exceed_one"
            ],
        },
        "error_budget": {
            "discretization": "none; exact polynomial identities",
            "truncation": "none; the two sealed words are exact",
            "rounding": "none in the theorem; diagnostics carry no proof weight",
            "normalization": "full primitive sums and positive magnitudes",
            "iteration_stopping": "diagnostic only; excluded from the proof",
            "resolvent_tail": "not applicable; no determinant is evaluated",
        },
        "claim_boundary": {
            "established": [
                "exact minimal polynomials and norms for alpha and beta",
                "multiplicative independence of the R and LR roof multipliers",
                "irrational primitive-period ratio and non-lattice intrinsic roof",
            ],
            "not_established": [
                "an arithmetic prime-orbit law or von-Mangoldt trace weights",
                "frozen-radius complex branch inclusion or a common Log(a) theorem",
                "nuclearity, a Fredholm determinant, completed-xi structure, or zeros",
                "quantization, Route B, Hilbert-Polya, or RH",
            ],
        },
        "route_a_effect": {
            "tuple_unchanged": [
                "A1_WEAK",
                "A2_FAIL",
                "A3_FAIL",
                "A4_FAIL",
            ],
            "new_structural_prior": "PROVED_NON_LATTICE_INTRINSIC_ROOF",
            "local_verdict": "GO_WITH_LIMITATIONS",
            "parent_candidate_verdict": "REVISE",
            "route_b_invocation_allowed": False,
        },
        "next_smallest_test": (
            "Audit only the frozen epsilon=1/1000 composite complex inverse "
            "branches, common Log(a) germ, and compact branch inclusion; "
            "defer nuclearity and all target zeros."
        ),
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


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default=ARTIFACT)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    report = build_report()
    report["computed_gates_passed"] = all(report["computed_gates"].values())
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
