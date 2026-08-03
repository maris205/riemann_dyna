import inspect
import tempfile
import unittest
from pathlib import Path

import numpy as np

from experiments import p4_logistic_medium_branch_audit as medium


class LogisticMediumBranchAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = medium.MediumConfig(
            full_schedule_steps=300,
            reference_bins=96,
            reference_steps=80,
            time_prefixes=(40, 80, 120),
            bin_profiles=(64, 96, 128),
            dense_anchor_bins=48,
            dense_anchor_steps=60,
            profile_k=16,
            reference_k_guard=(10, 16),
            arpack_ncv=40,
            strong_modulus_floor=0.05,
            moderate_modulus_floor=0.01,
            weak_modulus_floor=1.0e-5,
            minimum_upper_half_strong_branches=2,
            k_edge_modulus_ceiling=1.1,
        )
        cls.report = medium.build_report(cls.config)

    def test_source_is_target_free(self) -> None:
        source = inspect.getsource(medium)
        self.assertNotIn("zetazero", source)
        self.assertNotIn("mpmath", source)
        self.assertTrue(self.report["target_free_computation"])
        self.assertFalse(self.report["target_tables_read_during_audit"])
        epsilon_provenance = self.report["historical_target_fitted_parameters"]["epsilon"]
        self.assertEqual(epsilon_provenance["value"], self.config.epsilon)
        self.assertIn("Riemann zeros 2--6", epsilon_provenance["provenance"])

    def test_all_time_cutoffs_share_one_frozen_schedule(self) -> None:
        schedule = medium.schedule_parameters(self.config)
        self.assertAlmostEqual(schedule["mu_first"], self.config.mu_end + self.config.delta_mu)
        self.assertAlmostEqual(schedule["mu_full_schedule_last"], self.config.mu_end)
        profiles = self.report["profiles"]
        self.assertGreater(
            profiles["dynamic_steps_40"]["metadata"]["last_mu"],
            profiles["dynamic_steps_120"]["metadata"]["last_mu"],
        )

    def test_primary_static_control_is_the_reference_window_mean(self) -> None:
        controls = medium.static_controls(self.config)
        self.assertAlmostEqual(
            controls["mean_matched"], medium.schedule_mean(self.config, self.config.reference_steps)
        )

    def test_correct_normalization_and_similarity(self) -> None:
        normalization = self.report["profiles"]["dynamic_reference"]["normalization"]
        self.assertLess(normalization["correct_occupied_row_sum_max_error"], 1e-12)
        self.assertLess(normalization["similarity_max_abs_residual"], 1e-10)
        self.assertGreater(normalization["legacy_occupied_row_sum_max_error"], 0.01)

    def test_static_empirical_matrix_equals_its_kernel_on_occupied_rows(self) -> None:
        for name in (
            "static_mean_matched",
            "static_endpoint_high",
            "static_endpoint_low",
            "static_legacy_regression",
        ):
            self.assertLess(self.report["profiles"][name]["static_kernel_identity_residual"], 1e-10)

    def test_dense_anchor_and_sparse_solver_agree(self) -> None:
        anchor = self.report["dense_physical_epsilon_anchor"]
        self.assertLess(anchor["sparse_max_relative_residual"], 1e-8)
        self.assertLess(anchor["max_complex_distance"], 1e-6)

    def test_raw_transition_round_trip_preserves_content_hash(self) -> None:
        matrices, metadata = medium.simulate_checkpoints(
            self.config, self.config.reference_bins, [self.config.reference_steps]
        )
        transition = matrices[self.config.reference_steps]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "raw_T.npz"
            medium.save_raw_transition(path, transition, metadata[self.config.reference_steps])
            loaded, loaded_metadata, declared_hash = medium.load_raw_transition(path)
        self.assertEqual(declared_hash, medium.matrix_content_hash(transition))
        self.assertEqual(medium.matrix_content_hash(loaded.toarray()), declared_hash)
        self.assertEqual(loaded_metadata, metadata[self.config.reference_steps])

    def test_complex_branch_matching_preserves_signed_complex_data(self) -> None:
        left = np.array([0.5 + 0.2j, 0.5 - 0.2j])
        right = np.array([0.51 + 0.21j, 0.49 - 0.19j])
        match = medium.match_branches(left, right, self.config)
        self.assertEqual(match["matched_count"], 2)
        self.assertLess(match["max_normalized_complex_drift"], 0.04)

    def test_matching_cutoff_maximizes_valid_pair_count_before_distance(self) -> None:
        normalized = np.array([[0.099, 0.001], [0.150, 0.099]])
        pairs = medium._assignment_pairs_with_cutoff(normalized, 0.10)
        self.assertEqual(set(pairs), {(0, 0), (1, 1)})

    def test_weak_edge_truncation_is_diagnostic_not_a_conjugate_gate(self) -> None:
        profiles = {
            "edge_truncated": {
                "spectrum": {
                    "conjugate_pair_defect": {
                        "strong": 0.0,
                        "moderate": 0.0,
                        "weak_diagnostic": 0.5,
                    }
                }
            }
        }
        self.assertTrue(medium.conjugate_layers_pass(profiles, profiles, self.config))
        profiles["edge_truncated"]["spectrum"]["conjugate_pair_defect"]["moderate"] = 0.5
        self.assertFalse(medium.conjugate_layers_pass(profiles, profiles, self.config))


if __name__ == "__main__":
    unittest.main()
