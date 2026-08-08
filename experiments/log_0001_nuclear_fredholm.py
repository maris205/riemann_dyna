#!/usr/bin/env python3
"""Target-free regression ledger for the frozen exact-U_c polar branches.

This program is deliberately not a Fredholm-determinant evaluation.  It
checks the finite based-word identities needed before such a theorem may be
invoked: contraction, cyclic fixed-point transport, signed inverse-Jacobian
denominators, and the exceptional pure-L boundary orbit.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
from typing import Any

import mpmath as mp

try:
    from experiments import p4_logistic_uc_first_return_support as support
    from experiments import p4_logistic_uc_polar_complex_branch as branches
except ModuleNotFoundError:  # Direct execution from the repository root.
    import p4_logistic_uc_first_return_support as support
    import p4_logistic_uc_polar_complex_branch as branches


AUDIT_ID = "LOG-0001-NUCLEAR-FREDHOLM-REGRESSION"
SOURCE_LOCK = "configs/source_locks/LOG-0001-NUCLEAR-FREDHOLM.yaml"
PARENT_LOCK = "configs/source_locks/P4-LOGISTIC-UC-POLAR-COMPLEX-BRANCH.yaml"
FORMAL_RESULT = "formal/results/log_0001_nuclear_fredholm.md"
GENERATOR = "experiments/log_0001_nuclear_fredholm.py"
ARTIFACT = (
    "artifacts/log_0001_nuclear_fredholm/"
    "nuclear_fredholm_certificate.json"
)
MAX_WORD_LENGTH = 8
DIAGNOSTIC_DIGITS = 100
CONTRACTION_UPPER_TEXT = branches.COMPLEX_CONTRACTION_SAFE_UPPER
REPRODUCTION_COMMAND = (
    "python3 experiments/log_0001_nuclear_fredholm.py --quiet --output "
    "artifacts/log_0001_nuclear_fredholm/nuclear_fredholm_certificate.json"
)


def file_sha256(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def parameters() -> tuple[mp.mpf, mp.mpf]:
    """Refine U_c inside the sealed 100-digit bracket for diagnostics."""
    lower = mp.mpf(support.U_LOWER_TEXT)
    upper = mp.mpf(support.U_UPPER_TEXT)
    midpoint = (lower + upper) / 2
    u = mp.findroot(lambda value: value**3 - 2 * value**2 + 2 * value - 2, midpoint)
    if not lower < u < upper:
        raise RuntimeError("refined U_c escaped the sealed bracket")
    return u, u - 1


def nonnegative_real(value: mp.mpf | mp.mpc, label: str) -> mp.mpf:
    """Remove only roundoff-sized endpoint imaginary/negative parts."""
    tolerance = mp.mpf("1e-85")
    if abs(mp.im(value)) >= tolerance:
        raise RuntimeError(f"{label} has a non-real value: {value}")
    real_value = mp.re(value)
    if real_value < 0:
        if abs(real_value) >= tolerance:
            raise RuntimeError(f"{label} is negative: {real_value}")
        return mp.mpf("0")
    return real_value


def inverse_magnitude(target: mp.mpf, u: mp.mpf, rho: mp.mpf) -> mp.mpf:
    t = mp.sqrt(nonnegative_real((1 + rho * mp.sin(target)) / u, "t^2"))
    return mp.sqrt((1 + t) * (rho + t)) / (4 * t)


def phi(letter: str, target: mp.mpf, u: mp.mpf, rho: mp.mpf) -> mp.mpf:
    """The sealed real composite inverse branches, with their fixed signs."""
    t = mp.sqrt(nonnegative_real((1 + rho * mp.sin(target)) / u, "t^2"))
    angle_square = nonnegative_real((1 - t) / (u * rho**2), "angle square")
    angle = mp.asin(mp.sqrt(angle_square))
    if letter == "L":
        return -angle
    if letter == "R":
        return angle
    raise ValueError(f"unknown branch {letter!r}")


def compose(word: str, target: mp.mpf, u: mp.mpf, rho: mp.mpf) -> mp.mpf:
    """phi_word=phi_w0 o ... o phi_w(n-1)."""
    value = target
    for letter in reversed(word):
        value = phi(letter, value, u, rho)
    return value


def fixed_point(word: str, u: mp.mpf, rho: mp.mpf) -> tuple[mp.mpf, int]:
    """Contraction iteration for the unique fixed point of a based word."""
    value = mp.mpf("0")
    for iteration in range(1, 1001):
        next_value = compose(word, value, u, rho)
        if abs(next_value - value) < mp.mpf("1e-90"):
            return next_value, iteration
        value = next_value
    raise RuntimeError(f"fixed-point iteration did not converge for {word}")


def word_ledger(
    word: str,
    u: mp.mpf,
    rho: mp.mpf,
    contraction_upper: mp.mpf,
) -> dict[str, Any]:
    point, iterations = fixed_point(word, u, rho)
    value = point
    derivative = mp.mpf("1")
    roof = mp.mpf("0")
    itinerary_signs_are_strict = True
    for letter in reversed(word):
        magnitude = inverse_magnitude(value, u, rho)
        derivative *= magnitude if letter == "L" else -magnitude
        roof -= mp.log(magnitude)
        value = phi(letter, value, u, rho)
        itinerary_signs_are_strict &= (value < 0) if letter == "L" else (value > 0)

    residual = abs(compose(word, point, u, rho) - point)
    sign = 1 if word.count("R") % 2 == 0 else -1
    expected_abs_derivative = mp.exp(-roof)
    expected_denominator = 1 - sign * expected_abs_derivative
    return {
        "word": word,
        "length": len(word),
        "fixed_point": mp.nstr(point, 70),
        "fixed_point_iterations": iterations,
        "fixed_point_residual": mp.nstr(residual, 8),
        "inverse_roof": mp.nstr(roof, 70),
        "inverse_derivative": mp.nstr(derivative, 70),
        "orientation_sign": sign,
        "signed_denominator": mp.nstr(1 - derivative, 70),
        "expected_signed_denominator": mp.nstr(expected_denominator, 70),
        "contraction_upper": mp.nstr(contraction_upper ** len(word), 50),
        "gates": {
            "fixed_point_residual_below_1e_80": residual < mp.mpf("1e-80"),
            "inverse_iterates_have_strict_branch_signs": itinerary_signs_are_strict,
            "derivative_sign_matches_R_parity": (derivative > 0) == (sign > 0),
            "absolute_derivative_is_strictly_contracting": abs(derivative) < 1,
            "absolute_derivative_below_frozen_bound": (
                abs(derivative) < contraction_upper ** len(word)
            ),
            "signed_denominator_matches_orientation_ledger": (
                abs((1 - derivative) - expected_denominator) < mp.mpf("1e-80")
            ),
        },
    }


def rotations(word: str) -> list[str]:
    return [word[index:] + word[:index] for index in range(len(word))]


def rotation_gate(word: str, records: dict[str, dict[str, Any]]) -> bool:
    baseline = records[word]
    baseline_roof = mp.mpf(baseline["inverse_roof"])
    baseline_derivative = mp.mpf(baseline["inverse_derivative"])
    for rotated in rotations(word):
        candidate = records[rotated]
        if abs(mp.mpf(candidate["inverse_roof"]) - baseline_roof) >= mp.mpf("1e-65"):
            return False
        if abs(mp.mpf(candidate["inverse_derivative"]) - baseline_derivative) >= mp.mpf("1e-65"):
            return False
    return True


def build_report() -> dict[str, Any]:
    mp.mp.dps = DIAGNOSTIC_DIGITS
    u, rho = parameters()
    contraction_upper = mp.mpf(CONTRACTION_UPPER_TEXT)
    all_records: dict[str, dict[str, Any]] = {}
    by_length: dict[str, dict[str, Any]] = {}

    for length in range(1, MAX_WORD_LENGTH + 1):
        words = ["".join(bits) for bits in itertools.product("LR", repeat=length)]
        records = {
            word: word_ledger(word, u, rho, contraction_upper) for word in words
        }
        all_records.update(records)
        rotation_ok = {word: rotation_gate(word, records) for word in words}
        for word, passed in rotation_ok.items():
            records[word]["gates"]["all_cyclic_rotations_preserve_roof_and_signed_derivative"] = passed
        by_length[str(length)] = {
            "based_word_count": len(words),
            "all_word_gates_passed": all(
                all(record["gates"].values()) for record in records.values()
            ),
            "records": [records[word] for word in words],
        }

    boundary = -mp.pi / 2
    a_boundary = u**2 / 4
    pure_l: dict[str, Any] = {}
    for length in range(1, MAX_WORD_LENGTH + 1):
        word = "L" * length
        record = all_records[word]
        pure_l[str(length)] = {
            "word": word,
            "fixed_point_is_P": abs(mp.mpf(record["fixed_point"]) - boundary) < mp.mpf("1e-65"),
            "inverse_derivative_is_a_P_to_n": (
                abs(mp.mpf(record["inverse_derivative"]) - a_boundary**length)
                < mp.mpf("1e-65")
            ),
            "trace_term": f"a_P^({length}*s)/(1-a_P^{length})",
            "a_P": "U_c^2/4",
        }

    computed_gates = {
        "all_based_words_lengths_1_through_8_enumerated": (
            sum(item["based_word_count"] for item in by_length.values())
            == sum(2**length for length in range(1, MAX_WORD_LENGTH + 1))
        ),
        "every_word_passes_fixed_point_orientation_and_contraction_gates": all(
            item["all_word_gates_passed"] for item in by_length.values()
        ),
        "pure_L_boundary_orbit_matches_exact_ledger_through_length_8": all(
            item["fixed_point_is_P"] and item["inverse_derivative_is_a_P_to_n"]
            for item in pure_l.values()
        ),
    }
    return {
        "artifact_schema_version": 1,
        "audit_id": AUDIT_ID,
        "candidate_id": "LOG-0001",
        "formal_candidate": True,
        "status": "TARGET_FREE_IMPLEMENTATION_REGRESSION_PASSED",
        "scope": {
            "established": [
                "target-free finite based-word regression through length 8",
                "signed inverse-Jacobian denominator convention",
                "pure-L boundary local trace term convention",
            ],
            "not_established_by_this_finite_regression": [
                "the companion analytic nuclearity and Fredholm theorem",
                "Fredholm or Riemann zero computation",
                "the companion global all-word trace theorem or quantization",
            ],
            "companion_theorem": FORMAL_RESULT,
        },
        "frozen_inputs": {
            "map": "G=q^(-1) o (-f^2) o q",
            "branches": "phi_L'=+a, phi_R'=-a",
            "a_P": "U_c^2/4",
            "complex_contraction_upper": CONTRACTION_UPPER_TEXT,
            "max_word_length": MAX_WORD_LENGTH,
            "diagnostic_precision_digits": DIAGNOSTIC_DIGITS,
        },
        "trace_convention": {
            "word_term": "exp(-s*T_word)/(1-epsilon_word*exp(-T_word))",
            "epsilon_word": "(-1)^(number of R letters)",
            "pure_L_boundary_term": "a_P^(n*s)/(1-a_P^n)",
            "multiplicity": (
                "distinct rotations are retained when distinct; a least-period-d "
                "orbit repeated to n=r*d contributes d based points and the "
                "determinant-log factor 1/n supplies repetition coefficient 1/r"
            ),
        },
        "computed_gates": computed_gates,
        "computed_gates_passed": all(computed_gates.values()),
        "by_length": by_length,
        "pure_L_boundary_ledger": pure_l,
        "provenance": {
            "generator": GENERATOR,
            "generator_sha256": file_sha256(GENERATOR),
            "source_inputs_sha256": {
                SOURCE_LOCK: file_sha256(SOURCE_LOCK),
                PARENT_LOCK: file_sha256(PARENT_LOCK),
                FORMAL_RESULT: file_sha256(FORMAL_RESULT),
                "experiments/p4_logistic_uc_first_return_support.py": file_sha256("experiments/p4_logistic_uc_first_return_support.py"),
                "experiments/p4_logistic_uc_polar_complex_branch.py": file_sha256("experiments/p4_logistic_uc_polar_complex_branch.py"),
            },
            "external_target_data_used": False,
            "reproduction_command": REPRODUCTION_COMMAND,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default=ARTIFACT)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()
    report = build_report()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if not args.quiet:
        print(json.dumps(report, indent=2, sort_keys=True))
    if not report["computed_gates_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
