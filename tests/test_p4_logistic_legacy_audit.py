import unittest
from pathlib import Path

from experiments.p4_logistic_legacy_audit import (
    build_report,
    normalization_audit,
)


REPOSITORY = Path(__file__).resolve().parents[1]


class LogisticLegacyAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = build_report(REPOSITORY)

    def test_legacy_and_correct_normalizations_are_similar(self) -> None:
        audit = normalization_audit()
        self.assertLess(audit["similarity_max_abs_residual"], 1e-14)
        self.assertLess(audit["best_dense_eigenvalue_matching_error"], 1e-12)
        self.assertLess(audit["correct_active_row_sum_max_error"], 1e-14)
        self.assertGreater(audit["legacy_active_row_sum_max_error"], 0.1)

    def test_saved_micro_prefix_is_fitted_and_does_not_generalize(self) -> None:
        metrics = self.report["saved_phase_match"]
        self.assertAlmostEqual(metrics["fitted_zeros_2_to_6"]["absolute_error_sum"], 1.7469707378)
        self.assertAlmostEqual(metrics["fitted_zeros_2_to_6"]["mae"], 0.34939414756)
        self.assertGreater(metrics["retrospective_zeros_7_to_20"]["mae"], 7.0)
        self.assertGreater(metrics["retrospective_zeros_21_to_85"]["mae"], 60.0)

    def test_saved_trials_are_solver_restarts_not_a_physical_ensemble(self) -> None:
        solver = self.report["solver_selection_audit"]
        self.assertEqual(solver["same_matrix_trial_count"], 20)
        self.assertEqual(solver["trial_count_below_2_2"], 4)
        self.assertAlmostEqual(solver["trial_error_sum_2_to_6_min"], 1.7470)
        self.assertAlmostEqual(solver["trial_error_sum_2_to_6_max"], 5.3630)
        self.assertFalse(solver["physical_ensemble"])

    def test_ustc_n20_overlay_is_not_an_amplitude_match(self) -> None:
        ustc = self.report["ustc_audit"]
        self.assertEqual(ustc["n20_experimental_deviations"], [0.26500000000000057, -0.34499999999999886, -0.32500000000000284])
        self.assertGreater(ustc["model_n20_error"], 16.0)
        self.assertFalse(ustc["independent_validation"])

    def test_route_a_candidate_is_not_created(self) -> None:
        self.assertFalse(self.report["formal_candidate"])
        self.assertEqual(self.report["route_a_preassessment"]["status"], "NOT_TESTABLE")
        self.assertFalse(self.report["route_a_preassessment"]["route_b_invocation_allowed"])
        self.assertIsNone(self.report["legacy_object"]["determinant_convention"])


if __name__ == "__main__":
    unittest.main()
