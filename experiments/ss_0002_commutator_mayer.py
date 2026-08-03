#!/usr/bin/env python3
"""Structural Route-A audit for SS-0002.

SS-0002 is the paired-Gauss Mayer transfer operator with regular C6 holonomy
for the commutator cover of the modular surface.  This diagnostic uses no
prime table and no Riemann-zero table.  Exact integer checks establish the
branch/cocycle ledger; floating-point values only illustrate already-known
convergence and counting exponents.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


Matrix2 = tuple[tuple[int, int], tuple[int, int]]

MODULUS = 6
S: Matrix2 = ((0, -1), (1, 0))
T: Matrix2 = ((1, 1), (0, 1))


def matmul(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def t_power(exponent: int) -> Matrix2:
    return ((1, exponent), (0, 1))


def projective_normalize(matrix: Matrix2) -> Matrix2:
    entries = matrix[0] + matrix[1]
    first_nonzero = next(value for value in entries if value)
    if first_nonzero > 0:
        return matrix
    return tuple(tuple(-value for value in row) for row in matrix)  # type: ignore[return-value]


def branch_matrix(a: int, b: int) -> Matrix2:
    if a < 1 or b < 1:
        raise ValueError("paired Gauss digits must be positive")
    return ((1, a), (b, a * b + 1))


def branch_matrix_from_generators(a: int, b: int) -> Matrix2:
    product = matmul(matmul(matmul(S, t_power(-b)), S), t_power(a))
    return projective_normalize(product)


def determinant(matrix: Matrix2) -> int:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def abelianization_cocycle(a: int, b: int) -> int:
    """Return alpha(S T^-b S T^a)=a-b in C6."""
    return (a - b) % MODULUS


def inverse_branch(z: complex, a: int, b: int) -> complex:
    return (z + a) / (b * (z + a) + 1)


def inverse_branch_derivative(z: complex, a: int, b: int) -> complex:
    return 1 / (b * (z + a) + 1) ** 2


def regular_representation_trace(cocycle: int) -> int:
    return MODULUS if cocycle % MODULUS == 0 else 0


def holonomy_order(cocycle: int) -> int:
    return MODULUS // math.gcd(cocycle % MODULUS, MODULUS)


def lifted_primitive_count(cocycle: int) -> int:
    """Number of primitive lifts after multiplying length by holonomy order."""
    return MODULUS // holonomy_order(cocycle)


def character_order(mode: int) -> int:
    return MODULUS // math.gcd(mode % MODULUS, MODULUS)


def validate_branch_square(start: int, stop: int) -> dict[str, int]:
    checked = 0
    for a in range(start, stop + 1):
        for b in range(start, stop + 1):
            matrix = branch_matrix(a, b)
            if matrix != branch_matrix_from_generators(a, b):
                raise AssertionError((a, b, matrix, branch_matrix_from_generators(a, b)))
            if determinant(matrix) != 1:
                raise AssertionError((a, b, determinant(matrix)))
            alpha_from_word = (3 - b + 3 + a) % MODULUS
            if abelianization_cocycle(a, b) != alpha_from_word:
                raise AssertionError((a, b, abelianization_cocycle(a, b), alpha_from_word))
            z = complex(0.75, 0.125)
            denominator = b * (z + a) + 1
            if denominator.real <= 0:
                raise AssertionError((a, b, denominator))
            if inverse_branch_derivative(z, a, b) != denominator ** -2:
                raise AssertionError((a, b))
            checked += 1
    return {"digit_start": start, "digit_stop": stop, "branch_pairs_checked": checked}


def branch_tail_partial_sum(sigma: float, cutoff: int, z: float = 1.0) -> float:
    return sum(
        (b * (z + a) + 1) ** (-2 * sigma)
        for a in range(1, cutoff + 1)
        for b in range(1, cutoff + 1)
    )


def branch_tail_diagnostics() -> list[dict[str, object]]:
    cutoffs = [8, 16, 32, 64, 128]
    diagnostics = []
    for sigma in (0.75, 1.0, 1.25):
        partial_sums = [branch_tail_partial_sum(sigma, cutoff) for cutoff in cutoffs]
        block_increments = [
            partial_sums[index] - partial_sums[index - 1]
            for index in range(1, len(partial_sums))
        ]
        diagnostics.append(
            {
                "sigma": sigma,
                "cutoffs": cutoffs,
                "partial_sums_at_z_1": partial_sums,
                "successive_block_increments": block_increments,
                "increments_strictly_decrease": all(
                    later < earlier
                    for earlier, later in zip(block_increments, block_increments[1:])
                ),
            }
        )
    return diagnostics


def riemann_von_mangoldt_main(height: float) -> float:
    scaled = height / (2 * math.pi)
    return scaled * math.log(scaled) - scaled + 7 / 8


def modular_cusp_lift_weyl_main(height: float) -> float:
    """Positive-height T^2/12 main term inherited from the modular surface."""
    return height * height / 12


def cover_resonance_weyl_two_sided_main(height: float) -> float:
    """Area/(2*pi) T^2 with area 2*pi for the six-sheeted cover."""
    return height * height


def counting_diagnostics() -> list[dict[str, float]]:
    rows = []
    for height in (100.0, 1_000.0, 10_000.0, 1_000_000.0):
        xi_main = riemann_von_mangoldt_main(height)
        lifted_main = modular_cusp_lift_weyl_main(height)
        rows.append(
            {
                "height": height,
                "xi_positive_main": xi_main,
                "modular_cusp_lift_positive_weyl_main": lifted_main,
                "cover_resonance_two_sided_weyl_main": cover_resonance_weyl_two_sided_main(height),
                "lifted_quadratic_over_xi_main": lifted_main / xi_main,
                "lifted_quadratic_over_T_log_T": lifted_main / (height * math.log(height)),
            }
        )
    return rows


def build_report() -> dict[str, object]:
    validation = validate_branch_square(1, 8)
    sealed_test = validate_branch_square(9, 16)

    if (2 * 3) % MODULUS != 0:
        raise AssertionError("S^2 relation failed in the abelianization")
    if (3 * (3 + 1)) % MODULUS != 0:
        raise AssertionError("(ST)^3 relation failed in the abelianization")

    holonomy = [
        {
            "cocycle": cocycle,
            "order": holonomy_order(cocycle),
            "primitive_lifts": lifted_primitive_count(cocycle),
            "length_multiplier": holonomy_order(cocycle),
            "regular_trace_before_closure": regular_representation_trace(cocycle),
        }
        for cocycle in range(MODULUS)
    ]
    characters = [
        {"mode": mode, "character_order": character_order(mode)}
        for mode in range(MODULUS)
    ]

    return {
        "candidate_id": "SS-0002",
        "clue_id": "CLUE-A1-002",
        "uses_prime_table": False,
        "uses_zero_table": False,
        "group": {
            "ambient": "PSL(2,Z)",
            "abelianization": "C6",
            "alpha_S": 3,
            "alpha_T": 1,
            "cover_group": "commutator subgroup ker(alpha)",
            "index": 6,
        },
        "cover_geometry": {
            "curvature": -1,
            "base_area": math.pi / 3,
            "cover_area": 2 * math.pi,
            "cusps": 1,
            "cusp_width": 6,
            "elliptic_points": 0,
            "genus": 1,
            "topology": "once-punctured torus",
        },
        "paired_branch": {
            "map": "phi_ab(z)=(z+a)/(b(z+a)+1)",
            "matrix": "[[1,a],[b,ab+1]]=S*T^(-b)*S*T^a",
            "derivative": "phi_ab'(z)=[b(z+a)+1]^(-2)",
            "cocycle": "a-b mod 6",
            "fibre_update": "r -> r-(a-b) mod 6",
            "validation": validation,
            "sealed_test": sealed_test,
        },
        "holonomy_lift_ledger": holonomy,
        "character_modes": characters,
        "nontrivial_mod3_character_modes": [2, 4],
        "clock": "periodic sum of log|H'| = 2 log(lambda_gamma) = geodesic length",
        "banach_space": "A(D_3/2) tensor C^6",
        "nuclearity_domain": "Re(s)>1/2",
        "determinant_ledger": {
            "frozen": "D_ab(s)=det_Fr(I-M_s)=Z_Gamma_com(s)",
            "initial_identity_domain": "Re(s)>1",
            "separate_objects": [
                "1/D_ab",
                "D_ab'/D_ab",
                "modular scattering determinant",
                "completed xi",
            ],
        },
        "branch_tail_diagnostics": branch_tail_diagnostics(),
        "counting_diagnostics": counting_diagnostics(),
        "structural_conclusion": (
            "The countable-branch, infinite-dimensional nuclear operator genuinely escapes OBR-005. "
            "Its same-object Fredholm determinant is nevertheless the finite-area cover Selberg zeta, "
            "whose spectral/resonance divisor has a quadratic Weyl scale rather than the completed-xi "
            "T log T scale. The modular scattering determinant is a separate ledger and is not used."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    report = build_report()
    payload = json.dumps(report, indent=2, sort_keys=True)
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(payload + "\n", encoding="utf-8")
    print(payload)


if __name__ == "__main__":
    main()
