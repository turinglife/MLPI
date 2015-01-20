# Hamiltonian Monte Carlo

- A generic MCMC method based on *Hamiltonian Dynamics*.
- Originally, it was devised for *molecular simulation*

. . .

- In 1987, a seminal paper by Duane, Kennedy, Pendleton, and Roweth unifies MCMC and molecular dynamics. They called this method *Hybrid Monte Carlo*, which abbreviates to *HMC*
- In many articles, people call it *Hamiltonian Monte Carlo*, as this name is considered to be more specific and informative, and it retains the same abbreviation "HMC".

---

# Motivating Example: Free Fall #

\begin{center}
\includegraphics[width=0.9\textwidth]{imgs/freefall.png}
\end{center}

. . .

- The change of *momentum* $p$ is caused by the accumulation/release of the *potential energy*:

	$$\frac{dp}{dt} = m \frac{dv}{dt} = -mg = - \frac{\partial U(q)}{\partial q}$$

- The change of location $q$ is caused by *velocity*, which is the derivative of *kinematic energy* *w.r.t.* the *momentum*:

	$$\frac{dq}{dt} = v = \frac{\partial V(p)}{\partial p}$$

---


# Hamiltonian Dynamics #

- *Hamiltonian Dynamics* is a generalized theory of the *classical mechanics*, which provides a elegant and flexible abstraction of a dynamic system in physics.

. . .

- In Hamiltonian Dynamics, a physical system is described by $(\mathbf{q}, \mathbf{p})$, where $q_i$ and $p_i$ are respectively the *position* and *momentum* of the $i$-th entity. The dynamics of the system is characterized by the *Hamilton's Equations*:

	$$\frac{d \mathbf{p}}{dt} = - \frac{\partial H}{\partial \mathbf{q}}$$
	
	$$\frac{d \mathbf{q}}{dt} = \frac{\partial H}{\partial \mathbf{p}}$$
	
	Here, $H$ is called the *Hamiltonian*, which can be interpreted as the *total energy* of the system. 

---

# Hamiltonian Dynamics (cont'd) #

- The *Hamiltonian* $H$ can usually be decomposed into the sum of the *potential energy* $U$ and the *kinetic energy* $V$, as

	$$H(\mathbf{q}, \mathbf{p}) = U(\mathbf{q}) + V(\mathbf{p})$$  

- With this setting, the *Hamilton's Equations* can be written as:

	$$\frac{d \mathbf{p}}{dt} = - \nabla_{\mathbf{q}} U(\mathbf{q})$$
	
	$$\frac{d \mathbf{q}}{dt} = \nabla_{\mathbf{p}} V(\mathbf{p})$$

---

# Conservation of Hamiltonian #

- The *Hamiltonian* is *conserved*, *i.e.*, it is *invariant* over time:

	$$\frac{dH}{dt} =
	\sum_{i=1}^n \left(
		\frac{dq_i}{dt} \frac{\partial H}{\partial q_i} + 
		\frac{dp_i}{dt} \frac{\partial H}{\partial p_i}
	\right) = 
	\sum_{i=1}^n \left(
		\frac{\partial H}{\partial p_i} \frac{\partial H}{\partial q_i} -
		\frac{\partial H}{\partial q_i} \frac{\partial H}{\partial p_i}
	\right) = 0$$

- Intuitively, this reflects the *law of energy conservation*.

. . .

- In the context of MCMC, this leads to high acceptance rate of the proposals.

---

# Reversibility of Hamiltonian Dynamics #

- The *Hamiltonian dynamics* is *reversible*
	- Let the initial states be $(q, p)$ and the states at time $t$ be $(q', p')$. Then, it we reverse the *process*, starting at $(q', -p')$, then the states at time $t$ would be $(q, -p)$.

. . .

- In the context of MCMC, this leads to the *reversibility* of the underlying chain.

---

# Computer Simulation of Hamiltonian Dynamics #

- A natural idea to simulate *Hamiltonian dynamics* is to use *Euler's method* over discretized time steps (with step size $\epsilon$):

	$$p_i(t + \epsilon) = p_i(t) + \epsilon \frac{dp_i}{dt} = p_i(t) - \epsilon \frac{\partial U}{\partial q_i}(\mathbf{q}(t))$$
	
	$$q_i(t + \epsilon) = q_i(t) + \epsilon \frac{dq_i}{dt} = q_i(t) + \epsilon \frac{\partial V}{\partial p_i}(\mathbf{p}(t))$$

- Is this a good method?

---

# Leapfrog Method #

- Better results can be obtained with the *leapfrog* method:

	$$p_i(t + \epsilon/2) = p_i(t) - (\epsilon/2) \frac{\partial U}{\partial q_i}(\mathbf{q}(t))$$
	
	$$q_i(t + \epsilon) = q_i(t) + \epsilon \frac{\partial V}{\partial p_i}(\mathbf{p}(t + \epsilon / 2))$$
	
	$$p_i(t + \epsilon) = p_i(t + \epsilon / 2) - (\epsilon/2) \frac{\partial U}{\partial q_i}(\mathbf{q}(t + \epsilon))$$

\begin{center}
\includegraphics[width=0.42\textwidth]{imgs/leapfrog.png}
\end{center}

- More importantly, the *leapfrog* update is *reversible*.

---

# Example #

- Consider a Hamiltonian system:

	$$H(q, p) = U(q) + V(p), \quad U(q) = p^2 / 2, \ \ V(p) = p^2 / 2$$

- The dynamics are described by the *Hamilton's Equations*:

	$$\frac{dq}{dt} = p, \quad \frac{dp}{dt} = -q$$

- Analytic Solution:

	$$q(t) = \rho \cos(t + \tau_0), \quad p(t) = -\rho \sin(t + \tau_0)$$

---

# Example (Simulation) #

\begin{center}
\includegraphics[width=0.98\textwidth]{imgs/leapfrogc.png}
\end{center}

---

# MCMC with Hamiltonian Dynamics #

- **(Basic idea):** Consider the *potential energy* as the *Gibbs energy*, and introduce the *"momentums"* as *auxiliary variables* to control the dynamics. 

. . .

- Suppose the *target distribution* is $\pi(q) = \frac{1}{Z} \exp \left( - U(q) \right)$, then we form an *augmented distribution* as 

	$$P(\mathbf{q}, \mathbf{p}) = \frac{1}{Z'} \exp \left( - H(\mathbf{p}, \mathbf{q}) \right) = \frac{1}{Z'} \exp \left( - U(\mathbf{q}) \right) \exp \left( - V(\mathbf{p}) \right)$$
	
	Here, the *locations* $\mathbf{q}$ represent the variables of interest, and the *momentums* $\mathbf{p}$ control the dynamics of simulation.

- In practice, the *kinetic* energy is often formalized as 

	$$V(\mathbf{p}) = \sum_{i=1}^n \frac{p_i^2}{m_i}.$$

---

# Hamiltonian Monte Carlo #

Each iteration of HMC comprises two steps:

1. *Gibbs update*: sample the *momentums* $\mathbf{p}$ from the Gaussian prior given by 

	$$P(\mathbf{p}) \propto \exp \left(- V(\mathbf{p})\right).$$

2. *Metropolis update*: using Hamiltonian dynamics to propose a new state. Starting from $(\mathbf{q}, \mathbf{p})$, simulate the dynamic system with the leapfrog method for $L$ steps with step-size $\epsilon$, which yields $(\mathbf{q}', \mathbf{p}')$. The proposed state is accepted with probability:

	$$\min \left\{1, \exp\left(H(\mathbf{q}, \mathbf{p}) - H(\mathbf{q}', \mathbf{p}') \right)\right\}$$

. . .

**Note:** If the simulation is *exact*, we will have $H(\mathbf{q}, \mathbf{p}) = H(\mathbf{q}', \mathbf{p}')$, and thus the proposed state should always be accepted. However, in practice, there can be some deviation due to discretization, we have to use the Metropolis rule to guarantee the correctness.

---

# Hamiltonian Monte Carlo (Discussion) #

- HMC has a high acceptance rate (due to *conservation of Hamiltonian*) while allowing large moves along less-constrained directions at each iteration. 
	- This is a key advantage as compared to *random walk* proposals, which, in order to maintain a reasonably high acceptance rate, has to keep a very small step size, resulting in substantial correlation between consecutive samples.

\begin{center}
\includegraphics[width=0.6\textwidth]{imgs/hmcex.png}
\end{center}

---

# Tuning HMC #

- For efficient simulation, it is important to choose appropriate values for both the leapfrog step size $\epsilon$ and the number of leapfrog steps at each iteration $L$. 

. . .

- Tuning HMC (and actually many generic sampling methods) often requires *preliminary runs* with different trial settings and different initial values, as well as careful analysis of the energy trajectories. 

. . .

- For most cases, $\epsilon$ and $L$ can be tuned *independently*. 
	- Too small a stepsize would waste computation time, while large stepsize would cause unstable simulation, and thus low acceptance rate. 
	- One should choose $\epsilon$ such that the energy trajectory is stable and the acceptance rate is maintained at a reasonably high level.
	- One should choose $L$ such that back-and-forth movement of the states can be observed. 

