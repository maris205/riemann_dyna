from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "experiments/p4_logistic_uc_polar_partition_trace.py"
ARTIFACT = ROOT / (
    "artifacts/p4_logistic_uc_polar_partition_trace/"
    "partition_trace_certificate.json"
)
LOCK = ROOT / "configs/source_locks/P4-LOGISTIC-UC-POLAR-PARTITION-TRACE.yaml"


class PolarPartitionTraceAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        subprocess.run(
            [sys.executable, str(SCRIPT), "--quiet", "--output", str(ARTIFACT)],
            cwd=ROOT,
            check=True,
        )
        cls.report = json.loads(ARTIFACT.read_text(encoding="utf-8"))

    def test_exact_u_c_endpoint_identities(self) -> None:
        identities = self.report["exact_endpoint_identities"]
        self.assertTrue(all(identities.values()))

    def test_half_open_partition_is_frozen(self) -> None:
        convention = self.report["half_open_convention"]
        self.assertEqual(convention["left"], "[-pi/2,0)")
        self.assertEqual(convention["right"], "[0,pi/2]")
        self.assertEqual(convention["partition_owner"], "R")

    def test_boundary_graph_classifies_partition_as_preperiodic(self) -> None:
        graph = self.report["endpoint_orbit_graph"]
        self.assertEqual(graph["forward_edges"], {"P": "P", "Q": "P", "Z": "Q"})
        self.assertEqual(graph["periodic_boundary_states"], ["P"])
        self.assertFalse(graph["partition_point_is_periodic"])
        self.assertEqual(graph["preperiodic_boundary_states"], ["Q", "Z"])

    def test_cyclic_and_endpoint_copy_quotient_gates(self) -> None:
        words = self.report["word_ledger"]
        self.assertTrue(words["rotation_invariance"])
        self.assertTrue(words["endpoint_copy_swap_invariance"])
        self.assertTrue(words["repetition_is_separate_from_endpoint_coding"])
        self.assertGreater(words["checked_word_rows"], 0)

    def test_matching_range_is_proved_but_trace_is_open(self) -> None:
        matching = self.report["matching_range"]
        self.assertTrue(matching["matching_range_is_proved"])
        self.assertTrue(matching["local_trace_identity_is_not_claimed"])
        block = self.report["conditional_block_trace"]
        self.assertTrue(block["conditional_block_form_trace_identity"])
        self.assertEqual(block["toy_matrix_trace"], block["toy_matching_restriction_trace"])
        self.assertTrue(block["toy_matching_does_not_halve_source_sum"])
        self.assertEqual(
            self.report["ledger_rule"]["local_matching_space_trace_identity"],
            "OPEN",
        )

    def test_route_boundary(self) -> None:
        route = self.report["route_a_effect"]
        self.assertEqual(
            route["tuple_unchanged"],
            ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        )
        self.assertFalse(route["route_b_invocation_allowed"])

    def test_source_lock_exists(self) -> None:
        self.assertTrue(LOCK.exists())
        self.assertEqual(self.report["source_lock"], str(LOCK.relative_to(ROOT)))


if __name__ == "__main__":
    unittest.main()
