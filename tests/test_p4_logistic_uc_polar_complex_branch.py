import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from flint import arb, ctx
import mpmath as mp
import yaml

from experiments import p4_logistic_uc_first_return_support as support
from experiments import p4_logistic_uc_polar_complex_branch as complex_branch


class LogisticUcPolarComplexBranchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = complex_branch.build_report()
        cls.lock = yaml.safe_load(
            Path(complex_branch.SOURCE_LOCK).read_text(encoding="utf-8")
        )

    def test_every_exact_interval_and_environment_gate_passes(self) -> None:
        self.assertTrue(
            all(self.report["computed_gates"].values()),
            self.report["computed_gates"],
        )
        exact = self.report["exact_identity_certificate"]
        analytic = self.report["analytic_bound_certificate"]
        self.assertTrue(exact["computed_gates_passed"])
        self.assertTrue(analytic["computed_gates_passed"])
        self.assertEqual(
            [
                name
                for name, passed in exact["computed_gates"].items()
                if not passed
            ],
            [],
        )
        self.assertEqual(
            [
                name
                for name, passed in analytic["computed_gates"].items()
                if not passed
            ],
            [],
        )

    def test_frozen_environment_radius_and_branch_pairs(self) -> None:
        environment = self.report["validated_environment"]
        self.assertEqual(
            environment["python_flint"],
            complex_branch.EXPECTED_PYTHON_FLINT_VERSION,
        )
        self.assertEqual(
            environment["flint"],
            complex_branch.EXPECTED_FLINT_VERSION,
        )
        self.assertEqual(
            environment["sympy"],
            complex_branch.EXPECTED_SYMPY_VERSION,
        )
        self.assertEqual(environment["arb_decimal_digits"], 100)
        self.assertEqual(
            self.lock["cutoff"]["complex_neighborhood_radius"],
            "1/1000",
        )
        self.assertEqual(
            self.lock["cutoff"]["branch_pairs"],
            ["LL", "LR", "RL", "RR"],
        )

    def test_exact_uc_and_real_jacobian_identities_close(self) -> None:
        exact = self.report["exact_identity_certificate"]
        gates = exact["computed_gates"]
        self.assertTrue(gates["u_rho_squared_equals_one_minus_rho"])
        self.assertTrue(gates["u_cubed_rho_equals_two"])
        self.assertTrue(
            gates[
                "one_plus_S_equals_u_times_one_minus_u_x_squared_squared"
            ]
        )
        self.assertTrue(gates["real_log_a_derivative_formula_is_exact"])
        self.assertTrue(
            gates["real_a_maximum_endpoint_value_is_u_squared_over_four"]
        )
        self.assertIn("<0", exact["identities"]["d_dt_log_a_0"])
        self.assertEqual(
            exact["identities"]["max_real_a_0"],
            "a_0(rho)=u^2/4",
        )

    def test_right_half_plane_and_t_perturbation_are_certified(self) -> None:
        certificate = self.report["analytic_bound_certificate"]
        gates = certificate["computed_gates"]
        self.assertTrue(gates["radicand_real_part_above_safe_lower"])
        self.assertTrue(gates["principal_t_real_part_above_safe_lower"])
        self.assertTrue(gates["t_perturbation_below_safe_upper"])
        self.assertTrue(gates["t_perturbation_is_smaller_than_rho"])
        self.assertTrue(gates["log_variation_below_safe_upper"])
        self.assertTrue(
            gates["log_variation_keeps_a_in_the_right_half_plane"]
        )

        previous_precision = ctx.prec
        try:
            ctx.dps = 100
            u = complex_branch.root_ball()
            rho = u - 1
            epsilon = arb(1) / 1000
            cosh_epsilon = epsilon.cosh()
            lower = (1 - rho * cosh_epsilon) / u
            delta = (rho / u) * epsilon * cosh_epsilon
            m = lower.sqrt()
            d = delta / (m + rho)
            self.assertGreater(
                lower,
                arb(complex_branch.RADICAND_REAL_PART_SAFE_LOWER),
            )
            self.assertLess(
                d,
                arb(complex_branch.T_PERTURBATION_SAFE_UPPER),
            )
        finally:
            ctx.prec = previous_precision

    def test_one_contraction_bound_gives_all_four_compact_inclusions(self) -> None:
        certificate = self.report["analytic_bound_certificate"]
        gates = certificate["computed_gates"]
        self.assertTrue(gates["complex_contraction_below_safe_upper"])
        self.assertTrue(gates["complex_contraction_is_strictly_below_one"])
        self.assertTrue(gates["image_radius_below_safe_upper"])
        self.assertTrue(gates["image_radius_is_strictly_below_epsilon"])
        self.assertTrue(gates["compact_margin_above_safe_lower"])

        inclusions = certificate["four_branch_inclusions"]
        self.assertEqual(
            set(inclusions).intersection({"LL", "LR", "RL", "RR"}),
            {"LL", "LR", "RL", "RR"},
        )
        self.assertEqual(
            inclusions["common_image_radius_upper"],
            complex_branch.IMAGE_RADIUS_SAFE_UPPER,
        )
        self.assertEqual(
            inclusions["common_compact_margin_lower"],
            complex_branch.COMPACT_MARGIN_SAFE_LOWER,
        )

    def test_complex_primitive_satisfies_inverse_identity_diagnostically(self) -> None:
        mp.mp.dps = 75
        u = (
            mp.mpf(support.U_LOWER_TEXT) + mp.mpf(support.U_UPPER_TEXT)
        ) / 2
        rho = u - 1

        def inverse_magnitude(z: mp.mpc | mp.mpf) -> mp.mpc | mp.mpf:
            t = mp.sqrt((1 + rho * mp.sin(z)) / u)
            return mp.sqrt(1 + t) * mp.sqrt(rho + t) / (4 * t)

        def phi_right(z: mp.mpc | mp.mpf) -> mp.mpc | mp.mpf:
            base = mp.pi / 2
            displacement = z - base
            return -displacement * mp.quad(
                lambda parameter: inverse_magnitude(
                    base + parameter * displacement
                ),
                [0, 1],
            )

        def reflected_map(x: mp.mpc | mp.mpf) -> mp.mpc | mp.mpf:
            return rho - 2 * u**2 * x**2 + u**3 * x**4

        sample_points = (
            -mp.pi / 2,
            mp.mpc("-1.2", "0.0007"),
            mp.mpc("-0.3", "-0.0006"),
            mp.mpc("0.3", "0.0007"),
            mp.mpc("1.2", "-0.0006"),
            mp.pi / 2 + mp.mpc(0, "0.0005"),
        )
        for target in sample_points:
            right = phi_right(target)
            left = -right
            for branch in (left, right):
                residual = (
                    reflected_map(rho * mp.sin(branch))
                    - rho * mp.sin(target)
                )
                self.assertLess(abs(residual), mp.mpf("1e-65"))
        self.assertLess(
            abs(phi_right(-mp.pi / 2) - mp.pi / 2),
            mp.mpf("1e-65"),
        )

    def test_common_log_and_primitive_definitions_are_not_scalar_branches(self) -> None:
        object_lock = self.lock["mathematical_object"]
        self.assertIn(
            "principal holomorphic square root",
            object_lock["common_t_and_jacobian"],
        )
        self.assertIn(
            "not from separate scalar asin",
            object_lock["composite_inverse_branches"],
        )
        self.assertIn(
            "principal logarithms on right-half-plane arguments",
            object_lock["common_log_germ"],
        )
        self.assertIn("ell=log(a)<0", object_lock["common_log_germ"])
        mathematical_object = self.report["mathematical_object"]
        self.assertEqual(
            mathematical_object["branches"]["signed_derivatives"],
            ["phi_L'=+a", "phi_R'=-a"],
        )

    def test_matching_space_corollary_does_not_claim_nuclearity(self) -> None:
        corollary = self.report["matching_space_corollary"]
        self.assertTrue(
            corollary["weighted_formula_is_well_defined_for_each_fixed_s"]
        )
        self.assertTrue(
            corollary[
                "two_output_components_are_restrictions_of_one_function_on_U"
            ]
        )
        self.assertTrue(corollary["matching_at_zero_is_preserved"])
        self.assertFalse(corollary["nuclearity_claimed"])
        self.assertFalse(corollary["fredholm_determinant_claimed"])
        self.assertEqual(
            self.report["route_a_effect"]["tuple_unchanged"],
            ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        )
        self.assertFalse(
            self.report["route_a_effect"]["route_b_invocation_allowed"]
        )
        self.assertTrue(
            self.report["proved_statement"][
                "global_univalence_of_both_branches"
            ]
        )

    def test_route_a_evaluation_keeps_a2_and_route_b_closed(self) -> None:
        evaluation_path = Path(
            "evaluations/route_a/P4-LOGISTIC-UC-POLAR-COMPLEX-BRANCH/"
            "20260805T125236Z.yaml"
        )
        evaluation = yaml.safe_load(
            evaluation_path.read_text(encoding="utf-8")
        )
        self.assertEqual(evaluation["a1"]["verdict"], "A1_WEAK")
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
            evaluation["a2"]["metrics"][
                "all_four_compact_inclusions_proved"
            ]
        )
        self.assertFalse(
            evaluation["a2"]["metrics"]["nuclearity_proved"]
        )
        self.assertFalse(
            evaluation["a2"]["metrics"]["fredholm_determinant_defined"]
        )

        source_commit = evaluation["source_commit"]
        self.assertEqual(
            source_commit,
            "3ae5e23508e27129cfa5910473b944026b904ea3",
        )
        for path in (
            complex_branch.SOURCE_LOCK,
            complex_branch.FORMAL_RESULT,
            complex_branch.GENERATOR,
            complex_branch.ARTIFACT,
            "tests/test_p4_logistic_uc_polar_complex_branch.py",
        ):
            subprocess.run(
                ["git", "cat-file", "-e", f"{source_commit}:{path}"],
                check=True,
            )

    def test_source_lock_preserves_data_firewall_and_scope(self) -> None:
        forbidden = " ".join(self.lock["forbidden_data"])
        self.assertIn("prime tables", forbidden)
        self.assertIn("zero tables", forbidden)
        self.assertIn("shrinking epsilon", forbidden)
        self.assertIn("separately choosing sqrt, asin, or Log", forbidden)
        self.assertIn("complex grid", forbidden)
        self.assertIn("nuclearity", forbidden)
        self.assertIn("Route B", forbidden)
        self.assertIn(
            "No Fredholm determinant",
            self.lock["determinant_convention"],
        )

    def test_formal_result_states_bounds_inclusions_and_nonclaims(self) -> None:
        proof = Path(complex_branch.FORMAL_RESULT).read_text(
            encoding="utf-8"
        )
        self.assertIn("one complex stadium", proof)
        self.assertIn("separate principal square roots", proof)
        self.assertIn("M=0.5962503819920866", proof)
        self.assertIn("L=0.0008500128404207560", proof)
        self.assertIn("globally univalent", proof)
        self.assertIn("0.0004037496180079133", proof)
        self.assertIn("`LL`, `LR`, `RL`, and `RR`", proof)
        self.assertIn("not a nuclearity theorem", proof)
        self.assertIn("Hilbert--Pólya", proof)

    def test_saved_artifact_is_byte_reproducible_and_hashed(self) -> None:
        expected_report = dict(self.report)
        expected_report["computed_gates_passed"] = all(
            expected_report["computed_gates"].values()
        )
        expected = json.dumps(expected_report, indent=2, sort_keys=True) + "\n"
        artifact = Path(complex_branch.ARTIFACT)
        self.assertEqual(artifact.read_text(encoding="utf-8"), expected)

        provenance = self.report["provenance"]
        self.assertEqual(
            provenance["generator_sha256"],
            complex_branch.file_sha256(provenance["generator"]),
        )
        for path, expected_hash in provenance["source_inputs_sha256"].items():
            self.assertEqual(
                expected_hash,
                complex_branch.file_sha256(path),
            )
        self.assertFalse(provenance["external_target_data_used"])

    def test_cli_reproduction_is_byte_identical(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "complex_branch_certificate.json"
            subprocess.run(
                [
                    sys.executable,
                    complex_branch.GENERATOR,
                    "--quiet",
                    "--output",
                    str(output),
                ],
                check=True,
            )
            self.assertEqual(
                output.read_bytes(),
                Path(complex_branch.ARTIFACT).read_bytes(),
            )


if __name__ == "__main__":
    unittest.main()
