import math
import unittest

from experiments.ss_0001_mod6_cayley import (
    adjacency_matrix,
    build_report,
    candidate_zero_count,
    determinant_polynomial,
    primitive_orbit_census,
)


class Mod6CayleyBaselineTests(unittest.TestCase):
    def test_graph_is_the_degree_two_mod6_cayley_graph(self) -> None:
        matrix = adjacency_matrix()
        self.assertEqual(len(matrix), 6)
        self.assertEqual([sum(row) for row in matrix], [2] * 6)
        self.assertTrue(all(matrix[row][column] == matrix[column][row] for row in range(6) for column in range(6)))

    def test_exact_determinant_factorization(self) -> None:
        self.assertEqual(determinant_polynomial(adjacency_matrix()), [1, 0, -6, 0, 9, 0, -4])

    def test_primitive_orbit_counts_are_integral(self) -> None:
        census = primitive_orbit_census(adjacency_matrix(), 24)
        self.assertEqual(len(census), 24)
        self.assertTrue(all(row["primitive_points"] == row["period"] * row["primitive_orbits"] for row in census))
        self.assertTrue(all(row["closed_walks"] == 0 for row in census[0::2]))

    def test_zero_count_has_linear_not_T_log_T_growth(self) -> None:
        low = candidate_zero_count(1_000.0) / (1_000.0 * math.log(1_000.0))
        high = candidate_zero_count(1_000_000.0) / (1_000_000.0 * math.log(1_000_000.0))
        self.assertLess(high, low)
        self.assertGreater(candidate_zero_count(1_000_000.0), candidate_zero_count(1_000.0))

    def test_report_respects_frozen_windows(self) -> None:
        report = build_report(24)
        census = report["orbit_census"]
        self.assertEqual([row["period"] for row in census["training_1_8"]], list(range(1, 9)))
        self.assertEqual([row["period"] for row in census["validation_9_16"]], list(range(9, 17)))
        self.assertEqual([row["period"] for row in census["test_17_24"]], list(range(17, 25)))
        self.assertTrue(report["mod3_character_modes_present"])


if __name__ == "__main__":
    unittest.main()
