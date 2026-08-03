#!/usr/bin/env python3
"""Reproducible pre-candidate audit of the legacy Paper-4 Logistic notebooks.

This module does not rerun the expensive legacy simulations and does not define
a Route-A candidate.  It extracts the saved notebook evidence, records target
data usage, and verifies the algebraic relationship between the legacy CSR
normalization and a correct row normalization.

The Riemann zeros are read only while scoring the already-saved predictions.
They are not inputs to any dynamical object defined here.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import re
import subprocess
from pathlib import Path
from typing import Any

import mpmath
import numpy as np


AUDIT_ID = "P4-LOGISTIC-LEGACY-AUDIT"
LEGACY_DIRECTORY = Path("docs/prior_work/legacy/4-riemann_logistic")
ABLATION_NOTEBOOK = LEGACY_DIRECTORY / "ablation_test.ipynb"
MICRO_NOTEBOOK = LEGACY_DIRECTORY / "micro_ustc_data_match.ipynb"
EPSILON_NOTEBOOK = LEGACY_DIRECTORY / "micro_find_best_eps_detail.ipynb"
MACRO_OPTIMIZER_NOTEBOOK = LEGACY_DIRECTORY / "macro_100_scale_find_1d.ipynb"


def load_notebook(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def code_text(notebook: dict[str, Any]) -> str:
    return "\n".join(
        "".join(cell.get("source", []))
        for cell in notebook.get("cells", [])
        if cell.get("cell_type") == "code"
    )


def output_text(notebook: dict[str, Any]) -> str:
    chunks: list[str] = []
    for cell in notebook.get("cells", []):
        for output in cell.get("outputs", []):
            if "text" in output:
                chunks.append("".join(output["text"]))
            plain = output.get("data", {}).get("text/plain")
            if plain:
                chunks.append("".join(plain))
    return "\n".join(chunks)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_commit(repository: Path) -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=repository, text=True
    ).strip()


def extract_saved_best_differences(notebook: dict[str, Any]) -> np.ndarray:
    for cell in notebook.get("cells", []):
        for output in cell.get("outputs", []):
            plain = output.get("data", {}).get("text/plain")
            if not plain:
                continue
            rendered = "".join(plain)
            match = re.search(r"array\(\[(.*?)\]\)", rendered, re.DOTALL)
            if match:
                values = np.fromstring(match.group(1).replace("\n", " "), sep=",")
                if values.size:
                    return values
    raise ValueError("saved best_diffs array was not found")


def extract_trial_records(notebook: dict[str, Any]) -> list[dict[str, float | int]]:
    pattern = re.compile(
        r"\[观测\s+(\d+)\]\s+ErrSum:\s+([0-9.]+)\s+\|\s+"
        r"N=20\s+尖峰\(带符号\):\s+([-+0-9.]+)"
    )
    return [
        {"trial": int(trial), "error_sum_2_to_6": float(error), "n20_error": float(n20)}
        for trial, error, n20 in pattern.findall(output_text(notebook))
    ]


def extract_ablation_metrics(notebook: dict[str, Any]) -> dict[str, dict[str, float]]:
    text = output_text(notebook)
    pattern = re.compile(
        r"\[(M\d):[^\]]+\].*?MSE:\s*([0-9.]+)\s*\|\s*"
        r"平均误差:\s*([0-9.]+)%\s*\|\s*最大误差:\s*([0-9.]+)%"
    )
    return {
        model: {
            "mse": float(mse),
            "mean_relative_error_percent": float(mean_error),
            "max_relative_error_percent": float(max_error),
        }
        for model, mse, mean_error, max_error in pattern.findall(text)
    }


def riemann_zeros(count: int) -> np.ndarray:
    mpmath.mp.dps = 30
    return np.array([float(mpmath.zetazero(index).imag) for index in range(1, count + 1)])


def interval_metrics(errors: np.ndarray, zeros: np.ndarray, start: int, stop: int) -> dict[str, float | int]:
    selected = np.abs(errors[start:stop])
    selected_zeros = zeros[start:stop]
    return {
        "count": int(selected.size),
        "absolute_error_sum": float(selected.sum()),
        "mae": float(selected.mean()),
        "rmse": float(np.sqrt(np.mean(selected**2))),
        "mean_relative_error_percent": float(np.mean(selected / selected_zeros) * 100.0),
        "max_absolute_error": float(selected.max()),
    }


def phase_match_metrics(saved_differences: np.ndarray) -> dict[str, Any]:
    zeros = riemann_zeros(saved_differences.size)
    return {
        "anchor_zero_1_error": float(abs(saved_differences[0])),
        "fitted_zeros_2_to_6": interval_metrics(saved_differences, zeros, 1, 6),
        "retrospective_zeros_7_to_20": interval_metrics(saved_differences, zeros, 6, 20),
        "retrospective_zeros_7_to_19_excluding_rewarded_n20": interval_metrics(
            saved_differences, zeros, 6, 19
        ),
        "retrospective_zeros_21_to_85": interval_metrics(
            saved_differences, zeros, 20, saved_differences.size
        ),
        "rewarded_n20": {
            "signed_error": float(saved_differences[19]),
            "relative_error_percent": float(saved_differences[19] / zeros[19] * 100.0),
        },
    }


def normalize_rows(transition: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    row_sums = transition.sum(axis=1)
    safe_sums = row_sums.copy()
    safe_sums[safe_sums == 0.0] = 1.0
    return transition / safe_sums[:, None], safe_sums


def normalize_legacy_destination_index(transition: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Model ``csr.data /= row_sums[csr.indices]`` as right diagonal scaling."""
    row_sums = transition.sum(axis=1)
    safe_sums = row_sums.copy()
    safe_sums[safe_sums == 0.0] = 1.0
    return transition / safe_sums[None, :], safe_sums


def best_eigenvalue_matching_error(left: np.ndarray, right: np.ndarray) -> float:
    left_values = np.linalg.eigvals(left)
    right_values = np.linalg.eigvals(right)
    best = float("inf")
    for permutation in itertools.permutations(range(right_values.size)):
        error = max(
            abs(left_values[index] - right_values[permutation[index]])
            for index in range(left_values.size)
        )
        best = min(best, float(error))
    return best


def normalization_audit() -> dict[str, Any]:
    transition = np.array(
        [
            [4.0, 1.0, 0.0, 0.0],
            [0.0, 2.0, 3.0, 0.0],
            [1.0, 0.0, 1.0, 4.0],
            [0.0, 2.0, 0.0, 1.0],
        ]
    )
    correct, row_sums = normalize_rows(transition)
    legacy, legacy_sums = normalize_legacy_destination_index(transition)
    if not np.array_equal(row_sums, legacy_sums):
        raise AssertionError("normalizations used different diagonal data")

    diagonal = np.diag(row_sums)
    inverse = np.diag(1.0 / row_sums)
    similarity_residual = np.max(np.abs(legacy - diagonal @ correct @ inverse))
    return {
        "legacy_formula": "B=T*D^(-1)",
        "correct_formula": "Q=D^(-1)*T",
        "similarity_identity": "B=D*Q*D^(-1)",
        "similarity_max_abs_residual": float(similarity_residual),
        "best_dense_eigenvalue_matching_error": best_eigenvalue_matching_error(legacy, correct),
        "correct_active_row_sum_max_error": float(np.max(np.abs(correct.sum(axis=1) - 1.0))),
        "legacy_active_row_sum_max_error": float(np.max(np.abs(legacy.sum(axis=1) - 1.0))),
        "row_sum_diagonal_condition_number": float(row_sums.max() / row_sums.min()),
        "interpretation": (
            "The legacy matrix is not row-stochastic, but it is exactly similar to the correct "
            "row-normalized matrix. Exact eigenvalues are unchanged; eigenvectors, Markov meaning, "
            "nonnormality, and finite-precision eigensolver conditioning are not unchanged."
        ),
    }


def parse_parenthesized_measurement(value: str) -> tuple[float, float]:
    match = re.fullmatch(r"([0-9.]+)\(([0-9]+)\)", value.strip())
    if not match:
        raise ValueError(value)
    central = match.group(1)
    decimals = len(central.split(".")[1]) if "." in central else 0
    return float(central), int(match.group(2)) * 10.0 ** (-decimals)


def ustc_audit(micro_source: str, model_n20_error: float) -> dict[str, Any]:
    match = re.search(r'raw_data_text\s*=\s*"""(.*?)"""', micro_source, re.DOTALL)
    if not match:
        raise ValueError("embedded USTC table was not found")

    selected_rows: list[dict[str, Any]] = []
    for line in match.group(1).strip().splitlines():
        fields = [field.strip() for field in line.split(",")]
        index = int(fields[0])
        exact = float(fields[1])
        measurements = [parse_parenthesized_measurement(fields[column]) for column in (3, 4, 5)]
        selected_rows.append(
            {
                "index": index,
                "deviations": [float(value - exact) for value, _ in measurements],
                "error_bars": [float(error) for _, error in measurements],
            }
        )

    n20 = selected_rows[19]
    largest_error_bar_row = max(
        selected_rows, key=lambda row: max(row["error_bars"])
    )
    return {
        "embedded_table_has_source_citation": False,
        "notebook_discards_column_index_2": True,
        "n20_experimental_deviations": n20["deviations"],
        "n20_experimental_error_bars": n20["error_bars"],
        "model_n20_error": model_n20_error,
        "largest_selected_experimental_error_bar": {
            "index": largest_error_bar_row["index"],
            "value": max(largest_error_bar_row["error_bars"]),
        },
        "independent_validation": False,
        "reason": (
            "The model-selection score rewards a large N=20 error, and the model error magnitude "
            "does not match the embedded experimental deviations or their error bars."
        ),
    }


def build_report(repository: Path) -> dict[str, Any]:
    paths = {
        "ablation": repository / ABLATION_NOTEBOOK,
        "micro": repository / MICRO_NOTEBOOK,
        "epsilon_scan": repository / EPSILON_NOTEBOOK,
        "macro_optimizer": repository / MACRO_OPTIMIZER_NOTEBOOK,
    }
    notebooks = {name: load_notebook(path) for name, path in paths.items()}
    sources = {name: code_text(notebook) for name, notebook in notebooks.items()}

    saved_differences = extract_saved_best_differences(notebooks["micro"])
    trials = extract_trial_records(notebooks["micro"])
    if len(trials) != 20:
        raise AssertionError(f"expected 20 saved eigensolver trials, found {len(trials)}")
    trial_errors = np.array([record["error_sum_2_to_6"] for record in trials])

    pattern_checks = {
        "epsilon_frozen_to_0_001916": "BEST_EPS = 0.001916" in sources["micro"],
        "first_six_zeros_loaded_as_targets": "TARGETS = TRUE_ZEROS[:6]" in sources["micro"],
        "legacy_destination_index_normalization": (
            "P_sparse.data /= sums[P_sparse.indices]" in sources["micro"]
        ),
        "same_matrix_reused_for_20_trials": "TRIALS = 20" in sources["micro"],
        "n20_error_rewarded_in_selection": (
            "score = err_sum_2_to_6 - (n20_spike_abs * 0.1)" in sources["micro"]
        ),
        "epsilon_scan_has_402_requested_values": all(
            marker in sources["epsilon_scan"]
            for marker in (
                "np.linspace(0.00065, 0.00075, 101)",
                "np.linspace(0.00170, 0.00200, 301)",
            )
        ),
        "ablation_method5_scoring_commented_out": (
            "#calib_dyn3, err_dyn3, mse_dyn3 = apply_scaling" in sources["ablation"]
        ),
        "macro_optimizer_uses_first_100_zeros": (
            "get_exact_riemann_zeros(100)" in sources["macro_optimizer"]
        ),
    }

    return {
        "audit_id": AUDIT_ID,
        "formal_candidate": False,
        "source_commit": git_commit(repository),
        "source_files": {
            name: {"path": str(path.relative_to(repository)), "sha256": sha256(path)}
            for name, path in paths.items()
        },
        "legacy_object": {
            "map": "x_(n+1)=1-mu_n*x_n^2",
            "schedule": "mu_n=u_c+k/log(n+10)^2, endpoint-anchored from 1.5637 to 1.5437",
            "empirical_flux": "T_ij=sum_n V_n(i)*K_(mu_n,epsilon)(i,j)",
            "correct_surrogate": "Q=D^(-1)T with D=diag(T*1)",
            "legacy_computed_matrix": "B=T*D^(-1)",
            "reported_observable": "sorted upper-half-plane eigenvalue principal phases, with modulus discarded",
            "phase_scale": "gamma_1/theta_1",
            "determinant_convention": None,
            "time_order_preserved": False,
        },
        "pattern_checks": pattern_checks,
        "normalization_audit": normalization_audit(),
        "solver_selection_audit": {
            "same_matrix_trial_count": len(trials),
            "trial_error_sum_2_to_6_mean": float(trial_errors.mean()),
            "trial_error_sum_2_to_6_std_population": float(trial_errors.std()),
            "trial_error_sum_2_to_6_std_sample": float(trial_errors.std(ddof=1)),
            "trial_error_sum_2_to_6_min": float(trial_errors.min()),
            "trial_error_sum_2_to_6_max": float(trial_errors.max()),
            "trial_count_below_2_2": int(np.sum(trial_errors < 2.2)),
            "physical_ensemble": False,
            "selection_reads_n20": True,
            "records": trials,
        },
        "saved_phase_match": phase_match_metrics(saved_differences),
        "ablation_saved_metrics": extract_ablation_metrics(notebooks["ablation"]),
        "ustc_audit": ustc_audit(sources["micro"], float(saved_differences[19])),
        "data_boundary": {
            "contaminated_training": [
                "zero 1 fixes the phase scale",
                "zeros 2-6 select epsilon and the reported eigensolver trial",
                "zero 20 enters the reported trial score through a large-error reward",
                "zeros 1-100 were used by the macro k optimizer underlying the ablation family",
            ],
            "honest_legacy_validation": None,
            "honest_legacy_test": None,
            "retrospective_only": "saved errors outside the fitted indices; useful for diagnosis, not sealed evidence",
        },
        "route_a_preassessment": {
            "status": "NOT_TESTABLE",
            "diagnostic_tuple": ["A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "strongest_evidence": (
                "The selected saved run has MAE 0.3494 on fitted zeros 2-6 after zero 1 fixes scale."
            ),
            "strongest_failure": (
                "There is no primitive-orbit ledger or explicit dynamical Zeta/Fredholm determinant, "
                "and the saved low-prefix match is target-fitted and solver-selected."
            ),
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": (
            "The legacy notebooks establish a fitted finite-matrix eigenphase observation and a useful "
            "numerical benchmark. They do not establish a dynamical determinant, a blind zero match, a "
            "natural quantization, or a Hilbert-Polya operator."
        ),
        "next_smallest_test": (
            "Freeze the legacy parameters, save one raw T matrix, construct Q and B explicitly, fix the "
            "eigensolver start and tolerances, report eigenvalue moduli and residuals, and track modes under "
            "a half-bin partition shift without target-data reselection."
        ),
        "recommended_verdict": "REVISE",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()

    report = build_report(arguments.repository.resolve())
    payload = json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False)
    if arguments.output:
        output = arguments.output
        if not output.is_absolute():
            output = arguments.repository / output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload + "\n", encoding="utf-8")
    print(payload)


if __name__ == "__main__":
    main()
