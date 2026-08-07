from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "experiments/p4_logistic_uc_polar_boundary_trace.py"
ARTIFACT = ROOT / (
    "artifacts/p4_logistic_uc_polar_boundary_trace/"
    "boundary_trace_certificate.json"
)
LOCK = ROOT / "configs/source_locks/P4-LOGISTIC-UC-POLAR-BOUNDARY-TRACE.yaml"


class PolarBoundaryTraceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        subprocess.run(
            [sys.executable, str(SCRIPT), "--quiet", "--output", str(ARTIFACT)],
            cwd=ROOT,
            check=True,
        )
        cls.report = json.loads(ARTIFACT.read_text(encoding="utf-8"))

    def test_exact_endpoint_and_multiplier_identities(self) -> None:
        exact = self.report["exact_identity_certificate"]
        self.assertTrue(exact["computed_gates_passed"])
        self.assertEqual(exact["alpha_0"], "u^2/4")
        self.assertEqual(exact["boundary_graph"], {"P": "P", "Q": "P", "Z": "Q"})

    def test_alpha_is_inside_certified_contraction_range(self) -> None:
        numeric = self.report["numerical_trace_certificate"]
        self.assertTrue(numeric["u_c_inside_certified_bracket"])
        self.assertTrue(numeric["alpha_0_strictly_between_zero_and_one"])

    def test_all_taylor_tail_identities_pass(self) -> None:
        numeric = self.report["numerical_trace_certificate"]
        self.assertTrue(numeric["tail_identities_pass"])
        self.assertEqual(numeric["powers"], [1, 2, 3, 4])
        self.assertEqual(numeric["cutoffs"], [4, 8, 16, 32, 64])
        self.assertEqual(numeric["s_values"], ["0", "1/2", "1", "2+i"])

    def test_local_trace_has_no_half_or_doubled_factor(self) -> None:
        ledger = self.report["trace_theorem_ledger"]
        self.assertTrue(ledger["P_is_complex_domain_interior"])
        self.assertFalse(ledger["real_boundary_half_weight_applies"])
        self.assertEqual(ledger["doubled_copy_factor"], 1)
        self.assertEqual(ledger["matching_space_factor"], 1)

    def test_full_nuclearity_and_determinant_stay_closed(self) -> None:
        ledger = self.report["trace_theorem_ledger"]
        self.assertFalse(ledger["full_two_component_nuclearity_claimed"])
        route = self.report["route_a_effect"]
        self.assertEqual(
            route["tuple_unchanged"],
            ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        )
        self.assertFalse(route["route_b_invocation_allowed"])

    def test_source_lock_and_artifact_provenance(self) -> None:
        self.assertTrue(LOCK.exists())
        self.assertEqual(self.report["source_lock"], str(LOCK.relative_to(ROOT)))
        self.assertFalse(self.report["provenance"]["external_target_data_used"])


if __name__ == "__main__":
    unittest.main()
