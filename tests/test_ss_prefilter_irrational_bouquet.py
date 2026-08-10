from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml

from experiments import ss_prefilter_irrational_bouquet as audit


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / audit.ARTIFACT


class IrrationalBouquetPrefilterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = audit.build_report(12)
        cls.lock = yaml.safe_load((ROOT / audit.SOURCE_LOCK).read_text(encoding="utf-8"))

    def test_non_candidate_firewall(self) -> None:
        self.assertFalse(self.report["formal_candidate"])
        self.assertIsNone(self.report["candidate_id"])
        self.assertFalse(self.report["uses_prime_table"])
        self.assertFalse(self.report["uses_zero_table"])
        self.assertEqual(self.lock["formal_candidate"], False)
        self.assertEqual(self.lock["candidate_id"], None)

    def test_certified_sqrt_bracket(self) -> None:
        self.assertLess(audit.SQRT2_LO * audit.SQRT2_LO, 2)
        self.assertLess(2, audit.SQRT2_HI * audit.SQRT2_HI)

    def test_primitive_and_repetition_ledger(self) -> None:
        ledger = self.report["primitive_orbit_ledger"]
        self.assertEqual([row["label"] for row in ledger], list(range(2, 13)))
        self.assertTrue(all(row["primitive_period"] == row["label"] for row in ledger))
        self.assertEqual(self.report["trace_power_terms_1_to_12"]["6"][0]["label"], 2)
        self.assertEqual(self.report["trace_power_terms_1_to_12"]["6"][0]["repetition"], 3)

    def test_non_lattice_and_real_part_escape(self) -> None:
        self.assertTrue(self.report["non_lattice_certificate"]["ratio_is_irrational"])
        self.assertTrue(self.report["closed_form_divisor"]["real_part_strictly_decreasing"])
        self.assertEqual(self.report["strip_indices"]["critical_half_plane_0_1"], [])
        self.assertEqual(self.report["strip_indices"]["moderate_strip_minus10_1"], list(range(2, 12)))

    def test_fixed_strip_count_is_linear(self) -> None:
        rows = self.report["divisor_count_diagnostics"]
        self.assertEqual([row["height"] for row in rows], [100.0, 1000.0, 10000.0])
        self.assertTrue(all(row["symmetric_count"] > 0 for row in rows))
        ratios = [row["symmetric_over_T_log_T"] for row in rows]
        self.assertGreater(ratios[0], ratios[1])
        self.assertGreater(ratios[1], ratios[2])

    def test_route_boundary(self) -> None:
        route = self.report["route_effect"]
        self.assertEqual(route["analytic_tuple"], ["A1_WEAK", "A2_ANALYTIC_DETERMINANT", "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_FAIL"])
        self.assertEqual(route["riemann_target_tuple"], ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"])
        self.assertEqual(route["obstruction"], "OBR-016")
        self.assertFalse(route["route_b_invocation_allowed"])

    def test_source_hash_and_reproducible_artifact(self) -> None:
        expected = self.report["source_lock_sha256"]
        actual = hashlib.sha256((ROOT / audit.SOURCE_LOCK).read_bytes()).hexdigest()
        self.assertEqual(expected, actual)
        self.assertEqual(
            self.report["generator_sha256"],
            hashlib.sha256((ROOT / audit.GENERATOR).read_bytes()).hexdigest(),
        )
        self.assertTrue((ROOT / audit.FORMAL_RESULT).exists())
        self.assertTrue((ROOT / audit.OBSTRUCTION).exists())
        self.assertEqual(json.loads(ARTIFACT.read_text(encoding="utf-8")), self.report)
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "audit.json"
            completed = subprocess.run(
                [sys.executable, audit.GENERATOR, "--n-max", "12", "--output", str(output)],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(output.read_bytes(), ARTIFACT.read_bytes())


if __name__ == "__main__":
    unittest.main()
