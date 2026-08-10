#!/usr/bin/env python3
"""Target-free scalar-continuation and endpoint-barrier audit.

This module records exact symbolic gates for COPRIME-0001's second audit.
It does not enumerate primes, evaluate zeta values, compute a determinant, or
locate a root.  The continuation statement is the squarefree-divisor
Sylvester identity

    C_s = V_s.T V_s M = zeta(s) T_s - P_1,
    D_tilde(s) = det_2(I-C_s),

which agrees with det_F(I-L_s) on Re(s)>1 and is an S_2 representation on
Re(s)>1/2 away from s=1.  A separate min--max ledger proves that the original
scalar determinant has infinitely many positive real zeros tending to s=1,
so no holomorphic or meromorphic germ can cross that endpoint.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


CANDIDATE_ID = "COPRIME-0001"
AUDIT_ID = "COPRIME-0001-SCALAR-BOUNDARY-001"
CLUE_ID = "CLUE-A1-009"
SOURCE_LOCK = "configs/source_locks/COPRIME-0001-SCALAR-BOUNDARY.yaml"
PARENT_EVALUATION = "evaluations/route_a/COPRIME-0001/20260809T134933Z.yaml"
GENERATOR = "experiments/coprime_0001_scalar_boundary.py"
ARTIFACT = "artifacts/coprime_0001/scalar_boundary_certificate.json"
FORMAL_RESULT = "formal/results/coprime_0001_scalar_boundary.md"
OBSTRUCTION = "formal/obstructions/coprime_scalar_endpoint_accumulation.md"


def file_sha256(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _local_factor_checks() -> dict[str, Any]:
    return {
        "local_kernel": (
            "M_p(q)_{ab}=1_{min(a,b)=0} q^((a+b)/2), "
            "q=p^(-s)"
        ),
        "rank": 2,
        "characteristic_polynomial": "lambda^2-lambda-q/(1-q)",
        "nonzero_eigenvalues": (
            "alpha_pm(q)=(1+-sqrt((1+3q)/(1-q)))/2"
        ),
        "sign_for_real_0_lt_q_lt_1": {
            "alpha_plus_positive": True,
            "alpha_minus_negative": True,
        },
        "growth_lower_bound": "alpha_plus(q)>=1+q",
        "growth_bound_identity": (
            "(1+3q)/(1-q)-(1+2q)^2=4q^3/(1-q)>=0"
        ),
        "ratio_nonzero": "rho_p=alpha_minus/alpha_plus != 0",
        "finite_prime_compression_spectrum": (
            "prod_{p in P} alpha_plus(p^(-s)) * "
            "prod_{p in S} rho_p(s), S subseteq P"
        ),
    }


def _sylvester_checks() -> dict[str, Any]:
    return {
        "divisor_index": "S={d>=1: d squarefree}",
        "factorization": "L_s=V_s M V_s^T",
        "V_entry": "V_s(m,d)=1_{d|m} m^(-s/2)",
        "M_entry": "M(d,d)=mu(d)",
        "gram_entry": (
            "(V_s^T V_s)_{de}=zeta(s)[d,e]^(-s)-delta_{d=e=1}"
        ),
        "auxiliary_entry": (
            "C_s=V_s^T V_s M=zeta(s)T_s-P_1, "
            "T_s(d,e)=mu(e)[d,e]^(-s)"
        ),
        "hs_euler_factor": "||H_s||_2^2=prod_p(1+3 p^(-2 Re(s)))",
        "hs_domain": "Re(s)>1/2",
        "continuation_domain": "Omega={Re(s)>1/2, s!=1}",
        "regularized_determinant": "D_tilde(s)=det_2(I-C_s)",
        "same_scalar_on_original_domain": True,
        "trace_on_original_domain": "Tr(C_s)=zeta(s)sum_sf mu(d)d^(-s)-1=0",
        "sylvester_identity": "det_F(I-L_s)=det_F(I-C_s), Re(s)>1",
        "original_operator_extended_below_boundary": False,
    }


def _endpoint_checks() -> dict[str, Any]:
    return {
        "label_one_completion": (
            "K_s(m,n)=1_{gcd(m,n)=1}(mn)^(-s/2), m,n>=1"
        ),
        "compression_relation": "L_s=K_s restricted/compressed to e_1^perp",
        "prime_coordinate_argument": (
            "finite squarefree-prime coordinate compressions; no prime table"
        ),
        "top_product_diverges": (
            "prod_p alpha_plus(p^(-sigma)) -> infinity as sigma downarrow 1"
        ),
        "fixed_positive_mode_count": (
            "for every M, the M-th positive eigenvalue of L_sigma tends to "
            "+infinity as sigma downarrow 1"
        ),
        "safe_right_endpoint": (
            "||L_3|| <= zeta(3)^2/zeta(6)-1 < 9/16 < 1"
        ),
        "continuity": "sigma -> L_sigma is trace-norm/operator-norm continuous on (1,infinity)",
        "fredholm_zero_criterion": "D_cop(sigma)=0 iff 1 is an eigenvalue of L_sigma",
        "real_zero_accumulation": "exists sigma_j>1 with sigma_j downarrow 1 and D_cop(sigma_j)=0",
        "root_locations_computed": False,
        "root_search_performed": False,
        "meromorphic_germ_at_one": False,
        "endpoint_scope": (
            "blocks any continuation containing a neighborhood of s=1; "
            "does not claim a barrier at every 1+it"
        ),
    }


def build_report(root: str | Path | None = None) -> dict[str, Any]:
    base = Path(root) if root is not None else Path(__file__).resolve().parents[1]
    source_inputs = {
        SOURCE_LOCK: file_sha256(base / SOURCE_LOCK),
        PARENT_EVALUATION: file_sha256(base / PARENT_EVALUATION),
    }
    return {
        "candidate_id": CANDIDATE_ID,
        "audit_id": AUDIT_ID,
        "clue_id": CLUE_ID,
        "formal_candidate": True,
        "target_data_used": {
            "prime_table": False,
            "prime_enumeration": False,
            "primality_predicate": False,
            "zero_table": False,
            "determinant_values": False,
            "root_locations": False,
            "fitting": False,
        },
        "local_factor_checks": _local_factor_checks(),
        "sylvester_continuation_checks": _sylvester_checks(),
        "endpoint_barrier_checks": _endpoint_checks(),
        "route_effect": {
            "analytic_tuple": [
                "A1_WEAK",
                "A2_ANALYTIC_DETERMINANT",
                "A3_CONTROLLED_CONTINUATION",
                "A4_FAIL",
            ],
            "riemann_target_tuple": [
                "A1_WEAK",
                "A2_FAIL",
                "A3_FAIL",
                "A4_FAIL",
            ],
            "overall_verdict": "ROUTE_A_EXPLORATORY",
            "scoped_audit_verdict": "STOP_SCOPED",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "established": [
                "D_tilde=det_2(I-C_s) is holomorphic on Re(s)>1/2, s!=1",
                "D_tilde equals D_cop on Re(s)>1",
                "the frozen ell^2 matrix is not extended below Re(s)=1",
                "D_cop has infinitely many positive real zeros accumulating at s=1",
                "no holomorphic or meromorphic germ crosses s=1",
            ],
            "not_established": [
                "a continuation through s=1",
                "a completed-xi functional equation or divisor equality",
                "a prime-orbit or von-Mangoldt law",
                "natural quantization, Route B, Hilbert-Polya, or RH",
            ],
        },
        "next_smallest_task": (
            "Park COPRIME-0001 under the endpoint obstruction; any reopening "
            "must freeze a new determinant or function space explicitly."
        ),
        "provenance": {
            "source_inputs_sha256": source_inputs,
            "generator_sha256": file_sha256(base / GENERATOR),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--output", type=Path, default=Path(ARTIFACT))
    args = parser.parse_args()
    report = build_report()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    if not args.quiet:
        print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
