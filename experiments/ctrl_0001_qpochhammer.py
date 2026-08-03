#!/usr/bin/env python3
"""Route-A A2 positive control for a four-channel Fredholm determinant.

The frozen object is a diagonal trace-class family

    L_s e_(c,n) = a_c q_c^n exp(-s) e_(c,n),

so D(s)=det_Fr(I-L_s) is a four-channel q-Pochhammer product.  This is
synthetic evaluation infrastructure, not an RH candidate.  It reads neither
prime tables nor Riemann-zero tables.

Root discovery uses Fredholm coefficients in z=exp(-s).  Exact synthetic
roots are generated only afterward for scoring.  Argument-principle counts
use the independent direct mode product, never the polynomial roots.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
import math
from pathlib import Path
from typing import Callable, Sequence

import mpmath as mp
import numpy as np
from scipy.optimize import linear_sum_assignment


CONTROL_ID = "CTRL-0001"
AUDIT_ID = "CTRL-A2-QPOCH-001"
CLUE_ID = "CLUE-A2-001"
SOURCE_LOCK_PATH = "configs/source_locks/CTRL-0001.yaml"
REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SOURCE_LOCK_FILE = REPOSITORY_ROOT / SOURCE_LOCK_PATH

REAL_MIN = -8 / 25
REAL_MAX = 17 / 25
IMAG_MIN = -34 / 5
IMAG_MAX = 34 / 5
CORE_IMAG = 17 / 5

MODE_CUTOFFS = (2, 3, 8, 16, 24, 32, 40, 48)
COEFFICIENT_CUTOFFS = (16, 20, 24, 28, 32)
PRIMARY_MODE_CUTOFF = 48
PRIMARY_COEFFICIENT_CUTOFF = 28
COEFFICIENT_GUARD = 32
CONTOUR_POINTS_PER_EDGE = (128, 256, 512, 1024)

MATCH_RADIUS = 1.0e-4
PHASE_STEP_MAX = math.pi / 3
WINDING_RESIDUAL_MAX = 1.0e-8


@dataclass(frozen=True)
class Channel:
    name: str
    alpha: float
    beta: float
    theta: float

    @property
    def a(self) -> complex:
        return complex(np.exp(self.alpha + 1j * self.theta))

    @property
    def q(self) -> float:
        return math.exp(-self.beta)


CHANNELS = (
    Channel("A_plus", 11 / 20, 2 / 5, math.pi / 3),
    Channel("A_minus", 11 / 20, 2 / 5, -math.pi / 3),
    Channel("B", 9 / 20, 1 / 2, math.pi),
    Channel("C", 3 / 10, 9 / 20, 0.0),
)
CHANNEL_BY_NAME = {channel.name: channel for channel in CHANNELS}

Bounds = tuple[float, float, float, float]
DEFAULT_BOUNDS: Bounds = (REAL_MIN, REAL_MAX, IMAG_MIN, IMAG_MAX)
CORE_BOUNDS: Bounds = (REAL_MIN, REAL_MAX, -CORE_IMAG, CORE_IMAG)
UPPER_BOUNDS: Bounds = (REAL_MIN, REAL_MAX, CORE_IMAG, IMAG_MAX)
LOWER_BOUNDS: Bounds = (REAL_MIN, REAL_MAX, IMAG_MIN, -CORE_IMAG)

MISSING_MODES = frozenset({("A_plus", 1), ("A_minus", 1)})
EXTRA_WEIGHTS = (
    complex(np.exp(1 / 20 + 0.5j * math.pi)),
    complex(np.exp(1 / 20 - 0.5j * math.pi)),
)


def complex_record(value: complex) -> dict[str, float]:
    return {"real": float(value.real), "imag": float(value.imag)}


def root_records(values: Sequence[complex]) -> list[dict[str, float]]:
    return [complex_record(complex(value)) for value in values]


def source_lock_sha256() -> str:
    return hashlib.sha256(SOURCE_LOCK_FILE.read_bytes()).hexdigest()


def mode_weight(channel: Channel, mode: int, absolute_weights: bool = False) -> complex:
    if mode < 0:
        raise ValueError("mode must be nonnegative")
    a = abs(channel.a) if absolute_weights else channel.a
    return complex(a * channel.q**mode)


def direct_determinant(
    s: complex | np.ndarray,
    mode_cutoff: int,
    *,
    omitted_modes: frozenset[tuple[str, int]] = frozenset(),
    extra_weights: Sequence[complex] = (),
    absolute_weights: bool = False,
) -> complex | np.ndarray:
    """Evaluate the frozen finite-mode product D_N(s)."""

    if mode_cutoff < 1:
        raise ValueError("mode_cutoff must be positive")
    scalar_input = np.ndim(s) == 0
    values = np.asarray(s, dtype=np.complex128)
    z = np.exp(-values)
    result = np.ones_like(values, dtype=np.complex128)
    for channel in CHANNELS:
        for mode in range(mode_cutoff):
            if (channel.name, mode) in omitted_modes:
                continue
            result *= 1 - mode_weight(channel, mode, absolute_weights) * z
    for weight in extra_weights:
        result *= 1 - weight * z
    if scalar_input:
        return complex(result)
    return result


def channel_coefficients(
    channel: Channel,
    cutoff: int,
    *,
    absolute_weights: bool = False,
) -> np.ndarray:
    """q-binomial coefficients of product_n>=0 (1-a q^n z)."""

    coefficients = np.ones(cutoff + 1, dtype=np.complex128)
    a = abs(channel.a) if absolute_weights else channel.a
    q = channel.q
    for degree in range(1, cutoff + 1):
        coefficients[degree] = (
            coefficients[degree - 1]
            * (-a * q ** (degree - 1))
            / (1 - q**degree)
        )
    return coefficients


def delete_linear_factor(coefficients: np.ndarray, weight: complex) -> np.ndarray:
    """Return coefficients of B(z)/(1-weight*z), truncated to the same order."""

    quotient = np.empty_like(coefficients)
    quotient[0] = coefficients[0]
    for degree in range(1, len(coefficients)):
        quotient[degree] = coefficients[degree] + weight * quotient[degree - 1]
    return quotient


def fredholm_coefficients(
    cutoff: int,
    *,
    omitted_modes: frozenset[tuple[str, int]] = frozenset(),
    extra_weights: Sequence[complex] = (),
    absolute_weights: bool = False,
) -> np.ndarray:
    """Construct D(z)=sum_m d_m z^m by channel convolution."""

    total = np.array([1.0 + 0.0j], dtype=np.complex128)
    for channel in CHANNELS:
        channel_series = channel_coefficients(
            channel, cutoff, absolute_weights=absolute_weights
        )
        omitted_for_channel = sorted(
            mode for name, mode in omitted_modes if name == channel.name
        )
        for mode in omitted_for_channel:
            channel_series = delete_linear_factor(
                channel_series,
                mode_weight(channel, mode, absolute_weights),
            )
        total = np.convolve(total, channel_series)[: cutoff + 1]
    for weight in extra_weights:
        total = np.convolve(total, np.array([1.0, -weight]))[: cutoff + 1]
    return np.asarray(total, dtype=np.complex128)


def power_trace(repetition: int) -> complex:
    """Return p_r=Tr(W^r)=sum_c a_c^r/(1-q_c^r)."""

    if repetition < 1:
        raise ValueError("repetition must be positive")
    return sum(
        channel.a**repetition / (1 - channel.q**repetition)
        for channel in CHANNELS
    )


def trace_recurrence_coefficients(cutoff: int) -> np.ndarray:
    """Independent Newton/Fredholm recurrence for the nominal coefficients."""

    coefficients = np.zeros(cutoff + 1, dtype=np.complex128)
    coefficients[0] = 1.0
    traces = np.array(
        [0.0j] + [power_trace(repetition) for repetition in range(1, cutoff + 1)],
        dtype=np.complex128,
    )
    for degree in range(1, cutoff + 1):
        convolution = sum(
            traces[repetition] * coefficients[degree - repetition]
            for repetition in range(1, degree + 1)
        )
        coefficients[degree] = -convolution / degree
    return coefficients


def direct_logarithmic_derivative(
    s: complex | np.ndarray,
    mode_cutoff: int,
) -> complex | np.ndarray:
    """Evaluate D_N'(s)/D_N(s) as a distinct meromorphic ledger."""

    scalar_input = np.ndim(s) == 0
    values = np.asarray(s, dtype=np.complex128)
    z = np.exp(-values)
    result = np.zeros_like(values, dtype=np.complex128)
    for channel in CHANNELS:
        for mode in range(mode_cutoff):
            weighted_z = mode_weight(channel, mode) * z
            result += weighted_z / (1 - weighted_z)
    if scalar_input:
        return complex(result)
    return result


def truncated_log_exponential(
    s: complex | np.ndarray,
    max_repetition: int = 4,
) -> complex | np.ndarray:
    """Exponentiate a finite log-D expansion; this object is zero-free."""

    if max_repetition < 1:
        raise ValueError("max_repetition must be positive")
    scalar_input = np.ndim(s) == 0
    values = np.asarray(s, dtype=np.complex128)
    z = np.exp(-values)
    exponent = np.zeros_like(values, dtype=np.complex128)
    for repetition in range(1, max_repetition + 1):
        exponent -= power_trace(repetition) * z**repetition / repetition
    result = np.exp(exponent)
    if scalar_input:
        return complex(result)
    return result


def normalized_polynomial_residual(coefficients: np.ndarray, z: complex) -> float:
    powers = z ** np.arange(len(coefficients))
    terms = coefficients * powers
    denominator = float(np.sum(np.abs(terms)))
    if denominator == 0:
        return math.inf
    return float(abs(np.sum(terms)) / denominator)


def roots_from_coefficients(
    coefficients: np.ndarray,
    bounds: Bounds = DEFAULT_BOUNDS,
) -> dict[str, object]:
    """Discover roots in s through polynomial roots in z=exp(-s)."""

    real_min, real_max, imag_min, imag_max = bounds
    z_roots = np.polynomial.polynomial.polyroots(coefficients)
    discovered: list[complex] = []
    for z_root in z_roots:
        if z_root == 0:
            continue
        base = -np.log(z_root)
        branch_min = math.ceil((imag_min - base.imag) / (2 * math.pi))
        branch_max = math.floor((imag_max - base.imag) / (2 * math.pi))
        for branch in range(branch_min, branch_max + 1):
            root = complex(base + 2j * math.pi * branch)
            if real_min < root.real < real_max and imag_min < root.imag < imag_max:
                discovered.append(root)
    discovered.sort(key=lambda value: (value.imag, value.real))
    residuals = [
        normalized_polynomial_residual(coefficients, complex(root))
        for root in z_roots
    ]
    return {
        "z_roots": np.asarray(z_roots, dtype=np.complex128),
        "s_roots": np.asarray(discovered, dtype=np.complex128),
        "max_normalized_polynomial_residual": max(residuals, default=0.0),
    }


def exact_scoring_ledger(
    bounds: Bounds = DEFAULT_BOUNDS,
) -> list[dict[str, object]]:
    """Generate exact synthetic roots for scoring, never for discovery."""

    real_min, real_max, imag_min, imag_max = bounds
    ledger: list[dict[str, object]] = []
    for channel in CHANNELS:
        mode = 0
        while channel.alpha - mode * channel.beta > real_min:
            real_part = channel.alpha - mode * channel.beta
            if real_part < real_max:
                branch_min = math.ceil((imag_min - channel.theta) / (2 * math.pi))
                branch_max = math.floor((imag_max - channel.theta) / (2 * math.pi))
                for branch in range(branch_min, branch_max + 1):
                    imaginary_part = channel.theta + 2 * math.pi * branch
                    if imag_min < imaginary_part < imag_max:
                        ledger.append(
                            {
                                "channel": channel.name,
                                "mode": mode,
                                "branch": branch,
                                "root": complex(real_part, imaginary_part),
                            }
                        )
            mode += 1
    ledger.sort(key=lambda row: (complex(row["root"]).imag, complex(row["root"]).real))
    return ledger


def root_region_counts(roots: Sequence[complex]) -> dict[str, int]:
    return {
        "total": int(len(roots)),
        "validation_core": int(
            sum(abs(complex(root).imag) < CORE_IMAG for root in roots)
        ),
        "test_upper": int(
            sum(CORE_IMAG < complex(root).imag < IMAG_MAX for root in roots)
        ),
        "test_lower": int(
            sum(IMAG_MIN < complex(root).imag < -CORE_IMAG for root in roots)
        ),
    }


def roots_in_bounds(roots: Sequence[complex], bounds: Bounds) -> np.ndarray:
    real_min, real_max, imag_min, imag_max = bounds
    return np.asarray(
        [
            complex(root)
            for root in roots
            if real_min < complex(root).real < real_max
            and imag_min < complex(root).imag < imag_max
        ],
        dtype=np.complex128,
    )


def match_roots(
    found: Sequence[complex],
    expected: Sequence[complex],
    radius: float = MATCH_RADIUS,
) -> dict[str, object]:
    """Maximum-cardinality one-to-one matching with explicit dummies."""

    found_array = np.asarray(found, dtype=np.complex128)
    expected_array = np.asarray(expected, dtype=np.complex128)
    found_count = len(found_array)
    expected_count = len(expected_array)
    if found_count == 0 or expected_count == 0:
        return {
            "matched_count": 0,
            "missing_count": expected_count,
            "extra_count": found_count,
            "max_match_error": None,
            "missing_roots": root_records(expected_array),
            "extra_roots": root_records(found_array),
            "matches": [],
        }

    distances = np.abs(found_array[:, None] - expected_array[None, :])
    size = found_count + expected_count
    forbidden_cost = 1.0e6
    unmatched_cost = 2.0
    costs = np.full((size, size), forbidden_cost, dtype=float)
    costs[:found_count, :expected_count] = np.where(
        distances <= radius, distances / radius, forbidden_cost
    )
    for index in range(found_count):
        costs[index, expected_count + index] = unmatched_cost
    for index in range(expected_count):
        costs[found_count + index, index] = unmatched_cost
    costs[found_count:, expected_count:] = 0.0

    row_indices, column_indices = linear_sum_assignment(costs)
    matches: list[dict[str, object]] = []
    matched_found: set[int] = set()
    matched_expected: set[int] = set()
    for row, column in zip(row_indices, column_indices):
        if row < found_count and column < expected_count:
            distance = float(distances[row, column])
            if distance <= radius:
                matched_found.add(int(row))
                matched_expected.add(int(column))
                matches.append(
                    {
                        "found": complex_record(complex(found_array[row])),
                        "expected": complex_record(complex(expected_array[column])),
                        "error": distance,
                    }
                )
    errors = [float(row["error"]) for row in matches]
    missing = [
        complex(expected_array[index])
        for index in range(expected_count)
        if index not in matched_expected
    ]
    extra = [
        complex(found_array[index])
        for index in range(found_count)
        if index not in matched_found
    ]
    return {
        "matched_count": len(matches),
        "missing_count": len(missing),
        "extra_count": len(extra),
        "max_match_error": max(errors, default=None),
        "missing_roots": root_records(missing),
        "extra_roots": root_records(extra),
        "matches": matches,
    }


def max_assignment_drift(left: Sequence[complex], right: Sequence[complex]) -> float:
    left_array = np.asarray(left, dtype=np.complex128)
    right_array = np.asarray(right, dtype=np.complex128)
    if len(left_array) != len(right_array) or len(left_array) == 0:
        return math.inf
    distances = np.abs(left_array[:, None] - right_array[None, :])
    rows, columns = linear_sum_assignment(distances)
    return float(np.max(distances[rows, columns]))


def max_rectangular_assignment_error(
    found: Sequence[complex], expected: Sequence[complex]
) -> float:
    """Best global assignment error, even when it exceeds the match radius."""

    found_array = np.asarray(found, dtype=np.complex128)
    expected_array = np.asarray(expected, dtype=np.complex128)
    if len(found_array) == 0 or len(expected_array) == 0:
        return math.inf
    distances = np.abs(found_array[:, None] - expected_array[None, :])
    rows, columns = linear_sum_assignment(distances)
    return float(np.max(distances[rows, columns]))


def high_precision_coefficients(cutoff: int, decimal_digits: int) -> list[mp.mpc]:
    """Independent arbitrary-precision q-binomial convolution."""

    with mp.workdps(decimal_digits):
        channel_parameters = (
            (mp.mpf(11) / 20, mp.mpf(2) / 5, mp.pi / 3),
            (mp.mpf(11) / 20, mp.mpf(2) / 5, -mp.pi / 3),
            (mp.mpf(9) / 20, mp.mpf(1) / 2, mp.pi),
            (mp.mpf(3) / 10, mp.mpf(9) / 20, mp.mpf(0)),
        )
        total = [mp.mpc(1)]
        for alpha, beta, theta in channel_parameters:
            a = mp.exp(alpha + 1j * theta)
            q = mp.exp(-beta)
            channel_series = [mp.mpc(1)]
            for degree in range(1, cutoff + 1):
                channel_series.append(
                    channel_series[-1]
                    * (-a * q ** (degree - 1))
                    / (1 - q**degree)
                )
            convolution = [
                mp.mpc(0)
                for _ in range(min(cutoff + 1, len(total) + len(channel_series) - 1))
            ]
            for left_degree, left_value in enumerate(total):
                for right_degree, right_value in enumerate(channel_series):
                    degree = left_degree + right_degree
                    if degree <= cutoff:
                        convolution[degree] += left_value * right_value
            total = convolution
        return total


def high_precision_roots(cutoff: int, decimal_digits: int) -> list[mp.mpc]:
    """Discover the same s-roots with arbitrary-precision polynomial roots."""

    with mp.workdps(decimal_digits):
        coefficients = high_precision_coefficients(cutoff, decimal_digits)
        z_roots = mp.polyroots(
            list(reversed(coefficients)),
            maxsteps=1000,
            extraprec=100,
            error=False,
        )
        real_min = -mp.mpf(8) / 25
        real_max = mp.mpf(17) / 25
        imag_min = -mp.mpf(34) / 5
        imag_max = mp.mpf(34) / 5
        discovered: list[mp.mpc] = []
        for z_root in z_roots:
            base = -mp.log(z_root)
            branch_min = int(mp.ceil((imag_min - base.imag) / (2 * mp.pi)))
            branch_max = int(mp.floor((imag_max - base.imag) / (2 * mp.pi)))
            for branch in range(branch_min, branch_max + 1):
                root = base + 2j * mp.pi * branch
                if real_min < root.real < real_max and imag_min < root.imag < imag_max:
                    discovered.append(root)
        discovered.sort(key=lambda value: (float(value.imag), float(value.real)))
        return discovered


def high_precision_truth(decimal_digits: int) -> list[mp.mpc]:
    with mp.workdps(decimal_digits):
        channel_parameters = (
            (mp.mpf(11) / 20, mp.mpf(2) / 5, mp.pi / 3),
            (mp.mpf(11) / 20, mp.mpf(2) / 5, -mp.pi / 3),
            (mp.mpf(9) / 20, mp.mpf(1) / 2, mp.pi),
            (mp.mpf(3) / 10, mp.mpf(9) / 20, mp.mpf(0)),
        )
        real_min = -mp.mpf(8) / 25
        real_max = mp.mpf(17) / 25
        imag_min = -mp.mpf(34) / 5
        imag_max = mp.mpf(34) / 5
        roots: list[mp.mpc] = []
        for alpha, beta, theta in channel_parameters:
            mode = 0
            while alpha - mode * beta > real_min:
                real_part = alpha - mode * beta
                if real_part < real_max:
                    branch_min = int(mp.ceil((imag_min - theta) / (2 * mp.pi)))
                    branch_max = int(mp.floor((imag_max - theta) / (2 * mp.pi)))
                    for branch in range(branch_min, branch_max + 1):
                        imaginary_part = theta + 2 * mp.pi * branch
                        if imag_min < imaginary_part < imag_max:
                            roots.append(mp.mpc(real_part, imaginary_part))
                mode += 1
        roots.sort(key=lambda value: (float(value.imag), float(value.real)))
        return roots


def high_precision_assignment_drift(
    left: Sequence[mp.mpc], right: Sequence[mp.mpc], working_digits: int
) -> mp.mpf:
    if len(left) != len(right) or not left:
        return mp.inf
    distances = np.abs(
        np.asarray([complex(value) for value in left])[:, None]
        - np.asarray([complex(value) for value in right])[None, :]
    )
    rows, columns = linear_sum_assignment(distances)
    with mp.workdps(working_digits):
        return max(abs(left[row] - right[column]) for row, column in zip(rows, columns))


def precision_drift_diagnostic() -> dict[str, object]:
    """Supplemental precision audit; it never changes the frozen primary gates."""

    decimal_digits = (50, 80, 120)
    roots_by_precision = {
        digits: high_precision_roots(PRIMARY_COEFFICIENT_CUTOFF, digits)
        for digits in decimal_digits
    }
    drift_50_to_80 = high_precision_assignment_drift(
        roots_by_precision[50], roots_by_precision[80], 130
    )
    drift_80_to_120 = high_precision_assignment_drift(
        roots_by_precision[80], roots_by_precision[120], 130
    )
    high_truth = high_precision_truth(120)
    high_error_to_truth = high_precision_assignment_drift(
        roots_by_precision[120], high_truth, 130
    )
    complex128_roots = roots_from_coefficients(
        fredholm_coefficients(PRIMARY_COEFFICIENT_CUTOFF)
    )["s_roots"]
    high_120_complex = np.asarray(
        [complex(value) for value in roots_by_precision[120]], dtype=np.complex128
    )
    complex128_to_120 = max_assignment_drift(complex128_roots, high_120_complex)
    return {
        "role": "supplemental observational audit; not used to retune the frozen complex128 gates",
        "coefficient_cutoff": PRIMARY_COEFFICIENT_CUTOFF,
        "decimal_digits": list(decimal_digits),
        "root_counts": {
            str(digits): len(roots_by_precision[digits]) for digits in decimal_digits
        },
        "max_root_drift_dps50_to_dps80": mp.nstr(drift_50_to_80, 16),
        "max_root_drift_dps80_to_dps120": mp.nstr(drift_80_to_120, 16),
        "max_root_drift_complex128_to_dps120": complex128_to_120,
        "dps120_k28_max_error_to_exact_scoring_ledger": mp.nstr(
            high_error_to_truth, 16
        ),
    }


def rectangle_contour(bounds: Bounds, points_per_edge: int) -> np.ndarray:
    if points_per_edge < 2:
        raise ValueError("points_per_edge must be at least two")
    real_min, real_max, imag_min, imag_max = bounds
    return np.concatenate(
        (
            np.linspace(real_min, real_max, points_per_edge, endpoint=False)
            + 1j * imag_min,
            np.full(points_per_edge, real_max)
            + 1j * np.linspace(imag_min, imag_max, points_per_edge, endpoint=False),
            np.linspace(real_max, real_min, points_per_edge, endpoint=False)
            + 1j * imag_max,
            np.full(points_per_edge, real_min)
            + 1j * np.linspace(imag_max, imag_min, points_per_edge, endpoint=False),
        )
    ).astype(np.complex128)


def winding_diagnostic(
    determinant: Callable[[np.ndarray], np.ndarray],
    bounds: Bounds,
    points_per_edge: int,
) -> dict[str, object]:
    contour = rectangle_contour(bounds, points_per_edge)
    values = np.asarray(determinant(contour), dtype=np.complex128)
    if np.any(values == 0):
        raise ArithmeticError("the determinant vanished on the contour")
    closed = np.concatenate((values, values[:1]))
    phase_increments = np.angle(closed[1:] / closed[:-1])
    raw_winding = float(np.sum(phase_increments) / (2 * math.pi))
    integer_count = int(round(raw_winding))
    return {
        "points_per_edge": points_per_edge,
        "raw_winding": raw_winding,
        "count": integer_count,
        "integer_residual": abs(raw_winding - integer_count),
        "max_adjacent_phase_increment": float(np.max(np.abs(phase_increments))),
        "minimum_boundary_modulus": float(np.min(np.abs(values))),
    }


def log_derivative_contour_integral(
    bounds: Bounds,
    points_per_edge: int,
    mode_cutoff: int = PRIMARY_MODE_CUTOFF,
) -> dict[str, object]:
    contour = rectangle_contour(bounds, points_per_edge)
    closed_contour = np.concatenate((contour, contour[:1]))
    values = np.asarray(
        direct_logarithmic_derivative(closed_contour, mode_cutoff),
        dtype=np.complex128,
    )
    integral = np.sum(
        0.5
        * (values[:-1] + values[1:])
        * (closed_contour[1:] - closed_contour[:-1])
    ) / (2j * math.pi)
    nearest_integer = int(round(float(integral.real)))
    return {
        "points_per_edge": points_per_edge,
        "integral_over_2pi_i": complex_record(complex(integral)),
        "nearest_integer": nearest_integer,
        "distance_to_nearest_integer": float(abs(integral - nearest_integer)),
    }


def partition_windings(
    determinant: Callable[[np.ndarray], np.ndarray],
    points_per_edge: int = 1024,
) -> dict[str, dict[str, object]]:
    return {
        "total": winding_diagnostic(determinant, DEFAULT_BOUNDS, points_per_edge),
        "validation_core": winding_diagnostic(determinant, CORE_BOUNDS, points_per_edge),
        "test_upper": winding_diagnostic(determinant, UPPER_BOUNDS, points_per_edge),
        "test_lower": winding_diagnostic(determinant, LOWER_BOUNDS, points_per_edge),
    }


def coefficient_comparison() -> dict[str, object]:
    q_binomial = fredholm_coefficients(COEFFICIENT_GUARD)
    trace_recurrence = trace_recurrence_coefficients(COEFFICIENT_GUARD)
    degreewise_scaled_defects = []
    for degree in range(25):
        scale = max(1.0, abs(q_binomial[degree]), abs(trace_recurrence[degree]))
        degreewise_scaled_defects.append(
            abs(q_binomial[degree] - trace_recurrence[degree]) / scale
        )
    max_absolute_defect = float(
        np.max(np.abs(q_binomial[:25] - trace_recurrence[:25]))
    )
    global_scale = float(
        max(1.0, np.max(np.abs(q_binomial[:25])), np.max(np.abs(trace_recurrence[:25])))
    )
    conjugation_defect = float(np.max(np.abs(q_binomial - np.conjugate(q_binomial))))
    return {
        "comparison_degree_max": 24,
        "max_absolute_q_binomial_vs_trace_defect": max_absolute_defect,
        "global_coefficient_scale": global_scale,
        "max_scaled_q_binomial_vs_trace_defect": max_absolute_defect / global_scale,
        "max_degreewise_stabilized_defect": float(max(degreewise_scaled_defects)),
        "max_nominal_coefficient_conjugation_defect_through_k32": conjugation_defect,
    }


def cancellation_diagnostic(repetition: int = 4) -> dict[str, object]:
    terms = [
        channel.a**repetition / (1 - channel.q**repetition)
        for channel in CHANNELS
    ]
    signed_sum = sum(terms)
    absolute_sum = float(sum(abs(term) for term in terms))
    return {
        "repetition": repetition,
        "channel_terms": {
            channel.name: complex_record(complex(term))
            for channel, term in zip(CHANNELS, terms)
        },
        "signed_trace": complex_record(complex(signed_sum)),
        "sum_of_absolute_channel_terms": absolute_sum,
        "cancellation_ratio": float(abs(signed_sum) / absolute_sum),
        "signed_real_part_is_negative": bool(signed_sum.real < 0),
    }


def serializable_winding_counts(
    diagnostics: dict[str, dict[str, object]],
) -> dict[str, int]:
    return {name: int(row["count"]) for name, row in diagnostics.items()}


def build_report() -> dict[str, object]:
    # Discovery is completed before opening the exact scoring ledger.
    coefficient_discoveries: dict[int, dict[str, object]] = {}
    for cutoff in COEFFICIENT_CUTOFFS:
        coefficients = fredholm_coefficients(cutoff)
        coefficient_discoveries[cutoff] = {
            "coefficients": coefficients,
            "roots": roots_from_coefficients(coefficients),
        }

    truth_ledger = exact_scoring_ledger()
    truth_roots = np.asarray(
        [complex(row["root"]) for row in truth_ledger], dtype=np.complex128
    )
    boundary_clearance = float(min(
        min(
            root.real - REAL_MIN,
            REAL_MAX - root.real,
            root.imag - IMAG_MIN,
            IMAG_MAX - root.imag,
        )
        for root in truth_roots
    ))

    coefficient_rows: list[dict[str, object]] = []
    for cutoff in COEFFICIENT_CUTOFFS:
        discovery = coefficient_discoveries[cutoff]["roots"]
        found_roots = np.asarray(discovery["s_roots"], dtype=np.complex128)
        matching = match_roots(found_roots, truth_roots)
        global_assignment_error = max_rectangular_assignment_error(
            found_roots, truth_roots
        )
        coefficient_rows.append(
            {
                "coefficient_cutoff": cutoff,
                "roots_found": len(found_roots),
                "region_counts": root_region_counts(found_roots),
                "matched_within_radius": matching["matched_count"],
                "missing_count": matching["missing_count"],
                "extra_count": matching["extra_count"],
                "max_root_error": global_assignment_error,
                "max_strict_match_error": matching["max_match_error"],
                "max_normalized_polynomial_residual": discovery[
                    "max_normalized_polynomial_residual"
                ],
                "discovered_roots": root_records(found_roots),
            }
        )
    coefficient_by_cutoff = {
        int(row["coefficient_cutoff"]): row for row in coefficient_rows
    }
    branch_drift_24_to_28 = max_assignment_drift(
        coefficient_discoveries[24]["roots"]["s_roots"],
        coefficient_discoveries[28]["roots"]["s_roots"],
    )
    primary_roots = np.asarray(
        coefficient_discoveries[PRIMARY_COEFFICIENT_CUTOFF]["roots"]["s_roots"],
        dtype=np.complex128,
    )
    primary_regional_scoring = {}
    for region_name, region_bounds in (
        ("validation_core", CORE_BOUNDS),
        ("test_upper", UPPER_BOUNDS),
        ("test_lower", LOWER_BOUNDS),
    ):
        found_region = roots_in_bounds(primary_roots, region_bounds)
        truth_region = roots_in_bounds(truth_roots, region_bounds)
        regional_matching = match_roots(found_region, truth_region)
        primary_regional_scoring[region_name] = {
            "found_count": len(found_region),
            "expected_count": len(truth_region),
            "missing_count": regional_matching["missing_count"],
            "extra_count": regional_matching["extra_count"],
            "max_root_error": max_rectangular_assignment_error(
                found_region, truth_region
            ),
        }

    primary_determinant = lambda points: np.asarray(
        direct_determinant(points, PRIMARY_MODE_CUTOFF), dtype=np.complex128
    )
    argument_rows = [
        winding_diagnostic(primary_determinant, DEFAULT_BOUNDS, points)
        for points in CONTOUR_POINTS_PER_EDGE
    ]
    argument_by_grid = {int(row["points_per_edge"]): row for row in argument_rows}
    final_partitions = partition_windings(primary_determinant)

    reciprocal_winding = winding_diagnostic(
        lambda points: 1 / primary_determinant(points),
        DEFAULT_BOUNDS,
        1024,
    )
    truncated_log_winding = winding_diagnostic(
        lambda points: np.asarray(truncated_log_exponential(points, 4)),
        DEFAULT_BOUNDS,
        1024,
    )
    residue_root = complex(CHANNEL_BY_NAME["A_plus"].alpha, CHANNEL_BY_NAME["A_plus"].theta)
    residue_offset = 1.0e-6
    scaled_log_derivative_residue = residue_offset * complex(
        direct_logarithmic_derivative(
            residue_root + residue_offset,
            PRIMARY_MODE_CUTOFF,
        )
    )
    log_derivative_integrals = [
        log_derivative_contour_integral(DEFAULT_BOUNDS, points)
        for points in (512, 1024)
    ]
    determinant_ledger_controls = {
        "nominal_D_winding": int(argument_by_grid[1024]["count"]),
        "reciprocal_1_over_D": {
            "winding": reciprocal_winding,
            "interpretation": "22 poles and no zeros in the frozen rectangle",
        },
        "logarithmic_derivative_D_prime_over_D": {
            "probe_root": complex_record(residue_root),
            "real_probe_offset": residue_offset,
            "scaled_residue_probe": complex_record(scaled_log_derivative_residue),
            "expected_residue": 1.0,
            "contour_integrals": log_derivative_integrals,
            "interpretation": "a meromorphic pole ledger, not a determinant divisor",
        },
        "truncated_log_exponential": {
            "max_repetition": 4,
            "winding": truncated_log_winding,
            "analytically_zero_free": True,
            "interpretation": "exponential of a finite entire sum; forbidden for root discovery",
        },
        "ledgers_combined": False,
    }

    mode_rows: list[dict[str, object]] = []
    for cutoff in MODE_CUTOFFS:
        determinant = lambda points, n=cutoff: np.asarray(
            direct_determinant(points, n), dtype=np.complex128
        )
        diagnostic = winding_diagnostic(determinant, DEFAULT_BOUNDS, 1024)
        mode_rows.append({"mode_cutoff": cutoff, **diagnostic})

    final_contour = rectangle_contour(DEFAULT_BOUNDS, 1024)
    determinant_n40 = np.asarray(direct_determinant(final_contour, 40))
    determinant_n48 = np.asarray(direct_determinant(final_contour, 48))
    mode_contour_relative_drift = float(
        np.max(
            np.abs(determinant_n48 - determinant_n40)
            / np.maximum(np.abs(determinant_n48), np.finfo(float).tiny)
        )
    )

    fault_specs = {
        "missing_only": {
            "omitted_modes": MISSING_MODES,
            "extra_weights": (),
            "absolute_weights": False,
        },
        "extra_only": {
            "omitted_modes": frozenset(),
            "extra_weights": EXTRA_WEIGHTS,
            "absolute_weights": False,
        },
        "balanced": {
            "omitted_modes": MISSING_MODES,
            "extra_weights": EXTRA_WEIGHTS,
            "absolute_weights": False,
        },
        "absolute_value": {
            "omitted_modes": frozenset(),
            "extra_weights": (),
            "absolute_weights": True,
        },
    }
    fault_rows: dict[str, dict[str, object]] = {}
    for name, specification in fault_specs.items():
        determinant = lambda points, spec=specification: np.asarray(
            direct_determinant(
                points,
                PRIMARY_MODE_CUTOFF,
                omitted_modes=spec["omitted_modes"],
                extra_weights=spec["extra_weights"],
                absolute_weights=bool(spec["absolute_weights"]),
            ),
            dtype=np.complex128,
        )
        windings = partition_windings(determinant)
        row: dict[str, object] = {
            "winding_counts": serializable_winding_counts(windings),
            "winding_diagnostics": windings,
            "winding_quality_gate_passed": all(
                float(diagnostic["max_adjacent_phase_increment"]) < PHASE_STEP_MAX
                and float(diagnostic["integer_residual"]) < WINDING_RESIDUAL_MAX
                for diagnostic in windings.values()
            ),
        }
        if name != "absolute_value":
            coefficients = fredholm_coefficients(
                PRIMARY_COEFFICIENT_CUTOFF,
                omitted_modes=specification["omitted_modes"],
                extra_weights=specification["extra_weights"],
            )
            discovery = roots_from_coefficients(coefficients)
            roots = np.asarray(discovery["s_roots"], dtype=np.complex128)
            row.update(
                {
                    "coefficient_roots_found": len(roots),
                    "coefficient_region_counts": root_region_counts(roots),
                    "nominal_truth_matching": match_roots(roots, truth_roots),
                    "max_normalized_polynomial_residual": discovery[
                        "max_normalized_polynomial_residual"
                    ],
                }
            )
        else:
            row["valid_nominal_substitute"] = False
            row["failure_reason"] = (
                "Replacing complex channel weights by absolute values changes the "
                "determinant and its divisor; it cannot be merged with the nominal ledger."
            )
        fault_rows[name] = row

    coefficient_check = coefficient_comparison()
    precision_audit = precision_drift_diagnostic()
    cancellation = cancellation_diagnostic()
    primary_row = coefficient_by_cutoff[PRIMARY_COEFFICIENT_CUTOFF]
    guard_row = coefficient_by_cutoff[COEFFICIENT_GUARD]

    gates = {
        "exact_truth_counts_are_22_12_5_5": root_region_counts(truth_roots)
        == {
            "total": 22,
            "validation_core": 12,
            "test_upper": 5,
            "test_lower": 5,
        },
        "minimum_boundary_clearance_is_at_least_0_07": boundary_clearance >= 0.07 - 1e-14,
        "k16_instability_is_reported": coefficient_by_cutoff[16]["roots_found"] == 28
        and coefficient_by_cutoff[16]["matched_within_radius"] == 6,
        "k20_is_not_misreported_as_position_stable": coefficient_by_cutoff[20][
            "roots_found"
        ]
        == 22
        and coefficient_by_cutoff[20]["missing_count"] > 0,
        "k24_gate": coefficient_by_cutoff[24]["missing_count"] == 0
        and coefficient_by_cutoff[24]["extra_count"] == 0
        and float(coefficient_by_cutoff[24]["max_root_error"]) <= 5.0e-5,
        "k28_gate": primary_row["missing_count"] == 0
        and primary_row["extra_count"] == 0
        and float(primary_row["max_root_error"]) <= 1.0e-6,
        "k32_guard": guard_row["missing_count"] == 0
        and guard_row["extra_count"] == 0
        and float(guard_row["max_root_error"]) <= 1.0e-8,
        "k24_to_k28_branch_drift_gate": branch_drift_24_to_28 <= 2.0e-5,
        "polynomial_residual_gate": max(
            float(row["max_normalized_polynomial_residual"])
            for row in coefficient_rows
        )
        <= 1.0e-10,
        "independent_coefficient_gate": float(
            coefficient_check["max_scaled_q_binomial_vs_trace_defect"]
        )
        <= 1.0e-9,
        "coefficient_conjugation_gate": float(
            coefficient_check["max_nominal_coefficient_conjugation_defect_through_k32"]
        )
        <= 5.0e-12,
        "mode_count_gate": all(
            int(row["count"]) == (18 if int(row["mode_cutoff"]) == 2 else 22)
            for row in mode_rows
        ),
        "mode_value_drift_gate": mode_contour_relative_drift <= 2.0e-6,
        "argument_principle_gate": int(argument_by_grid[512]["count"]) == 22
        and int(argument_by_grid[1024]["count"]) == 22
        and float(argument_by_grid[512]["max_adjacent_phase_increment"])
        < PHASE_STEP_MAX
        and float(argument_by_grid[1024]["max_adjacent_phase_increment"])
        < PHASE_STEP_MAX
        and float(argument_by_grid[1024]["integer_residual"])
        < WINDING_RESIDUAL_MAX,
        "coarse_phase_aliasing_is_reported": float(
            argument_by_grid[128]["max_adjacent_phase_increment"]
        )
        >= PHASE_STEP_MAX
        and float(argument_by_grid[256]["max_adjacent_phase_increment"])
        >= PHASE_STEP_MAX,
        "nominal_partition_count_gate": serializable_winding_counts(final_partitions)
        == {"total": 22, "validation_core": 12, "test_upper": 5, "test_lower": 5},
        "missing_injection_gate": fault_rows["missing_only"]["winding_counts"]
        == {"total": 18, "validation_core": 10, "test_upper": 4, "test_lower": 4}
        and fault_rows["missing_only"]["nominal_truth_matching"]["missing_count"] == 4
        and fault_rows["missing_only"]["nominal_truth_matching"]["extra_count"] == 0,
        "extra_injection_gate": fault_rows["extra_only"]["winding_counts"]
        == {"total": 26, "validation_core": 14, "test_upper": 6, "test_lower": 6}
        and fault_rows["extra_only"]["nominal_truth_matching"]["missing_count"] == 0
        and fault_rows["extra_only"]["nominal_truth_matching"]["extra_count"] == 4,
        "balanced_corruption_gate": fault_rows["balanced"]["winding_counts"]
        == {"total": 22, "validation_core": 12, "test_upper": 5, "test_lower": 5}
        and fault_rows["balanced"]["nominal_truth_matching"]["missing_count"] == 4
        and fault_rows["balanced"]["nominal_truth_matching"]["extra_count"] == 4,
        "absolute_value_ablation_gate": fault_rows["absolute_value"]["winding_counts"][
            "total"
        ]
        == 30
        and fault_rows["absolute_value"]["valid_nominal_substitute"] is False,
        "signed_cancellation_gate": float(cancellation["cancellation_ratio"]) < 0.02
        and bool(cancellation["signed_real_part_is_negative"]),
        "determinant_ledger_separation_gate": int(reciprocal_winding["count"]) == -22
        and int(truncated_log_winding["count"]) == 0
        and abs(scaled_log_derivative_residue - 1) < 1.0e-5
        and all(
            int(row["nearest_integer"]) == 22
            and float(row["distance_to_nearest_integer"]) < 1.0e-4
            for row in log_derivative_integrals
        ),
        "fault_winding_quality_gate": all(
            bool(row["winding_quality_gate_passed"])
            for row in fault_rows.values()
        ),
    }
    gates = {name: bool(value) for name, value in gates.items()}
    all_gates_pass = all(gates.values())

    serialized_truth = [
        {
            "channel": row["channel"],
            "mode": int(row["mode"]),
            "branch": int(row["branch"]),
            "root": complex_record(complex(row["root"])),
        }
        for row in truth_ledger
    ]

    return {
        "control_id": CONTROL_ID,
        "audit_id": AUDIT_ID,
        "clue_id": CLUE_ID,
        "formal_candidate": False,
        "source_lock": SOURCE_LOCK_PATH,
        "source_lock_sha256": source_lock_sha256(),
        "uses_prime_table": False,
        "uses_zero_table": False,
        "mathematical_object": {
            "hilbert_space": "ell^2({A_plus,A_minus,B,C} x N_0)",
            "operator": "L_s e_(c,n)=a_c q_c^n exp(-s)e_(c,n)",
            "trace_class_for_every_complex_s": True,
            "determinant_entire": True,
            "channels": [
                {
                    "name": channel.name,
                    "alpha": channel.alpha,
                    "beta": channel.beta,
                    "theta": channel.theta,
                    "a": complex_record(channel.a),
                    "q": channel.q,
                }
                for channel in CHANNELS
            ],
        },
        "determinant_ledger": {
            "frozen": "D(s)=det_Fr(I-L_s)=product_c product_n (1-a_c q_c^n exp(-s))",
            "reciprocal": "1/D is a separate pole ledger",
            "logarithmic_derivative": "D'/D is a separate meromorphic ledger",
            "truncated_log_exponential": "zero-free and forbidden for root discovery",
            "absolute_value_ablation": "a different invalid determinant, never a nominal bound",
        },
        "determinant_ledger_controls": determinant_ledger_controls,
        "truth_scoring_ledger": {
            "opened_after_discovery": True,
            "root_formula": "alpha_c-n beta_c+i(theta_c+2*pi*k)",
            "region_counts": root_region_counts(truth_roots),
            "minimum_boundary_clearance": boundary_clearance,
            "roots": serialized_truth,
            "split_interpretation": "deterministic holdout, not cryptographically sealed",
        },
        "coefficient_root_discovery": {
            "method": "q-binomial channel convolution, polynomial roots in z=exp(-s), then all logarithm branches in the frozen rectangle",
            "exact_roots_used_as_seeds": False,
            "match_radius": MATCH_RADIUS,
            "cutoff_diagnostics": coefficient_rows,
            "max_branch_drift_k24_to_k28": branch_drift_24_to_28,
            "primary_k28_regional_scoring": primary_regional_scoring,
        },
        "independent_coefficient_check": coefficient_check,
        "supplemental_precision_audit": precision_audit,
        "direct_product_argument_principle": {
            "method": "counterclockwise boundary winding of D_N from direct mode factors",
            "polynomial_roots_used": False,
            "evidence_status": "NUMERICAL_OBSERVATION",
            "rigor_boundary": "successive sampling and phase-step gates are anti-alias diagnostics, not an interval-arithmetic winding certificate",
            "grid_diagnostics": argument_rows,
            "accepted_successive_grids": [512, 1024],
            "partition_windings_at_n48": final_partitions,
        },
        "mode_cutoff_diagnostics": {
            "rows": mode_rows,
            "max_relative_contour_drift_n40_to_n48": mode_contour_relative_drift,
            "root_count_stabilizes_before_determinant_values": True,
        },
        "signed_cancellation": cancellation,
        "fault_injections": fault_rows,
        "acceptance_gates": gates,
        "all_frozen_gates_pass": all_gates_pass,
        "control_route_a_tuple": [
            "A1_WEAK",
            "A2_ANALYTIC_DETERMINANT",
            "A3_PARTIAL_ANALYTIC_STRUCTURE",
            "A4_FAIL",
        ],
        "candidate_route_a_tuple": [
            "A1_FAIL",
            "A2_FAIL",
            "A3_FAIL",
            "A4_FAIL",
        ],
        "route_a_tuple": [
            "A1_WEAK",
            "A2_ANALYTIC_DETERMINANT",
            "A3_PARTIAL_ANALYTIC_STRUCTURE",
            "A4_FAIL",
        ],
        "control_verdict": "GO_WITH_LIMITATIONS" if all_gates_pass else "REVISE",
        "candidate_scope_verdict": "STOP_SCOPED",
        "claim_boundary": {
            "established": [
                "The frozen diagonal family is analytic trace class and its q-Pochhammer Fredholm determinant is entire.",
                "Independent coefficient and direct-product implementations reproduce the frozen 22-root divisor prefix.",
                "The matcher detects missing and extra roots even when balanced corruption preserves every regional count.",
                "Signed complex cancellation is essential and the absolute-value ablation changes the divisor.",
                "Executable negative controls distinguish D, 1/D, D'/D, and the zero-free truncated-log exponential.",
            ],
            "not_established": [
                "No natural primitive-orbit dynamics or rational-prime correspondence is supplied.",
                "No completed-xi functional equation, Gamma factor, trivial-zero structure, or T log T divisor law is reproduced.",
                "No physical quantization, self-adjoint operator, or Route-B obligation is opened.",
                "A fixed frozen-prefix numerical success is not a moving-order theorem for unrelated candidates.",
                "The sampled winding gate is not a rigorous interval or derivative-bound argument-principle certificate.",
            ],
        },
        "next_smallest_task": (
            "Reuse CTRL-0001 as a regression benchmark for the next explicit non-Selberg candidate: "
            "require the same determinant ledger, independent winding count, cutoff drift, and balanced-corruption matcher before interpreting any zero match."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    arguments = parser.parse_args()
    report = build_report()
    payload = json.dumps(report, indent=2, sort_keys=True)
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(payload + "\n", encoding="utf-8")
    if not arguments.quiet:
        print(payload)


if __name__ == "__main__":
    main()
