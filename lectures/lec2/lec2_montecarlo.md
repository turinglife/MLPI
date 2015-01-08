---
title: Lecture 2 - Monte Carlo Methods
---

# Monte Carlo Methods #

*Monte Carlo methods* generally refer to a large family of computational algorithms that rely on *random sampling*. These methods are mainly used for

- Numerical integration
- Stochastic optimization
- Characterizing distributions

---

# Computing Integration #

- Computing *expectation* is perhaps the most common operation in statistical analysis.

	$$E[f(x)] = \int f \mu(dx)$$

- This formula can be expanded to different forms depending on the base measure $dx$:
	- For discrete space:
	
	$$E[f(x)] = \sum_{k \in \Omega} f(k) P(x=k)$$

	- For continuous space and *Riemann-integrable* function $f$:
	
	$$E[f(x)] = \int_\Omega f(x) dx$$
	
- Complexity grow exponentially as dimension of $\Omega$ increases

---

# Monte Carlo Integration #

- *(Strong) Law of Large Numbers (LLN)*: Let $X_1, X_2, \ldots$ be iid random variables with $E[X_1] = E[X_2] = \ldots = m$, and $\bar{X}_n \triangleq \frac{1}{n} \sum_{i=1}^n x_i$, then 

	$$\bar{X}_n \xrightarrow{a.s.} m, \text{ as } n \rightarrow \infty.$$
	
- We can use *sample mean* to *approximate* expectation:

	$$E[f(X)] \simeq \frac{1}{n} \sum_{i=1}^n x_i$$

- How many samples are enough?

. . .

- The variance of $\bar{X}_n$ is $\frac{1}{n}\mathrm{var}(X)$.
- It takes $O(\sigma_x^2 / \sigma_*^2)$ samples to reach a desired variance $\sigma_*^2$.

---

# 







