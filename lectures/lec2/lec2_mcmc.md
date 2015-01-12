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

- Consider an irreducible Markov chain $(X_t)$ $Markov(\pi, P)$ where $\pi$ is in *detailed balance* with $P$, its *reversal* $(\hat{X}_t)$ is given by $(\pi, \hat{P})$ with $\hat{P}(x, y) \triangleq \pi(y) P(y, x) / \pi(x)$. Then

	$$\Pr(X_0 = x_0, \ldots, X_n = x_n) = \Pr(\hat{X}_0 = x_n, \ldots, \hat{X}_n = x_0).$$

---

# Reversible Chains on General Spaces #

Over a general measurable space $(\Omega, \mathcal{S})$:

- A stochastic kernel $P$ is called *reversible* *w.r.t.* a probability measure $\pi$ if 

	$$\int \int f(x, y) \pi(dx) P(x, dy) = \int \int f(y, x) \pi(dx) P(x, dy)$$
	
	for any bounded measurable function $f: \Omega \times \Omega \rightarrow \mathbb{R}$.

- Suppose both $\pi$ and $P_x$ are absolutely continuous *w.r.t.* a base measure $\mu$, that is, $\pi(dx) = \pi(x) \mu(dx)$ and $P(x, dy) = P_x(dy) = p_x(y) \mu(dy)$, then the chain is *reversible* if and only if

	$$\pi(x) p_x(y) = \pi(y) p_y(x),$$

	which is called the *detailed balance*.

- If $P$ is *reversible* *w.r.t.* $\pi$, then $\pi$ is an *invariant* to $P$.

---



