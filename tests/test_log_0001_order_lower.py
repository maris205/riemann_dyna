import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from flint import arb, ctx
import yaml

from experiments import log_0001_order_lower as audit


class Log0001OrderLowerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = audit.build_report()
        cls.root = Path(__file__).resolve().parents[1]

    def test_all_target_free_gates_pass(self) -> None:
        self.assertEqual(self.report["candidate_id"], "LOG-0001")
        self.assertEqual(self.report["audit_id"], "LOG-0001-ORDER-LOWER")
        self.assertTrue(self.report["formal_candidate"])
        self.assertTrue(self.report["computed_gates_passed"])
        self.assertTrue(all(self.report["computed_gates"].values()))
        self.assertTrue(
            all(not value for value in self.report["data_firewall"].values())
        )

    def test_pl_ledger_and_order_interval(self) -> None:
        proof = self.report["pl_proof_ledger"]
        self.assertTrue(proof["computed_gates_passed"])
        self.assertEqual(proof["translated_variable"], "g(z)=D_pol(2-z), Re(z)>0")
        self.assertEqual(
            proof["assumption_for_contradiction"], "ord(D_pol)=rho<1"
        )
        route = self.report["route_a_effect"]
        self.assertEqual(route["order_lower_bound"], "1<=ord(D_pol)<=2")
        self.assertFalse(route["route_b_invocation_allowed"])

    def test_independent_1024_bit_scalar_recomputation(self) -> None:
        before = ctx.prec
        try:
            ctx.prec = audit.ARB_BITS
            u = audit.root_ball()
            alpha_0 = u**2 / 4
            q_2 = 2 * alpha_0**2
            b_2 = -(1 - q_2).log() / (1 - alpha_0)
            k_2 = b_2.exp()
            self.assertGreater(k_2, 1)
            self.assertGreater(b_2, 0)
        finally:
            ctx.prec = before

    def test_source_lock_and_route_a_parity(self) -> None:
        lock = yaml.safe_load(
            (self.root / audit.SOURCE_LOCK).read_text(encoding="utf-8")
        )
        self.assertEqual(lock["candidate_id"], "LOG-0001")
        self.assertEqual(lock["audit_id"], "LOG-0001-ORDER-LOWER")
        self.assertIn("Re(s)>=2", lock["candidate_definition"]["half_plane_anchor"])
        self.assertEqual(lock["cutoff"]["pl_half_plane_boundary"], "Re(s)=2")
        self.assertEqual(lock["precision"]["arb_bits"], audit.ARB_BITS)
        self.assertEqual(lock["precision"]["python_version"], audit.EXPECTED_PYTHON_VERSION)
        forbidden = "\n".join(lock["forbidden_data"])
        self.assertIn("prime tables", forbidden)
        self.assertIn("Fredholm determinant values", forbidden)
        evaluation = yaml.safe_load(
            (self.root / audit.EVALUATION).read_text(encoding="utf-8")
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
        self.assertFalse(evaluation["route_b_invocation_allowed"])
        self.assertEqual(evaluation["a3"]["metrics"]["classical_order_lower"], ">=1")

    def test_artifact_reproduces_byte_for_byte(self) -> None:
        artifact = self.root / audit.ARTIFACT
        self.assertTrue(artifact.exists())
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "certificate.json"
            completed = subprocess.run(
                [
                    sys.executable,
                    audit.GENERATOR,
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

    def test_provenance_hashes_and_environment(self) -> None:
        provenance = self.report["provenance"]
        environment = self.report["validated_environment"]
        self.assertFalse(provenance["external_target_data_used"])
        self.assertEqual(environment["python"], audit.EXPECTED_PYTHON_VERSION)
        self.assertEqual(environment["python_flint"], audit.EXPECTED_PYTHON_FLINT_VERSION)
        self.assertEqual(environment["flint"], audit.EXPECTED_FLINT_VERSION)
        self.assertEqual(environment["arb_bits"], audit.ARB_BITS)
        for relative, expected in provenance["source_inputs_sha256"].items():
            actual = hashlib.sha256((self.root / relative).read_bytes()).hexdigest()
            self.assertEqual(actual, expected, relative)
        generator_hash = hashlib.sha256(
            (self.root / audit.GENERATOR).read_bytes()
        ).hexdigest()
        self.assertEqual(generator_hash, provenance["generator_sha256"])

    def test_arb_context_restored(self) -> None:
        before = ctx.prec
        audit.build_report()
        self.assertEqual(ctx.prec, before)


if __name__ == "__main__":
    unittest.main()
