from fractions import Fraction
from pathlib import Path
import unittest

import mpmath as mp
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
        self.assertEqual(self.lock["lock_version"], 2)
        self.assertEqual(self.lock["supersedes_lock_version"], 1)
        self.assertFalse(self.lock["formal_candidate"])

    def test_exact_map_branches_and_roof_are_explicit(self) -> None:
        obj = self.lock["mathematical_object"]
        self.assertIn("S=-T=rho-2*U_c^2*x^2+U_c^3*x^4", obj["parity_reduced_map"])
        self.assertIn("q(theta)=rho*sin(theta)", obj["polar_coordinate"])
        self.assertIn("phi_L'=+a", obj["inverse_branches"])
        self.assertIn("phi_R'=-a", obj["inverse_branches"])
        self.assertIn("tau(theta)=log|G'(theta)|", obj["intrinsic_roof"])
        self.assertIn("log|(G^n)'(theta)|", obj["suspension_period"])

    def test_real_inverse_formula_and_signed_derivatives(self) -> None:
        mp.mp.dps = 80
        u = (
            mp.mpf(support.U_LOWER_TEXT) + mp.mpf(support.U_UPPER_TEXT)
        ) / 2
        rho = u - 1

        def reduced_map(x: mp.mpf) -> mp.mpf:
            return rho - 2 * u**2 * x**2 + u**3 * x**4

        def phi(eta: mp.mpf, sign: int) -> mp.mpf:
            t = mp.sqrt((1 + rho * mp.sin(eta)) / u)
            return sign * mp.asin(mp.sqrt((1 - t) / u) / rho)

        def inverse_magnitude(eta: mp.mpf) -> mp.mpf:
            t = mp.sqrt((1 + rho * mp.sin(eta)) / u)
            return mp.sqrt((1 + t) * (rho + t)) / (4 * t)

        for eta_text in ("-1.1", "-0.4", "0", "0.7", "1.2"):
            eta = mp.mpf(eta_text)
            left = phi(eta, -1)
            right = phi(eta, 1)
            for branch_point in (left, right):
                recovered = mp.asin(
                    reduced_map(rho * mp.sin(branch_point)) / rho
                )
                self.assertLess(abs(recovered - eta), mp.mpf("1e-70"))
            magnitude = inverse_magnitude(eta)
            self.assertLess(
                abs(mp.diff(lambda value: phi(value, -1), eta) - magnitude),
                mp.mpf("1e-65"),
            )
            self.assertLess(
                abs(mp.diff(lambda value: phi(value, 1), eta) + magnitude),
                mp.mpf("1e-65"),
            )

    def test_roof_endpoint_values_are_strictly_positive(self) -> None:
        u_lower = support.U_LOWER
        u_upper = support.U_UPPER
        polar_lower = Fraction(4) / u_upper**2
        polar_upper = Fraction(4) / u_lower**2
        center_lower, center_upper = support.sqrt_interval(
            Fraction(8) / u_upper,
            Fraction(8) / u_lower,
        )
        self.assertGreater(polar_lower, 1)
        self.assertGreater(center_lower, polar_upper)
        self.assertGreater(center_lower, 1)
        self.assertGreater(polar_upper, polar_lower)
        self.assertGreater(center_upper, center_lower)

        endpoint_text = self.lock["mathematical_object"]["roof_endpoint_values"]
        self.assertIn("log(4/U_c^2)>0", endpoint_text)
        self.assertIn("(1/2)*log(8/U_c)", endpoint_text)

    def test_reflected_physical_conjugacy_is_explicit_and_correct(self) -> None:
        clocks = self.lock["clock"]
        self.assertIn("H=-q", clocks["physical_discrete_clock"])
        self.assertIn("H o G=f^2 o H", clocks["physical_discrete_clock"])
        self.assertIn("H' vanishes", clocks["physical_discrete_clock"])

        mp.mp.dps = 80
        u = (
            mp.mpf(support.U_LOWER_TEXT) + mp.mpf(support.U_UPPER_TEXT)
        ) / 2
        rho = u - 1
        logistic = lambda x: 1 - u * x**2
        reduced = lambda x: rho - 2 * u**2 * x**2 + u**3 * x**4
        for theta_text in ("-1.2", "-0.5", "0", "0.6", "1.25"):
            theta = mp.mpf(theta_text)
            q_value = rho * mp.sin(theta)
            g_value = mp.asin(reduced(q_value) / rho)
            left = -rho * mp.sin(g_value)
            h_value = -q_value
            right = logistic(logistic(h_value))
            self.assertLess(abs(left - right), mp.mpf("1e-70"))

    def test_markov_and_quotient_ledgers_are_not_mixed(self) -> None:
        phase_space = self.lock["mathematical_object"]["markov_phase_space"]
        determinant = self.lock["determinant_convention"]
        self.assertIn("0_L and 0_R remain distinct", phase_space)
        self.assertIn("may not be mixed", phase_space)
        self.assertIn("doubled two-component Markov extension", determinant["endpoint_multiplicity"])
        self.assertIn("different object", determinant["endpoint_multiplicity"])
        self.assertIn("Not defined in lock v2", determinant["endpoint_trace_rule"])
        self.assertIn("R and LR witnesses are interior", determinant["endpoint_trace_rule"])

    def test_physical_and_roof_clocks_are_separate(self) -> None:
        clocks = self.lock["clock"]
        self.assertIn("exactly two iterates of f", clocks["physical_discrete_clock"])
        self.assertIn("tau=log|G'|", clocks["intrinsic_suspension_clock"])
        self.assertIn("must be reported separately", clocks["separation_rule"])
        self.assertIn("Neither may be substituted", clocks["separation_rule"])

    def test_function_space_and_weighted_family_are_frozen(self) -> None:
        data_type = self.lock["data_type"]
        self.assertIn("epsilon=1/1000", data_type["complex_domain"])
        self.assertIn("composite holomorphic continuations", data_type["complex_domain"])
        self.assertIn("remain obligations, not claims", data_type["complex_domain"])
        self.assertIn("v_L(0)=v_R(0)", data_type["analytic_function_space"])
        self.assertIn("exp(s*Log(a(z)))", data_type["weighted_transfer_family"])
        self.assertIn("potential -s*tau", data_type["weighted_transfer_family"])
        self.assertIn("common-germ convention", data_type["weighted_transfer_family"])

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
        self.assertIn("multiplicatively independent", next_test)
        self.assertIn("Do not audit Fredholm", next_test)
        self.assertIn("do not", next_test.lower())
        self.assertIn("target zeros", next_test.lower())

    def test_witness_words_and_one_way_lattice_logic_are_frozen(self) -> None:
        obj = self.lock["mathematical_object"]
        convention = obj["periodic_word_convention"]
        self.assertIn("forward branch", convention)
        self.assertIn("unique interior fixed point", convention)
        self.assertIn("unique interior primitive two-cycle", convention)
        self.assertIn("LR and RL are cyclic names", convention)
        self.assertIn("Lambda_R=G'(theta_R)<0", convention)
        self.assertIn("Lambda_LR=G'(theta_L)*G'(theta_R)<0", convention)

        lattice = obj["lattice_definition"]
        self.assertIn("irrational ratio T_LR/T_R proves non-lattice", lattice)
        self.assertIn("rational relation", lattice)
        self.assertIn("inconclusive", lattice)
        stopping = " ".join(self.lock["stopping_conditions"])
        self.assertIn("REVISE or NOT_TESTABLE", stopping)
        self.assertIn("only if a full periodic-sum", stopping)

    def test_route_status_is_defined_but_not_evaluated(self) -> None:
        status = self.lock["route_status_at_lock"]
        self.assertEqual(
            status["route_a_tuple_inherited"],
            ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        )
        self.assertFalse(status["route_a_evaluation_performed"])
        self.assertFalse(status["route_b_invocation_allowed"])
        self.assertFalse(status["formal_candidate_created"])
        self.assertEqual(status["checkpoint_status"], "DEFINED_NOT_EVALUATED")
        self.assertEqual(status["recommended_verdict"], "REVISE")


if __name__ == "__main__":
    unittest.main()
