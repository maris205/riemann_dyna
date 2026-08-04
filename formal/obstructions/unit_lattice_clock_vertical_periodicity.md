# Unit-lattice clocks force a vertically periodic divisor

## Status

`PROVED_OBSTRUCTION`

Source: `CLUE-A1-004` / `P4-LOGISTIC-RECURRENT-UC-ANCHORED-CLOCK`

## Theorem

Let $H$ be a nonzero single-valued meromorphic function on
$\mathbb C\setminus\{0\}$, and define

\[
D(s)=H(e^{-s}).
\]

Then

\[
D(s+2\pi i)=D(s).
\]

Fix a bounded real interval $[a,b]$. If zeros and poles are counted with
multiplicity in

\[
R_T=\{s:a\leq\Re s\leq b,\ 0<\Im s\leq T\},
\]

the zero and pole counts of $D$ are both $O(T)$.

### Proof

The periodicity follows immediately from

\[
e^{-(s+2\pi i)}=e^{-s}.
\]

The image of one closed fundamental rectangle

\[
R_0=\{s:a\leq\Re s\leq b,\ 0\leq\Im s\leq2\pi\}
\]

under $s\mapsto e^{-s}$ is the compact annulus

\[
A_{a,b}=\{z:e^{-b}\leq |z|\leq e^{-a}\}\subset\mathbb C\setminus\{0\}.
\]

Because $H$ is nonzero and meromorphic on a neighborhood of this compact
annulus, it has only finitely many zeros and poles there, counted with
multiplicity. Equivalently, $D$ has a finite divisor count in one vertical
fundamental rectangle. Translating that rectangle by integer multiples of
$2\pi i$ covers $R_T$ with $O(T)$ copies. Periodicity repeats the same
finite divisor ledger in each copy, proving the claim. ∎

## Completed-xi consequence

The nontrivial-zero count of the completed Riemann xi function in the critical
strip obeys the Riemann--von Mangoldt law

\[
N_\xi(T)
=\frac{T}{2\pi}\log\frac{T}{2\pi}
-\frac{T}{2\pi}+O(\log T)
=\Theta(T\log T).
\]

Therefore no determinant whose divisor is entirely inherited from a
single-valued meromorphic $H(e^{-s})$ can equal the completed-xi divisor in
any bounded real strip containing the nontrivial zeros. Multiplication by a
zero-free entire prefactor does not help: it changes no zeros and leaves the
periodic $O(T)$ divisor count unchanged.

For the recurrent Logistic tower,

\[
Z_T(z)=\frac{1-z^2}{1-2z^2}
\]

and the locally defined full reciprocal Artin--Mazur series both use the
unit tower-age clock. Substitution $z=e^{-s}$ is therefore only a lattice
clock diagnostic; it cannot by itself produce a completed-xi determinant.

## Scope

The obstruction applies when the same determinant remains a single-valued
meromorphic function of $e^{-s}$, possibly times a zero-free prefactor. It
does not rule out:

- an intrinsically derived non-lattice roof;
- a determinant with additional nonperiodic dynamical variables;
- a different, rigorously defined transfer-operator ledger whose $s$
  dependence does not factor through $e^{-s}$.

Adding a zero-producing factor by hand is not an escape: it changes the
determinant ledger and must be justified as part of the same dynamical object.

## Reopening condition

Derive, from the same target-free dynamics, a non-lattice clock or same-object
operator family whose divisor has a proved nonperiodic counting regime. The
new clock, normalization, repetition law, function space, and determinant
convention must be frozen before any zero comparison.
