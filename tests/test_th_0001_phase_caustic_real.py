from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml

from experiments import th_0001_phase_caustic_real as audit


ROOT = Path(__file__).resolve().parents[1]


class TH0001OnShellCausticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = audit.build_report()
        cls.lock = yaml.safe_load((ROOT / audit.SOURCE_LOCK).read_text(encoding="utf-8"))

    def test_identity_and_firewall(self) -> None:
        self.assertEqual(self.report["candidate_id"], "TH-0001")
        self.assertEqual(self.report["audit_id"], "TH-0001-A4-PHASE-CAUSTIC-REAL-001")
        self.assertTrue(self.report["formal_candidate"])
        self.assertTrue(all(not value for value in self.report["target_data_used"].values()))
        self.assertEqual(self.lock["audit_id"], self.report["audit_id"])

    def test_exact_on_shell_parameterization(self) -> None:
        incidence = self.report["on_shell_caustic"]
        self.assertTrue(incidence["all_real_nonzero_t_are_on_shell"])
        self.assertEqual(incidence["q2"], "1/(15*t)")
        self.assertEqual(incidence["endpoint_jacobian_plus_hessian"], [["0", "0"], ["0", "0"]])

    def test_rational_canonical_witness(self) -> None:
        trajectory = self.report["canonical_trajectory"]
        self.assertTrue(trajectory["all_step_residuals_zero"])
        self.assertEqual(trajectory["q"], {"q0": "-17/30", "q1": "1", "q2": "1/15", "q3": "-1/90"})
        self.assertEqual(trajectory["p"], {"p0": "-289/1800", "p1": "-17/30", "p2": "1", "p3": "1/15"})

    def test_regular_rank_one_witness(self) -> None:
        witness = self.report["regular_rank_one_witness"]
        self.assertEqual(witness["rank"], 1)
        self.assertEqual(witness["hessian_times_null"], ["0", "0"])
        self.assertEqual(witness["third_directional_derivative"], "132")
        self.assertTrue(witness["nonzero_third_directional_derivative"])

    def test_route_boundary(self) -> None:
        route = self.report["route_effect"]
        self.assertEqual(route["analytic_tuple"], ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"])
        self.assertEqual(route["riemann_target_tuple"], ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"])
        self.assertEqual(route["obstruction_refined"], "OBR-011")
        self.assertFalse(route["route_b_invocation_allowed"])

    def test_registered_result_and_obstruction(self) -> None:
        result = (ROOT / audit.FORMAL_RESULT).read_text(encoding="utf-8")
        obstruction = (ROOT / audit.OBSTRUCTION).read_text(encoding="utf-8")
        self.assertIn("on-shell", result.lower())
        self.assertIn("TH-0001-A4-PHASE-CAUSTIC-REAL-001", obstruction)
        self.assertIn("not a new independent", obstruction.lower())

    def test_source_hashes_and_reproducible_artifact(self) -> None:
        provenance = self.report["provenance"]
        for relative, expected in provenance["source_inputs_sha256"].items():
            actual = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
            self.assertEqual(actual, expected, relative)
        self.assertEqual(
            hashlib.sha256((ROOT / audit.GENERATOR).read_bytes()).hexdigest(),
            provenance["generator_sha256"],
        )
        artifact = ROOT / audit.ARTIFACT
        self.assertEqual(json.loads(artifact.read_text(encoding="utf-8")), self.report)
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "certificate.json"
            completed = subprocess.run(
                [sys.executable, audit.GENERATOR, "--quiet", "--output", str(output)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(output.read_bytes(), artifact.read_bytes())


if __name__ == "__main__":
    unittest.main()
