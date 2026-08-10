from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml

from experiments import coprime_0001_scalar_boundary as audit


ROOT = Path(__file__).resolve().parents[1]


class CoprimeScalarBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = audit.build_report()
        cls.lock = yaml.safe_load(
            (ROOT / audit.SOURCE_LOCK).read_text(encoding="utf-8")
        )

    def test_identity_and_firewall(self) -> None:
        self.assertEqual(self.report["candidate_id"], "COPRIME-0001")
        self.assertEqual(
            self.report["audit_id"], "COPRIME-0001-SCALAR-BOUNDARY-001"
        )
        self.assertTrue(self.report["formal_candidate"])
        self.assertTrue(
            all(not value for value in self.report["target_data_used"].values())
        )
        self.assertEqual(self.lock["candidate_id"], "COPRIME-0001")
        self.assertEqual(
            self.lock["audit_id"], "COPRIME-0001-SCALAR-BOUNDARY-001"
        )

    def test_local_prime_factor_ledger(self) -> None:
        local = self.report["local_factor_checks"]
        self.assertEqual(local["rank"], 2)
        self.assertEqual(
            local["characteristic_polynomial"],
            "lambda^2-lambda-q/(1-q)",
        )
        self.assertIn("4q^3/(1-q)", local["growth_bound_identity"])
        self.assertTrue(local["sign_for_real_0_lt_q_lt_1"]["alpha_plus_positive"])
        self.assertTrue(local["sign_for_real_0_lt_q_lt_1"]["alpha_minus_negative"])

    def test_sylvester_s2_continuation_ledger(self) -> None:
        continuation = self.report["sylvester_continuation_checks"]
        self.assertEqual(continuation["hs_domain"], "Re(s)>1/2")
        self.assertEqual(
            continuation["continuation_domain"],
            "Omega={Re(s)>1/2, s!=1}",
        )
        self.assertEqual(
            continuation["regularized_determinant"],
            "D_tilde(s)=det_2(I-C_s)",
        )
        self.assertTrue(continuation["same_scalar_on_original_domain"])
        self.assertTrue(continuation["sylvester_identity"] .startswith("det_F"))
        self.assertFalse(continuation["original_operator_extended_below_boundary"])

    def test_endpoint_barrier_is_stronger_than_operator_boundary(self) -> None:
        endpoint = self.report["endpoint_barrier_checks"]
        self.assertIn("infinity", endpoint["top_product_diverges"])
        self.assertIn("every M", endpoint["fixed_positive_mode_count"])
        self.assertIn("9/16", endpoint["safe_right_endpoint"])
        self.assertTrue(endpoint["real_zero_accumulation"].startswith("exists"))
        self.assertFalse(endpoint["root_locations_computed"])
        self.assertFalse(endpoint["root_search_performed"])
        self.assertFalse(endpoint["meromorphic_germ_at_one"])

    def test_route_boundary(self) -> None:
        route = self.report["route_effect"]
        self.assertEqual(
            route["analytic_tuple"],
            [
                "A1_WEAK",
                "A2_ANALYTIC_DETERMINANT",
                "A3_CONTROLLED_CONTINUATION",
                "A4_FAIL",
            ],
        )
        self.assertEqual(
            route["riemann_target_tuple"],
            ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        )
        self.assertEqual(route["scoped_audit_verdict"], "STOP_SCOPED")
        self.assertFalse(route["route_b_invocation_allowed"])

    def test_obstruction_and_formal_result_are_registered(self) -> None:
        obstruction = ROOT / audit.OBSTRUCTION
        result = ROOT / audit.FORMAL_RESULT
        self.assertTrue(obstruction.exists())
        self.assertTrue(result.exists())
        obstruction_text = obstruction.read_text(encoding="utf-8")
        result_text = result.read_text(encoding="utf-8")
        self.assertIn("OBR-015", obstruction_text)
        self.assertIn("no holomorphic or meromorphic", obstruction_text.lower())
        self.assertIn("det_2(I-C_s)", result_text)
        self.assertIn("s_j\\downarrow1", result_text)

    def test_source_hashes_and_artifact_are_reproducible(self) -> None:
        provenance = self.report["provenance"]
        for relative, expected in provenance["source_inputs_sha256"].items():
            actual = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
            self.assertEqual(actual, expected, relative)
        generator_hash = hashlib.sha256((ROOT / audit.GENERATOR).read_bytes()).hexdigest()
        self.assertEqual(generator_hash, provenance["generator_sha256"])

        artifact = ROOT / audit.ARTIFACT
        self.assertTrue(artifact.exists())
        self.assertEqual(
            json.loads(artifact.read_text(encoding="utf-8")), self.report
        )
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
