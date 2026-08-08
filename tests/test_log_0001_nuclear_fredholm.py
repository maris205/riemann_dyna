import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml

from experiments import log_0001_nuclear_fredholm as log_0001


class Log0001NuclearFredholmTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = log_0001.build_report()

    def test_all_frozen_based_words_and_gates_pass(self) -> None:
        self.assertEqual(self.report["candidate_id"], "LOG-0001")
        self.assertTrue(self.report["formal_candidate"])
        self.assertTrue(self.report["computed_gates_passed"])
        self.assertTrue(
            self.report["computed_gates"][
                "all_based_words_lengths_1_through_8_enumerated"
            ]
        )
        self.assertEqual(
            sum(item["based_word_count"] for item in self.report["by_length"].values()),
            sum(2**length for length in range(1, 9)),
        )

    def test_signed_orientation_and_cyclic_rotation_ledger(self) -> None:
        for item in self.report["by_length"].values():
            self.assertTrue(item["all_word_gates_passed"])
            for record in item["records"]:
                self.assertTrue(record["gates"]["derivative_sign_matches_R_parity"])
                self.assertTrue(
                    record["gates"]["inverse_iterates_have_strict_branch_signs"]
                )
                self.assertTrue(record["gates"]["signed_denominator_matches_orientation_ledger"])
                self.assertTrue(
                    record["gates"][
                        "all_cyclic_rotations_preserve_roof_and_signed_derivative"
                    ]
                )

    def test_pure_left_boundary_trace_rule(self) -> None:
        ledger = self.report["pure_L_boundary_ledger"]
        self.assertEqual(ledger["1"]["trace_term"], "a_P^(1*s)/(1-a_P^1)")
        for length, item in ledger.items():
            self.assertEqual(item["word"], "L" * int(length))
            self.assertTrue(item["fixed_point_is_P"])
            self.assertTrue(item["inverse_derivative_is_a_P_to_n"])
            self.assertEqual(item["a_P"], "U_c^2/4")

    def test_committed_artifact_reproduces_exactly(self) -> None:
        artifact = Path(log_0001.ARTIFACT)
        self.assertTrue(artifact.exists())
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "certificate.json"
            completed = subprocess.run(
                [sys.executable, log_0001.GENERATOR, "--quiet", "--output", str(output)],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(output.read_bytes(), artifact.read_bytes())

    def test_source_lock_and_route_a_boundary_are_frozen(self) -> None:
        root = Path(__file__).resolve().parents[1]
        lock_path = root / log_0001.SOURCE_LOCK
        evaluation_path = (
            root / "evaluations/route_a/LOG-0001/20260808T051519Z.yaml"
        )
        lock = yaml.safe_load(lock_path.read_text(encoding="utf-8"))
        evaluation = yaml.safe_load(evaluation_path.read_text(encoding="utf-8"))
        self.assertEqual(lock["candidate_id"], "LOG-0001")
        self.assertTrue(lock["formal_candidate"])
        self.assertEqual(
            lock["route_status_at_lock"]["formal_candidate_id"], "LOG-0001"
        )
        self.assertEqual(
            evaluation["analytic_route_tuple"],
            [
                "A1_WEAK",
                "A2_ANALYTIC_DETERMINANT",
                "A3_PARTIAL_ANALYTIC_STRUCTURE",
                "A4_FAIL",
            ],
        )
        self.assertEqual(
            evaluation["riemann_target_tuple"],
            ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        )
        self.assertFalse(evaluation["route_b_invocation_allowed"])

    def test_artifact_hashes_and_target_data_boundary(self) -> None:
        root = Path(__file__).resolve().parents[1]
        provenance = self.report["provenance"]
        self.assertFalse(provenance["external_target_data_used"])
        for relative, expected in provenance["source_inputs_sha256"].items():
            actual = hashlib.sha256((root / relative).read_bytes()).hexdigest()
            self.assertEqual(actual, expected, relative)
        generator_hash = hashlib.sha256(
            (root / log_0001.GENERATOR).read_bytes()
        ).hexdigest()
        self.assertEqual(generator_hash, provenance["generator_sha256"])


if __name__ == "__main__":
    unittest.main()
