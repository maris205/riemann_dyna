# Literature boundary for SS-0003 a-point counting

The scalar continuation produced by the frozen renewal graph is 2-zeta(s).
The only external fact used in the prefilter is the classical counting theorem
for fixed a-points of the Riemann zeta function.

## Sources

- H. Bohr, E. Landau, and J. E. Littlewood, Sur la fonction zeta(s) dans le
  voisinage de la droite sigma=1/2, Bull. Acad. Roy. Belg. (1913), 3--35.
  Landau's result gives the Riemann-von Mangoldt type count for fixed a != 1,
  with a=2 as the case used here.
- E. C. Titchmarsh and M. Heath-Brown, The Theory of the Riemann
  Zeta-Function, 2nd ed., Clarendon Press, 1986, section 9.4 (a-points).
- P.-C. Hang and M.-J. Luo, Note on the a-points of the Riemann zeta
  function, arXiv:2411.13255v2 (2024), introduction, equation (1.3), which
  restates Landau's formula as
  N_a(T)=T/(2*pi)*log(T/(2*pi*e*c_a))+O(log T), c_a=1 for a != 1,
  for nontrivial a-points (Re rho_a>0, positive ordinate).

The arXiv source writes the error as `\mo(log T)` and defines
`\mo` to mean `\mathcal{O}`; hence the `O(log T)` transcription above is
literal, not a strengthened error term.

## Scope used in the repository

For a=2, the elementary bound

\[
|\zeta(\sigma+it)-1|\le\sum_{n\ge2}n^{-\sigma}<1
\quad(\sigma\ge2)
\]

excludes a=2 points in Re(s)>=2.  Thus the nontrivial a=2 points counted by
Landau's theorem lie in the fixed strip 0<Re(s)<2.  This is a divisor-order
prefilter only.  It does not assert that the points lie on the critical line,
that their multiplicities match Riemann zeros, or that the scalar continuation
is a Fredholm determinant outside Re(s)>1.

No zero table, numerical root search, or target fitting is used.
