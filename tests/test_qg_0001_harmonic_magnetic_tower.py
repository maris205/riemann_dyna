import json
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

import yaml

from experiments.qg_0001_harmonic_magnetic_tower import (
    build_report,
    identity,
    matmul,
    orbit_amplitude,
    orbit_edge_counts,
    scattering_matrix,
    transpose,
)


ROOT = Path(__file__).resolve().parents[1]


class QG0001HarmonicMagneticTowerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = build_report()
        cls.lock = yaml.safe_load(
            (ROOT / "configs/source_locks/QG-0001.yaml").read_text(encoding="utf-8")
        )

    def test_source_lock_freezes_target_free_infinite_graph(self) -> None:
        self.assertEqual(self.lock["candidate_id"], "QG-0001")
        self.assertIn("1/n", self.lock["mathematical_object"]["tower"])
        self.assertIn("NOT_OPENED", self.lock["determinant_convention"])
        self.assertIn("prime tables", self.lock["forbidden_data"][0])
        self.assertIn("Riemann-zero tables", self.lock["forbidden_data"][0])
        self.assertEqual(self.report["target_data_used"], {
            "prime_table": False,
            "zero_table": False,
            "fitting": False,
        })

    def test_vertex_scattering_is_exactly_orthogonal(self) -> None:
        matrix = scattering_matrix()
        self.assertEqual(matmul(transpose(matrix), matrix), identity(8))
        self.assertEqual(self.report["base_graph"]["vertices"]["L"]["degree"], 4)
        self.assertEqual(self.report["base_graph"]["vertices"]["R"]["degree"], 3)
        self.assertEqual(self.report["base_graph"]["vertices"]["D"]["boundary"], "Dirichlet")

    def test_complete_primitive_prefix_and_repetition_ledgers(self) -> None:
        self.assertEqual(
            self.report["primitive_orbit_counts"],
            {"1": 0, "2": 10, "3": 0, "4": 45, "5": 0, "6": 330},
        )
        checks = self.report["trace_repetition_checks"]
        self.assertTrue(all(row["identity_passed"] for row in checks.values()))
        self.assertEqual(checks["6"]["based_closed_words"], 2000)
        self.assertEqual(checks["6"]["primitive_orbits"], 330)

    def test_asymmetric_decoration_blocks_the_local_geometric_reversor(self) -> None:
        audit = self.report["geometric_antiunitary_audit"]
        self.assertEqual(audit["length_preserving_graph_automorphisms"], 1)
        self.assertEqual(audit["only_graph_automorphism"], "identity")
        self.assertFalse(audit["identity_gauge_equivalent_to_flux_reversal"])
        self.assertFalse(audit["inherited_local_geometric_antiunitary"])
        self.assertTrue(audit["abstract_spectral_basis_conjugation_exists"])
        self.assertFalse(audit["abstract_conjugation_geometric_or_orbit_interpretation"])

    def test_harmonic_scaling_has_the_target_counting_order_without_a_fit(self) -> None:
        theorem = self.report["operator_theorem"]
        self.assertEqual(theorem["component_self_adjointness"].split()[0], "PROVED")
        self.assertEqual(theorem["compact_resolvent"].split()[0], "PROVED")
        self.assertTrue(theorem["counting_order_matches_T_log_T"])
        self.assertFalse(theorem["leading_coefficient_matches_without_rescaling"])
        self.assertGreater(theorem["unfitted_leading_coefficient_ratio"], 12.0)
        self.assertLess(theorem["unfitted_leading_coefficient_ratio"], 13.0)

    def test_pendant_bounce_proves_the_naive_product_is_not_defined(self) -> None:
        self.assertEqual(orbit_amplitude((3, 7)), Fraction(1, 2))
        self.assertEqual(orbit_edge_counts((3, 7)), (0, 0, 0, 2))
        obstruction = self.report["naive_determinant_obstruction"]
        self.assertEqual(obstruction["factor_limit_as_n_to_infinity"], "1/2")
        self.assertFalse(obstruction["ordinary_nonzero_euler_product_exists"])
        self.assertEqual(obstruction["component_bond_trace_norm_limit"], 8)
        self.assertFalse(obstruction["direct_sum_bond_block_compact"])
        self.assertFalse(obstruction["direct_sum_bond_block_trace_class"])
        self.assertFalse(obstruction["standard_direct_sum_fredholm_determinant_exists"])

    def test_spectral_zeta_is_not_promoted_to_a_secular_divisor(self) -> None:
        warning = self.report["spectral_zeta_data_type_warning"]
        self.assertEqual(warning["identity"], "zeta_H(z)=zeta(2*z)*zeta_H1(z)")
        self.assertIn("exponent variable", warning["meaning"])
        self.assertIn("secular characteristic divisor", warning["not_meaning"])
        self.assertTrue(warning["cross_ledger_promotion_forbidden"])
        self.assertEqual(self.report["determinant_convention"], "NOT_OPENED")

    def test_saved_artifact_is_byte_reproducible(self) -> None:
        expected_path = ROOT / "artifacts/qg_0001/route_a_prefilter.json"
        expected = json.loads(expected_path.read_text(encoding="utf-8"))
        self.assertEqual(self.report, expected)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "audit.json"
            path.write_text(json.dumps(self.report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            self.assertEqual(path.read_bytes(), expected_path.read_bytes())


if __name__ == "__main__":
    unittest.main()
