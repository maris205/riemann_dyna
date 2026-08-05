from decimal import Decimal
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml

from experiments import p4_logistic_uc_acip_sharp_cone_enclosure as sharp


class LogisticUcAcipSharpConeEnclosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = sharp.build_report()

    def test_every_validated_gate_passes(self) -> None:
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
            environment["python_flint"], sharp.EXPECTED_PYTHON_FLINT_VERSION
        )
        self.assertEqual(environment["flint"], sharp.EXPECTED_FLINT_VERSION)
        self.assertEqual(environment["arb_decimal_digits"], 100)

    def test_closed_cover_certifies_the_global_distortion_upper_bound(self) -> None:
        certificate = self.report["distortion_certificate"]
        cover = certificate["global_cover"]
        self.assertEqual(cover["closed_interval_count"], 1 << 18)
        self.assertEqual(cover["domain"], ["0", "1"])
        self.assertTrue(cover["all_denominators_strictly_positive"])
        self.assertTrue(cover["all_cells_below_D_upper_squared"])
        self.assertEqual(cover["D_upper_safe"], "0.17014")
        self.assertEqual(cover["maximum_interval_upper_cell_index"], 198117)

    def test_sealed_interval_is_a_strict_lower_witness(self) -> None:
        witness = self.report["distortion_certificate"]["lower_witness"]
        self.assertEqual(witness["closed_t_interval"], ["0.75575", "0.75576"])
        self.assertTrue(witness["denominator_strictly_positive"])
        self.assertTrue(witness["all_points_above_D_lower_squared"])
        self.assertEqual(
            self.report["distortion_certificate"]["certified_statement"],
            "0.17013 < D < 0.17014",
        )

    def test_sharp_cone_identity_and_density_normalization(self) -> None:
        ledger = self.report["cone_ledger"]
        self.assertEqual(ledger["inverse_contraction_safe_upper"], "0.595744")
        self.assertEqual(ledger["distortion_safe_upper"], "0.17014")
        self.assertEqual(ledger["log_lipschitz_cone_slope"], "42535/101064")
        self.assertTrue(
            self.report["computed_gates"]["sharp_cone_bound_identity_is_exact"]
        )
        self.assertEqual(
            self.report["certified_enclosures"]["normalization_identity"],
            "g_A(0)=2*h(0)",
        )

    def test_safe_enclosures_are_strict_and_sharper_than_parent(self) -> None:
        parent = json.loads(
            Path(
                "artifacts/p4_logistic_uc_acip_cone_enclosure/certified_bounds.json"
            ).read_text(encoding="utf-8")
        )["certified_enclosures"]
        for name, row in self.report["certified_enclosures"].items():
            if name == "normalization_identity":
                continue
            lower = Decimal(row["safe_lower"])
            upper = Decimal(row["safe_upper"])
            self.assertLess(lower, upper)
            self.assertGreater(lower, Decimal(parent[name]["lower"]))
            self.assertLess(upper, Decimal(parent[name]["upper"]))

    def test_four_finite_mass_intervals_tighten_parent_bounds(self) -> None:
        parent_rows = json.loads(
            Path(
                "artifacts/p4_logistic_uc_acip_cone_enclosure/certified_bounds.json"
            ).read_text(encoding="utf-8")
        )["finite_branch_mass_enclosures"]
        rows = self.report["finite_branch_mass_enclosures"]
        self.assertEqual(
            [row["physical_return_label"] for row in rows], [12, 14, 16, 18]
        )
        for row, parent in zip(rows, parent_rows):
            lower = Decimal(row["certified_mass"]["lower"])
            upper = Decimal(row["certified_mass"]["upper"])
            self.assertTrue(row["endpoint_radius_gate_passed"])
            self.assertLess(lower, upper)
            self.assertGreater(lower, Decimal(parent["certified_mass"]["lower"]))
            self.assertLess(upper, Decimal(parent["certified_mass"]["upper"]))

        gates = self.report["computed_gates"]
        self.assertTrue(gates["physical_return_labels_are_sealed"])
        self.assertTrue(gates["all_four_endpoint_radius_gates_pass"])
        self.assertTrue(gates["all_four_mass_intervals_have_strict_order"])

    def test_six_required_error_categories_are_explicit(self) -> None:
        budget = self.report["error_budget"]
        self.assertEqual(
            set(budget),
            {
                "discretization",
                "truncation",
                "rounding",
                "normalization",
                "iteration_stopping",
                "resolvent_tail",
            },
        )
        self.assertIn("closed Arb cells", budget["discretization"])
        self.assertIn("not used", budget["resolvent_tail"])

    def test_source_lock_and_route_a_evaluation_keep_scope_closed(self) -> None:
        lock = yaml.safe_load(Path(sharp.SOURCE_LOCK).read_text(encoding="utf-8"))
        self.assertEqual(lock["audit_id"], sharp.AUDIT_ID)
        self.assertEqual(lock["cutoff"]["closed_cover_intervals"], 1 << 18)
        self.assertEqual(lock["precision"]["python_flint_version"], "0.9.0")
        self.assertIn("point samples", " ".join(lock["forbidden_data"]))

        evaluation = yaml.safe_load(
            Path(
                "evaluations/route_a/P4-LOGISTIC-UC-ACIP-SHARP-CONE-ENCLOSURE/20260805T012200Z.yaml"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(evaluation["a1"]["verdict"], "A1_WEAK")
        self.assertEqual(evaluation["a2"]["verdict"], "A2_FAIL")
        self.assertEqual(evaluation["a3"]["verdict"], "A3_FAIL")
        self.assertEqual(evaluation["a4"]["verdict"], "A4_FAIL")
        self.assertFalse(evaluation["route_b_invocation_allowed"])
        self.assertEqual(
            evaluation["source_commit"],
            "f34117824702404fe0837f5811a5465d33cc65de",
        )
        self.assertEqual(
            evaluation["a2"]["metrics"]["root_count_discrepancy"],
            "not_testable",
        )
        for layer in ("a2", "a3", "a4"):
            self.assertEqual(evaluation[layer]["artifacts"], [])

        source_commit = evaluation["source_commit"]
        for path in (
            sharp.SOURCE_LOCK,
            sharp.FORMAL_RESULT,
            sharp.GENERATOR,
            "artifacts/p4_logistic_uc_acip_sharp_cone_enclosure/interval_certificate.json",
        ):
            subprocess.run(
                ["git", "cat-file", "-e", f"{source_commit}:{path}"],
                check=True,
            )

    def test_formal_result_states_the_certificate_and_nonclaims(self) -> None:
        proof = Path(sharp.FORMAL_RESULT).read_text(encoding="utf-8")
        self.assertIn("0.17013<D", proof)
        self.assertIn("0.20655", proof)
        self.assertIn("complete closed-interval cover", proof)
        self.assertIn("Hilbert--Pólya", proof)

    def test_saved_artifact_is_byte_reproducible(self) -> None:
        expected = json.dumps(self.report, indent=2, sort_keys=True) + "\n"
        artifact = Path(
            "artifacts/p4_logistic_uc_acip_sharp_cone_enclosure/"
            "interval_certificate.json"
        )
        self.assertEqual(artifact.read_text(encoding="utf-8"), expected)
        provenance = self.report["provenance"]
        self.assertIn(
            "formal/results/exact_uc_first_return_support.md",
            provenance["source_inputs_sha256"],
        )
        self.assertEqual(
            provenance["generator_sha256"],
            sharp.file_sha256(provenance["generator"]),
        )
        for path, expected_hash in provenance["source_inputs_sha256"].items():
            self.assertEqual(expected_hash, sharp.file_sha256(path))
        self.assertFalse(provenance["external_target_data_used"])

    def test_cli_reproduction_is_byte_identical(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "interval_certificate.json"
            subprocess.run(
                [
                    sys.executable,
                    sharp.GENERATOR,
                    "--quiet",
                    "--output",
                    str(output),
                ],
                check=True,
            )
            expected = Path(
                "artifacts/p4_logistic_uc_acip_sharp_cone_enclosure/"
                "interval_certificate.json"
            ).read_bytes()
            self.assertEqual(output.read_bytes(), expected)


if __name__ == "__main__":
    unittest.main()
