from fractions import Fraction
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import sympy as sp
import yaml

from experiments import p4_logistic_uc_polar_nonlattice as nonlattice


class LogisticUcPolarNonLatticeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = nonlattice.build_report()

    def test_every_exact_and_environment_gate_passes(self) -> None:
        self.assertTrue(
            all(self.report["computed_gates"].values()),
            self.report["computed_gates"],
        )
        algebra = self.report["exact_algebra_certificate"]
        self.assertTrue(algebra["computed_gates_passed"])
        self.assertEqual(
            [
                name
                for name, passed in algebra["computed_gates"].items()
                if not passed
            ],
            [],
        )

    def test_frozen_environment_and_exact_data_type(self) -> None:
        environment = self.report["validated_environment"]
        self.assertEqual(environment["sympy"], nonlattice.EXPECTED_SYMPY_VERSION)
        self.assertEqual(
            environment["mpmath"],
            nonlattice.EXPECTED_MPMATH_VERSION,
        )
        self.assertEqual(environment["diagnostic_decimal_digits"], 100)

        lock = yaml.safe_load(
            Path(nonlattice.SOURCE_LOCK).read_text(encoding="utf-8")
        )
        self.assertEqual(lock["cutoff"]["witness_words"], ["R", "LR"])
        self.assertFalse(lock["cutoff"]["additional_words_allowed"])
        self.assertEqual(
            lock["cutoff"]["primitive_period_convention"],
            "full_sum_not_symbol_average",
        )

    def test_fixed_point_and_dynatomic_identities_are_exact(self) -> None:
        algebra = self.report["exact_algebra_certificate"]
        gates = algebra["computed_gates"]
        self.assertTrue(gates["fixed_point_factorization_is_exact"])
        self.assertTrue(gates["right_fixed_multiplier_is_minus_alpha"])
        self.assertTrue(gates["dynatomic_division_is_exact"])
        self.assertTrue(gates["dynatomic_degree_is_12"])
        self.assertTrue(gates["signed_multiplier_remainder_degree_is_10"])
        self.assertTrue(gates["period_two_multiplier_identity_zero_mod_P"])
        self.assertEqual(algebra["dynatomic_degree"], 12)
        self.assertEqual(algebra["signed_multiplier_remainder_degree"], 10)
        self.assertIn("H_u(m)=", algebra["relative_multiplier_polynomial"])

    def test_alpha_cubic_is_irreducible_and_has_norm_2_to_6(self) -> None:
        algebra = self.report["exact_algebra_certificate"]
        self.assertEqual(
            algebra["alpha_minimal_polynomial_descending"],
            [1, 4, 16, -64],
        )
        self.assertEqual(
            algebra["alpha_polynomial_mod_3_values_at_0_1_2"],
            [2, 2, 1],
        )
        self.assertEqual(algebra["alpha_degree"], 3)
        self.assertEqual(algebra["alpha_norm"], "2^6")

    def test_beta_degree_nine_polynomial_and_rabin_certificate(self) -> None:
        algebra = self.report["exact_algebra_certificate"]
        self.assertEqual(
            algebra["beta_minimal_polynomial_descending"],
            nonlattice.BETA_POLYNOMIAL_DESCENDING,
        )
        self.assertEqual(algebra["beta_degree"], 9)
        self.assertEqual(algebra["beta_norm"], "2^36")
        rabin = algebra["beta_rabin_certificate"]
        self.assertEqual(rabin["prime"], 5)
        self.assertEqual(rabin["gcd_with_degree_three_frobenius"], [1])
        self.assertEqual(rabin["x_to_5_ninth_minus_x_remainder"], [0])
        self.assertTrue(rabin["irreducible"])

    def test_norm_ledger_leaves_only_beta_equals_alpha_squared(self) -> None:
        algebra = self.report["exact_algebra_certificate"]
        ledger = algebra["common_field_norm_ledger"]
        self.assertEqual(ledger["Norm_K(alpha)"], "2^(2*d)")
        self.assertEqual(ledger["Norm_K(beta)"], "2^(4*d)")
        self.assertEqual(ledger["forced_exponent_relation"], "a=2*b")
        self.assertEqual(
            ledger["coprime_remaining_case"],
            "a=2, b=1, beta=alpha^2",
        )
        self.assertEqual(algebra["critical_at_3_over_2"], "-1/8")
        self.assertEqual(algebra["critical_at_2"], "2")
        self.assertEqual(algebra["critical_derivative_discriminant"], -8)
        self.assertIn("!= 0", algebra["remaining_case_exclusion"])

        alpha_norm_per_degree = Fraction(6, 3)
        beta_norm_per_degree = Fraction(36, 9)
        self.assertEqual(
            beta_norm_per_degree / alpha_norm_per_degree,
            2,
        )

        u, m = sp.symbols("u m")
        critical = sp.Poly(u**3 - 2 * u**2 + 2 * u - 2, u)
        alpha = 4 * (u - 1)
        relative_multiplier = (
            m**3
            + (48 - 16 * u**2) * m**2
            + 256 * (1 + u**2) * m
            - 4096
        )
        target = -8192 * (u - 2) * (2 * u - 3)
        residual = sp.rem(
            sp.Poly(
                sp.expand(relative_multiplier.subs(m, alpha**2) - target),
                u,
            ),
            critical,
        )
        self.assertTrue(residual.is_zero)
        critical_value = lambda value: (
            value**3 - 2 * value**2 + 2 * value - 2
        )
        self.assertEqual(critical_value(Fraction(3, 2)), Fraction(-1, 8))
        self.assertEqual(critical_value(Fraction(2, 1)), Fraction(2, 1))

    def test_diagnostic_orbit_preserves_itinerary_and_signs(self) -> None:
        diagnostics = self.report["numerical_diagnostics"]
        self.assertEqual(
            diagnostics["proof_weight"],
            "none; identification and reproduction diagnostic only",
        )
        self.assertTrue(diagnostics["itinerary_is_strict_LR"])
        self.assertTrue(diagnostics["signed_multipliers_are_negative"])
        self.assertTrue(diagnostics["positive_multipliers_exceed_one"])
        self.assertLess(float(diagnostics["x_L"]), 0)
        self.assertGreater(float(diagnostics["x_R"]), 0)
        self.assertAlmostEqual(
            float(diagnostics["positive_multiplier_alpha"]),
            2.1747560507683054,
            places=15,
        )
        self.assertAlmostEqual(
            float(diagnostics["positive_multiplier_beta"]),
            4.409001789601263,
            places=15,
        )

    def test_proved_statement_is_non_lattice_but_not_a_determinant(self) -> None:
        self.assertEqual(
            self.report["proved_statement"]["period_ratio"],
            "T_LR/T_R is irrational",
        )
        self.assertEqual(
            self.report["proved_statement"]["roof"],
            "tau=log|G'| is non-lattice",
        )
        self.assertEqual(
            self.report["route_a_effect"]["tuple_unchanged"],
            ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        )
        self.assertFalse(
            self.report["route_a_effect"]["route_b_invocation_allowed"]
        )
        nonclaims = " ".join(self.report["claim_boundary"]["not_established"])
        self.assertIn("Fredholm determinant", nonclaims)
        self.assertIn("Route B", nonclaims)
        self.assertIn("RH", nonclaims)

    def test_source_lock_forbids_target_data_and_decimal_irrationality(self) -> None:
        lock = yaml.safe_load(
            Path(nonlattice.SOURCE_LOCK).read_text(encoding="utf-8")
        )
        forbidden = " ".join(lock["forbidden_data"])
        self.assertIn("prime tables", forbidden)
        self.assertIn("zero tables", forbidden)
        self.assertIn("finite-precision irrationality", lock["data_type"]["excluded"])
        self.assertIn("bounded denominator search", forbidden)
        self.assertIn("full primitive sum", forbidden)
        self.assertIn("No Fredholm determinant", lock["determinant_convention"])

    def test_route_a_evaluation_keeps_a2_and_route_b_closed(self) -> None:
        evaluation_path = Path(
            "evaluations/route_a/P4-LOGISTIC-UC-POLAR-NONLATTICE/"
            "20260805T110654Z.yaml"
        )
        evaluation = yaml.safe_load(
            evaluation_path.read_text(encoding="utf-8")
        )
        self.assertEqual(evaluation["a1"]["verdict"], "A1_WEAK")
        self.assertEqual(evaluation["a1"]["evidence_status"], "PROVED")
        self.assertEqual(evaluation["a2"]["verdict"], "A2_FAIL")
        self.assertEqual(evaluation["a3"]["verdict"], "A3_FAIL")
        self.assertEqual(evaluation["a4"]["verdict"], "A4_FAIL")
        self.assertEqual(
            evaluation["overall_verdict"],
            "ROUTE_A_EXPLORATORY",
        )
        self.assertEqual(
            evaluation["scoped_audit_verdict"],
            "GO_WITH_LIMITATIONS",
        )
        self.assertFalse(evaluation["route_b_invocation_allowed"])
        self.assertTrue(
            evaluation["a1"]["metrics"]["intrinsic_roof_non_lattice"]
        )
        self.assertFalse(
            evaluation["a2"]["metrics"]["fredholm_determinant_defined"]
        )

        source_commit = evaluation["source_commit"]
        self.assertEqual(
            source_commit,
            "36a38f0db16652bf0e0c1459be6c69f6bdafec12",
        )
        for path in (
            nonlattice.SOURCE_LOCK,
            nonlattice.FORMAL_RESULT,
            nonlattice.GENERATOR,
            nonlattice.ARTIFACT,
            "tests/test_p4_logistic_uc_polar_nonlattice.py",
        ):
            subprocess.run(
                ["git", "cat-file", "-e", f"{source_commit}:{path}"],
                check=True,
            )

    def test_formal_result_states_exact_norm_proof_and_nonclaims(self) -> None:
        proof = Path(nonlattice.FORMAL_RESULT).read_text(encoding="utf-8")
        self.assertIn("Exact non-lattice theorem", proof)
        self.assertIn("N_{\\mathbb Q(\\alpha)/\\mathbb Q}(\\alpha)=2^6", proof)
        self.assertIn("N_{\\mathbb Q(\\beta)/\\mathbb Q}(\\beta)=2^{36}", proof)
        self.assertIn("a=2b", proof)
        self.assertIn("H_u(\\alpha^2)", proof)
        self.assertIn("\\notin\\mathbb Q", proof)
        self.assertIn("does not establish a", proof)
        self.assertIn("Hilbert--Pólya", proof)

    def test_saved_artifact_is_byte_reproducible_and_hashed(self) -> None:
        expected_report = dict(self.report)
        expected_report["computed_gates_passed"] = all(
            expected_report["computed_gates"].values()
        )
        expected = json.dumps(expected_report, indent=2, sort_keys=True) + "\n"
        artifact = Path(nonlattice.ARTIFACT)
        self.assertEqual(artifact.read_text(encoding="utf-8"), expected)

        provenance = self.report["provenance"]
        self.assertEqual(
            provenance["generator_sha256"],
            nonlattice.file_sha256(provenance["generator"]),
        )
        for path, expected_hash in provenance["source_inputs_sha256"].items():
            self.assertEqual(expected_hash, nonlattice.file_sha256(path))
        self.assertFalse(provenance["external_target_data_used"])

    def test_cli_reproduction_is_byte_identical(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "nonlattice_certificate.json"
            subprocess.run(
                [
                    sys.executable,
                    nonlattice.GENERATOR,
                    "--quiet",
                    "--output",
                    str(output),
                ],
                check=True,
            )
            self.assertEqual(
                output.read_bytes(),
                Path(nonlattice.ARTIFACT).read_bytes(),
            )


if __name__ == "__main__":
    unittest.main()
