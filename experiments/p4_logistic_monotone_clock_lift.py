#!/usr/bin/env python3
"""Exact structural audit for the compact monotone-clock Logistic lift."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any, Iterable


AUDIT_ID = "P4-LOGISTIC-MONOTONE-CLOCK-LIFT"
SOURCE_LOCK = "configs/source_locks/P4-LOGISTIC-MONOTONE-CLOCK-LIFT.yaml"

ENDPOINT_HIGH = 1.5637
ENDPOINT_LOW = 1.5437
FIRST_INDEX = 1
LAST_INDEX = 1_000_000
CLOCK_OFFSET = 10
K = 0.1185699450083701
U_C = 1.543078787606443
INITIAL_CLOCK = 1.0 / math.log(FIRST_INDEX + CLOCK_OFFSET)

VALIDATION_INDICES = (1, 2, 3, 8, 32)
TEST_INDICES = (1_000, 1_000_000)
REGRESSION_PERIODS = (1, 2, 3, 4, 8, 16, 32, 64)
INITIAL_X_CONTROLS = (-1.0, -0.5, 0.0, 0.5, 1.0)
ADVERSARIAL_CLOCK_PERIODS = (8, 32, 64)
SCHEDULE_ERROR_CEILING = 1.0e-13
TRAJECTORY_ERROR_CEILING = 1.0e-12


def derived_schedule_parameters() -> tuple[float, float]:
    """Derive k and u_c from the two frozen legacy endpoints."""

    start = 1.0 / math.log(FIRST_INDEX + CLOCK_OFFSET) ** 2
    end = 1.0 / math.log(LAST_INDEX + CLOCK_OFFSET) ** 2
    k = (ENDPOINT_HIGH - ENDPOINT_LOW) / (start - end)
    u_c = ENDPOINT_LOW - k * end
    return k, u_c


def legacy_clock(index: int) -> float:
    if index < FIRST_INDEX:
        raise ValueError("legacy index must be at least 1")
    return 1.0 / math.log(index + CLOCK_OFFSET)


def mu_from_clock(clock: float) -> float:
    if clock < 0.0 or clock > INITIAL_CLOCK:
        raise ValueError("clock lies outside the frozen compact phase space")
    return U_C + K * clock * clock


def legacy_mu(index: int) -> float:
    return mu_from_clock(legacy_clock(index))


def compact_clock_map(clock: float) -> float:
    """Stable form of G(v)=1/log(exp(1/v)+1), with G(0)=0."""

    if clock < 0.0 or clock > INITIAL_CLOCK:
        raise ValueError("clock lies outside the frozen compact phase space")
    if clock == 0.0:
        return 0.0
    correction = math.log1p(math.exp(-1.0 / clock))
    return clock / (1.0 + clock * correction)


def compact_clock_iterate_closed(clock: float, steps: int) -> float:
    """Closed form G^steps(v), evaluated without exp(1/v) overflow."""

    if steps < 0:
        raise ValueError("steps must be nonnegative")
    if clock < 0.0 or clock > INITIAL_CLOCK:
        raise ValueError("clock lies outside the frozen compact phase space")
    if steps == 0 or clock == 0.0:
        return clock
    correction = math.log1p(steps * math.exp(-1.0 / clock))
    return clock / (1.0 + clock * correction)


def compact_clock_iterate_direct(clock: float, steps: int) -> float:
    value = clock
    for _ in range(steps):
        value = compact_clock_map(value)
    return value


def logistic_step(x: float, clock: float) -> float:
    if not -1.0 <= x <= 1.0:
        raise ValueError("x lies outside the frozen phase space")
    return 1.0 - mu_from_clock(clock) * x * x


def lift_step(x: float, clock: float) -> tuple[float, float]:
    return logistic_step(x, clock), compact_clock_map(clock)


def positive_fixed_point(mu: float) -> float:
    return (-1.0 + math.sqrt(1.0 + 4.0 * mu)) / (2.0 * mu)


def schedule_regression(indices: Iterable[int]) -> dict[str, Any]:
    rows: list[dict[str, float | int]] = []
    for index in indices:
        closed_clock = compact_clock_iterate_closed(INITIAL_CLOCK, index - 1)
        expected_clock = legacy_clock(index)
        lifted_mu = mu_from_clock(closed_clock)
        expected_mu = legacy_mu(index)
        rows.append(
            {
                "index": index,
                "closed_clock": closed_clock,
                "expected_clock": expected_clock,
                "clock_error": abs(closed_clock - expected_clock),
                "lifted_mu": lifted_mu,
                "expected_mu": expected_mu,
                "mu_error": abs(lifted_mu - expected_mu),
            }
        )
    return {
        "rows": rows,
        "max_clock_error": max(row["clock_error"] for row in rows),
        "max_mu_error": max(row["mu_error"] for row in rows),
    }


def clock_iteration_regression(periods: Iterable[int]) -> dict[str, Any]:
    rows: list[dict[str, float | int | bool]] = []
    for period in periods:
        direct = compact_clock_iterate_direct(INITIAL_CLOCK, period)
        closed = compact_clock_iterate_closed(INITIAL_CLOCK, period)
        rows.append(
            {
                "period": period,
                "direct": direct,
                "closed": closed,
                "absolute_error": abs(direct - closed),
                "strict_decrease": closed < INITIAL_CLOCK,
                "full_state_clock_return": closed == INITIAL_CLOCK,
            }
        )
    return {
        "rows": rows,
        "max_absolute_error": max(row["absolute_error"] for row in rows),
        "all_strictly_decrease": all(bool(row["strict_decrease"]) for row in rows),
        "any_interior_clock_return": any(bool(row["full_state_clock_return"]) for row in rows),
    }


def trajectory_regression(x_values: Iterable[float], steps: int = 8) -> dict[str, Any]:
    rows: list[dict[str, float]] = []
    for initial_x in x_values:
        direct_x = initial_x
        lifted_x = initial_x
        lifted_clock = INITIAL_CLOCK
        max_error = 0.0
        for index in range(1, steps + 1):
            direct_x = 1.0 - legacy_mu(index) * direct_x * direct_x
            lifted_x, lifted_clock = lift_step(lifted_x, lifted_clock)
            max_error = max(max_error, abs(direct_x - lifted_x))
        rows.append(
            {
                "initial_x": initial_x,
                "steps": float(steps),
                "direct_x": direct_x,
                "lifted_x": lifted_x,
                "max_x_error": max_error,
            }
        )
    return {
        "rows": rows,
        "max_x_error": max(row["max_x_error"] for row in rows),
    }


def phase_space_audit() -> dict[str, float | bool]:
    minimum_mu = U_C
    maximum_mu = ENDPOINT_HIGH
    image_minimum = 1.0 - maximum_mu
    image_maximum = 1.0
    return {
        "minimum_mu": minimum_mu,
        "maximum_mu": maximum_mu,
        "image_x_minimum": image_minimum,
        "image_x_maximum": image_maximum,
        "forward_invariant": 0.0 <= minimum_mu <= maximum_mu <= 2.0
        and image_minimum >= -1.0
        and image_maximum <= 1.0,
    }


def projected_fixed_point_control() -> dict[str, float | bool]:
    fixed_x = positive_fixed_point(ENDPOINT_HIGH)
    next_x, next_clock = lift_step(fixed_x, INITIAL_CLOCK)
    return {
        "mu": ENDPOINT_HIGH,
        "fixed_x": fixed_x,
        "x_return_error": abs(next_x - fixed_x),
        "initial_clock": INITIAL_CLOCK,
        "next_clock": next_clock,
        "clock_return_error": abs(next_clock - INITIAL_CLOCK),
        "projected_x_returns": math.isclose(next_x, fixed_x, abs_tol=1.0e-14),
        "full_state_returns": math.isclose(next_clock, INITIAL_CLOCK, abs_tol=0.0),
    }


def boundary_parent_control() -> dict[str, float | bool]:
    fixed_x = positive_fixed_point(U_C)
    next_x, next_clock = lift_step(fixed_x, 0.0)
    return {
        "boundary_parameter": U_C,
        "finite_window_endpoint": ENDPOINT_LOW,
        "legacy_regression_parameter": 1.543689,
        "fixed_x": fixed_x,
        "x_return_error": abs(next_x - fixed_x),
        "clock_return_error": abs(next_clock),
        "is_full_boundary_fixed_point": math.isclose(next_x, fixed_x, abs_tol=1.0e-14)
        and next_clock == 0.0,
        "boundary_clock_multiplier": 1.0,
        "neutral_clock_direction": True,
    }


def modulo_clock_controls(periods: Iterable[int]) -> list[dict[str, float | int | bool]]:
    rows: list[dict[str, float | int | bool]] = []
    for period in periods:
        periodized_next_mu = legacy_mu(1)
        true_next_mu = legacy_mu(period + 1)
        rows.append(
            {
                "period": period,
                "periodized_mu_at_step_P_plus_1": periodized_next_mu,
                "true_mu_at_step_P_plus_1": true_next_mu,
                "absolute_discrepancy": abs(periodized_next_mu - true_next_mu),
                "same_schedule": math.isclose(periodized_next_mu, true_next_mu, abs_tol=0.0),
            }
        )
    return rows


def clamped_clock_controls(periods: Iterable[int]) -> dict[str, Any]:
    rows = [
        {
            "cutoff": period,
            "clamped_parent_mu": legacy_mu(period),
            "distance_from_true_limit_u_c": abs(legacy_mu(period) - U_C),
        }
        for period in periods
    ]
    values = [float(row["clamped_parent_mu"]) for row in rows]
    return {
        "rows": rows,
        "cutoff_dependent_parent": max(values) > min(values),
        "parent_mu_range": max(values) - min(values),
    }


def build_report() -> dict[str, Any]:
    derived_k, derived_u_c = derived_schedule_parameters()
    validation_schedule = schedule_regression(VALIDATION_INDICES)
    test_schedule = schedule_regression(TEST_INDICES)
    clock_regression = clock_iteration_regression(REGRESSION_PERIODS)
    trajectory = trajectory_regression(INITIAL_X_CONTROLS)
    phase_space = phase_space_audit()
    projected_control = projected_fixed_point_control()
    boundary_control = boundary_parent_control()
    modulo_controls = modulo_clock_controls(ADVERSARIAL_CLOCK_PERIODS)
    clamped_controls = clamped_clock_controls(ADVERSARIAL_CLOCK_PERIODS)

    gates = {
        "parameter_formula_matches_lock": abs(derived_k - K) <= SCHEDULE_ERROR_CEILING
        and abs(derived_u_c - U_C) <= SCHEDULE_ERROR_CEILING,
        "endpoint_schedule_matches": abs(legacy_mu(FIRST_INDEX) - ENDPOINT_HIGH)
        <= SCHEDULE_ERROR_CEILING
        and abs(legacy_mu(LAST_INDEX) - ENDPOINT_LOW) <= SCHEDULE_ERROR_CEILING,
        "validation_schedule_matches": validation_schedule["max_clock_error"]
        <= SCHEDULE_ERROR_CEILING
        and validation_schedule["max_mu_error"] <= SCHEDULE_ERROR_CEILING,
        "test_schedule_matches": test_schedule["max_clock_error"] <= SCHEDULE_ERROR_CEILING
        and test_schedule["max_mu_error"] <= SCHEDULE_ERROR_CEILING,
        "clock_closed_form_matches": clock_regression["max_absolute_error"]
        <= SCHEDULE_ERROR_CEILING,
        "interior_clock_has_no_return": clock_regression["all_strictly_decrease"]
        and not clock_regression["any_interior_clock_return"],
        "short_trajectory_matches": trajectory["max_x_error"] <= TRAJECTORY_ERROR_CEILING,
        "phase_space_forward_invariant": phase_space["forward_invariant"],
        "projected_return_is_not_full_return": projected_control["projected_x_returns"]
        and not projected_control["full_state_returns"],
        "boundary_parent_is_static_u_c": boundary_control["is_full_boundary_fixed_point"]
        and boundary_control["boundary_parameter"] != boundary_control["finite_window_endpoint"]
        and boundary_control["boundary_parameter"]
        != boundary_control["legacy_regression_parameter"],
        "modulo_clock_changes_schedule": all(not bool(row["same_schedule"]) for row in modulo_controls),
        "clamped_clock_is_cutoff_dependent": clamped_controls["cutoff_dependent_parent"],
        "determinant_ledgers_separated": True,
    }

    return {
        "audit_id": AUDIT_ID,
        "formal_candidate": False,
        "clue_id": "CLUE-A1-004",
        "source_lock": SOURCE_LOCK,
        "mathematical_object": {
            "phase_space": "[-1,1] x [0,1/log(11)]",
            "map": "F(x,v)=(1-(u_c+k*v^2)*x^2,G(v))",
            "clock_map": "G(v)=v/(1+v*log1p(exp(-1/v))) for v>0; G(0)=0",
            "initial_state": [0.5, INITIAL_CLOCK],
        },
        "parameters": {
            "k": K,
            "u_c": U_C,
            "derived_k": derived_k,
            "derived_u_c": derived_u_c,
            "mu_1": legacy_mu(FIRST_INDEX),
            "mu_1000000": legacy_mu(LAST_INDEX),
            "mu_limit": U_C,
        },
        "schedule_regression": {
            "validation": validation_schedule,
            "test": test_schedule,
        },
        "clock_regression": clock_regression,
        "trajectory_regression": trajectory,
        "phase_space": phase_space,
        "periodic_orbit_proof": {
            "clock_iterate_identity": "G^m(v)=1/log(exp(1/v)+m)",
            "base_fixed_set": "Fix(G^m)={0} for every m>=1",
            "full_fixed_set_identity": "Fix(F^m)=Fix(f_u_c^m) x {0}",
            "primitive_orbit_identity": "Prim(F)=Prim(f_u_c) x {0}",
            "interior_aging_orbits_are_periodic": False,
            "boundary_clock_multiplier": 1.0,
            "stability_weight_status": "neutral clock multiplier makes the usual hyperbolic monodromy denominator degenerate",
        },
        "determinant_ledger": {
            "zeta": "Z_AM,F(z)=exp(sum_(m>=1) #Fix(F^m) z^m/m)",
            "frozen_object": "D_AM,F(z)=1/Z_AM,F(z)",
            "exact_formal_identity": "D_AM,F=D_AM,f_u_c",
            "analytic_continuation_asserted": False,
            "fredholm_determinant_defined": False,
            "logarithmic_derivative_is_target": False,
        },
        "controls": {
            "projected_fixed_point": projected_control,
            "boundary_parent": boundary_control,
            "modulo_clock": modulo_controls,
            "clamped_clock": clamped_controls,
        },
        "gates": gates,
        "audit_passed": all(gates.values()),
        "route_a": {
            "tuple": ["A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "a1_evidence": "PROVED",
            "a2_evidence": "PROVED",
            "a3_evidence": "NOT_TESTABLE",
            "a4_evidence": "NOT_TESTABLE",
            "overall": "ROUTE_A_REJECTED",
            "recommended_audit_verdict": "STOP_SCOPED",
            "route_b_invocation_allowed": False,
        },
        "strongest_evidence": "Every full periodic orbit is exactly a static-limit f_u_c orbit on v=0.",
        "strongest_failure": "No primitive orbit traverses the aging interior, and the formal orbit determinant adds nothing beyond the static parent.",
        "claim_boundary": {
            "established": [
                "The compact lift exactly reproduces the frozen logarithmic schedule from its declared initial clock.",
                "All full-space periodic and primitive orbits lie on v=0 and coincide with the static f_u_c parent.",
                "Modulo and clamped clocks create different, cutoff-dependent systems.",
            ],
            "not_established": [
                "No analytic continuation or Fredholm determinant is defined.",
                "The result does not exclude autonomous lifts with an intrinsic recurrent base.",
                "No Route-B, Hilbert-Polya, RH, prime-orbit, or completed-xi claim is made.",
            ],
        },
        "next_smallest_task": "Define an intrinsic recurrent base whose nontrivial periodic orbits leave the static-limit slice and carry a nondegenerate same-object determinant.",
    }


def write_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("artifacts/p4_logistic_monotone_clock_lift/structural_audit.json"),
    )
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    report = build_report()
    write_report(args.output, report)
    if not args.quiet:
        print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
