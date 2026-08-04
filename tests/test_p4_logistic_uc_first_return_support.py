from decimal import Decimal, localcontext
import json
from pathlib import Path
import unittest

import yaml

from experiments import p4_logistic_uc_first_return_support as support


class LogisticUcFirstReturnSupportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = support.build_report()

    def test_algebraic_root_has_exact_rational_enclosure(self) -> None:
        certificate = self.report["rational_interval_certificate"]
        self.assertTrue(certificate["polynomial_negative_at_lower"])
        self.assertTrue(certificate["polynomial_positive_at_upper"])
        self.assertLess(support.critical_polynomial(support.U_LOWER), 0)
        self.assertGreater(support.critical_polynomial(support.U_UPPER), 0)
        self.assertGreater(support.U_LOWER, support.Fraction(3, 2))
        self.assertLess(support.U_UPPER, support.Fraction(2))
        self.assertEqual(
            support.U_UPPER - support.U_LOWER,
            support.fraction_from_decimal("0." + "0" * 99 + "1"),
        )

    def test_outward_rational_square_root_bounds(self) -> None:
        lower = support.sqrt_floor_fraction(support.Fraction(2))
        upper = support.sqrt_ceil_fraction(support.Fraction(2))
        self.assertLessEqual(lower * lower, 2)
        self.assertGreaterEqual(upper * upper, 2)
        self.assertLess(lower, upper)

        exact_lower = support.sqrt_floor_fraction(support.Fraction(1, 4))
        exact_upper = support.sqrt_ceil_fraction(support.Fraction(1, 4))
        self.assertEqual(exact_lower, support.Fraction(1, 2))
        self.assertEqual(exact_upper, support.Fraction(1, 2))

    def test_154_endpoint_intervals_are_strictly_certified(self) -> None:
        certificate = self.report["rational_interval_certificate"]
        self.assertEqual(certificate["certified_branch_count"], 154)
        self.assertEqual(certificate["maximum_certified_physical_return"], 308)
        self.assertTrue(certificate["all_endpoint_intervals_strictly_separated"])
        self.assertTrue(certificate["all_endpoint_intervals_below_rho"])
        self.assertEqual(len(certificate["endpoint_rows"]), 154)
        for row in certificate["endpoint_rows"]:
            self.assertTrue(row["strictly_above_previous"])
            self.assertTrue(row["strictly_below_rho"])

    def test_exact_band_swap_identities(self) -> None:
        diagnostic = self.report["high_precision_diagnostics"]
        for residual in diagnostic["band_identity_residuals"].values():
            self.assertLess(Decimal(residual), Decimal("1e-170"))
        self.assertEqual(
            self.report["exact_theorem"]["band_swap"],
            ["f([-rho,rho])=[rho,1]", "f([rho,1])=[-rho,rho]"],
        )

    def test_report_encodes_branch_theorem_and_midpoint_diagnostics(self) -> None:
        theorem = self.report["exact_theorem"]["physical_branches"]
        self.assertEqual(theorem["topological_support"], "2*N_{>=1}")
        self.assertEqual(theorem["C_odd"], "empty")
        self.assertEqual(
            theorem["branch_multiplicity"],
            "exactly one nondegenerate interval per even label",
        )
        self.assertIn("diffeomorphism", theorem["full_branch_map"])
        self.assertIn("every finite word", theorem["finite_return_word_cylinders"])
        diagnostic = self.report["high_precision_diagnostics"]
        self.assertTrue(diagnostic["core_midpoint_first_returns_pass"])
        for row in diagnostic["core_branch_rows"]:
            self.assertEqual(row["midpoint_first_return"], row["return_time"])
            self.assertGreater(Decimal(row["length"]), 0)

    def test_endpoint_recursion_is_the_positive_inverse_of_f_squared(self) -> None:
        with localcontext() as context:
            context.prec = support.HIGH_PRECISION_DIGITS
            u = support.decimal_root()
            endpoint = Decimal(0)
            for _ in range(12):
                next_endpoint = support.decimal_positive_t_inverse(endpoint, u)
                self.assertLess(
                    abs(support.decimal_t(next_endpoint, u) - endpoint),
                    Decimal("1e-170"),
                )
                self.assertGreater(next_endpoint, endpoint)
                endpoint = next_endpoint

    def test_ambient_domain_has_all_odd_transient_branches(self) -> None:
        theorem = self.report["exact_theorem"]["ambient_branches"]
        self.assertEqual(theorem["topological_support"], "N_{>=1}")
        self.assertEqual(theorem["transient_odd_union"], "[-1,-rho)")
        diagnostic = self.report["high_precision_diagnostics"]
        self.assertTrue(diagnostic["ambient_midpoint_first_returns_pass"])
        observed = [
            row["midpoint_first_return"]
            for row in diagnostic["ambient_odd_branch_rows"]
        ]
        self.assertEqual(observed[:6], [1, 3, 5, 7, 9, 11])

    def test_zero_is_a_non_event_and_endpoints_are_half_open(self) -> None:
        self.assertEqual(
            self.report["mathematical_object"]["zero_convention"],
            "x=0 is not an L event",
        )
        rows = self.report["high_precision_diagnostics"]["core_branch_rows"]
        self.assertFalse(rows[0]["upper_closed"])
        self.assertTrue(all(row["upper_closed"] for row in rows[1:]))

    def test_invariant_weight_claims_are_domain_and_measure_scoped(self) -> None:
        ledger = self.report["invariant_weight_ledger"]
        self.assertEqual(
            ledger["all_invariant_probabilities"]["mass_of_X_minus_J"], 0
        )
        self.assertEqual(
            ledger["all_invariant_probabilities"][
                "mass_of_every_ambient_odd_branch"
            ],
            0,
        )
        self.assertEqual(
            ledger["physical_acip_with_support_J"][
                "mass_of_every_physical_even_branch"
            ],
            "strictly_positive",
        )
        self.assertFalse(ledger["measure_independence"])

    def test_period_two_measure_witness_closes(self) -> None:
        witness = self.report["high_precision_diagnostics"][
            "period_two_measure_witness"
        ]
        self.assertLess(
            Decimal(witness["f_negative_to_positive_residual"]),
            Decimal("1e-170"),
        )
        self.assertLess(
            Decimal(witness["f_positive_to_negative_residual"]),
            Decimal("1e-170"),
        )
        self.assertLess(Decimal(witness["negative_point"]), 0)
        self.assertGreater(Decimal(witness["positive_point"]), 0)
        ledger = self.report["invariant_weight_ledger"]["counterexamples"][
            "period_two_orbit_measure"
        ]
        self.assertEqual(ledger["mass_of_C_2"], "1/2")
        self.assertEqual(ledger["mass_of_C_2n_for_n_at_least_2"], 0)
        self.assertEqual(ledger["conditional_return_support_on_L"], "C_2 only")

    def test_unaccelerated_first_return_is_not_uniformly_expanding(self) -> None:
        correction = self.report["prior_work_correction"][
            "paper_2_induced_uniform_expansion"
        ]
        counterexample = correction["counterexample"]
        self.assertEqual(counterexample["x"], "-0.01")
        self.assertEqual(counterexample["first_negative_return"], 2)
        self.assertTrue(counterexample["strictly_below_one"])
        self.assertLess(Decimal(counterexample["absolute_first_return_derivative"]), 1)
        self.assertEqual(
            correction["all_branch_infimum"],
            "inf_(C_2n) |(f^(2n))'| = 0 for every n>=1",
        )
        self.assertFalse(correction["ordinary_bv_markov_argument_ready"])

    def test_historical_support_artifact_keeps_then_open_weight_clue(self) -> None:
        # The versioned support artifact predates the separate density theorem
        # and remains byte-stable as historical evidence.
        clue = self.report["open_weight_clue"]
        self.assertEqual(clue["status"], "OPEN_CONDITIONAL_CLUE")
        self.assertEqual(clue["endpoint_length_ratio_status"], "PROVED")
        self.assertEqual(clue["mass_ratio_status"], "OPEN_CONDITIONAL_CLUE")
        self.assertIn("C*t^(-1/2)*(1+o(1))", clue["required_density_hypothesis"])
        self.assertAlmostEqual(
            float(clue["endpoint_length_ratio_limit"]), 0.3549108444, places=9
        )
        self.assertAlmostEqual(
            float(clue["conditional_square_root_mass_ratio"]),
            0.5957439420,
            places=9,
        )

    def test_source_lock_matches_implementation(self) -> None:
        lock = yaml.safe_load(Path(support.SOURCE_LOCK).read_text(encoding="utf-8"))
        self.assertEqual(lock["audit_id"], support.AUDIT_ID)
        self.assertEqual(lock["parent_audit_id"], support.PARENT_AUDIT_ID)
        self.assertEqual(lock["lock_version"], 1)
        self.assertEqual(
            lock["cutoff"]["exact_rational_endpoint_certificate"],
            support.RATIONAL_CERTIFIED_BRANCHES,
        )
        self.assertEqual(
            lock["precision"]["rational_sqrt_scale_digits"],
            support.RATIONAL_SQRT_SCALE_DIGITS,
        )
        self.assertEqual(lock["precision"]["rational_u_lower"], support.U_LOWER_TEXT)
        self.assertEqual(lock["precision"]["rational_u_upper"], support.U_UPPER_TEXT)
        self.assertEqual(
            lock["cutoff"]["high_precision_midpoint_diagnostic_branches"],
            support.HIGH_PRECISION_DIAGNOSTIC_BRANCHES,
        )
        self.assertEqual(
            lock["cutoff"]["reported_endpoint_rows"],
            support.REPORTED_ENDPOINT_ROWS,
        )
        self.assertEqual(
            lock["precision"]["high_precision_decimal_digits"],
            support.HIGH_PRECISION_DIGITS,
        )
        self.assertEqual(
            Decimal(str(lock["precision"]["derivative_counterexample_x"])),
            support.DERIVATIVE_COUNTEREXAMPLE_X,
        )
        self.assertIn(
            "C*t^(-1/2)*(1+o(1))", lock["open_mass_ratio_hypothesis"]
        )

    def test_saved_artifact_is_byte_reproducible(self) -> None:
        expected = json.dumps(self.report, indent=2, sort_keys=True) + "\n"
        actual = Path(
            "artifacts/p4_logistic_uc_first_return_support/structural_audit.json"
        ).read_text(encoding="utf-8")
        self.assertEqual(actual, expected)

    def test_source_has_no_target_lookup(self) -> None:
        source = Path(
            "experiments/p4_logistic_uc_first_return_support.py"
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

    def test_route_a_scope_remains_exploratory(self) -> None:
        self.assertTrue(self.report["audit_passed"])
        self.assertTrue(all(self.report["computational_gates"].values()))
        self.assertIn(
            "critical_polynomial_changes_sign_on_rational_bracket",
            self.report["computational_gates"],
        )
        self.assertNotIn(
            "algebraic_u_c_is_rationally_isolated",
            self.report["computational_gates"],
        )
        self.assertNotIn("physical_odd_return_sets_are_empty", self.report["computational_gates"])
        self.assertEqual(
            self.report["formal_evidence"][
                "physical_support_and_unique_branches"
            ]["status"],
            "PROVED",
        )
        self.assertFalse(
            self.report["formal_evidence"][
                "physical_support_and_unique_branches"
            ]["executable_gate"]
        )
        route = self.report["route_a_update"]
        self.assertEqual(
            route["tuple"], ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
        )
        self.assertEqual(route["overall_verdict"], "ROUTE_A_EXPLORATORY")
        self.assertEqual(route["recommended_audit_verdict"], "REVISE")
        self.assertFalse(route["route_b_invocation_allowed"])


if __name__ == "__main__":
    unittest.main()
