---
title: Lecture 1 - Overview of Machine Learning
shorttitle: Lecture 1
---

# About this Course #

- This is a *graduate level* introduction to *statistical learning*. 
- The course is *not* to teach you:
	- Support Vector Machine
	- Linear Regression
	- ...
	- Deep Learning
- Instead, you are going to learn *foundational tools* for developing *your own* models and algorithms.

---

# Course Format #

- **No Exams!**
- Topic driven
- For each topic:
	- Introductory lecture
	- Paper reading and Homework
	- In-class discussion
- You will present a paper/subject at the end of the course

---

# What is _Machine Learning_? #

> **Machine learning** is a scientific discipline that explores the construction and study of algorithms that can learn from data. Such algorithms operate by building a model based on inputs and using that to make predictions and decisions, rather than following only explicitly programmed instructions.   -- Wikipedia

---

# Elements of Machine Learning #

- Elements:
	- Data
	- Model
	- Learning Algorithms
	- Prediction
	
- Learn from old data, make predictions on new data. The common aspects of both the old and new data are captured by the model.

---

Please write down five machine learning algorithms that you know

Don't write *Deep Learning*!

---

# Overview of Machine Learning #

- Tasks
	- Supervised learning
	- Unsupervised learning
	- Semi-supervised learning
	- Reinforcement learning
	
- Problems
	- Classification
	- Regression
	- Clustering
	- Dimension Reduction
	- Density Estimation

---

# Topics #

- Exponential family distributions and conjugate prior
- Generalized linear model
- Empirical risk minimization and Stochastic gradient descent 
- Proximal methods for optimization
- Graphical models: Bayesian Networks and Markov random fields
- Sum-product and max-product algorithms, Belief propagation
- Variational inference methods
- Markov Chain Monte Carlo
- Gaussian Processes and Copula Processes
- Handling Big Data: Streaming process and Core sets

---

Let's take a five-minute break.

---

# Math Prerequisites #

- Machine Learning is a subject that involves a lot of math
	- Especially true when you want to develop your own methods instead of calling something out of box.
- You should have learned:
	- Calculus
	- Linear algebra
	- (Classical) Probability theory and Statistics
	- Basic knowledge about Optimization
- Are these sufficient? 

---

# You Probably Need to Know More #

Let's look at an example -- the notion of *kernel* plays a crucial role in modern learning theory. 

Given a *measure space* $(\Omega, \mu)$, a *positive definite kernel* $K: \Omega \times \Omega \rightarrow \mathbb{R}$ is a *symmetric map* that is *L2-integrable*, meaning

$$\int_X \int_X K(x, y)^2 d\mu(x) d\mu(y) < +\infty, \ \forall x, y \in X,$$

and satisfies

$$\sum_{i=1}^n \sum_{j=1}^n a_i a_j K(x_i, x_j) > 0$$

for arbitrary finite subset $x_1, \ldots, x_n \in X$ and non-zero vector $(a_1, \ldots, a_n)$.

---

# You Probably Need to Know More (cont'd) #

Let $\mathcal{H}$ be a *Hilbert space* of real-valued functions defined on $X$. We can define a *linear functional* $F_x$ for each $x \in X$ as

$$F_x: f \mapsto f(x), \ \forall f \in \mathcal{H}.$$

Then $\mathcal{H}$ is called a *Reproducing Kernel Hilbert Space (RKHS)*, if $F_x$ is a *bounded operator* for any $x \in X$.

$$\quad$$

Each *positive definite kernel* $K$ defined on $X$ induces a *Reproducing Kernel Hilbert Space (RKHS)* such that 

$$K(x, y) = \langle K_x, K_y \rangle_{\mathcal{H}}$$

where $K_x: y \mapsto K(x, y)$.

---

# You Probably Need to Know More (cont'd) #

In these statements, we came across several concepts:

- Measure space
- L2-integrable, which means 

	$$\int_X f^2(x) d\mu(x) < +\infty$$
	But, then how can you do integration over arbitrary measure spaces?
- Hilbert space
- Linear functional
- Inner product between two functions
- Bounded operator

---

# What You Need to Know #

In addition to what you have learned in undergraduate, you probably need some exposure to these subjects:

- Basics of Functional analysis
	- *metric*, *norm*, *inner product*, *Banach space*, *Hilbert space*
	- *linear functional*, *operator*, *spectrum*
	- *strong convergence*, *weak convergence*
- Basics of Measure theory
	- *measurable space*, *measure*, *probability measure*
	- *almost everywhere*, *almost surely*
	- *integration*, *L1-integrable*, *L2-integrable*
- Basics of Convex optimization
	- *convex set*, *convex function*, *convex conjugate*
	- *Lagrange multiplier*
	- *strong duality*, *weak duality*

---




