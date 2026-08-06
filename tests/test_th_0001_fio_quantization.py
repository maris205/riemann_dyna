import json
import tempfile
import unittest
from pathlib import Path

import sympy as sp
import yaml

from experiments.th_0001_fio_quantization import (
    PARAMETERS,
    Q,
    build_report,
    generating_function,
    q,
)


ROOT = Path(__file__).resolve().parents[1]


class TH0001FIOQuantizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = build_report()
        cls.lock = yaml.safe_load(
            (ROOT / "configs/source_locks/TH-0001-FIO.yaml").read_text(encoding="utf-8")
        )

    def test_source_lock_freezes_same_order_l2_object(self) -> None:
        self.assertEqual(self.lock["candidate_id"], "TH-0001")
        self.assertEqual(self.lock["mathematical_object"]["superoperator"], "U=U_(5/2) U_(3/2) U_(1/2)")
        self.assertEqual(self.lock["normalization"]["hbar"], "1 (dimensionless target-free normalization; identities hold for every hbar>0)")
        self.assertIn("L^2(R", self.lock["normalization"]["hilbert_space"])
        self.assertIn("NOT_OPENED", self.lock["determinant_convention"])

    def test_data_firewall_and_no_spectral_object(self) -> None:
        forbidden = " ".join(self.lock["forbidden_data"]).lower()
        self.assertIn("zero tables", forbidden)
        self.assertIn("fft grids", forbidden)
        self.assertIn("route-b", forbidden)
        self.assertFalse(self.report["unitarity_audit"]["spectrum_computed"])
        self.assertEqual(self.report["source_lock"], "configs/source_locks/TH-0001-FIO.yaml")

    def test_generating_function_derivatives_recover_each_kick(self) -> None:
        for parameter in PARAMETERS:
            S = generating_function(parameter)
            self.assertEqual(sp.diff(S, q, Q), 1)
        for value in self.report["generating_function_audit"]["derivatives"].values():
            self.assertEqual(value["mixed_hessian"], "1")
            self.assertIn("q**2", value["solved_Q"])

    def test_fourier_integral_normalization_is_frozen(self) -> None:
        definition = self.report["definition"]
        self.assertEqual(definition["fourier_plus"], "(F_+ psi)(Q)=(2*pi)^(-1/2) integral exp(+i*q*Q) psi(q)dq")
        self.assertEqual(definition["global_phase"], "1")
        self.assertTrue(self.report["unitarity_audit"]["fourier_unitary_by_plancherel"])

    def test_each_factor_and_product_are_unitary(self) -> None:
        audit = self.report["unitarity_audit"]
        self.assertTrue(audit["potential_real_for_frozen_parameters"])
        self.assertTrue(audit["each_factor_unitary_on_all_L2"])
        self.assertTrue(audit["product_unitary_on_all_L2"])
        self.assertEqual(
            audit["inverse_word"],
            ["U_(1/2)^(-1)", "U_(3/2)^(-1)", "U_(5/2)^(-1)"],
        )

    def test_caustic_and_oscillatory_kernel_boundary_is_explicit(self) -> None:
        audit = self.report["unitarity_audit"]
        self.assertIn("iterated oscillatory", audit["triple_kernel_status"])
        self.assertIn("caustic", audit["caustic_warning"])
        self.assertNotIn("absolute convergence", audit["triple_kernel_status"])

    def test_parent_swap_antiunitary_is_involutive(self) -> None:
        audit = self.report["antiunitary_audit"]
        self.assertEqual(audit["antiunitary"], "A=F_+ C")
        self.assertTrue(audit["A_squared"])
        self.assertEqual(audit["A_q_A_inverse"], "p")
        self.assertEqual(audit["A_p_A_inverse"], "q")
        self.assertTrue(audit["single_kick_reversor"])

    def test_nonpalindromic_product_fails_inherited_antiunitary(self) -> None:
        audit = self.report["antiunitary_audit"]
        self.assertFalse(audit["inherited_A_reversor_for_product"])
        self.assertNotEqual(audit["A_conjugated_product_word"], audit["product_inverse_word"])
        self.assertFalse(audit["reverse_word_is_cyclic_rotation"])
        self.assertFalse(audit["natural_clock_reflection_reversor"])
        self.assertEqual(audit["arbitrary_antiunitary_reversor"], "OPEN")

    def test_exact_classical_swap_witness_is_preserved(self) -> None:
        controls = self.report["exact_order_controls"]
        self.assertEqual(controls["G_inverse_origin"], ["-1/2", "-1/8"])
        self.assertEqual(controls["R_G_R_origin"], ["-1/2", "-5/8"])
        self.assertTrue(controls["swap_reversor_witness_differs"])

    def test_exact_operator_order_witness_is_nonzero(self) -> None:
        witness = self.report["exact_order_controls"]["noncommutation_pair"]
        self.assertEqual(witness["difference"], "-p**2")
        self.assertTrue(witness["nonzero_for_frozen_a_b"])

    def test_route_a_upgrades_only_a4_and_keeps_route_b_closed(self) -> None:
        status = self.report["route_a_a4"]
        self.assertEqual(status["verdict"], "A4_NATURAL_QUANTIZATION")
        self.assertTrue(status["unitary_product"])
        self.assertFalse(status["route_b_ready"])
        self.assertNotIn("spectrum", self.report["claim_boundary"]["established"])

    def test_saved_artifact_is_byte_reproducible(self) -> None:
        expected_path = ROOT / "artifacts/th_0001/fio_quantization_audit.json"
        expected = json.loads(expected_path.read_text(encoding="utf-8"))
        self.assertEqual(self.report, expected)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "audit.json"
            path.write_text(json.dumps(self.report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            self.assertEqual(path.read_bytes(), expected_path.read_bytes())


if __name__ == "__main__":
    unittest.main()
