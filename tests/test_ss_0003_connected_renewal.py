from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml

from experiments import ss_0003_connected_renewal as audit


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / audit.ARTIFACT


class ConnectedRenewalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = audit.build_report(10, 4)
        cls.lock = yaml.safe_load((ROOT / audit.SOURCE_LOCK).read_text(encoding="utf-8"))

    def test_candidate_firewall(self) -> None:
        self.assertTrue(self.report["formal_candidate"])
        self.assertEqual(self.report["candidate_id"], "SS-0003")
        self.assertFalse(self.report["uses_prime_table"])
        self.assertFalse(self.report["uses_zero_table"])
        self.assertTrue(self.report["strong_connectivity"])
        self.assertEqual(self.lock["candidate_id"], "SS-0003")

    def test_primitive_necklaces_and_repetitions(self) -> None:
        rows = self.report["primitive_repetition_ledger"]
        self.assertTrue(rows)
        self.assertTrue(all(row["primitive"] for row in rows))
        words = {tuple(row["word"]) for row in rows}
        self.assertIn((2,), words)
        self.assertIn((2, 3), words)
        self.assertNotIn((2, 2), words)
        self.assertTrue(all(row["edge_period"] == 2 * row["excursion_length"] for row in rows))

    def test_trace_and_determinant_ledgers(self) -> None:
        trace = self.report["trace_power_ledger"]
        self.assertEqual(trace[0]["trace"], "0")
        self.assertEqual(trace[1]["trace"], "2*(sum_(n>=2) n^(-s))^1")
        determinant = self.report["determinant_ledger"]
        self.assertEqual(determinant["exact_identity"], "1-sum_(n>=2)n^(-s)=2-zeta(s)")
        self.assertEqual(self.report["trace_class"]["rank_bound"], 2)
        self.assertEqual(
            self.report["trace_class"]["trace_norm_bound"],
            "||L_s||_1 = 2*(sum_(n>=2)n^(-Re(s)))^(1/2)",
        )

    def test_non_lattice_and_divisor_regime(self) -> None:
        cert = self.report["non_lattice_certificate"]
        self.assertTrue(cert["ratio_is_irrational"])
        divisor = self.report["divisor_regime"]
        self.assertEqual(divisor["fixed_strip"], "0<Re(s)<2")
        self.assertEqual(divisor["asymptotic_regime"], "Theta(T log T)")
        self.assertFalse(divisor["root_search_used"])

    def test_right_half_plane_obstruction(self) -> None:
        obstruction = self.report["right_half_plane_obstruction"]
        self.assertIn("(1,2)", obstruction["statement"])
        self.assertEqual(obstruction["extra_zero"], "D_renew(sigma_star)=0")
        self.assertEqual(self.report["route_effect"]["obstruction"], "OBR-017")
        self.assertFalse(self.report["route_effect"]["route_b_invocation_allowed"])

    def test_hashes_and_cli_reproduction(self) -> None:
        self.assertEqual(
            self.report["source_lock_sha256"],
            hashlib.sha256((ROOT / audit.SOURCE_LOCK).read_bytes()).hexdigest(),
        )
        self.assertEqual(
            self.report["generator_sha256"],
            hashlib.sha256((ROOT / audit.GENERATOR).read_bytes()).hexdigest(),
        )
        self.assertTrue((ROOT / audit.FORMAL_RESULT).exists())
        self.assertTrue((ROOT / audit.OBSTRUCTION).exists())
        self.assertTrue((ROOT / audit.LITERATURE).exists())
        if ARTIFACT.exists():
            self.assertEqual(json.loads(ARTIFACT.read_text(encoding="utf-8")), self.report)
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "audit.json"
            completed = subprocess.run(
                [
                    sys.executable,
                    audit.GENERATOR,
                    "--label-max",
                    "10",
                    "--word-length-max",
                    "4",
                    "--output",
                    str(output),
                ],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), self.report)


if __name__ == "__main__":
    unittest.main()
