#!/usr/bin/env python3
"""Base-component characteristic audit for QG-0001.

This is a deliberately local sub-audit.  It defines the physical n=1
vertex-matching characteristic with sinc continuation, compares it with the
parent directed-bond determinant, and resolves the apparent k=0 bond zero.
It does not define a tower determinant or read any prime/zero data.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable

import mpmath as mp
import sympy as sp

if __package__:
    from experiments.qg_0001_harmonic_magnetic_tower import scattering_matrix
else:
    from qg_0001_harmonic_magnetic_tower import scattering_matrix


MP_DPS = 80
LENGTHS_SYM = (sp.Integer(1), sp.sqrt(2), sp.sqrt(3), sp.sqrt(5))
PHASES_SYM = (sp.Integer(0), sp.pi / 3, 2 * sp.pi / 3, sp.Integer(0))
PHASE_FACTORS_SYM = (
    sp.Integer(1),
    sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2,
    -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2,
    sp.Integer(1),
)
SAMPLE_K = ("0.11", "0.731", "1.2", "pi")


def _remaining(values: Iterable[int], excluded: Iterable[int]) -> list[int]:
    return sorted(set(values) - set(excluded))


def pole_free_expression(k: sp.Symbol) -> sp.Expr:
    """Return the exact entire F(k)=k^2*C_phys(k) expression."""
    lengths = LENGTHS_SYM
    phases = PHASES_SYM
    s = [sp.sin(k * value) for value in lengths]
    c = [sp.cos(k * value) for value in lengths]
    theta = -3 * s[0] * s[1] * s[2]
    for i in range(3):
        for j in range(i + 1, 3):
            ell = _remaining(range(3), (i, j))[0]
            theta += 2 * s[ell] * (
                c[i] * c[j] - sp.cos(phases[i] - phases[j])
            )
    pendant = sum(
        c[i]
        * s[_remaining(range(3), (i,))[0]]
        * s[_remaining(range(3), (i,))[1]]
        for i in range(3)
    )
    return sp.expand_trig(s[3] * theta + c[3] * pendant)


def physical_zero_matrix() -> sp.Matrix:
    """Exact k=0 sinc-matching matrix in the frozen gauge convention."""
    matrix = sp.zeros(6, 6)
    for edge, length in enumerate(LENGTHS_SYM):
        matrix[edge, 0] = 1
        if edge < 3:
            matrix[edge, 1] = -sp.conjugate(PHASE_FACTORS_SYM[edge])
        matrix[edge, 2 + edge] = length
    for edge in range(4):
        matrix[4, 2 + edge] = 1
    for edge in range(3):
        matrix[5, 2 + edge] = -PHASE_FACTORS_SYM[edge]
    return matrix


def exact_zero_characteristic() -> sp.Expr:
    return sp.simplify(sp.expand(physical_zero_matrix().det()))


def physical_matrix_numeric(k: mp.mpf) -> mp.matrix:
    lengths = [mp.mpf(1), mp.sqrt(2), mp.sqrt(3), mp.sqrt(5)]
    phases = [mp.mpf(0), mp.pi / 3, 2 * mp.pi / 3, mp.mpf(0)]
    s = [mp.sin(k * value) for value in lengths]
    c = [mp.cos(k * value) for value in lengths]
    matrix = mp.matrix(6, 6)
    for row in range(6):
        for column in range(6):
            matrix[row, column] = mp.mpc(0)
    for edge, length in enumerate(lengths):
        matrix[edge, 0] = c[edge]
        if edge < 3:
            matrix[edge, 1] = -mp.exp(-1j * phases[edge])
        matrix[edge, 2 + edge] = length if k == 0 else s[edge] / k
    for edge in range(4):
        matrix[4, 2 + edge] = 1
    matrix[5, 0] = k * sum(
        mp.exp(1j * phases[edge]) * s[edge] for edge in range(3)
    )
    for edge in range(3):
        matrix[5, 2 + edge] = -mp.exp(1j * phases[edge]) * c[edge]
    return matrix


def physical_characteristic_numeric(k: mp.mpf) -> mp.mpc:
    return mp.det(physical_matrix_numeric(k))


def pole_free_numeric(k: mp.mpf) -> mp.mpc:
    lengths = [mp.mpf(1), mp.sqrt(2), mp.sqrt(3), mp.sqrt(5)]
    phases = [mp.mpf(0), mp.pi / 3, 2 * mp.pi / 3, mp.mpf(0)]
    s = [mp.sin(k * value) for value in lengths]
    c = [mp.cos(k * value) for value in lengths]
    theta = -3 * s[0] * s[1] * s[2]
    for i, j, ell in ((0, 1, 2), (0, 2, 1), (1, 2, 0)):
        theta += 2 * s[ell] * (
            c[i] * c[j] - mp.cos(phases[i] - phases[j])
        )
    pendant = sum(
        c[i]
        * s[_remaining(range(3), (i,))[0]]
        * s[_remaining(range(3), (i,))[1]]
        for i in range(3)
    )
    return s[3] * theta + c[3] * pendant


def bond_characteristic_numeric(k: mp.mpf) -> mp.mpc:
    lengths = [mp.mpf(1), mp.sqrt(2), mp.sqrt(3), mp.sqrt(5)]
    phases = [mp.mpf(0), mp.pi / 3, 2 * mp.pi / 3, mp.mpf(0)]
    scattering = scattering_matrix()
    matrix = mp.matrix(8, 8)
    for row in range(8):
        for column in range(8):
            edge = column % 4
            phase = phases[edge] if column < 4 else -phases[edge]
            value = scattering[row][column]
            weight = mp.mpf(value.numerator) / mp.mpf(value.denominator)
            matrix[row, column] = (
                (1 if row == column else 0)
                - weight * mp.exp(1j * (k * lengths[edge] + phase))
            )
    return mp.det(matrix)


def _mp_text(value: mp.mpf | mp.mpc, digits: int = 45) -> str:
    if isinstance(value, mp.mpc):
        return f"{mp.nstr(value.real, digits)} + {mp.nstr(value.imag, digits)}i"
    return mp.nstr(value, digits)


def build_report() -> dict:
    mp.mp.dps = MP_DPS
    k = sp.symbols("k")
    F = pole_free_expression(k)
    A = exact_zero_characteristic()
    expected_A = sp.sqrt(2) + sp.sqrt(3) + sp.sqrt(6) + sp.sqrt(5) * (
        1 + sp.sqrt(3) + 3 * sp.sqrt(2)
    )
    if sp.simplify(A - expected_A) != 0:
        raise AssertionError("unexpected exact k=0 characteristic")
    if sp.simplify(F.subs(k, -k) - F) != 0:
        raise AssertionError("pole-free characteristic is not even")
    if sp.simplify(sp.limit(F / k**2, k, 0) - A) != 0:
        raise AssertionError("F/k^2 does not match physical characteristic")
    F_series = sp.series(F, k, 0, 6).removeO().expand()
    physical_quadratic = sp.simplify(F_series.coeff(k, 4))
    normalized_quadratic = sp.simplify(physical_quadratic / A)

    total_length = sum(LENGTHS_SYM)
    leading_bond = sp.simplify(-sp.Rational(4, 3) * A)
    samples = []
    residuals = []
    for sample in SAMPLE_K:
        value = mp.pi if sample == "pi" else mp.mpf(sample)
        physical = physical_characteristic_numeric(value)
        pole_free = pole_free_numeric(value)
        bond = bond_characteristic_numeric(value)
        relation_residual = bond + mp.mpf(4) / 3 * value**2 * mp.exp(
            1j * value * sum([mp.mpf(1), mp.sqrt(2), mp.sqrt(3), mp.sqrt(5)])
        ) * physical
        pole_residual = pole_free - value**2 * physical
        residuals.extend([abs(relation_residual), abs(pole_residual)])
        samples.append(
            {
                "k": sample,
                "physical_characteristic": _mp_text(physical),
                "bond_characteristic": _mp_text(bond),
                "bond_identity_residual": _mp_text(relation_residual),
                "pole_free_vs_sinc_residual": _mp_text(pole_residual),
                "edge_sine_zero_sample": sample == "pi",
            }
        )

    A_mp = mp.mpf(str(sp.N(A, 80)))
    small_k = mp.mpf("1e-6")
    bond_scaled = bond_characteristic_numeric(small_k) / small_k**2
    leading_mp = -mp.mpf(4) / 3 * A_mp
    return {
        "candidate_id": "QG-0001",
        "subaudit_id": "QG-0001-BASE-CHARACTERISTIC-001",
        "parent_source_lock": "configs/source_locks/QG-0001.yaml",
        "source_lock": "configs/source_locks/QG-0001-BASE-CHARACTERISTIC.yaml",
        "target_data_used": {"prime_table": False, "zero_table": False, "fitting": False},
        "physical_characteristic": {
            "matrix_dimension": 6,
            "unknown_order": ["u_L", "u_R", "q_0", "q_1", "q_2", "q_3"],
            "entire": True,
            "even": True,
            "zero_mode": False,
            "zero_mode_reason": "Dirichlet terminal D forces a covariantly constant zero-form to vanish",
            "exact_value_at_zero": str(sp.expand(A)),
            "compact_value_at_zero": str(expected_A),
            "value_at_zero_decimal": _mp_text(A_mp),
            "normalized_characteristic": "chi_0(k)=C_phys(k)/A; chi_0(0)=1",
            "normalized_taylor": "chi_0(k)=1+a2*k^2+O(k^4)",
            "normalized_quadratic_coefficient_exact": str(normalized_quadratic),
            "normalized_quadratic_coefficient_decimal": _mp_text(
                mp.mpf(str(sp.N(normalized_quadratic, 80)))
            ),
        },
        "bond_characteristic": {
            "convention": "Delta_bond(k)=det(I_8-S*P(k))",
            "exact_relation": "Delta_bond(k)=-(4/3)*k^2*exp(i*k*L0)*C_phys(k)",
            "L0": "1 + sqrt(2) + sqrt(3) + sqrt(5)",
            "zero_at_k0_order": 2,
            "zero_is_physical": False,
            "leading_coefficient_exact": str(leading_bond),
            "leading_coefficient_decimal": _mp_text(leading_mp),
            "raw_normalized_factor": "beta(k)=-(3/(4*A*k^2))*Delta_bond(k)=exp(i*k*L0)*chi_0(k)",
            "raw_normalized_taylor": "beta(k)=1+i*L0*k+O(k^2)",
            "first_nonconstant_coefficient_exact": "i*(1 + sqrt(2) + sqrt(3) + sqrt(5))",
            "first_nonconstant_coefficient_decimal": (
                "0 + " + _mp_text(mp.mpf(str(sp.N(total_length, 80)))) + "i"
            ),
            "dephasing_factor": "exp(-i*k*L0)",
            "component_n_dephasing_factor": "exp(-i*k*L0/n)",
            "scaled_small_k_value": _mp_text(bond_scaled),
            "scaled_small_k_error": _mp_text(bond_scaled - leading_mp),
            "division_by_k2_allowed_only_after_identity": True,
        },
        "pole_free_formula": {
            "formula": "F(k)=s3[-3*s0*s1*s2+2*sum_{i<j<3}s_l*(c_i*c_j-cos(alpha_i-alpha_j))]+c3*sum_i c_i*s_j*s_m",
            "relation_to_physical": "F(k)=k^2*C_phys(k)",
            "individual_sine_factors_are_not_independent_zeros": True,
        },
        "sample_checks": samples,
        "max_abs_residual": _mp_text(max(residuals)),
        "exact_parity_check": True,
        "exact_zero_limit_check": True,
        "route_b_invoked": False,
        "structural_conclusion": (
            "The physical n=1 matching characteristic is entire and nonzero at k=0. "
            "The directed-bond determinant has an exact double k=0 zero caused by "
            "the degenerate plane-wave parametrization, with leading coefficient "
            "-(4/3)A. Dividing by k^2 is justified only by the proved identity; "
            "this local repair does not define a tower determinant."
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
