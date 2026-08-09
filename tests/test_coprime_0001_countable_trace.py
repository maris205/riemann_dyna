from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml

from experiments import coprime_0001_countable_trace as audit


class Coprime0001CountableTraceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root = Path(__file__).resolve().parents[1]
        cls.report = audit.build_report()

    def test_all_target_free_gates_pass(self) -> None:
        self.assertEqual(self.report["candidate_id"], "COPRIME-0001")
        self.assertEqual(self.report["audit_id"], "COPRIME-0001-COUNTABLE-TRACE")
        self.assertTrue(self.report["formal_candidate"])
        self.assertTrue(self.report["computed_gates_passed"])
        self.assertTrue(all(self.report["computed_gates"].values()))
        self.assertTrue(all(not value for value in self.report["data_firewall"].values()))

    def test_trace_class_statement_and_domain(self) -> None:
        proof = self.report["trace_class_proof"]
        self.assertEqual(proof["half_plane"], "Re(s)>1")
        self.assertIn("zeta(sigma)^2/zeta(2 sigma)-1", proof["nuclear_norm_bound"])
        self.assertTrue(proof["local_uniform_trace_norm_convergence"])
        self.assertTrue(proof["holomorphic_trace_class_family"])
        self.assertTrue(proof["operator_domain_exact_for_frozen_ell2_kernel"])
        self.assertIn("sigma<=1", proof["ell2_boundary_witness"])
        self.assertTrue(proof["trace_expansion_fubini_justified"])
        self.assertIn("(zeta(sigma)-1)^k", proof["cycle_trace_absolute_bound"])
        self.assertEqual(
            proof["determinant_convention"],
            "D_cop(s)=det_F(I-L_s), never its reciprocal",
        )

    def test_exact_repetition_ledger_through_six(self) -> None:
        rows = self.report["repetition_control"]["rows"]
        self.assertEqual([row["k"] for row in rows], list(range(1, 7)))
        self.assertTrue(all(row["equal"] for row in rows))
        self.assertEqual(rows[0]["cyclic_word_count"], 0)

    def test_low_period_orientation_and_inclusion_exclusion(self) -> None:
        low = self.report["primitive_low_period_ledger"]
        self.assertEqual(low["period_1"]["primitive_count"], 0)
        self.assertTrue(low["period_1"]["trace_power_zero"])
        self.assertTrue(low["period_2"]["canonical_a_lt_b"])
        self.assertTrue(low["period_2"]["trace_equals_two_times_primitive"])
        self.assertTrue(low["period_3"]["pairwise_distinct"])
        self.assertTrue(low["period_3"]["trace_equals_three_times_primitive"])
        inclusion = self.report["inclusion_exclusion_checks"]
        self.assertTrue(inclusion["c2_equal"])
        self.assertTrue(inclusion["c3_equal"])

    def test_validation_and_sealed_blocks_are_disjoint(self) -> None:
        validation = self.report["validation_cycle_ledger"]
        sealed = self.report["sealed_test_cycle_ledger"]
        self.assertEqual(validation["label_block"], [2, 10])
        self.assertEqual(sealed["label_block"], [11, 18])
        self.assertTrue(validation["all_equal"])
        self.assertTrue(sealed["all_equal"])
        self.assertTrue(self.report["computed_gates"]["validation_test_label_blocks_disjoint"])

    def test_route_a_boundary_and_route_b_gate(self) -> None:
        route = self.report["route_a_effect"]
        self.assertEqual(
            route["tuple"],
            ["A1_WEAK", "A2_ANALYTIC_DETERMINANT", "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_FAIL"],
        )
        self.assertEqual(route["overall_verdict"], "ROUTE_A_EXPLORATORY")
        self.assertFalse(route["route_b_invocation_allowed"])
        self.assertFalse(self.report["data_firewall"]["Fredholm_roots_searched"])

    def test_scoped_operator_boundary_is_registered(self) -> None:
        obstruction = self.root / "formal/obstructions/coprime_ell2_operator_boundary.md"
        self.assertTrue(obstruction.exists())
        text = obstruction.read_text(encoding="utf-8")
        self.assertIn("PROVED_OBSTRUCTION", text)
        self.assertIn("sigma<=1", text)
        registry = (self.root / "docs/obstruction_registry.md").read_text(encoding="utf-8")
        self.assertIn("OBR-014", registry)

    def test_source_lock_and_evaluation_parity(self) -> None:
        lock = yaml.safe_load((self.root / audit.SOURCE_LOCK).read_text(encoding="utf-8"))
        self.assertEqual(lock["candidate_id"], "COPRIME-0001")
        self.assertEqual(lock["audit_id"], "COPRIME-0001-COUNTABLE-TRACE")
        self.assertIn("Re(s)>1", lock["candidate_definition"]["initial_domain"])
        self.assertEqual(lock["determinant_convention"]["frozen_object"], "D_cop(s)=det_F(I-L_s)")
        self.assertEqual(lock["cutoff"]["validation_label_block"], "2..10, periods 1..3")
        forbidden = "\n".join(lock["forbidden_data"])
        self.assertIn("prime tables", forbidden)
        self.assertIn("Riemann-zero tables", forbidden)
        evaluation = yaml.safe_load((self.root / audit.EVALUATION).read_text(encoding="utf-8"))
        self.assertEqual(evaluation["analytic_route_tuple"], self.report["route_a_effect"]["tuple"])
        self.assertFalse(evaluation["route_b_invocation_allowed"])
        self.assertEqual(evaluation["a2"]["metrics"]["trace_class_domain"], "Re(s)>1")

    def test_artifact_reproduces_byte_for_byte(self) -> None:
        artifact = self.root / audit.ARTIFACT
        self.assertTrue(artifact.exists())
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "certificate.json"
            completed = subprocess.run(
                [sys.executable, audit.GENERATOR, "--quiet", "--output", str(output)],
                cwd=self.root,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(output.read_bytes(), artifact.read_bytes())

    def test_provenance_hashes(self) -> None:
        provenance = self.report["provenance"]
        self.assertFalse(provenance["external_target_data_used"])
        for relative, expected in provenance["source_inputs_sha256"].items():
            actual = hashlib.sha256((self.root / relative).read_bytes()).hexdigest()
            self.assertEqual(actual, expected, relative)
        generator_hash = hashlib.sha256((self.root / audit.GENERATOR).read_bytes()).hexdigest()
        self.assertEqual(generator_hash, provenance["generator_sha256"])


if __name__ == "__main__":
    unittest.main()
