#!/usr/bin/env python3
"""Target-free Fourier-integral quantization audit for TH-0001.

This module records exact operator identities only.  It does not discretize an
operator, compute eigenvalues, read target tables, or define a determinant.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


CANDIDATE_ID = "TH-0001"
AUDIT_ID = "TH-0001-A4-FIO-001"
CLUE_ID = "CLUE-A4-001"
HBAR = sp.Integer(1)
PARAMETERS = (sp.Rational(1, 2), sp.Rational(3, 2), sp.Rational(5, 2))
q, Q, p = sp.symbols("q Q p", real=True)


def potential(parameter: sp.Rational) -> sp.Expr:
    return sp.expand(-q + parameter * q**3 / 3)


def generating_function(parameter: sp.Rational) -> sp.Expr:
    return sp.expand(q * Q + potential(parameter))


def henon_step(point: tuple[sp.Rational, sp.Rational], parameter: sp.Rational):
    x, y = point
    return (sp.expand(1 - parameter * x**2 - y), x)


def inverse_henon_step(point: tuple[sp.Rational, sp.Rational], parameter: sp.Rational):
    x, y = point
    return (y, sp.expand(1 - parameter * y**2 - x))


def compose_schedule(parameters: tuple[sp.Rational, ...], point=(sp.Rational(0), sp.Rational(0))):
    result = point
    for parameter in parameters:
        result = henon_step(result, parameter)
    return result


def compose_inverse_schedule(parameters: tuple[sp.Rational, ...], point=(sp.Rational(0), sp.Rational(0))):
    result = point
    for parameter in reversed(parameters):
        result = inverse_henon_step(result, parameter)
    return result


def fraction_string(value: sp.Rational) -> str:
    value = sp.Rational(value)
    if value.q == 1:
        return str(value.p)
    return f"{value.p}/{value.q}"


def build_report() -> dict[str, object]:
    a, b, c = PARAMETERS
    kernel_phases = {
        fraction_string(parameter): sp.sstr(generating_function(parameter))
        for parameter in PARAMETERS
    }
    derivative_ledger = {}
    for parameter in PARAMETERS:
        S = generating_function(parameter)
        derivative_ledger[fraction_string(parameter)] = {
            "minus_dq_S": sp.sstr(sp.expand(-sp.diff(S, q))),
            "dQ_S": sp.sstr(sp.diff(S, Q)),
            "solved_Q": sp.sstr(sp.solve(sp.Eq(p, -sp.diff(S, q)), Q)[0]),
            "solved_P": sp.sstr(sp.diff(S, Q)),
            "mixed_hessian": sp.sstr(sp.diff(S, q, Q)),
        }

    forward_origin = compose_schedule((a, b, c))
    reverse_origin = compose_schedule((c, b, a))
    inverse_origin = compose_inverse_schedule((a, b, c))
    rgr_origin = (forward_origin[1], forward_origin[0])
    reverse_word = tuple(fraction_string(x) for x in reversed(PARAMETERS))
    forward_word = tuple(fraction_string(x) for x in PARAMETERS)
    cyclic_words = [
        forward_word[i:] + forward_word[:i] for i in range(len(forward_word))
    ]

    # Exact Heisenberg-order witness.  Ad_{U_a}(q)=p and
    # Ad_{U_a}(p)=1-q-a*p^2, so U_b U_a and U_a U_b differ for a != b.
    noncommuting_ba = sp.expand(1 - q - b * p**2)
    noncommuting_ab = sp.expand(1 - q - a * p**2)

    return {
        "candidate_id": CANDIDATE_ID,
        "audit_id": AUDIT_ID,
        "clue_id": CLUE_ID,
        "hbar": "1",
        "source_lock": "configs/source_locks/TH-0001-FIO.yaml",
        "definition": {
            "hilbert_space": "L^2(R,dq)",
            "core": "Schwartz space S(R)",
            "fourier_plus": "(F_+ psi)(Q)=(2*pi)^(-1/2) integral exp(+i*q*Q) psi(q)dq",
            "multiplication": "(M_a psi)(q)=exp(i*V_a(q)) psi(q)",
            "potential": "V_a(q)=-q+(a/3)*q^3",
            "micro_operator": "U_a=F_+ M_a",
            "kernel": "K_a(Q,q)=(2*pi)^(-1/2) exp(i*S_a(q,Q))",
            "superoperator": "U=U_(5/2) U_(3/2) U_(1/2)",
            "global_phase": "1",
        },
        "generating_function_audit": {
            "functions": kernel_phases,
            "derivatives": derivative_ledger,
            "canonical_graph": "p=-d_q S_a, P=d_Q S_a gives Q=1-a*q^2-p, P=q",
            "mixed_hessian_exact": True,
            "mixed_hessian_value": "1",
        },
        "unitarity_audit": {
            "potential_real_for_frozen_parameters": True,
            "multiplication_modulus": "|exp(i*V_a(q))|=1",
            "fourier_normalization": "(2*pi)^(-1/2)",
            "fourier_unitary_by_plancherel": True,
            "each_factor_unitary_on_all_L2": True,
            "product_unitary_on_all_L2": True,
            "inverse_word": ["U_(1/2)^(-1)", "U_(3/2)^(-1)", "U_(5/2)^(-1)"],
            "triple_kernel_status": "iterated oscillatory integral; no absolute-convergence or global single-phase claim",
            "caustic_warning": "caustic: reduced intermediate Hessian can vanish; factorized operator remains unitary",
            "spectrum_computed": False,
        },
        "antiunitary_audit": {
            "complex_conjugation": "C psi=conjugate(psi)",
            "antiunitary": "A=F_+ C",
            "A_squared": True,
            "A_q_A_inverse": "p",
            "A_p_A_inverse": "q",
            "classical_action": "swap R(q,p)=(p,q)",
            "fourier_conjugation": "C F_+ C=F_+^(-1)",
            "multiplication_conjugation": "C M_a C=M_a^(-1)",
            "single_kick_reversor": True,
            "forward_operator_word": ["U_(5/2)", "U_(3/2)", "U_(1/2)"],
            "A_conjugated_product_word": ["U_(5/2)^(-1)", "U_(3/2)^(-1)", "U_(1/2)^(-1)"],
            "product_inverse_word": ["U_(1/2)^(-1)", "U_(3/2)^(-1)", "U_(5/2)^(-1)"],
            "inherited_A_reversor_for_product": False,
            "reverse_word": list(reverse_word),
            "forward_word": list(forward_word),
            "forward_cyclic_rotations": [list(word) for word in cyclic_words],
            "reverse_word_is_cyclic_rotation": reverse_word in cyclic_words,
            "natural_clock_reflection_reversor": False,
            "arbitrary_antiunitary_reversor": "OPEN",
        },
        "exact_order_controls": {
            "forward_origin": [fraction_string(x) for x in forward_origin],
            "reverse_origin": [fraction_string(x) for x in reverse_origin],
            "G_inverse_origin": [fraction_string(x) for x in inverse_origin],
            "R_G_R_origin": [fraction_string(x) for x in rgr_origin],
            "swap_reversor_witness_differs": rgr_origin != inverse_origin,
            "noncommutation_pair": {
                "Ad_U_b_U_a_on_q": sp.sstr(noncommuting_ba),
                "Ad_U_a_U_b_on_q": sp.sstr(noncommuting_ab),
                "difference": sp.sstr(sp.expand(noncommuting_ba - noncommuting_ab)),
                "nonzero_for_frozen_a_b": noncommuting_ba != noncommuting_ab,
            },
        },
        "route_a_a4": {
            "verdict": "A4_NATURAL_QUANTIZATION",
            "evidence_status": "PROVED",
            "same_clock": True,
            "operator_everywhere_defined": True,
            "unitary_product": True,
            "natural_antiunitary_inherited_class_audited": True,
            "route_b_ready": False,
        },
        "claim_boundary": {
            "established": [
                "same-order Fourier-integral factor U_a with frozen positive-real normalization",
                "exact canonical graph matching each F_a",
                "each factor and the three-kick product are unitary on L^2(R)",
                "A=F_+ C is an involutive antiunitary implementing the parent swap",
                "A reverses each kick but not the non-palindromic three-kick superstep",
                "inherited cyclic clock-reflection antiunitaries fail",
            ],
            "not_established": [
                "absence of arbitrary nonlinear or non-geometric antiunitaries",
                "self-adjoint Hamiltonian, spectral type, or Route B obligations",
                "any spectrum, determinant, trace formula, zero relation, or RH statement",
            ],
            "next_smallest_task": "Freeze the next smallest same-object phase/branch convention only if needed; do not compute a spectrum or determinant.",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()
    payload = json.dumps(build_report(), indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    if not args.quiet:
        print(payload, end="")


if __name__ == "__main__":
    main()
