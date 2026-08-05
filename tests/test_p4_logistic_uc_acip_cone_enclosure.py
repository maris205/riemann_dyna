from decimal import Decimal, localcontext
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml

from experiments import p4_logistic_uc_acip_cone_enclosure as cone


class LogisticUcAcipConeEnclosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = cone.build_report()

    def test_every_certification_gate_passes(self) -> None:
        self.assertTrue(self.report["computed_gates_passed"])
        failed = [
            name
            for name, passed in self.report["computed_gates"].items()
            if not passed
        ]
        self.assertEqual(failed, [])

    def test_pi_bracket_is_ordered_and_has_the_frozen_width(self) -> None:
        bracket = self.report["certified_root_bracket"]
        lower = Decimal(bracket["pi_lower"])
        upper = Decimal(bracket["pi_upper"])
        with localcontext() as context:
            context.prec = 120
            self.assertLess(lower, upper)
            self.assertEqual(upper - lower, Decimal("1e-100"))
        self.assertTrue(
            self.report["computed_gates"][
                "pi_bracket_is_certified_by_machin_series"
            ]
        )
        certificate = bracket["pi_certificate"]
        self.assertEqual(certificate["atan_1_over_5_terms"], 100)
        self.assertEqual(certificate["atan_1_over_239_terms"], 30)
        self.assertTrue(
            self.report["computed_gates"][
                "pi_bracket_is_certified_by_machin_series"
            ]
        )

    def test_cone_constants_close_the_invariance_inequality(self) -> None:
        ledger = self.report["cone_ledger"]
        self.assertEqual(ledger["inverse_branch_contraction_upper"], "3/5")
        self.assertEqual(ledger["log_inverse_weight_derivative_upper"], "3/10")
        self.assertEqual(ledger["log_lipschitz_cone_slope"], "3/4")
        self.assertEqual(
            ledger["invariance_inequality"],
            "3/10 + (3/5)*(3/4) = 3/4",
        )

    def test_conditional_and_full_density_normalizations_are_distinct(self) -> None:
        bounds = self.report["certified_enclosures"]
        g_lower = Decimal(bounds["conditional_x_density_g_A_0"]["lower"])
        g_upper = Decimal(bounds["conditional_x_density_g_A_0"]["upper"])
        h_lower = Decimal(bounds["full_physical_density_h_0"]["lower"])
        h_upper = Decimal(bounds["full_physical_density_h_0"]["upper"])

        rounding_unit = Decimal(1).scaleb(-cone.OUTPUT_PLACES)
        with localcontext() as context:
            context.prec = 80
            self.assertLessEqual(abs(g_lower - 2 * h_lower), 2 * rounding_unit)
            self.assertLessEqual(abs(g_upper - 2 * h_upper), 2 * rounding_unit)
        self.assertEqual(bounds["normalization_identity"], "g_A(0)=2*h(0)")
        self.assertGreater(h_lower, Decimal("0.15"))
        self.assertLess(h_upper, Decimal("0.5"))

    def test_endpoint_coefficient_is_positive_and_ordered(self) -> None:
        bounds = self.report["certified_enclosures"]["endpoint_coefficient_C_h"]
        lower = Decimal(bounds["lower"])
        upper = Decimal(bounds["upper"])
        self.assertGreater(lower, 0)
        self.assertLess(lower, upper)
        self.assertLess(upper, Decimal("0.23"))

    def test_explicit_endpoint_remainder_is_frozen(self) -> None:
        remainder = self.report["explicit_endpoint_remainder"]
        self.assertEqual(remainder["t_range"], "0 < t <= 1/200")
        self.assertIn("61/100", remainder["statement"])
        self.assertEqual(remainder["local_x_radius"], "1/20")
        self.assertEqual(remainder["local_h_lipschitz_upper"], "27/10")

    def test_selected_finite_branch_masses_are_certified(self) -> None:
        rows = self.report["finite_branch_mass_enclosures"]
        self.assertEqual(
            [row["physical_return_label"] for row in rows],
            [12, 14, 16, 18],
        )
        previous_upper = None
        for row in rows:
            self.assertTrue(row["endpoint_radius_gate_passed"])
            lower = Decimal(row["certified_mass"]["lower"])
            upper = Decimal(row["certified_mass"]["upper"])
            self.assertGreater(lower, 0)
            self.assertLess(lower, upper)
            if previous_upper is not None:
                self.assertLess(upper, previous_upper)
            previous_upper = upper

    def test_error_budget_does_not_use_a_finite_rank_residual_as_proof(self) -> None:
        budget = self.report["error_budget"]
        for key in (
            "discretization",
            "truncation",
            "rounding",
            "normalization",
            "iteration_stopping",
            "resolvent_tail",
        ):
            self.assertIn(key, budget)
        self.assertIn("not used", budget["finite_rank_projection_or_quadrature"])
        self.assertIn("not used", budget["invariant_vector_residual"])
        self.assertIn("not used", budget["truncation_or_resolvent_tail"])
        self.assertIn("g_A(0)", budget["normalization_conversion"])
        self.assertNotIn(
            "certified finite-rank resolvent",
            self.report["claim_boundary"]["established"],
        )

    def test_source_lock_matches_the_audit(self) -> None:
        lock = yaml.safe_load(Path(cone.SOURCE_LOCK).read_text(encoding="utf-8"))
        self.assertEqual(lock["audit_id"], cone.AUDIT_ID)
        self.assertEqual(lock["parent_audit_id"], cone.PARENT_AUDIT_ID)
        self.assertEqual(lock["lock_version"], 1)
        self.assertEqual(lock["cutoff"]["cone_slope"], "3/4")
        self.assertEqual(lock["cutoff"]["reported_physical_returns"], [12, 14, 16, 18])
        self.assertIn("g_A=2h", lock["normalization"])
        self.assertIn(
            "finite-rank stationary-vector residual",
            " ".join(lock["forbidden_data"]),
        )
        self.assertEqual(
            lock["error_budget_categories"],
            [
                "discretization",
                "truncation",
                "rounding",
                "normalization",
                "iteration_stopping",
                "resolvent_tail",
            ],
        )

        evaluation_path = Path(
            "evaluations/route_a/P4-LOGISTIC-UC-ACIP-CONE-ENCLOSURE/20260804T233200Z.yaml"
        )
        evaluation = yaml.safe_load(evaluation_path.read_text(encoding="utf-8"))
        self.assertEqual(evaluation["audit_id"], cone.AUDIT_ID)
        self.assertEqual(evaluation["a1"]["verdict"], "A1_WEAK")
        self.assertEqual(evaluation["a2"]["verdict"], "A2_FAIL")
        self.assertEqual(evaluation["a3"]["verdict"], "A3_FAIL")
        self.assertEqual(evaluation["a4"]["verdict"], "A4_FAIL")
        self.assertFalse(evaluation["route_b_invocation_allowed"])
        self.assertFalse(evaluation["a1"]["metrics"]["finite_rank_resolvent_certified"])

    def test_formal_result_records_the_normalization_and_nonclaims(self) -> None:
        proof = Path(cone.FORMAL_RESULT).read_text(encoding="utf-8")
        self.assertIn("g_A(0)=\\frac{w(0)}{\\rho}", proof)
        self.assertIn("h(0)=\\frac{g_A(0)}2", proof)
        self.assertIn("\\frac{61}{100}", proof)
        self.assertIn("finite-rank", proof)
        self.assertIn("not used", proof)
        self.assertIn("Hilbert-Pólya", proof)

    def test_saved_artifact_is_byte_reproducible(self) -> None:
        expected = json.dumps(self.report, indent=2, sort_keys=True) + "\n"
        artifact_path = Path(
            "artifacts/p4_logistic_uc_acip_cone_enclosure/certified_bounds.json"
        )
        self.assertEqual(artifact_path.read_text(encoding="utf-8"), expected)

        provenance = self.report["provenance"]
        self.assertEqual(
            provenance["generator_sha256"],
            cone.file_sha256(provenance["generator"]),
        )
        for path, expected_sha in provenance["source_inputs_sha256"].items():
            self.assertEqual(expected_sha, cone.file_sha256(path))
        self.assertFalse(provenance["external_target_data_used"])
        self.assertEqual(provenance["reproduction_command"], cone.REPRODUCTION_COMMAND)

    def test_cli_reproduction_is_byte_identical(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "certified_bounds.json"
            subprocess.run(
                [
                    sys.executable,
                    "experiments/p4_logistic_uc_acip_cone_enclosure.py",
                    "--quiet",
                    "--output",
                    str(output),
                ],
                check=True,
            )
            expected = Path(
                "artifacts/p4_logistic_uc_acip_cone_enclosure/certified_bounds.json"
            ).read_bytes()
            self.assertEqual(output.read_bytes(), expected)


if __name__ == "__main__":
    unittest.main()
