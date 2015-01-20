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

**Slice Sampling**

---

# Slice Sampler #

- Sampling $x \sim p(x)$ is equivalent to sampling uniformly from the area under $p(x)$: $\mathcal{A} = \{(x, y): 0 \le y \le f(x)\}$.

. . .   

- Gibbs sampling based on the uniform distribution over $\mathcal{A}$. Each iteration consists of two steps:
    - Given $x$, $y \sim \mathrm{Uniform}([0, f(x)])$
    - Given $y$, $x \sim \mathrm{Uniform}(\{x: f(x) \ge y\})$

\begin{center}
\includegraphics[width=0.5\textwidth]{imgs/slicesample.png}
\end{center}

---

# Slice Sampler (Discussion) #

- *Slice sampler* can mix very rapidly, as it will not be locally trapped.

. . .

- *Slice sampler* is often very difficult to implement in practice. 
    - For many distributions, drawing $x \sim \mathrm{Uniform}(\{x: f(x) \ge y\})$ is no less difficult than drawing directly from the original distribution.

. . .

- For distributions of certain forms, which have an *easy way* to draw $x \sim \mathrm{Uniform}(\{x: f(x) \ge y\})$, *slice sampling* is good strategy. 
    - **Note:** In the step to draw $x$ (given $y$), one can use MCMC.

---

# Generative Model With Gaussian Prior #

- Consider a generative model with Gaussian prior:
    - prior: $\boldsymbol{\theta} \sim \mathcal{N}(\mathbf{0}, \boldsymbol{\Sigma})$
    - likelihood: $L(\boldsymbol{\theta}) = \prod_{i=1}^n p(\mathbf{x}_i | \boldsymbol{\theta})$

- Hence the posterior distribution has a density proportional to $\exp\left(- \frac{1}{2} \boldsymbol{\theta}^T \boldsymbol{\Sigma}^{-1} \boldsymbol{\theta}\right) L(\boldsymbol{\theta})$

. . .

- If the likelihood model is non-Gaussian, sampling from this posterior is often nontrivial. 

---

# Metropolis Algorithm #

We begin with the Metropolis algorithm. In each iteration

- Propose a new state: $\boldsymbol{\theta}' = \boldsymbol{\theta} \cos(\alpha) + \boldsymbol{\nu} \sin(\alpha)$ with $\boldsymbol{\nu} \sim \mathcal{N}(\mathbf{0}, \boldsymbol{\Sigma})$
    - Here, $\alpha$ is the *(circular) step size*
    - When $\alpha = \pm \pi$, it is a new draw from the prior, when $\alpha$ is close to $0$, it is a conservative perturbation of the original state. 

. . .

- How can you decide the step size $\alpha$?

. . .

- It is desirable to have an algorithm that can *adaptively* choose the step size. 
    - A natural idea: incorporate $\alpha$ as an *auxiliary variable*.

---

# Elliptical Slice Sampling (One Update Iteration) #

\begin{center}
\includegraphics[width=0.85\textwidth]{imgs/essalg1.png}
\end{center}


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

