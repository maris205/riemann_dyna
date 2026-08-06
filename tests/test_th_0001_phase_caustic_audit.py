import json
import tempfile
import unittest
from pathlib import Path

from experiments.th_0001_phase_caustic_audit import build_report


ROOT = Path(__file__).resolve().parents[1]


class TH0001PhaseCausticAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = build_report()

    def test_internal_hessian_is_exact(self) -> None:
        self.assertEqual(self.report["internal_hessian"], [["3*q1", "1"], ["1", "5*q2"]])
        self.assertEqual(self.report["internal_hessian_determinant"], "15*q1*q2 - 1")
        self.assertEqual(self.report["caustic_equation"], "15*q1*q2-1=0")

    def test_caustic_has_exact_nonempty_witness(self) -> None:
        self.assertEqual(self.report["caustic_nonempty_witness"], {"q1": "1", "q2": "1/15"})
        self.assertFalse(self.report["global_single_phase_reduction"])

    def test_ordered_kernel_and_unitary_scope_are_preserved(self) -> None:
        self.assertTrue(self.report["ordered_oscillatory_integral_remains_defined"])
        self.assertTrue(self.report["factorized_unitarity_unaffected"])
        self.assertEqual(self.report["route_a_a4"]["new_obstruction"], "OBR-011")

    def test_phase_convention_does_not_assign_maslov_index(self) -> None:
        phase = self.report["phase_convention"]
        self.assertEqual(phase["factor_amplitude"], "positive real (2*pi)^(-1/2)")
        self.assertEqual(phase["factor_phase"], "exp(+i*S_a)")
        self.assertEqual(phase["global_maslov_index"], "NOT_ASSIGNED")

    def test_saved_artifact_is_byte_reproducible(self) -> None:
        expected_path = ROOT / "artifacts/th_0001/phase_caustic_audit.json"
        expected = json.loads(expected_path.read_text(encoding="utf-8"))
        self.assertEqual(self.report, expected)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "audit.json"
            path.write_text(json.dumps(self.report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            self.assertEqual(path.read_bytes(), expected_path.read_bytes())


if __name__ == "__main__":
    unittest.main()
