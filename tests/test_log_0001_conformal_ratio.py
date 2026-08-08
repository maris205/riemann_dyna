import hashlib
import json
from fractions import Fraction
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from flint import arb, ctx
import yaml

from experiments import log_0001_conformal_ratio as conformal


class Log0001ConformalRatioTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = conformal.build_report()
        cls.root = Path(__file__).resolve().parents[1]

    def test_all_target_free_gates_pass(self) -> None:
        self.assertEqual(self.report["candidate_id"], "LOG-0001")
        self.assertEqual(
            self.report["audit_id"], "LOG-0001-CONFORMAL-RATIO"
        )
        self.assertTrue(self.report["formal_candidate"])
        self.assertTrue(self.report["computed_gates_passed"])
        self.assertTrue(all(self.report["computed_gates"].values()))
        self.assertFalse(
            self.report["data_firewall"]["Fredholm_determinant_evaluated"]
        )
        self.assertFalse(
            self.report["data_firewall"]["numerical_conformal_map_computed"]
        )

    def test_exact_stadium_geometry_and_factor_two(self) -> None:
        exact = self.report["exact_geometry_certificate"]
        self.assertEqual(
            Fraction(exact["outer_radius"]), Fraction(1, 1000)
        )
        self.assertEqual(
            Fraction(exact["inner_radius"]), Fraction(3, 5000)
        )
        self.assertEqual(
            Fraction(exact["inner_to_outer_radius_ratio"]),
            Fraction(3, 5),
        )
        self.assertEqual(Fraction(exact["disk_distance_cross_ratio"]), 4)
        self.assertEqual(
            Fraction(exact["center_path_pi_coefficient"]), 500
        )
        self.assertEqual(exact["branch_interval_length"], "pi/2")
        self.assertEqual(exact["Poincare_disk_center_density"], "2/R")
        self.assertTrue(all(exact["computed_gates"].values()))

    def test_arb_resolves_the_gap_below_one(self) -> None:
        previous_precision = ctx.prec
        try:
            ctx.prec = conformal.ARB_BITS
            d_star = 500 * arb.pi() + arb(4).log()
            t_star = (-d_star).exp()
            r_star = (1 - t_star) / (1 + t_star)
            delta_star = 2 * t_star / (1 + t_star)
            beta_star = ((1 + t_star) / (1 - t_star)).log()

            self.assertGreater(t_star, 0)
            self.assertLess(t_star, 1)
            self.assertGreater(r_star, 0)
            self.assertLess(r_star, 1)
            self.assertGreater(delta_star, 0)
            self.assertGreater(beta_star, 0)
            self.assertTrue(delta_star.overlaps(1 - r_star))
            self.assertTrue(beta_star.overlaps(-r_star.log()))
            self.assertGreaterEqual(delta_star.rel_accuracy_bits(), 1000)
            self.assertGreaterEqual(beta_star.rel_accuracy_bits(), 1000)
            self.assertGreater(delta_star, arb("3.24e-683"))
            self.assertLess(delta_star, arb("3.25e-683"))
        finally:
            ctx.prec = previous_precision

    def test_explicit_quadratic_constants_are_certified(self) -> None:
        intervals = self.report["arb_interval_certificate"]
        gates = intervals["computed_gates"]
        self.assertTrue(gates["c0_is_below_frozen_safe_ceiling"])
        self.assertTrue(gates["c1_is_below_frozen_safe_ceiling"])
        self.assertEqual(intervals["C0_safe_ceiling"], "3.45e689")
        self.assertEqual(intervals["C1_safe_ceiling"], "4.20e682")
        self.assertEqual(
            self.report["explicit_growth_ledger"]["gaussian_theta"],
            "1/4096",
        )
        self.assertIn(
            "3.45e689",
            self.report["explicit_growth_ledger"][
                "published_quadratic_envelope"
            ],
        )
        self.assertTrue(
            self.report["explicit_growth_ledger"][
                "same_object_determinant"
            ]
        )
        self.assertFalse(
            self.report["explicit_growth_ledger"][
                "signed_trace_identity_replaced"
            ]
        )

    def test_source_lock_and_route_a_boundary(self) -> None:
        lock = yaml.safe_load(
            (self.root / conformal.SOURCE_LOCK).read_text(encoding="utf-8")
        )
        evaluation = yaml.safe_load(
            (self.root / conformal.EVALUATION).read_text(encoding="utf-8")
        )
        self.assertEqual(lock["candidate_id"], "LOG-0001")
        self.assertEqual(
            lock["audit_id"], "LOG-0001-CONFORMAL-RATIO"
        )
        self.assertEqual(lock["precision"]["arb_bits"], 4096)
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
        artifact = self.root / conformal.ARTIFACT
        self.assertTrue(artifact.exists())
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "certificate.json"
            completed = subprocess.run(
                [
                    sys.executable,
                    conformal.GENERATOR,
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

    def test_artifact_hashes_environment_and_data_firewall(self) -> None:
        provenance = self.report["provenance"]
        firewall = self.report["data_firewall"]
        environment = self.report["validated_environment"]
        self.assertFalse(provenance["external_target_data_used"])
        self.assertTrue(all(not value for value in firewall.values()))
        self.assertEqual(
            environment["python_flint"],
            conformal.EXPECTED_PYTHON_FLINT_VERSION,
        )
        self.assertEqual(
            environment["flint"], conformal.EXPECTED_FLINT_VERSION
        )
        self.assertEqual(environment["arb_bits"], conformal.ARB_BITS)
        for relative, expected in provenance["source_inputs_sha256"].items():
            actual = hashlib.sha256(
                (self.root / relative).read_bytes()
            ).hexdigest()
            self.assertEqual(actual, expected, relative)
        generator_hash = hashlib.sha256(
            (self.root / conformal.GENERATOR).read_bytes()
        ).hexdigest()
        self.assertEqual(generator_hash, provenance["generator_sha256"])


if __name__ == "__main__":
    unittest.main()
