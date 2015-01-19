---
title: Lecture 3 - Advanced Sampling Techniques 
shorttitle: Lecture 3
---

# Overview #

- Partially Collapsed Sampling
- Parallel Tempering
- Slice Sampling
- Swendsen-Wang Algorithm
- Reversible Jump
- Particle Filtering

---

**Partially Collapsed Sampling**

---

# Motivating Example #

$$x_{ij} = g_i  + \varepsilon_{ij}, \quad i = 1, \ldots, k, j = 1, \ldots, n$$

with 

$$g_i \sim \mathcal{N}(\mu, \tau^2), \text{ and } \varepsilon_{ij} \sim \mathcal{N}(0, \sigma^2).$$

We want to sample from $p\left((g_i), (\mu_i) | (y_{ij})\right)$.

---

# Gibbs Sampling #

1. Draw $g_i \sim g_i | \mu_i, \mathbf{y}_i$ where $\mathbf{y}_i = (y_{i1}, \ldots, y_{in})$:

    $$p(g_i|\mu_i, \mathbf{y}_i) \sim 
    \mathcal{N}\left(
        \frac{n \sigma^{-2} \bar{y}_i + \tau^{-2} \mu_i}{n \sigma^{-2} + \tau^{-2}}, 
        \frac{1}{n \sigma^{-2} + \tau^{-2}}
    \right),$$

    with $\bar{y}_i = \frac{1}{n} \sum_{j=1}^n y_{ij}$.

2. Draw $\mu \sim \mu | \mathbf{g}, Y)$:

    $$p \left(\mu | \mathbf{g}, Y \right) \sim 
    \mathcal{N} \left(
        \frac{1}{k} \sum_{i=1}^k g_i,
        \frac{\tau^2}{k}
    \right).$$

. . .

3. How well can this sampler perform when $n \sigma^{-2} < \tau^{-2}$?

---

# Collapsed Gibbs Sampling #

- **Basic idea:** replace the original conditional distribution with a conditional distribution of a *marginal distribution*, often called a *reduced conditional distribution*.

- Consider the example above, we consider a *marginal distribution*:

	$$p(\mu | Y) = \int p(\mathbf{g}, \mu | Y) d\mathbf{g}.$$
	
---

# Collapsed Gibbs Sampling (cont'd) #

- Sampling procedure:
	1. Draw $\mu \sim p(\mu | Y)$, with $\mathbf{g}$ marginalized out, as:
		
		$$p(\mu | Y) \sim \mathcal{N} \left(
			\frac{1}{nk} \sum_{i=1}^k \sum_{j=1}^n y_{ij},
			\frac{n \tau^2 + \sigma^2}{nk}
		\right)$$

	2. Draw $g_i \sim g_i | \mu_i, \mathbf{y}_i$

. . .

- How well does this sampler perform ?

. . .

- Can we exchange the order of these two steps? Why?

---

# Basic Guidelines #

- Goal: allow partially collapsed steps while ensuring that the target stationary distribution is maintained.

. . .

- **Order of steps matters!**

- Generally, one can move components from *"being conditioned on"* to *"being sampled"*
	- neither alters the stationary distribution nor destroys the dependencies

- Removing draws from output or replacing outputs with intermediates would *change* the stationary distribution. 

- One may draw a variable multiple times in an iteration

---

# Lag-one Autocorrelation #

- Generally, a Markov chain $(X_t)$ mixes faster when it has lower *lag-one autocorrelation* $\rho(X_{t+1}, X_t)$, where $\rho$ is defined to be:

	$$\rho(Y, X) \triangleq \sup \mathrm{corr}(h(Y), g(X)) = \sup_{h: \mathrm{var}(h(Y)) = 1}
	\left( \mathrm{var}\left[ E[h(Y) | X] \right] \right)^{1/2}$$

. . .

- *(Rao-Blackwell Theorem)* Sampling more components in the first step of a Gibbs sampler improves (*i.e.* reduces) the maximal autocorrelation.

	$$E\left[ E[h(X) | x_1]^2 \right] \le E\left[ E[h(X) | x_1, x_2]^2 \right]$$








