#!/usr/bin/env python3
"""Exact short-orbit Route-A prefilter for TH-0001.

The candidate is the target-free autonomous superstep

    G = F_(5/2) o F_(3/2) o F_(1/2),
    F_a(q,p) = (1-a*q^2-p, q).

No prime, zero, zeta, xi, GUE, USTC, or legacy fitted data is read.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

import sympy as sp


CANDIDATE_ID = "TH-0001"
CLUE_ID = "CLUE-A4-001"
PARAMETERS = (sp.Rational(1, 2), sp.Rational(3, 2), sp.Rational(5, 2))
Q, P = sp.symbols("q p")
ROOT_EPSILON = sp.Rational(1, 10) ** 28


def henon_step(q: object, p: object, parameter: object) -> tuple[object, object]:
    return 1 - parameter * q * q - p, q


def inverse_henon_step(q: object, p: object, parameter: object) -> tuple[object, object]:
    return p, 1 - parameter * p * p - q


def superstep(q: object, p: object) -> tuple[object, object]:
    for parameter in PARAMETERS:
        q, p = henon_step(q, p, parameter)
    return q, p


def inverse_superstep(q: object, p: object) -> tuple[object, object]:
    for parameter in reversed(PARAMETERS):
        q, p = inverse_henon_step(q, p, parameter)
    return q, p


def symbolic_superstep(q: sp.Expr, p: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
    q_out, p_out = q, p
    for parameter in PARAMETERS:
        q_out, p_out = henon_step(q_out, p_out, parameter)
        q_out, p_out = sp.expand(q_out), sp.expand(p_out)
    return q_out, p_out


def symbolic_iterate(period: int) -> tuple[sp.Expr, sp.Expr]:
    q_out, p_out = Q, P
    for _ in range(period):
        q_out, p_out = symbolic_superstep(q_out, p_out)
    return sp.expand(q_out), sp.expand(p_out)


def primitive_integer_polynomial(expression: sp.Expr) -> sp.Poly:
    polynomial = sp.Poly(expression, Q, domain=sp.QQ)
    _, polynomial = polynomial.clear_denoms(convert=True)
    _, polynomial = polynomial.primitive()
    if polynomial.LC() < 0:
        polynomial = -polynomial
    return polynomial


def polynomial_hash(polynomial: sp.Poly) -> str:
    payload = ",".join(str(coefficient) for coefficient in polynomial.all_coeffs())
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def p_expression_from_basis(basis: sp.GroebnerBasis) -> sp.Expr:
    first = basis.polys[0].as_expr()
    coefficient = sp.Poly(first, P).coeff_monomial(P)
    remainder = first.subs(P, 0)
    return sp.cancel(-remainder / coefficient)


@lru_cache(maxsize=1)
def elimination_data() -> dict[str, object]:
    q1, p1 = symbolic_iterate(1)
    basis1 = sp.groebner([q1 - Q, p1 - P], P, Q, order="lex", domain=sp.QQ)
    r1 = primitive_integer_polynomial(basis1.polys[-1].as_expr())

    q2, p2 = symbolic_iterate(2)
    basis2 = sp.groebner([q2 - Q, p2 - P], P, Q, order="lex", domain=sp.QQ)
    r2 = primitive_integer_polynomial(basis2.polys[-1].as_expr())
    quotient, remainder = r2.div(r1)
    if not remainder.is_zero:
        raise ArithmeticError("period-one eliminant does not divide period-two eliminant")
    d2 = primitive_integer_polynomial(quotient.as_expr())

    return {
        "basis1": basis1,
        "basis2": basis2,
        "r1": r1,
        "r2": r2,
        "d2": d2,
        "p1": p_expression_from_basis(basis1),
        "p2": p_expression_from_basis(basis2),
    }


def as_fraction(value: object) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, sp.Rational):
        return Fraction(int(value.p), int(value.q))
    return Fraction(value)


@dataclass(frozen=True)
class RationalInterval:
    lower: Fraction
    upper: Fraction

    def __init__(self, lower: object, upper: object | None = None):
        lo = as_fraction(lower)
        hi = lo if upper is None else as_fraction(upper)
        if lo > hi:
            raise ValueError((lo, hi))
        object.__setattr__(self, "lower", lo)
        object.__setattr__(self, "upper", hi)

    def __add__(self, other: object) -> "RationalInterval":
        rhs = other if isinstance(other, RationalInterval) else RationalInterval(other)
        return RationalInterval(self.lower + rhs.lower, self.upper + rhs.upper)

    __radd__ = __add__

    def __neg__(self) -> "RationalInterval":
        return RationalInterval(-self.upper, -self.lower)

    def __sub__(self, other: object) -> "RationalInterval":
        rhs = other if isinstance(other, RationalInterval) else RationalInterval(other)
        return self + (-rhs)

    def __rsub__(self, other: object) -> "RationalInterval":
        return RationalInterval(other) - self

    def __mul__(self, other: object) -> "RationalInterval":
        rhs = other if isinstance(other, RationalInterval) else RationalInterval(other)
        products = (
            self.lower * rhs.lower,
            self.lower * rhs.upper,
            self.upper * rhs.lower,
            self.upper * rhs.upper,
        )
        return RationalInterval(min(products), max(products))

    __rmul__ = __mul__


def evaluate_polynomial_interval(
    polynomial: sp.Poly, argument: RationalInterval
) -> RationalInterval:
    value = RationalInterval(0)
    for coefficient in polynomial.all_coeffs():
        value = value * argument + as_fraction(coefficient)
    return value


def interval_matrix_multiply(
    left: list[list[RationalInterval]], right: list[list[RationalInterval]]
) -> list[list[RationalInterval]]:
    return [
        [
            sum(
                (left[row][index] * right[index][column] for index in range(2)),
                RationalInterval(0),
            )
            for column in range(2)
        ]
        for row in range(2)
    ]


def monodromy_trace_interval(
    q_interval: RationalInterval,
    p_interval: RationalInterval,
    period: int,
) -> RationalInterval:
    q_value, p_value = q_interval, p_interval
    monodromy = [
        [RationalInterval(1), RationalInterval(0)],
        [RationalInterval(0), RationalInterval(1)],
    ]
    for _ in range(period):
        for parameter_sympy in PARAMETERS:
            parameter = as_fraction(parameter_sympy)
            jacobian = [
                [-2 * parameter * q_value, RationalInterval(-1)],
                [RationalInterval(1), RationalInterval(0)],
            ]
            monodromy = interval_matrix_multiply(jacobian, monodromy)
            q_new = RationalInterval(1) - parameter * q_value * q_value - p_value
            q_value, p_value = q_new, q_value
    return monodromy[0][0] + monodromy[1][1]


def hyperbolicity_margin(trace: RationalInterval) -> Fraction:
    if trace.lower > 2:
        return trace.lower - 2
    if trace.upper < -2:
        return -trace.upper - 2
    return Fraction(-1)


def fraction_decimal(value: Fraction, significant_digits: int = 18) -> str:
    with localcontext() as context:
        context.prec = significant_digits + 8
        decimal_value = Decimal(value.numerator) / Decimal(value.denominator)
        return format(decimal_value, f".{significant_digits}g")


def fraction_digest(value: Fraction) -> str:
    numerator = value.numerator.to_bytes(
        max(1, (abs(value.numerator).bit_length() + 8) // 8), "big", signed=True
    )
    denominator = value.denominator.to_bytes(
        max(1, (value.denominator.bit_length() + 7) // 8), "big", signed=False
    )
    return hashlib.sha256(numerator + b"/" + denominator).hexdigest()


def interval_payload(
    interval: RationalInterval, include_exact_fraction: bool = True
) -> dict[str, object]:
    payload: dict[str, object] = {
        "lower_decimal_display": fraction_decimal(interval.lower),
        "upper_decimal_display": fraction_decimal(interval.upper),
        "lower_fraction_sha256": fraction_digest(interval.lower),
        "upper_fraction_sha256": fraction_digest(interval.upper),
        "lower_numerator_bits": abs(interval.lower.numerator).bit_length(),
        "upper_numerator_bits": abs(interval.upper.numerator).bit_length(),
        "lower_denominator_bits": interval.lower.denominator.bit_length(),
        "upper_denominator_bits": interval.upper.denominator.bit_length(),
    }
    if include_exact_fraction:
        payload["lower_fraction"] = str(interval.lower)
        payload["upper_fraction"] = str(interval.upper)
    return payload


def numeric_superstep(point: tuple[float, float]) -> tuple[float, float]:
    q_value, p_value = point
    for parameter in (0.5, 1.5, 2.5):
        q_value, p_value = 1.0 - parameter * q_value * q_value - p_value, q_value
    return q_value, p_value


def numeric_monodromy(point: tuple[float, float], period: int) -> list[list[float]]:
    q_value, p_value = point
    monodromy = [[1.0, 0.0], [0.0, 1.0]]
    for _ in range(period):
        for parameter in (0.5, 1.5, 2.5):
            jacobian = [[-2.0 * parameter * q_value, -1.0], [1.0, 0.0]]
            monodromy = [
                [
                    sum(jacobian[row][index] * monodromy[index][column] for index in range(2))
                    for column in range(2)
                ]
                for row in range(2)
            ]
            q_value, p_value = 1.0 - parameter * q_value * q_value - p_value, q_value
    return monodromy


def signed_multipliers(trace: float) -> tuple[float, float]:
    discriminant = math.sqrt(trace * trace - 4.0)
    values = ((trace + discriminant) / 2.0, (trace - discriminant) / 2.0)
    stable = min(values, key=abs)
    unstable = max(values, key=abs)
    return stable, unstable


def root_phase_records(
    polynomial: sp.Poly, p_expression: sp.Expr, period: int
) -> list[dict[str, object]]:
    p_polynomial = sp.Poly(p_expression, Q, domain=sp.QQ)
    intervals = polynomial.intervals(eps=ROOT_EPSILON)
    records: list[dict[str, object]] = []
    for index, ((lower, upper), multiplicity) in enumerate(intervals):
        if multiplicity != 1:
            raise ArithmeticError("non-simple isolated root")
        q_interval = RationalInterval(lower, upper)
        p_interval = evaluate_polynomial_interval(p_polynomial, q_interval)
        trace_interval = monodromy_trace_interval(q_interval, p_interval, period)
        margin = hyperbolicity_margin(trace_interval)
        if margin <= 0:
            raise ArithmeticError("short orbit is not certified hyperbolic")

        q_mid = (q_interval.lower + q_interval.upper) / 2
        p_mid_sympy = p_polynomial.eval(sp.Rational(q_mid.numerator, q_mid.denominator))
        point = (float(q_mid), float(p_mid_sympy))
        monodromy = numeric_monodromy(point, period)
        trace = monodromy[0][0] + monodromy[1][1]
        determinant = monodromy[0][0] * monodromy[1][1] - monodromy[0][1] * monodromy[1][0]
        stable, unstable = signed_multipliers(trace)

        records.append(
            {
                "phase_index": index,
                "point": {"q": format(point[0], ".16g"), "p": format(point[1], ".16g")},
                "q_isolating_interval": interval_payload(q_interval),
                "p_interval": interval_payload(p_interval),
                "algebraic_multiplicity": 1,
                "trace": format(trace, ".16g"),
                "trace_interval": interval_payload(trace_interval, include_exact_fraction=False),
                "hyperbolicity_margin_lower": fraction_decimal(margin),
                "det_monodromy_numeric": format(determinant, ".16g"),
                "stable_multiplier_signed": format(stable, ".16g"),
                "unstable_multiplier_signed": format(unstable, ".16g"),
                "det_I_minus_M_signed": format(2.0 - trace, ".16g"),
            }
        )
    return records


def nearest_phase_index(
    target: tuple[float, float], phases: list[dict[str, object]]
) -> tuple[int, float]:
    distances = []
    for phase in phases:
        point = phase["point"]
        candidate = (float(point["q"]), float(point["p"]))
        distances.append(math.hypot(target[0] - candidate[0], target[1] - candidate[1]))
    index = min(range(len(distances)), key=distances.__getitem__)
    return index, distances[index]


def orbit_records(
    period_one_phases: list[dict[str, object]],
    period_two_phases: list[dict[str, object]],
) -> tuple[list[dict[str, object]], float]:
    orbits: list[dict[str, object]] = []
    for index, phase in enumerate(period_one_phases, start=1):
        orbits.append(
            {
                "orbit_id": f"TH-0001-P1-{index:03d}",
                "G_period": 1,
                "micro_kick_count": 3,
                "cyclic_phase_multiplicity": 1,
                "forward_orientation": "one G-step",
                "phases": [phase],
                "det_monodromy_exact": "1",
                "repetition_rule": "M_(gamma^r)=M_gamma^r",
                "magnetic_phase": "NOT_DEFINED",
                "Maslov_phase": "NOT_DEFINED",
                "zeta_amplitude": "NOT_DEFINED",
            }
        )

    partner: dict[int, int] = {}
    max_pair_distance = 0.0
    for index, phase in enumerate(period_two_phases):
        point = (float(phase["point"]["q"]), float(phase["point"]["p"]))
        next_point = numeric_superstep(point)
        partner_index, distance = nearest_phase_index(next_point, period_two_phases)
        partner[index] = partner_index
        max_pair_distance = max(max_pair_distance, distance)
    if max_pair_distance >= 1e-10:
        raise ArithmeticError(f"period-two pairing drift {max_pair_distance}")
    if any(partner[index] == index or partner[partner[index]] != index for index in partner):
        raise ArithmeticError("period-two phase pairing is not a fixed-point-free involution")

    pairs = sorted({tuple(sorted((index, partner[index]))) for index in partner})
    for orbit_number, (left, right) in enumerate(pairs, start=1):
        phases = [period_two_phases[left], period_two_phases[right]]
        phases.sort(key=lambda phase: (float(phase["point"]["q"]), float(phase["point"]["p"])))
        orbits.append(
            {
                "orbit_id": f"TH-0001-P2-{orbit_number:03d}",
                "G_period": 2,
                "micro_kick_count": 6,
                "cyclic_phase_multiplicity": 2,
                "forward_orientation": "canonical phase followed by one G-step",
                "phases": phases,
                "det_monodromy_exact": "1",
                "repetition_rule": "M_(gamma^r)=M_gamma^r",
                "magnetic_phase": "NOT_DEFINED",
                "Maslov_phase": "NOT_DEFINED",
                "zeta_amplitude": "NOT_DEFINED",
            }
        )
    return orbits, max_pair_distance


def cyclic_rotations(values: tuple[sp.Rational, ...]) -> set[tuple[sp.Rational, ...]]:
    return {values[index:] + values[:index] for index in range(len(values))}


def build_report() -> dict[str, object]:
    data = elimination_data()
    basis1 = data["basis1"]
    basis2 = data["basis2"]
    r1 = data["r1"]
    r2 = data["r2"]
    d2 = data["d2"]

    expected_r1 = sp.Poly(
        225 * Q**8
        - 1800 * Q**6
        + 1920 * Q**5
        + 2760 * Q**4
        - 3840 * Q**3
        - 736 * Q**2
        + 1536 * Q
        - 48,
        Q,
        domain=sp.ZZ,
    )
    if r1 != expected_r1:
        raise AssertionError(r1)

    hashes = {
        "R1": polynomial_hash(r1),
        "R2": polynomial_hash(r2),
        "D2": polynomial_hash(d2),
    }
    expected_hashes = {
        "R1": "a0ed76ae20ec9a1300785e86109dd145039c50eb44879be7d9e2202a3acbbc7a",
        "R2": "eee0ae04452a9ff02da3c2eadbb8bba4b05787e0392978c029b2c131288d2d0a",
        "D2": "60dd88608e229e19708948f239bc7e4f8f80f536a3c54a763dbe59ee924c46dc",
    }
    if hashes != expected_hashes:
        raise AssertionError(hashes)

    if sp.gcd(r1, r1.diff()).degree() != 0:
        raise ArithmeticError("R1 is not square-free")
    if sp.gcd(r2, r2.diff()).degree() != 0:
        raise ArithmeticError("R2 is not square-free")
    if sp.gcd(d2, d2.diff()).degree() != 0:
        raise ArithmeticError("D2 is not square-free")
    if sp.gcd(r1, d2).degree() != 0:
        raise ArithmeticError("primitive period-two quotient intersects R1")

    period_one_phases = root_phase_records(r1, data["p1"], 1)
    period_two_phases = root_phase_records(d2, data["p2"], 2)
    orbits, max_pair_distance = orbit_records(period_one_phases, period_two_phases)
    margins = [
        Fraction(phase["hyperbolicity_margin_lower"])
        for phase in period_one_phases + period_two_phases
    ]

    reverse_schedule = tuple(reversed(PARAMETERS))
    swap_left = superstep(0, 0)
    swap_left = (swap_left[1], swap_left[0])
    inverse_at_origin = inverse_superstep(0, 0)
    lambda_symbol = sp.symbols("lambda")
    first, _, last = PARAMETERS
    affine_gcd = sp.gcd(
        sp.Poly(first**2 * lambda_symbol**5 - last**2, lambda_symbol, domain=sp.QQ),
        sp.Poly(first**3 * lambda_symbol**7 - last**3, lambda_symbol, domain=sp.QQ),
    )

    return {
        "candidate_id": CANDIDATE_ID,
        "clue_id": CLUE_ID,
        "formal_candidate": True,
        "definition": {
            "phase_space": "R^2",
            "symplectic_form": "dq wedge dp",
            "micro_map": "F_a(q,p)=(1-a*q^2-p,q)",
            "parameter_rule": "a_j=j+1/2 for j=0,1,2",
            "micro_kick_order": ["1/2", "3/2", "5/2"],
            "autonomous_map": "G=F_(5/2) o F_(3/2) o F_(1/2)",
            "clock": "one G-superstep",
            "determinant_convention": "NOT_OPENED",
        },
        "symplectic_audit": {
            "micro_jacobian": "[[-2*a*q,-1],[1,0]]",
            "micro_determinant_exact": 1,
            "superstep_determinant_exact": 1,
            "generating_function": "S_a(q,Q)=q*Q-q+(a/3)*q^3",
            "algebraic_degree_G": 8,
            "algebraic_dynamical_degree": 8,
            "inverse_order": ["5/2", "3/2", "1/2"],
        },
        "time_reversal_audit": {
            "parent_swap_reversor": "R(q,p)=(p,q), R F_a R=F_a^-1",
            "swap_reversor_for_G": False,
            "swap_witness_RGR_at_origin": [str(swap_left[0]), str(swap_left[1])],
            "swap_witness_G_inverse_at_origin": [str(inverse_at_origin[0]), str(inverse_at_origin[1])],
            "reverse_schedule_is_cyclic_rotation": reverse_schedule in cyclic_rotations(PARAMETERS),
            "inherited_clock_reflection_reversor": False,
            "affine_antisymplectic_involution": False,
            "affine_leading_equations": ["a^2*lambda^5=c^2", "a^3*lambda^7=c^3"],
            "affine_equation_gcd_degree": affine_gcd.degree(),
            "arbitrary_nonlinear_reversor": "OPEN",
        },
        "low_depth_controls": {
            "single_quadratic_post_shear": "conjugate to a single shifted-parameter Henon map",
            "static_generalized_Henon": "still reversible under coordinate swap",
            "two_kick_composition": "reversible under I_a=F_a^-1 o R",
            "parent_F1_real_fixed_points": 2,
        },
        "exact_elimination": {
            "basis_shapes": {
                "period_1": [[int(poly.degree(P)), int(poly.degree(Q))] for poly in basis1.polys],
                "period_2": [[int(poly.degree(P)), int(poly.degree(Q))] for poly in basis2.polys],
            },
            "R1_degree": int(r1.degree()),
            "R2_degree": int(r2.degree()),
            "D2_degree": int(d2.degree()),
            "R1_real_roots": int(r1.count_roots(-sp.oo, sp.oo)),
            "R2_real_roots": int(r2.count_roots(-sp.oo, sp.oo)),
            "D2_real_roots": int(d2.count_roots(-sp.oo, sp.oo)),
            "R1_square_free": True,
            "R2_square_free": True,
            "D2_square_free": True,
            "gcd_R1_D2_degree": int(sp.gcd(r1, d2).degree()),
            "polynomial_hashes": hashes,
            "R1_coefficients_descending": [int(value) for value in r1.all_coeffs()],
        },
        "primitive_orbit_census": {
            "cutoff_G_period": 2,
            "search_box": None,
            "random_seed": None,
            "real_period_1_phase_points": len(period_one_phases),
            "real_primitive_period_2_phase_points": len(period_two_phases),
            "real_primitive_period_1_orbits": len(period_one_phases),
            "real_primitive_period_2_orbits": len(period_two_phases) // 2,
            "total_real_primitive_orbits": len(orbits),
            "total_real_phase_points": len(period_one_phases) + len(period_two_phases),
            "all_short_orbits_hyperbolic": True,
            "minimum_certified_abs_trace_minus_two": fraction_decimal(min(margins)),
            "period_two_max_pairing_distance": format(max_pair_distance, ".16g"),
            "completeness": "global over R^2 for real G-period <=2 only",
            "orbits": orbits,
        },
        "route_a_prefilter": {
            "A1": "A1_WEAK",
            "A2": "A2_FAIL",
            "A3": "A3_FAIL",
            "A4": "A4_FORMAL_HINT",
            "overall": "ROUTE_A_EXPLORATORY",
            "recommended_verdict": "GO_WITH_LIMITATIONS",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "established": [
                "one explicit autonomous target-free exact-symplectic three-kick map",
                "absence of inherited and affine anti-symplectic reversors",
                "non-conjugacy to every single legacy F_a by degree and fixed-point count",
                "complete real primitive UPO census through G-period two",
                "signed monodromy and certified hyperbolicity for every orbit in that prefix",
            ],
            "not_established": [
                "absence of arbitrary nonlinear anti-symplectic reversors",
                "complete UPOs at G-period three or higher",
                "a prime-like clock, von-Mangoldt weights, or arithmetic orbit law",
                "a dynamical zeta or Fredholm determinant",
                "global analytic structure, a quantum operator, Route B, Hilbert-Polya, or RH",
            ],
            "next_smallest_task": (
                "Freeze the same-order Fourier-integral quantization U=U_(5/2) U_(3/2) U_(1/2) "
                "on L2(R), then prove its normalization and unitarity and audit its natural antiunitary "
                "symmetry. Do not compute a spectrum or define a determinant in that task."
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    arguments = parser.parse_args()
    report = build_report()
    payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(payload, encoding="utf-8")
    if not arguments.quiet:
        print(payload, end="")


if __name__ == "__main__":
    main()
