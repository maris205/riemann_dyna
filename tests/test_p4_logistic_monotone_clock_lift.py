import math
from pathlib import Path
import unittest

import yaml

from experiments.p4_logistic_monotone_clock_lift import (
    ENDPOINT_HIGH,
    ENDPOINT_LOW,
    INITIAL_CLOCK,
    K,
    LAST_INDEX,
    U_C,
    boundary_parent_control,
    build_report,
    compact_clock_iterate_closed,
    compact_clock_iterate_direct,
    compact_clock_map,
    derived_schedule_parameters,
    legacy_clock,
    legacy_mu,
    modulo_clock_controls,
    phase_space_audit,
    projected_fixed_point_control,
)


class LogisticMonotoneClockLiftTests(unittest.TestCase):
    def test_source_lock_and_code_constants_match(self) -> None:
        lock_path = Path("configs/source_locks/P4-LOGISTIC-MONOTONE-CLOCK-LIFT.yaml")
        lock = yaml.safe_load(lock_path.read_text(encoding="utf-8"))
        parameters = lock["mathematical_object"]["schedule_parameters"]
        self.assertFalse(lock["formal_candidate"])
        self.assertEqual(lock["audit_id"], "P4-LOGISTIC-MONOTONE-CLOCK-LIFT")
        self.assertEqual(parameters["k_binary64"], K)
        self.assertEqual(parameters["u_c_binary64"], U_C)

    def test_endpoint_parameter_derivation(self) -> None:
        derived_k, derived_u_c = derived_schedule_parameters()
        self.assertAlmostEqual(derived_k, K, places=15)
        self.assertAlmostEqual(derived_u_c, U_C, places=15)
        self.assertAlmostEqual(legacy_mu(1), ENDPOINT_HIGH, places=14)
        self.assertAlmostEqual(legacy_mu(LAST_INDEX), ENDPOINT_LOW, places=14)

    def test_compact_clock_closed_form_iterate(self) -> None:
        for period in (1, 2, 3, 4, 8, 16, 32, 64):
            direct = compact_clock_iterate_direct(INITIAL_CLOCK, period)
            closed = compact_clock_iterate_closed(INITIAL_CLOCK, period)
            self.assertLessEqual(abs(direct - closed), 1.0e-14)

    def test_lift_reproduces_frozen_schedule(self) -> None:
        for index in (1, 2, 3, 8, 32, 1_000, 1_000_000):
            lifted_clock = compact_clock_iterate_closed(INITIAL_CLOCK, index - 1)
            self.assertLessEqual(abs(lifted_clock - legacy_clock(index)), 1.0e-14)
            self.assertLessEqual(abs(U_C + K * lifted_clock**2 - legacy_mu(index)), 1.0e-14)

    def test_clock_strictly_decreases_off_boundary(self) -> None:
        self.assertEqual(compact_clock_map(0.0), 0.0)
        for index in (1, 2, 3, 8, 32, 1_000, 1_000_000):
            clock = legacy_clock(index)
            self.assertLess(compact_clock_map(clock), clock)

    def test_phase_space_is_forward_invariant(self) -> None:
        audit = phase_space_audit()
        self.assertTrue(audit["forward_invariant"])
        self.assertGreaterEqual(audit["image_x_minimum"], -1.0)
        self.assertLessEqual(audit["image_x_maximum"], 1.0)

    def test_projected_x_return_is_not_full_state_return(self) -> None:
        control = projected_fixed_point_control()
        self.assertTrue(control["projected_x_returns"])
        self.assertFalse(control["full_state_returns"])
        self.assertGreater(control["clock_return_error"], 0.0)

    def test_boundary_orbits_use_static_limit_parent(self) -> None:
        control = boundary_parent_control()
        self.assertTrue(control["is_full_boundary_fixed_point"])
        self.assertEqual(control["boundary_parameter"], U_C)
        self.assertNotEqual(control["boundary_parameter"], ENDPOINT_LOW)
        self.assertNotEqual(control["boundary_parameter"], 1.543689)
        self.assertEqual(control["boundary_clock_multiplier"], 1.0)

    def test_periodicizing_clock_changes_schedule(self) -> None:
        controls = modulo_clock_controls((8, 32, 64))
        self.assertTrue(all(not row["same_schedule"] for row in controls))
        self.assertTrue(all(row["absolute_discrepancy"] > 0.0 for row in controls))

    def test_report_confirms_scoped_obstruction(self) -> None:
        report = build_report()
        self.assertTrue(report["audit_passed"])
        self.assertFalse(report["formal_candidate"])
        self.assertEqual(
            report["periodic_orbit_proof"]["full_fixed_set_identity"],
            "Fix(F^m)=Fix(f_u_c^m) x {0}",
        )
        self.assertEqual(report["determinant_ledger"]["exact_formal_identity"], "D_AM,F=D_AM,f_u_c")
        self.assertFalse(report["determinant_ledger"]["fredholm_determinant_defined"])
        self.assertEqual(report["route_a"]["recommended_audit_verdict"], "STOP_SCOPED")
        self.assertFalse(report["route_a"]["route_b_invocation_allowed"])

    def test_experiment_source_has_no_target_table_api(self) -> None:
        source = Path("experiments/p4_logistic_monotone_clock_lift.py").read_text(encoding="utf-8").lower()
        for forbidden in ("zetazero", "riemann_10k_true", "ustc_data", "loadtxt(", "numpy.load("):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
