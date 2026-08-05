#!/usr/bin/env python3
"""Validated sharp distortion and ACIP bounds for the exact-U_c polar map."""

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
    from experiments import p4_logistic_uc_acip_cone_enclosure as coarse
    from experiments import p4_logistic_uc_first_return_support as support
except ModuleNotFoundError:  # Direct execution from the repository root.
    import p4_logistic_uc_acip_cone_enclosure as coarse
    import p4_logistic_uc_first_return_support as support


AUDIT_ID = "P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE"
PARENT_AUDIT_ID = "P4-LOGISTIC-UC-ACIP-CONE-ENCLOSURE"
SOURCE_LOCK = (
    "configs/source_locks/P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE.yaml"
)
FORMAL_RESULT = "formal/results/exact_uc_acip_sharp_cone_enclosure.md"
GENERATOR = "experiments/p4_logistic_uc_acip_sharp_cone_enclosure.py"

ARB_DECIMAL_DIGITS = 100
GRID_INTERVALS = 1 << 18
EXPECTED_PYTHON_FLINT_VERSION = "0.9.0"
EXPECTED_FLINT_VERSION = "3.6.0"

D_LOWER_SAFE = "0.17013"
D_UPPER_SAFE = "0.17014"
KAPPA_UPPER_SAFE = "0.595744"
CONE_SLOPE_NUMERATOR = 42535
CONE_SLOPE_DENOMINATOR = 101064
LOWER_WITNESS_T = ("0.75575", "0.75576")

SAFE_ENCLOSURES = {
    "conditional_theta_density_w_0": ("0.22460", "0.43504"),
    "conditional_x_density_g_A_0": ("0.41310", "0.80016"),
    "full_physical_density_h_0": ("0.20655", "0.40008"),
    "endpoint_coefficient_C_h": ("0.09461", "0.18327"),
}

REPRODUCTION_COMMAND = (
    "python3 experiments/p4_logistic_uc_acip_sharp_cone_enclosure.py --quiet "
    "--output artifacts/p4_logistic_uc_acip_sharp_cone_enclosure/"
    "interval_certificate.json"
)


def file_sha256(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def root_ball() -> arb:
    return arb(support.U_LOWER_TEXT).union(arb(support.U_UPPER_TEXT))


def distortion_squared(u: arb, rho: arb, t: arb) -> tuple[arb, arb]:
    """Return R=D^2 and its positive denominator on a closed t interval."""

    y = rho**2 * t
    denominator = 16 * (1 - y) * (2 - u * y) * (1 - u * y) ** 4
    numerator = u * y * (rho**2 - y) * (u**2 * y - 3 * u + 2) ** 2
    return numerator / denominator, denominator


def full_cover_certificate(u: arb, rho: arb) -> dict[str, Any]:
    threshold = arb(D_UPPER_SAFE) ** 2
    maximum_upper = arb(0)
    maximum_cell = -1
    minimum_denominator_lower: arb | None = None
    denominators_positive = True
    upper_threshold_passed = True

    for index in range(GRID_INTERVALS):
        t_interval = (arb(index) / GRID_INTERVALS).union(
            arb(index + 1) / GRID_INTERVALS
        )
        value, denominator = distortion_squared(u, rho, t_interval)
        denominator_lower = denominator.lower()
        if minimum_denominator_lower is None or (
            denominator_lower < minimum_denominator_lower
        ):
            minimum_denominator_lower = denominator_lower
        if not (denominator > 0):
            denominators_positive = False
            upper_threshold_passed = False
            break
        if not value.is_finite() or not (value < threshold):
            upper_threshold_passed = False
            break
        value_upper = value.upper()
        if value_upper > maximum_upper:
            maximum_upper = value_upper
            maximum_cell = index

    if minimum_denominator_lower is None:
        raise RuntimeError("empty distortion cover")

    return {
        "coordinate": "t=y/rho^2",
        "domain": ["0", "1"],
        "closed_interval_count": GRID_INTERVALS,
        "all_denominators_strictly_positive": denominators_positive,
        "all_cells_below_D_upper_squared": upper_threshold_passed,
        "D_upper_safe": D_UPPER_SAFE,
        "maximum_interval_upper_cell_index": maximum_cell,
        "maximum_interval_upper_t_cell": [
            f"{maximum_cell}/{GRID_INTERVALS}",
            f"{maximum_cell + 1}/{GRID_INTERVALS}",
        ],
        "maximum_interval_upper_for_R": maximum_upper.str(40),
        "minimum_denominator_lower": minimum_denominator_lower.str(40),
    }


def lower_witness_certificate(u: arb, rho: arb) -> dict[str, Any]:
    t_interval = arb(LOWER_WITNESS_T[0]).union(arb(LOWER_WITNESS_T[1]))
    value, denominator = distortion_squared(u, rho, t_interval)
    threshold = arb(D_LOWER_SAFE) ** 2
    return {
        "closed_t_interval": list(LOWER_WITNESS_T),
        "R_ball": value.str(40),
        "denominator_strictly_positive": denominator > 0,
        "all_points_above_D_lower_squared": value > threshold,
        "D_lower_safe": D_LOWER_SAFE,
    }


def density_enclosures(u: arb, rho: arb) -> tuple[dict[str, Any], dict[str, bool]]:
    cone_slope = arb(CONE_SLOPE_NUMERATOR) / CONE_SLOPE_DENOMINATOR
    exponential = (cone_slope * arb.pi() / 2).exp()
    w_lower = cone_slope / (2 * (exponential - 1))
    w_upper = cone_slope / (2 * (1 - 1 / exponential))
    g_lower = w_lower / rho
    g_upper = w_upper / rho
    h_lower = g_lower / 2
    h_upper = g_upper / 2
    coefficient_lower = h_lower / (arb(2).sqrt() * u)
    coefficient_upper = h_upper / (arb(2).sqrt() * u)

    raw = {
        "conditional_theta_density_w_0": (w_lower, w_upper),
        "conditional_x_density_g_A_0": (g_lower, g_upper),
        "full_physical_density_h_0": (h_lower, h_upper),
        "endpoint_coefficient_C_h": (coefficient_lower, coefficient_upper),
    }
    rows: dict[str, Any] = {}
    gates: dict[str, bool] = {}
    for name, (lower, upper) in raw.items():
        safe_lower, safe_upper = SAFE_ENCLOSURES[name]
        gates[f"{name}_inside_safe_interval"] = (
            lower > arb(safe_lower) and upper < arb(safe_upper)
        )
        rows[name] = {
            "safe_lower": safe_lower,
            "safe_upper": safe_upper,
            "validated_lower_formula_ball": lower.str(50),
            "validated_upper_formula_ball": upper.str(50),
        }
    rows["normalization_identity"] = "g_A(0)=2*h(0)"
    return rows, gates


def finite_branch_mass_rows() -> list[dict[str, Any]]:
    coefficient_lower, coefficient_upper = SAFE_ENCLOSURES[
        "endpoint_coefficient_C_h"
    ]
    with localcontext() as decimal_context:
        decimal_context.prec = coarse.DECIMAL_DIGITS
        return coarse.finite_branch_mass_rows(
            Decimal(coefficient_lower), Decimal(coefficient_upper)
        )


def build_report() -> dict[str, Any]:
    previous_precision = ctx.prec
    try:
        ctx.dps = ARB_DECIMAL_DIGITS
        u = root_ball()
        rho = u - 1
        cover = full_cover_certificate(u, rho)
        lower_witness = lower_witness_certificate(u, rho)
        enclosures, enclosure_gates = density_enclosures(u, rho)
        mass_rows = finite_branch_mass_rows()

        d_upper = arb(D_UPPER_SAFE)
        kappa_upper = arb(KAPPA_UPPER_SAFE)
        cone_slope = arb(CONE_SLOPE_NUMERATOR) / CONE_SLOPE_DENOMINATOR
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
            "root_ball_is_strictly_inside_1_5_and_2": u > arb("1.5") and u < 2,
            "all_cover_denominators_are_positive": cover[
                "all_denominators_strictly_positive"
            ],
            "full_cover_proves_D_below_0_17014": cover[
                "all_cells_below_D_upper_squared"
            ],
            "lower_witness_proves_D_above_0_17013": lower_witness[
                "denominator_strictly_positive"
            ]
            and lower_witness["all_points_above_D_lower_squared"],
            "inverse_contraction_below_0_595744": u**2 / 4 < kappa_upper,
            "sharp_cone_bound_identity_is_exact": (
                Fraction(D_UPPER_SAFE)
                + Fraction(KAPPA_UPPER_SAFE)
                * Fraction(CONE_SLOPE_NUMERATOR, CONE_SLOPE_DENOMINATOR)
                == Fraction(CONE_SLOPE_NUMERATOR, CONE_SLOPE_DENOMINATOR)
            ),
            "physical_return_labels_are_sealed": (
                [row["physical_return_label"] for row in mass_rows]
                == [12, 14, 16, 18]
            ),
            "all_four_endpoint_radius_gates_pass": all(
                row["endpoint_radius_gate_passed"] for row in mass_rows
            ),
            "all_four_mass_intervals_have_strict_order": all(
                Decimal(row["certified_mass"]["lower"])
                < Decimal(row["certified_mass"]["upper"])
                for row in mass_rows
            ),
            "all_four_finite_mass_intervals_are_positive": all(
                Decimal(row["certified_mass"]["lower"]) > 0 for row in mass_rows
            ),
            **enclosure_gates,
        }

        source_inputs = [
            SOURCE_LOCK,
            FORMAL_RESULT,
            coarse.SOURCE_LOCK,
            coarse.FORMAL_RESULT,
            "experiments/p4_logistic_uc_acip_cone_enclosure.py",
            "experiments/p4_logistic_uc_first_return_support.py",
            "formal/results/exact_uc_first_return_support.md",
        ]

        return {
            "artifact_schema_version": 1,
            "audit_id": AUDIT_ID,
            "parent_audit_id": PARENT_AUDIT_ID,
            "formal_candidate": False,
            "status": "NUMERICALLY_CERTIFIED_SHARP_CONE",
            "source_lock": SOURCE_LOCK,
            "mathematical_object": {
                "map": "f(x)=1-U_c*x^2 on J=[-(U_c-1),1]",
                "polar_map": (
                    "G=q^(-1) o (-f^2) o q, q(theta)=(U_c-1)*sin(theta)"
                ),
                "distortion_function": (
                    "R=D^2=u*y*(rho^2-y)*(u^2*y-3*u+2)^2/"
                    "(16*(1-y)*(2-u*y)*(1-u*y)^4), y=rho^2*t"
                ),
            },
            "validated_environment": {
                "python": platform.python_version(),
                "python_flint": flint.__version__,
                "flint": flint.__FLINT_VERSION__,
                "arb_decimal_digits": ARB_DECIMAL_DIGITS,
            },
            "certified_root_ball": u.str(110),
            "distortion_certificate": {
                "global_cover": cover,
                "lower_witness": lower_witness,
                "certified_statement": "0.17013 < D < 0.17014",
            },
            "cone_ledger": {
                "inverse_contraction_safe_upper": KAPPA_UPPER_SAFE,
                "distortion_safe_upper": D_UPPER_SAFE,
                "log_lipschitz_cone_slope": (
                    f"{CONE_SLOPE_NUMERATOR}/{CONE_SLOPE_DENOMINATOR}"
                ),
                "invariance_identity": (
                    "0.17014 + 0.595744*(42535/101064) "
                    "= 42535/101064"
                ),
            },
            "certified_enclosures": enclosures,
            "finite_branch_mass_enclosures": mass_rows,
            "computed_gates": computed_gates,
            "computed_gates_passed": all(computed_gates.values()),
            "error_budget": {
                "discretization": (
                    "2^18 closed Arb cells cover [0,1]; interval dependency only widens enclosures"
                ),
                "truncation": "not used; no operator or orbit truncation enters",
                "rounding": "Arb directed real balls at 100 decimal digits",
                "normalization": "w -> g_A -> h -> C_h is explicit",
                "iteration_stopping": "not used; no stationary-vector solve enters",
                "resolvent_tail": (
                    "not used; the parent analytic cone controls the invariant density"
                ),
            },
            "claim_boundary": {
                "established": [
                    "validated 0.17013<D<0.17014 on the full distortion domain",
                    "sharper target-free safe enclosures of w(0), g_A(0), h(0), and C_h",
                    "tighter certified masses for physical returns 12,14,16,18",
                ],
                "not_established": [
                    "a closed form or narrow interval-Ulam/resolvent enclosure",
                    "an exponential finite-order mass remainder",
                    "an arithmetic orbit law, determinant, quantization, Route B, or RH",
                ],
            },
            "route_a_effect": {
                "tuple_unchanged": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
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
            "artifacts/p4_logistic_uc_acip_sharp_cone_enclosure/"
            "interval_certificate.json"
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
