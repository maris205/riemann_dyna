from decimal import Decimal, localcontext
from pathlib import Path
import unittest

import yaml

from experiments import p4_logistic_uc_first_return_support as support


SOURCE_LOCK = Path(
    "configs/source_locks/P4-LOGISTIC-UC-POLAR-INTRINSIC-ROOF.yaml"
)


class LogisticUcPolarIntrinsicRoofLockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lock = yaml.safe_load(SOURCE_LOCK.read_text(encoding="utf-8"))

    def test_identity_and_parent_are_frozen(self) -> None:
        self.assertEqual(
            self.lock["audit_id"],
            "P4-LOGISTIC-UC-POLAR-INTRINSIC-ROOF",
        )
        self.assertEqual(
            self.lock["parent_audit_id"],
            "P4-LOGISTIC-UC-BRANCH-MASS-RATE",
        )
        self.assertEqual(self.lock["lock_version"], 1)
        self.assertFalse(self.lock["formal_candidate"])

    def test_exact_map_branches_and_roof_are_explicit(self) -> None:
        obj = self.lock["mathematical_object"]
        self.assertIn("S=-T=rho-2*U_c^2*x^2+U_c^3*x^4", obj["parity_reduced_map"])
        self.assertIn("q(theta)=rho*sin(theta)", obj["polar_coordinate"])
        self.assertIn("phi_L'=+a", obj["inverse_branches"])
        self.assertIn("phi_R'=-a", obj["inverse_branches"])
        self.assertIn("tau(theta)=log|G'(theta)|", obj["intrinsic_roof"])
        self.assertIn("log|(G^n)'(theta)|", obj["suspension_period"])

    def test_roof_endpoint_values_are_strictly_positive(self) -> None:
        with localcontext() as context:
            context.prec = 100
            u = (
                Decimal(support.U_LOWER_TEXT)
                + Decimal(support.U_UPPER_TEXT)
            ) / 2
            rho = u - 1
            polar_derivative = Decimal(4) / (u * u)
            center_derivative = (Decimal(8) / u).sqrt()
            self.assertGreater(polar_derivative, 1)
            self.assertGreater(center_derivative, polar_derivative)
            self.assertGreater(polar_derivative.ln(), 0)
            self.assertGreater(center_derivative.ln(), 0)

            t_left = ((1 - rho) / u).sqrt()
            t_right = ((1 + rho) / u).sqrt()
            self.assertLess(abs(t_left - rho), Decimal("1e-95"))
            self.assertLess(abs(t_right - 1), Decimal("1e-95"))

    def test_markov_and_quotient_ledgers_are_not_mixed(self) -> None:
        phase_space = self.lock["mathematical_object"]["markov_phase_space"]
        determinant = self.lock["determinant_convention"]
        self.assertIn("0_L and 0_R remain distinct", phase_space)
        self.assertIn("may not be mixed", phase_space)
        self.assertIn("doubled two-component Markov extension", determinant["endpoint_multiplicity"])
        self.assertIn("different object", determinant["endpoint_multiplicity"])

    def test_physical_and_roof_clocks_are_separate(self) -> None:
        clocks = self.lock["clock"]
        self.assertIn("exactly two iterates of f", clocks["physical_discrete_clock"])
        self.assertIn("tau=log|G'|", clocks["intrinsic_suspension_clock"])
        self.assertIn("must be reported separately", clocks["separation_rule"])
        self.assertIn("Neither may be substituted", clocks["separation_rule"])

    def test_function_space_and_weighted_family_are_frozen(self) -> None:
        data_type = self.lock["data_type"]
        self.assertIn("epsilon=1/1000", data_type["complex_domain"])
        self.assertIn("v_L(0)=v_R(0)", data_type["analytic_function_space"])
        self.assertIn("exp(s*Log(a(z)))", data_type["weighted_transfer_family"])
        self.assertIn("potential -s*tau", data_type["weighted_transfer_family"])

    def test_determinant_is_one_conditional_ledger(self) -> None:
        convention = self.lock["determinant_convention"]
        self.assertIn("D_pol(s)=det_Fr(I-L_s)", convention["sole_intended_object"])
        self.assertIn("only if", convention["sole_intended_object"])
        self.assertIn("not an established Fredholm determinant", convention["sole_intended_object"])
        self.assertEqual(len(convention["forbidden_ledgers"]), 4)

    def test_data_firewall_and_frozen_controls_are_complete(self) -> None:
        forbidden = " ".join(self.lock["forbidden_data"])
        self.assertIn("prime tables", forbidden)
        self.assertIn("zero tables", forbidden)
        self.assertIn("changing epsilon", forbidden)
        self.assertIn("physical branch masses", forbidden)
        self.assertIn("signed branch orientation", forbidden)
        self.assertEqual(self.lock["training_split"].split(";")[0], "empty")

    def test_sealed_next_audit_is_non_lattice_only(self) -> None:
        cutoff = self.lock["cutoff"]
        self.assertEqual(cutoff["sealed_non_lattice_witness_words"], ["R", "LR"])
        self.assertIn("Freeze the object only", cutoff["current_checkpoint_scope"])
        next_test = self.lock["next_smallest_test"]
        self.assertIn("R and LR", next_test)
        self.assertIn("Do not audit Fredholm", next_test)
        self.assertIn("do not", next_test.lower())
        self.assertIn("target zeros", next_test.lower())

    def test_route_status_is_defined_but_not_evaluated(self) -> None:
        status = self.lock["route_status_at_lock"]
        self.assertEqual(
            status["route_a_tuple_inherited"],
            ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        )
        self.assertFalse(status["route_a_evaluation_performed"])
        self.assertFalse(status["route_b_invocation_allowed"])
        self.assertFalse(status["formal_candidate_created"])
        self.assertEqual(status["checkpoint_verdict"], "DEFINED_NOT_EVALUATED")


if __name__ == "__main__":
    unittest.main()
