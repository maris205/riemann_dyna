import math
import unittest

from experiments.ss_0002_commutator_mayer import (
    abelianization_cocycle,
    branch_matrix,
    branch_matrix_from_generators,
    branch_tail_diagnostics,
    build_report,
    counting_diagnostics,
    determinant,
    holonomy_order,
    lifted_primitive_count,
    regular_representation_trace,
    validate_branch_square,
)


class CommutatorMayerTests(unittest.TestCase):
    def test_paired_branch_matrix_and_cocycle_are_exact(self) -> None:
        for a in range(1, 17):
            for b in range(1, 17):
                self.assertEqual(branch_matrix(a, b), branch_matrix_from_generators(a, b))
                self.assertEqual(determinant(branch_matrix(a, b)), 1)
                self.assertEqual(abelianization_cocycle(a, b), (a - b) % 6)

    def test_frozen_validation_and_test_squares_are_disjoint(self) -> None:
        validation = validate_branch_square(1, 8)
        sealed_test = validate_branch_square(9, 16)
        self.assertEqual(validation["branch_pairs_checked"], 64)
        self.assertEqual(sealed_test["branch_pairs_checked"], 64)
        self.assertLess(validation["digit_stop"], sealed_test["digit_start"])

    def test_regular_holonomy_lift_ledger(self) -> None:
        expected_orders = [1, 6, 3, 2, 3, 6]
        expected_lifts = [6, 1, 2, 3, 2, 1]
        self.assertEqual([holonomy_order(c) for c in range(6)], expected_orders)
        self.assertEqual([lifted_primitive_count(c) for c in range(6)], expected_lifts)
        self.assertEqual([regular_representation_trace(c) for c in range(6)], [6, 0, 0, 0, 0, 0])

    def test_branch_tail_diagnostic_matches_half_plane_threshold(self) -> None:
        diagnostics = branch_tail_diagnostics()
        self.assertEqual([row["sigma"] for row in diagnostics], [0.75, 1.0, 1.25])
        for row in diagnostics:
            partial_sums = row["partial_sums_at_z_1"]
            self.assertTrue(all(later > earlier for earlier, later in zip(partial_sums, partial_sums[1:])))
            self.assertTrue(row["increments_strictly_decrease"])

    def test_quadratic_weyl_scale_dominates_T_log_T(self) -> None:
        rows = counting_diagnostics()
        ratios = [row["lifted_quadratic_over_T_log_T"] for row in rows]
        self.assertTrue(all(later > earlier for earlier, later in zip(ratios, ratios[1:])))
        self.assertAlmostEqual(rows[0]["cover_resonance_two_sided_weyl_main"], rows[0]["height"] ** 2)
        self.assertGreater(rows[-1]["modular_cusp_lift_positive_weyl_main"], rows[-1]["xi_positive_main"])

    def test_report_preserves_the_determinant_ledger(self) -> None:
        report = build_report()
        self.assertFalse(report["uses_prime_table"])
        self.assertFalse(report["uses_zero_table"])
        self.assertEqual(report["cover_geometry"]["cover_area"], 2 * math.pi)
        self.assertEqual(report["cover_geometry"]["topology"], "once-punctured torus")
        self.assertEqual(report["nontrivial_mod3_character_modes"], [2, 4])
        self.assertEqual(report["determinant_ledger"]["frozen"], "D_ab(s)=det_Fr(I-M_s)=Z_Gamma_com(s)")
        self.assertIn("modular scattering determinant", report["determinant_ledger"]["separate_objects"])


if __name__ == "__main__":
    unittest.main()
