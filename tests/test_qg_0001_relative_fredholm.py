import json
import tempfile
import unittest
from pathlib import Path

import sympy as sp
import yaml

from experiments.qg_0001_relative_fredholm import build_report


ROOT = Path(__file__).resolve().parents[1]


def parse_complex(value: str) -> complex:
    body = value.removesuffix("i")
    if " + " in body:
        real, imaginary = body.rsplit(" + ", 1)
        return complex(float(real), float(imaginary))
    if " - " in body:
        real, imaginary = body.rsplit(" - ", 1)
        return complex(float(real), -float(imaginary))
    return complex(float(body), 0.0)


class QG0001RelativeFredholmTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = build_report()
        cls.lock = yaml.safe_load(
            (ROOT / "configs/source_locks/QG-0001-RELATIVE-FREDHOLM.yaml")
            .read_text(encoding="utf-8")
        )

    def test_source_lock_freezes_one_target_free_determinant(self) -> None:
        self.assertEqual(self.lock["candidate_id"], "QG-0001")
        self.assertEqual(
            self.lock["subaudit_id"], "QG-0001-RELATIVE-FREDHOLM-001"
        )
        self.assertIn("det_F(I-k^2*H^{-1})", self.lock["determinant_convention"])
        self.assertIn("not the ordinary primitive-orbit", self.lock["determinant_convention"])
        self.assertTrue(all(not value for value in self.report["target_data_used"].values()))

    def test_inverse_is_trace_class_with_exact_scaling(self) -> None:
        operator = self.report["operator"]
        self.assertTrue(operator["strictly_positive"])
        self.assertTrue(operator["compact_resolvent"])
        self.assertEqual(operator["inverse_class"], "trace_class")
        self.assertEqual(
            operator["trace_class_identity"],
            "Tr(H^{-1})=zeta(2)*Tr(H_1^{-1})",
        )
        self.assertIn("p>1/2", operator["schatten_H_inverse"])
        self.assertIn("p>1", operator["schatten_H_minus_half"])

    def test_exact_trace_sum_rule_and_tower_coefficient(self) -> None:
        coefficients = self.report["exact_coefficients"]
        base_quadratic = sp.sympify(coefficients["base_quadratic"])
        trace_h1 = sp.sympify(coefficients["trace_H1_inverse"])
        trace_h = sp.sympify(coefficients["trace_H_inverse"])
        tower_quadratic = sp.sympify(coefficients["tower_quadratic"])
        self.assertEqual(sp.simplify(base_quadratic + trace_h1), 0)
        self.assertEqual(sp.simplify(trace_h - sp.zeta(2) * trace_h1), 0)
        self.assertEqual(sp.simplify(tower_quadratic + trace_h), 0)
        self.assertAlmostEqual(
            float(coefficients["trace_H_inverse_decimal"]),
            7.243565369143686,
            places=14,
        )

    def test_component_product_is_same_operator_fredholm_determinant(self) -> None:
        determinant = self.report["determinant"]
        self.assertEqual(
            determinant["component_identity"],
            "D_H(k)=product_{n>=1} chi_0(k/n)",
        )
        self.assertTrue(determinant["normal_convergence_on_compacts"])
        self.assertFalse(determinant["is_naive_orbit_product"])
        self.assertFalse(determinant["is_direct_sum_bond_block_determinant"])
        self.assertFalse(determinant["is_heat_or_spectral_zeta"])
        self.assertFalse(determinant["is_completed_xi"])
        self.assertFalse(determinant["zero_at_origin"])
        self.assertEqual(determinant["canonical_genus_in_k"], 1)
        self.assertEqual(
            determinant["paired_canonical_genus_in_z_equals_k_squared"], 0
        )
        self.assertEqual(determinant["entire_type_in_k"], "infinite")
        self.assertTrue(determinant["coincident_pair_multiplicities_add"])

    def test_raw_bond_phase_requires_factorwise_counterphase(self) -> None:
        raw = self.report["raw_bond_product"]
        self.assertFalse(
            raw[
                "standalone_product_converges_away_from_the_divisor_for_nonzero_real_k"
            ]
        )
        self.assertTrue(raw["counterphase_must_remain_factorwise"])
        self.assertIn("H_N", raw["partial_product_phase"])
        controls = self.report["finite_product_controls"]
        self.assertLess(float(controls["max_raw_ratio_residual"]), 1e-70)
        for sample in controls["samples"]:
            arguments = [
                float(row["raw_phase_argument_unwrapped"])
                for row in sample["partial_products"]
            ]
            self.assertEqual(arguments, sorted(arguments))
            self.assertGreater(arguments[-1] - arguments[0], 2.0)

    def test_finite_products_show_target_free_normal_convergence(self) -> None:
        controls = self.report["finite_product_controls"]
        self.assertEqual(controls["cutoffs"], [8, 16, 32, 64, 128, 256])
        self.assertLess(
            float(controls["max_tail_corrected_128_to_256_drift"]), 4e-9
        )
        for sample in controls["samples"]:
            rows = sample["partial_products"]
            last = parse_complex(rows[-1]["leading_tail_corrected_product"])
            previous = parse_complex(rows[-2]["leading_tail_corrected_product"])
            self.assertLess(abs(last - previous), 4e-9)

    def test_exact_counting_coefficient_is_a_scoped_obstruction(self) -> None:
        counting = self.report["counting"]
        ratio = sp.sympify(counting["candidate_to_target_ratio_exact"])
        expected = 2 + 2 * sp.sqrt(2) + 2 * sp.sqrt(3) + 2 * sp.sqrt(5)
        self.assertEqual(sp.simplify(ratio - expected), 0)
        self.assertAlmostEqual(
            float(counting["candidate_to_target_ratio_decimal"]),
            12.764664694883524,
            places=14,
        )
        self.assertFalse(counting["leading_coefficient_matches_target"])
        self.assertFalse(counting["zero_free_prefactor_can_repair_count"])

    def test_saved_artifact_is_byte_reproducible(self) -> None:
        expected_path = ROOT / "artifacts/qg_0001/relative_fredholm.json"
        expected = json.loads(expected_path.read_text(encoding="utf-8"))
        self.assertEqual(self.report, expected)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "audit.json"
            path.write_text(
                json.dumps(self.report, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            self.assertEqual(path.read_bytes(), expected_path.read_bytes())


if __name__ == "__main__":
    unittest.main()
