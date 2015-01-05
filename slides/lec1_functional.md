# Norms and Banach Spaces #

- Things become much more interesting when *vector spaces* meet with *metrics*.

. . .

- Consider a *vector space* $\Omega$, a function $\|\cdot\|: \Omega \mapsto \mathbb{R}$ is called a *norm* if:
    - $\|\mathbf{x}\| \ge 0, \forall \mathbf{x} \in \Omega$
    - $\|\mathbf{x}\| = 0$ iff $x = 0$. ($\|\cdot\|$ is called a *seminorm* without this)
    - $\|\alpha \mathbf{x}\| = |\alpha| \cdot \|\mathbf{x}\|, \ \forall \alpha \in \mathbb{R}, \mathbf{x} \in \Omega$.
    - $\|\mathbf{x} + \mathbf{y}\| \le \|\mathbf{x}\| + \|\mathbf{y}\|, \ \forall \mathbf{x}, \mathbf{y} \in \Omega$.
- A vector space together with a norm, as $(\Omega, \|\cdot\|)$, is called a *normed space*. 
    - A *normed space* is always a *metric space*, where the *norm* induces a *metric* as $d(\mathbf{x}, \mathbf{y}) = \|\mathbf{x} - \mathbf{y}\|$.
- A *complete normed space* is called a *Banach space*.

---

# Properties of Norms #

- The *norm* function $x \mapsto \|x\|$ is Lipschitz continuous:
    
    $$\left| \|x\| - \|y\| \right| \le \|x - y\|$$

- The metric $d$ induced by the norm: 
    - *translation-invariance*: $d(x+a, y+a) = d(x, y)$
    - $d(\alpha x, \alpha y) = |\alpha| \cdot d(x, y)$

---

# Examples of Norms #

Consider a real vector space $\mathbb{R}^m$. For each $p \ge 1$, we can define $L_p$-norm as:

$$\| \mathbf{x} \|_p \triangleq \left( \sum_{i=1}^m |x^{(i)}|^p \right)^{1/p}$$

It can be easily verified that $\|\cdot\|_p$ is a *norm*. When $p$ is set to $\infty$, $L_\infty$-norm is still a *norm*, defined as

$$\| \mathbf{x} \|_\infty \triangleq \max_{i=1}^m |x^{(i)}|$$

We will extend these norms to the *space of functions*.

---

# Convergence of Vectors and Basis #

- Let $x_1, x_2, \ldots$ be a sequence of vectors in a Banach space, we say $(x_n)$ *converges* to $x$ if $\|x_n - x\| \rightarrow 0$ as $n \rightarrow \infty$.
	- This is sometimes called *convergence in norm*.

- Consider an infinite series $s = x_1 + x_2 + \cdots$ in a Banach space, then $s$ is said to be *absolutely convergent* if $\|x_1\| + \|x_2\| + \cdots$ converges.

. . .

- Let $(e_n)$ be a sequence in a Banach space $\Omega$, it is called a *(Schauder) basis* of $\Omega$ if for each $x \in \Omega$, there exists a unique sequence of real values $(\alpha_n)$ such that 

	$$\|x - (\alpha_1 e_1 + \cdots + \alpha_n e_n)\| \rightarrow 0, \quad \text{ as } n \rightarrow 0$$ 

- Not every Banach space has a Schauder basis.

---

# Inner Products and Hilbert Spaces #

- An inner product on a real vector space $\Omega$ is a mapping $(x, y) \mapsto \langle x, y \rangle$ that satisfies:
    - $\langle x, x \rangle \ge 0$
    - $\langle x, x \rangle = 0$ iff $x = 0$
    - *(symmetry)* $\langle x, y \rangle = \langle y, x \rangle$
    - *(bilinearity)* $\langle \alpha x + \beta y, z \rangle = \alpha \langle x, z \rangle + \beta \langle y, z \rangle$
- A vector space together with an inner product is called an *inner product space*.
- An *inner product space* is always a *normed space*, where the *norm* is induced by the *inner product*, as $\|x\| = \sqrt{\langle x, x \rangle}$.
- A *complete inner product space* is called a *Hilbert space*.
    - A *Hilbert space* is always a *Banach space*.
- $\mathbb{R}^m$ is a *Hilbert space* with the inner product defined by $\langle \mathbf{x}, \mathbf{y} \rangle = \sum_{i=1}^m x^{(i)} y^{(i)}$, which induces the $L_2$-norm and *Euclidean metric*.

---

# Properties of Inner Products #

- *(Parallelogram equality)* $\|x + y\|^2 + \|x - y\|^2 = \|x\|^2 + \|y\|^2$ -- this only holds for norms induced by inner products.
- *(Cauchy–Schwarz inequality)* $\left|\langle x, y \rangle\right| \le \|x\| \cdot \|y\|$, or equivalently, $\left(\langle x, y \rangle\right)^2 \le \langle x, x \rangle \cdot \langle y, y \rangle$.
- *(Continuity)* if $x_n \rightarrow x$ and $y_n \rightarrow y$, then $\langle x_n, y_n \rangle \rightarrow \langle x, y \rangle$.

---

# Spaces #

\includegraphics[width=1.0\textwidth]{imgs/spaces.pdf}

---

# Linear Operators and Functionals #

- Let $X$ and $Y$ be two linear spaces, a function: $T: X \rightarrow Y$ is called a *linear operator* if it preserves *linear dependency*, that is, 

	$$T(\alpha x_1 + \beta x_2) = \alpha T(x_1) + \beta T(x_2), \ \forall x_1, x_2 \in X, \alpha, \beta \in \mathbb{R}$$
	
	In particular, when $Y$ is $\mathbb{R}$, $T$ is called a *linear functional*.

- The set $\mathscr{N}(T) \triangleq \{x: T(x) = 0\}$ is a subspace of $X$, called the *null space* of $T$.

---

# Bounded Operators #

Let $X$ and $Y$ be normed spaces, and $T: X \rightarrow Y$ be a linear operator:

- $T$ is said to be *bounded*, if $\exists c > 0, \forall x \in X, \|Tx\| \le c \|x\|$.
- The *(operator) norm* of $T$ is defined as

	$$\|T\|_{op} \triangleq \sup_{x \ne 0} \frac{\|Tx\|}{\|x\|}$$ 
	
	Hence, $\|Tx\| \le \|T\|_{op} \|x\|$ always holds.
- Given a linear operator $T$, the following statements are equivalent:
	- $T$ is bounded
	- $T$ is continuous
	- $\|T\|$ is finite 
- All linear operators with finite dimensional domain are bounded.

---

# Space of Bounded Operators and Dual Space #

- All *bounded* operators $T: X \rightarrow Y$ form a *normed space*, denoted by $B(X, Y)$. 
	- When $Y$ is a Banach space, $B(X, Y)$ is a Banach space.
- All *bounded* functionals $f: X \rightarrow \mathbb{R}$ form a *normed space*, called the *dual space* of $X$, denoted by $X^*$, where the norm is called the *dual norm*, defined as:

	$$\|f\|_* = \sup_{x \ne 0} \frac{|f(x)|}{\|x\|}$$
	
	Note $X^*$ is always a Banach space, no matter whether $X$ is or not.
	
- The dual space of $\mathbb{R}^n$ is isomorphic to $\mathbb{R}^n$.

---

# Function Space and Uniform Norm #

- The set of all continuous real valued functions defined on a *compact space* $\Omega$ forms a normed vector space, denoted by $C(\Omega)$, where the norm is defined by $\|x\| = \sup_{v \in S} x(v)$, which is called the *uniform norm* (or *Chebyshev norm*).
	- When $\Omega$ is a closed interval $[a, b]$, $C(\Omega)$ is often written as $C[a, b]$.
- Given any compact space $\Omega$, $C(\Omega)$ is a *Banach space*.
- There are other ways to define norms of functions, which we will discuss later.

. . .

- **Question:** Let $C'[a, b]$ be a subspace of $C[a, b]$ that comprises all *continuously differentiable functions* on $[a, b]$. Let $m = (a + b) / 2$. We define a functional as $f_m: x \mapsto x'(m)$ which takes the derivative at $m$. 
	- Is $f_m$ a linear functional?
	- Is $f_m$ bounded?

---

# Orthogonality and Projection #

Let $\Omega$ be a Hilbert space:

- $x, y \in \Omega$ are said to be *orthogonal* to each other, denoted by $x \perp y$, if $\langle x, y \rangle = 0$.
- A subset $M \subset \Omega$ is called an *orthogonal set* if elements of $M$ are mutually orthogonal. Moreover, if each element has a unit norm, then $M$ is called an *orthonormal set*.
- *(Pythagorean theorem)* $x \perp y \Leftrightarrow \|x\|^2 + \|y\|^2 = \|x + y\|^2$.

. . .

- Let $x \in \Omega$ and $S \subset \Omega$, then the *distance* between $x$ and $S$ is defined to be $d(x, S) \triangleq \inf_{y \in S} d(x, y)$.

- Let $S$ be a non-empty convex closed subset of $\Omega$. Then there exists a unique element $y_* \in S$ such that $d(x, y_*) = d(x, S)$. This element $y_*$ is called the *projection* of $x$ onto $S$, denoted by $\mathrm{proj}_S(x)$.

...

- **Question:** Why does $S$ need to be closed and convex?

---

# Orthogonality and Projection (cont'd) #

Let $\Omega$ be a Hilbert space and $S$ be a subspace of $\Omega$:

- Given $x \in \Omega$ and $y = \mathrm{proj}_S(x)$, then $x - y \perp S$, meaning that $x - y \perp z, \forall z \in S$.

Let $P = \mathrm{proj}_S$ be a projection, where $S$ is non-empty:

- $P$ is a bounded operator with $\|P\|_{op} = 1$.
- $P$ is *idempotent*, namely, $P^2 = P$, *i.e.* $P^2 x = P(Px) = Px$.

---

# Direct Sum and Orthogonal Complement #

- A vector space $Z$ is said to be the *direct sum* of two subspaces $X$ and $Y$, denoted by $X \oplus Y$, if each $z \in Z$ can be expressed *uniquely* as $x + y$ with $x \in X$ and $y \in Y$. 

- Let $S$ be a subspace of $\Omega$. The *orthogonal complement* of $S$, denoted by $S^\perp$, is defined to be $S^\perp \triangleq \{y \in \Omega: y \perp S\}$. 
	- $S^\perp$ is also a subspace of $\Omega$.

- *(Projection theorem)* $S \oplus S^\perp = \Omega$
	- Each $x \in \Omega$ can be expressed uniquely as $x = y + z$ with $y \in S$ and $z \in S^\perp$. Particularly, we have $y = \mathrm{proj}_S(x)$ and $z = x - y$. 
	
- $S^{\perp \perp} = S$.

---

# Orthonormal Basis of Hilbert Space #

- Let $\Omega$ be a Hilbert space, a subset $M \subset \Omega$ is called a *total subset* of $\Omega$ if $cl(\mathrm{span}(M)) = \Omega$.

- $M$ is a *total subset* of $\Omega$ if and only if $x \perp M \Rightarrow x = 0$.

- A *total orthonormal set* is called an *orthonormal basis*.

- *(Parseval theorem)* An orthonormal sequence $(e_k)$ is *total* if and only if

	$$\sum_k \left|\langle x, e_k \rangle\right|^2 = \|x\|^2, \quad \forall x \in \Omega$$
	
	In this case, each $x \in \Omega$ can be uniquely expressed as
	
	$$x = \sum_k \langle x, e_k \rangle e_k$$
	
	Here, the value $\langle x, e_k \rangle$ is sometimes called the *Fourier coefficients*.

. . .

- **Question:** Why $\mathrm{span}(M) \ne \Omega$ in general?

---

# Representation of Functionals #

- *(Riesz's theorem)* Every *bounded* linear functional $f$ on a Hilbert space $\Omega$ can be represented in terms of inner product, namely, $f(x) = \langle x, z \rangle$, where $z$ is uniquely determined by $f$ and has $\|z\| = \|f\|_*$. 

. . .

- **Question:** How can you find $z$ given $f$?

. . .

- For a Hilbert space with a countable orthonormal basis $(e_k)$, we have

	$$z = \sum_k f(e_k) e_k$$

---

# Bilinear Forms #

- Let $X$ and $Y$ be Hilbert spaces. Then the function $h: X \times Y \rightarrow \mathbb{R}$ is called a *bilinear form* if it is linear *w.r.t* each argument with the other fixed.

- Let $h$ be a *bilinear form* on $X \times Y$, then $h$ is said to be *bounded* if there exists $c > 0$ with $|h(x, y)| \le c \|x\| \|y\|, \forall x \in X, y \in Y$. In such case, the norm of $h$ is defined to be 
	
	$$\|h\| = \sup_{x \ne 0, y \ne 0} \frac{|h(x,y)|}{\|x\|\|y\|}$$

	Hence, we always have $|h(x,y)| \le \|h\|\|x\|\|y\|$.
	
- *(Generalized Riesz's theorem)* Let $h$ be a *bounded* bilinear form on $X \times Y$. Then $h$ has a representation as $h(x, y) = \langle Sx, y \rangle$, where $S$ is a bounded linear operator uniquely determined by $h$ and have $\|S\|_{op} = \|h\|$.


