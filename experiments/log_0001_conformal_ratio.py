#!/usr/bin/env python3
"""Target-free conformal-ratio certificate for LOG-0001.

The companion theorem is ``formal/results/log_0001_conformal_ratio.md``.
This program evaluates only the frozen stadium path constants and the
resulting explicit determinant-growth majorant.  It never computes a
conformal map, evaluates the Fredholm determinant, searches for roots, or
reads arithmetic target data.
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


AUDIT_ID = "LOG-0001-CONFORMAL-RATIO"
PARENT_AUDIT_ID = "LOG-0001-GROWTH-ORDER"
SOURCE_LOCK = "configs/source_locks/LOG-0001-CONFORMAL-RATIO.yaml"
PARENT_LOCK = "configs/source_locks/LOG-0001-GROWTH-ORDER.yaml"
PARENT_RESULT = "formal/results/log_0001_growth_order.md"
PARENT_ARTIFACT = (
    "artifacts/log_0001_growth_order/growth_order_certificate.json"
)
FORMAL_RESULT = "formal/results/log_0001_conformal_ratio.md"
GENERATOR = "experiments/log_0001_conformal_ratio.py"
ARTIFACT = (
    "artifacts/log_0001_conformal_ratio/"
    "conformal_ratio_certificate.json"
)
EVALUATION = "evaluations/route_a/LOG-0001/20260808T151232Z.yaml"

ARB_BITS = 4096
EXPECTED_PYTHON_FLINT_VERSION = "0.9.0"
EXPECTED_FLINT_VERSION = "3.6.0"

OUTER_RADIUS = Fraction(1, 1000)
INNER_RADIUS = Fraction(3, 5000)
BRANCH_LENGTH_PI_COEFFICIENT = Fraction(1, 2)
ELL_NORM = Fraction(103, 125)
THETA = Fraction(1, 4096)
C0_SAFE_CEILING = "3.45e689"
C1_SAFE_CEILING = "4.20e682"

REPRODUCTION_COMMAND = (
    "python3 experiments/log_0001_conformal_ratio.py --quiet --output "
    "artifacts/log_0001_conformal_ratio/"
    "conformal_ratio_certificate.json"
)


def file_sha256(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def exact_geometry_certificate() -> dict[str, Any]:
    radius_ratio = INNER_RADIUS / OUTER_RADIUS
    disk_cross_ratio = (
        (OUTER_RADIUS + INNER_RADIUS)
        / (OUTER_RADIUS - INNER_RADIUS)
    )
    center_path_pi_coefficient = (
        Fraction(2, 1)
        / OUTER_RADIUS
        * BRANCH_LENGTH_PI_COEFFICIENT
        / 2
    )
    one_minus_two_theta = 1 - 2 * THETA
    gates = {
        "inner_radius_is_strictly_smaller_than_outer_radius": (
            INNER_RADIUS < OUTER_RADIUS
        ),
        "inner_to_outer_radius_ratio_is_three_fifths": (
            radius_ratio == Fraction(3, 5)
        ),
        "disk_distance_cross_ratio_is_four": disk_cross_ratio == 4,
        "center_path_coefficient_is_five_hundred_pi": (
            center_path_pi_coefficient == 500
        ),
        "gaussian_theta_is_between_zero_and_one_half": (
            0 < THETA < Fraction(1, 2)
        ),
        "one_minus_two_theta_is_2047_over_2048": (
            one_minus_two_theta == Fraction(2047, 2048)
        ),
        "ell_norm_upper_is_exactly_103_over_125": (
            ELL_NORM == Fraction(103, 125)
        ),
    }
    return {
        "outer_radius": fraction_text(OUTER_RADIUS),
        "inner_radius": fraction_text(INNER_RADIUS),
        "branch_interval_length": "pi/2",
        "branch_midpoint_to_projection_maximum": "pi/4",
        "Poincare_disk_center_density": "2/R",
        "inner_to_outer_radius_ratio": fraction_text(radius_ratio),
        "disk_distance_cross_ratio": fraction_text(disk_cross_ratio),
        "center_path_pi_coefficient": fraction_text(
            center_path_pi_coefficient
        ),
        "theta": fraction_text(THETA),
        "one_minus_two_theta": fraction_text(one_minus_two_theta),
        "ell_norm_safe_upper": fraction_text(ELL_NORM),
        "computed_gates": gates,
        "computed_gates_passed": all(gates.values()),
    }


def arb_interval_certificate() -> dict[str, Any]:
    previous_precision = ctx.prec
    try:
        ctx.prec = ARB_BITS
        outer_radius = arb(OUTER_RADIUS.numerator) / OUTER_RADIUS.denominator
        inner_radius = arb(INNER_RADIUS.numerator) / INNER_RADIUS.denominator
        theta = arb(THETA.numerator) / THETA.denominator
        ell_norm = arb(ELL_NORM.numerator) / ELL_NORM.denominator

        center_path = arb(500) * arb.pi()
        disk_path = (
            (outer_radius + inner_radius)
            / (outer_radius - inner_radius)
        ).log()
        d_star = center_path + disk_path

        # Stable formulas.  Directly evaluating 1-tanh(D_*/2) at ordinary
        # precision would round away the gap of size about 10^(-683).
        t_star = (-d_star).exp()
        r_star = (1 - t_star) / (1 + t_star)
        delta_star = 2 * t_star / (1 + t_star)
        beta_star = ((1 + t_star) / (1 - t_star)).log()

        one_minus_two_theta = 1 - 2 * theta
        b_theta = (
            -delta_star.log()
            + beta_star / 2
            + ((1 / (theta * beta_star)).log() - 1) / 2
            + arb(2).log()
        )
        gaussian_prefactor_log = (
            1
            + (
                4
                * arb.pi()
                / (beta_star * one_minus_two_theta)
            ).sqrt()
        ).log()
        c0 = (
            gaussian_prefactor_log
            + 2
            * (b_theta - ell_norm) ** 2
            / (beta_star * one_minus_two_theta)
        )
        c1 = (
            2
            * ell_norm**2
            / (beta_star * one_minus_two_theta)
        )

        c0_ceiling = arb(C0_SAFE_CEILING)
        c1_ceiling = arb(C1_SAFE_CEILING)
        log_four = arb(4).log()
        delta_from_r = 1 - r_star
        beta_from_r = -r_star.log()

        gates = {
            "disk_path_ball_overlaps_log_four": disk_path.overlaps(log_four),
            "d_star_is_strictly_positive": d_star > 0,
            "t_star_is_strictly_between_zero_and_one": (
                t_star > 0 and t_star < 1
            ),
            "r_star_is_strictly_between_zero_and_one": (
                r_star > 0 and r_star < 1
            ),
            "delta_star_has_positive_lower_bound": delta_star > 0,
            "beta_star_has_positive_lower_bound": beta_star > 0,
            "stable_delta_overlaps_one_minus_r_star": (
                delta_star.overlaps(delta_from_r)
            ),
            "stable_beta_overlaps_negative_log_r_star": (
                beta_star.overlaps(beta_from_r)
            ),
            "delta_star_has_at_least_one_thousand_relative_bits": (
                delta_star.rel_accuracy_bits() >= 1000
            ),
            "beta_star_has_at_least_one_thousand_relative_bits": (
                beta_star.rel_accuracy_bits() >= 1000
            ),
            "b_theta_is_positive": b_theta > 0,
            "c0_is_positive": c0 > 0,
            "c1_is_positive": c1 > 0,
            "c0_is_below_frozen_safe_ceiling": c0 < c0_ceiling,
            "c1_is_below_frozen_safe_ceiling": c1 < c1_ceiling,
        }

        return {
            "arb_bits": ARB_BITS,
            "approximate_decimal_digits": 1233,
            "center_path_ball": center_path.str(90),
            "disk_path_ball": disk_path.str(90),
            "D_star_ball": d_star.str(100),
            "t_star_ball": t_star.str(100),
            "r_star_ball": r_star.str(720),
            "delta_star_ball": delta_star.str(100),
            "beta_star_ball": beta_star.str(100),
            "delta_star_relative_accuracy_bits": (
                delta_star.rel_accuracy_bits()
            ),
            "beta_star_relative_accuracy_bits": (
                beta_star.rel_accuracy_bits()
            ),
            "theta_ball": theta.str(30),
            "one_minus_two_theta_ball": one_minus_two_theta.str(40),
            "b_theta_ball": b_theta.str(100),
            "gaussian_prefactor_log_ball": (
                gaussian_prefactor_log.str(100)
            ),
            "C0_formula_ball": c0.str(100),
            "C1_formula_ball": c1.str(100),
            "C0_safe_ceiling": C0_SAFE_CEILING,
            "C1_safe_ceiling": C1_SAFE_CEILING,
            "computed_gates": gates,
            "computed_gates_passed": all(gates.values()),
        }
    finally:
        ctx.prec = previous_precision


def build_report() -> dict[str, Any]:
    exact = exact_geometry_certificate()
    intervals = arb_interval_certificate()
    computed_gates = {
        "python_flint_version_is_frozen": (
            flint.__version__ == EXPECTED_PYTHON_FLINT_VERSION
        ),
        "flint_version_is_frozen": (
            flint.__FLINT_VERSION__ == EXPECTED_FLINT_VERSION
        ),
        "all_exact_geometry_gates_pass": exact[
            "computed_gates_passed"
        ],
        "all_arb_interval_gates_pass": intervals[
            "computed_gates_passed"
        ],
    }
    source_inputs = [
        SOURCE_LOCK,
        PARENT_LOCK,
        PARENT_RESULT,
        PARENT_ARTIFACT,
        FORMAL_RESULT,
    ]
    return {
        "artifact_schema_version": 1,
        "audit_id": AUDIT_ID,
        "parent_audit_id": PARENT_AUDIT_ID,
        "candidate_id": "LOG-0001",
        "formal_candidate": True,
        "status": "TARGET_FREE_EXPLICIT_CONFORMAL_RATIO_PASSED",
        "source_lock": SOURCE_LOCK,
        "frozen_object": {
            "operator": "same LOG-0001 matching-space family L_s|_B",
            "determinant": "D_pol(s)=det_Fr(I-L_s|_B)",
            "clock": "T_gamma=sum log|G'|",
            "outer_stadium_radius": "1/1000",
            "proof_only_inner_stadium_radius": "3/5000",
            "normalized_Riemann_maps": (
                "h_L(0)=-pi/4, h_R(0)=pi/4, h_sigma'(0)>0"
            ),
            "auxiliary_fredholm_variable_kept_separate": True,
        },
        "exact_geometry_certificate": exact,
        "arb_interval_certificate": intervals,
        "proved_statement": {
            "Poincare_metric_convention": (
                "lambda_D(w)=2/(1-|w|^2)"
            ),
            "hyperbolic_path_bound": "D_*=500*pi+log(4)",
            "common_ratio_bound": (
                "r_L=r_R<=r_*=tanh(D_*/2)<1"
            ),
            "r_star_exact": (
                "(4*exp(500*pi)-1)/(4*exp(500*pi)+1)"
            ),
            "delta_star_exact": (
                "2*exp(-D_*)/(1+exp(-D_*))"
            ),
            "beta_star_exact": (
                "log((1+exp(-D_*))/(1-exp(-D_*)))"
            ),
        },
        "explicit_growth_ledger": {
            "rank_one_stream_count": 2,
            "ell_norm_safe_upper": "103/125",
            "coefficient_bound": (
                "|a_q(s)|<=q^(q/2)*(q+1)*"
                "(exp((103/125)*|s|)/delta_*)^q*"
                "r_*^(q^2/4-q/2)"
            ),
            "gaussian_theta": "1/4096",
            "master_bound": (
                "|D_pol(s)|<=(1+sqrt(4*pi/(beta_*(1-2*theta))))*"
                "exp(((103/125)*|s|+b_theta)^2/"
                "(beta_*(1-2*theta)))"
            ),
            "published_quadratic_envelope": (
                "|D_pol(s)|<=exp(3.45e689+"
                "4.20e682*(1+|s|)^2)"
            ),
            "same_object_determinant": True,
            "signed_trace_identity_replaced": False,
        },
        "analytic_proof_ledger": [
            "every disk B(x,1/1000), x in I_sigma, lies in U_sigma",
            "the midpoint-to-projection path costs at most 500*pi",
            "the projection-to-z disk path costs at most log(4)",
            "normalized Riemann maps are hyperbolic isometries",
            "translation by pi/2 identifies the left and right normalized stadium pairs",
            "stable t=exp(-D_*) formulas preserve the 10^(-683) gap",
            "the inherited two-stream coefficient theorem is unchanged",
            "a shifted-Gaussian sum converts the explicit coefficient bound into a numerical quadratic envelope",
        ],
        "computed_gates": computed_gates,
        "computed_gates_passed": all(computed_gates.values()),
        "error_budget": {
            "geometric_discretization": "none; no conformal grid or boundary solver",
            "operator_truncation": "none in the theorem",
            "rounding": "4096-bit outward Arb scalar intervals",
            "normalization": "one frozen Poincare convention and normalized Riemann maps",
            "cancellation": "absolute values used only for convergence and upper growth",
            "root_finding": "none; no Fredholm or target root is evaluated",
        },
        "data_firewall": {
            "prime_tables_used": False,
            "primality_predicates_used": False,
            "Riemann_zero_tables_used": False,
            "xi_or_zeta_evaluated": False,
            "Fredholm_determinant_evaluated": False,
            "Fredholm_roots_searched": False,
            "numerical_conformal_map_computed": False,
            "USTC_data_used": False,
            "fitting_or_parameter_search_used": False,
        },
        "claim_boundary": {
            "route_a_effect": (
                "A3 proof constants become fully explicit; tuple unchanged"
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
                "exact conformal ratios or sharp growth type",
                "exact order or any lower growth bound",
                "Fredholm or Riemann zeros and a T*log(T) divisor law",
                "completed-xi, quantization, Route B, Hilbert-Polya, or RH",
            ],
            "route_b_invocation_allowed": False,
        },
        "next_smallest_test": (
            "Audit whether one explicit nonzero coefficient or signed trace "
            "term can yield a theorem-level lower maximum-modulus bound "
            "without determinant roots or target data."
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
