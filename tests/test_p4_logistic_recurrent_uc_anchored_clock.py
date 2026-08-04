import math
from pathlib import Path
import unittest

import yaml

from experiments import p4_logistic_recurrent_uc_anchored_clock as recurrent


class LogisticRecurrentUcAnchoredClockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = recurrent.build_report()

    def test_exact_algebraic_uc_and_critical_orbit(self) -> None:
        audit = self.report["critical_parent"]
        self.assertEqual(recurrent.U_C.hex(), "0x1.8b2f3400b4fdcp+0")
        self.assertLessEqual(
            abs(recurrent.critical_polynomial(recurrent.U_C)),
            recurrent.POLYNOMIAL_RESIDUAL_CEILING,
        )
        self.assertEqual(audit["derivative_discriminant"], -8.0)
        self.assertTrue(audit["derivative_strictly_positive"])
        self.assertEqual(
            audit["critical_orbit"],
            [
                0.0,
                1.0,
                1.0 - recurrent.U_C,
                recurrent.U_C - 1.0,
                recurrent.U_C - 1.0,
            ],
        )
        self.assertEqual(audit["landing_residual"], 0.0)
        self.assertEqual(audit["fixed_point_residual"], 0.0)

    def test_rounded_literal_is_only_a_failed_anchor_control(self) -> None:
        audit = self.report["critical_parent"]
        self.assertLess(recurrent.LEGACY_ROUNDED_U_C, recurrent.U_C)
        self.assertAlmostEqual(
            audit["legacy_rounding_error"],
            recurrent.LEGACY_ROUNDED_U_C - recurrent.U_C,
            places=22,
        )
        rounded_schedule = recurrent.block_schedule(
            2, u_c=recurrent.LEGACY_ROUNDED_U_C
        )
        self.assertEqual(rounded_schedule[-1], recurrent.LEGACY_ROUNDED_U_C)
        self.assertNotEqual(rounded_schedule[-1], recurrent.U_C)
        control = self.report["controls"]["simpler_parent_and_neighbor_parameters"]
        self.assertTrue(control["rounded_terminal_equals_rounded_value"])
        self.assertTrue(control["rounded_terminal_misses_algebraic_u_c"])

    def test_critical_seed_x0_zero_has_one_left_hit_and_no_gap(self) -> None:
        control = recurrent.critical_seed_gap_control(16)
        self.assertEqual(control["initial_x"], 0.0)
        self.assertEqual(control["l_hit_positions_one_based"], [2])
        self.assertEqual(control["gaps"], [])
        self.assertTrue(control["exactly_one_l_hit"])
        self.assertEqual(control["gap_count"], 0)
        self.assertTrue(control["generic_initial_state_required_for_gap_statistics"])

    def test_even_block_length_and_terminal_bitwise_uc_contract(self) -> None:
        for length in recurrent.VALIDATION_GAP_LENGTHS + recurrent.TEST_GAP_LENGTHS:
            schedule = recurrent.block_schedule(length)
            self.assertEqual(len(schedule), length)
            self.assertTrue(all(value > recurrent.U_C for value in schedule[:-1]))
            self.assertTrue(
                all(right < left for left, right in zip(schedule, schedule[1:]))
            )
            self.assertEqual(schedule[-1], recurrent.U_C)
            self.assertEqual(schedule[-1].hex(), recurrent.U_C.hex())
        with self.assertRaises(ValueError):
            recurrent.block_schedule(3)
        with self.assertRaises(ValueError):
            recurrent.block_mu(0, 2)

    def test_terminal_update_occurs_before_tower_renewal(self) -> None:
        trace = recurrent.tower_ordering_trace((1, 2))
        self.assertEqual(len(trace), 6)
        self.assertEqual(
            [(row["return_symbol"], row["gap_length"]) for row in trace],
            [(1, 2), (1, 2), (2, 4), (2, 4), (2, 4), (2, 4)],
        )
        self.assertFalse(trace[0]["terminal_update"])
        self.assertEqual((trace[0]["next_block_index"], trace[0]["next_age"]), (0, 2))
        self.assertTrue(trace[1]["terminal_update"])
        self.assertEqual(trace[1]["parameter"], recurrent.U_C)
        self.assertEqual((trace[1]["next_block_index"], trace[1]["next_age"]), (1, 1))
        self.assertTrue(trace[-1]["terminal_update"])
        self.assertEqual(trace[-1]["parameter"], recurrent.U_C)
        self.assertEqual((trace[-1]["next_block_index"], trace[-1]["next_age"]), (0, 1))

    def test_left_center_and_rounded_channels_are_even_but_right_opens_odd(self) -> None:
        boundary = self.report["gap_phase_boundary"]
        self.assertEqual(
            boundary["gates"],
            {
                "center_odd_gap_mass_is_zero": True,
                "left_controls_remain_even": True,
                "right_controls_open_odd_gap_channel": True,
                "rounded_legacy_value_remains_on_even_left_side": True,
            },
        )
        for row in boundary["rows"]:
            self.assertEqual(row["center"]["odd_gap_count"], 0)
            self.assertEqual(row["legacy_rounded"]["odd_gap_count"], 0)
            for control in row["controls"]:
                self.assertEqual(control["left"]["odd_gap_count"], 0)
                self.assertGreater(control["right"]["odd_gap_count"], 0)

    def test_tower_fixed_counts_follow_the_even_length_zeta(self) -> None:
        for period in range(1, 17):
            if period % 2:
                expected = 0
            else:
                half_period = period // 2
                expected = 2 * (2**half_period - 1)
                # log((1-z^2)/(1-2*z^2)) has coefficient
                # (2^r-1)/r at z^(2r), hence Fix(G^(2r))=2*(2^r-1).
                logarithm_coefficient = (2**half_period - 1) / half_period
                self.assertEqual(logarithm_coefficient * period, expected)
            self.assertEqual(recurrent.tower_fixed_count(period), expected)
        self.assertEqual(
            self.report["tower_primitive_census"]["tower_zeta"],
            "Z_T(z)=(1-z^2)/(1-2*z^2)",
        )

    def test_mobius_primitive_counts_match_exact_enumeration(self) -> None:
        expected = {
            1: 0,
            2: 1,
            3: 0,
            4: 1,
            5: 0,
            6: 2,
            7: 0,
            8: 3,
            9: 0,
            10: 6,
            11: 0,
            12: 9,
            13: 0,
            14: 18,
            15: 0,
            16: 30,
        }
        census = self.report["tower_primitive_census"]
        self.assertTrue(census["all_enumerations_match"])
        for row in census["rows"]:
            period = row["period"]
            self.assertEqual(row["primitive_orbit_count_formula"], expected[period])
            self.assertEqual(row["primitive_orbit_count_enumerated"], expected[period])
            self.assertEqual(
                recurrent.tower_primitive_orbit_count(period), expected[period]
            )

    def test_repetitions_and_cyclic_rotations_are_not_new_primitive_orbits(self) -> None:
        self.assertEqual(recurrent.canonical_rotation((2, 1)), (1, 2))
        self.assertEqual(recurrent.canonical_rotation((3, 1, 1)), (1, 1, 3))
        self.assertFalse(recurrent.is_primitive_word((1, 2, 1, 2)))
        self.assertFalse(recurrent.is_primitive_word((2, 2)))
        self.assertTrue(recurrent.is_primitive_word((1, 2)))
        self.assertEqual(recurrent.primitive_return_words(6), [(1, 2), (3,)])
        self.assertEqual(
            recurrent.primitive_return_words(8),
            [(1, 1, 2), (1, 3), (4,)],
        )
        self.assertEqual(recurrent.primitive_return_words(7), [])

    def test_full_fibre_witnesses_close_and_keep_signed_multipliers(self) -> None:
        witnesses = self.report["full_fibre_witnesses"]
        self.assertEqual(witnesses["witness_count"], 70)
        self.assertLessEqual(
            witnesses["maximum_return_residual"],
            recurrent.FIXED_POINT_RESIDUAL_CEILING,
        )
        self.assertTrue(witnesses["all_terminal_parameters_bitwise_u_c"])
        self.assertTrue(witnesses["all_full_periods_certified_by_projection"])
        self.assertIn("not a full root census", witnesses["fibre_root_completeness"])
        for row in witnesses["rows"]:
            self.assertEqual(len(recurrent.expand_return_word(row["return_word"])), row["period"])
            self.assertLessEqual(
                row["return_residual"], recurrent.FIXED_POINT_RESIDUAL_CEILING
            )
            self.assertLess(row["signed_multiplier"], 0.0)
            self.assertEqual(row["orientation"], "reversing")
            self.assertEqual(row["phase_label"], "pi")
            self.assertTrue(row["terminal_parameters_bitwise_u_c"])

    def test_signed_multiplier_repetition_is_multiplicative_not_absolute(self) -> None:
        control = recurrent.repetition_control()
        primitive = control["primitive_signed_multiplier"]
        repeated = control["repeated_signed_multiplier"]
        self.assertLess(primitive, 0.0)
        self.assertGreater(repeated, 0.0)
        self.assertAlmostEqual(repeated, primitive**2, places=11)
        self.assertLessEqual(
            control["multiplier_relative_error"],
            recurrent.REPEATED_ORBIT_RESIDUAL_CEILING,
        )
        self.assertFalse(control["repeated_word_is_new_primitive_base_orbit"])

    def test_full_fixed_count_bounds_are_finite(self) -> None:
        ledger = self.report["fixed_count_and_determinant_ledger"]
        for row in ledger["rows"]:
            period = row["period"]
            base = recurrent.tower_fixed_count(period)
            self.assertEqual(row["tower_fixed_count"], base)
            self.assertEqual(row["full_fixed_count_lower_bound"], base)
            self.assertEqual(row["full_fixed_count_upper_bound"], (2**period) * base)
            self.assertLessEqual(
                row["full_fixed_count_upper_bound"], row["coarse_four_power_bound"]
            )

    def test_tower_zeta_and_full_determinant_ledgers_are_separate(self) -> None:
        ledger = self.report["fixed_count_and_determinant_ledger"]
        self.assertEqual(ledger["tower_zeta"], "Z_T(z)=(1-z^2)/(1-2*z^2)")
        self.assertEqual(
            ledger["full_determinant"],
            "D_AM,F(z)=exp(-sum_(n>=1) Fix(F^n)*z^n/n)",
        )
        self.assertTrue(ledger["base_and_full_ledgers_are_distinct"])
        self.assertFalse(ledger["fredholm_determinant_defined"])
        self.assertEqual(ledger["proved_log_series_disk"], "|z|<1/4")
        self.assertFalse(ledger["unit_lattice_completed_xi_candidate"])

    def test_source_lock_constants_and_conventions_match_code(self) -> None:
        lock_path = Path(
            "configs/source_locks/P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK.yaml"
        )
        lock = yaml.safe_load(lock_path.read_text(encoding="utf-8"))
        parameters = lock["mathematical_object"]["parameters"]
        self.assertEqual(lock["lock_version"], 3)
        self.assertFalse(lock["formal_candidate"])
        self.assertEqual(lock["audit_id"], recurrent.AUDIT_ID)
        self.assertEqual(parameters["u_c_binary64"], recurrent.U_C)
        self.assertEqual(parameters["legacy_rounded_u_c"], recurrent.LEGACY_ROUNDED_U_C)
        self.assertEqual(parameters["k"], recurrent.K)
        self.assertEqual(parameters["offset"], recurrent.OFFSET)
        self.assertEqual(parameters["minimum_return_symbol"], 1)
        self.assertEqual(parameters["minimum_gap_length"], 2)
        self.assertEqual(
            lock["cutoff"]["validation_gap_lengths"],
            list(recurrent.VALIDATION_GAP_LENGTHS),
        )
        self.assertEqual(
            lock["cutoff"]["test_gap_lengths"], list(recurrent.TEST_GAP_LENGTHS)
        )
        self.assertEqual(
            lock["cutoff"]["validation_periods"], list(recurrent.VALIDATION_PERIODS)
        )
        self.assertEqual(lock["cutoff"]["test_periods"], list(recurrent.TEST_PERIODS))
        self.assertIn(
            "(1-z^2)/(1-2*z^2)", lock["determinant_convention"]["tower_zeta"]
        )
        self.assertIn(
            "D_AM,F", lock["determinant_convention"]["frozen_full_object"]
        )
        self.assertIn(
            "physical event",
            lock["mathematical_object"]["event_and_gap"],
        )
        self.assertIn(
            "tau_J(-rho)=infinity",
            lock["mathematical_object"]["event_and_gap"],
        )
        self.assertTrue(
            any(
                "post-burn-in physical-core" in condition
                for condition in lock["stopping_conditions"]
            )
        )

    def test_experiment_has_no_prime_or_zero_lookup(self) -> None:
        source = Path(
            "experiments/p4_logistic_recurrent_uc_anchored_clock.py"
        ).read_text(encoding="utf-8").lower()
        for forbidden in (
            "zetazero",
            "riemann_10k_true",
            "ustc_data",
            "isprime",
            "prime_table",
            "primality",
            "loadtxt(",
            "numpy.load(",
            "np.load(",
        ):
            self.assertNotIn(forbidden, source)

    def test_report_keeps_the_route_a_claim_boundary_scoped(self) -> None:
        self.assertTrue(self.report["audit_passed"])
        self.assertFalse(self.report["formal_candidate"])
        self.assertEqual(
            self.report["route_a"]["tuple"],
            ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        )
        self.assertEqual(
            self.report["route_a"]["overall_verdict"], "ROUTE_A_EXPLORATORY"
        )
        self.assertEqual(
            self.report["route_a"]["recommended_audit_verdict"], "REVISE"
        )
        self.assertFalse(self.report["route_a"]["route_b_invocation_allowed"])
        ambient_claim = next(
            claim
            for claim in self.report["claim_boundary"]["established"]
            if "ambient [-1,1] support" in claim
        )
        self.assertIn("topologically nonempty", ambient_claim)
        self.assertIn("zero invariant mass", ambient_claim)


if __name__ == "__main__":
    unittest.main()
