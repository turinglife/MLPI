---
title: Lecture 1 - Mathematics of Metrics
shorttitle: Lecture 1
---

# Metrics #

- Measurement of *distances* or *deviation* lies at the heart of many learning problems.
- Given an arbitrary set $\Omega$, a real-valued function $d: \Omega \times \Omega \mapsto \mathbb{R}$ is called a *metric*, if it satisfies:
	- *(non-negativity)* $d(x, y) \ge 0, \ \forall x, y \in \Omega$
	- *(coincidence axiom)* $d(x, y) = 0 \Leftrightarrow x = y$
	- *(symmetry)* $d(x, y) = d(y, x), \ \forall x, y \in \Omega$
	- *(triangle inequality)* $d(x, y) + d(y, z) \ge d(x, z), \ \forall, x, y, z \in \Omega$
- A set $\Omega$ together with a metric $d$ defined thereon is called a *metric space*, denoted by $(\Omega, d)$.

---

# Metrics Defines Topology #

- *Topological space* is a more general concept than *metric space*
	- With *metrics*, *topological concepts* can be defined in a more intuitive way

. . .

- *Open ball* of radius $r$: $B_\epsilon(x) = \{y \in \Omega: d(y, x) < \epsilon\}$
- Consider a metric space $(\Omega, d)$, and a subset $S \subset \Omega$:
	- $S$ is called an *open set*, if $\forall x \in S, \exists \epsilon > 0: B_\epsilon(x) \subset \Omega$
	- $S$ is called a *closed set*, if $\Omega - S$ is open
	- $x$ is called a *boundary point* of $S$, if for any $\epsilon > 0$, $B_\epsilon(x)$ overlaps with both $S$ and $\Omega - S$.
	- The *boundary* of $S$, denoted by $\partial S$, is the set of all *boundary points* of $S$.

. . .

- Useful properties
	- $S$ is *open* if $\partial S \cap S = \emptyset$.
	- $S$ is *closed* if $\partial S \subset S$.
	- Unions of open sets are open
	- Intersections of closed sets are closed

---

# Questions #

- Consider an arbitrary metric space $(\Omega, d)$, are $\Omega$ and $\emptyset$ open or closed?

. . .

- Let $(\Omega, d)$ be a finite metric space and $x \in \Omega$, is $\{x\}$ open or closed?

. . .

- Consider *Euclidean space* $\mathbb{R}^2$ and $S = (a, b) \times \{0\}$, is $S$ open or closed? what is $\partial S$?

---

# Closure #

- Let $S$ be a subset of a metric space $(\Omega, d)$, then the *(topological) closure* of $S$, denoted by $\mathrm{cl}(S)$, is defined to be the *minimum* closed set that contains $S$, namely the intersection of all closed sets that contain $S$.
- $S$ is closed iff $\mathrm{cl}(S) = S$.
- $\mathrm{cl}(S) = S \cup \partial S$. 
- Examples:
	- $\mathrm{cl}((a, b)) = [a, b]$
	- $\mathrm{cl}(B_\epsilon(x)) = \{y \in \Omega: d(x, y) \le \epsilon\}$.

---

# Limits #

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

- A metric space $(\Omega, d)$ is called a *complete metric space* if *all Cauchy sequences are convergent*.
	- $\mathbb{R}$ is complete, but $\mathbb{Q}$ is *not*.
	- $\mathbb{R}$ can be constructed by *completing* $\mathbb{Q}$.

. . .

- **Question:** Is the integer space $\mathbb{Z}$ with $d(x, y) \triangleq |x - y|$ a *complete metric space*? 

---








