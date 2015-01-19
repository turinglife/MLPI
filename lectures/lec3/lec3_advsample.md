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

# Rao-Blackwell Theorem #

- Why do collapsed samplers often perform better than full-fledged Gibbs samplers?

. . .

- Consider an example $p(X, Y)$ and we want to estimate $E[h(X, Y)]$. Suppose we have two tractable ways to do so:
	1. Draw $(x_1, y_1), \ldots, (x_n, y_n) \sim p(X, Y)$, and compute

		$$\bar{h}_1 = \frac{1}{n} \sum_{i=1}^n h(x_i, y_i).$$

	2. Draw $x_1, \ldots, x_n \sim p(X)$ where $p(X)$ is the marginal distribution, and compute
	
		$$\bar{h}_2 = \frac{1}{n} \sum_{i=1}^n E_{p(Y|x_i)}[h(x_i, y)].$$
		
		Here, we assume that there is a tractable way to compute $E_{p(Y|x)}[h(x, y)]$ exactly.

. . .

- Which one is better? Can you justify your answer?

---

# Rao-Blackwell Theorem (cont'd) #

- Let $\mu = E[h(X, Y)]$, then $E[\bar{h}_1] = E[\bar{h}_2] = \mu$. By Strong LLN, both $\bar{h}_1$ and $\bar{h}_2$ converge to $\mu$ almost surely.

. . .

- *(Rao-Blackwell Theorem)* Sample variance will be reduced when some components are marginalized out. With the setting above, we have

	$$\mathrm{var}\left[ \bar{h}_1 \right] \ge \mathrm{var} \left[ \bar{h}_2 \right].$$
	
	Can you show this? 

. . .

- Generally, *reducing sample variance* would also lead to the reduction of *autocorrelation* of the chain, thus improving the mixing performance. 

---

# Gaussian Mixture Model (Revisited) #

- Consider the following model

	$$\theta_1, \ldots, \theta_m \sim \mathcal{N}(0, \sigma_0^2)$$
	
	$$z_i \sim \pi, \ x_i \sim \mathcal{N}(\mu_{z_i}, \sigma_x^2), \ \text{ for } i = 1, \ldots, n$$

- Please design a *Collapsed Gibbs sampler* with $\boldsymbol{\theta} = (\theta_1, \ldots, \theta_m)$ marginalized out.  

. . .








