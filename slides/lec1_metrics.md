---
title: Lecture 1 - Metrics and Kernels
shorttitle: Lecture 1
---

# Distances in Machine Learning #

- *Distances* or *similarities* lies at the heart of many learning problems.
- A lot of models are formulated based on a simple principle

	> Similar inputs should yield similar outputs
	
- A classical examples based on this principle is *k-nearest neighbor*.

- Affinity-based regularization:

	$$\sum_{i=1}^n loss(x, f(x; \theta)) + \sum_{i,j} w_{ij} \left(f(x_i; \theta) - f(x_j; \theta)\right)^2$$

	Here, $w_{ij}$ is set to a higher value when $x_i$ and $x_j$ are closer to each other.
	
---

# Kernels in Machine Learning #

- Another way to characterize *relations* between samples is to use *kernels*
- Consider a simple case where samples reside in a vector space $\mathbb{R}^m$. A popular way to make predictions is to use a *linear functional* (with bias), as

	$$f(\mathbf{x}) = \boldsymbol{\theta}^T \mathbf{x} + b$$
	
. . .

- What if the samples are not vectors?
- A natural idea: use a *feature map* $\boldsymbol{\varphi}$ to map the samples to a vector space, then the predictor can be written as

	$$f(\mathbf{x}) = \boldsymbol{\theta}^T \boldsymbol{\varphi}(x) + b$$

---

# Kernels in Machine Learning (cont'd) #

- Given a set of *training samples* $x_1, \ldots, x_n$. In many learning framework, the optimal solution to $\boldsymbol{\theta}$ must be written as a linear combination of *training features*, as

	$$\boldsymbol{\theta} = \sum_{i=1}^n \alpha_i \boldsymbol{\varphi}(x_i)$$

	Then the predictor can be rewritten as

	$$f(\mathbf{x}) = \sum_{i=1}^n \alpha_i \boldsymbol{\varphi}(x_i)^T \boldsymbol{\varphi}(x_j) + b$$

- In practice, you may *directly* compute the dot product of features without explicitly constructing the *feature map*, as

	$$K(x_i, x_j) = \boldsymbol{\varphi}(x_i)^T \boldsymbol{\varphi}(x_j)$$

	This function $K$ is called a *kernel*.  

---

# Big Picture #

- *Metrics* and *kernels* are two most important ways in machine learning to characterize the relations between samples.

- In this lecture, we will elaborate on the theory behind *metrics* and *kernels*, as well as their connections.


- In many nontrivial cases, the feature maps would map each sample to a *function* rather than a *finite-dimensional vector*. 
	- In such cases, we are faced with a question: *how to compute metrics or kernels between functions?*
	- We are going to explore this in this lecture. 

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

# Examples of Norms #

Consider a real vector space $\mathbb{R}^m$. For each $p \ge 1$, we can define $L_p$-norm as:

$$\| \mathbf{x} \|_p \triangleq \left( \sum_{i=1}^m |x^{(i)}|^p \right)^{1/p}$$

It can be easily verified that $\|\cdot\|_p$ is a *norm*. When $p$ is set to $\infty$, $L_\infty$-norm is still a *norm*, defined as

$$\| \mathbf{x} \|_\infty \triangleq \max_{i=1}^m |x^{(i)}|$$

We will extend these norms to the *space of functions*.

---

# Inner Products and Hilbert Spaces #






