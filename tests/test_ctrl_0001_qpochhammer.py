import hashlib
import math
from pathlib import Path
import unittest

import numpy as np
import yaml

from experiments.ctrl_0001_qpochhammer import (
    CHANNELS,
    COEFFICIENT_CUTOFFS,
    COEFFICIENT_GUARD,
    CONTOUR_POINTS_PER_EDGE,
    MODE_CUTOFFS,
    MATCH_RADIUS,
    PHASE_STEP_MAX,
    PRIMARY_COEFFICIENT_CUTOFF,
    PRIMARY_MODE_CUTOFF,
    build_report,
    cancellation_diagnostic,
    coefficient_comparison,
    direct_determinant,
    direct_logarithmic_derivative,
    exact_scoring_ledger,
    fredholm_coefficients,
    root_region_counts,
    truncated_log_exponential,
)


class QPochhammerPositiveControlTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = build_report()

    def test_exact_scoring_divisor_is_frozen_and_clear_of_boundaries(self) -> None:
        ledger = exact_scoring_ledger()
        roots = [complex(row["root"]) for row in ledger]
        self.assertEqual(
            root_region_counts(roots),
            {
                "total": 22,
                "validation_core": 12,
                "test_upper": 5,
                "test_lower": 5,
            },
        )
        self.assertAlmostEqual(
            self.report["truth_scoring_ledger"]["minimum_boundary_clearance"],
            0.07,
            places=12,
        )
        self.assertTrue(self.report["truth_scoring_ledger"]["opened_after_discovery"])
        self.assertFalse(
            self.report["coefficient_root_discovery"]["exact_roots_used_as_seeds"]
        )

    def test_two_coefficient_constructions_agree_and_preserve_conjugation(self) -> None:
        comparison = coefficient_comparison()
        self.assertLess(
            comparison["max_scaled_q_binomial_vs_trace_defect"], 1.0e-9
        )
        self.assertLess(
            comparison["max_nominal_coefficient_conjugation_defect_through_k32"],
            5.0e-12,
        )
        coefficients = fredholm_coefficients(COEFFICIENT_GUARD)
        self.assertEqual(len(coefficients), COEFFICIENT_GUARD + 1)

    def test_direct_product_and_coefficient_value_paths_agree(self) -> None:
        coefficients = fredholm_coefficients(COEFFICIENT_GUARD)
        for s in (0.2 + 0.4j, -0.1 + 2.0j, 0.4 - 1.0j):
            z = np.exp(-s)
            polynomial_value = np.sum(coefficients * z ** np.arange(len(coefficients)))
            product_value = direct_determinant(s, 48)
            relative_error = abs(polynomial_value - product_value) / abs(product_value)
            self.assertLess(relative_error, 5.0e-8)

    def test_coefficient_cutoffs_expose_instability_before_passing(self) -> None:
        rows = {
            row["coefficient_cutoff"]: row
            for row in self.report["coefficient_root_discovery"]["cutoff_diagnostics"]
        }
        self.assertEqual((rows[16]["roots_found"], rows[16]["matched_within_radius"]), (28, 6))
        self.assertEqual((rows[16]["missing_count"], rows[16]["extra_count"]), (16, 22))
        self.assertAlmostEqual(rows[16]["max_root_error"], 0.135492020213, places=10)
        self.assertEqual((rows[20]["roots_found"], rows[20]["matched_within_radius"]), (22, 15))
        self.assertGreater(rows[20]["max_root_error"], MATCH_RADIUS)
        for cutoff in (24, 28, 32):
            self.assertEqual((rows[cutoff]["missing_count"], rows[cutoff]["extra_count"]), (0, 0))
        self.assertLessEqual(rows[24]["max_root_error"], 5.0e-5)
        self.assertLessEqual(rows[28]["max_root_error"], 1.0e-6)
        self.assertLessEqual(rows[32]["max_root_error"], 1.0e-8)
        self.assertLessEqual(
            self.report["coefficient_root_discovery"]["max_branch_drift_k24_to_k28"],
            2.0e-5,
        )

    def test_argument_principle_requires_the_fine_phase_gate(self) -> None:
        rows = {
            row["points_per_edge"]: row
            for row in self.report["direct_product_argument_principle"]["grid_diagnostics"]
        }
        self.assertEqual([rows[size]["count"] for size in (128, 256, 512, 1024)], [22] * 4)
        self.assertGreaterEqual(rows[128]["max_adjacent_phase_increment"], PHASE_STEP_MAX)
        self.assertGreaterEqual(rows[256]["max_adjacent_phase_increment"], PHASE_STEP_MAX)
        self.assertLess(rows[512]["max_adjacent_phase_increment"], PHASE_STEP_MAX)
        self.assertLess(rows[1024]["max_adjacent_phase_increment"], PHASE_STEP_MAX)
        self.assertLess(rows[1024]["integer_residual"], 1.0e-8)
        self.assertFalse(
            self.report["direct_product_argument_principle"]["polynomial_roots_used"]
        )
        self.assertEqual(
            self.report["direct_product_argument_principle"]["evidence_status"],
            "NUMERICAL_OBSERVATION",
        )
        self.assertIn(
            "not an interval-arithmetic",
            self.report["direct_product_argument_principle"]["rigor_boundary"],
        )

    def test_mode_cutoffs_separate_count_stability_from_value_stability(self) -> None:
        rows = {
            row["mode_cutoff"]: row
            for row in self.report["mode_cutoff_diagnostics"]["rows"]
        }
        self.assertEqual(rows[2]["count"], 18)
        self.assertTrue(all(rows[cutoff]["count"] == 22 for cutoff in (3, 8, 16, 24, 32, 40, 48)))
        self.assertLessEqual(
            self.report["mode_cutoff_diagnostics"][
                "max_relative_contour_drift_n40_to_n48"
            ],
            2.0e-6,
        )
        self.assertTrue(
            self.report["mode_cutoff_diagnostics"][
                "root_count_stabilizes_before_determinant_values"
            ]
        )

    def test_fault_injections_detect_identity_not_just_count(self) -> None:
        faults = self.report["fault_injections"]
        self.assertTrue(
            all(fault["winding_quality_gate_passed"] for fault in faults.values())
        )
        self.assertEqual(
            faults["missing_only"]["winding_counts"],
            {"total": 18, "validation_core": 10, "test_upper": 4, "test_lower": 4},
        )
        self.assertEqual(
            (
                faults["missing_only"]["nominal_truth_matching"]["missing_count"],
                faults["missing_only"]["nominal_truth_matching"]["extra_count"],
            ),
            (4, 0),
        )
        self.assertEqual(
            faults["extra_only"]["winding_counts"],
            {"total": 26, "validation_core": 14, "test_upper": 6, "test_lower": 6},
        )
        self.assertEqual(
            (
                faults["extra_only"]["nominal_truth_matching"]["missing_count"],
                faults["extra_only"]["nominal_truth_matching"]["extra_count"],
            ),
            (0, 4),
        )
        self.assertEqual(
            faults["balanced"]["winding_counts"],
            {"total": 22, "validation_core": 12, "test_upper": 5, "test_lower": 5},
        )
        self.assertEqual(
            (
                faults["balanced"]["nominal_truth_matching"]["missing_count"],
                faults["balanced"]["nominal_truth_matching"]["extra_count"],
            ),
            (4, 4),
        )

    def test_absolute_values_are_a_failed_determinant_ablation(self) -> None:
        ablation = self.report["fault_injections"]["absolute_value"]
        self.assertEqual(ablation["winding_counts"]["total"], 30)
        self.assertFalse(ablation["valid_nominal_substitute"])
        self.assertIn("changes the determinant", ablation["failure_reason"])

    def test_signed_trace_cancellation_is_not_replaced_by_absolute_bounds(self) -> None:
        cancellation = cancellation_diagnostic(4)
        self.assertAlmostEqual(
            cancellation["signed_trace"]["real"], -0.33393858995368, places=12
        )
        self.assertAlmostEqual(
            cancellation["sum_of_absolute_channel_terms"], 33.59028440713513, places=11
        )
        self.assertLess(cancellation["cancellation_ratio"], 0.02)
        self.assertTrue(cancellation["signed_real_part_is_negative"])

    def test_report_keeps_determinant_ledgers_and_scope_separate(self) -> None:
        ledger = self.report["determinant_ledger"]
        self.assertIn("det_Fr(I-L_s)", ledger["frozen"])
        self.assertIn("separate pole ledger", ledger["reciprocal"])
        self.assertIn("separate meromorphic ledger", ledger["logarithmic_derivative"])
        self.assertIn("zero-free", ledger["truncated_log_exponential"])
        self.assertTrue(self.report["all_frozen_gates_pass"])
        self.assertEqual(self.report["control_verdict"], "GO_WITH_LIMITATIONS")
        self.assertEqual(self.report["candidate_scope_verdict"], "STOP_SCOPED")
        self.assertEqual(
            self.report["route_a_tuple"],
            [
                "A1_WEAK",
                "A2_ANALYTIC_DETERMINANT",
                "A3_PARTIAL_ANALYTIC_STRUCTURE",
                "A4_FAIL",
            ],
        )
        self.assertFalse(self.report["formal_candidate"])
        self.assertFalse(self.report["uses_prime_table"])
        self.assertFalse(self.report["uses_zero_table"])
        self.assertEqual(
            self.report["candidate_route_a_tuple"],
            ["A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        )

    def test_executable_ledger_controls_have_distinct_divisor_behavior(self) -> None:
        controls = self.report["determinant_ledger_controls"]
        self.assertEqual(controls["nominal_D_winding"], 22)
        self.assertEqual(controls["reciprocal_1_over_D"]["winding"]["count"], -22)
        self.assertIn("poles", controls["reciprocal_1_over_D"]["interpretation"])
        residue = controls["logarithmic_derivative_D_prime_over_D"][
            "scaled_residue_probe"
        ]
        self.assertLess(abs(complex(residue["real"], residue["imag"]) - 1), 1.0e-5)
        for row in controls["logarithmic_derivative_D_prime_over_D"][
            "contour_integrals"
        ]:
            self.assertEqual(row["nearest_integer"], 22)
            self.assertLess(row["distance_to_nearest_integer"], 1.0e-4)
        self.assertEqual(
            controls["truncated_log_exponential"]["winding"]["count"], 0
        )
        self.assertTrue(
            controls["truncated_log_exponential"]["analytically_zero_free"]
        )
        self.assertFalse(controls["ledgers_combined"])

        root = 11 / 20 + 1j * math.pi / 3
        offset = 1.0e-6
        residue_probe = offset * direct_logarithmic_derivative(root + offset, 48)
        self.assertLess(abs(residue_probe - 1), 1.0e-5)
        self.assertNotEqual(truncated_log_exponential(0.2 + 0.4j, 4), 0)

    def test_supplemental_high_precision_audit_reports_root_drift(self) -> None:
        audit = self.report["supplemental_precision_audit"]
        self.assertEqual(audit["coefficient_cutoff"], 28)
        self.assertEqual(audit["decimal_digits"], [50, 80, 120])
        self.assertEqual(audit["root_counts"], {"50": 22, "80": 22, "120": 22})
        self.assertLess(float(audit["max_root_drift_dps50_to_dps80"]), 1.0e-40)
        self.assertLess(float(audit["max_root_drift_dps80_to_dps120"]), 1.0e-70)
        self.assertLess(audit["max_root_drift_complex128_to_dps120"], 1.0e-10)

    def test_primary_k28_errors_are_reported_by_holdout_region(self) -> None:
        regions = self.report["coefficient_root_discovery"][
            "primary_k28_regional_scoring"
        ]
        self.assertEqual(
            {name: row["expected_count"] for name, row in regions.items()},
            {"validation_core": 12, "test_upper": 5, "test_lower": 5},
        )
        for row in regions.values():
            self.assertEqual((row["missing_count"], row["extra_count"]), (0, 0))
            self.assertLess(row["max_root_error"], 1.0e-6)

    def test_source_lock_and_code_constants_have_machine_checked_parity(self) -> None:
        lock_path = Path(__file__).resolve().parents[1] / "configs/source_locks/CTRL-0001.yaml"
        payload = lock_path.read_bytes()
        lock = yaml.safe_load(payload)
        self.assertEqual(lock["lock_version"], 2)
        self.assertFalse(lock["formal_candidate"])
        self.assertEqual(lock["cutoff"]["mode_cutoffs"], list(MODE_CUTOFFS))
        self.assertEqual(
            lock["cutoff"]["coefficient_cutoffs"], list(COEFFICIENT_CUTOFFS)
        )
        self.assertEqual(
            lock["cutoff"]["contour_points_per_edge"],
            list(CONTOUR_POINTS_PER_EDGE),
        )
        self.assertEqual(lock["cutoff"]["primary_mode_cutoff"], PRIMARY_MODE_CUTOFF)
        self.assertEqual(
            lock["cutoff"]["primary_coefficient_cutoff"],
            PRIMARY_COEFFICIENT_CUTOFF,
        )
        self.assertEqual(lock["precision"]["match_radius"], MATCH_RADIUS)
        expected_channels = {
            "A_plus": ("11/20", "2/5", "+pi/3"),
            "A_minus": ("11/20", "2/5", "-pi/3"),
            "B": ("9/20", "1/2", "pi"),
            "C": ("3/10", "9/20", "0"),
        }
        self.assertEqual([channel.name for channel in CHANNELS], list(expected_channels))
        for channel_name, values in expected_channels.items():
            row = lock["mathematical_object"]["channels"][channel_name]
            self.assertEqual((row["alpha"], row["beta"], row["theta"]), values)
        self.assertEqual(
            hashlib.sha256(payload).hexdigest(), self.report["source_lock_sha256"]
        )


if __name__ == "__main__":
    unittest.main()
