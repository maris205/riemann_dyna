import hashlib
import json
from fractions import Fraction
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import mpmath as mp
import yaml

from experiments import log_0001_growth_order as growth


class Log0001GrowthOrderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = growth.build_report()
        cls.root = Path(__file__).resolve().parents[1]

    def test_all_target_free_gates_pass(self) -> None:
        self.assertEqual(self.report["candidate_id"], "LOG-0001")
        self.assertEqual(self.report["audit_id"], "LOG-0001-GROWTH-ORDER")
        self.assertTrue(self.report["formal_candidate"])
        self.assertTrue(self.report["computed_gates_passed"])
        self.assertTrue(all(self.report["computed_gates"].values()))
        self.assertFalse(
            self.report["safe_vertical_line"]["Fredholm_roots_evaluated"]
        )

    def test_exact_zero_free_threshold_and_safe_line(self) -> None:
        constants = self.report["exact_real_constants"]
        alpha_0 = mp.mpf(constants["alpha_0"])
        tau_min = mp.mpf(constants["tau_min"])
        sigma_star = mp.mpf(constants["sigma_star"])
        safe = self.report["safe_vertical_line"]
        q_safe = mp.mpf(safe["q_sigma"])

        self.assertAlmostEqual(float(tau_min), float(-mp.log(alpha_0)), places=14)
        self.assertAlmostEqual(
            float(sigma_star), float(mp.log(2) / tau_min), places=14
        )
        self.assertLess(sigma_star, mp.mpf(safe["sigma"]))
        self.assertLess(q_safe, 1)
        self.assertGreater(mp.mpf(safe["determinant_modulus_lower"]), 0)
        self.assertLess(mp.mpf(safe["determinant_modulus_lower"]), 1)
        self.assertGreater(mp.mpf(safe["determinant_modulus_upper"]), 1)

    def test_two_stream_quadratic_exponent_is_exactly_guarded(self) -> None:
        ledger = self.report["two_stream_combinatorial_ledger"]
        self.assertEqual(ledger["q_max"], growth.COMBINATORIAL_Q_MAX)
        self.assertEqual(len(ledger["rows"]), growth.COMBINATORIAL_Q_MAX + 1)
        for row in ledger["rows"]:
            q = row["q"]
            minimum = min(
                Fraction(k * (k - 1) + (q - k) * (q - k - 1), 2)
                for k in range(q + 1)
            )
            lower = Fraction(q * q, 4) - Fraction(q, 2)
            self.assertGreaterEqual(minimum, lower)
            self.assertTrue(row["gate_minimum_is_at_least_quadratic_lower"])
            self.assertEqual(row["allocation_count"], q + 1)

    def test_complex_log_envelope_stays_below_frozen_bound(self) -> None:
        envelope = self.report["complex_log_envelope"]
        self.assertLess(
            mp.mpf(envelope["ell_norm_envelope"]),
            mp.mpf(envelope["ell_norm_safe_upper"]),
        )
        self.assertEqual(
            envelope["inherited_complex_variation_safe_upper"], "0.000851"
        )

    def test_source_lock_and_route_a_boundary(self) -> None:
        lock = yaml.safe_load(
            (self.root / growth.SOURCE_LOCK).read_text(encoding="utf-8")
        )
        evaluation = yaml.safe_load(
            (self.root / growth.EVALUATION).read_text(encoding="utf-8")
        )
        self.assertEqual(lock["candidate_id"], "LOG-0001")
        self.assertEqual(lock["audit_id"], "LOG-0001-GROWTH-ORDER")
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
        self.assertEqual(
            evaluation["a3"]["metrics"]["classical_order_upper"], 2
        )
        self.assertFalse(evaluation["route_b_invocation_allowed"])

    def test_committed_artifact_reproduces_exactly(self) -> None:
        artifact = self.root / growth.ARTIFACT
        self.assertTrue(artifact.exists())
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "certificate.json"
            completed = subprocess.run(
                [
                    sys.executable,
                    growth.GENERATOR,
                    "--quiet",
                    "--output",
                    str(output),
                ],
                cwd=self.root,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(output.read_bytes(), artifact.read_bytes())

    def test_artifact_hashes_and_data_firewall(self) -> None:
        provenance = self.report["provenance"]
        firewall = self.report["data_firewall"]
        self.assertFalse(provenance["external_target_data_used"])
        self.assertTrue(all(not value for value in firewall.values()))
        for relative, expected in provenance["source_inputs_sha256"].items():
            actual = hashlib.sha256((self.root / relative).read_bytes()).hexdigest()
            self.assertEqual(actual, expected, relative)
        generator_hash = hashlib.sha256(
            (self.root / growth.GENERATOR).read_bytes()
        ).hexdigest()
        self.assertEqual(generator_hash, provenance["generator_sha256"])


if __name__ == "__main__":
    unittest.main()
