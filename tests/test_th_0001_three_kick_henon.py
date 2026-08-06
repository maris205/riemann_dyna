import json
import tempfile
import unittest
from pathlib import Path

import sympy as sp
import yaml

from experiments.th_0001_three_kick_henon import (
    P,
    PARAMETERS,
    Q,
    build_report,
    cyclic_rotations,
    elimination_data,
    inverse_superstep,
    polynomial_hash,
    superstep,
    symbolic_superstep,
)


ROOT = Path(__file__).resolve().parents[1]


class ThreeKickHenonPrefilterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = build_report()

    def test_source_lock_freezes_one_target_free_superstep(self) -> None:
        lock = yaml.safe_load((ROOT / "configs/source_locks/TH-0001.yaml").read_text(encoding="utf-8"))
        self.assertEqual(lock["candidate_id"], "TH-0001")
        self.assertEqual(lock["mathematical_object"]["micro_kick_order"], ["1/2", "3/2", "5/2"])
        self.assertEqual(lock["cutoff"]["primitive_upo_period_supersteps"], 2)
        self.assertIn("NOT_OPENED", lock["determinant_convention"])
        forbidden = " ".join(lock["forbidden_data"]).lower()
        self.assertIn("riemann-zero", forbidden)
        self.assertIn("gue", forbidden)

    def test_exact_map_inverse_and_symplectic_jacobian(self) -> None:
        q_out, p_out = symbolic_superstep(Q, P)
        q_back, p_back = inverse_superstep(q_out, p_out)
        self.assertEqual(sp.expand(q_back - Q), 0)
        self.assertEqual(sp.expand(p_back - P), 0)
        jacobian = sp.Matrix([q_out, p_out]).jacobian([Q, P])
        self.assertEqual(sp.expand(jacobian.det()), 1)

    def test_generating_function_produces_each_micro_map(self) -> None:
        q_new = sp.symbols("Q_new")
        for parameter in PARAMETERS:
            generating = Q * q_new - Q + parameter * Q**3 / 3
            p_old = -sp.diff(generating, Q)
            p_new = sp.diff(generating, q_new)
            solved_q_new = sp.solve(sp.Eq(P, p_old), q_new)[0]
            self.assertEqual(sp.expand(solved_q_new - (1 - parameter * Q**2 - P)), 0)
            self.assertEqual(p_new, Q)

    def test_nonpalindromic_clock_and_swap_reversor_failure(self) -> None:
        self.assertNotIn(tuple(reversed(PARAMETERS)), cyclic_rotations(PARAMETERS))
        q_forward, p_forward = superstep(0, 0)
        rgr_origin = (p_forward, q_forward)
        self.assertEqual(rgr_origin, (sp.Rational(-1, 2), sp.Rational(-5, 8)))
        self.assertEqual(inverse_superstep(0, 0), (sp.Rational(-1, 2), sp.Rational(-1, 8)))

    def test_affine_antisymplectic_leading_equations_are_incompatible(self) -> None:
        lam = sp.symbols("lambda")
        first, _, last = PARAMETERS
        equation_one = sp.Poly(first**2 * lam**5 - last**2, lam, domain=sp.QQ)
        equation_two = sp.Poly(first**3 * lam**7 - last**3, lam, domain=sp.QQ)
        self.assertEqual(sp.gcd(equation_one, equation_two).degree(), 0)
        self.assertFalse(self.report["time_reversal_audit"]["affine_antisymplectic_involution"])

    def test_exact_elimination_shapes_hashes_and_counts(self) -> None:
        data = elimination_data()
        self.assertEqual([(poly.degree(P), poly.degree(Q)) for poly in data["basis1"].polys], [(1, 7), (0, 8)])
        self.assertEqual([(poly.degree(P), poly.degree(Q)) for poly in data["basis2"].polys], [(1, 63), (0, 64)])
        self.assertEqual(data["r1"].degree(), 8)
        self.assertEqual(data["r2"].degree(), 64)
        self.assertEqual(data["d2"].degree(), 56)
        self.assertEqual(data["r1"].count_roots(-sp.oo, sp.oo), 4)
        self.assertEqual(data["r2"].count_roots(-sp.oo, sp.oo), 20)
        self.assertEqual(data["d2"].count_roots(-sp.oo, sp.oo), 16)
        self.assertEqual(
            polynomial_hash(data["d2"]),
            "60dd88608e229e19708948f239bc7e4f8f80f536a3c54a763dbe59ee924c46dc",
        )

    def test_primitive_period_two_is_exact_quotient_not_residual_filter(self) -> None:
        data = elimination_data()
        quotient, remainder = data["r2"].div(data["r1"])
        self.assertTrue(remainder.is_zero)
        self.assertEqual(quotient.monic(), data["d2"].monic())
        self.assertEqual(sp.gcd(data["r1"], data["d2"]).degree(), 0)

    def test_complete_short_orbit_census_and_signed_monodromy(self) -> None:
        census = self.report["primitive_orbit_census"]
        self.assertEqual(census["real_primitive_period_1_orbits"], 4)
        self.assertEqual(census["real_primitive_period_2_orbits"], 8)
        self.assertEqual(census["total_real_primitive_orbits"], 12)
        self.assertEqual(census["total_real_phase_points"], 20)
        self.assertTrue(census["all_short_orbits_hyperbolic"])
        self.assertGreater(float(census["minimum_certified_abs_trace_minus_two"]), 1.6)
        self.assertLess(float(census["period_two_max_pairing_distance"]), 1e-10)
        for orbit in census["orbits"]:
            self.assertEqual(orbit["det_monodromy_exact"], "1")
            self.assertEqual(orbit["magnetic_phase"], "NOT_DEFINED")
            for phase in orbit["phases"]:
                self.assertNotEqual(float(phase["stable_multiplier_signed"]), 0.0)
                self.assertNotEqual(float(phase["unstable_multiplier_signed"]), 0.0)

    def test_route_a_boundary_stays_weak_and_route_b_closed(self) -> None:
        status = self.report["route_a_prefilter"]
        self.assertEqual(status["A1"], "A1_WEAK")
        self.assertEqual(status["A2"], "A2_FAIL")
        self.assertEqual(status["A3"], "A3_FAIL")
        self.assertEqual(status["A4"], "A4_FORMAL_HINT")
        self.assertFalse(status["route_b_invocation_allowed"])

    def test_saved_artifact_is_byte_reproducible(self) -> None:
        expected = json.loads((ROOT / "artifacts/th_0001/route_a_prefilter.json").read_text(encoding="utf-8"))
        self.assertEqual(self.report, expected)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.json"
            payload = json.dumps(self.report, indent=2, sort_keys=True) + "\n"
            path.write_text(payload, encoding="utf-8")
            self.assertEqual(path.read_bytes(), (ROOT / "artifacts/th_0001/route_a_prefilter.json").read_bytes())


if __name__ == "__main__":
    unittest.main()
