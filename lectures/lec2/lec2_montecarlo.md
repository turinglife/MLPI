---
title: Lecture 2 - Monte Carlo Methods
---

# Monte Carlo Methods #

*Monte Carlo methods* are a large family of computational algorithms that rely on *random sampling*. These methods are mainly used for

- Numerical integration
- Stochastic optimization
- Characterizing distributions

---

# Motivation: Expectations in Statistical Analysis #

Computing *expectation* is perhaps the most common operation in statistical analysis. 

- Computing the *normalization factor* in posterior distribution:

	$$p(x | y) = \frac{p(y | x) p(x)}{\int_X p(y | x') p(x') dx'} 
	= \frac{p(x, y)}{E_X[p(X, y)]}.$$

- Computing marginalization:

	$$p(x) = \int_Z p(x, z) dz = E_Z[p(x, Z)].$$

- Computing expectation of functions:

	$$E_X(f(X)) = \int_X f(x) p(x) dx.$$

---

# Computing Expectation #

- Generally, *expectation* can be written as.

	$$E[f(x)] = \int f \mu(dx).$$

- This formula can be expanded to different forms depending on the base measure $dx$:
	- For discrete space:
	
	$$E[f(x)] = \sum_{k \in \Omega} f(k) P(x=k).$$

	- For continuous space and *Riemann-integrable* function $f$:
	
	$$E[f(x)] = \int_\Omega f(x) dx.$$
	
- Complexity grow exponentially as dimension of $\Omega$ increases

---

# Monte Carlo Integration #

- *(Strong) Law of Large Numbers (LLN)*: Let $X, X_1, X_2, \ldots$ be i.i.d random variables and $f$ be a measurable function. Let $I_n(f) \triangleq \frac{1}{n} \sum_{i=1}^n f(X_i)$, then 

	$$I_n(f) \xrightarrow{a.s.} E[f(X)], \text{ as } n \rightarrow \infty.$$
	
- We can use *sample mean* to *approximate* expectation:

	$$E[f(X)] \simeq \frac{1}{n} \sum_{i=1}^n f(x_i)$$

- How many samples are enough?

---

# Variance of Sample Mean #

- By the *Central Limit Theorem (CLT)*:

	$$\sqrt{n}\left(I_n(f) - E[(f(X))]\right) \xrightarrow{d} \mathcal{N}(0, \sigma_f^2), \text{ as } n \rightarrow \infty.$$
	
	Here, $\sigma_f^2$ is the variance of $f(X)$. 
	
- The variance of $f(X)$ is $\sigma_f^2 / n$. The number of samples required to attain a certain variance $\sigma_\epsilon^2$ is at least $\sigma_f^2 / \sigma_\epsilon^2$.

- The variance $\sigma_f^2$ is usually a polynomial of the dimension of $X$, and even a constant in some cases. 


---

# Random Number Generation #

- All sampling methods rely on a stream of *random numbers* to construct random samples.

- *"True"* random numbers are difficult to obtain. A more widely used approach is to use computational algorithms to produce long sequences of *apparently random* numbers, called *pseudorandom numbers*.

- The sequence of *pseudorandom numbers* is determined by a *seed*. 
	- If a randomized simulation is based on a single *random stream*, it can be *exactly* reproduced by fixing the *seed* initially.

---

# Pseudorandom Number Generators #

- Linear Congruential Generator (LCG): $m = 2^{32} \text{ or } 2^{64}$.
	- C and Java's builtin. 
	- Useful for simple randomized program.
	- Not good enough for serious Monte Carlo simulation.
- Mersenne Twister (MT): $m = 2^{19937} - 1$
	- Passes *Die-hard* tests, good enough for most Monte Carlo experiments
	- Provided by C++'11 or Boost
	- Default RNG for MATLAB, Numpy, Julia, and many other numerical softwares
	- Not amenable to parallel use
- Xorshift1024: $m = 2^{1024}$
	- Proposed in year 2014
	- Passes *BigCrush*
	- Incredibly simple (*5 - 6* lines of C code)

---

# Sampling from a Discrete Distribution #

Let $p$ be the *probability mass function* over $\{1, \ldots, K\}$. Please design an algorithm to sample from this distribution and analyze its complexity.

. . . 

- Linear search: $O(K)$
- Sorted search: $O(K)$, but much faster when prob. mass concentrates on a few values
- Binary search: $O(\log_2 K)$, but each step is a bit more expensive
- Can we do better?

. . .

- Huffman coding: $O(K)$ preprocessing + $O(Entropy)$ per sample
- Alias methods (by *A. J. Walker*): $O(K)$ preprocessing + $O(1)$ per sample

---

# Transform Sampling #

- Let $F$ be the *cumulative distribution function (cdf)* of a distribution $D$. Let $U \sim \mathrm{Uniform}([0, 1])$, then $F^{-1}(U) \sim D$.

. . .

- **(Proof):** Let $X = F^{-1}(U)$:

	$$P(X \le t) = P(F^{-1}(U) \le t) = P(U \le F(t)) = F(t).$$

- How to generate a *exponentially distributed* sample ?

. . . 

- How to draw a sample from a *multivariate normal distribution* $\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ ?

. . .

- **(Algorithm):** 
	1. Perform Cholesky decomposition to get $\mathbf{L}$ s.t. $\mathbf{LL}^T = \mathbf{\Sigma}$.
	2. Generate a vector $\mathbf{z}$ comprised of iid values from $\mathcal{N}(0, 1)$
	3. Let $\mathbf{x} = \mathbf{L} \mathbf{z}$. 

---

# Rejection Sampling #

- **(Rejection sampling algorithm):** To sample from a distribution $p(x)$, which has $p(x) \le M q(x)$ for some $M < +\infty$:
	1. Sample $x \sim q(x)$
	2. Accept $x$ with probability $\frac{p(x)}{M q(x)}$.

. . .

- Expected acceptance rate:

	$$P(\text{accept}) = \int \frac{p(x)}{M q(x)} q(x) \mu(dx) = \frac{1}{M}.$$

- What are the problems of this method?

---

# Importance Sampling #

- Basic idea: generate samples from an *easier distribution* $q(x)$, which is often referred to as the *proposal distribution*, and then reweight the samples.

- Let $p(x)$ be the *target distribution* and $q(x)$ be the *proposal distribution*, which have $p \prec q$ (meaning $p$ is alsolutely continuous *w.r.t.* $q$), and let the *importance weight* be $w(x) = p(x) / q(x)$. Then

	$$E_p[f(x)] = E_q[w(x) \cdot f(x)].$$
	
- We can approximate $E_p[f(x)]$ with:

	$$E_p[f(x)] \simeq I_{q,n}(f) \triangleq \frac{1}{n} \sum_{i=1}^n w(x_i) f(x_i), \ \text{ with } x_1, \ldots, x_n \sim q$$

	By the *strong law of large numbers*, we have $I_{q,n}(f) \xrightarrow{a.s.} E_p[f]$, as $n \rightarrow \infty$.

---

# Variance of Importance Sampling #

- How to choose a good proposal distribution $q$?

. . .

- The variance of $w(x) f(x)$ is

	$$\mathrm{var}_q\left( w(x) f(x) \right) = E_q\left[ w^2(x) f^2(x) \right] - (E_p[f])^2$$
	
	The 2nd term does not depend on $q$, while the 1st term has
	
	$$E_q\left[w^2(x) f^2(x)\right] \ge \left( E_q\left[ w(x) \left|f(x)\right| \right] \right)^2 = \left(E_p \left[ \left|f(x)\right| \right]\right)^2.$$

	The lower bound is attached when $w(x) \left|f(x)\right|$ is a constant:
	
	$$\hat{q}(x) = \frac{\left|f(x)\right| p(x)}{\int \left|f(x)\right| p(x) \mu(dx)}.$$
	
. . .

- The *optimal proposal distribution* is generally difficult to sample from. However, this analysis leads us to an insight: we can achieve high sampling efficiency by emphasizing regions where the value of $p(x) \left|f(x)\right|$ is high.

---

# Adaptive Importance Sampling #

- Basic idea -- *Learn* to do sampling
	- choose the proposal from a tractable family: $q(x; \theta)$.

. . .

- Objective: minimize the sample mean of $f^2(x) w^2(x; \theta)$. Update the parameter $\theta$ as:
	
	$$\theta_{t+1} \leftarrow \theta_t - \alpha \frac{1}{N} \sum_{i=1}^N f^2(x_i) w(x_i; \theta_t) \nabla_\theta w(x_i, \theta_t)$$

	with $x_1, \ldots, x_N \sim q(x; \theta_t)$.

---

# Self-Normalized Weights #

- In many practical cases, $w(x) \propto p(x) / q(x)$ is known only upto a normalizing constant. For such case, we can write:

	$$E_p[f] = \frac{\int f(x) w(x) q(x) \mu(dx)}{\int w(x) q(x) \mu(dx)}.$$

- Hence, we may approximate $E_p[f]$ with

	$$\tilde{I}_{q,n}(f) = \frac{1}{n} \sum_{i=1}^n \tilde{w}_i f(x_i)$$

	Here, $\tilde{w}_i$ is called the *self-normalized weight$, given by $\tilde{w}_i = \frac{w(x_i)}{\sum_{i=1}^n w(x_i)}.$

- By strong law of large numbers, we have $\tilde{I}_{q,n}(f) \xrightarrow{a.s.} E_p[f]$ as $n \rightarrow \infty$.

---

