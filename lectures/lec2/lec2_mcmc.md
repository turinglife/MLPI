# Markov Chain Monte Carlo #

*(Markov Chain Monte Carlo)*: To sample from a *target distribution* $\pi$:

1. We first construct a Markov chain with *transition probability kernel* $P$ such that $\pi P = \pi$. 
2. Then we simulate the chain, usually in two stages:
	- *(Burning stage)* simulate the chain and ignore all samples, until it gets close enough to the *equilibrium distribution*
	- *(Sampling stage)* collect samples $x_1, \ldots, x_n$ from a subsampled chain $P^m$ or $P_q$.
3. Approximate the expectation of the function $f$ of interest using the sample mean, as
		
	$$E_\pi[f] \simeq \frac{1}{n} f(x_i).$$

---

# Detailed Balance and Reversible Chains #

Most Markov chains in MCMC practice falls in a special family: *reversible chains*

- A distribution $\pi$ over a *countable space* is said to be *in detailed balance* with $P$ if $\pi(x) P(x, y) = \pi(y) P(y, x)$. 
	- *Detailed balance* implies *invariance*.
	- The converse is not true. 

. . .

- An irreducible Markov chain with TPM $P$ and an invariant distribution $\pi$ is called *reversible* if $\pi$ is in *detailed balance* with $P$. 

- Consider an irreducible Markov chain $(X_t)$ $Markov(\pi, P)$ where $\pi$ is in *detailed balance* with $P$, then

	$$\Pr(X_0 = x_0, \ldots, X_n = x_n) = \Pr(X_0 = x_n, \ldots, X_n = x_0).$$

---

# Reversible Chains on General Spaces #

Over a general measurable space $(\Omega, \mathcal{S})$:

- A stochastic kernel $P$ is called *reversible* *w.r.t.* a probability measure $\pi$ if 

	$$\int \int f(x, y) \pi(dx) P(x, dy) = \int \int f(y, x) \pi(dx) P(x, dy)$$
	
	for any bounded measurable function $f: \Omega \times \Omega \rightarrow \mathbb{R}$.

- If $P$ is *reversible* *w.r.t.* $\pi$, then $\pi$ is an *invariant* to $P$.

# Reversible Chains on General Spaces (cont'd) #

- Suppose both $\pi$ and $P_x$ are absolutely continuous *w.r.t.* a base measure $\mu$, that is, $\pi(dx) = \pi(x) \mu(dx)$ and $P(x, dy) = P_x(dy) = p_x(y) \mu(dy)$, then the chain is *reversible* if and only if

	$$\pi(x) p_x(y) = \pi(y) p_y(x), \ a.e.$$

	which is called the *detailed balance*. 

- More generally, if $P(x, dy) = m(x) I_x(dy) + p_x(y) \mu(dy)$, where $I_x(A) = 1(x \in A)$, then the chain is *reversible* if 

	$$\pi(x) p_x(y) = \pi(y) p_y(x), \ a.e.$$

---

# Metropolis-Hastings: An Overview #

- In MCMC practice, the *target distribution* $\pi$ is usually known up to an *unnormalized density* $h$, such that $\pi(x) = h(x) / c$, and the *normalizing constant* $c$ is often intractable to compute. 

. . .

- The *Metropolis-Hastings algorithm (M-H algorithm)* is a classical and popular approach to MCMC sampling. It works as follows:
	1. It is associated with a *proposal kernel* $Q$.
	2. At each iteration, a *candidate* is generated from $Q_x$ given the current state $x$.
	3. With a certain acceptance ratio, which depends on both $Q$ and $h$, the *candidate* is *accepted*. 
	
- The acceptance ratio is determined in a way that maintains *detailed balance*, so the resultant chain is *reversible* *w.r.t.* $\pi$.

. . .
	
- Many sampling algorithms, notably *Gibbs sampling* and *Slice sampling*, are special cases of the M-H algorithm.

---

# Metropolis Algorithm #

- The *Metropolis algorithm* is a precursor (and a special case) of the M-H algorithm, which requires the designer to provide a *symmetric kernel* $Q$, *i.e.* $q_x(y) = q_y(x)$, where $q_x$ is the density of $Q_x$. 
	- **Note:** $\pi$ is not necessarily invariant to $Q$
	- *Gaussian random walk* is a symmetric kernel.

. . .

- At each iteration, with current state $x$:
	1. Generate a candidate $y$ from $Q_x$
	2. Accept the candidate with *acceptance ratio* $a(x, y) = \min\{h(y) / h(x), 1\}$.

. . .

- The *Metropolis update* satisfies *detailed balance*. Why?

---

# Metropolis-Hastings Algorithm #

- The *Metropolis-Hastings algorithm* requires a *proposal kernel* $Q$, 
	- $Q$ is NOT necessarily *symmetric* and does NOT necessarily admit $\pi$ as an invariant measure.

. . .

- At each iteration, with current status $x$:
	- Generate a candidate $y$ from $Q_x$
	- Accept the candidate with *acceptance ratio* $a(x, y) = \min\{r(x, y), 1\}$, with 

		$$r(x, y) = \frac{h(y)q_y(x)}{h(x)q_x(y)}.$$
		
. . .

- The *Metropolis-Hastings update* satisfies *detailed balance*. Why?

---

# Gibbs Sampling #

- The *Gibbs sampler* was introduced by Geman and Geman (1984) from sampling from a Markov random field over images, and popularized by Gelfand and Smith (1990). 

- Each state $x$ is comprised of multiple components $(x^{(1)}, \ldots, x^{(n)})$. 

- At each iteration, following a permutation $\sigma$ over $(1, \ldots, n)$:
	- For $i = 1, \ldots, n$, let $j = \sigma(i)$, update $x$ by re-drawing $x^{(j)}$ conditioned on all other components:
	
		$$x^{(j)} \sim \pi_{/j}\left(\cdot | x^{(1)}, \ldots, x^{(j-1)}, x^{(j+1)}, \ldots, x^{(n)}\right).$$
	- At each iteration, one can use either a *random scan* or a *fixed scan*.
	- Different schedules can be used at different iterations to scan the components. 

- The *Gibbs update* is a special case of *M-H update*, and thus satisfies *detailed-balance*. Why?

---

# Combination of MCMC Kernels #

Let $K_1, \ldots, K_m$ be *stochastic kernels* with the same invariant probability measure $\pi$:

- *(Mixture of kernels)*: Let $q$ be a probability vector, then $K := \sum_{i=1}^m q_i K_i$ remains a *stochastic kernel* with invariant probability measure $\pi$. 
	- Furthermore, if $K_1, \ldots, K_m$ are all reversible, then $K$ is reversible.

. . .

- *(Composition of kernels)*: $K = K_m \circ \cdots \circ K_1$ is also a *stochastic kernel* with invariant probability measure $\pi$.
	- **Note:** $K$ is generally not *reversible* even when $K_1, \ldots, K_m$ are all reversible, except when $K_1 = \cdots = K_m$. 





