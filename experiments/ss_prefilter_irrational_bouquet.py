#!/usr/bin/env python3
"""Route-A prefilter for a countable irrational-roof cycle bouquet.

This is deliberately a non-candidate structural control for CLUE-A4-002.
The phase space is a countable disjoint union of cyclic components.  The
block-diagonal transfer family is trace class for every complex ``s`` and its
Fredholm determinant has an explicit product and divisor.  The audit checks
the primitive/repetition ledger and proves the fixed-strip divisor count is
linear in height.  It never searches numerical roots or reads target tables.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
SOURCE_LOCK = "configs/source_locks/SS-PREFILTER-IRRATIONAL-BOUQUET.yaml"
ARTIFACT = "artifacts/ss_prefilter_irrational_bouquet/audit.json"
GENERATOR = "experiments/ss_prefilter_irrational_bouquet.py"
FORMAL_RESULT = "formal/results/ss_prefilter_irrational_bouquet.md"
OBSTRUCTION = "formal/obstructions/countable_irrational_bouquet_linear_divisor.md"
AUDIT_ID = "SS-PREFILTER-IRRATIONAL-BOUQUET-001"
CLUE_ID = "CLUE-A4-002"
N_MIN = 2

# A certified rational enclosure.  The endpoints are checked against x^2=2
# in ``build_report``; no floating approximation is used for the theorem.
SQRT2_LO = Fraction(1414213562373095, 10**15)
SQRT2_HI = Fraction(1414213562373096, 10**15)


def _fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def cycle_length(n: int) -> str:
    return f"{n}+sqrt(2)"


def primitive_orbit_ledger(n_max: int) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for n in range(N_MIN, n_max + 1):
        rows.append(
            {
                "label": n,
                "states": n,
                "primitive_period": n,
                "primitive_roof": cycle_length(n),
                "primitive_action": f"{n}^2",
                "primitive_weight": f"exp(-{n}^2)",
                "repeat_rule": "r -> exp(-r*n^2-s*r*(n+sqrt(2)))",
            }
        )
    return rows


def divisors_in_range(number: int) -> list[int]:
    return [candidate for candidate in range(1, number + 1) if number % candidate == 0]


def trace_power_terms(power: int) -> list[dict[str, object]]:
    """Return the exact symbolic terms in tr(L_s**power)."""
    terms: list[dict[str, object]] = []
    for n in range(N_MIN, power + 1):
        if power % n:
            continue
        repetition = power // n
        terms.append(
            {
                "label": n,
                "block_trace_multiplicity": n,
                "repetition": repetition,
                "term": f"{n}*exp(-{power}*{n}-s*{power}*(1+sqrt(2)/{n}))",
            }
        )
    return terms


def alpha_interval(n: int) -> tuple[Fraction, Fraction]:
    """Certified interval for alpha_n=-n^2/(n+sqrt(2))."""
    lower = -Fraction(n * n, 1) / (n + SQRT2_LO)
    upper = -Fraction(n * n, 1) / (n + SQRT2_HI)
    if lower > upper:
        raise AssertionError("sqrt(2) enclosure produced an inverted interval")
    return lower, upper


def strip_indices(left: int, right: int, n_limit: int = 10000) -> list[int]:
    """Return n whose exact real zero line meets [left,right]."""
    if left > right:
        raise ValueError("strip endpoints must be ordered")
    indices: list[int] = []
    for n in range(N_MIN, n_limit + 1):
        alpha_low, alpha_high = alpha_interval(n)
        if alpha_high < left:
            # alpha_n is strictly decreasing; all later labels are outside.
            break
        if alpha_low > right:
            continue
        if alpha_low >= left and alpha_high <= right:
            indices.append(n)
            continue
        raise AssertionError(
            f"sqrt(2) bracket does not decide strip membership for n={n}: "
            f"[{alpha_low},{alpha_high}] vs [{left},{right}]"
        )
    else:
        raise AssertionError("strip search hit n_limit before leaving the strip")
    return indices


def diagnostic_zero_counts(indices: Iterable[int], heights: Iterable[float]) -> list[dict[str, object]]:
    labels = list(indices)
    rows: list[dict[str, object]] = []
    for height in heights:
        positive = sum(
            math.floor(height * (n + math.sqrt(2)) / (2.0 * math.pi))
            for n in labels
        )
        symmetric = 2 * positive + len(labels)
        rows.append(
            {
                "height": height,
                "positive_height_count": positive,
                "symmetric_count": symmetric,
                "symmetric_over_T_log_T": symmetric / (height * math.log(height)),
            }
        )
    return rows


def build_report(n_max: int = 12) -> dict[str, object]:
    if n_max < N_MIN:
        raise ValueError("n_max must be at least 2")
    if not (SQRT2_LO * SQRT2_LO < 2 < SQRT2_HI * SQRT2_HI):
        raise AssertionError("invalid certified sqrt(2) bracket")

    lock_path = ROOT / SOURCE_LOCK
    lock_hash = hashlib.sha256(lock_path.read_bytes()).hexdigest()
    generator_hash = hashlib.sha256((ROOT / GENERATOR).read_bytes()).hexdigest()
    ledger = primitive_orbit_ledger(n_max)
    test_powers = {str(power): trace_power_terms(power) for power in range(1, 13)}
    strips = {
        "critical_half_plane_0_1": strip_indices(0, 1),
        "moderate_strip_minus10_1": strip_indices(-10, 1),
        "deep_strip_minus100_minus1": strip_indices(-100, -1),
    }
    moderate_indices = strips["moderate_strip_minus10_1"]

    return {
        "audit_id": AUDIT_ID,
        "formal_candidate": False,
        "candidate_id": None,
        "clue_id": CLUE_ID,
        "source_lock": SOURCE_LOCK,
        "source_lock_sha256": lock_hash,
        "generator": GENERATOR,
        "generator_sha256": generator_hash,
        "formal_result": FORMAL_RESULT,
        "obstruction": OBSTRUCTION,
        "uses_prime_table": False,
        "uses_zero_table": False,
        "phase_space": "disjoint_union_{n>=2} Z/nZ",
        "map": "sigma(n,j)=(n,j+1 mod n)",
        "roof": "tau_n=1+sqrt(2)/n; L_n=n+sqrt(2)",
        "potential": "phi_n=-n per base step; A_n=n^2 per primitive cycle",
        "transfer_operator": "(L_s f)(n,j)=exp(-n-s*tau_n) f(n,j-1 mod n)",
        "hilbert_space": "ell^2(Sigma) with counting measure",
        "determinant_ledger": {
            "frozen": "D_bouquet(s)=det_Fr(I-L_s)",
            "factorization": "product_{n>=2}(1-exp(-n^2-s*(n+sqrt(2))))",
            "entire_trace_class_family": True,
            "local_trace_norm_bound": "||L_s||_1 <= exp(2*M)*sum_{n>=2} n*exp(-n) for |Re(s)|<=M",
            "trace_power_formula": "tr(L_s^k)=sum_{n|k,n>=2} n*exp(-k*n-s*k*(1+sqrt(2)/n))",
        },
        "primitive_orbit_ledger": ledger,
        "trace_power_terms_1_to_12": test_powers,
        "non_lattice_certificate": {
            "periods_checked": ["2+sqrt(2)", "3+sqrt(2)"],
            "ratio": "(4+sqrt(2))/7",
            "ratio_is_irrational": True,
            "caveat": "The base is disconnected; global incommensurability does not imply mixing.",
        },
        "closed_form_divisor": {
            "zeros": "s_{n,k}=(-n^2-2*pi*i*k)/(n+sqrt(2)), n>=2, k in Z",
            "real_part": "alpha_n=-n^2/(n+sqrt(2))",
            "real_part_strictly_decreasing": True,
            "real_part_limit": "-infinity",
            "fixed_strip_count": "N_[a,b](T)=sum_{n: a<=alpha_n<=b}(2*floor(T*(n+sqrt(2))/(2*pi))+1)=O(T)",
            "target_divisor_regime": "completed-xi has Theta(T log T) in fixed critical strips",
        },
        "strip_indices": strips,
        "divisor_count_diagnostics": diagnostic_zero_counts(moderate_indices, [100.0, 1000.0, 10000.0]),
        "route_effect": {
            "analytic_tuple": ["A1_WEAK", "A2_ANALYTIC_DETERMINANT", "A3_PARTIAL_ANALYTIC_STRUCTURE", "A4_FAIL"],
            "riemann_target_tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "verdict": "STOP_SCOPED",
            "obstruction": "OBR-016",
            "route_b_invocation_allowed": False,
        },
        "structural_conclusion": (
            "The object is an explicit target-free countable, globally incommensurate suspension "
            "with an entire trace-class Fredholm determinant, but its divisor has only O(T) zeros "
            "in every bounded vertical strip. The disconnected bouquet and superexponentially "
            "escaping cycle actions provide no arithmetic orbit law; this is a reusable negative "
            "structural prior, not a formal SS-0003 candidate."
        ),
        "claim_boundary": {
            "established": [
                "exact primitive/repetition ledger",
                "entire trace-class family and same-object determinant",
                "closed-form zero divisor",
                "linear fixed-strip divisor-count obstruction",
            ],
            "not_established": [
                "prime correspondence or von-Mangoldt weights",
                "connected/mixing symbolic dynamics",
                "completed-xi equality, spectrum, Route B, or RH",
            ],
        },
        "next_smallest_test": (
            "Pivot again within CLUE-A4-002 only after defining a connected or renewal object "
            "whose cycle actions do not escape every fixed strip; do not promote this bouquet."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=12)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    report = build_report(arguments.n_max)
    payload = json.dumps(report, indent=2, sort_keys=True)
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(payload + "\n", encoding="utf-8")
    print(payload)


if __name__ == "__main__":
    main()
