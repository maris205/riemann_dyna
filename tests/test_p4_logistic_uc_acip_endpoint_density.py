from decimal import Decimal, localcontext
import json
from pathlib import Path
import unittest

import yaml

from experiments import p4_logistic_uc_acip_endpoint_density as endpoint


class LogisticUcAcipEndpointDensityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = endpoint.build_report()

    def test_algebraic_identity_gates_close(self) -> None:
        gates = self.report["computed_gates"]
        self.assertTrue(gates["critical_polynomial_residual_below_1e_170"])
        self.assertTrue(gates["band_identity_residual_below_1e_170"])
        self.assertTrue(gates["multiplier_identity_residual_below_1e_170"])

    def test_polar_conjugate_has_strict_expansion_margin(self) -> None:
        constants = self.report["constants"]
        lower_bound = Decimal(constants["uniform_expansion_lower_bound"])
        multiplier = Decimal(constants["fixed_postcritical_multiplier"])
        sampled = Decimal(
            self.report["computed_diagnostics"]["sampled_polar_minimum"]
        )
        self.assertGreater(lower_bound, 1)
        self.assertLess(abs(lower_bound - multiplier), Decimal("1e-170"))
        self.assertLess(abs(lower_bound - sampled), Decimal("1e-170"))
        self.assertTrue(
            self.report["computed_gates"][
                "polar_grid_is_monotone_decreasing"
            ]
        )

    def test_inverse_jacobian_has_the_proved_endpoint_coefficient(self) -> None:
        rows = self.report["computed_diagnostics"]["inverse_jacobian_rows"]
        errors = [Decimal(row["relative_error"]) for row in rows]
        self.assertEqual([int(row["t_exponent"]) for row in rows], [8, 16, 32, 64])
        self.assertLess(errors[-1], Decimal("1e-7"))
        self.assertTrue(all(right < left for left, right in zip(errors, errors[1:])))

    def test_mass_ratio_closed_forms_agree(self) -> None:
        constants = self.report["constants"]
        ratio = Decimal(constants["endpoint_mass_ratio"])
        ratio_u = Decimal(constants["endpoint_mass_ratio_as_U_c_squared_over_4"])
        length_ratio = Decimal(constants["endpoint_length_ratio"])
        with localcontext() as context:
            context.prec = endpoint.DECIMAL_DIGITS
            self.assertLess(abs(ratio - ratio_u), Decimal("1e-170"))
            self.assertLess(abs(length_ratio - ratio * ratio), Decimal("1e-170"))
        self.assertAlmostEqual(float(ratio), 0.5957439419765594, places=15)

    def test_formal_claims_are_separated_from_computed_gates(self) -> None:
        claims = self.report["formal_claims"]
        self.assertEqual(claims["endpoint_density"]["status"], "PROVED")
        self.assertEqual(
            claims["physical_branch_mass_ratio"]["status"], "PROVED"
        )
        self.assertEqual(
            claims["raw_first_return_uniform_expansion"]["status"],
            "REFUTED",
        )
        self.assertTrue(
            claims["raw_first_return_uniform_expansion"][
                "unchanged_by_this_audit"
            ]
        )
        self.assertTrue(self.report["computed_diagnostics_passed"])
        route_a = self.report["route_a_effect"]
        self.assertEqual(route_a["local_endpoint_audit_verdict"], "GO_WITH_LIMITATIONS")
        self.assertEqual(route_a["candidate_recommended_verdict"], "REVISE")

    def test_source_lock_matches_the_audit(self) -> None:
        lock = yaml.safe_load(Path(endpoint.SOURCE_LOCK).read_text(encoding="utf-8"))
        self.assertEqual(lock["audit_id"], endpoint.AUDIT_ID)
        self.assertEqual(lock["parent_audit_id"], endpoint.PARENT_AUDIT_ID)
        self.assertEqual(lock["lock_version"], 1)
        self.assertEqual(
            lock["cutoff"]["polar_derivative_grid_intervals"],
            endpoint.POLAR_GRID_INTERVALS,
        )
        self.assertEqual(
            lock["cutoff"]["algebraic_diagnostic_t_exponents"],
            list(endpoint.T_EXPONENTS),
        )
        self.assertIn("Jiang-Ruelle", lock["data_type"]["primary"])
        self.assertIn("No determinant", lock["determinant_convention"])
        corrected = lock["published_source_lock"]["corrected_formula_cross_check"]
        self.assertIn("equation (1.1)", corrected["citation"])
        self.assertEqual(corrected["arxiv"], "2008.01654v4")

    def test_formal_and_literature_sources_exist(self) -> None:
        self.assertTrue(Path(endpoint.FORMAL_RESULT).is_file())
        self.assertTrue(Path(endpoint.LITERATURE_AUDIT).is_file())
        proof = Path(endpoint.FORMAL_RESULT).read_text(encoding="utf-8")
        self.assertIn("h(-\\rho+t)", proof)
        self.assertIn("\\frac{1}{2U_c(U_c-1)}", proof)
        self.assertIn("does not remove `OBR-009`", proof)
        self.assertIn("unique **absolutely continuous**", proof)
        self.assertIn("corrected equation (1.1)", proof)
        self.assertIn("g_A=2h", proof)

    def test_saved_artifact_is_byte_reproducible(self) -> None:
        expected = json.dumps(self.report, indent=2, sort_keys=True) + "\n"
        actual = Path(
            "artifacts/p4_logistic_uc_acip_endpoint_density/structural_audit.json"
        ).read_text(encoding="utf-8")
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
