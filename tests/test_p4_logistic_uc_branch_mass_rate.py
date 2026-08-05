from decimal import Decimal
from fractions import Fraction
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml

from experiments import p4_logistic_uc_branch_mass_rate as rate


class LogisticUcBranchMassRateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = rate.build_report()

    def test_every_certification_gate_passes(self) -> None:
        self.assertTrue(self.report["computed_gates_passed"])
        self.assertEqual(
            [
                name
                for name, passed in self.report["computed_gates"].items()
                if not passed
            ],
            [],
        )

    def test_frozen_environment_and_precision_are_recorded(self) -> None:
        environment = self.report["validated_environment"]
        self.assertEqual(
            environment["python_flint"],
            rate.EXPECTED_PYTHON_FLINT_VERSION,
        )
        self.assertEqual(environment["flint"], rate.EXPECTED_FLINT_VERSION)
        self.assertEqual(environment["arb_decimal_digits"], 100)

    def test_one_closed_arb_interval_certifies_both_derivatives(self) -> None:
        certificate = self.report["derivative_certificate"]
        self.assertEqual(certificate["x_domain"], ["rho-1/200", "rho"])
        self.assertGreater(
            Decimal(certificate["psi_prime_lower"]),
            Decimal("0.35"),
        )
        self.assertLess(
            Decimal(certificate["psi_prime_upper"]),
            Decimal("0.36"),
        )
        self.assertGreater(
            Decimal(certificate["psi_second_lower"]),
            Decimal("0"),
        )
        self.assertLess(
            Decimal(certificate["psi_second_upper"]),
            Decimal("0.16"),
        )

    def test_exact_delta_5_starts_the_complete_tail(self) -> None:
        certificate = self.report["base_endpoint_certificate"]
        interval = certificate["delta_5_exact_interval"]
        lower = Fraction(interval["lower"])
        upper = Fraction(interval["upper"])
        self.assertGreater(lower, 0)
        self.assertLess(lower, upper)
        self.assertLess(upper, Fraction(1, 200))
        self.assertLess(upper, Fraction(27, 500) ** 2)
        self.assertTrue(certificate["delta_5_below_cusp_radius"])
        self.assertTrue(certificate["sqrt_delta_5_below_27_over_500"])

    def test_cusp_space_and_normalization_are_frozen(self) -> None:
        space = self.report["cusp_adapted_space"]
        self.assertEqual(space["radius"], "1/200")
        self.assertEqual(space["norm"], "|c|+||b||_infinity")
        self.assertEqual(space["physical_coefficient_lower"], "0.09461")
        self.assertEqual(space["physical_remainder_upper"], "0.61")

        lock = yaml.safe_load(Path(rate.SOURCE_LOCK).read_text(encoding="utf-8"))
        self.assertEqual(lock["audit_id"], rate.AUDIT_ID)
        self.assertEqual(lock["cutoff"]["minimum_branch_index"], 6)
        self.assertIn(
            "shared by every branch",
            lock["normalization"],
        )

    def test_exact_fraction_ledger_closes_the_rate_constant(self) -> None:
        ledger = self.report["exact_rate_ledger"]
        self.assertEqual(Fraction(ledger["q_error_raw"]), Fraction(8, 59))
        self.assertEqual(
            Fraction(ledger["relative_mass_error_raw"]),
            Fraction(48800, 9461),
        )
        self.assertEqual(
            Fraction(ledger["geometry_error_raw"]),
            Fraction(8687, 20000),
        )
        self.assertEqual(
            Fraction(ledger["combined_rate_coefficient"]),
            Fraction(88447, 12500),
        )
        self.assertLess(
            Fraction(ledger["combined_rate_coefficient"]),
            Fraction(ledger["local_rate_constant"]),
        )
        self.assertEqual(
            Fraction(ledger["exponential_rate_prefactor"]),
            Fraction(243, 625),
        )

    def test_rate_statement_is_all_tail_and_keeps_scope_closed(self) -> None:
        statement = self.report["certified_statement"]
        self.assertIn("(36/5)*sqrt(delta_(n-1)), n>=6", statement["local"])
        self.assertIn(
            "(243/625)*(3/5)^(n-6), n>=6",
            statement["exponential"],
        )
        self.assertEqual(
            self.report["route_a_effect"]["tuple_unchanged"],
            ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        )
        nonclaims = " ".join(self.report["claim_boundary"]["not_established"])
        self.assertIn("ordinary-BV spectral gap", nonclaims)
        self.assertIn("determinant", nonclaims)
        self.assertIn("Route B", nonclaims)

    def test_source_lock_forbids_target_data_and_determinant_inference(self) -> None:
        lock = yaml.safe_load(Path(rate.SOURCE_LOCK).read_text(encoding="utf-8"))
        forbidden = " ".join(lock["forbidden_data"])
        self.assertIn("prime tables", forbidden)
        self.assertIn("zero tables", forbidden)
        self.assertIn("different endpoint coefficients", forbidden)
        self.assertIn("determinant", forbidden)
        self.assertEqual(
            lock["determinant_convention"].split(".")[0],
            "No determinant is defined",
        )

    def test_route_a_evaluation_has_complete_schema_and_source_commit(self) -> None:
        evaluation_path = Path(
            "evaluations/route_a/P4-LOGISTIC-UC-BRANCH-MASS-RATE/"
            "20260805T083731Z.yaml"
        )
        evaluation = yaml.safe_load(
            evaluation_path.read_text(encoding="utf-8")
        )
        self.assertEqual(evaluation["a1"]["verdict"], "A1_WEAK")
        self.assertEqual(evaluation["a2"]["verdict"], "A2_FAIL")
        self.assertEqual(evaluation["a3"]["verdict"], "A3_FAIL")
        self.assertEqual(evaluation["a4"]["verdict"], "A4_FAIL")
        self.assertFalse(evaluation["route_b_invocation_allowed"])
        self.assertEqual(
            evaluation["supersedes"],
            "evaluations/route_a/P4-LOGISTIC-UC-BRANCH-MASS-RATE/"
            "20260805T035348Z.yaml",
        )
        self.assertEqual(
            evaluation["source_commit"],
            "dbcb58d21ff93ef842df869c177a3ec3e8c0a785",
        )
        self.assertIn(
            "root_count_discrepancy",
            evaluation["a2"]["metrics"],
        )
        for layer in ("a1", "a2", "a3", "a4"):
            self.assertIn("artifacts", evaluation[layer])

        historical = yaml.safe_load(
            Path(evaluation["supersedes"]).read_text(encoding="utf-8")
        )
        self.assertEqual(
            historical["source_commit"],
            "02727fceef6e7cde3fc4a4452ea409b2faa21f1f",
        )
        self.assertLess(
            historical["evaluation_date"],
            evaluation["evaluation_date"],
        )

        source_commit = evaluation["source_commit"]
        for path in (
            rate.SOURCE_LOCK,
            rate.FORMAL_RESULT,
            rate.GENERATOR,
            "artifacts/p4_logistic_uc_branch_mass_rate/rate_certificate.json",
            "tests/test_p4_logistic_uc_branch_mass_rate.py",
        ):
            subprocess.run(
                ["git", "cat-file", "-e", f"{source_commit}:{path}"],
                check=True,
            )

    def test_formal_result_states_the_rate_and_nonclaims(self) -> None:
        proof = Path(rate.FORMAL_RESULT).read_text(encoding="utf-8")
        self.assertIn("Quantitative physical branch-mass-ratio rate", proof)
        self.assertIn("\\frac{36}{5}\\sqrt{\\delta_{n-1}}", proof)
        self.assertIn("\\frac{243}{625}", proof)
        self.assertIn("common-coefficient calculation", proof)
        self.assertIn("No spectral gap", proof)
        self.assertIn("Hilbert-Polya", proof)

    def test_saved_artifact_is_byte_reproducible(self) -> None:
        expected = json.dumps(self.report, indent=2, sort_keys=True) + "\n"
        artifact = Path(
            "artifacts/p4_logistic_uc_branch_mass_rate/"
            "rate_certificate.json"
        )
        self.assertEqual(artifact.read_text(encoding="utf-8"), expected)

        provenance = self.report["provenance"]
        self.assertIn(
            "configs/source_locks/"
            "P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE.yaml",
            provenance["source_inputs_sha256"],
        )
        self.assertEqual(
            provenance["generator_sha256"],
            rate.file_sha256(provenance["generator"]),
        )
        for path, expected_hash in provenance["source_inputs_sha256"].items():
            self.assertEqual(expected_hash, rate.file_sha256(path))
        self.assertFalse(provenance["external_target_data_used"])

    def test_cli_reproduction_is_byte_identical(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "rate_certificate.json"
            subprocess.run(
                [
                    sys.executable,
                    rate.GENERATOR,
                    "--quiet",
                    "--output",
                    str(output),
                ],
                check=True,
            )
            expected = Path(
                "artifacts/p4_logistic_uc_branch_mass_rate/"
                "rate_certificate.json"
            ).read_bytes()
            self.assertEqual(output.read_bytes(), expected)


if __name__ == "__main__":
    unittest.main()
