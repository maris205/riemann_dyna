#!/usr/bin/env python3
"""Certify the frozen-radius complex branches of the exact-U_c polar map."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path
from typing import Any

import flint
from flint import arb, ctx
import sympy as sp

try:
    from experiments import p4_logistic_uc_first_return_support as support
except ModuleNotFoundError:  # Direct execution from the repository root.
    import p4_logistic_uc_first_return_support as support


AUDIT_ID = "P4-LOGISTIC-UC-POLAR-COMPLEX-BRANCH"
PARENT_AUDIT_ID = "P4-LOGISTIC-UC-POLAR-NONLATTICE"
SOURCE_LOCK = (
    "configs/source_locks/P4-LOGISTIC-UC-POLAR-COMPLEX-BRANCH.yaml"
)
PARENT_SOURCE_LOCK = (
    "configs/source_locks/P4-LOGISTIC-UC-POLAR-INTRINSIC-ROOF.yaml"
)
NONLATTICE_SOURCE_LOCK = (
    "configs/source_locks/P4-LOGISTIC-UC-POLAR-NONLATTICE.yaml"
)
FORMAL_RESULT = "formal/results/exact_uc_polar_complex_branch.md"
GENERATOR = "experiments/p4_logistic_uc_polar_complex_branch.py"
ARTIFACT = (
    "artifacts/p4_logistic_uc_polar_complex_branch/"
    "complex_branch_certificate.json"
)

ARB_DECIMAL_DIGITS = 100
EXPECTED_PYTHON_FLINT_VERSION = "0.9.0"
EXPECTED_FLINT_VERSION = "3.6.0"
EXPECTED_SYMPY_VERSION = "1.14.0"

EPSILON_NUMERATOR = 1
EPSILON_DENOMINATOR = 1000
RADICAND_REAL_PART_SAFE_LOWER = "0.29559"
T_REAL_PART_SAFE_LOWER = "0.54368"
T_PERTURBATION_SAFE_UPPER = "0.000324"
LOG_VARIATION_SAFE_UPPER = "0.000851"
RELATIVE_FACTOR_SAFE_UPPER = "1.000851"
COMPLEX_CONTRACTION_SAFE_UPPER = "0.59626"
IMAGE_RADIUS_SAFE_UPPER = "0.00059626"
COMPACT_MARGIN_SAFE_LOWER = "0.00040374"

REPRODUCTION_COMMAND = (
    "python3 experiments/p4_logistic_uc_polar_complex_branch.py --quiet "
    "--output artifacts/p4_logistic_uc_polar_complex_branch/"
    "complex_branch_certificate.json"
)


def file_sha256(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def root_ball() -> arb:
    return arb(support.U_LOWER_TEXT).union(arb(support.U_UPPER_TEXT))


def exact_identity_certificate() -> dict[str, Any]:
    u, x, t = sp.symbols("u x t")
    rho = u - 1
    critical = sp.Poly(u**3 - 2 * u**2 + 2 * u - 2, u)
    reflected = rho - 2 * u**2 * x**2 + u**3 * x**4

    def zero_mod_critical(expression: sp.Expr) -> bool:
        remainder = sp.rem(sp.Poly(sp.expand(expression), u), critical)
        return remainder.is_zero

    band_identity = u * rho**2 - (1 - rho)
    endpoint_multiplier_identity = u**3 * rho - 2
    one_plus_map_identity = sp.expand(
        1 + reflected - u * (1 - u * x**2) ** 2
    )
    log_derivative = (
        sp.Rational(1, 2) / (1 + t)
        + sp.Rational(1, 2) / (rho + t)
        - 1 / t
    )
    log_derivative_target = -(
        u * t + 2 * rho
    ) / (2 * t * (1 + t) * (rho + t))
    log_derivative_residual = sp.cancel(
        log_derivative - log_derivative_target
    )
    endpoint_a_squared_residual = sp.together(
        (u**2 / 4) ** 2
        - ((1 + rho) * (rho + rho)) / (16 * rho**2)
    )
    endpoint_numerator = sp.fraction(endpoint_a_squared_residual)[0]

    gates = {
        "u_rho_squared_equals_one_minus_rho": zero_mod_critical(
            band_identity
        ),
        "u_cubed_rho_equals_two": zero_mod_critical(
            endpoint_multiplier_identity
        ),
        "one_plus_S_equals_u_times_one_minus_u_x_squared_squared": (
            one_plus_map_identity == 0
        ),
        "real_log_a_derivative_formula_is_exact": (
            log_derivative_residual == 0
        ),
        "real_a_maximum_endpoint_value_is_u_squared_over_four": (
            zero_mod_critical(endpoint_numerator)
        ),
    }
    return {
        "critical_polynomial": "u^3-2*u^2+2*u-2",
        "rho": "u-1",
        "identities": {
            "u*rho^2": "1-rho",
            "u^3*rho": "2",
            "1+S(x)": "u*(1-u*x^2)^2",
            "d_dt_log_a_0": (
                "-(u*t+2*rho)/(2*t*(1+t)*(rho+t))<0"
            ),
            "max_real_a_0": "a_0(rho)=u^2/4",
        },
        "computed_gates": gates,
        "computed_gates_passed": all(gates.values()),
    }


def analytic_bound_certificate() -> dict[str, Any]:
    previous_precision = ctx.prec
    try:
        ctx.dps = ARB_DECIMAL_DIGITS
        u = root_ball()
        rho = u - 1
        epsilon = arb(EPSILON_NUMERATOR) / EPSILON_DENOMINATOR
        cosh_epsilon = epsilon.cosh()

        # For z in closure(U), Re(sin z) >= -cosh(epsilon).
        radicand_real_part_lower = (1 - rho * cosh_epsilon) / u
        t_real_part_lower = radicand_real_part_lower.sqrt()

        # If x is a nearest point on the real interval, then the segment
        # [x,z] stays in the stadium and |sin z-sin x|<=eps*cosh(eps).
        radicand_perturbation_upper = (
            (rho / u) * epsilon * cosh_epsilon
        )
        t_perturbation_upper = radicand_perturbation_upper / (
            t_real_part_lower + rho
        )

        log_derivative_absolute_upper = (
            1 / (2 * (u - t_perturbation_upper))
            + 1 / (2 * (2 * rho - t_perturbation_upper))
            + 1 / (rho - t_perturbation_upper)
        )
        log_variation_upper = (
            t_perturbation_upper * log_derivative_absolute_upper
        )

        relative_factor_upper = (
            (
                (1 + t_perturbation_upper / u)
                * (1 + t_perturbation_upper / (2 * rho))
            ).sqrt()
            / (1 - t_perturbation_upper / rho)
        )
        real_contraction_maximum = u**2 / 4
        complex_contraction_upper = (
            real_contraction_maximum * relative_factor_upper
        )
        image_radius_upper = complex_contraction_upper * epsilon
        compact_margin_lower = (1 - complex_contraction_upper) * epsilon

        gates = {
            "critical_root_has_certified_sign_bracket": (
                support.critical_polynomial(support.U_LOWER) < 0
                < support.critical_polynomial(support.U_UPPER)
            ),
            "root_ball_is_strictly_between_three_halves_and_two": (
                u > arb("1.5") and u < 2
            ),
            "radicand_real_part_above_safe_lower": (
                radicand_real_part_lower
                > arb(RADICAND_REAL_PART_SAFE_LOWER)
            ),
            "principal_t_real_part_above_safe_lower": (
                t_real_part_lower > arb(T_REAL_PART_SAFE_LOWER)
            ),
            "t_perturbation_below_safe_upper": (
                t_perturbation_upper < arb(T_PERTURBATION_SAFE_UPPER)
            ),
            "t_perturbation_is_smaller_than_rho": (
                t_perturbation_upper < rho
            ),
            "log_variation_below_safe_upper": (
                log_variation_upper < arb(LOG_VARIATION_SAFE_UPPER)
            ),
            "log_variation_keeps_a_in_the_right_half_plane": (
                log_variation_upper < arb("0.001")
                and arb("0.001") < arb.pi() / 2
            ),
            "relative_factor_below_safe_upper": (
                relative_factor_upper < arb(RELATIVE_FACTOR_SAFE_UPPER)
            ),
            "complex_contraction_below_safe_upper": (
                complex_contraction_upper
                < arb(COMPLEX_CONTRACTION_SAFE_UPPER)
            ),
            "complex_contraction_is_strictly_below_one": (
                complex_contraction_upper < 1
            ),
            "image_radius_below_safe_upper": (
                image_radius_upper < arb(IMAGE_RADIUS_SAFE_UPPER)
            ),
            "image_radius_is_strictly_below_epsilon": (
                image_radius_upper < epsilon
            ),
            "compact_margin_above_safe_lower": (
                compact_margin_lower > arb(COMPACT_MARGIN_SAFE_LOWER)
            ),
        }

        return {
            "epsilon": "1/1000",
            "certified_root_ball": u.str(110),
            "rho_ball": rho.str(110),
            "cosh_epsilon_ball": cosh_epsilon.str(80),
            "radicand_real_part_lower_ball": (
                radicand_real_part_lower.str(80)
            ),
            "principal_t_real_part_lower_ball": (
                t_real_part_lower.str(80)
            ),
            "radicand_perturbation_upper_ball": (
                radicand_perturbation_upper.str(80)
            ),
            "t_perturbation_upper_ball": t_perturbation_upper.str(80),
            "log_derivative_absolute_upper_ball": (
                log_derivative_absolute_upper.str(80)
            ),
            "log_variation_upper_ball": log_variation_upper.str(80),
            "real_contraction_maximum_ball": (
                real_contraction_maximum.str(80)
            ),
            "relative_factor_upper_ball": relative_factor_upper.str(80),
            "complex_contraction_upper_ball": (
                complex_contraction_upper.str(80)
            ),
            "image_radius_upper_ball": image_radius_upper.str(80),
            "compact_margin_lower_ball": compact_margin_lower.str(80),
            "safe_thresholds": {
                "radicand_real_part_lower": RADICAND_REAL_PART_SAFE_LOWER,
                "principal_t_real_part_lower": T_REAL_PART_SAFE_LOWER,
                "t_perturbation_upper": T_PERTURBATION_SAFE_UPPER,
                "log_variation_upper": LOG_VARIATION_SAFE_UPPER,
                "relative_factor_upper": RELATIVE_FACTOR_SAFE_UPPER,
                "complex_contraction_upper": (
                    COMPLEX_CONTRACTION_SAFE_UPPER
                ),
                "image_radius_upper": IMAGE_RADIUS_SAFE_UPPER,
                "compact_margin_lower": COMPACT_MARGIN_SAFE_LOWER,
            },
            "four_branch_inclusions": {
                "LL": "phi_L(closure(U_L)) compactly contained in U_L",
                "LR": "phi_R(closure(U_L)) compactly contained in U_R",
                "RL": "phi_L(closure(U_R)) compactly contained in U_L",
                "RR": "phi_R(closure(U_R)) compactly contained in U_R",
                "common_image_radius_upper": IMAGE_RADIUS_SAFE_UPPER,
                "common_compact_margin_lower": COMPACT_MARGIN_SAFE_LOWER,
            },
            "computed_gates": gates,
            "computed_gates_passed": all(gates.values()),
        }
    finally:
        ctx.prec = previous_precision


def build_report() -> dict[str, Any]:
    exact = exact_identity_certificate()
    analytic = analytic_bound_certificate()
    computed_gates = {
        "python_flint_version_is_frozen": (
            flint.__version__ == EXPECTED_PYTHON_FLINT_VERSION
        ),
        "flint_version_is_frozen": (
            flint.__FLINT_VERSION__ == EXPECTED_FLINT_VERSION
        ),
        "sympy_version_is_frozen": (
            sp.__version__ == EXPECTED_SYMPY_VERSION
        ),
        "all_exact_identity_gates_pass": exact["computed_gates_passed"],
        "all_analytic_bound_gates_pass": analytic[
            "computed_gates_passed"
        ],
    }
    source_inputs = [
        SOURCE_LOCK,
        PARENT_SOURCE_LOCK,
        NONLATTICE_SOURCE_LOCK,
        FORMAL_RESULT,
        "formal/results/exact_uc_acip_endpoint_density.md",
        "formal/results/exact_uc_polar_nonlattice.md",
        "experiments/p4_logistic_uc_first_return_support.py",
    ]
    return {
        "artifact_schema_version": 1,
        "audit_id": AUDIT_ID,
        "parent_audit_id": PARENT_AUDIT_ID,
        "formal_candidate": False,
        "status": "PROVED_FROZEN_COMPLEX_BRANCH_INCLUSION",
        "source_lock": SOURCE_LOCK,
        "mathematical_object": {
            "domains": (
                "U_L and U_R are radius-1/1000 stadiums; "
                "U=U_L union U_R is the full convex stadium"
            ),
            "common_t": "sqrt((1+rho*sin(z))/U_c) on the right half-plane",
            "common_a": "sqrt(1+t)*sqrt(rho+t)/(4*t)=exp(ell)",
            "common_log": (
                "ell=-log(4)+Log(1+t)/2+Log(rho+t)/2-Log(t)"
            ),
            "branches": {
                "phi_L": "+integral_(pi/2)^z a(w)dw",
                "phi_R": "-integral_(pi/2)^z a(w)dw",
                "signed_derivatives": ["phi_L'=+a", "phi_R'=-a"],
            },
            "inverse_identity": (
                "S(rho*sin(phi_sigma(z)))=rho*sin(z)"
            ),
        },
        "validated_environment": {
            "python": platform.python_version(),
            "python_flint": flint.__version__,
            "flint": flint.__FLINT_VERSION__,
            "sympy": sp.__version__,
            "arb_decimal_digits": ARB_DECIMAL_DIGITS,
        },
        "exact_identity_certificate": exact,
        "analytic_bound_certificate": analytic,
        "analytic_proof_ledger": [
            "U_L union U_R is the convex radius-1/1000 stadium of I",
            "Re((1+rho*sin(z))/U_c)>0 on a neighborhood of closure(U)",
            "principal t, sqrt(1+t), sqrt(rho+t), a, and ell are one common holomorphic germ",
            "the primitive-defined phi_L and phi_R continue the real composite inverse branches",
            "the q-level inverse identity follows on U by the identity theorem",
            "the common logarithm varies by less than 0.000851 from the real interval, so Re(a)>0 and both branches are globally univalent",
            "one certified |a| bound below one gives all four compact inclusions",
        ],
        "proved_statement": {
            "common_holomorphic_germ": True,
            "composite_inverse_branches_on_frozen_stadiums": True,
            "global_univalence_of_both_branches": True,
            "common_Log_a": True,
            "all_four_compact_inclusions": True,
            "complex_contraction_safe_upper": (
                COMPLEX_CONTRACTION_SAFE_UPPER
            ),
            "compact_margin_safe_lower": COMPACT_MARGIN_SAFE_LOWER,
        },
        "matching_space_corollary": {
            "weighted_formula_is_well_defined_for_each_fixed_s": True,
            "two_output_components_are_restrictions_of_one_function_on_U": True,
            "matching_at_zero_is_preserved": True,
            "nuclearity_claimed": False,
            "fredholm_determinant_claimed": False,
        },
        "computed_gates": computed_gates,
        "error_budget": {
            "discretization": "none; no complex grid enters the proof",
            "truncation": "none; all four frozen branch pairs are covered",
            "rounding": "100-digit outward Arb scalar margins",
            "normalization": "one common a, signed derivatives, and unscaled roof",
            "iteration_stopping": "not applicable; no orbit solve is used",
            "resolvent_tail": "not applicable; no resolvent is evaluated",
        },
        "claim_boundary": {
            "established": [
                "one common holomorphic t, a, and Log(a) germ on the frozen complex domain",
                "both composite inverse branches with preserved signed derivatives",
                "positive real part of a and global univalence of both complex branches",
                "all four compact branch inclusions with a positive explicit margin",
                "well-defined matching-space weighted composition for each fixed s",
            ],
            "not_established": [
                "partition-hit target-copy or trace multiplicity rules",
                "nuclearity, a Fredholm determinant, or an orbit trace formula",
                "a completed-xi divisor, functional equation, or target zeros",
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
            "new_structural_prior": (
                "PROVED_FROZEN_COMPLEX_BRANCH_INCLUSION"
            ),
            "local_verdict": "GO_WITH_LIMITATIONS",
            "parent_candidate_verdict": "REVISE",
            "route_b_invocation_allowed": False,
        },
        "next_smallest_test": (
            "Freeze only the doubled-partition target-copy and multiplicity "
            "rule for partition-hit traces on the matching space; defer "
            "nuclearity, Fredholm zeros, target divisors, and Route B."
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
    report["computed_gates_passed"] = all(
        report["computed_gates"].values()
    )
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
