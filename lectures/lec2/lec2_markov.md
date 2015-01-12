# MCMC: Motivation and Overview #

- Simple strategies like *transform sampling*, *rejection sampling*, and *importance sampling* all rely on drawing *independent samples* from $p$ or a proposal distribution $q$ over the sample space. 
    - This can become very difficult (if not impossible) for complex distributions.

. . .

- **Markov Chain Monte Carlo (MCMC)** explores the sample space through an *ergodic* Markov chain, whose equilibrium distribution is the target distribution $p$.

- Many sampling methods used in practice belong to MCMC:
    - Gibbs sampling
    - Metropolis-Hastings algorithm
    - Slice sampling
    - Reversible Jump
    - ...

---

# Markov Processes #

- Intuitively, a *Markov process* is a stochastic process for which the future depends only on the present and not on the past.

- A sequence of random variables $X_0, X_1, X_2, \ldots$ defined on a measurable space $\Omega$ is called a *(discrete-time) Markov process* if it satisfies the *Markov property*:

    $$P(X_{t+1} \in A | X_0 = x_0, \ldots, X_t = x_t) = P(X_{t+1} \in A | X_t = x_t)$$
    
    Here, $A$ is an arbitrary measurable subset of $\Omega$.
    
. . .

- We first review the formulation and properties of *Markov chains* under a simple setting, where $\Omega$ is a countable space. We will later extend the analysis to more general spaces.

---

# Homogeneous Markov Chains #

- A *homogeneous Markov chain* on a countable state space $\Omega$, denoted by $Markov(\pi_0, P)$ is characterized by an initial distribution $\pi_0$ and a *transition probability matrix (TPM)*, denoted by $P$, such that 
	- $\mathrm{Pr}(X_0 = x) = \pi_0(x)$, and
	- $\mathrm{Pr}(X_{t+1} = y | X_t = x) = P(x, y)$.

- The TPM $P$ is non-negative and has $\sum_{y \in \Omega} P(x, y) = 1, \forall x \in \Omega$. Such a matrix is called a *stochastic matrix*.

. . .

- Let $\pi_t$ be the distribution of $X_t$, then:

    $$\pi_{t+1}(y) = \sum_{x \in \Omega} \pi_t(x) P(x, y),$$
    
    or simply $\pi_{t+1} = \pi_t P$. 
 
---
   
# Multi-step Transition Probabilities #

- Consider two transition steps:

	$$\mathrm{Pr}(X_2 = y | X_0 = x) = \sum_{z \in \Omega} P(x, z) P(z, y) = P^2(x, y)$$

. . .

- More generally, $\mathrm{Pr}(X_{t+m} = y | X_t = x) = P^m(x, y)$.

- Let $\pi_t$ be the distribution of $X_t$, then $\pi_{t+m} = \pi_t P^m$.

---

# Classes of States #

- A state $y$ is said to be *accessible* from state $x$, or $x$ *leads to* $y$, denoted by $x \rightarrow y$, if $P^n(x, y) > 0$ for some $n$.
- States $x$ and $y$ are said to *communicate* with each other, denoted by $x \leftrightarrow y$, if $x \rightarrow y$ and $y \rightarrow x$.
- $x \leftrightarrow y$ is an *equivalence relation* on $\Omega$, which partitions $\Omega$ into *communicating classes*, where states within the same class communicate with each other.

. . .

- The Markov chain is said to be *irreducible* if it forms a single communicating class, or in other words, all states communicate with any other states.

---

# Periodicity of Markov Chains #

- The *period* of a state $x$ is defined as 

    $$\mathrm{period}(x) \triangleq \mathrm{gcd}\left\{n: P^m(x, x) > 0\right\}.$$
    
- A state $x$ is said to be *aperiodic* if $\mathrm{period}(x) = 1$.

- *Period* is a class property: if $x \leftrightarrow y$, then $\mathrm{period}(x) = \mathrm{period}(y)$.

- A Markov chain is called *aperiodic*, if all states are *aperiodic*.

- An *irreducible Markov chain* is *aperiodic*, if there exists an *aperiodic* state. 

- Lazyness breaks periodicity: $\alpha I + (1 - \alpha) P$. 

---

# Recurrence of Markov Chains #

- Suppose the chain is initially at state $x$, the *first return time* to state $x$ is defined to be 

	$$T_x = \inf\left\{ t \ge 1: X_t = x | X_0 = x \right\}.$$ 

	``Note that $T_x$ is a random variable.

- We also define $f_{xx}^{(n)} = \mathrm{Pr}(T_x = n)$, the probability that the chain returns to $x$ *for the first time* after $n$ steps.  

- A state $x$ is said to be *recurrent* if it is guaranteed to have a *finite hitting time*, as 

	$$\mathrm{Pr}(T_x < \infty) = \sum_{n=1}^\infty f_{xx}^{(n)} = 1.$$

	Otherwise, $x$ is said to be *transient*.

---

# Recurrence of Markov Chains (cont'd) #

- A state $x$ is *recurrent* if and only if the chain returns to $x$ *infinitely often*:

	$$\sum_{n=1}^\infty P^n(x, x) = \infty.$$

- *Recurrence* is a class property: if $x \leftrightarrow y$ and $x$ is *recurrent*, then $y$ is also *recurrent*.

- Every *finite* communicating class is *recurrent*.
	- An irreducible finite Markov chain is *recurrent*.

---

# Invariant Distributions #

Consider a Markov chain with TPM $P$ on $\Omega$:

- A distribution $\pi$ over $\Omega$ is called an *invariant distribution* (or *stationary distribution*) if $\pi P = \pi$.

- *Invariant distribution* is NOT necessarily *existent* and *unique*.

- Under certain condition (*ergodicity*), there exists a unique invariant distribution $\pi$. In such cases, $\pi$ is often called an *equilibrium distribution*.

---

# Detailed and Reversible Markov Chains #

- A distribution $\pi$ is said to be *in detailed balance* with $P$ if $\pi(x) P(x, y) = \pi(y) P(y, x)$. 
	- *Detailed balance* implies *invariance*.
	- The converse is not true. 

. . .

- An irreducible Markov chain with TPM $P$ and an invariant distribution $\pi$ is called *reversible* if $\pi$ is in *detailed balance* with $P$. 

- Consider an irreducible Markov chain $(X_t)$ $Markov(\pi, P)$ where $\pi$ is in *detailed balance* with $P$, its *reversal* $(\hat{X}_t)$ is given by $(\pi, \hat{P})$ with $\hat{P}(x, y) \triangleq \pi(y) P(y, x) / \pi(x)$. Then

	$$\Pr(X_0 = x_0, \ldots, X_n = x_n) = \Pr(\hat{X}_0 = x_n, \ldots, \hat{X}_n = x_0).$$

- Reversible chains are widely used in MCMC practice.

---

# Positive Recurrence #

- The *expected return time* of a state $x$ is defined to be $m_x \triangleq E[T_x]$.

- When $x$ is transient, $m_x = \infty$. If $x$ is recurrent, $m_x$ is NOT necessarily finite. 

- A *recurrent state* $x$ is called *positive recurrent* if $m_x < \infty$. Otherwise, it is called *null recurrent*.

. . .

- *(Existence of Invariant distributions)* For an *irreducible* Markov chain, if some state is *positive recurrent*, then all states are *positive recurrent* and the chain has an *invariance distribution* $\pi$ given by $\pi(x) = 1 / m_x$. 

---

# Ergodic Markov Chains #

- An *irreducible*, *aperiodic*, and *positive recurrent* Markov chain is called an *ergodic Markov chain*, or simply *ergodic chain*. 

- A finite Markov chain is *ergodic* if and only if it is irreducible and aperiodic. 

- A Markov chain is *ergodic* if it is aperiodic and there exist $N$ such that any state can be reached from any other state within $N$ steps with positive probability. 

. . .

- *(Convergence to equilibrium)* Let $P$ be the transition probability matrix of an *ergodic* Markov chain, then there exists a unique *invariant distribution* $\pi$. Then with any initial distribution, $\mathrm{Pr}(X_n = x) \rightarrow \pi(x)$ as $n \rightarrow \infty$ for all $x \in \Omega$. Particularly, $P^n(x', x) \rightarrow \pi(x)$ as $n \rightarrow \infty$ for all $x, y \in \Omega$. 

---

# Ergodic Theorem #

- The *ergodic theorem* relates *time mean* to *space mean*:

- Let $Markov(\pi_0, P)$ be an *ergodic Markov chain* over $\Omega$ with equilibrium distribution $\pi$, and $f$ be a measurable function on $\Omega$, then 

	$$\frac{1}{n} \sum_{t=0}^n f(X_t) \xrightarrow{a.s.} E_\pi[f], \ \text{ as } n \rightarrow \infty.$$

	More generally, we have for any positive integer $m$:
	
	$$\frac{1}{n} \sum_{t=0}^n f(X_{\tau + t m}) \xrightarrow{a.s.} E_\pi[f], \ \text{ as } n \rightarrow \infty.$$

- The *ergodic theorem* is the theoretical foundation for MCMC.

---

# Mixing #

- Let $\mu$ and $\nu$ be probability measures over a measurable space $(\Omega, \mathcal{S})$, then the *total variation distance* between them is defined as

	$$\|\mu - \nu\|_{TV} = \sup_{A \in \mathcal{S}} \left|\mu(S) - \nu(S)\right|.$$
	
	If $\Omega$ is *countable*, we have
	
	$$\|\mu - \nu\|_{TV} = \frac{1}{2} \sum_{x \in \Omega} \left|\mu(x) - \nu(x)\right|.$$

- The *total variation distance* is a metric.

. . .

- The time required by a Markov chain to get close to the equilibrium distribution is measured by the *mixing time*, defined as $t_{mix}(\epsilon) = \inf\{t: d(t) \le \epsilon\}$, and in particular $t_{mix} \triangleq t_{mix}(1/4)$.

---

# Bounds of Mixing Time #

There are various ways to bound the mixing time, taking into account different factors:

- Counting Bound
- Diameter Bound
- Spectral Analysis
- Conductance

---

# Simple Bounds on Mixing Time #

- *(Counting Bound)*: if the chain can only transit to a limited number of states from each state, it may take quite a long time to cover the explore the entire space. Consider an ergodic finite Markov chain over $\Omega$ whose equilibrium distribution is uniform, then

	$$t_{mix}(\epsilon) \ge \frac{\log\left(|\Omega|(1 - \epsilon)\right)}{\log \Delta}.$$

	Here, $\Delta$ is the maximum outgoing degree of each state.
	
. . .

- *(Diameter Bound)*: For an ergodic finite Markov chain, we have $t_{mix}(\epsilon) \ge L / 2$ for any $\epsilon < 1 / 2$, where $L$ is the *diameter* of the state graph.

---

# Spectral Representation #

Let $P$ be a *stochastic matrix* over a finite space $\Omega$ with $|\Omega| = N$:

- The *spectral radius* of $P$, namely the maximum absolute value of all eigenvalues, is $\rho(P) = 1$. 

. . .

Furthermore, if $P$ is *ergodic* and *reversible* with equilibrium distribution $\pi$:

- Consider an inner product space $\left(\mathbb{R}^{\Omega}, \langle \cdot, \cdot \rangle_\pi\right)$ with 

	$$\langle f, g \rangle_\pi \triangleq E_\pi[f(x) g(x)] = \sum_{x \in \Omega} \pi(x) f(x) g(x).$$

- All eigenvalues of $P$ are real values, given by $1 = \lambda_1 > \lambda_2 \ge \cdots \ge \lambda_N > -1$. Let $f_i$ be the right eigenvector associated with $\lambda_i$. Then the left eigenvector is $\pi_i \circ f_i$ *(element-wise product), and $P^t$ can be represented as 

	$$\frac{P^t(x, y)}{\pi(y)} = \sum_{i=1}^{N} f_i(x) f_i(y) \lambda_i^t = 1 + \sum_{i=2}^{N} f_i(x) f_i(y) \lambda_i^t.$$

---

# Spectral Gap and Relaxation Time #

- Let $\lambda_* \triangleq \sup \left\{|\lambda_i|: 2 \le i \le |\Omega|\right\}$. Then the *spectral gap* is defined to be $\gamma \triangleq 1 - \lambda_2$ and the *absolute spectral gap* is defined to be $\gamma_* \triangleq 1 - \lambda_*$. Then:

	$$\left|\frac{P^t(x, y)}{\pi(y)} - 1 \right| \le \frac{\lambda_*^t}{\sqrt{\pi(x) \pi(y)}} \le \frac{\lambda_*^t}{\pi_{min}} \le \frac{e^{-\gamma_* t}}{\pi_{min}}.$$
	
	Here, $\pi_{min} = \min_{x \in \Omega} \pi(x)$.

- The *relaxation time* of a *Markov chain* is defined to be $t_{rel} = 1 / \gamma_*$, then

	$$\log \left( \frac{1}{2\epsilon} \right) (t_{rel} - 1) \le t_{mix}(\epsilon) \le \log \left( \frac{1}{\epsilon \pi_{min}} \right) t_{rel}.$$

- Generally, the goal to design a *rapidly mixing* reversible Markov chain is to minimize $\lambda_*$, or in other words, maximize the $\gamma_*$.

---

# Conductance #

Consider an ergodic Markov chain on a finite space $\Omega$ with transition probability matrix $P$ and equilibrium distribution $\pi$:

- The *ergodic flow* from a subset $A$ to another subset $B$ is defined as 

	$$Q(A, B) \triangleq \sum_{x \in A, y \in B} \pi(x) P(x, y).$$

- The *conductance* of a Markov chain is defined as
	
	$$\Phi_* = \inf_{S: \pi(S) \le \frac{1}{2}} \frac{Q(S, S^c)}{\pi(S)}.$$

. . .

- *(Jerrum and Sinclair (1989))* The spectral gap is bounded by

	$$\frac{1}{2} \Phi_*^2 \le \gamma \le 2 \Phi_*.$$

---

# Exercise 1 #

Consider an ergodic finite chain $P$ with $\gamma_* < \gamma$. To improve the mixing time, one can add a little bit lazyness as $P' = (1 - \alpha) P + \alpha I$. Please solve the optimal value of $\alpha$ that maximizes the *absolute spectral gap* $\gamma_*$.

---

# Exercise 2 #

Consider a $2 \times 2$ stochastic matrix $P$, given by $P(x, y) = 1 - p$ when $x \ne y$.

- Please specify the condition under which $P$ is ergodic.

- What is the equilibrium distribution when $P$ is ergodic?

. . .

- Solve the optimal value of $p$ that maximizes the absolute spectral gap.

---

# Exercise 3 #

- Consider a random walk on a circle of length $n$, where $n$ is even. At each state $x$, it walks to either of its neighbor with probability $p$, and stays at $x$ with probability $1 - 2p$.

- Please specify the condition under which $P$ is ergodic.

- What is the equilibrium distribution when $P$ is ergodic?

. . .

- Solve the optimal value of $p$ that maximizes the *conductance*.

. . .

- If we allow the chain to jump from $x$ to its *opposite* state with probability $q$ and thus the probability of staying at $x$ is $1 - 2p - q$. What's the conductance now?

- Solve the optimal setting of $p$ and $q$.

---


# General Markov Chains #

Next, we extend the formulation of *Markov chain* from *countable space* to general *measurable space*. 

- First, the *Markov property* remains.

. . .

- Generally, a *homogeneous Markov chain* over a measurable space $(\Omega, \mathcal{S})$ is characterized by an *initial measure* $\pi_0$ and a *stochastic kernel* $P: \Omega \times \mathcal{S} \rightarrow [0, 1]$, denoted by $Markov(\pi_0, P)$.  Here, $\Omega$ is called the *state space*; and:

	$$\mathrm{Pr}(X_{t+1} \in A | X_t = x) = P(x, A).$$
	
- The *stochastic kernel* $P$ has to satisfy:
	- Given $x \in \Omega$, $P_x: A \mapsto P(x, A)$ is a *probability measure* over $(\Omega, \mathcal{S})$.
	- Given a measurable subset $A \in \mathcal{S}$, $P(\cdot, A): x \mapsto P(x, A)$ is a measurable function. 

- When $\Omega$ is a countable space, $P$ reduces to a *stochastic matrix*.

---

# General Markov Chains (cont'd) #

- Suppose the distribution of $X_t$ is $\pi_t$, then

	$$\pi_{t+1}(A) = \int_\Omega P(x, A) \pi_t(dx)$$
	
	Again, we can simply write this as $\pi_{t+1} = \pi_t P$.

- Composition of stochastic kernels $P$ and $Q$ remains a stochastic kernel, denoted by $Q \circ P$, which is given by:

	$$(Q \circ P)(x, A) = \int_\Omega P(x, dy) Q(y, A).$$

- Recursive composition of $P$ for $m$ times results in a stochastic kernel denoted by $P^m$, and we have $\mu_{t+m} = \mu_t P^m$.

---

# Example: Random Walk in $\mathbb{R}^n$ #

$$X_{t+1} = X_t + B_t, \ \text{ with } B_t \sim \mathcal{N}(0, \sigma^2 I).$$

- For this case, the stochastic kernel is given by $P_x = P_{\mathcal{N}(x, \sigma^2 I)}$.

---

# Irreducibility #

- Let $\mu$ be a positive measure over $(\Omega, \mathcal{S})$. A *stochastic kernel* $P$ is called *$\mu$-irreducible* if for each $x \in \Omega$ and $A \in \mathcal{S}$ with $\mu(A) > 0$, there exists a positive integer $n$ such that $P^n(x, A) > 0$. 

. . .

- For typical spaces, we usually choose the *canonical base measure* as $\mu$. 
	- For *countable space*, we use *counting measure* as $\mu$
	- For $\mathbb{R}$, $\mathbb{R}^n$ or manifolds, we use *Lebesgue measure* as $\mu$.
	- When $\mu$ is implicitly indicated by the context, we simply call a kernel $P$ *irreducible*.
	- When $\Omega$ is countable, this notion is *irreducibility* coincides with the one introduced earlier.

---

# Irreducibility (cont'd) #
	
The following theorem provides an easier way to verify *irreducibility*.

- A measurable subset $A \in \mathcal{S}$ with $\mu(A) > 0$ is called *$\mu$-communicating* if for each $x \in A$ and each $B \in \mathcal{S}$ that is contained in $A$, there exists a positive integer $n > 0$ such that $P^n(x, B) > 0$. 
	- $P$ is irreducible if and only if $\Omega$ is *$\mu$-communicating*. 

. . .

- *(Irreducibility Theorem)* Let $P$ be a *stochastic kernel* over a *measurable* state space $(\Omega, \mathcal{S})$, then $P$ is *$\mu$-irreducible* if the following conditions are satisfied:
	- $\Omega$ is *separable* (meaning $\Omega$ has a countable dense set) and *connected*;
	- Every non-empty open subset $A$ of $\Omega$ has $\mu(A) > 0$;
	- Every $x \in \Omega$ has a $\mu$-communicating neighborhood.

. . .

- **Note:** This irreducibility theorem does *NOT* apply to countable space. Why?

---



	



