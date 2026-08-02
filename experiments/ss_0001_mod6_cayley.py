#!/usr/bin/env python3
"""Exact Route-A baseline for SS-0001.

The candidate is the constant-roof suspension over the edge shift of
Cay(Z/6Z, {+1, -1}).  It is deliberately parameter-free and does not read
prime or Riemann-zero data.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path
from typing import Iterable


Matrix = list[list[int]]
Polynomial = list[int]


def adjacency_matrix(modulus: int = 6) -> Matrix:
    """Return the directed adjacency matrix for steps +1 and -1 modulo n."""
    return [
        [int((column - row) % modulus in {1, modulus - 1}) for column in range(modulus)]
        for row in range(modulus)
    ]


def identity(size: int) -> Matrix:
    return [[int(row == column) for column in range(size)] for row in range(size)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    return [
        [sum(left[row][k] * right[k][column] for k in range(size)) for column in range(size)]
        for row in range(size)
    ]


def matrix_power(matrix: Matrix, exponent: int) -> Matrix:
    result = identity(len(matrix))
    base = matrix
    power = exponent
    while power:
        if power & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        power >>= 1
    return result


def trace(matrix: Matrix) -> int:
    return sum(matrix[index][index] for index in range(len(matrix)))


def polynomial_multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result = [0] * (len(left) + len(right) - 1)
    for left_degree, left_value in enumerate(left):
        for right_degree, right_value in enumerate(right):
            result[left_degree + right_degree] += left_value * right_value
    return result


def permutation_sign(permutation: Iterable[int]) -> int:
    values = list(permutation)
    inversions = sum(
        values[left] > values[right]
        for left in range(len(values))
        for right in range(left + 1, len(values))
    )
    return -1 if inversions % 2 else 1


def determinant_polynomial(matrix: Matrix) -> Polynomial:
    """Return coefficients of det(I-zA) in increasing powers of z."""
    size = len(matrix)
    result = [0] * (size + 1)
    for permutation in itertools.permutations(range(size)):
        term = [1]
        for row, column in enumerate(permutation):
            term = polynomial_multiply(term, [int(row == column), -matrix[row][column]])
        sign = permutation_sign(permutation)
        for degree, coefficient in enumerate(term):
            result[degree] += sign * coefficient
    return result


def divisors(number: int) -> list[int]:
    return [divisor for divisor in range(1, number + 1) if number % divisor == 0]


def mobius(number: int) -> int:
    prime_factors = 0
    remaining = number
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            prime_factors += 1
            if remaining % prime == 0:
                return 0
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        prime_factors += 1
    return -1 if prime_factors % 2 else 1


def primitive_orbit_census(matrix: Matrix, max_period: int) -> list[dict[str, int]]:
    traces = {period: trace(matrix_power(matrix, period)) for period in range(1, max_period + 1)}
    census = []
    for period in range(1, max_period + 1):
        primitive_points = sum(
            mobius(divisor) * traces[period // divisor] for divisor in divisors(period)
        )
        if primitive_points % period:
            raise ArithmeticError(f"primitive point count is not divisible by period {period}")
        census.append(
            {
                "period": period,
                "closed_walks": traces[period],
                "primitive_points": primitive_points,
                "primitive_orbits": primitive_points // period,
            }
        )
    return census


def candidate_zero_count(height: float) -> int:
    """Count zeros of det(I-exp(-s)A) with |Im(s)| <= height, multiplicity included."""
    positive_sequence = 2 * math.floor(height / (2 * math.pi)) + 1
    odd_bound = math.floor(height / math.pi)
    negative_sequence = 2 * ((odd_bound + 1) // 2)
    # Eigenvalues: 2 (x1), 1 (x2), -1 (x2), -2 (x1).
    return 3 * positive_sequence + 3 * negative_sequence


def riemann_von_mangoldt_main(height: float) -> float:
    scaled = height / (2 * math.pi)
    return scaled * math.log(scaled) - scaled + 7 / 8


def build_report(max_period: int = 24) -> dict[str, object]:
    matrix = adjacency_matrix()
    determinant = determinant_polynomial(matrix)
    expected_determinant = [1, 0, -6, 0, 9, 0, -4]
    if determinant != expected_determinant:
        raise AssertionError((determinant, expected_determinant))

    census = primitive_orbit_census(matrix, max_period)
    windows = {
        "training_1_8": census[:8],
        "validation_9_16": census[8:16],
        "test_17_24": census[16:24],
    }
    heights = [100.0, 10_000.0, 1_000_000.0]
    zero_counts = [
        {
            "height": height,
            "candidate_count": candidate_zero_count(height),
            "riemann_von_mangoldt_main": riemann_von_mangoldt_main(height),
            "candidate_over_T_log_T": candidate_zero_count(height) / (height * math.log(height)),
        }
        for height in heights
    ]

    return {
        "candidate_id": "SS-0001",
        "clue_id": "CLUE-A1-002",
        "graph": "Cay(Z/6Z,{+1,-1})",
        "adjacency": matrix,
        "vertex_out_degrees": [sum(row) for row in matrix],
        "determinant_convention": "D(s)=det(I-exp(-s)A)",
        "determinant_in_z": {
            "coefficients_increasing_degree": determinant,
            "factorization": "(1-4*z^2)*(1-z^2)^2",
        },
        "adjacency_spectrum_with_multiplicity": {"2": 1, "1": 2, "-1": 2, "-2": 1},
        "mod3_character_modes_present": True,
        "orbit_census": windows,
        "zero_real_parts": [0.0, math.log(2.0)],
        "zero_count_diagnostics": zero_counts,
        "structural_conclusion": (
            "The mod-6 lift contains nontrivial mod-3 character modes, but its constant integer clock "
            "and finite-state determinant yield only finitely many vertical arithmetic progressions of zeros "
            "with O(T) counting, not a log-prime orbit clock or Riemann-von Mangoldt O(T log T) growth."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-period", type=int, default=24)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    report = build_report(arguments.max_period)
    payload = json.dumps(report, indent=2, sort_keys=True)
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(payload + "\n", encoding="utf-8")
    print(payload)


if __name__ == "__main__":
    main()
