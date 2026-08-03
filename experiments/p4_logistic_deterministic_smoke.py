#!/usr/bin/env python3
"""Target-free deterministic spectral smoke test for the legacy Logistic route.

The profile preserves the legacy Gaussian width in *bin units* while reducing
the matrix and time cutoffs enough to permit a complete dense eigenspectrum.
It is an eigensolver/partition mechanics test, not a fidelity reproduction and
not a Route-A candidate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import numpy as np
import scipy.sparse as sp
from scipy.optimize import linear_sum_assignment
from scipy.sparse.linalg import eigs


AUDIT_ID = "P4-LOGISTIC-DETERMINISTIC-SMOKE"


@dataclass(frozen=True)
class SmokeConfig:
    bins: int = 128
    steps: int = 1000
    c_offset: float = 10.0
    mu_end: float = 1.5437
    delta_mu: float = 0.02
    initial_x: float = 0.5
    probability_threshold: float = 1.0e-12
    legacy_epsilon: float = 0.001916
    legacy_bins: int = 6000
    gaussian_sigma_cutoff: float = 5.0
    arpack_k: int = 40
    arpack_ncv: int = 90
    arpack_tolerance: float = 1.0e-10
    arpack_maxiter: int = 10000
    imag_threshold: float = 1.0e-8
    resolved_modulus_threshold: float = 1.0e-3

    @property
    def dx(self) -> float:
        return 2.0 / self.bins

    @property
    def epsilon(self) -> float:
        return self.legacy_epsilon * self.legacy_bins / self.bins

    @property
    def epsilon_over_dx(self) -> float:
        return self.epsilon / self.dx


def schedule_parameters(config: SmokeConfig) -> dict[str, float]:
    q_first = 1.0 / np.log(1.0 + config.c_offset) ** 2
    q_last = 1.0 / np.log(config.steps + config.c_offset) ** 2
    coefficient = config.delta_mu / (q_first - q_last)
    critical = config.mu_end - coefficient * q_last
    mu_first = critical + coefficient * q_first
    mu_last = critical + coefficient * q_last
    return {
        "k": float(coefficient),
        "u_c": float(critical),
        "mu_first": float(mu_first),
        "mu_last": float(mu_last),
    }


def build_empirical_flux(
    config: SmokeConfig, partition_shift_fraction: float
) -> tuple[np.ndarray, dict[str, Any]]:
    schedule = schedule_parameters(config)
    centers = -1.0 + (
        np.arange(config.bins, dtype=np.float64) + 0.5 + partition_shift_fraction
    ) * config.dx
    first_edge = centers[0] - 0.5 * config.dx

    probability = np.zeros(config.bins, dtype=np.float64)
    initial_bin = int(np.floor((config.initial_x - first_edge) / config.dx))
    initial_bin = int(np.clip(initial_bin, 0, config.bins - 1))
    probability[initial_bin] = 1.0

    transition = np.zeros((config.bins, config.bins), dtype=np.float64)
    inverse_two_epsilon_squared = 1.0 / (2.0 * config.epsilon**2)
    radius = int(config.gaussian_sigma_cutoff * config.epsilon / config.dx) + 1
    discarded_mass = 0.0

    for step in range(1, config.steps + 1):
        mu = schedule["u_c"] + schedule["k"] / np.log(step + config.c_offset) ** 2
        next_probability = np.zeros(config.bins, dtype=np.float64)
        active = probability >= config.probability_threshold
        discarded_mass += float(probability[~active].sum())

        for source in np.flatnonzero(active):
            mapped = 1.0 - mu * centers[source] ** 2
            center_index = int(np.floor((mapped - first_edge) / config.dx))
            lower = max(0, center_index - radius)
            upper = min(config.bins - 1, center_index + radius)
            destinations = np.arange(lower, upper + 1)
            weights = np.exp(
                -(centers[destinations] - mapped) ** 2 * inverse_two_epsilon_squared
            )
            weights /= weights.sum()
            flow = probability[source] * weights
            next_probability[destinations] += flow
            transition[source, destinations] += flow

        probability = next_probability

    return transition, {
        "partition_shift_fraction": partition_shift_fraction,
        "initial_bin": initial_bin,
        "gaussian_radius_bins": radius,
        "discarded_mass_sum_over_steps": discarded_mass,
        "final_probability_mass": float(probability.sum()),
        "transition_nnz": int(np.count_nonzero(transition)),
        "schedule": schedule,
    }


def normalize(transition: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    row_sums = transition.sum(axis=1)
    safe_sums = row_sums.copy()
    safe_sums[safe_sums == 0.0] = 1.0
    correct = transition / safe_sums[:, None]
    legacy = transition / safe_sums[None, :]
    return correct, legacy, safe_sums


def matrix_hash(matrix: np.ndarray) -> str:
    contiguous = np.ascontiguousarray(matrix, dtype=np.float64)
    return hashlib.sha256(contiguous.tobytes()).hexdigest()


def match_values(left: np.ndarray, right: np.ndarray) -> dict[str, Any]:
    if left.size == 0 or right.size == 0:
        return {
            "matched_count": 0,
            "unmatched_left": int(left.size),
            "unmatched_right": int(right.size),
            "median_distance": None,
            "max_distance": None,
        }
    costs = np.abs(left[:, None] - right[None, :])
    left_indices, right_indices = linear_sum_assignment(costs)
    distances = costs[left_indices, right_indices]
    return {
        "matched_count": int(distances.size),
        "unmatched_left": int(left.size - distances.size),
        "unmatched_right": int(right.size - distances.size),
        "median_distance": float(np.median(distances)),
        "max_distance": float(np.max(distances)),
        "p90_distance": float(np.quantile(distances, 0.9)),
    }


def phase_records(values: np.ndarray, config: SmokeConfig) -> list[dict[str, Any]]:
    largest_modulus = values[np.argsort(-np.abs(values), kind="stable")[: config.arpack_k]]
    upper = largest_modulus[largest_modulus.imag > config.imag_threshold]
    upper = upper[np.argsort(np.angle(upper), kind="stable")]
    return [
        {
            "real": float(value.real),
            "imag": float(value.imag),
            "modulus": float(abs(value)),
            "phase": float(np.angle(value)),
            "resolved": bool(abs(value) >= config.resolved_modulus_threshold),
        }
        for value in upper
    ]


def arpack_profile(
    matrix: np.ndarray,
    dense_values: np.ndarray,
    config: SmokeConfig,
    start_name: str,
    start_vector: np.ndarray,
) -> dict[str, Any]:
    values, vectors = eigs(
        sp.csr_matrix(matrix),
        k=config.arpack_k,
        which="LM",
        v0=start_vector,
        ncv=config.arpack_ncv,
        tol=config.arpack_tolerance,
        maxiter=config.arpack_maxiter,
    )
    residuals = np.linalg.norm(matrix @ vectors - vectors * values, axis=0) / np.linalg.norm(
        vectors, axis=0
    )
    dense_largest = dense_values[
        np.argsort(-np.abs(dense_values), kind="stable")[: config.arpack_k]
    ]
    return {
        "start": start_name,
        "max_relative_residual": float(residuals.max()),
        "median_relative_residual": float(np.median(residuals)),
        "dense_top_k_match": match_values(values, dense_largest),
        "phase_records": phase_records(values, config),
    }


def matrix_profile(
    transition: np.ndarray, metadata: dict[str, Any], config: SmokeConfig
) -> dict[str, Any]:
    correct, legacy, row_sums = normalize(transition)
    active = transition.sum(axis=1) > 0.0
    diagonal = np.diag(row_sums)
    inverse = np.diag(1.0 / row_sums)
    similarity_residual = np.max(np.abs(legacy - diagonal @ correct @ inverse))

    correct_values = np.linalg.eigvals(correct)
    legacy_values = np.linalg.eigvals(legacy)
    starts = {
        "ones": np.ones(config.bins),
        "ramp": np.linspace(1.0, 2.0, config.bins),
        "seed17_normal": np.random.default_rng(17).normal(size=config.bins),
    }
    solvers = {
        "correct_Q": [
            arpack_profile(correct, correct_values, config, name, vector)
            for name, vector in starts.items()
        ],
        "legacy_B": [
            arpack_profile(legacy, legacy_values, config, name, vector)
            for name, vector in starts.items()
        ],
    }

    correct_phases = phase_records(correct_values, config)
    return {
        "metadata": metadata,
        "hashes": {
            "transition_T": matrix_hash(transition),
            "correct_Q": matrix_hash(correct),
            "legacy_B": matrix_hash(legacy),
        },
        "normalization": {
            "occupied_rows": int(np.sum(active)),
            "correct_occupied_row_sum_max_error": float(
                np.max(np.abs(correct.sum(axis=1)[active] - 1.0))
            ),
            "legacy_occupied_row_sum_max_error": float(
                np.max(np.abs(legacy.sum(axis=1)[active] - 1.0))
            ),
            "occupation_condition_number": float(row_sums[active].max() / row_sums[active].min()),
            "similarity_max_abs_residual": float(similarity_residual),
            "dense_eigen_multiset_match": match_values(correct_values, legacy_values),
        },
        "dense_correct_spectrum": {
            "spectral_radius": float(np.max(np.abs(correct_values))),
            "top_k_upper_half_phase_records": correct_phases,
            "top_k_upper_half_count": len(correct_phases),
            "top_k_upper_half_resolved_count": sum(record["resolved"] for record in correct_phases),
            "first_six_unresolved_count": sum(
                not record["resolved"] for record in correct_phases[:6]
            ),
        },
        "arpack": solvers,
        "_dense_correct_values": correct_values,
    }


def build_report(config: SmokeConfig = SmokeConfig()) -> dict[str, Any]:
    baseline_transition, baseline_metadata = build_empirical_flux(config, 0.0)
    shifted_transition, shifted_metadata = build_empirical_flux(config, 0.5)
    baseline = matrix_profile(baseline_transition, baseline_metadata, config)
    shifted = matrix_profile(shifted_transition, shifted_metadata, config)

    baseline_values = baseline.pop("_dense_correct_values")
    shifted_values = shifted.pop("_dense_correct_values")
    baseline_resolved = baseline_values[np.abs(baseline_values) >= config.resolved_modulus_threshold]
    shifted_resolved = shifted_values[np.abs(shifted_values) >= config.resolved_modulus_threshold]

    return {
        "audit_id": AUDIT_ID,
        "formal_candidate": False,
        "target_data_used": False,
        "profile_scope": (
            "Dense mechanics smoke profile preserving legacy epsilon/dx; not a physical-epsilon "
            "or full-cutoff reproduction."
        ),
        "config": asdict(config)
        | {
            "dx": config.dx,
            "epsilon": config.epsilon,
            "epsilon_over_dx": config.epsilon_over_dx,
        },
        "baseline_partition": baseline,
        "half_bin_shift_partition": shifted,
        "partition_drift": {
            "all_dense_modes": match_values(baseline_values, shifted_values),
            "resolved_dense_modes": match_values(baseline_resolved, shifted_resolved),
            "baseline_resolved_mode_count": int(baseline_resolved.size),
            "shifted_resolved_mode_count": int(shifted_resolved.size),
        },
        "strongest_evidence": (
            "With fixed starts and tight tolerance, ARPACK can reproduce the dense top-|lambda| "
            "spectrum on the reduced profile."
        ),
        "strongest_failure": (
            "The legacy phase-ranking rule includes near-zero eigenvalues whose phases are not robust "
            "spectral levels, and a half-bin partition shift changes the selected phase list."
        ),
        "claim_boundary": (
            "This profile tests numerical mechanics only. It neither evaluates Riemann-zero agreement "
            "nor defines a dynamical determinant."
        ),
        "next_smallest_test": (
            "Implement a medium fidelity profile with physical epsilon fixed, save raw T, and track "
            "only residual-certified eigenbranches across bins, steps, and a half-bin shift."
        ),
        "recommended_verdict": "REVISE",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bins", type=int, default=128)
    parser.add_argument("--steps", type=int, default=1000)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    config = SmokeConfig(bins=arguments.bins, steps=arguments.steps)
    report = build_report(config)
    payload = json.dumps(report, indent=2, sort_keys=True)
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(payload + "\n", encoding="utf-8")
    print(payload)


if __name__ == "__main__":
    main()
