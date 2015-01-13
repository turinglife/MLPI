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

# Exercise 1 #

\begin{center}
\includegraphics[width=0.35\textwidth]{imgs/communicateclass.png}
\end{center}

- Is this Markov chain *irreducible* ?
- Please identify the *communicating classes*.

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

	$$\tau_x = \inf\left\{ t \ge 1: X_t = x | X_0 = x \right\}.$$ 

	Note that $\tau_x$ is a random variable.

- We also define $f_{xx}^{(n)} = \mathrm{Pr}(\tau_x = n)$, the probability that the chain returns to $x$ *for the first time* after $n$ steps.  

- A state $x$ is said to be *recurrent* if it is guaranteed to have a *finite hitting time*, as 

	$$\mathrm{Pr}(\tau_x < \infty) = \sum_{n=1}^\infty f_{xx}^{(n)} = 1.$$

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

# Exercise 2 #

\begin{center}
\includegraphics[width=0.45\textwidth]{imgs/mchain2.png}
\end{center}

- Is this chain *irreducible*? 
- Is this chain *periodic*?
- Please compute the *invariant distribution*.

---

# Positive Recurrence #

- The *expected return time* of a state $x$ is defined to be $m_x \triangleq E[T_x]$.

- When $x$ is transient, $m_x = \infty$. If $x$ is recurrent, $m_x$ is NOT necessarily finite. 

- A *recurrent state* $x$ is called *positive recurrent* if $m_x < \infty$. Otherwise, it is called *null recurrent*.

. . .

- *(Existence of Invariant distributions)* For an *irreducible* Markov chain, if some state is *positive recurrent*, then all states are *positive recurrent* and the chain has an *invariance distribution* $\pi$ given by $\pi(x) = 1 / m_x$. 

---

# Example: 1D Random Walk #

\begin{center}
\includegraphics[width=0.75\textwidth]{imgs/rwalk1d.png}
\end{center}

- Under what condition is this chain *recurrent*?
- When it is *recurrent*, is it *positive recurrent* or *null recurrent*?

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

	$$\|\mu - \nu\|_{TV} = \sup_{A \in \mathcal{S}} \left|\mu(A) - \nu(A)\right|.$$
	
	If $\Omega$ is *countable*, we have
	
	$$\|\mu - \nu\|_{TV} = \frac{1}{2} \sum_{x \in \Omega} \left|\mu(x) - \nu(x)\right|.$$

- The *total variation distance* is a metric.

. . .

- The time required by a Markov chain to get close to the equilibrium distribution is measured by the *mixing time*, defined as $t_{mix}(\epsilon) = \inf\{t: d(t) \le \epsilon\}$, and in particular $t_{mix} \triangleq t_{mix}(1/4)$.

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

# Conductance (Illustration) #

\begin{center}
\includegraphics[width=0.85\textwidth]{imgs/mcbottleneck.png}
\end{center}

---

# Exercise 3 #

Consider an ergodic finite chain $P$ with $\gamma_* < \gamma$. To improve the mixing time, one can add a little bit lazyness as $P' = (1 - \alpha) P + \alpha I$. Please solve the optimal value of $\alpha$ that maximizes the *absolute spectral gap* $\gamma_*$.

---

# Exercise 4 #

Consider a $2 \times 2$ stochastic matrix $P$, given by $P(x, y) = 1 - p$ when $x \ne y$.

- Please specify the condition under which $P$ is ergodic.

- What is the equilibrium distribution when $P$ is ergodic?

. . .

- Solve the optimal value of $p$ that maximizes the absolute spectral gap.

---


# General Markov Chains #

Next, we extend the formulation of *Markov chain* from *countable space* to general *measurable space*. 

- First, the *Markov property* remains.

. . .

- Generally, a *homogeneous Markov chain* over a measurable space $(\Omega, \mathcal{S})$ is characterized by an *initial measure* $\pi_0$ and a *transition probability kernel* $P: \Omega \times \mathcal{S} \rightarrow [0, 1]$, denoted by $Markov(\pi_0, P)$.  Here, $\Omega$ is called the *state space*; and:

	$$\mathrm{Pr}(X_{t+1} \in A | X_t = x) = P(x, A).$$
	
- $P$ must be a *stochastic kernel*:
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

- Recursive composition of $P$ for $m$ times results in a stochastic kernel denoted by $P^m$, and we have $P^{n+m} = P^n \circ P^m$ and $\mu_{t+m} = \mu_t P^m$.

---

# Example: Random Walk in $\mathbb{R}^n$ #

$$X_{t+1} = X_t + B_t, \ \text{ with } B_t \sim \mathcal{N}(0, \sigma^2 I).$$

- For this case, the stochastic kernel is given by $P_x = P_{\mathcal{N}(x, \sigma^2 I)}$.

\begin{center}
\includegraphics[width=0.5\textwidth]{imgs/brownianmotion.png}
\end{center}

---

# Occupation Time, Return Time, and Hitting Time #

For general space, talking about the probability of *hitting a point* makes no sense. Instead, we should talk about sets:

. . .

Given a Markov train $(X_t)$ over $(\Omega, \mathcal{S})$, and $A \in \mathcal{S}$:

- The *occupation time* of $A$ is defined to be $\eta_A \triangleq \sum_{t=1}^\infty 1(X_t \in A)$. 
- The *return time* of $A$ is defined to be $\tau_A \triangleq \inf \left\{ t \ge 1: X_t \in A \right\}$.
- The *hitting time* of $A$ is defined to be $\sigma_A \triangleq \inf \left\{ t \ge 0: X_t \in A \right\}$. 
- $\eta_A$, $\tau_A$ and $\sigma_A$ are all random variables. 

---

# $\varphi$-irreducibility #

- Define $L(x, A) \triangleq P_x(\tau_A < \infty) = P_x(X \text{ ever enters } A)$.

- $L(x, A)$ has

	$$L(x, A) = P(x, A) + \int_{A^c} P(x, dy) L(y, A).$$

- Given a positive measure $\varphi$ over $(\Omega, \mathcal{S})$, a markov chain is called *$\varphi$-irreducible* if $L(x, A) > 0 \ \forall x \in \Omega$ whenever $A$ is *$\varphi$-positive*, *i.e.* $\varphi(A) > 0$. 

- Intuitively, it means that for any $\varphi$-positive set $A$, there is positive chance that the chain enters $A$ within finite time, no matter where it begins.

---

# $\varphi$-irreducibility (cont'd) # 

- A Markov chain over $\Omega$ is $\varphi$-irreducible if and only if either of the following statement holds:
	- $\varphi(A) > 0 \Rightarrow \forall x \in \Omega, \ E_x(\eta_A) > 0$
	- $\varphi(A) > 0 \Rightarrow \forall x \in \Omega, \ \exists t \in \mathbb{N}^+, \ P^t(x, A) > 0$

. . .

- Typical spaces usually come with *natural measure* $\varphi$:
	- The *natural measure* for countable space is the *counting measure*. In this case, the notion of $varphi$-irreducibility coincides with the one introduced earlier.
	- The *natural measure* for $\mathbb{R}$, $\mathbb{R}^n$, or a finite-dimensional manifold is the *Lebesgue measure*
	- When $\varphi$ is implicitly indicated, we simple call the chain *irreducible*.

---

# $\varphi$-irreducibility (cont'd) #

The following theorem provides an easier way to verify *irreducibility* for separable space.

- A set $S$ is called *$\varphi$-communicating* if for every $x \in S$ and every $\varphi$-positive subset $A \subset S$ (*i.e.* $A$ is measurable and $\varphi(A) > 0$), $x \rightarrow A$.
	- The space $\Omega$ is *$\varphi$-irreducible* if and only if $\Omega$ is *$\varphi$-communicating*. 

. . .

- *(Irreducibility Theorem)* Let $P$ be a *stochastic kernel* over a *measurable* state space $(\Omega, \mathcal{S})$, then $P$ is *$\mu$-irreducible* if the following conditions are satisfied:
	- $\Omega$ is *separable* (meaning $\Omega$ has a countable dense set) and *connected*;
	- Every non-empty open subset $A$ is $\varphi$-positive;
	- Every $x \in \Omega$ has a $\varphi$-communicating neighborhood.

. . .

- **Note:** This irreducibility theorem does *NOT* apply to countable space. Why?

--- 

# Transience and Recurrence #

Given a Markov chain $(X_t)$ over $(\Omega, S)$, and $A \in \mathcal{S}$:

- $A$ is called *transient* if $E_x[\eta_A] < \infty$ for every $x \in A$.
- $A$ is called *uniformly transient* if there exists $M > 0$ such that $U(x, A) < M$ for every $x \in A$.
- $A$ is called *recurrent* if $E_x[\eta_A] = \infty$ for every $x \in A$.

. . .

- Consider an $\varphi$-irreducible chain, then either:
	- Every $\varphi$-positive subset is recurrent, then we call the chain *recurrent*
	- $\Omega$ is covered by countably many uniformly transient sets, then we call the chain *transient*.

---

# Harris Recurrence #

- A set $A$ is called *Harris recurrent* if 

	$$P_x(\eta_A = \infty) = 1, \ \forall x \in A,$$
	
	which means any chain starts within $A$ visits $A$ infinitely often.

- A Markov chain is called *Harris recurrent* if it is $\varphi$-irreducible (with maximal irreducibility measure) and every $\varphi$-positive subset is Harris recurrent.

- Most MCMC samplers are *Harris recurrent*.

. . .

- *Harris recurrence* implies *recurrence*.
	- Note: $P_x(\eta_A = \infty) = 1 \Rightarrow E_x[\eta_A] = \infty$, but the converse is generally not true. 

---

# Invariant Measures #

- A measure $\pi$ is called an *invariant measure* *w.r.t.* the stochastic kernel $P$ if $\pi = \pi P$, *i.e.*

	$$\pi(A) = \int_\Omega \pi(dx) P(x, A), \ \forall A \in \mathcal{S}.$$

- A *recurrent* Markov chain admits a unique *invariant measure* $\pi$ (up to a scale constant). 
	- **Note:** This measure $\pi$ can be finite or infinite.

---

# Positive Chains #

- A Markov chain is called *positive* if it is irreducible and admits an *invariant probability measure* $\pi$.
	
- If a Markov chain is *positive* then it is *recurrent*, and thus it admits a *unique* invariant probability measure. 

- If a Markov chain is *Harris positive* and *recurrent*, then it is called a *positive Harris chain*.

. . .

- The study of the *existence* of $\pi$ requires more sophisticated analysis that involves *petite sets*, *sub-invariance*, and *atoms*. 
	- We are not going into these details, as in MCMC practice, existence of $\pi$ is usually not an issue.

---

# Subsampled Chains #

Suppose $P$ is a stochastic kernel and $q$ is a probability vector over $\mathbb{N}$.

- Then $P_q$ defined as below is also a stochastic kernel:

	$$P_q(x, A) = \sum_{k=0}^\infty q_k P^k(x, A)$$
	
	The chain with kernel $P_q$ is called a *subsampled chain* with $q$.
	
- When $q_n = 1(n = m)$, $P_q = P^m$.

- If $\pi$ is invariant *w.r.t.* $P$, then $\pi$ is also invariant *w.r.t.* $P_q$.

---

# Birkhoff Ergodic Theorem #

- A stochastic process $(X_t)$ is called a *stationary process* if 

	$$P(X_{t_1+\tau}, \ldots, X_{t_k+\tau}) = P(X_{t_1}, \ldots, X_{t_k})$$
	
- A Markov chain is *stationary* if it has an invariant probability measure and that is also its initial distribution.

- *(Birkhoff Ergodic Theorem)* Every *irreducible stationary* Markov chain $(X_t)$ is *ergodic*, that is, for any real-valued measurable function $f$:

	$$\frac{1}{n} \sum_{i=1}^n f(X_i) \xrightarrow{a.s.} E_\pi[f(X)], \ \text{ as } n \rightarrow \infty.$$
	
	where $\pi$ is the invariant probability measure.

- If $Markov(\pi, P)$ is a stationary Markov chain, then $Markov(\pi, P_q)$ is also a stationary Markov chain.

---

# Convergence of Measures #

- For a *positive Harris chain* $Markov(\pi_0, P)$ with invariant probability measure $\pi_*$, and $\pi_t = \pi_0 P^t$, we have

	$$\|\pi_t - \pi_*\|_{TV} \rightarrow 0, \ \text{ as } t \rightarrow \infty.$$
	
- As an immediate corollary, we have

	$$\|P^t(x, \cdot) - \pi_*\|_{TV} \rightarrow 0, \ \text{ as } t \rightarrow \infty.$$

. . .

- The chain is called *geometric ergodic* if there exist a nonnegative function $M$ and $\rho \in (0, 1)$ such that

	$$\|P^t(x, \cdot) - \pi_*\| \le M(x) \rho^t, \ \forall x \in \Omega.$$
	
---


