# Metrics #

- Measurement of *distances* or *deviation* lies at the heart of many learning problems.
- Given an arbitrary set $\Omega$, a real-valued function $d: \Omega \times \Omega \mapsto \mathbb{R}$ is called a *metric*, if it satisfies:
    - *(non-negativity)* $d(x, y) \ge 0, \ \forall x, y \in \Omega$
    - *(coincidence axiom)* $d(x, y) = 0 \Leftrightarrow x = y$
    - *(symmetry)* $d(x, y) = d(y, x), \ \forall x, y \in \Omega$
    - *(triangle inequality)* $d(x, y) + d(y, z) \ge d(x, z), \ \forall, x, y, z \in \Omega$
- The *triangle inequality* can be further generalized:
    
    $$d(x_1, x_n) \le d(x_1, x_2) + d(x_2, x_3) + \cdots + d(x_{n-1}, x_n).$$   
- A set $\Omega$ together with a metric $d$ defined thereon is called a *metric space*, denoted by $(\Omega, d)$.

---

# Examples of Metrics #

- *Euclidean metric* $d_{euc}: \mathbb{R}^m \times \mathbb{R}^m \rightarrow \mathbb{R}$:

    $$d_{euc}(\mathbf{x}, \mathbf{y}) \triangleq \sqrt{\sum_{i=1}^m 
    \left( x^{(i)} - y^{(i)} \right)^2}$$

- *Rectilinear metric* $d_{rec}:\mathbb{R}^m \times \mathbb{R}^m \rightarrow \mathbb{R}$:

    $$d_{rec}(\mathbf{x}, \mathbf{y}) \triangleq \sum_{i=1}^m 
    \left| x^{(i)} - y^{(i)} \right|$$ 

. . .

- One can define a metric over an arbitrary set $S$ through an *injective map* $f: S \rightarrow \Omega$ to a metric space $(\Omega, d_\Omega)$:

    $$d_S(x, y) = d_\Omega(f(x), f(y)), \ \forall x, y \in S$$

    It can be easily verified that $d_S$ is a metric on $S$.

---

# Metrics Defines Topology #

- *Topological space* is a more general concept than *metric space*
    - With *metrics*, *topological concepts* can be defined in a more intuitive way

. . .

- *Open ball* of radius $r$: $B_\epsilon(x) = \{y \in \Omega: d(y, x) < \epsilon\}$

- $x$ is called an *interior point* of $S$ if there exists $\epsilon > 0$ such that $B_\epsilon(x) \subset S$. The *interior* of $S$, denoted by $S^\circ$ or $\mathrm{int}(S)$, is the set of all interior points of $S$ is called.

- $x$ is called a *boundary point* of $S$, if for any $\epsilon > 0$, $B_\epsilon(x)$ overlaps with both $S$ and $\Omega - S$. The *boundary* of $S$, denoted by $\partial S$, is the set of all *boundary points* of $S$.

. . .

- Consider a metric space $(\Omega, d)$, and a subset $S \subset \Omega$:
    - $S$ is called an *open set*, if $S = S^\circ$
    - $S$ is called a *closed set*, if $\Omega - S$ is open


# Properties of Open and Closed Sets #

- $S$ is *open* if $\partial S \cap S = \emptyset$.
- $S$ is *closed* if $\partial S \subset S$.
- The union of any collections of open sets is open.
- The intersection of *finitely many* open sets is open. 
- The intersection of any collections of closed sets is closed.
- The union of *finitely many* closed sets is closed.

---

# Questions #

- Consider an arbitrary metric space $(\Omega, d)$, are $\Omega$ and $\emptyset$ open or closed?

. . .

- Let $(\Omega, d)$ be a finite metric space and $x \in \Omega$, is $\{x\}$ open or closed?

. . .

- Consider *Euclidean space* $\mathbb{R}^2$ and $S = (a, b) \times \{0\}$, is $S$ open or closed? what is $\partial S$?

---

# Closure #

- Let $S$ be a subset of a metric space $(\Omega, d)$, then the *(topological) closure* of $S$, denoted by $\bar{S}$ or $\mathrm{cl}(S)$, is defined to be the *minimum* closed set that contains $S$, namely the intersection of all closed sets that contain $S$.
- $S$ is closed if and only if $\bar{S} = S$.
- $\bar{S} = S \cup \partial S$. 
- $\partial S = \bar{S} - S^\circ$.
- Examples:
    - $\mathrm{cl}((a, b)) = [a, b]$
    - $\mathrm{cl}(B_\epsilon(x)) = \{y \in \Omega: d(x, y) \le \epsilon\}$.

---

# Convergence and Cauchy Sequences #

- Let $x_1, x_2, \ldots$ be a sequence in a metric space $(\Omega, d)$, then $x_* \in \Omega$ is called a *limit* of this sequence if
    
    $$\forall \epsilon > 0, \ \exists N: \forall m > N, d(x_m, x_*) < \epsilon.$$

- A sequence is said to be *convergent* if it has a *limit*.
- The *limit* of a convergent sequence is unique.

. . .

- A sequence $x_1, x_2, \ldots$ is called a *Cauchy sequence* if 
    
    $$\forall \epsilon > 0, \ \exists N: \forall m, n > N, d(x_m, x_n) < \epsilon.$$ 

. . .

- A *convergent sequence* must be a *Cauchy sequence*
- **Question:** Is a *Cauchy sequence* always convergent?

---

# Complete Metric Space #

- Consider a real valued sequence $x_n = \left(1 + \frac{1}{n}\right)^n$. 
    - We have learned in Calculus that $x_n \rightarrow e$ as $n \rightarrow \infty$.

. . .

- Note that $(x_n)$ is a rational sequence. Is this sequence convergent in the *rational space* $\mathbb{Q}$?

. . .

- **Convergence is not an intrinsic property of a sequence, which also depends on the space in which the sequence lies.**
- A metric space $(\Omega, d)$ is called a *complete metric space* if *every Cauchy sequence converges*.
    - $\mathbb{R}$ is complete, but $\mathbb{Q}$ is *not*.
    - $\mathbb{R}$ can be constructed by *completing* $\mathbb{Q}$.

. . .

- **Question:** Is the integer space $\mathbb{Z}$ with $d(x, y) \triangleq |x - y|$ a *complete metric space*? 

---

# Closed, Bounded, and Convergent #

Let $S$ be a subset of a complete metric space $(\Omega, d)$:

- Being *closed* means *"containing all the limits"*:
    - Let $(x_n)$ be a sequence in $S$ and $x_n \rightarrow x$, then $x \in \bar{S}$
    - $S$ is *closed* if and only if $S$ is *complete*, meaning *all convergent sequences in $S$ converge within $S$*. 

. . .

- The *diameter* of $S$, denoted by $\delta(S)$, is defined to be the largest distance between points in $S$, as

    $$\delta(S) \triangleq \sup_{x,y \in S} d(x, y).$$
    
- $S$ is said to be bounded if $\delta(S) < \infty$.

---

# Compactness #

- In elementary Calculus, we learned that *"every bounded sequence in $\mathbb{R}^n$ has a convergent subsequence"*. 
    - Does this hold in general metric spaces?

. . .

- Consider a metric space $(\Omega, d)$. Then $\Omega$ is said to be *compact* if any open cover of $\Omega$ has a finite subcover.

. . .

- A metric space $(\Omega, d)$ is *compact* if and only if either of the following holds:
    - $\Omega$ is *complete* and *totally bounded*, namely, for every $\epsilon > 0$, there exists a finite cover of $\Omega$ by $\epsilon$-balls.
    - $\Omega$ is *sequentially compact*, *i.e.* every sequence in $\Omega$ has a convergent subsequence.

. . .

- Compact sets are always *closed and bounded*.
    - But, the converse is *generally false*.
    - $S \subset \mathbb{R}^m$ is compact *if and only if* $S$ is bounded and closed.

---

# Continuous Function #

- Let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces. A function $f: X \rightarrow Y$ is called a *continuous function*, if $f^{-1}(V) = \{x \in X: f(x) \in V\}$ is open whenever $V \subset Y$ is open.

- $f$ is continuous, if and only if either of the following holds:
    - (*Weierstrass definition*) $\forall \epsilon > 0, \forall x \in X, \exists \delta > 0, d_X(x, x') < \delta \Rightarrow d_Y(f(x), f(x')) < \epsilon$
    - (*Sequential continuity*) $f(x_n) \rightarrow f(x)$ whenever $x_n \rightarrow x$.

. . .

- $f$ is called *uniformly continuous*, if $\forall \epsilon > 0, \exists \delta > 0, \forall x, x' \in X,  d_X(x, x') < \delta \Rightarrow d_Y(f(x), f(x')) < \epsilon$.

- $f$ is called *Lipschitz continuous*, if there exists $L > 0$, such that $d_Y(f(x), f(x')) \le L \cdot d_X(x, x'), \forall x, x' \in X$. Here, $L$ is called the *Lipschitz constant*.

- *Lipschitz continuous* $\Rightarrow$ *Uniform continuous* $\Rightarrow$ *Continuous*. 

---

# Continuous Function on Compact Domain #

- Let $f$ be a continuous function, then  $f(S) = \{f(x): x \in S\}$ is compact whenever $S$ is compact.
- Let $f: S \rightarrow \mathbb{R}$, then $f$ assumes *maximum* and *minimum* within $S$ when $S$ is compact.
- A *continuous function* is *uniformly continuous* over a compact domain.
- A *continuously differentiable function* is *Lipschitz continuous* over a compact domain.

---

# Contraction and Fixed Points #

Consider a function $f: \Omega \rightarrow \Omega$. 

- $x \in \Omega$ is called a *fixed point* of $f$ if $f(x) = x$.
	- Some functions may not have fixed points, *e.g.* $x \mapsto x + a$
	- Some functions may have infinitely many fixed points, *e.g.* $x \mapsto x$

- A function $f: \Omega \rightarrow \Omega$ defined on a metric space $(\Omega, d)$ is called a *contraction* if it is *Lipschitz continuous* with $L < 1$.

- *(Banach fixed point theorem)* Let $f$ be a *contraction* on a metric space $(\Omega, d)$, then $f$ has a unique fixed point.

- Let $f$ be a contraction with fixed point $x_*$. Consider an iterative sequence $x_0, x_1 = f(x_0), x_2 = f(x_1), \ldots$, then $x_n \rightarrow x_*$ as $n \rightarrow \infty$. 
	- *(Prior error estimate):* $d(x_m, x) \le \frac{L^m}{1 - L} d(x_0, x_1)$.
	- *(Posterior error estimate):* $d(x_m, x) \le \frac{L}{1 - L} d(x_{m-1}, x_m)$.




