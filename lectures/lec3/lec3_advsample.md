---
title: Lecture 3 - Advanced Sampling Techniques 
shorttitle: Lecture 3
---

# Overview #

- Partially Collapsed Sampling
- Sampling with Auxiliary Variables 
	- Simulated Tempering & Parallel Tempering
	- Swendsen-Wang Algorithm
	- Slice Sampling
- Hamiltonian Monte Carlo
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

---

# Sampling with Auxiliary Variables #

- The *Rao Blackwell Theorem* suggests that in order to achieve better performance, one should try to marginalize out as many components as possible.

- However, in many cases, one may want to do the opposite, that is, to introduce additional variables to facilitate the simulations. 

- For example, when the *target distribution* is *multimodal*, one may use an auxiliary variable, such as temperature, to help the chain escape from local traps.

. . .

- Basic framework
	- Specify an auxiliary variable $U$ and the joint distribution $p(X, U)$ such that $p(x) = \int p(x, u) \mu(du)$ for certain $\mu$. 
	- Design a chain to update $(X, U)$ using the M-H algorithm or the Gibbs sampler.
	- The samples of $p(X)$ can then be obtained through *marginalization* or *conditioning*.

---

**Simulated Tempering**

---

# Gibbs Measure #

- A *Gibbs measure* is a probability measure with a density in the following form:

	$$p(x) = \frac{1}{Z(\alpha)} \exp \left( - \alpha E(x) \right).$$
	
	Here, $E(x)$ is called the *energy function*, $\alpha$ is called the *inverse temperature*, and the normalizing constant $Z$ depends on $\alpha$. 

\begin{center}
\includegraphics[width=0.3\textwidth]{imgs/amde.jpg}
\end{center}
	
- In literature of MCMC sampling, we often parameterize a Gibbs measure using the *temperature parameter* $\tau = \alpha^{-1}$, thus $p(x) = \frac{1}{Z(\tau)} \exp \left( -E(x) / \tau \right)$.

---

# Tempered MCMC #

- Typical MCMC methods usually rely on *local moves* to explore the state space. What is the problem?

. . .

- Local traps often leads to very poor mixing. Can we improve this?

\begin{center}
\includegraphics[width=0.45\textwidth]{imgs/ptemper.png}
\end{center}

---

# Simulated Tempering #

Suppose we intend to sample from $p(x) = \frac{1}{Z} \exp(-E(x))$:

- **Basic idea:** Augment the target distribution by including a *temperature index $k$*,  which takes values from a finite set $1 \le \tau_0 < \cdots < \tau_m$, with joint distribution given by

	$$p(x, k) = \frac{\pi_k}{Z_k} \exp\left(-\frac{E(x)}{\tau_k}\right)$$
	
	Here, $\pi_k$ is the prior weight of the $k$-th temperature and $Z_k$ is the corresponding normalizing constant. We only collect samples at the *lowest temperature*, $\tau_0 = 1$. 

. . .

- The chain mixes much faster at high temperatures, but we want to collect samples at the lowest temperature. So we have to constantly switch between temperatures. 

- **Question:** How can we set the probabilities of switching between temperatures?

---

# Simulated Tempering (Algorithm) #

One iteration of *Simulated Tempering* consists of two steps:

- *(Base transition)*: update $x$ at the same temperature, *i.e.* holding $k$ fixed.

- *(Temperature switching)*: with $x$ fixed, propose $k \rightarrow k'$ with $q(k, k')$
	- $q(k, k')$ is typically set in a way such that $q(k, k') = q(k', k)$
	- Accept the change with probability $a(k, k'|x) = \min(1, p(x, k') / p(x, k))$. 

- All temperature levels play an important role. So it is desirable to spend comparable amount of time at each level. Setting $\pi_k = \frac{1}{m+1}$ for each $k$, we have

	$$\frac{p(x, k')}{p(x, k)} = \frac{Z_k}{Z_{k'}} \exp 
	\left( \left(\tau_{k}^{-1} - \tau_{k'}^{-1} \right) E(x) \right)$$

---

# Simulated Tempering (Discussion) #

- The acceptance rate of temperature switching proposals depends on $p(x, k') / p(x, k)$. To have high acceptance rate, the distribution should have *similar shapes*.
	- Set $\tau_0 = 1$. Given $\tau_k$, we should set $\tau_{k+1}$ such that uphill moves from ($(x, k) \rightarrow (x, k+1)$) should have a considerable probability of being accepted. 
	- Build the *temperature ladder* step by step until we have a sufficiently smooth distribution at the top.

. . .

- The time spent on the base level $\tau_0$ is around $1 / (1 + m)$. If we have too many levels, only a very small portion of samples can be used. 

. . .

- The normalzing constants $Z_k$ are typically unknown and estimating them is very difficult and expensive.

---

**Parallel Tempering**

---

# Parallel Tempering #

- **(Basic idea):** rather than jumping between temperatures, it *simultaneously* simulate multiple chains, each at a temperature level $\tau_k$, called a *replica*, and constantly swap samples between replicas. 

. . .

- **(Algorithm):** each iteration consists of the following steps:
	- *(Parallel update):* simulate each replica with its own transition kernel
	- *(Replica exchange):* propose to swap states between two replicas (say the $i$-th and $j$-th, where $j = i \pm 1$): 

		$$(x_t^{(i)}, x_t^{(j)}) \rightarrow (x_{t+1}^{(i)} = x_t^{(j)}, x_{t+1}^{(j)} = x_t^{(i)})$$
	
		The proposal is accepted with probability $a(i, j|x_t) = \min\{1, r(i, j|x_t)\}$, where
		
		$$r(i, j | x) = \exp\left((\tau_k^{-1} - \tau_{k+1}^{-1}) (E(x^{(i)}) - E(x^{(j)})\right)$$	
	- We collect samples from the base replica (the one with $\tau_0 = 1$).

. . .

- Why does this algorithm produce the desired distribution?

---

# Parallel Tempering (Justification) #

- Let $\mathbf{x} = (x^{(0)}, \ldots, x^{(m)})$. We define

	$$p(\mathbf{x}) = \prod_{k=1}^m p_k(x^{(k)}), 
	\ \text{ with } 
	p_k(x) = \frac{1}{Z_k} \exp \left( 
		- \frac{E(x)}{\tau_k}
	\right)$$

. . .

- Obviously, the step of *parallel update* preserves the invariant distribution $p(\mathbf{x})$. 

. . .

- Note that the step of *replica exchange* is *symmetric*, *i.e.* the probabilities of going up and down are equal, then according to the *Metropolis algorithm*, we have $a = \min(1, r)$ with

	$$r = \frac{p(\mathbf{x'})}{p(\mathbf{x})}
	= \frac{p_i(x^{(j)}) p_j(x^{(i)})}{p_i(x^{(i)})p_j(x^{(j)})}
	= \left(\tau_i^{-1} - \tau_j^{-1} \right)\left(E(x^{(i)}) - E(x^{(j)})\right).$$

---

# Parallel Tempering (Discussion) #

- It is efficient and very easy to implement, especially in a parallel computing environment. 

. . .

- It is often an *art* instead of a *technique* to tune a parallel tempering system (both the temperature ladder and the controlling parameter of each individual chain). 

. . .

- The *parallel tempering* is a special case of a large family of MCMC methods called *Extended Ensemble Monte Carlo*, which involves a collection of *parallel* Markov chains and the simulation switches between these them.  

---

**Swendsen-Wang Algorithm**

---

# Extended Ising Model #

- The standard *Ising model* is defined as

	$$p(\mathbf{x} | \boldsymbol{\theta}) = 
	\frac{1}{Z} \prod_{\{i,j\} \in E} f_{ij}\left(x^{(i)}, x^{(j)}\right) = 
	\frac{1}{Z} \exp\left(
		\sum_{\{i,j\} \in E} \theta_{ij} x^{(i)} x^{(j)}
	\right),$$
	
	where $x_i \in \{-1, +1\}$ for each $i$ is called a *spin*, and $\theta_{ij} \ge 0$. 
	
- Gibbs sampling is extremely slow, especially when the temperature is low.

. . .

- We extend the model by introducing additional *bond variables* $u^{(ij)}$, each for an edge. Each bond has two states: $0$ indicating *connected* and $1$ indicating *disconnected*. 

- We define a joint distribution that couples the *spins* and *bonds*, 

	$$p(\mathbf{x}, \mathbf{b}) 
	= \frac{1}{Z'} \prod_{\{i,j\} \in E}
	g_{ij}\left(x^{(i)}, x^{(j)}, u^{(ij)}\right)$$  

---

# Extended Ising Model (cont'd) #

- Here, $g_{ij}(x, y, u)$ is described as below:
	- When $u = 0$, $g_{ij}(x, y, u) = \exp(-\theta_{ij})$ for each setting of $(x, y)$ 
	- When $u = 1$, $g_{ij}(x, y, u) = 1(x = y) \left( \exp(\theta_{ij}) - \exp(-\theta_{ij}) \right)$  

. . .

- With this setting, $g_{ij}(x, y, u)$ can be written as:

	$$g_{ij}(x, y, u) = f_{ij}(x, y) \cdot q_{ij}(u|x, y),$$
	
	where $q_{ij}(u | x, y) = g_{ij}(x, y, u) / f_{ij}(x, y)$, which can be described as:
	
	- when $x \ne y$, $u$ must be $0$
	- when $x = y$, $u$ is set to zero with probability $\exp(-2 \theta_{ij})$.  
 
---

# Swendsen-Wang Algorithm #

The *Swendsen-Wang* algorithm (*R. Swendsen* and *J. Wang*, *1987*) is a Gibbs sampling algorithm based on the *extended Ising model*. Each iteration consists of two steps:

- *(Clustering):* conditioned on the *spins* $\mathbf{x}$, draw the *bonds* $\mathbf{u} \sim p(\mathbf{u} | \mathbf{x})$ independenly. For an edge $\{i, j\} \in E$:
	- If $x^{(i)} \ne x^{(j)}$, set $u^{(ij)} = 0$
	- If $x^{(i)} = x^{(j)}$, set $u^{(ij)} = 1$ with probability $1 - \exp(-2\theta_{ij})$ or $0$ otherwise.
	- Given $\mathbf{u}$, all nodes are partitioned into several *connected components*.

. . .

- *(Swapping):* conditioned on the *bonds* $\mathbf{b}$, draw the *spins* $\mathbf{x} \sim p(\mathbf{x} | \mathbf{u})$. 
	- For each connected component, draw $+1$ or $-1$ with equal chance, and assign the resultant value to all nodes in the component. 

---

# Swendsen-Wang Algorithm (Illustration) #

\begin{center}
\includegraphics[width=0.98\textwidth]{imgs/swang1.pdf}
\end{center}

---

# Swendsen-Wang Algorithm (Discussion) #

- When $\theta_{ij}$ is large, $u^{(ij)}$ has a high probability of being set to one, *i.e.* $x^{(i)}$ and $x^{(j)}$ are likely to be connected. 

. . .

- Experiments show that the *Swendsen-Wang* algorithm mixes very rapidly, especially for rectangular grids.
	- Can you provide an intuitive explanation?

. . .

- The *Swendsen-Wang* algorithm can be generalized to Potts models (nodes can take values from a finite set). 

- The *Swendsen-Wang* algorithm has been widely used in image analysis applications, *e.g.* image segmentation (in this case, it is called *Swendsen-Wang cut*).

---



