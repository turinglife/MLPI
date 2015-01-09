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







