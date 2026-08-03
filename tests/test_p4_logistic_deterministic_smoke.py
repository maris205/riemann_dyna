import inspect
import unittest

from experiments import p4_logistic_deterministic_smoke as smoke


class LogisticDeterministicSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = smoke.SmokeConfig(bins=64, steps=200, arpack_k=20, arpack_ncv=45)
        cls.report = smoke.build_report(cls.config)

    def test_construction_source_is_target_free(self) -> None:
        source = inspect.getsource(smoke)
        self.assertNotIn("zetazero", source)
        self.assertNotIn("mpmath", source)
        self.assertFalse(self.report["target_data_used"])

    def test_schedule_hits_frozen_endpoints(self) -> None:
        schedule = smoke.schedule_parameters(self.config)
        self.assertAlmostEqual(schedule["mu_first"], self.config.mu_end + self.config.delta_mu)
        self.assertAlmostEqual(schedule["mu_last"], self.config.mu_end)

    def test_empirical_flow_preserves_mass_to_threshold_accuracy(self) -> None:
        metadata = self.report["baseline_partition"]["metadata"]
        self.assertLess(metadata["discarded_mass_sum_over_steps"], 1e-8)
        self.assertAlmostEqual(metadata["final_probability_mass"], 1.0, places=8)

    def test_normalization_similarity_and_row_sums(self) -> None:
        normalization = self.report["baseline_partition"]["normalization"]
        self.assertLess(normalization["correct_occupied_row_sum_max_error"], 1e-12)
        self.assertLess(normalization["similarity_max_abs_residual"], 1e-10)
        self.assertGreater(normalization["legacy_occupied_row_sum_max_error"], 0.1)

    def test_fixed_arpack_profiles_have_small_residuals(self) -> None:
        profiles = self.report["baseline_partition"]["arpack"]
        for matrix_profiles in profiles.values():
            for profile in matrix_profiles:
                self.assertLess(profile["max_relative_residual"], 1e-8)

    def test_phase_ranking_contains_unresolved_modes(self) -> None:
        spectrum = self.report["baseline_partition"]["dense_correct_spectrum"]
        self.assertGreater(spectrum["first_six_unresolved_count"], 0)


if __name__ == "__main__":
    unittest.main()
