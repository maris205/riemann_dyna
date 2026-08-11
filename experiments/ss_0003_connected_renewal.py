#!/usr/bin/env python3
"""Target-free Route-A prefilter for a connected countable renewal graph.

The graph has one hub h and one spoke v_n for every integer n>=2, with edges
in both directions.  Each edge of the n-excursion carries half the roof
log(n).  The first-return grammar is the full countable shift on integer
labels, while the edge realization is a finite-rank holomorphic transfer
family on Re(s)>1.  The exact Fredholm determinant is derived from the graph:

    det(I-L_s) = 1 - sum_{n>=2} n**(-s) = 2 - zeta(s).

No prime/zero table, numerical root search, or spectral computation is used.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
from typing import Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
SOURCE_LOCK = "configs/source_locks/SS-0003-CONNECTED-RENEWAL.yaml"
ARTIFACT = "artifacts/ss_0003/connected_renewal_audit.json"
GENERATOR = "experiments/ss_0003_connected_renewal.py"
FORMAL_RESULT = "formal/results/ss_0003_connected_renewal.md"
OBSTRUCTION = "formal/obstructions/positive_renewal_right_half_plane_zero.md"
LITERATURE = "docs/literature/ss_0003_a_points_sources.md"
AUDIT_ID = "SS-0003-CONNECTED-RENEWAL-001"
CANDIDATE_ID = "SS-0003"
CLUE_ID = "CLUE-A4-002"


def rotations(word: Sequence[int]) -> list[tuple[int, ...]]:
    values = tuple(word)
    return [values[i:] + values[:i] for i in range(len(values))]


def canonical_rotation(word: Sequence[int]) -> tuple[int, ...]:
    return min(rotations(word))


def is_primitive_word(word: Sequence[int]) -> bool:
    values = tuple(word)
    length = len(values)
    for divisor in range(1, length):
        if length % divisor == 0 and values == values[:divisor] * (length // divisor):
            return False
    return True


def primitive_necklaces(labels: Iterable[int], word_length: int) -> list[tuple[int, ...]]:
    if word_length < 1:
        raise ValueError("word_length must be positive")
    result: set[tuple[int, ...]] = set()
    label_tuple = tuple(labels)
    for word in itertools.product(label_tuple, repeat=word_length):
        if is_primitive_word(word) and canonical_rotation(word) == tuple(word):
            result.add(tuple(word))
    return sorted(result)


def cycle_ledger(label_max: int = 6, word_length_max: int = 4) -> list[dict[str, object]]:
    if label_max < 2:
        raise ValueError("label_max must be at least 2")
    rows: list[dict[str, object]] = []
    labels = range(2, label_max + 1)
    for length in range(1, word_length_max + 1):
        for word in primitive_necklaces(labels, length):
            product = 1
            for label in word:
                product *= label
            rows.append(
                {
                    "word": list(word),
                    "excursion_length": length,
                    "edge_period": 2 * length,
                    "roof": " + ".join(f"log({label})" for label in word),
                    "action_product": product,
                    "weight": f"{product}^(-s)",
                    "primitive": True,
                    "repeat_rule": f"r -> {product}^(-r*s)",
                }
            )
    return rows


def trace_ledger(edge_power_max: int = 8) -> list[dict[str, object]]:
    if edge_power_max < 2:
        raise ValueError("edge_power_max must be at least 2")
    rows: list[dict[str, object]] = []
    for edge_power in range(1, edge_power_max + 1):
        if edge_power % 2:
            rows.append(
                {
                    "edge_power": edge_power,
                    "trace": "0",
                    "reason": "bipartite hub-spoke graph has no odd closed walks",
                }
            )
        else:
            k = edge_power // 2
            rows.append(
                {
                    "edge_power": edge_power,
                    "trace": f"2*(sum_(n>=2) n^(-s))^{k}",
                    "reason": "two edge-start sectors and k renewal excursions",
                }
            )
    return rows


def build_report(label_max: int = 10, word_length_max: int = 4) -> dict[str, object]:
    if label_max < 2 or word_length_max < 1:
        raise ValueError("invalid audit cutoff")
    lock_path = ROOT / SOURCE_LOCK
    generator_path = ROOT / GENERATOR
    return {
        "audit_id": AUDIT_ID,
        "candidate_id": CANDIDATE_ID,
        "formal_candidate": True,
        "clue_id": CLUE_ID,
        "source_lock": SOURCE_LOCK,
        "source_lock_sha256": hashlib.sha256(lock_path.read_bytes()).hexdigest(),
        "generator": GENERATOR,
        "generator_sha256": hashlib.sha256(generator_path.read_bytes()).hexdigest(),
        "formal_result": FORMAL_RESULT,
        "obstruction": OBSTRUCTION,
        "literature": LITERATURE,
        "uses_prime_table": False,
        "uses_zero_table": False,
        "phase_space": "V={h} union {v_n:n>=2}; edges h<->v_n",
        "induced_renewal": "full countable shift on labels n>=2 at the hub",
        "edge_period": 2,
        "strong_connectivity": True,
        "roof": "tau(h,v_n)=tau(v_n,h)=0.5*log(n); excursion roof log(n)",
        "potential": "phi=0",
        "hilbert_space": "C direct_sum ell^2({2,3,...})",
        "operator": "L_s(c,x)=(sum_n n^(-s/2)x_n, c*(n^(-s/2))_n), Re(s)>1",
        "operator_pairing": "holomorphic bilinear coordinate functional",
        "operator_domain": "Re(s)>1",
        "trace_class": {
            "rank_bound": 2,
            "trace_norm_bound": "||L_s||_1 = 2*(sum_(n>=2)n^(-Re(s)))^(1/2)",
            "holomorphic_on_domain": True,
        },
        "determinant_ledger": {
            "frozen": "D_renew(s)=det_Fr(I-L_s), Re(s)>1",
            "exact_identity": "1-sum_(n>=2)n^(-s)=2-zeta(s)",
            "nonzero_eigenvalue_equation": "lambda^2=sum_(n>=2)n^(-s)",
            "cycle_log_domain": "abs(sum_(n>=2)n^(-s))<1",
            "scalar_continuation": "2-zeta(s) on C\\{1}, not a Fredholm continuation",
        },
        "primitive_repetition_ledger": cycle_ledger(label_max, word_length_max),
        "trace_power_ledger": trace_ledger(8),
        "non_lattice_certificate": {
            "periods_checked": ["log(2)", "log(3)"],
            "ratio_is_irrational": True,
            "proof": "log(2)/log(3)=a/b would imply 2^b=3^a by unique factorization",
            "edge_flow_caveat": "edge shift has period two; no mixing claim is made for the discrete edge clock",
        },
        "divisor_regime": {
            "scalar_zero_equation": "zeta(s)=2",
            "no_zero_for_Re_ge_2": "|zeta(s)-1| <= zeta(2)-1 < 1",
            "fixed_strip": "0<Re(s)<2",
            "counting_theorem": "N_2(T)=T/(2*pi)*log(T/(2*pi*e))+O(log(T))",
            "asymptotic_regime": "Theta(T log T)",
            "source": LITERATURE,
            "root_search_used": False,
        },
        "right_half_plane_obstruction": {
            "statement": "There is a unique real sigma_star in (1,2) with sum_(n>=2)n^(-sigma_star)=1",
            "proof": "strict decrease, divergence at 1+, and sum_(n>=2)n^(-2)<3/4",
            "extra_zero": "D_renew(sigma_star)=0",
            "target_conflict": "completed xi is zero-free for Re(s)>1",
        },
        "route_effect": {
            "analytic_tuple": ["A1_WEAK", "A2_ANALYTIC_DETERMINANT", "A3_FAIL", "A4_FAIL"],
            "riemann_target_tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall_verdict": "ROUTE_A_REJECTED",
            "scoped_verdict": "STOP_SCOPED",
            "obstruction": "OBR-017",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "established": [
                "connected countable renewal graph and exact cyclic-word ledger",
                "rank-two holomorphic trace-class Fredholm family on Re(s)>1",
                "same-object determinant identity 2-zeta(s)",
                "fixed-strip Theta(T log T) a-point divisor order by classical theorem",
                "unique extra real zero in (1,2) without root search",
            ],
            "not_established": [
                "prime correspondence or von-Mangoldt weights",
                "Fredholm continuation of the same operator into Re(s)<=1",
                "functional equation, Gamma/trivial-zero ledger, or completed-xi equality",
                "natural quantization, Route B, Hilbert-Polya, or RH",
            ],
        },
        "next_smallest_test": (
            "Park SS-0003 under OBR-017. Reopen only with a new source-locked "
            "connected grammar whose signed/complex weights remove the positive "
            "right-half-plane obstruction without post-hoc target data."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--label-max", type=int, default=10)
    parser.add_argument("--word-length-max", type=int, default=4)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = build_report(args.label_max, args.word_length_max)
    payload = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")
    print(payload)


if __name__ == "__main__":
    main()
