# Frozen COPRIME kernel: exact ell^2 operator boundary

Status: PROVED_OBSTRUCTION (candidate-local, scope-limited)

Source: COPRIME-0001 / formal/results/coprime_0001_countable_trace.md

Let I={2,3,...} and

~~~text
(L_s)_{mn} = 1_{gcd(m,n)=1} (mn)^(-s/2)
~~~

act on ell^2(I), with sigma=Re(s). For sigma>1, the Mobius rank-one
decomposition gives a locally uniformly trace-norm convergent family. The
half-plane is sharp for the frozen matrix as a bounded operator: for the
coordinate vector e_2,

~~~text
||L_s e_2||_2^2
  = 2^(-sigma) * sum_{m>=3, m odd} m^(-sigma).
~~~

The odd p-series diverges for sigma<=1. Thus the same matrix is not a bounded
ell^2 operator, and in particular cannot be trace class, on that half-plane.

## Impact

Any continuation of the scalar Fredholm determinant across Re(s)=1 would
need a separately proved scalar continuation theorem, a different function
space, or a different regularized object. It cannot be described as a silent
extension of the original bounded ell^2 transfer operator.

This obstruction does not rule out continuation of a scalar determinant, nor
does it rule out a different intrinsically defined Banach/Hilbert realization.
It also does not by itself establish a target-divisor mismatch.

## Reopening condition

Freeze one explicit continuation or alternate function-space construction,
prove its operator/determinant identity, and keep its clock and determinant
ledger separate from the original D_cop(s)=det_F(I-L_s).
