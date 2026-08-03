#!/usr/bin/env python3
"""Target-free-computation physical-epsilon audit for the Logistic route.

The construction uses one frozen million-step non-autonomous clock, compiled
binary64 accumulation without fastmath, identical-estimator static controls,
and residual-certified complex-plane branch matching.  It intentionally reads
no prime, Riemann-zero, or experimental target table.  The frozen physical
epsilon is nevertheless a historically zero-fitted legacy constant, so this is
a robustness audit rather than blind arithmetic validation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable

import llvmlite
import numba
import numpy as np
import scipy
import scipy.sparse as sp
from numba import njit
from scipy.optimize import linear_sum_assignment
from scipy.sparse.linalg import ArpackNoConvergence, eigs


AUDIT_ID = "P4-LOGISTIC-MEDIUM-PHYSICAL-EPSILON"


@dataclass(frozen=True)
class MediumConfig:
    full_schedule_steps: int = 1_000_000
    c_offset: float = 10.0
    mu_end: float = 1.5437
    delta_mu: float = 0.02
    epsilon: float = 0.001916
    gaussian_sigma_cutoff: float = 5.0
    probability_threshold: float = 1.0e-12
    initial_x: float = 0.5
    reference_bins: int = 2048
    reference_steps: int = 100_000
    time_prefixes: tuple[int, ...] = (50_000, 100_000, 200_000)
    bin_profiles: tuple[int, ...] = (1536, 2048, 3072)
    translated_grid_shifts: tuple[float, ...] = (0.0, 0.5)
    dense_anchor_bins: int = 256
    dense_anchor_steps: int = 5_000
    profile_k: int = 450
    reference_k_guard: tuple[int, ...] = (300, 450)
    arpack_ncv: int = 1200
    arpack_tolerance: float = 1.0e-11
    arpack_maxiter: int = 100_000
    primary_start: str = "ones"
    secondary_start: str = "seed17_normal"
    imag_threshold: float = 1.0e-8
    strong_modulus_floor: float = 0.5
    moderate_modulus_floor: float = 0.1
    weak_modulus_floor: float = 0.001
    residual_ceiling: float = 1.0e-9
    conjugate_pair_defect_ceiling: float = 1.0e-8
    matching_distance_cutoff: float = 0.10
    minimum_upper_half_strong_branches: int = 20
    survival_fraction_minimum: float = 0.75
    median_drift_ceiling: float = 0.01
    p90_drift_ceiling: float = 0.05
    max_drift_ceiling: float = 0.10
    phase_drift_ceiling: float = 0.03
    log_modulus_ratio_ceiling: float = 0.10
    phase_rank_median_ceiling: float = 0.0
    phase_rank_max_ceiling: int = 2
    ambiguity_ratio_ceiling: float = 2.0 / 3.0
    dynamic_static_margin_median_minimum: float = 2.0
    dynamic_static_margin_fraction_minimum: float = 2.0 / 3.0
    probability_mass_loss_ceiling: float = 1.0e-6
    row_sum_error_ceiling: float = 1.0e-12
    static_kernel_identity_ceiling: float = 1.0e-10
    k_edge_modulus_ceiling: float = 0.4


def schedule_parameters(config: MediumConfig) -> dict[str, float]:
    q_first = 1.0 / np.log(1.0 + config.c_offset) ** 2
    q_last = 1.0 / np.log(config.full_schedule_steps + config.c_offset) ** 2
    coefficient = config.delta_mu / (q_first - q_last)
    critical = config.mu_end - coefficient * q_last
    return {
        "k": float(coefficient),
        "u_c": float(critical),
        "mu_first": float(critical + coefficient * q_first),
        "mu_full_schedule_last": float(critical + coefficient * q_last),
    }


def schedule_mean(config: MediumConfig, steps: int) -> float:
    schedule = schedule_parameters(config)
    indices = np.arange(1, steps + 1, dtype=np.float64)
    values = schedule["u_c"] + schedule["k"] / np.log(indices + config.c_offset) ** 2
    return float(values.mean())


def static_controls(config: MediumConfig) -> dict[str, float]:
    return {
        "mean_matched": schedule_mean(config, config.reference_steps),
        "endpoint_high": config.mu_end + config.delta_mu,
        "endpoint_low": config.mu_end,
        "legacy_regression": 1.543689,
    }


@njit(cache=False)
def _simulate_compiled(
    bins: int,
    checkpoints: np.ndarray,
    partition_shift: float,
    dynamics_code: int,
    static_mu: float,
    c_offset: float,
    schedule_k: float,
    schedule_u_c: float,
    epsilon: float,
    gaussian_sigma_cutoff: float,
    probability_threshold: float,
    initial_x: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, int, int]:
    dx = 2.0 / bins
    centers = -1.0 + (np.arange(bins) + 0.5 + partition_shift) * dx
    first_edge = centers[0] - 0.5 * dx
    center_squares = centers * centers
    probability = np.zeros(bins, dtype=np.float64)
    initial_bin = int(np.floor((initial_x - first_edge) / dx))
    if initial_bin < 0:
        initial_bin = 0
    elif initial_bin >= bins:
        initial_bin = bins - 1
    probability[initial_bin] = 1.0
    transition = np.zeros((bins, bins), dtype=np.float64)
    snapshots = np.zeros((checkpoints.size, bins, bins), dtype=np.float64)
    discarded = np.zeros(checkpoints.size, dtype=np.float64)
    masses = np.zeros(checkpoints.size, dtype=np.float64)
    last_mus = np.zeros(checkpoints.size, dtype=np.float64)

    inverse_two_epsilon_squared = 1.0 / (2.0 * epsilon * epsilon)
    radius = int(gaussian_sigma_cutoff * epsilon / dx) + 1
    cumulative_discarded = 0.0
    checkpoint_index = 0

    for step in range(1, checkpoints[-1] + 1):
        if dynamics_code == 1:
            mu = schedule_u_c + schedule_k / (np.log(step + c_offset) ** 2)
        else:
            mu = static_mu
        next_probability = np.zeros(bins, dtype=np.float64)

        for source in range(bins):
            source_mass = probability[source]
            if source_mass < probability_threshold:
                cumulative_discarded += source_mass
                continue

            mapped = 1.0 - mu * center_squares[source]
            center_index = int(np.floor((mapped - first_edge) / dx))
            lower = center_index - radius
            upper = center_index + radius
            if lower < 0:
                lower = 0
            if upper >= bins:
                upper = bins - 1

            weight_sum = 0.0
            for target in range(lower, upper + 1):
                distance = centers[target] - mapped
                weight_sum += np.exp(-(distance * distance) * inverse_two_epsilon_squared)

            if weight_sum == 0.0:
                continue
            inverse_weight_sum = 1.0 / weight_sum
            for target in range(lower, upper + 1):
                distance = centers[target] - mapped
                weight = np.exp(-(distance * distance) * inverse_two_epsilon_squared)
                flow = source_mass * weight * inverse_weight_sum
                next_probability[target] += flow
                transition[source, target] += flow

        probability = next_probability
        if checkpoint_index < checkpoints.size and step == checkpoints[checkpoint_index]:
            snapshots[checkpoint_index, :, :] = transition
            discarded[checkpoint_index] = cumulative_discarded
            masses[checkpoint_index] = probability.sum()
            last_mus[checkpoint_index] = mu
            checkpoint_index += 1

    return snapshots, discarded, masses, last_mus, radius, initial_bin


def simulate_checkpoints(
    config: MediumConfig,
    bins: int,
    checkpoint_steps: Iterable[int],
    partition_shift: float = 0.0,
    dynamics: str = "dynamic",
    static_mu: float | None = None,
) -> tuple[dict[int, np.ndarray], dict[int, dict[str, Any]]]:
    checkpoints = np.asarray(sorted(set(int(step) for step in checkpoint_steps)), dtype=np.int64)
    if checkpoints.size == 0 or checkpoints[0] <= 0:
        raise ValueError("checkpoint steps must be positive")
    if dynamics not in {"dynamic", "static"}:
        raise ValueError(dynamics)
    if dynamics == "static" and static_mu is None:
        raise ValueError("static_mu is required for a static profile")

    schedule = schedule_parameters(config)
    snapshots, discarded, masses, last_mus, radius, initial_bin = _simulate_compiled(
        bins,
        checkpoints,
        partition_shift,
        1 if dynamics == "dynamic" else 0,
        0.0 if static_mu is None else static_mu,
        config.c_offset,
        schedule["k"],
        schedule["u_c"],
        config.epsilon,
        config.gaussian_sigma_cutoff,
        config.probability_threshold,
        config.initial_x,
    )

    matrices: dict[int, np.ndarray] = {}
    metadata: dict[int, dict[str, Any]] = {}
    for index, step_value in enumerate(checkpoints):
        step = int(step_value)
        transition = snapshots[index]
        row_sums = transition.sum(axis=1)
        active = row_sums > 0.0
        matrices[step] = transition
        metadata[step] = {
            "steps": step,
            "bins": bins,
            "partition_shift_fraction": partition_shift,
            "partition_control_type": "translated_grid" if partition_shift else "reference_grid",
            "dynamics": dynamics,
            "static_mu": static_mu,
            "last_mu": float(last_mus[index]),
            "gaussian_radius_bins": int(radius),
            "epsilon_over_dx": float(config.epsilon / (2.0 / bins)),
            "discarded_mass_sum_over_steps": float(discarded[index]),
            "probability_mass": float(masses[index]),
            "probability_mass_loss": float(max(0.0, 1.0 - masses[index])),
            "transition_nnz": int(np.count_nonzero(transition)),
            "occupied_rows": int(np.sum(active)),
            "positive_occupation_min": float(row_sums[active].min()),
            "positive_occupation_max": float(row_sums[active].max()),
            "initial_bin": int(initial_bin),
        }
    return matrices, metadata


def matrix_content_hash(matrix: np.ndarray) -> str:
    return hashlib.sha256(np.ascontiguousarray(matrix, dtype=np.float64).tobytes()).hexdigest()


def normalize_transition(
    transition: np.ndarray,
) -> tuple[sp.csr_matrix, sp.csr_matrix, np.ndarray, np.ndarray]:
    sparse_transition = sp.csr_matrix(transition)
    row_sums = np.asarray(sparse_transition.sum(axis=1)).ravel()
    active = row_sums > 0.0
    safe_sums = row_sums.copy()
    safe_sums[~active] = 1.0
    inverse = sp.diags(1.0 / safe_sums)
    correct = (inverse @ sparse_transition).tocsr()
    legacy = (sparse_transition @ inverse).tocsr()
    return correct, legacy, safe_sums, active


def deterministic_start(size: int, name: str) -> np.ndarray:
    if name == "ones":
        return np.ones(size)
    if name == "ramp":
        return np.linspace(1.0, 2.0, size)
    if name == "seed17_normal":
        return np.random.default_rng(17).normal(size=size)
    raise ValueError(name)


def solve_spectrum(
    matrix: sp.csr_matrix,
    k: int,
    config: MediumConfig,
    start_name: str,
) -> dict[str, Any]:
    if k >= matrix.shape[0] - 1:
        raise ValueError("ARPACK k must be smaller than dimension minus one")
    ncv = min(matrix.shape[0], max(k + 2, config.arpack_ncv))
    converged = True
    try:
        values, vectors = eigs(
            matrix,
            k=k,
            which="LM",
            v0=deterministic_start(matrix.shape[0], start_name),
            ncv=ncv,
            tol=config.arpack_tolerance,
            maxiter=config.arpack_maxiter,
        )
    except ArpackNoConvergence as error:
        converged = False
        values = error.eigenvalues
        vectors = error.eigenvectors
        if values is None or vectors is None or values.size == 0:
            return {
                "values": np.array([], dtype=np.complex128),
                "residuals": np.array([], dtype=np.float64),
                "start": start_name,
                "k_requested": k,
                "k_returned": 0,
                "ncv": ncv,
                "converged": False,
            }

    residuals = np.linalg.norm(matrix @ vectors - vectors * values, axis=0) / np.linalg.norm(
        vectors, axis=0
    )
    order = np.lexsort((values.imag, values.real, -np.abs(values)))
    return {
        "values": values[order],
        "residuals": residuals[order],
        "start": start_name,
        "k_requested": k,
        "k_returned": int(values.size),
        "ncv": ncv,
        "converged": converged,
    }


def spectrum_records(solution: dict[str, Any]) -> list[dict[str, float]]:
    return [
        {
            "real": float(value.real),
            "imag": float(value.imag),
            "modulus": float(abs(value)),
            "phase": float(np.angle(value)),
            "relative_residual": float(residual),
        }
        for value, residual in zip(solution["values"], solution["residuals"], strict=True)
    ]


def layer_values(
    solution: dict[str, Any], config: MediumConfig, layer: str, upper_half: bool = True
) -> np.ndarray:
    values = solution["values"]
    residuals = solution["residuals"]
    if layer == "strong":
        mask = np.abs(values) >= config.strong_modulus_floor
    elif layer == "moderate":
        mask = (np.abs(values) >= config.moderate_modulus_floor) & (
            np.abs(values) < config.strong_modulus_floor
        )
    elif layer == "weak":
        mask = (np.abs(values) >= config.weak_modulus_floor) & (
            np.abs(values) < config.moderate_modulus_floor
        )
    else:
        raise ValueError(layer)
    mask &= residuals <= config.residual_ceiling
    if upper_half:
        mask &= values.imag > config.imag_threshold
    selected = values[mask]
    return selected[np.argsort(np.angle(selected), kind="stable")]


def conjugate_pair_defect(values: np.ndarray) -> float:
    if values.size == 0:
        return float("inf")
    defects = []
    for value in values:
        distances = np.abs(values - np.conjugate(value)) / max(abs(value), 1.0e-15)
        defects.append(float(distances.min()))
    return max(defects)


def conjugate_layers_pass(
    profiles: dict[str, Any], profile_names: Iterable[str], config: MediumConfig
) -> bool:
    """Gate resolved strong/moderate layers, not a weak ARPACK edge truncation."""
    return all(
        profiles[name]["spectrum"]["conjugate_pair_defect"][layer]
        <= config.conjugate_pair_defect_ceiling
        for name in profile_names
        for layer in ("strong", "moderate")
    )


def _phase_ranks(values: np.ndarray) -> np.ndarray:
    order = np.argsort(np.angle(values), kind="stable")
    ranks = np.empty(values.size, dtype=np.int64)
    ranks[order] = np.arange(values.size)
    return ranks


def _assignment_pairs_with_cutoff(
    normalized_distances: np.ndarray, distance_cutoff: float
) -> list[tuple[int, int]]:
    """Maximize valid match cardinality, then minimize total normalized drift."""
    if distance_cutoff <= 0.0:
        raise ValueError("distance_cutoff must be positive")
    reference_count, comparison_count = normalized_distances.shape
    if reference_count == 0 or comparison_count == 0:
        return []

    size = reference_count + comparison_count
    maximum_pair_count = min(reference_count, comparison_count)
    valid_scale = distance_cutoff * (maximum_pair_count + 1)
    large = 1.0e6
    costs = np.full((size, size), large, dtype=np.float64)
    valid = normalized_distances < distance_cutoff
    costs[:reference_count, :comparison_count] = np.where(
        valid, normalized_distances / valid_scale, large
    )
    for index in range(reference_count):
        costs[index, comparison_count + index] = 1.0
    for index in range(comparison_count):
        costs[reference_count + index, index] = 1.0
    costs[reference_count:, comparison_count:] = 0.0
    rows, columns = linear_sum_assignment(costs)
    return [
        (int(row), int(column))
        for row, column in zip(rows, columns, strict=True)
        if row < reference_count
        and column < comparison_count
        and valid[row, column]
    ]


def match_branches(
    reference: np.ndarray, comparison: np.ndarray, config: MediumConfig
) -> dict[str, Any]:
    reference_count = int(reference.size)
    comparison_count = int(comparison.size)
    if reference_count == 0 or comparison_count == 0:
        return {
            "matched_count": 0,
            "unmatched_reference": reference_count,
            "unmatched_comparison": comparison_count,
            "survival_fraction": 0.0,
            "stable_fraction": 0.0,
            "_pairs": [],
            "_stable_reference_indices": [],
        }

    normalized = np.abs(reference[:, None] - comparison[None, :]) / np.maximum(
        np.abs(reference)[:, None], 1.0e-15
    )
    assignments = _assignment_pairs_with_cutoff(
        normalized, config.matching_distance_cutoff
    )

    reference_ranks = _phase_ranks(reference)
    comparison_ranks = _phase_ranks(comparison)
    pairs: list[dict[str, Any]] = []
    stable_reference_indices: list[int] = []
    for row, column in assignments:
        distance = float(normalized[row, column])
        left = reference[row]
        right = comparison[column]
        phase_drift = float(abs(np.angle(right / left)))
        log_modulus_ratio = float(abs(np.log(abs(right) / abs(left))))
        alternatives = np.sort(normalized[row])
        ambiguity_ratio = (
            float(alternatives[0] / alternatives[1])
            if alternatives.size >= 2 and alternatives[1] > 0.0
            else 0.0
        )
        rank_displacement = int(abs(reference_ranks[row] - comparison_ranks[column]))
        stable = bool(
            distance <= config.max_drift_ceiling
            and phase_drift <= config.phase_drift_ceiling
            and log_modulus_ratio <= config.log_modulus_ratio_ceiling
            and ambiguity_ratio <= config.ambiguity_ratio_ceiling
        )
        if stable:
            stable_reference_indices.append(int(row))
        pairs.append(
            {
                "reference_index": int(row),
                "comparison_index": int(column),
                "normalized_complex_drift": distance,
                "phase_drift": phase_drift,
                "log_modulus_ratio": log_modulus_ratio,
                "ambiguity_ratio": ambiguity_ratio,
                "phase_rank_displacement": rank_displacement,
                "stable": stable,
            }
        )

    distances = np.array([pair["normalized_complex_drift"] for pair in pairs])
    phase_drifts = np.array([pair["phase_drift"] for pair in pairs])
    modulus_drifts = np.array([pair["log_modulus_ratio"] for pair in pairs])
    rank_drifts = np.array([pair["phase_rank_displacement"] for pair in pairs])
    return {
        "matched_count": len(pairs),
        "unmatched_reference": reference_count - len(pairs),
        "unmatched_comparison": comparison_count - len(pairs),
        "survival_fraction": float(len(pairs) / reference_count),
        "stable_fraction": float(len(stable_reference_indices) / reference_count),
        "median_normalized_complex_drift": float(np.median(distances)) if distances.size else None,
        "p90_normalized_complex_drift": float(np.quantile(distances, 0.9)) if distances.size else None,
        "max_normalized_complex_drift": float(np.max(distances)) if distances.size else None,
        "max_phase_drift": float(np.max(phase_drifts)) if phase_drifts.size else None,
        "max_log_modulus_ratio": float(np.max(modulus_drifts)) if modulus_drifts.size else None,
        "median_phase_rank_displacement": float(np.median(rank_drifts)) if rank_drifts.size else None,
        "max_phase_rank_displacement": int(np.max(rank_drifts)) if rank_drifts.size else None,
        "pairs": pairs,
        "_pairs": pairs,
        "_stable_reference_indices": stable_reference_indices,
    }


def sparse_similarity_residual(
    correct: sp.csr_matrix, legacy: sp.csr_matrix, row_sums: np.ndarray
) -> float:
    difference = legacy - sp.diags(row_sums) @ correct @ sp.diags(1.0 / row_sums)
    difference = difference.tocsr()
    return float(np.max(np.abs(difference.data))) if difference.nnz else 0.0


def one_step_kernel(
    config: MediumConfig, bins: int, partition_shift: float, mu: float
) -> sp.csr_matrix:
    dx = 2.0 / bins
    centers = -1.0 + (np.arange(bins, dtype=np.float64) + 0.5 + partition_shift) * dx
    first_edge = centers[0] - 0.5 * dx
    radius = int(config.gaussian_sigma_cutoff * config.epsilon / dx) + 1
    inverse_two_epsilon_squared = 1.0 / (2.0 * config.epsilon**2)
    rows: list[int] = []
    columns: list[int] = []
    data: list[float] = []
    for source, center in enumerate(centers):
        mapped = 1.0 - mu * center * center
        center_index = int(np.floor((mapped - first_edge) / dx))
        lower = max(0, center_index - radius)
        upper = min(bins - 1, center_index + radius)
        targets = np.arange(lower, upper + 1)
        weights = np.exp(-((centers[targets] - mapped) ** 2) * inverse_two_epsilon_squared)
        weights /= weights.sum()
        rows.extend([source] * targets.size)
        columns.extend(int(value) for value in targets)
        data.extend(float(value) for value in weights)
    return sp.csr_matrix((data, (rows, columns)), shape=(bins, bins))


def static_kernel_identity_residual(
    correct: sp.csr_matrix,
    active: np.ndarray,
    config: MediumConfig,
    bins: int,
    partition_shift: float,
    mu: float,
) -> float:
    kernel = one_step_kernel(config, bins, partition_shift, mu)
    difference = (correct[active] - kernel[active]).tocsr()
    return float(np.max(np.abs(difference.data))) if difference.nnz else 0.0


def profile_summary(
    name: str,
    transition: np.ndarray,
    metadata: dict[str, Any],
    config: MediumConfig,
    start_name: str,
    static_mu: float | None = None,
) -> tuple[dict[str, Any], dict[str, Any], sp.csr_matrix, sp.csr_matrix, np.ndarray]:
    correct, legacy, row_sums, active = normalize_transition(transition)
    solution = solve_spectrum(correct, config.profile_k, config, start_name)
    values = solution["values"]
    strong_all = layer_values(solution, config, "strong", upper_half=False)
    moderate_all = layer_values(solution, config, "moderate", upper_half=False)
    weak_all = layer_values(solution, config, "weak", upper_half=False)
    summary: dict[str, Any] = {
        "name": name,
        "metadata": metadata,
        "transition_content_sha256": matrix_content_hash(transition),
        "normalization": {
            "correct_occupied_row_sum_max_error": float(
                np.max(np.abs(np.asarray(correct.sum(axis=1)).ravel()[active] - 1.0))
            ),
            "legacy_occupied_row_sum_max_error": float(
                np.max(np.abs(np.asarray(legacy.sum(axis=1)).ravel()[active] - 1.0))
            ),
            "occupation_condition_number": float(row_sums[active].max() / row_sums[active].min()),
            "similarity_max_abs_residual": sparse_similarity_residual(correct, legacy, row_sums),
        },
        "spectrum": {
            "converged": bool(solution["converged"]),
            "requested_k": int(solution["k_requested"]),
            "returned_k": int(solution["k_returned"]),
            "ncv": int(solution["ncv"]),
            "edge_modulus": float(np.min(np.abs(values))) if values.size else None,
            "max_relative_residual": float(solution["residuals"].max())
            if solution["residuals"].size
            else None,
            "conjugate_pair_defect": {
                "strong": conjugate_pair_defect(strong_all),
                "moderate": conjugate_pair_defect(moderate_all),
                "weak_diagnostic": conjugate_pair_defect(weak_all),
                "weak_is_edge_truncated": bool(
                    values.size
                    and np.min(np.abs(values)) >= config.weak_modulus_floor
                ),
            },
            "strong_upper_count": int(layer_values(solution, config, "strong").size),
            "moderate_upper_count": int(layer_values(solution, config, "moderate").size),
            "weak_upper_count": int(layer_values(solution, config, "weak").size),
            "records": spectrum_records(solution),
        },
    }
    if static_mu is not None:
        summary["static_kernel_identity_residual"] = static_kernel_identity_residual(
            correct,
            active,
            config,
            metadata["bins"],
            metadata["partition_shift_fraction"],
            static_mu,
        )
    return summary, solution, correct, legacy, active


def save_raw_transition(path: Path, transition: np.ndarray, metadata: dict[str, Any]) -> None:
    sparse = sp.csr_matrix(transition)
    path.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        path,
        data=sparse.data,
        indices=sparse.indices,
        indptr=sparse.indptr,
        shape=np.asarray(sparse.shape, dtype=np.int64),
        metadata=np.asarray(json.dumps(metadata, sort_keys=True)),
        content_sha256=np.asarray(matrix_content_hash(transition)),
    )


def load_raw_transition(path: Path) -> tuple[sp.csr_matrix, dict[str, Any], str]:
    with np.load(path, allow_pickle=False) as payload:
        shape = tuple(int(value) for value in payload["shape"])
        matrix = sp.csr_matrix(
            (payload["data"], payload["indices"], payload["indptr"]), shape=shape
        )
        metadata = json.loads(str(payload["metadata"]))
        content_hash = str(payload["content_sha256"])
    return matrix, metadata, content_hash


def dense_anchor_audit(config: MediumConfig) -> dict[str, Any]:
    matrices, metadata = simulate_checkpoints(
        config, config.dense_anchor_bins, [config.dense_anchor_steps]
    )
    transition = matrices[config.dense_anchor_steps]
    correct, _, _, _ = normalize_transition(transition)
    dense_values = np.linalg.eigvals(correct.toarray())
    k = min(128, config.dense_anchor_bins - 2)
    solution = solve_spectrum(correct, k, config, config.primary_start)
    dense_top = dense_values[np.argsort(-np.abs(dense_values), kind="stable")[:k]]
    distances = np.abs(dense_top[:, None] - solution["values"][None, :])
    rows, columns = linear_sum_assignment(distances)
    matched = distances[rows, columns]
    dense_strong = dense_values[
        (np.abs(dense_values) >= config.strong_modulus_floor)
        & (dense_values.imag > config.imag_threshold)
    ]
    sparse_strong = layer_values(solution, config, "strong")
    strong_match = match_branches(dense_strong, sparse_strong, config)
    return {
        "metadata": metadata[config.dense_anchor_steps],
        "transition_content_sha256": matrix_content_hash(transition),
        "matched_count": int(matched.size),
        "median_complex_distance": float(np.median(matched)),
        "max_complex_distance": float(np.max(matched)),
        "strong_upper_match": _strip_internal(strong_match),
        "sparse_max_relative_residual": float(solution["residuals"].max()),
    }


def _profile_gate(match: dict[str, Any], config: MediumConfig) -> bool:
    required = (
        match.get("median_normalized_complex_drift"),
        match.get("p90_normalized_complex_drift"),
        match.get("max_normalized_complex_drift"),
        match.get("max_phase_drift"),
        match.get("max_log_modulus_ratio"),
        match.get("median_phase_rank_displacement"),
        match.get("max_phase_rank_displacement"),
    )
    if any(value is None for value in required):
        return False
    return bool(
        match["median_normalized_complex_drift"] <= config.median_drift_ceiling
        and match["p90_normalized_complex_drift"] <= config.p90_drift_ceiling
        and match["max_normalized_complex_drift"] <= config.max_drift_ceiling
        and match["max_phase_drift"] <= config.phase_drift_ceiling
        and match["max_log_modulus_ratio"] <= config.log_modulus_ratio_ceiling
        and match["median_phase_rank_displacement"] <= config.phase_rank_median_ceiling
        and match["max_phase_rank_displacement"] <= config.phase_rank_max_ceiling
    )


def _strip_internal(match: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in match.items() if not key.startswith("_")}


def build_report(
    config: MediumConfig = MediumConfig(), raw_directory: Path | None = None
) -> dict[str, Any]:
    schedule = schedule_parameters(config)
    controls = static_controls(config)

    reference_matrices, reference_metadata = simulate_checkpoints(
        config, config.reference_bins, config.time_prefixes
    )
    reference_transition = reference_matrices[config.reference_steps]
    reference_summary, reference_solution, reference_q, reference_b, reference_active = (
        profile_summary(
            "dynamic_reference",
            reference_transition,
            reference_metadata[config.reference_steps],
            config,
            config.primary_start,
        )
    )
    reference_strong = layer_values(reference_solution, config, "strong")

    profiles: dict[str, Any] = {"dynamic_reference": reference_summary}
    solutions: dict[str, dict[str, Any]] = {"dynamic_reference": reference_solution}
    active_rows: dict[str, np.ndarray] = {"dynamic_reference": reference_active}

    for step in config.time_prefixes:
        if step == config.reference_steps:
            continue
        name = f"dynamic_steps_{step}"
        summary, solution, _, _, active = profile_summary(
            name,
            reference_matrices[step],
            reference_metadata[step],
            config,
            config.primary_start,
        )
        profiles[name] = summary
        solutions[name] = solution
        active_rows[name] = active

    for bins in config.bin_profiles:
        if bins == config.reference_bins:
            continue
        matrices, metadata = simulate_checkpoints(config, bins, [config.reference_steps])
        name = f"dynamic_bins_{bins}"
        summary, solution, _, _, active = profile_summary(
            name,
            matrices[config.reference_steps],
            metadata[config.reference_steps],
            config,
            config.primary_start,
        )
        profiles[name] = summary
        solutions[name] = solution
        active_rows[name] = active

    translated_matrices, translated_metadata = simulate_checkpoints(
        config,
        config.reference_bins,
        [config.reference_steps],
        partition_shift=0.5,
    )
    translated_name = "dynamic_translated_half_bin"
    translated_summary, translated_solution, _, _, translated_active = profile_summary(
        translated_name,
        translated_matrices[config.reference_steps],
        translated_metadata[config.reference_steps],
        config,
        config.primary_start,
    )
    profiles[translated_name] = translated_summary
    solutions[translated_name] = translated_solution
    active_rows[translated_name] = translated_active

    static_solutions: dict[str, dict[str, Any]] = {}
    static_transitions: dict[str, np.ndarray] = {}
    for control_name, mu in controls.items():
        matrices, metadata = simulate_checkpoints(
            config,
            config.reference_bins,
            [config.reference_steps],
            dynamics="static",
            static_mu=mu,
        )
        transition = matrices[config.reference_steps]
        name = f"static_{control_name}"
        summary, solution, _, _, active = profile_summary(
            name,
            transition,
            metadata[config.reference_steps],
            config,
            config.primary_start,
            static_mu=mu,
        )
        profiles[name] = summary
        solutions[name] = solution
        active_rows[name] = active
        static_solutions[name] = solution
        static_transitions[name] = transition

    internal_names = [
        f"dynamic_steps_{config.time_prefixes[0]}",
        f"dynamic_steps_{config.time_prefixes[-1]}",
        f"dynamic_bins_{config.bin_profiles[0]}",
        f"dynamic_bins_{config.bin_profiles[-1]}",
        translated_name,
    ]
    internal_matches_raw = {
        name: match_branches(reference_strong, layer_values(solutions[name], config, "strong"), config)
        for name in internal_names
    }
    internal_matches = {
        name: _strip_internal(match) for name, match in internal_matches_raw.items()
    }
    internal_profile_passes = {
        name: _profile_gate(match, config) for name, match in internal_matches_raw.items()
    }

    stable_sets = [set(match["_stable_reference_indices"]) for match in internal_matches_raw.values()]
    surviving_all = set.intersection(*stable_sets) if stable_sets else set()
    all_profile_survival_fraction = (
        float(len(surviving_all) / reference_strong.size) if reference_strong.size else 0.0
    )

    time_low = internal_matches_raw[f"dynamic_steps_{config.time_prefixes[0]}"]
    time_high = internal_matches_raw[f"dynamic_steps_{config.time_prefixes[-1]}"]
    bin_low = internal_matches_raw[f"dynamic_bins_{config.bin_profiles[0]}"]
    bin_high = internal_matches_raw[f"dynamic_bins_{config.bin_profiles[-1]}"]
    time_convergence = bool(
        time_high.get("median_normalized_complex_drift") is not None
        and time_low.get("median_normalized_complex_drift") is not None
        and time_high["median_normalized_complex_drift"]
        <= max(0.8 * time_low["median_normalized_complex_drift"], 0.01)
    )
    bin_convergence = bool(
        bin_high.get("median_normalized_complex_drift") is not None
        and bin_low.get("median_normalized_complex_drift") is not None
        and bin_high["median_normalized_complex_drift"]
        <= max(0.8 * bin_low["median_normalized_complex_drift"], 0.01)
    )

    reference_k_solutions = {
        str(k): solve_spectrum(reference_q, k, config, config.primary_start)
        for k in config.reference_k_guard
    }
    k_low = reference_k_solutions[str(config.reference_k_guard[0])]
    k_high = reference_k_solutions[str(config.reference_k_guard[-1])]
    k_guard_match_raw = match_branches(
        layer_values(k_low, config, "strong"), layer_values(k_high, config, "strong"), config
    )
    k_edge_modulus = float(np.min(np.abs(k_high["values"]))) if k_high["values"].size else None
    k_guard = {
        "low_k": config.reference_k_guard[0],
        "high_k": config.reference_k_guard[-1],
        "high_k_edge_modulus": k_edge_modulus,
        "strong_branch_match": _strip_internal(k_guard_match_raw),
        "low_k_records": spectrum_records(k_low),
        "high_k_records": spectrum_records(k_high),
    }

    solver_audit: dict[str, Any] = {}
    for matrix_name, matrix in (("correct_Q", reference_q), ("legacy_B", reference_b)):
        matrix_results: dict[str, Any] = {}
        for start_name in (config.primary_start, config.secondary_start):
            solution = solve_spectrum(matrix, config.profile_k, config, start_name)
            match = match_branches(reference_strong, layer_values(solution, config, "strong"), config)
            matrix_results[start_name] = {
                "converged": bool(solution["converged"]),
                "requested_k": int(solution["k_requested"]),
                "returned_k": int(solution["k_returned"]),
                "max_relative_residual": float(solution["residuals"].max())
                if solution["residuals"].size
                else None,
                "strong_branch_match_to_reference": _strip_internal(match),
            }
        solver_audit[matrix_name] = matrix_results

    per_reference_internal_radius = np.full(
        reference_strong.size, config.matching_distance_cutoff
    )
    for reference_index in range(reference_strong.size):
        observed = []
        for match in internal_matches_raw.values():
            for pair in match["_pairs"]:
                if pair["reference_index"] == reference_index:
                    observed.append(pair["normalized_complex_drift"])
                    break
        if observed:
            per_reference_internal_radius[reference_index] = max(observed)

    static_union = np.concatenate(
        [layer_values(solution, config, "strong") for solution in static_solutions.values()]
    )
    if reference_strong.size and static_union.size:
        static_distances = np.abs(reference_strong[:, None] - static_union[None, :]) / np.maximum(
            np.abs(reference_strong)[:, None], 1.0e-15
        )
        nearest_static = static_distances.min(axis=1)
        margins = nearest_static / np.maximum(per_reference_internal_radius, 1.0e-6)
    else:
        nearest_static = np.array([], dtype=np.float64)
        margins = np.array([], dtype=np.float64)
    margin_median = float(np.median(margins)) if margins.size else 0.0
    margin_fraction = float(np.mean(margins >= 1.5)) if margins.size else 0.0
    static_margin = {
        "reference_branch_count": int(reference_strong.size),
        "static_union_branch_count": int(static_union.size),
        "median_margin": margin_median,
        "fraction_margin_at_least_1_5": margin_fraction,
        "median_nearest_static_normalized_distance": float(np.median(nearest_static))
        if nearest_static.size
        else None,
        "per_branch_margins": [float(value) for value in margins],
    }

    support_controls: dict[str, Any] = {}
    dynamic_support = active_rows["dynamic_reference"]
    for name in static_solutions:
        static_support = active_rows[name]
        intersection = int(np.sum(dynamic_support & static_support))
        union = int(np.sum(dynamic_support | static_support))
        support_controls[name] = {
            "intersection": intersection,
            "union": union,
            "jaccard": float(intersection / union) if union else 1.0,
        }

    dynamic_repeat, _ = simulate_checkpoints(
        config, config.reference_bins, [config.reference_steps]
    )
    dynamic_repeat_hash = matrix_content_hash(dynamic_repeat[config.reference_steps])
    primary_static_name = "static_mean_matched"
    primary_static_repeat, _ = simulate_checkpoints(
        config,
        config.reference_bins,
        [config.reference_steps],
        dynamics="static",
        static_mu=controls["mean_matched"],
    )
    static_repeat_hash = matrix_content_hash(primary_static_repeat[config.reference_steps])
    hash_reproduction = {
        "dynamic_reference": {
            "first": profiles["dynamic_reference"]["transition_content_sha256"],
            "repeat": dynamic_repeat_hash,
            "equal": profiles["dynamic_reference"]["transition_content_sha256"]
            == dynamic_repeat_hash,
        },
        "static_mean_matched": {
            "first": profiles[primary_static_name]["transition_content_sha256"],
            "repeat": static_repeat_hash,
            "equal": profiles[primary_static_name]["transition_content_sha256"]
            == static_repeat_hash,
        },
    }

    raw_artifacts: dict[str, Any] = {}
    if raw_directory is not None:
        raw_specs = {
            "dynamic_reference": (
                reference_transition,
                reference_metadata[config.reference_steps],
            ),
            "static_mean_matched": (
                static_transitions[primary_static_name],
                profiles[primary_static_name]["metadata"],
            ),
        }
        for name, (transition, metadata) in raw_specs.items():
            path = raw_directory / f"{name}_T.npz"
            save_raw_transition(path, transition, metadata)
            loaded, loaded_metadata, declared_hash = load_raw_transition(path)
            loaded_hash = matrix_content_hash(loaded.toarray())
            raw_artifacts[name] = {
                "path": str(path),
                "declared_content_sha256": declared_hash,
                "loaded_content_sha256": loaded_hash,
                "expected_content_sha256": matrix_content_hash(transition),
                "metadata_roundtrip_equal": loaded_metadata == metadata,
            }

    mechanics_profile_names = list(profiles)
    mass_gate = all(
        profiles[name]["metadata"]["discarded_mass_sum_over_steps"]
        <= config.probability_mass_loss_ceiling
        and profiles[name]["metadata"]["probability_mass_loss"]
        <= config.probability_mass_loss_ceiling
        for name in mechanics_profile_names
    )
    row_gate = all(
        profiles[name]["normalization"]["correct_occupied_row_sum_max_error"]
        <= config.row_sum_error_ceiling
        for name in mechanics_profile_names
    )
    static_identity_gate = all(
        profiles[name]["static_kernel_identity_residual"]
        <= config.static_kernel_identity_ceiling
        for name in static_solutions
    )
    residual_gate = all(
        profiles[name]["spectrum"]["max_relative_residual"] is not None
        and profiles[name]["spectrum"]["max_relative_residual"] <= config.residual_ceiling
        for name in mechanics_profile_names
    )
    conjugate_gate = conjugate_layers_pass(profiles, mechanics_profile_names, config)
    hash_gate = all(entry["equal"] for entry in hash_reproduction.values())
    raw_gate = all(
        entry["declared_content_sha256"] == entry["loaded_content_sha256"]
        == entry["expected_content_sha256"]
        and entry["metadata_roundtrip_equal"]
        for entry in raw_artifacts.values()
    ) if raw_artifacts else True
    profile_solver_convergence_gate = all(
        profiles[name]["spectrum"]["converged"]
        and profiles[name]["spectrum"]["returned_k"]
        == profiles[name]["spectrum"]["requested_k"]
        for name in mechanics_profile_names
    )
    all_profile_k_edge_gate = all(
        profiles[name]["spectrum"]["edge_modulus"] is not None
        and profiles[name]["spectrum"]["edge_modulus"] < config.k_edge_modulus_ceiling
        for name in mechanics_profile_names
    )
    k_guard_solver_gate = all(
        solution["converged"]
        and solution["k_returned"] == solution["k_requested"]
        and solution["residuals"].size > 0
        and float(solution["residuals"].max()) <= config.residual_ceiling
        for solution in reference_k_solutions.values()
    )
    k_guard_match_gate = bool(
        k_guard_match_raw["matched_count"] == reference_strong.size
        and k_guard_match_raw["survival_fraction"] == 1.0
        and k_guard_match_raw["stable_fraction"] == 1.0
    )
    solver_start_similarity_gate = all(
        entry["converged"]
        and entry["returned_k"] == entry["requested_k"]
        and entry["max_relative_residual"] is not None
        and entry["max_relative_residual"] <= config.residual_ceiling
        and entry["strong_branch_match_to_reference"]["matched_count"]
        == reference_strong.size
        and entry["strong_branch_match_to_reference"]["survival_fraction"] == 1.0
        and entry["strong_branch_match_to_reference"]["stable_fraction"] == 1.0
        for matrix_results in solver_audit.values()
        for entry in matrix_results.values()
    )
    dense_anchor = dense_anchor_audit(config)
    dense_anchor_match = dense_anchor["strong_upper_match"]
    dense_anchor_gate = bool(
        dense_anchor["sparse_max_relative_residual"] <= config.residual_ceiling
        and dense_anchor_match["matched_count"] > 0
        and dense_anchor_match["survival_fraction"] == 1.0
        and dense_anchor_match["stable_fraction"] == 1.0
    )
    k_edge_gate = bool(
        k_edge_modulus is not None
        and k_edge_modulus < config.k_edge_modulus_ceiling
        and all_profile_k_edge_gate
        and k_guard_solver_gate
        and k_guard_match_gate
    )
    mechanics_pass = all(
        (
            mass_gate,
            row_gate,
            static_identity_gate,
            residual_gate,
            conjugate_gate,
            profile_solver_convergence_gate,
            k_edge_gate,
            solver_start_similarity_gate,
            dense_anchor_gate,
            hash_gate,
            raw_gate,
        )
    )

    branch_count_pass = reference_strong.size >= config.minimum_upper_half_strong_branches
    survival_pass = all_profile_survival_fraction >= config.survival_fraction_minimum
    phase_rank_pass = all(
        match.get("median_phase_rank_displacement") is not None
        and match["median_phase_rank_displacement"] <= config.phase_rank_median_ceiling
        and match["max_phase_rank_displacement"] <= config.phase_rank_max_ceiling
        for match in internal_matches_raw.values()
    )
    internal_pass = all(internal_profile_passes.values()) and time_convergence and bin_convergence
    static_margin_pass = (
        margin_median >= config.dynamic_static_margin_median_minimum
        and margin_fraction >= config.dynamic_static_margin_fraction_minimum
    )

    if not mechanics_pass:
        recommended_verdict = "NOT_TESTABLE"
    elif not branch_count_pass or not survival_pass or not phase_rank_pass:
        recommended_verdict = "STOP_SCOPED"
    elif not internal_pass or not static_margin_pass:
        recommended_verdict = "REVISE"
    else:
        recommended_verdict = "GO_WITH_LIMITATIONS"

    return {
        "audit_id": AUDIT_ID,
        "formal_candidate": False,
        "target_free_computation": True,
        "target_tables_read_during_audit": False,
        "historical_target_fitted_parameters": {
            "epsilon": {
                "value": config.epsilon,
                "provenance": "selected in legacy work using Riemann zeros 2--6",
                "use_in_this_audit": "frozen without target-table access or reoptimization",
            }
        },
        "source_lock": "configs/source_locks/P4-LOGISTIC-MEDIUM-PHYSICAL-EPSILON.yaml",
        "source_lock_version": 2,
        "runtime": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "numba": numba.__version__,
            "llvmlite": llvmlite.__version__,
        },
        "config": asdict(config),
        "schedule": schedule,
        "static_controls": controls,
        "determinant_convention": None,
        "profiles": profiles,
        "internal_branch_matches": internal_matches,
        "all_profile_stable_survival_fraction": all_profile_survival_fraction,
        "convergence": {
            "time_drift_contracts": time_convergence,
            "bin_drift_contracts": bin_convergence,
        },
        "k_edge_guard": k_guard,
        "solver_start_and_similarity_audit": solver_audit,
        "dynamic_static_margin": static_margin,
        "dynamic_static_support": support_controls,
        "hash_reproduction": hash_reproduction,
        "dense_physical_epsilon_anchor": dense_anchor,
        "raw_transition_artifacts": raw_artifacts,
        "acceptance": {
            "mechanics": {
                "mass_gate": mass_gate,
                "row_sum_gate": row_gate,
                "static_kernel_identity_gate": static_identity_gate,
                "residual_gate": residual_gate,
                "conjugate_pair_gate": conjugate_gate,
                "profile_solver_convergence_gate": profile_solver_convergence_gate,
                "all_profile_k_edge_gate": all_profile_k_edge_gate,
                "reference_k_guard_solver_gate": k_guard_solver_gate,
                "reference_k_guard_match_gate": k_guard_match_gate,
                "k_edge_gate": k_edge_gate,
                "solver_start_and_similarity_gate": solver_start_similarity_gate,
                "dense_anchor_gate": dense_anchor_gate,
                "hash_reproduction_gate": hash_gate,
                "raw_roundtrip_gate": raw_gate,
                "pass": mechanics_pass,
            },
            "reference_strong_upper_branch_count": int(reference_strong.size),
            "branch_count_pass": branch_count_pass,
            "internal_profile_passes": internal_profile_passes,
            "all_internal_profiles_pass": internal_pass,
            "all_profile_survival_pass": survival_pass,
            "phase_rank_pass": phase_rank_pass,
            "dynamic_static_margin_pass": static_margin_pass,
        },
        "route_a_preassessment": {
            "status": "NOT_TESTABLE",
            "diagnostic_tuple": ["A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": (
            "This audit reads no arithmetic target table and performs no new target fitting, "
            "but it inherits the historically zero-fitted epsilon=0.001916. It therefore "
            "establishes or refutes finite empirical-matrix eigenbranch robustness only, not "
            "blind arithmetic validation. It does not define chronological primitive orbits, "
            "a dynamical determinant, completed-xi zeros, a quantization, or a Hilbert-Polya "
            "operator."
        ),
        "next_smallest_test": (
            "GO_WITH_LIMITATIONS opens only an autonomous slow-variable lift or transfer-cocycle "
            "determinant definition. STOP_SCOPED retires the empirical phase-level observable and "
            "retains its mode-selection/occupation-aggregation obstruction."
        ),
        "recommended_verdict": recommended_verdict,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--raw-directory", type=Path)
    arguments = parser.parse_args()
    report = build_report(MediumConfig(), arguments.raw_directory)
    payload = json.dumps(report, indent=2, sort_keys=True)
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(payload + "\n", encoding="utf-8")
    print(payload)


if __name__ == "__main__":
    main()
