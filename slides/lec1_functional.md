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



