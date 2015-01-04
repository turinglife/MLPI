---
title: Lecture 1 - Mathematics of Metrics
shorttitle: Lecture 1
---

# Metrics #

- Measurement of *distances* or *deviation* lies at the heart of many learning problems.
- Given an arbitrary set $\Omega$, a real-valued function $d: \Omega \times \Omega \mapsto \mathbb{R}$ is called a *metric*, if it satisfies:
	- *(non-negativity)* $d(x, y) \ge 0, \ \forall x, y \in \Omega$
	- *(coincidence axiom)* $d(x, y) = 0 \Leftrightarrow x = y$
	- *(symmetry)* $d(x, y) = d(y, x), \ \forall x, y \in \Omega$
	- *(triangle inequality)* $d(x, y) + d(y, z) \ge d(x, z), \ \forall, x, y, z \in \Omega$
- A set $\Omega$ together with a metric $d$ defined thereon is called a *metric space*, denoted by $(\Omega, d)$.
- Let $d_1, d_2, \ldots, d_n$ be metrics on $\Omega$, and $\alpha_1, \ldots, \alpha_n \ge 0$ with at least one non-zero values, then $\alpha_1 d_1 + \cdots + \alpha_n d_n$ remains a metric.

