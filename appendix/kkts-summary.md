# KKT conditions: summary

## Standard form formulation

Consider the following general inequality and equality constrained optimisation problem written in a standard form:

\begin{align}
    \text{min.} \; & f(x) \\
    \text{s.t.} \; & h_i(x) = 0 \quad (\lambda_i) \quad \forall i \in \{1,2,...,m\}  \\
    & g_j(x) \leq 0 \quad (\mu_j) \quad \forall j \in \{1,2,...,n\}
\end{align}

There are $m$ equality constraints associated with Lagrange multipliers $\lambda_i$ and $n$ inequality constraints associated with Lagrange multipliers $\mu_j$.

## Lagrangian

\begin{equation}
    \mathcal{L} = f(x) + \sum_{i=1}^m \lambda_i \cdot h_i(x) + \sum_{j=1}^{n} \mu_j \cdot g_j(x)
\end{equation}

The Lagrangian has three components: the original objective function, the equality constraints multiplied by their Lagrange multipliers, and the inequality constraints multiplied by their Lagrange multipliers.

## KKT Conditions

\begin{align}
    & \frac{\partial \mathcal{L}}{\partial x} = 0   \quad & (\text{Optimality conditions})\\
    & \frac{\partial \mathcal{L}}{\partial \lambda_i} = h_i(x) = 0 \quad \forall i \in  \{1,2,...,m\}  \quad &  (\text{Primal feasibility}) \\
    & g_j(x) \leq 0 \quad \forall j \in  \{1,2,...,n\}  \quad & (\text{Primal feasibility}) \\
    & \mu_j \cdot g_j(x) =  0 \quad \forall j \in  \{1,2,...,n\}  \quad & (\text{Complementary slackness conditions}) \\
    & \mu_j \geq 0 \quad \forall j \in  \{1,2,...,n\} & (\text{Dual feasibility})
\end{align}

Let's look at each of these equations in a little more detail. We have:
1. Derivative of Lagrangian w.r.t. decision variables $x$ equal to zero $\rightarrow$ optimality conditions
2. Derivative of Lagrangian w.r.t. Lagrange multipliers $\lambda_i$ (equality constraints) $\rightarrow$ primal feasibility (solution is feasible with respect to the primal constraints)
3. Derivative of Lagrangian w.r.t. Lagrange multipliers $\mu_j$ (inequality constraints) $\rightarrow$ primal feasibility
4. The multiplication of a Lagrange multiplier with its associated inequality constraint is zero $\rightarrow$ complementary slackness conditions (indicates that in some cases the inequality constraints might not be binding)
5. Lagrange multipliers $\mu_j$ need to be positive or zero $\rightarrow$ dual feasibility

:::{admonition} Interpretation of the complementary slackness conditions
:class: important

If a constraint is binding, we can replace the inequality sign with an equality sign, so we have $g_j(x) = 0$. Then, the Lagrange multiplier $\mu_j$ may take on any non-zero value ($\mu_j \geq 0$), and the constraint $\mu_j \cdot g_j(x) = 0$ will be satisfied. If the constraint is non-binding ($g_j(x) < 0$), the Lagrange multiplier will equal zero ($\mu_j = 0$). Otherwise the constraint $\mu_j \cdot g_j(x) = 0$ would be violated. Note that these constraints are non-linear.
:::

The KKT conditions are a large set of equations. For simple cases addressed in this course, we can solve the problem by using trial-and-error. We try different combinations of constraints, come up with candidate solutions, then assess whether they are optimal or not. Depending on the problem, we reason which inequality constraints are likely to be binding. Then, we make them equality constraints, and their corresponding $\mu_j \neq 0$. For the non-binding inequality constraints, their corresponding $\mu_j = 0$. This can greatly simplify the KKT conditions. We will be left with as many equations as there are unknowns, so we can solve for $x$, $\lambda_i$, and $\mu_j$ to obtain the optimal solution to the problem. We can also check if there is alternative combination of binding/non-binding constraints that would yield a better solution.
