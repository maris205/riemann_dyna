import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from flint import arb, ctx
import yaml

from experiments import log_0001_lower_growth as lower


class Log0001LowerGrowthTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = lower.build_report()
        cls.root = Path(__file__).resolve().parents[1]

    def test_all_target_free_gates_pass(self) -> None:
        self.assertEqual(self.report["candidate_id"], "LOG-0001")
        self.assertEqual(
            self.report["audit_id"], "LOG-0001-LOWER-GROWTH"
        )
        self.assertTrue(self.report["formal_candidate"])
        self.assertTrue(self.report["computed_gates_passed"])
        self.assertTrue(all(self.report["computed_gates"].values()))
        firewall = self.report["data_firewall"]
        self.assertTrue(all(not value for value in firewall.values()))

    def test_exact_bracket_and_cauchy_geometry(self) -> None:
        exact = self.report["exact_bracket_and_cauchy_certificate"]
        self.assertEqual(exact["safe_real_point"], 2)
        self.assertEqual(exact["Cauchy_radius"], "R-2")
        self.assertEqual(exact["radial_factor"], "1/2")
        self.assertTrue(all(exact["computed_gates"].values()))

    def test_arb_derivative_and_maximum_modulus_floors(self) -> None:
        intervals = self.report["arb_interval_certificate"]
        gates = intervals["computed_gates"]
        self.assertTrue(gates["c_2_is_above_published_derivative_floor"])
        self.assertTrue(gates["half_c_2_is_above_published_radial_floor"])
        self.assertGreaterEqual(
            intervals["c_2_relative_accuracy_bits"], 300
        )
        before = ctx.prec
        try:
            ctx.prec = lower.ARB_BITS
            u = lower.root_ball()
            alpha_0 = u**2 / 4
            tau_star = -alpha_0.log()
            b_2 = -(1 - 2 * alpha_0**2).log() / (1 - alpha_0)
            c_2 = (-b_2).exp() * tau_star * alpha_0**2 / (1 - alpha_0)
            self.assertGreater(c_2, arb(213) / 10000)
            self.assertGreater(c_2 / 2, arb(213) / 20000)
        finally:
            ctx.prec = before

    def test_same_object_signed_ledger_and_claim_boundary(self) -> None:
        ledger = self.report["analytic_ledger"]
        self.assertTrue(ledger["all_real_derivative_summands_strictly_positive"])
        self.assertTrue(ledger["orientation_signs_preserved"])
        self.assertTrue(
            ledger["retained_term_is_a_proof_lower_bound_not_a_truncation"]
        )
        self.assertEqual(ledger["pure_left_ledger"]["matching_factor"], 1)
        consequence = self.report["maximum_modulus_consequence"]
        self.assertTrue(consequence["transcendental_entire"])
        self.assertTrue(consequence["qualitative_super_polynomial_growth"])
        self.assertTrue(
            any(
                "positive or exact entire-function order" in item
                for item in self.report["claim_boundary"]["not_established"]
            )
        )

    def test_source_lock_and_route_a_boundary(self) -> None:
        lock = yaml.safe_load(
            (self.root / lower.SOURCE_LOCK).read_text(encoding="utf-8")
        )
        self.assertEqual(lock["candidate_id"], "LOG-0001")
        self.assertEqual(lock["audit_id"], "LOG-0001-LOWER-GROWTH")
        self.assertIn(
            "s_0=2", lock["candidate_definition"]["scalar_anchor"]
        )
        self.assertEqual(
            lock["cutoff"]["retained_lower_bound_term"],
            "n=1 pure-left based word L",
        )
        self.assertEqual(lock["precision"]["arb_bits"], 1024)
        self.assertEqual(
            lock["precision"]["python_version"],
            lower.EXPECTED_PYTHON_VERSION,
        )
        self.assertEqual(
            lock["precision"]["derivative_safe_floor"], "0.0213"
        )
        self.assertEqual(
            lock["precision"]["radial_linear_safe_floor"], "0.01065"
        )
        self.assertEqual(
            lock["determinant_convention"]["candidate_determinant"],
            "D_pol(s)=Delta(1,s)",
        )
        self.assertIn(
            "T_gamma=sum tau=log|(G^n)'|",
            lock["clock"]["determinant_clock"],
        )
        forbidden = "\n".join(lock["forbidden_data"])
        self.assertIn("prime tables", forbidden)
        self.assertIn("Fredholm determinant values", forbidden)
        self.assertIn("auxiliary lambda expansion", forbidden)
        evaluation = yaml.safe_load(
            (self.root / lower.EVALUATION).read_text(encoding="utf-8")
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
        self.assertEqual(
            evaluation["a3"]["metrics"]["D_pol_prime_at_2"],
            ">0.0213",
        )

    def test_committed_artifact_reproduces_exactly(self) -> None:
        artifact = self.root / lower.ARTIFACT
        self.assertTrue(artifact.exists())
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "certificate.json"
            completed = subprocess.run(
                [
                    sys.executable,
                    lower.GENERATOR,
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

    def test_artifact_hashes_and_environment(self) -> None:
        provenance = self.report["provenance"]
        environment = self.report["validated_environment"]
        self.assertFalse(provenance["external_target_data_used"])
        self.assertEqual(
            environment["python"], lower.EXPECTED_PYTHON_VERSION
        )
        self.assertEqual(
            environment["python_flint"], lower.EXPECTED_PYTHON_FLINT_VERSION
        )
        self.assertEqual(environment["flint"], lower.EXPECTED_FLINT_VERSION)
        self.assertEqual(environment["arb_bits"], lower.ARB_BITS)
        self.assertIn(lower.PARENT_LOCK, provenance["source_inputs_sha256"])
        self.assertIn(lower.GROWTH_LOCK, provenance["source_inputs_sha256"])
        self.assertIn(lower.PARENT_RESULT, provenance["source_inputs_sha256"])
        self.assertIn(lower.GROWTH_RESULT, provenance["source_inputs_sha256"])
        self.assertIn(
            lower.GROWTH_ARTIFACT, provenance["source_inputs_sha256"]
        )
        for relative, expected in provenance["source_inputs_sha256"].items():
            actual = hashlib.sha256(
                (self.root / relative).read_bytes()
            ).hexdigest()
            self.assertEqual(actual, expected, relative)
        generator_hash = hashlib.sha256(
            (self.root / lower.GENERATOR).read_bytes()
        ).hexdigest()
        self.assertEqual(generator_hash, provenance["generator_sha256"])

    def test_arb_context_is_restored(self) -> None:
        before = ctx.prec
        lower.build_report()
        self.assertEqual(ctx.prec, before)


if __name__ == "__main__":
    unittest.main()
