# SS-0002 literature and determinant ledger

**Candidate:** SS-0002
**Scope:** paired-Gauss transfer operator with regular Z/6Z holonomy for the
commutator cover of the modular surface

## Frozen objects

The candidate uses one Fredholm determinant:

\[
D_{\rm ab}(s)=\det_{\rm Fr}(I-\mathcal M_s).
\]

The external theorem chain used by the Route-A evaluation is

\[
D_{\rm ab}(s)
=Z_{\Gamma}(s,\operatorname{Ind}_{\Gamma_{\rm com}}^{\Gamma}\mathbf 1)
=Z_{\Gamma_{\rm com}}(s),
\]

where \(\Gamma=\operatorname{PSL}_2(\mathbb Z)\) and
\(\Gamma_{\rm com}=[\Gamma,\Gamma]\).

This identity is first used in the absolute-convergence half-plane
\(\Re s>1\). Continuation outside that half-plane is inherited from the cited
Mayer--Selberg and Selberg-zeta theorems; it is not inferred from a finite
branch cutoff.

## Same-object trace ledger in the convergence half-plane

The finite-cover identity can also be checked directly at the Euler-factor
level, which fixes the convention used by SS-0002.

Let \(P\) be a primitive hyperbolic conjugacy class of \(\Gamma\), let
\(c=\alpha(P)\in C_6\), and let \(d\) be the order of \(c\). In the regular
representation \(\rho_{\rm reg}\), the permutation \(\rho_{\rm reg}(P)\)
consists of \(6/d\) cycles of length \(d\). Therefore

\[
\det\!\left(I-x\rho_{\rm reg}(P)\right)
=(1-x^d)^{6/d}.
\]

The corresponding twisted Selberg factor is

\[
\prod_{k\ge0}
\det\!\left(I-\rho_{\rm reg}(P)N(P)^{-s-k}\right)
=\prod_{k\ge0}
\left(1-N(P)^{-d(s+k)}\right)^{6/d}.
\]

On the cover, \(P\) closes after the minimal power \(d\), producing exactly
\(6/d\) primitive lifts, each with length \(d\ell(P)\). Hence the right-hand
side is precisely their Selberg factor. Multiplying over primitive base
classes proves

\[
Z_\Gamma(s,\rho_{\rm reg})=Z_{\Gamma_{\rm com}}(s)
\]

for \(\Re s>1\). Inserting the same regular-representation trace into the
standard Mayer trace expansion for the paired branches gives

\[
\det_{\rm Fr}(I-\mathcal M_s)=Z_\Gamma(s,\rho_{\rm reg}).
\]

This calculation also shows why base cycles with nonzero holonomy must close
after their holonomy order rather than be discarded.

## Sources and exact use

### Momeni and Venkov (arXiv:1008.4229v2)

Arash Momeni and Alexei Venkov, *Mayer Transfer Operator Approach to Selberg
Zeta Function*.

Used for:

- the scalar Mayer operator
  \((\mathcal L_s f)(z)=\sum_{n\ge1}(z+n)^{-2s}f(1/(z+n))\);
- the disk-algebra model on \(D_r=\{z:|z-1|<r\}\), including \(r=3/2\);
- nuclearity of order zero for \(\Re s>1/2\);
- the standard modular identity
  \(\det(I-\mathcal L_s^2)=Z_{\operatorname{PSL}_2(\mathbb Z)}(s)\)
  for \(\Re s>1\), followed by continuation;
- periodic continued-fraction orbits and primitive closed-geodesic lengths.

The paired branch in SS-0002 is exactly the branch appearing in
\(\mathcal L_s^2\):

\[
\phi_{a,b}(z)=\frac{z+a}{b(z+a)+1},\qquad
\phi'_{a,b}(z)=[b(z+a)+1]^{-2}.
\]

### Fraczek and Mayer (DOI: 10.2140/ant.2012.6.587)

Markus Fraczek and Dieter Mayer, *Symmetries of the transfer operator for
Gamma_0(N) and a character deformation of the Selberg zeta function for
Gamma_0(4)*, Algebra & Number Theory 6 (2012), 587--610.

Used as a finite-dimensional character-twist reference for Mayer transfer
operators and Selberg zeta functions. The SS-0002 fibre action is the regular
representation of the finite quotient \(\Gamma/\Gamma_{\rm com}\cong C_6\).

### Fraczek (DOI: 10.1007/978-3-319-51296-9_7)

Markus Szymon Fraczek, *Transfer Operators for the Geodesic Flow on Hyperbolic
Surfaces*, in *Selberg Zeta Functions and Transfer Operators* (2017),
129--194.

Used as a general hyperbolic-surface reference for transfer-operator
realizations of Selberg zeta functions beyond the scalar modular example.

### Venkov and Zograf (DOI: 10.1070/IM1983v021n03ABEH001800)

A. B. Venkov and P. G. Zograf, *On analogues of the Artin factorization
formulas in the spectral theory of automorphic functions connected with
induced representations of Fuchsian groups*, Mathematics of the USSR-Izvestiya
21 (1983), 435--443.

Used for the induced-representation/finite-cover identity

\[
Z_{\Gamma_{\rm com}}(s)
=Z_{\Gamma}\!\left(s,
\operatorname{Ind}_{\Gamma_{\rm com}}^{\Gamma}\mathbf 1\right).
\]

Because the quotient is abelian, the regular representation also gives the
six-character factorization

\[
Z_{\Gamma_{\rm com}}(s)
=\prod_{\chi\in\widehat{C_6}}Z_\Gamma(s,\chi).
\]

This factorization is within one induced-representation determinant ledger; it
does not authorize multiplication by unrelated scattering or xi factors.

### Balslev and Venkov (DOI: 10.1007/s000390050063)

E. Balslev and A. Venkov, *The Weyl Law for Subgroups of the Modular Group*,
Geometric and Functional Analysis 8 (1998), 437--465.

Used for the quadratic spectral counting scale for finite-index modular
subgroups. For the present cover, the hyperbolic area is

\[
[\Gamma:\Gamma_{\rm com}]\,\frac{\pi}{3}=2\pi.
\]

The project obstruction only needs the weaker consequence that modular Maass
cusp forms lift to the cover, yielding at least an \(\Omega(T^2)\) family of
spectral zeros.

### Borthwick (arXiv:1305.4850v2)

David Borthwick, *Distribution of resonances for hyperbolic surfaces*.

Used for:

- the link between the Selberg-zeta divisor and the resonance set;
- the finite-area two-sided resonance Weyl law
  \(\#\{\zeta:|\Im\zeta|\le T\}\sim
  \operatorname{vol}(X)T^2/(2\pi)\).

For the area-\(2\pi\) cover, this has main term \(T^2\). The exact split among
cuspidal eigenvalues, scattering resonances, topological zeros, and cusp poles
is not needed for the Route-A rejection.

## Separate object: scattering determinant

The modular scattering determinant is not \(D_{\rm ab}\). With common
normalizations it contains a ratio of completed zeta factors of the schematic
form

\[
\varphi(s)\sim\frac{\Lambda(2s-1)}{\Lambda(2s)},
\]

possibly accompanied by convention-dependent elementary factors. It has both
zeros and poles and is a different determinant data type. Its arithmetic ratio
cannot be used to cancel or replace the Selberg divisor unless a single exact
physical determinant identity is proved first.

## Claim boundary

The sources establish a natural countable-branch nuclear determinant and its
finite-cover Selberg interpretation. They do not establish any rational-prime
orbit correspondence, von-Mangoldt weight, completed-xi divisor identity, or
Hilbert--Polya realization.
