#!/usr/bin/env python3
"""Exact structural prefilter for QG-0001.

QG-0001 is an infinite disjoint tower of asymmetrically decorated magnetic
metric graphs.  Component ``n`` is the exact ``1/n`` metric scaling of one
fixed lollipop-theta graph.  The script uses no prime table, zero table, or
fitted spectral data.

The audit keeps three ledgers separate:

* directed primitive graph orbits and their signed magnetic weights;
* the natural direct-sum magnetic Laplacian and its wavenumber count;
* the currently unopened global dynamical/secular determinant.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Iterator, Sequence


VERTEX_L = 0
VERTEX_R = 1
VERTEX_D = 2
VERTEX_NAMES = {VERTEX_L: "L", VERTEX_R: "R", VERTEX_D: "D"}

# Every length is represented by its coefficient of
# (1, sqrt(2), sqrt(3), sqrt(5)).
RADICANDS = (1, 2, 3, 5)
EDGE_NAMES = ("e0", "e1", "e2", "e3")
EDGE_TERMINI = (VERTEX_R, VERTEX_R, VERTEX_R, VERTEX_D)
EDGE_PHASE_UNITS = (0, 1, 2, 0)  # units of pi/3 in the L-outward orientation
PHASE_MODULUS = 6


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def bond_name(bond: int) -> str:
    edge = bond % 4
    direction = "+" if bond < 4 else "-"
    return f"{EDGE_NAMES[edge]}{direction}"


def reverse_bond(bond: int) -> int:
    return bond + 4 if bond < 4 else bond - 4


def bond_edge(bond: int) -> int:
    return bond % 4


def bond_origin(bond: int) -> int:
    if bond < 4:
        return VERTEX_L
    return EDGE_TERMINI[bond_edge(bond)]


def bond_terminal(bond: int) -> int:
    if bond < 4:
        return EDGE_TERMINI[bond_edge(bond)]
    return VERTEX_L


def bond_phase_units(bond: int) -> int:
    units = EDGE_PHASE_UNITS[bond_edge(bond)]
    return units if bond < 4 else -units


def outgoing_bonds(vertex: int) -> tuple[int, ...]:
    return tuple(bond for bond in range(8) if bond_origin(bond) == vertex)


def transition_amplitude(current: int, following: int) -> Fraction:
    """Return the exact vertex-scattering amplitude current -> following."""
    vertex = bond_terminal(current)
    if bond_origin(following) != vertex:
        return Fraction(0)
    if vertex == VERTEX_D:
        # The degree-one terminal is Dirichlet, not degree-one Kirchhoff.
        return Fraction(-1) if following == reverse_bond(current) else Fraction(0)
    degree = len(outgoing_bonds(vertex))
    return Fraction(2, degree) - int(following == reverse_bond(current))


def scattering_matrix() -> list[list[Fraction]]:
    return [
        [transition_amplitude(current, following) for current in range(8)]
        for following in range(8)
    ]


def transpose(matrix: Sequence[Sequence[Fraction]]) -> list[list[Fraction]]:
    return [list(column) for column in zip(*matrix)]


def matmul(
    left: Sequence[Sequence[Fraction]], right: Sequence[Sequence[Fraction]]
) -> list[list[Fraction]]:
    rows = len(left)
    shared = len(right)
    columns = len(right[0])
    return [
        [sum(left[row][k] * right[k][column] for k in range(shared)) for column in range(columns)]
        for row in range(rows)
    ]


def identity(size: int) -> list[list[Fraction]]:
    return [[Fraction(int(row == column)) for column in range(size)] for row in range(size)]


def based_closed_words(period: int) -> Iterator[tuple[int, ...]]:
    """Yield closed directed-bond words with a distinguished starting bond."""
    if period < 1:
        return

    def extend(prefix: tuple[int, ...]) -> Iterator[tuple[int, ...]]:
        if len(prefix) == period:
            if transition_amplitude(prefix[-1], prefix[0]):
                yield prefix
            return
        for following in outgoing_bonds(bond_terminal(prefix[-1])):
            if transition_amplitude(prefix[-1], following):
                yield from extend(prefix + (following,))

    for start in range(8):
        yield from extend((start,))


def canonical_rotation(word: Sequence[int]) -> tuple[int, ...]:
    values = tuple(word)
    return min(values[index:] + values[:index] for index in range(len(values)))


def is_primitive_word(word: Sequence[int]) -> bool:
    values = tuple(word)
    period = len(values)
    for divisor in range(1, period):
        if period % divisor == 0 and values == values[:divisor] * (period // divisor):
            return False
    return True


def primitive_orbits(max_period: int) -> dict[int, list[tuple[int, ...]]]:
    result: dict[int, list[tuple[int, ...]]] = {}
    for period in range(1, max_period + 1):
        necklaces = {canonical_rotation(word) for word in based_closed_words(period)}
        result[period] = sorted(word for word in necklaces if is_primitive_word(word))
    return result


def orbit_amplitude(word: Sequence[int]) -> Fraction:
    return math.prod(
        transition_amplitude(word[index], word[(index + 1) % len(word)])
        for index in range(len(word))
    )


def orbit_edge_counts(word: Sequence[int]) -> tuple[int, int, int, int]:
    counts = [0, 0, 0, 0]
    for bond in word:
        counts[bond_edge(bond)] += 1
    return tuple(counts)  # type: ignore[return-value]


def orbit_phase_units(word: Sequence[int]) -> int:
    return sum(bond_phase_units(bond) for bond in word) % PHASE_MODULUS


def reverse_orbit(word: Sequence[int]) -> tuple[int, ...]:
    return canonical_rotation(tuple(reverse_bond(bond) for bond in reversed(word)))


def length_text(counts: Sequence[int], component: int = 1) -> str:
    terms: list[str] = []
    for count, radicand in zip(counts, RADICANDS):
        if not count:
            continue
        radical = "1" if radicand == 1 else f"sqrt({radicand})"
        if count == 1:
            terms.append(radical)
        else:
            terms.append(f"{count}*{radical}")
    numerator = " + ".join(terms) if terms else "0"
    return numerator if component == 1 else f"({numerator})/{component}"


Monomial = tuple[tuple[int, int, int, int], int]


def trace_ledger_from_based_words(period: int) -> dict[Monomial, Fraction]:
    ledger: dict[Monomial, Fraction] = defaultdict(Fraction)
    for word in based_closed_words(period):
        key = (orbit_edge_counts(word), orbit_phase_units(word))
        ledger[key] += orbit_amplitude(word)
    return dict(ledger)


def trace_ledger_from_primitives(
    period: int, orbits: dict[int, list[tuple[int, ...]]]
) -> dict[Monomial, Fraction]:
    ledger: dict[Monomial, Fraction] = defaultdict(Fraction)
    for primitive_period, words in orbits.items():
        if primitive_period > period or period % primitive_period:
            continue
        repetition = period // primitive_period
        for word in words:
            counts = tuple(value * repetition for value in orbit_edge_counts(word))
            phase = (orbit_phase_units(word) * repetition) % PHASE_MODULUS
            coefficient = primitive_period * orbit_amplitude(word) ** repetition
            ledger[(counts, phase)] += coefficient
    return dict(ledger)


def serialized_ledger(ledger: dict[Monomial, Fraction]) -> list[dict[str, object]]:
    return [
        {
            "edge_counts": list(counts),
            "phase_units_mod_6": phase,
            "coefficient": fraction_text(coefficient),
        }
        for (counts, phase), coefficient in sorted(ledger.items())
        if coefficient
    ]


def orbit_record(word: Sequence[int]) -> dict[str, object]:
    counts = orbit_edge_counts(word)
    return {
        "word": [bond_name(bond) for bond in word],
        "topological_period": len(word),
        "edge_counts": list(counts),
        "base_metric_length": length_text(counts),
        "scattering_amplitude": fraction_text(orbit_amplitude(word)),
        "phase_units_mod_6": orbit_phase_units(word),
        "reverse_word": [bond_name(bond) for bond in reverse_orbit(word)],
        "reverse_is_same_oriented_necklace": reverse_orbit(word) == canonical_rotation(word),
    }


def riemann_von_mangoldt_main(height: float) -> float:
    scaled = height / (2 * math.pi)
    return scaled * math.log(scaled) - scaled + 7 / 8


def build_report(max_period: int = 6) -> dict[str, object]:
    if max_period != 6:
        raise ValueError("QG-0001 source lock freezes max_period=6")

    matrix = scattering_matrix()
    if matmul(transpose(matrix), matrix) != identity(8):
        raise AssertionError("the exact vertex-scattering matrix is not orthogonal")

    orbits = primitive_orbits(max_period)
    trace_checks: dict[str, object] = {}
    all_trace_ledgers: dict[str, object] = {}
    for period in range(1, max_period + 1):
        direct = trace_ledger_from_based_words(period)
        repeated = trace_ledger_from_primitives(period, orbits)
        if direct != repeated:
            raise AssertionError(f"primitive/repetition trace mismatch at period {period}")
        serialized = serialized_ledger(direct)
        trace_checks[str(period)] = {
            "identity_passed": True,
            "based_closed_words": sum(1 for _ in based_closed_words(period)),
            "primitive_orbits": len(orbits[period]),
            "nonzero_trace_monomials": len(serialized),
        }
        all_trace_ledgers[str(period)] = serialized

    primitive_records = {
        str(period): [orbit_record(word) for word in words]
        for period, words in orbits.items()
    }
    primitive_payload = json.dumps(primitive_records, sort_keys=True, separators=(",", ":"))
    trace_payload = json.dumps(all_trace_ledgers, sort_keys=True, separators=(",", ":"))

    pendant_word = (3, 7)
    pendant_amplitude = orbit_amplitude(pendant_word)
    pendant_counts = orbit_edge_counts(pendant_word)
    if pendant_amplitude != Fraction(1, 2) or pendant_counts != (0, 0, 0, 2):
        raise AssertionError("unexpected pendant-bounce witness")

    cycle_flux_units = sorted(
        {
            (EDGE_PHASE_UNITS[left] - EDGE_PHASE_UNITS[right]) % PHASE_MODULUS
            for left in range(3)
            for right in range(left + 1, 3)
        }
    )
    doubled_flux_units = sorted({(2 * value) % PHASE_MODULUS for value in cycle_flux_units})
    if 0 in doubled_flux_units:
        raise AssertionError("a frozen core flux became time-reversal invariant")

    total_length = 1 + math.sqrt(2) + math.sqrt(3) + math.sqrt(5)
    tower_coefficient = total_length / math.pi
    target_coefficient = 1 / (2 * math.pi)
    heights = (100.0, 10_000.0, 1_000_000.0)

    return {
        "candidate_id": "QG-0001",
        "clue_id": "CLUE-A4-003",
        "title": "Harmonic magnetic lollipop-theta tower",
        "target_data_used": {"prime_table": False, "zero_table": False, "fitting": False},
        "base_graph": {
            "vertices": {
                "L": {"boundary": "covariant Kirchhoff", "degree": 4},
                "R": {"boundary": "covariant Kirchhoff", "degree": 3},
                "D": {"boundary": "Dirichlet", "degree": 1},
            },
            "edges": [
                {
                    "name": EDGE_NAMES[index],
                    "endpoints": ["L", VERTEX_NAMES[EDGE_TERMINI[index]]],
                    "base_length": "1" if RADICANDS[index] == 1 else f"sqrt({RADICANDS[index]})",
                    "phase_units_pi_over_3": EDGE_PHASE_UNITS[index],
                }
                for index in range(4)
            ],
            "total_base_length": "1 + sqrt(2) + sqrt(3) + sqrt(5)",
            "total_base_length_float": total_length,
            "directed_bond_order": [bond_name(bond) for bond in range(8)],
            "scattering_matrix": [
                [fraction_text(value) for value in row] for row in matrix
            ],
            "scattering_matrix_exactly_orthogonal": True,
        },
        "tower_rule": {
            "components": "n=1,2,...",
            "metric_scaling": "ell_(n,e)=ell_e/n",
            "oriented_magnetic_line_integrals": "fixed in n",
            "operator_scaling": "H_n is unitarily equivalent to n^2*H_1",
            "orbit_scaling": "L_(p,n)=L_p/n; scattering amplitude and phase unchanged",
        },
        "source_lock_splits": {
            "training": {"topological_periods": [1, 2], "tower_labels": [1, 2, 3, 4]},
            "validation": {"topological_periods": [3, 4], "tower_labels": [5, 6, 7, 8]},
            "test": {"topological_periods": [5, 6], "tower_labels": list(range(9, 17))},
        },
        "primitive_orbit_census": primitive_records,
        "primitive_orbit_counts": {str(period): len(words) for period, words in orbits.items()},
        "primitive_ledger_sha256": hashlib.sha256(primitive_payload.encode()).hexdigest(),
        "trace_repetition_checks": trace_checks,
        "trace_ledgers": all_trace_ledgers,
        "trace_ledger_sha256": hashlib.sha256(trace_payload.encode()).hexdigest(),
        "geometric_antiunitary_audit": {
            "vertex_signatures": ["Kirchhoff-degree-4", "Kirchhoff-degree-3", "Dirichlet-degree-1"],
            "length_preserving_graph_automorphisms": 1,
            "only_graph_automorphism": "identity",
            "gauge_invariant_core_flux_units_mod_6": cycle_flux_units,
            "doubled_flux_units_mod_6": doubled_flux_units,
            "identity_gauge_equivalent_to_flux_reversal": False,
            "inherited_local_geometric_antiunitary": False,
            "abstract_spectral_basis_conjugation_exists": True,
            "abstract_conjugation_geometric_or_orbit_interpretation": False,
        },
        "operator_theorem": {
            "hilbert_space": "direct sum over n>=1 and four component edges of L2(0,ell_e/n)",
            "base_positive_gap": "PROVED by the Dirichlet terminal and continuity",
            "component_self_adjointness": "PROVED by the closed magnetic quadratic form",
            "direct_sum_self_adjointness": "PROVED on the graph-norm direct-sum domain",
            "compact_resolvent": "PROVED from H_n ~= n^2 H_1 and lambda_1(H_1)>0",
            "positive_wavenumber_count": (
                "N_QG(K)=(L0/pi)*K*log(K)+O(K), L0=1+sqrt(2)+sqrt(3)+sqrt(5)"
            ),
            "tower_leading_coefficient": tower_coefficient,
            "riemann_positive_zero_leading_coefficient": target_coefficient,
            "unfitted_leading_coefficient_ratio": tower_coefficient / target_coefficient,
            "counting_order_matches_T_log_T": True,
            "leading_coefficient_matches_without_rescaling": False,
        },
        "counting_diagnostics": [
            {
                "height": height,
                "tower_main_term": tower_coefficient * height * math.log(height),
                "riemann_von_mangoldt_main": riemann_von_mangoldt_main(height),
                "tower_main_over_T_log_T": tower_coefficient,
            }
            for height in heights
        ],
        "naive_determinant_obstruction": {
            "witness_primitive_word": [bond_name(bond) for bond in pendant_word],
            "witness_scattering_weight": fraction_text(pendant_amplitude),
            "witness_component_length": f"{length_text(pendant_counts)}/n",
            "subproduct": "product_(n>=1) [1-(1/2)*exp(-2*sqrt(5)*s/n)]",
            "factor_limit_as_n_to_infinity": "1/2",
            "ordinary_nonzero_euler_product_exists": False,
            "component_bond_block": "B_n(s)=S*diag_b(exp(-s*ell_b/n+i*alpha_b))",
            "component_bond_trace_norm_limit": 8,
            "direct_sum_bond_block_compact": False,
            "direct_sum_bond_block_trace_class": False,
            "standard_direct_sum_fredholm_determinant_exists": False,
            "reopening_requirement": "an explicit regularized same-object determinant and trace counterterm ledger",
        },
        "spectral_zeta_data_type_warning": {
            "identity_domain": "Re(z)>1/2",
            "identity": "zeta_H(z)=zeta(2*z)*zeta_H1(z)",
            "meaning": "heat/spectral zeta in the exponent variable z",
            "not_meaning": "a secular characteristic divisor in wavenumber K",
            "cross_ledger_promotion_forbidden": True,
        },
        "determinant_convention": "NOT_OPENED",
        "route_b_invoked": False,
        "structural_conclusion": (
            "The target-free harmonic graph tower escapes the finite-graph O(T) count and has a natural "
            "compact-resolvent magnetic Laplacian with T*log(T) wavenumber growth. Its primitive metric "
            "periods accumulate at zero, however, and an explicit pendant-bounce subproduct proves that "
            "the ordinary infinite orbit/Fredholm determinant is not defined. The heat/spectral-zeta "
            "factor zeta(2*z) is a different data type and cannot be promoted to a secular xi divisor."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-period", type=int, default=6)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    arguments = parser.parse_args()
    report = build_report(arguments.max_period)
    payload = json.dumps(report, indent=2, sort_keys=True)
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(payload + "\n", encoding="utf-8")
    if not arguments.quiet:
        print(payload)


if __name__ == "__main__":
    main()
