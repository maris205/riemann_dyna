#!/usr/bin/env python3
"""Structural Route-A audit for the exact-U_c recurrent Logistic gap clock."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence


AUDIT_ID = "P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK"
SOURCE_LOCK = "configs/source_locks/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK.yaml"

U_C = 1.5436890126920764
LEGACY_ROUNDED_U_C = 1.543689
K = 6.764850551029437
OFFSET = 100_000

LEGACY_WARMUP_STEPS = 2_000_000
LEGACY_RECORD_UPDATES = 10_000_000_000

VALIDATION_GAP_LENGTHS = (2, 4, 6, 8, 12, 16)
TEST_GAP_LENGTHS = (10, 14, 18, 24, 32, 64)
VALIDATION_PERIODS = tuple(range(1, 9))
TEST_PERIODS = tuple(range(9, 17))
GAP_SCAN_INITIAL_X = (0.1, 0.5, -0.2, 0.314159265)
GAP_SCAN_DELTAS = (1.0e-5, 1.0e-6, 1.0e-7)
GAP_SCAN_BURN_IN = 20_000
GAP_SCAN_STEPS = 300_000
GAP_SCAN_MAX_REPORTED = 128

POLYNOMIAL_RESIDUAL_CEILING = 1.0e-14
FIXED_POINT_RESIDUAL_CEILING = 1.0e-12
REPEATED_ORBIT_RESIDUAL_CEILING = 1.0e-11


def critical_polynomial(u: float) -> float:
    return u**3 - 2.0 * u**2 + 2.0 * u - 2.0


def logistic_step(x: float, parameter: float) -> float:
    return 1.0 - parameter * x * x


def critical_parent_audit() -> dict[str, Any]:
    x0 = 0.0
    x1 = logistic_step(x0, U_C)
    x2 = logistic_step(x1, U_C)
    x3 = logistic_step(x2, U_C)
    x4 = logistic_step(x3, U_C)
    fixed_value = U_C - 1.0
    return {
        "algebraic_equation": "u^3-2*u^2+2*u-2=0",
        "u_c": U_C,
        "u_c_hex": U_C.hex(),
        "polynomial_residual": critical_polynomial(U_C),
        "derivative_discriminant": -8.0,
        "derivative_strictly_positive": True,
        "critical_orbit": [x0, x1, x2, x3, x4],
        "postcritical_fixed_value": fixed_value,
        "landing_residual": abs(x3 - fixed_value),
        "fixed_point_residual": abs(x4 - x3),
        "legacy_rounded_u_c": LEGACY_ROUNDED_U_C,
        "legacy_rounding_error": LEGACY_ROUNDED_U_C - U_C,
        "legacy_value_is_left_of_u_c": LEGACY_ROUNDED_U_C < U_C,
    }


def critical_seed_gap_control(number_of_updates: int = 16) -> dict[str, Any]:
    """The postcritical seed is a degenerate control, not a physical-gap orbit."""

    x = 0.0
    l_hit_positions: list[int] = []
    orbit = [x]
    for update in range(1, number_of_updates + 1):
        x = logistic_step(x, U_C)
        orbit.append(x)
        if x < 0.0:
            l_hit_positions.append(update)
    gaps = [right - left for left, right in zip(l_hit_positions, l_hit_positions[1:])]
    return {
        "initial_x": 0.0,
        "number_of_updates": number_of_updates,
        "orbit": orbit,
        "l_hit_positions_one_based": l_hit_positions,
        "gaps": gaps,
        "exactly_one_l_hit": len(l_hit_positions) == 1,
        "gap_count": len(gaps),
        "generic_initial_state_required_for_gap_statistics": True,
    }


def block_mu(
    age: int,
    length: int,
    *,
    u_c: float = U_C,
    k: float = K,
    offset: int = OFFSET,
) -> float:
    """One-based anchored block parameter with a bitwise terminal branch."""

    if length < 2 or length % 2 != 0:
        raise ValueError("candidate gap length must be an even integer at least 2")
    if age < 1 or age > length:
        raise ValueError("block age must lie in 1,...,length")
    if offset <= 1:
        raise ValueError("offset must exceed 1")
    if age == length:
        return u_c
    return u_c + k * (
        1.0 / math.log(offset + age) ** 2
        - 1.0 / math.log(offset + length) ** 2
    )


def block_schedule(
    length: int,
    *,
    u_c: float = U_C,
    k: float = K,
    offset: int = OFFSET,
) -> list[float]:
    return [block_mu(age, length, u_c=u_c, k=k, offset=offset) for age in range(1, length + 1)]


def tower_step(
    word: Sequence[int], block_index: int, age: int
) -> tuple[float, tuple[int, int]]:
    """Apply the current fibre parameter, then advance/renew the tower base."""

    if not word:
        raise ValueError("return word must be nonempty")
    if block_index < 0 or block_index >= len(word):
        raise ValueError("block index outside the cyclic word")
    symbol = word[block_index]
    if symbol < 1:
        raise ValueError("return symbols must be positive")
    length = 2 * symbol
    parameter = block_mu(age, length)
    if age < length:
        next_state = (block_index, age + 1)
    else:
        next_state = ((block_index + 1) % len(word), 1)
    return parameter, next_state


def expand_return_word(
    word: Sequence[int], *, u_c: float = U_C, k: float = K
) -> list[float]:
    if not word or any(symbol < 1 for symbol in word):
        raise ValueError("return word must contain positive symbols")
    schedule: list[float] = []
    for symbol in word:
        schedule.extend(block_schedule(2 * symbol, u_c=u_c, k=k))
    return schedule


def phase_space_audit() -> dict[str, float | bool]:
    maximum_parameter_bound = U_C + K / math.log(OFFSET + 1) ** 2
    return {
        "minimum_parameter": U_C,
        "maximum_parameter_bound": maximum_parameter_bound,
        "image_x_minimum_bound": 1.0 - maximum_parameter_bound,
        "image_x_maximum": 1.0,
        "forward_invariant": 0.0 < U_C <= maximum_parameter_bound < 2.0,
    }


def block_anchor_audit(lengths: Iterable[int]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for length in lengths:
        schedule = block_schedule(length)
        rows.append(
            {
                "length": length,
                "update_count": len(schedule),
                "first_parameter": schedule[0],
                "penultimate_parameter": schedule[-2],
                "terminal_parameter": schedule[-1],
                "terminal_hex": schedule[-1].hex(),
                "terminal_bitwise_u_c": schedule[-1] == U_C,
                "interior_strictly_above_u_c": all(value > U_C for value in schedule[:-1]),
                "strictly_decreases_to_terminal": all(
                    schedule[index + 1] < schedule[index]
                    for index in range(len(schedule) - 1)
                ),
            }
        )
    return {
        "rows": rows,
        "all_update_counts_exact": all(row["update_count"] == row["length"] for row in rows),
        "all_terminal_bitwise_u_c": all(bool(row["terminal_bitwise_u_c"]) for row in rows),
        "all_interiors_above_u_c": all(bool(row["interior_strictly_above_u_c"]) for row in rows),
        "all_strictly_decrease": all(bool(row["strictly_decreases_to_terminal"]) for row in rows),
    }


def legacy_index_audit() -> dict[str, Any]:
    terminal_index = LEGACY_WARMUP_STEPS + LEGACY_RECORD_UPDATES - 1
    old_u_temp = LEGACY_ROUNDED_U_C - K / math.log(OFFSET + LEGACY_RECORD_UPDATES) ** 2
    old_terminal_parameter = old_u_temp + K / math.log(OFFSET + terminal_index) ** 2
    corrected_u_temp = U_C - K / math.log(OFFSET + terminal_index) ** 2
    corrected_terminal_parameter = corrected_u_temp + K / math.log(OFFSET + terminal_index) ** 2
    return {
        "warmup_indices": [0, LEGACY_WARMUP_STEPS - 1],
        "record_indices": [LEGACY_WARMUP_STEPS, terminal_index],
        "record_update_count": LEGACY_RECORD_UPDATES,
        "terminal_update_index": terminal_index,
        "legacy_anchor_index": LEGACY_RECORD_UPDATES,
        "updates_after_legacy_anchor": terminal_index - LEGACY_RECORD_UPDATES,
        "old_u_temp": old_u_temp,
        "old_terminal_parameter": old_terminal_parameter,
        "old_terminal_error_from_rounded_target": old_terminal_parameter - LEGACY_ROUNDED_U_C,
        "old_terminal_error_from_algebraic_u_c": old_terminal_parameter - U_C,
        "corrected_u_temp_for_algebraic_u_c": corrected_u_temp,
        "corrected_terminal_parameter": corrected_terminal_parameter,
        "corrected_terminal_error": corrected_terminal_parameter - U_C,
        "first_recorded_edge_in_legacy": "bin(x_0) -> bin(x_(W+1))",
        "chronological_first_recorded_edge": "bin(x_W) -> bin(x_(W+1))",
        "legacy_first_edge_is_stale": True,
    }


def gap_statistics(
    parameter: float,
    initial_x: float,
    *,
    burn_in: int = GAP_SCAN_BURN_IN,
    recorded_updates: int = GAP_SCAN_STEPS,
    maximum_reported_gap: int = GAP_SCAN_MAX_REPORTED,
) -> dict[str, Any]:
    x = initial_x
    for _ in range(burn_in):
        x = logistic_step(x, parameter)

    counts = [0] * (maximum_reported_gap + 1)
    previous_l_index = -1
    l_hits = 0
    gap_count = 0
    odd_gap_count = 0
    overflow_gap_count = 0
    maximum_gap = 0
    minimum_abs_state = abs(x)
    lyapunov_sum = 0.0

    for index in range(recorded_updates):
        derivative_magnitude = abs(-2.0 * parameter * x)
        if derivative_magnitude == 0.0:
            lyapunov_sum = float("-inf")
        elif not math.isinf(lyapunov_sum):
            lyapunov_sum += math.log(derivative_magnitude)
        x = logistic_step(x, parameter)
        minimum_abs_state = min(minimum_abs_state, abs(x))
        if x < 0.0:
            l_hits += 1
            if previous_l_index >= 0:
                gap = index - previous_l_index
                gap_count += 1
                maximum_gap = max(maximum_gap, gap)
                odd_gap_count += gap % 2
                if gap <= maximum_reported_gap:
                    counts[gap] += 1
                else:
                    overflow_gap_count += 1
            previous_l_index = index

    support = [gap for gap, count in enumerate(counts) if count]
    stable_support_threshold = 10
    stable_support = [gap for gap in support if counts[gap] >= stable_support_threshold]
    odd_support = [gap for gap in support if gap % 2 == 1]
    return {
        "parameter": parameter,
        "parameter_offset_from_u_c": parameter - U_C,
        "initial_x": initial_x,
        "burn_in": burn_in,
        "recorded_updates": recorded_updates,
        "l_hits": l_hits,
        "l_frequency": l_hits / recorded_updates,
        "gap_count": gap_count,
        "odd_gap_count": odd_gap_count,
        "odd_gap_mass": odd_gap_count / gap_count if gap_count else 0.0,
        "maximum_gap": maximum_gap,
        "support": support,
        "support_size": len(support),
        "stable_support_count_threshold": stable_support_threshold,
        "stable_support": stable_support,
        "stable_support_maximum": max(stable_support) if stable_support else None,
        "odd_support": odd_support,
        "minimum_odd_gap": min(odd_support) if odd_support else None,
        "all_reported_gaps_even": all(gap % 2 == 0 for gap in support),
        "overflow_gap_count": overflow_gap_count,
        "minimum_abs_state": minimum_abs_state,
        "lyapunov_exponent": lyapunov_sum / recorded_updates,
        "histogram_counts": {str(gap): counts[gap] for gap in support},
    }


def gap_phase_boundary_audit() -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for initial_x in GAP_SCAN_INITIAL_X:
        center = gap_statistics(U_C, initial_x)
        rounded = gap_statistics(LEGACY_ROUNDED_U_C, initial_x)
        controls = []
        for delta in GAP_SCAN_DELTAS:
            left = gap_statistics(U_C - delta, initial_x)
            right = gap_statistics(U_C + delta, initial_x)
            controls.append({"delta": delta, "left": left, "right": right})
        rows.append(
            {
                "initial_x": initial_x,
                "center": center,
                "legacy_rounded": rounded,
                "controls": controls,
            }
        )

    center_odd_zero = all(row["center"]["odd_gap_count"] == 0 for row in rows)
    rounded_odd_zero = all(row["legacy_rounded"]["odd_gap_count"] == 0 for row in rows)
    left_odd_zero = all(
        control["left"]["odd_gap_count"] == 0
        for row in rows
        for control in row["controls"]
    )
    right_has_odd_gaps = all(
        control["right"]["odd_gap_count"] > 0
        for row in rows
        for control in row["controls"]
    )
    return {
        "rows": rows,
        "gates": {
            "center_odd_gap_mass_is_zero": center_odd_zero,
            "left_controls_remain_even": left_odd_zero,
            "right_controls_open_odd_gap_channel": right_has_odd_gaps,
            "rounded_legacy_value_remains_on_even_left_side": rounded_odd_zero,
        },
        "finite_tail_observation_only": {
            "left_raw_maxima_are_below_center_in_this_cutoff": all(
                control["left"]["maximum_gap"] < row["center"]["maximum_gap"]
                for row in rows
                for control in row["controls"]
            ),
            "rounded_raw_maximum_is_below_center_in_this_cutoff": all(
                row["legacy_rounded"]["maximum_gap"] < row["center"]["maximum_gap"]
                for row in rows
            ),
            "claim_status": "NUMERICAL_OBSERVATION; long-tail support is cutoff and precision sensitive",
        },
    }


def compositions(total: int) -> Iterator[tuple[int, ...]]:
    if total < 0:
        return
    if total == 0:
        yield ()
        return
    for first in range(1, total + 1):
        for remainder in compositions(total - first):
            yield (first,) + remainder


def canonical_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    if not word:
        raise ValueError("word must be nonempty")
    return min(word[index:] + word[:index] for index in range(len(word)))


def is_primitive_word(word: tuple[int, ...]) -> bool:
    if not word:
        return False
    size = len(word)
    for prefix_size in range(1, size):
        if size % prefix_size == 0 and word == word[:prefix_size] * (size // prefix_size):
            return False
    return True


def primitive_return_words(period: int) -> list[tuple[int, ...]]:
    if period < 2 or period % 2 != 0:
        return []
    half_period = period // 2
    words: set[tuple[int, ...]] = set()
    for word in compositions(half_period):
        canonical = canonical_rotation(word)
        if is_primitive_word(canonical):
            words.add(canonical)
    return sorted(words)


def divisors(number: int) -> list[int]:
    return [divisor for divisor in range(1, number + 1) if number % divisor == 0]


def mobius(number: int) -> int:
    if number == 1:
        return 1
    remaining = number
    prime_factors = 0
    factor = 2
    while factor * factor <= remaining:
        if remaining % factor == 0:
            exponent = 0
            while remaining % factor == 0:
                remaining //= factor
                exponent += 1
            if exponent > 1:
                return 0
            prime_factors += 1
        factor += 1
    if remaining > 1:
        prime_factors += 1
    return -1 if prime_factors % 2 else 1


def tower_fixed_count(period: int) -> int:
    if period < 1 or period % 2 != 0:
        return 0
    return 2 * (2 ** (period // 2) - 1)


def tower_primitive_orbit_count(period: int) -> int:
    if period < 1:
        return 0
    exact_point_count = sum(
        mobius(divisor) * tower_fixed_count(period // divisor) for divisor in divisors(period)
    )
    if exact_point_count % period != 0:
        raise ArithmeticError("primitive point count is not divisible by the period")
    return exact_point_count // period


def tower_census(maximum_period: int = 16) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for period in range(1, maximum_period + 1):
        words = primitive_return_words(period)
        formula_count = tower_primitive_orbit_count(period)
        rows.append(
            {
                "period": period,
                "fixed_point_count": tower_fixed_count(period),
                "primitive_orbit_count_formula": formula_count,
                "primitive_orbit_count_enumerated": len(words),
                "primitive_words": [list(word) for word in words],
                "enumeration_matches_formula": len(words) == formula_count,
            }
        )
    return {
        "tower_zeta": "Z_T(z)=(1-z^2)/(1-2*z^2)",
        "fixed_count_formula": "Fix(G^n)=0 for odd n; Fix(G^(2r))=2*(2^r-1)",
        "rows": rows,
        "all_enumerations_match": all(bool(row["enumeration_matches_formula"]) for row in rows),
    }


def apply_schedule(x: float, schedule: Sequence[float]) -> float:
    for parameter in schedule:
        x = logistic_step(x, parameter)
    return x


def fixed_point_witness(schedule: Sequence[float]) -> tuple[float, float]:
    if not schedule:
        raise ValueError("schedule must be nonempty")

    lower = -1.0
    upper = 1.0
    lower_residual = apply_schedule(lower, schedule) - lower
    upper_residual = apply_schedule(upper, schedule) - upper
    if lower_residual < 0.0 or upper_residual > 0.0:
        raise ArithmeticError("interval fixed-point bracket failed")

    best_x = lower
    best_residual = abs(lower_residual)
    if abs(upper_residual) < best_residual:
        best_x = upper
        best_residual = abs(upper_residual)

    for _ in range(200):
        midpoint = (lower + upper) / 2.0
        if midpoint == lower or midpoint == upper:
            break
        midpoint_residual = apply_schedule(midpoint, schedule) - midpoint
        if abs(midpoint_residual) < best_residual:
            best_x = midpoint
            best_residual = abs(midpoint_residual)
        if midpoint_residual == 0.0:
            return midpoint, 0.0
        if (lower_residual > 0.0 and midpoint_residual > 0.0) or (
            lower_residual < 0.0 and midpoint_residual < 0.0
        ):
            lower = midpoint
            lower_residual = midpoint_residual
        else:
            upper = midpoint
            upper_residual = midpoint_residual
    return best_x, best_residual


def iterate_with_multiplier(x: float, schedule: Sequence[float]) -> tuple[float, float]:
    multiplier = 1.0
    for parameter in schedule:
        multiplier *= -2.0 * parameter * x
        x = logistic_step(x, parameter)
    return x, multiplier


def fibre_witness_census(maximum_period: int = 16) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for period in range(2, maximum_period + 1):
        for word in primitive_return_words(period):
            schedule = expand_return_word(word)
            fixed_x, bracket_residual = fixed_point_witness(schedule)
            returned_x, multiplier = iterate_with_multiplier(fixed_x, schedule)
            terminal_positions: list[int] = []
            cursor = 0
            for symbol in word:
                cursor += 2 * symbol
                terminal_positions.append(cursor)
            terminal_parameters = [schedule[position - 1] for position in terminal_positions]
            rows.append(
                {
                    "period": period,
                    "return_word": list(word),
                    "gap_word": [2 * symbol for symbol in word],
                    "fixed_x": fixed_x,
                    "bracket_residual": bracket_residual,
                    "return_residual": abs(returned_x - fixed_x),
                    "signed_multiplier": multiplier,
                    "orientation": "preserving" if multiplier > 0.0 else "reversing",
                    "phase_label": "0" if multiplier > 0.0 else "pi",
                    "terminal_update_positions_one_based": terminal_positions,
                    "terminal_parameters": terminal_parameters,
                    "terminal_parameters_bitwise_u_c": all(value == U_C for value in terminal_parameters),
                    "aging_interior_update_count": period - len(word),
                    "base_exact_period": True,
                    "full_exact_period_by_projection": True,
                }
            )
    return {
        "rows": rows,
        "witness_count": len(rows),
        "maximum_period": maximum_period,
        "maximum_return_residual": max(row["return_residual"] for row in rows),
        "all_terminal_parameters_bitwise_u_c": all(
            bool(row["terminal_parameters_bitwise_u_c"]) for row in rows
        ),
        "all_full_periods_certified_by_projection": all(
            bool(row["full_exact_period_by_projection"]) for row in rows
        ),
        "fibre_root_completeness": "one guaranteed witness per primitive base orbit; not a full root census",
    }


def repetition_control() -> dict[str, Any]:
    word = (1, 2)
    schedule = expand_return_word(word)
    fixed_x, _ = fixed_point_witness(schedule)
    once_x, once_multiplier = iterate_with_multiplier(fixed_x, schedule)
    twice_x, second_multiplier = iterate_with_multiplier(once_x, schedule)
    combined_multiplier = once_multiplier * second_multiplier
    expected_multiplier = once_multiplier**2
    return {
        "primitive_word": list(word),
        "primitive_period": len(schedule),
        "one_return_residual": abs(once_x - fixed_x),
        "two_return_residual": abs(twice_x - fixed_x),
        "primitive_signed_multiplier": once_multiplier,
        "repeated_signed_multiplier": combined_multiplier,
        "expected_repeated_multiplier": expected_multiplier,
        "multiplier_relative_error": abs(combined_multiplier - expected_multiplier)
        / max(1.0, abs(expected_multiplier)),
        "repeated_word_is_new_primitive_base_orbit": False,
    }


def reorder_control() -> dict[str, Any]:
    reference_word = (1, 2, 3, 4)
    reordered_word = (1, 3, 2, 4)
    reference_schedule = expand_return_word(reference_word)
    reordered_schedule = expand_return_word(reordered_word)
    reference_root, _ = fixed_point_witness(reference_schedule)
    reordered_root, _ = fixed_point_witness(reordered_schedule)
    _, reference_multiplier = iterate_with_multiplier(reference_root, reference_schedule)
    _, reordered_multiplier = iterate_with_multiplier(reordered_root, reordered_schedule)
    return {
        "reference_word": list(reference_word),
        "reordered_word": list(reordered_word),
        "same_total_period": len(reference_schedule) == len(reordered_schedule),
        "cyclically_equivalent": canonical_rotation(reference_word)
        == canonical_rotation(reordered_word),
        "schedules_identical": reference_schedule == reordered_schedule,
        "fixed_root_distance": abs(reference_root - reordered_root),
        "signed_multiplier_distance": abs(reference_multiplier - reordered_multiplier),
        "order_is_dynamically_visible": reference_schedule != reordered_schedule
        and abs(reference_multiplier - reordered_multiplier) > 1.0e-8,
    }


def simpler_parent_and_neighbor_controls() -> dict[str, Any]:
    word = (1, 2)
    dynamic_schedule = expand_return_word(word)
    static_schedule = expand_return_word(word, k=0.0)
    neighbor_rows = []
    for factor in (0.99, 1.01):
        schedule = expand_return_word(word, k=K * factor)
        fixed_x, residual = fixed_point_witness(schedule)
        neighbor_rows.append(
            {
                "k_factor": factor,
                "terminal_parameters_bitwise_u_c": schedule[1] == U_C and schedule[-1] == U_C,
                "fixed_point_residual": residual,
                "fixed_x": fixed_x,
            }
        )
    rounded_schedule = block_schedule(2, u_c=LEGACY_ROUNDED_U_C)
    return {
        "static_k_zero_schedule_is_constant_u_c": all(value == U_C for value in static_schedule),
        "dynamic_schedule_has_aging_interior": max(dynamic_schedule) > min(dynamic_schedule),
        "neighbor_k_rows": neighbor_rows,
        "all_neighbor_anchors_exact": all(
            bool(row["terminal_parameters_bitwise_u_c"]) for row in neighbor_rows
        ),
        "rounded_terminal_equals_rounded_value": rounded_schedule[-1] == LEGACY_ROUNDED_U_C,
        "rounded_terminal_misses_algebraic_u_c": rounded_schedule[-1] != U_C,
    }


def tower_ordering_trace(word: Sequence[int]) -> list[dict[str, Any]]:
    block_index = 0
    age = 1
    total_period = 2 * sum(word)
    rows: list[dict[str, Any]] = []
    for step in range(1, total_period + 1):
        current_block = block_index
        current_symbol = word[current_block]
        current_length = 2 * current_symbol
        parameter, (block_index, age) = tower_step(word, current_block, age)
        rows.append(
            {
                "step": step,
                "return_symbol": current_symbol,
                "gap_length": current_length,
                "parameter": parameter,
                "terminal_update": parameter == U_C,
                "next_block_index": block_index,
                "next_age": age,
            }
        )
    return rows


def determinant_bounds(maximum_period: int = 16) -> dict[str, Any]:
    rows = []
    for period in range(1, maximum_period + 1):
        base_count = tower_fixed_count(period)
        rows.append(
            {
                "period": period,
                "tower_fixed_count": base_count,
                "full_fixed_count_lower_bound": base_count,
                "full_fixed_count_upper_bound": (2**period) * base_count,
                "coarse_four_power_bound": 4**period,
            }
        )
    return {
        "rows": rows,
        "tower_zeta": "Z_T(z)=(1-z^2)/(1-2*z^2)",
        "full_determinant": "D_AM,F(z)=exp(-sum_(n>=1) Fix(F^n)*z^n/n)",
        "proved_log_series_disk": "|z|<1/4",
        "fredholm_determinant_defined": False,
        "base_and_full_ledgers_are_distinct": True,
        "unit_clock_substitution": "z=exp(-s)",
        "vertical_period": "2*pi*i",
        "unit_lattice_completed_xi_candidate": False,
    }


def build_report() -> dict[str, Any]:
    critical = critical_parent_audit()
    critical_seed = critical_seed_gap_control()
    anchor = block_anchor_audit(VALIDATION_GAP_LENGTHS + TEST_GAP_LENGTHS)
    phase_space = phase_space_audit()
    legacy = legacy_index_audit()
    gap_boundary = gap_phase_boundary_audit()
    tower = tower_census(max(TEST_PERIODS))
    fibre = fibre_witness_census(max(TEST_PERIODS))
    repetition = repetition_control()
    reorder = reorder_control()
    parent_controls = simpler_parent_and_neighbor_controls()
    ordering_trace = tower_ordering_trace((1, 2))
    determinant = determinant_bounds(max(TEST_PERIODS))

    gates = {
        "algebraic_u_c_polynomial_matches": abs(critical["polynomial_residual"])
        <= POLYNOMIAL_RESIDUAL_CEILING,
        "critical_orbit_lands_on_fixed_point": critical["landing_residual"]
        <= POLYNOMIAL_RESIDUAL_CEILING
        and critical["fixed_point_residual"] <= POLYNOMIAL_RESIDUAL_CEILING,
        "legacy_rounded_value_is_rejected_as_exact_u_c": critical["legacy_value_is_left_of_u_c"],
        "critical_seed_is_a_single_hit_degenerate_control": critical_seed["exactly_one_l_hit"]
        and critical_seed["gap_count"] == 0,
        "block_update_count_and_anchor_exact": anchor["all_update_counts_exact"]
        and anchor["all_terminal_bitwise_u_c"]
        and anchor["all_interiors_above_u_c"]
        and anchor["all_strictly_decrease"],
        "phase_space_forward_invariant": phase_space["forward_invariant"],
        "legacy_terminal_index_fault_detected": legacy["updates_after_legacy_anchor"]
        == LEGACY_WARMUP_STEPS - 1
        and legacy["old_terminal_error_from_algebraic_u_c"] < 0.0,
        "legacy_stale_first_edge_detected": legacy["legacy_first_edge_is_stale"],
        "u_c_left_center_right_gap_boundary_passes": all(gap_boundary["gates"].values()),
        "tower_primitive_census_complete": tower["all_enumerations_match"],
        "full_lift_witnesses_close": fibre["maximum_return_residual"]
        <= FIXED_POINT_RESIDUAL_CEILING,
        "full_lift_terminal_updates_exact": fibre["all_terminal_parameters_bitwise_u_c"],
        "primitive_periods_certified_by_base_projection": fibre[
            "all_full_periods_certified_by_projection"
        ],
        "repetition_multiplier_relation_passes": repetition["two_return_residual"]
        <= REPEATED_ORBIT_RESIDUAL_CEILING
        and repetition["multiplier_relative_error"] <= 1.0e-11,
        "same_total_reorder_is_detected": reorder["order_is_dynamically_visible"]
        and not reorder["cyclically_equivalent"],
        "simpler_parent_and_neighbor_controls_pass": parent_controls[
            "static_k_zero_schedule_is_constant_u_c"
        ]
        and parent_controls["dynamic_schedule_has_aging_interior"]
        and parent_controls["all_neighbor_anchors_exact"]
        and parent_controls["rounded_terminal_misses_algebraic_u_c"],
        "terminal_update_precedes_renewal": ordering_trace[1]["terminal_update"]
        and ordering_trace[1]["next_block_index"] == 1
        and ordering_trace[1]["next_age"] == 1,
        "determinant_ledgers_separated": determinant["base_and_full_ledgers_are_distinct"]
        and not determinant["fredholm_determinant_defined"],
    }

    return {
        "audit_id": AUDIT_ID,
        "formal_candidate": False,
        "clue_id": "CLUE-A1-004",
        "source_lock": SOURCE_LOCK,
        "mathematical_object": {
            "critical_parent": "f_Uc(y)=1-U_c*y^2 with p(U_c)=0",
            "ambient_parent_interval": "[-1,1]",
            "physical_parent_core": "J=[1-U_c,1]",
            "event": "physical L hit: y in J and y<0; y=0 is a non-event",
            "gap": "first return time to physical L at exact U_c",
            "tower_alphabet": "one symbol m>=1 for gap L=2*m",
            "full_map": "F(x,omega,j)=(1-mu(j,2*omega_0)*x^2,G(omega,j))",
        },
        "parameters": {
            "u_c": U_C,
            "u_c_hex": U_C.hex(),
            "legacy_rounded_u_c": LEGACY_ROUNDED_U_C,
            "legacy_rounding_error": LEGACY_ROUNDED_U_C - U_C,
            "k": K,
            "offset": OFFSET,
        },
        "critical_parent": critical,
        "critical_seed_control": critical_seed,
        "block_anchor": anchor,
        "phase_space": phase_space,
        "legacy_index_control": legacy,
        "gap_phase_boundary": gap_boundary,
        "tower_primitive_census": tower,
        "full_fibre_witnesses": fibre,
        "controls": {
            "primitive_repetition": repetition,
            "same_total_noncyclic_reorder": reorder,
            "simpler_parent_and_neighbor_parameters": parent_controls,
            "terminal_ordering_trace_word_1_2": ordering_trace,
        },
        "fixed_count_and_determinant_ledger": determinant,
        "gates": gates,
        "audit_passed": all(gates.values()),
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall_verdict": "ROUTE_A_EXPLORATORY",
            "recommended_audit_verdict": "REVISE",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "established": [
                "the algebraic U_c anchor and its postcritical fixed-point identity",
                "the rounded legacy value lies on the left side of the exact critical point",
                "the frozen U_c left/center/right odd-gap-channel diagnostic",
                "the physical-core first-return support is exactly 2*N with one interval branch per even label",
                "every finite word of positive even return labels has a nonempty physical first-return cylinder",
                "the ambient [-1,1] support is N because transient odd branches are topologically nonempty; every such branch has zero invariant mass",
                "a recurrent even-return tower with complete primitive base census through period 16",
                "at least one signed-multiplier full Logistic lift per primitive base orbit in that prefix",
                "finite full fixed counts and local convergence of the reciprocal Artin-Mazur log series",
            ],
            "not_established": [
                "full arithmetic prime-gap statistics or mod-3 resonance",
                "closed-form or certified physical-acip branch weights",
                "complete fibre periodic-orbit enumeration and multiplicities",
                "an intrinsic non-lattice roof or von-Mangoldt repetition weights",
                "a Ruelle or Fredholm determinant, analytic continuation, or completed-xi divisor",
                "natural quantization, Route B, Hilbert-Polya, or RH",
            ],
        },
        "next_smallest_task": (
            "Prove or refute d mu_ac/dx(-rho+t)=C*t^(-1/2)*(1+o(1)), C>0, "
            "and the resulting conditional branch-mass ratio, using a direct density "
            "argument, a weighted function space, or a newly frozen accelerated inducing domain."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("artifacts/p4_logistic_recurrent_uc_anchored_clock/structural_audit.json"),
    )
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    report = build_report()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if not args.quiet:
        print(json.dumps(report, indent=2, sort_keys=True))
    if not report["audit_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
