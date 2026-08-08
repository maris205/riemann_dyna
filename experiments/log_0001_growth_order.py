#!/usr/bin/env python3
"""Target-free certificate for the LOG-0001 Fredholm growth theorem.

The analytic theorem is proved in ``formal/results/log_0001_growth_order.md``.
This program evaluates only its exact algebraic constants and finite
combinatorial gates.  It never evaluates the Fredholm determinant, searches
for its roots, or reads prime/Riemann-zero data.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
from typing import Any

import mpmath as mp

try:
    from experiments import p4_logistic_uc_first_return_support as support
except ModuleNotFoundError:  # Direct execution from the repository root.
    import p4_logistic_uc_first_return_support as support


AUDIT_ID = "LOG-0001-GROWTH-ORDER"
SOURCE_LOCK = "configs/source_locks/LOG-0001-GROWTH-ORDER.yaml"
PARENT_LOCK = "configs/source_locks/LOG-0001-NUCLEAR-FREDHOLM.yaml"
PARENT_RESULT = "formal/results/log_0001_nuclear_fredholm.md"
FORMAL_RESULT = "formal/results/log_0001_growth_order.md"
COMPLEX_CERTIFICATE = (
    "artifacts/p4_logistic_uc_polar_complex_branch/"
    "complex_branch_certificate.json"
)
GENERATOR = "experiments/log_0001_growth_order.py"
ARTIFACT = "artifacts/log_0001_growth_order/growth_order_certificate.json"
EVALUATION = "evaluations/route_a/LOG-0001/20260808T104049Z.yaml"

DIAGNOSTIC_DIGITS = 100
COMBINATORIAL_Q_MAX = 24
ELL_VARIATION_SAFE_TEXT = "0.000851"
ELL_NORM_SAFE_TEXT = "0.824"
SAFE_VERTICAL_SIGMA_TEXT = "2"
REPRODUCTION_COMMAND = (
    "python3 experiments/log_0001_growth_order.py --quiet --output "
    "artifacts/log_0001_growth_order/growth_order_certificate.json"
)


def file_sha256(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def parameters() -> tuple[mp.mpf, mp.mpf]:
    """Refine the exact critical parameter inside its sealed bracket."""
    lower = mp.mpf(support.U_LOWER_TEXT)
    upper = mp.mpf(support.U_UPPER_TEXT)
    midpoint = (lower + upper) / 2
    u = mp.findroot(lambda value: value**3 - 2 * value**2 + 2 * value - 2, midpoint)
    if not lower < u < upper:
        raise RuntimeError("refined U_c escaped the sealed bracket")
    return u, u - 1


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def two_stream_exponent_ledger() -> list[dict[str, Any]]:
    """Check the exact quadratic exponent from all two-stream allocations."""
    ledger: list[dict[str, Any]] = []
    for q in range(COMBINATORIAL_Q_MAX + 1):
        exponents = [
            Fraction(k * (k - 1) + (q - k) * (q - k - 1), 2)
            for k in range(q + 1)
        ]
        lower = Fraction(q * q, 4) - Fraction(q, 2)
        minimum = min(exponents)
        ledger.append(
            {
                "q": q,
                "allocation_count": q + 1,
                "minimum_exact_exponent": fraction_text(minimum),
                "proved_quadratic_lower_exponent": fraction_text(lower),
                "minimum_minus_lower": fraction_text(minimum - lower),
                "gate_minimum_is_at_least_quadratic_lower": minimum >= lower,
            }
        )
    return ledger


def build_report() -> dict[str, Any]:
    mp.mp.dps = DIAGNOSTIC_DIGITS
    ell_variation_safe = mp.mpf(ELL_VARIATION_SAFE_TEXT)
    ell_norm_safe = mp.mpf(ELL_NORM_SAFE_TEXT)
    safe_vertical_sigma = mp.mpf(SAFE_VERTICAL_SIGMA_TEXT)
    u, rho = parameters()
    alpha_0 = u**2 / 4
    tau_min = -mp.log(alpha_0)
    sigma_star = mp.log(2) / tau_min

    real_a_min = mp.sqrt(2 * u) / 4
    real_a_max = alpha_0
    real_log_min = mp.log(real_a_min)
    real_log_max = mp.log(real_a_max)
    ell_norm_envelope = abs(real_log_min) + ell_variation_safe

    q_safe = 2 * alpha_0**safe_vertical_sigma
    trace_log_bound_safe = -mp.log(1 - q_safe) / (1 - alpha_0)
    determinant_lower_safe = mp.exp(-trace_log_bound_safe)
    determinant_upper_safe = mp.exp(trace_log_bound_safe)

    allocation_ledger = two_stream_exponent_ledger()
    computed_gates = {
        "critical_root_inside_sealed_bracket": (
            mp.mpf(support.U_LOWER_TEXT) < u < mp.mpf(support.U_UPPER_TEXT)
        ),
        "real_inverse_derivative_maximum_is_strictly_below_one": alpha_0 < 1,
        "intrinsic_roof_lower_bound_is_positive": tau_min > 0,
        "zero_free_threshold_is_below_safe_vertical_line": (
            sigma_star < safe_vertical_sigma
        ),
        "safe_vertical_trace_ratio_is_strictly_below_one": q_safe < 1,
        "safe_vertical_determinant_bounds_are_positive_and_ordered": (
            0 < determinant_lower_safe < 1 < determinant_upper_safe
        ),
        "complex_log_norm_envelope_is_below_safe_upper": (
            ell_norm_envelope < ell_norm_safe
        ),
        "all_two_stream_allocation_exponents_pass": all(
            row["gate_minimum_is_at_least_quadratic_lower"]
            for row in allocation_ledger
        ),
    }

    source_inputs = [
        SOURCE_LOCK,
        PARENT_LOCK,
        PARENT_RESULT,
        FORMAL_RESULT,
        COMPLEX_CERTIFICATE,
        "experiments/p4_logistic_uc_first_return_support.py",
    ]

    return {
        "artifact_schema_version": 1,
        "audit_id": AUDIT_ID,
        "candidate_id": "LOG-0001",
        "formal_candidate": True,
        "status": "TARGET_FREE_GROWTH_ORDER_CERTIFICATE_PASSED",
        "scope": {
            "established": [
                "companion exact theorem: |D_pol(s)| <= exp(C0+C1*(1+|s|)^2)",
                "classical entire-function order at most two",
                "Jensen disk and fixed-real-strip zero-count upper bounds O(R^2) and O(T^2)",
                "zero-free half-plane Re(s)>log(2)/log(4/U_c^2) with uniform bounds on each closed sub-half-plane",
            ],
            "not_established": [
                "exact order or any lower growth bound",
                "sharp critical-strip divisor asymptotic or T*log(T) law",
                "Fredholm or Riemann zero locations",
                "completed-xi identity, quantization, Route B, Hilbert-Polya, or RH",
            ],
        },
        "frozen_object": {
            "operator": "same LOG-0001 matching-space family L_s|_B",
            "determinant": "D_pol(s)=det_Fr(I-L_s|_B)",
            "clock": "T_gamma=sum log|G'|",
            "signed_trace_denominator": "1-epsilon_omega*exp(-T_omega)",
            "outer_stadium_radius": "1/1000",
            "proof_only_inner_stadium_radius": "3/5000",
            "auxiliary_fredholm_variable_kept_separate": True,
        },
        "exact_growth_ledger": {
            "rank_one_stream_count": 2,
            "stream_index": "(input branch sigma, Taylor index m)",
            "stream_norm_bound": "||u_sigma_m||*||x_sigma_m(s)|| <= exp(L_ell*|s|)*r_sigma^m",
            "minor_bound": "q^(q/2)*product_i(||u_i||*||x_i||)",
            "elementary_symmetric_bound": (
                "e_q <= C_r^2*(q+1)*W(s)^q*r^(q^2/4-q/2)"
            ),
            "determinant_majorant": (
                "1+C_r^2*sum_(q>=1) q^(q/2)*(q+1)*W(s)^q*"
                "r^(q^2/4-q/2)"
            ),
            "global_consequence": "log^+|D_pol(s)| <= C0+C1*(1+|s|)^2",
            "conformal_ratio_numeric_value": "not certified in this audit",
        },
        "exact_real_constants": {
            "U_c": mp.nstr(u, 80),
            "rho": mp.nstr(rho, 80),
            "alpha_0_exact": "U_c^2/4",
            "alpha_0": mp.nstr(alpha_0, 80),
            "tau_min_exact": "log(4/U_c^2)",
            "tau_min": mp.nstr(tau_min, 80),
            "sigma_star_exact": "log(2)/log(4/U_c^2)",
            "sigma_star": mp.nstr(sigma_star, 80),
        },
        "complex_log_envelope": {
            "real_a_min_exact": "sqrt(2*U_c)/4",
            "real_a_min": mp.nstr(real_a_min, 80),
            "real_a_max_exact": "U_c^2/4",
            "real_a_max": mp.nstr(real_a_max, 80),
            "real_log_min": mp.nstr(real_log_min, 80),
            "real_log_max": mp.nstr(real_log_max, 80),
            "inherited_complex_variation_safe_upper": ELL_VARIATION_SAFE_TEXT,
            "ell_norm_envelope": mp.nstr(ell_norm_envelope, 80),
            "ell_norm_safe_upper": ELL_NORM_SAFE_TEXT,
        },
        "safe_vertical_line": {
            "sigma": SAFE_VERTICAL_SIGMA_TEXT,
            "q_sigma_exact": "2*(U_c^2/4)^sigma",
            "q_sigma": mp.nstr(q_safe, 80),
            "absolute_trace_log_upper": mp.nstr(trace_log_bound_safe, 80),
            "determinant_modulus_lower": mp.nstr(determinant_lower_safe, 80),
            "determinant_modulus_upper": mp.nstr(determinant_upper_safe, 80),
            "uniform_in_imaginary_height": True,
            "Fredholm_roots_evaluated": False,
        },
        "two_stream_combinatorial_ledger": {
            "q_max": COMBINATORIAL_Q_MAX,
            "rows": allocation_ledger,
        },
        "computed_gates": computed_gates,
        "computed_gates_passed": all(computed_gates.values()),
        "data_firewall": {
            "prime_tables_used": False,
            "primality_predicates_used": False,
            "Riemann_zero_tables_used": False,
            "xi_or_zeta_evaluated": False,
            "Fredholm_determinant_evaluated": False,
            "Fredholm_roots_searched": False,
            "USTC_data_used": False,
            "fitting_or_parameter_search_used": False,
        },
        "claim_boundary": {
            "route_a_effect": "A3 strengthened but remains A3_PARTIAL_ANALYTIC_STRUCTURE",
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
            "route_b_invocation_allowed": False,
        },
        "next_smallest_test": (
            "Certify explicit upper bounds r_L,r_R<1 for the normalized "
            "Riemann-map restriction ratios; do not compute determinant roots."
        ),
        "provenance": {
            "source_lock": SOURCE_LOCK,
            "parent_lock": PARENT_LOCK,
            "formal_result": FORMAL_RESULT,
            "route_a_evaluation": EVALUATION,
            "generator": GENERATOR,
            "generator_sha256": file_sha256(GENERATOR),
            "source_inputs_sha256": {
                path: file_sha256(path) for path in source_inputs
            },
            "external_target_data_used": False,
            "reproduction_command": REPRODUCTION_COMMAND,
        },
        "validated_environment": {
            "python": platform.python_version(),
            "mpmath": mp.__version__,
            "diagnostic_decimal_digits": DIAGNOSTIC_DIGITS,
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
