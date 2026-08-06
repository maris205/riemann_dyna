#!/usr/bin/env python3
"""Same-operator relative Fredholm determinant audit for QG-0001.

The theorem-level object is

    D_H(k) = det_F(I - k^2 H^{-1}) = product_{n>=1} chi_0(k/n),

where H is the frozen harmonic direct sum of magnetic graph Laplacians.  The
finite products below are target-free implementation controls only.  They do
not define the determinant by cutoff and they do not read prime/zero tables.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

if __package__:
    from experiments.qg_0001_base_characteristic import (
        LENGTHS_SYM,
        exact_zero_characteristic,
        physical_characteristic_numeric,
        pole_free_expression,
    )
else:
    from qg_0001_base_characteristic import (
        LENGTHS_SYM,
        exact_zero_characteristic,
        physical_characteristic_numeric,
        pole_free_expression,
    )


MP_DPS = 80
PRODUCT_CUTOFFS = (8, 16, 32, 64, 128, 256)
SAMPLE_K = ("0.11", "0.25", "0.5", "0.731")


def _mp_text(value: mp.mpf | mp.mpc, digits: int = 45) -> str:
    if isinstance(value, mp.mpc):
        sign = "+" if value.imag >= 0 else "-"
        return (
            f"{mp.nstr(value.real, digits)} {sign} "
            f"{mp.nstr(abs(value.imag), digits)}i"
        )
    return mp.nstr(value, digits)


def _parse_mp_complex(value: str) -> mp.mpc:
    """Parse the deterministic complex format emitted by _mp_text."""
    body = value.removesuffix("i")
    if " + " in body:
        real, imaginary = body.rsplit(" + ", 1)
        return mp.mpc(mp.mpf(real), mp.mpf(imaginary))
    if " - " in body:
        real, imaginary = body.rsplit(" - ", 1)
        return mp.mpc(mp.mpf(real), -mp.mpf(imaginary))
    return mp.mpc(mp.mpf(body), 0)


def exact_coefficients() -> dict[str, sp.Expr]:
    """Return exact local and tower trace coefficients."""
    k = sp.symbols("k")
    pole_free = pole_free_expression(k)
    base_value = exact_zero_characteristic()
    series = sp.series(pole_free, k, 0, 6).removeO().expand()
    base_quadratic = sp.simplify(series.coeff(k, 4) / base_value)
    trace_h1_inverse = sp.simplify(-base_quadratic)
    trace_h_inverse = sp.simplify(sp.zeta(2) * trace_h1_inverse)
    tower_quadratic = sp.simplify(-trace_h_inverse)
    return {
        "base_value": base_value,
        "base_quadratic": base_quadratic,
        "trace_h1_inverse": trace_h1_inverse,
        "trace_h_inverse": trace_h_inverse,
        "tower_quadratic": tower_quadratic,
    }


def chi_zero_numeric(k: mp.mpf, base_value: mp.mpf) -> mp.mpc:
    return physical_characteristic_numeric(k) / base_value


def finite_product_ledger(
    k: mp.mpf,
    base_value: mp.mpf,
    base_quadratic: mp.mpf,
    total_length: mp.mpf,
) -> list[dict]:
    """Compute frozen partial products and first-tail-corrected diagnostics."""
    product = mp.mpc(1)
    harmonic_one = mp.mpf(0)
    harmonic_two = mp.mpf(0)
    rows: list[dict] = []
    cutoff_set = set(PRODUCT_CUTOFFS)
    for component in range(1, PRODUCT_CUTOFFS[-1] + 1):
        q = k / component
        product *= chi_zero_numeric(q, base_value)
        harmonic_one += mp.mpf(1) / component
        harmonic_two += mp.mpf(1) / (component * component)
        if component not in cutoff_set:
            continue
        tail_two = mp.zeta(2) - harmonic_two
        tail_corrected = product * mp.exp(base_quadratic * k**2 * tail_two)
        raw_bond_product = product * mp.exp(1j * k * total_length * harmonic_one)
        expected_ratio = mp.exp(1j * k * total_length * harmonic_one)
        rows.append(
            {
                "components": component,
                "physical_product": _mp_text(product),
                "leading_tail_corrected_product": _mp_text(tail_corrected),
                "sum_n_gt_N_inverse_square": _mp_text(tail_two),
                "raw_bond_product": _mp_text(raw_bond_product),
                "raw_phase_argument_unwrapped": _mp_text(
                    k * total_length * harmonic_one
                ),
                "raw_over_physical_ratio_residual": _mp_text(
                    raw_bond_product / product - expected_ratio
                ),
            }
        )
    return rows


def build_report() -> dict:
    mp.mp.dps = MP_DPS
    coefficients = exact_coefficients()
    base_value_mp = mp.mpf(str(sp.N(coefficients["base_value"], MP_DPS)))
    base_quadratic_mp = mp.mpf(
        str(sp.N(coefficients["base_quadratic"], MP_DPS))
    )
    trace_h1_mp = mp.mpf(
        str(sp.N(coefficients["trace_h1_inverse"], MP_DPS))
    )
    trace_h_mp = mp.mpf(str(sp.N(coefficients["trace_h_inverse"], MP_DPS)))
    tower_quadratic_mp = mp.mpf(
        str(sp.N(coefficients["tower_quadratic"], MP_DPS))
    )
    total_length_exact = sp.simplify(sum(LENGTHS_SYM))
    total_length_mp = mp.mpf(str(sp.N(total_length_exact, MP_DPS)))
    coefficient_ratio_exact = sp.simplify(2 * total_length_exact)

    samples = []
    max_ratio_residual = mp.mpf(0)
    max_corrected_last_step = mp.mpf(0)
    for sample in SAMPLE_K:
        value = mp.mpf(sample)
        ledger = finite_product_ledger(
            value,
            base_value_mp,
            base_quadratic_mp,
            total_length_mp,
        )
        for row in ledger:
            max_ratio_residual = max(
                max_ratio_residual,
                abs(_parse_mp_complex(row["raw_over_physical_ratio_residual"])),
            )
        previous = _parse_mp_complex(
            ledger[-2]["leading_tail_corrected_product"]
        )
        latest = _parse_mp_complex(ledger[-1]["leading_tail_corrected_product"])
        corrected_last_step = abs(latest - previous)
        max_corrected_last_step = max(max_corrected_last_step, corrected_last_step)
        samples.append({"k": sample, "partial_products": ledger})

    return {
        "candidate_id": "QG-0001",
        "subaudit_id": "QG-0001-RELATIVE-FREDHOLM-001",
        "source_lock": "configs/source_locks/QG-0001-RELATIVE-FREDHOLM.yaml",
        "parent_source_locks": [
            "configs/source_locks/QG-0001.yaml",
            "configs/source_locks/QG-0001-BASE-CHARACTERISTIC.yaml",
        ],
        "target_data_used": {
            "prime_table": False,
            "zero_table": False,
            "fitting": False,
        },
        "operator": {
            "definition": "H=direct_sum_{n>=1} H_n",
            "domain": "{u=(u_n): u_n in Dom(H_n), sum_n ||H_n u_n||^2 < infinity}",
            "component_scaling": "H_n unitarily equivalent to n^2 H_1",
            "strictly_positive": True,
            "inverse_class": "trace_class",
            "trace_class_identity": "Tr(H^{-1})=zeta(2)*Tr(H_1^{-1})",
            "schatten_H_inverse": "H^{-1} is in S_p exactly for p>1/2",
            "schatten_H_minus_half": "H^{-1/2} is in S_p exactly for p>1",
            "compact_resolvent": True,
        },
        "determinant": {
            "convention": "D_H(k)=det_F(I-k^2*H^{-1})=det_rel(H-k^2,H)",
            "component_identity": "D_H(k)=product_{n>=1} chi_0(k/n)",
            "bond_factor_identity": "chi_0(k/n)=exp(-i*k*L0/n)*beta_n(k)",
            "normal_convergence_on_compacts": True,
            "base_factor_is_fredholm": "chi_0(k)=det_F(I-k^2*H_1^{-1})",
            "zero_divisor": "k=+/-n*sqrt(lambda_j(H_1)), with multiplicity",
            "coincident_pair_multiplicities_add": True,
            "zero_at_origin": False,
            "entire_order_in_k": 1,
            "canonical_genus_in_k": 1,
            "entire_type_in_k": "infinite",
            "finite_exponential_type_in_k": False,
            "entire_order_in_z_equals_k_squared": "1/2",
            "paired_canonical_genus_in_z_equals_k_squared": 0,
            "imaginary_axis_growth": "log(D_H(iR))=L0*R*log(R)+O(R)",
            "is_naive_orbit_product": False,
            "is_direct_sum_bond_block_determinant": False,
            "is_heat_or_spectral_zeta": False,
            "is_completed_xi": False,
        },
        "exact_coefficients": {
            "L0": str(total_length_exact),
            "base_quadratic": str(coefficients["base_quadratic"]),
            "trace_H1_inverse": str(coefficients["trace_h1_inverse"]),
            "trace_H_inverse": str(coefficients["trace_h_inverse"]),
            "tower_quadratic": str(coefficients["tower_quadratic"]),
            "trace_H1_inverse_decimal": _mp_text(trace_h1_mp),
            "trace_H_inverse_decimal": _mp_text(trace_h_mp),
            "tower_quadratic_decimal": _mp_text(tower_quadratic_mp),
        },
        "counting": {
            "positive_wavenumber_count": "N_H(K)=(L0/pi)*K*log(K)+O(K)",
            "riemann_von_mangoldt_leading_coefficient": "1/(2*pi)",
            "candidate_leading_coefficient": "L0/pi",
            "candidate_to_target_ratio_exact": str(coefficient_ratio_exact),
            "candidate_to_target_ratio_decimal": _mp_text(
                2 * total_length_mp
            ),
            "leading_coefficient_matches_target": False,
            "zero_free_prefactor_can_repair_count": False,
        },
        "raw_bond_product": {
            "uncounterphased_factor": "beta_n(k)=exp(i*k*L0/n)*chi_0(k/n)",
            "partial_product_phase": "exp(i*k*L0*H_N)",
            "standalone_product_converges_away_from_the_divisor_for_nonzero_real_k": False,
            "reason": "H_N=log(N)+EulerGamma+o(1), so the unwrapped phase is unbounded away from zeros of the physical product",
            "counterphase_must_remain_factorwise": True,
        },
        "finite_product_controls": {
            "cutoffs": list(PRODUCT_CUTOFFS),
            "samples": samples,
            "tail_correction": "exp(a2*k^2*sum_{n>N}n^-2); diagnostic only",
            "max_raw_ratio_residual": _mp_text(max_ratio_residual),
            "max_tail_corrected_128_to_256_drift": _mp_text(
                max_corrected_last_step
            ),
        },
        "route_a": {
            "a1_changed": False,
            "a2_global_same_operator_determinant_now_defined": True,
            "a2_target_match": False,
            "a3_target_counting_match": False,
            "a4_same_operator_compatibility": True,
            "route_b_invoked": False,
        },
        "structural_conclusion": (
            "The frozen tower has a genuine same-operator trace-class relative "
            "Fredholm determinant. It is the normally convergent product of the "
            "dephased physical component characteristics, not the failed orbit or "
            "bond-block product. Its exact divisor has the wrong frozen leading "
            "counting coefficient, so determinant existence does not produce a "
            "Riemann Route-A match."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()
    report = build_report()
    payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    if not args.quiet:
        print(payload)


if __name__ == "__main__":
    main()
