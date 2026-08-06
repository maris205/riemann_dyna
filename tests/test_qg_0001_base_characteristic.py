import json
import tempfile
import unittest
from pathlib import Path

import sympy as sp
import yaml

from experiments.qg_0001_base_characteristic import (
    build_report,
    exact_zero_characteristic,
    physical_characteristic_numeric,
)


ROOT = Path(__file__).resolve().parents[1]


def parse_complex(text: str) -> complex:
    real, imaginary = text.removesuffix("i").split(" + ")
    return complex(float(real), float(imaginary))


class QG0001BaseCharacteristicTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = build_report()
        cls.lock = yaml.safe_load(
            (ROOT / "configs/source_locks/QG-0001-BASE-CHARACTERISTIC.yaml")
            .read_text(encoding="utf-8")
        )

    def test_source_lock_is_local_and_target_free(self) -> None:
        self.assertEqual(self.lock["candidate_id"], "QG-0001")
        self.assertEqual(self.lock["subaudit_id"], "QG-0001-BASE-CHARACTERISTIC-001")
        self.assertIn("BASE_PHYSICAL_MATCHING_ONLY", self.lock["determinant_convention"])
        self.assertTrue(all(not value for value in self.report["target_data_used"].values()))
        self.assertIn("tower component determinants", self.lock["forbidden_data"][1])

    def test_exact_zero_characteristic_is_positive(self) -> None:
        value = exact_zero_characteristic()
        expected = sp.sqrt(2) + sp.sqrt(3) + sp.sqrt(5) + sp.sqrt(6) + sp.sqrt(15) + 3 * sp.sqrt(10)
        self.assertEqual(sp.simplify(value - expected), 0)
        self.assertGreater(float(sp.N(value, 30)), 0.0)
        self.assertFalse(self.report["physical_characteristic"]["zero_mode"])

    def test_sinc_matrix_is_entire_even_and_normalized(self) -> None:
        physical = self.report["physical_characteristic"]
        self.assertTrue(physical["entire"])
        self.assertTrue(physical["even"])
        self.assertEqual(physical["normalized_characteristic"], "chi_0(k)=C_phys(k)/A; chi_0(0)=1")
        self.assertEqual(physical["normalized_taylor"], "chi_0(k)=1+a2*k^2+O(k^4)")
        self.assertAlmostEqual(
            float(physical["normalized_quadratic_coefficient_decimal"]),
            -4.403559701953713,
            places=12,
        )

    def test_bond_zero_order_and_exact_leading_coefficient(self) -> None:
        bond = self.report["bond_characteristic"]
        self.assertEqual(bond["zero_at_k0_order"], 2)
        self.assertFalse(bond["zero_is_physical"])
        self.assertIn("k^2*exp(i*k*L0)", bond["exact_relation"])
        self.assertAlmostEqual(
            float(bond["leading_coefficient_decimal"]),
            -28.255517889249993,
            places=13,
        )
        self.assertEqual(bond["raw_normalized_taylor"], "beta(k)=1+i*L0*k+O(k^2)")
        self.assertAlmostEqual(
            parse_complex(bond["first_nonconstant_coefficient_decimal"]).imag,
            6.382332347441762,
            places=13,
        )
        self.assertEqual(bond["component_n_dephasing_factor"], "exp(-i*k*L0/n)")
        self.assertLess(abs(parse_complex(bond["scaled_small_k_error"])), 2e-4)

    def test_bond_identity_residuals_are_high_precision(self) -> None:
        self.assertLess(float(self.report["max_abs_residual"]), 1e-70)
        for row in self.report["sample_checks"]:
            self.assertLess(abs(parse_complex(row["bond_identity_residual"])), 1e-70)
            self.assertLess(abs(parse_complex(row["pole_free_vs_sinc_residual"])), 1e-70)

    def test_edge_dirichlet_sample_uses_the_entire_characteristic(self) -> None:
        row = next(row for row in self.report["sample_checks"] if row["k"] == "pi")
        self.assertTrue(row["edge_sine_zero_sample"])
        self.assertTrue(abs(parse_complex(row["physical_characteristic"])) > 0)
        self.assertTrue(self.report["pole_free_formula"]["individual_sine_factors_are_not_independent_zeros"])

    def test_zero_matching_matrix_is_finite_at_k_zero(self) -> None:
        import mpmath as mp

        mp.mp.dps = 60
        value = physical_characteristic_numeric(mp.mpf(0))
        expected = mp.mpf(self.report["physical_characteristic"]["value_at_zero_decimal"])
        self.assertLess(abs(value - expected), mp.mpf("1e-42"))

    def test_saved_artifact_is_byte_reproducible(self) -> None:
        expected_path = ROOT / "artifacts/qg_0001/base_characteristic_zero.json"
        expected = json.loads(expected_path.read_text(encoding="utf-8"))
        self.assertEqual(self.report, expected)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "audit.json"
            path.write_text(json.dumps(self.report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            self.assertEqual(path.read_bytes(), expected_path.read_bytes())


if __name__ == "__main__":
    unittest.main()
