# One-pager summary: KKT conditions

## Unconstrained optimisation
Let's go back to basic optimisation (high school mathematics). Whenever you had to optimise (minimise or maximise) a function, you were doing unconstrained optimisation. To determine the optimum of a certain function, we should take the derivative of that function w.r.t. the decision variable $x$ and equate it to zero. Then we take the second order derivative to see if it is a minimum or maximum.

\begin{align}
    \min f(x) & \rightarrow & \frac{\partial f(x)}{\partial x} =  0 \quad \text{(necessary condition)} \\
    & & \frac{\partial^2 f(x)}{\partial x^2} > 0 \quad \text{(sufficient condition)} \\
    \max f(x) & \rightarrow & \frac{\partial f(x)}{\partial x} =  0 \quad \text{(necessary condition)} \\
    & & \frac{\partial^2 f(x)}{\partial x^2} < 0 \quad \text{(sufficient condition)} \\
\end{align}

## Equality constrained optimisation
Now consider an optimisation problem with an equality constraint, such as the demand constraint in an economic dispatch problem. To deal with the constraint, we introduce the Lagrangian. The Lagrangian elevates the constraint to the objective function.

Consider the following minimisation problem with equality constraints $h_i(x)$ written in standard form:
\begin{align}
    \text{min.} \; & f(x) \\
    \text{s.t.} \; & h_i(x) = 0 \quad (\lambda_i) \quad \forall i \in \{1,2,...,m\}
\end{align}
There are $m$ equality constraints. We associate a Lagrange multiplier $\lambda_i$ to each constraint.

The Lagrangian is:
\begin{equation}
    \mathcal{L} = f(x) + \sum_{i=1}^m \lambda_i \cdot h_i(x)
\end{equation}
The first part of the Lagrangian is the original objective function. Then we add the constraints multiplied by their Lagrange multipliers $\lambda_i$.

To find the optimal solution ($x^*, \lambda_i^*$), we draw on our knowledge of unconstrained optimisation, since now we have a single function, the Lagrangian, to minimise. We take the derivative of the Lagrangian w.r.t. the decision variables $x$ and w.r.t. the Lagrange multipliers $\lambda_i$. Notice that taking $\frac{\partial \mathcal{L}}{\partial \lambda_i} = 0$ recovers the equality constraints $h_i(x) = 0$.

\begin{align}
    & \frac{\partial \mathcal{L}}{\partial x} = 0 \\
    & \frac{\partial \mathcal{L}}{\partial \lambda_i} = h_i(x) = 0 \quad \forall i \in  \{1,2,...,m\}
\end{align}

Notice that now we have as many equations as we have unknowns, so we can solve for $x$ and $\lambda_i$, to obtain the optimal solution to the original optimisation problem.

## Inequality and equality constrained optimisation
In energy systems, we not only have equality constraints, but also inequality constraints. For example, capacity constraints in the economic dispatch problem. Sometimes inequality constraints are active/binding and sometimes they are not. To solve a problem with equality and inequality constraints, we first want to figure out which inequality constraints are active. We can replace these constraints with equality constraints. Then we have an equality constrained optimisation problem which we know how to solve.

However, for most problems, we do not know which constraints will be binding. So, we use a set of optimality conditions called Karush-Kuhn-Tucker (KKT) conditions to reflect the fact that in some cases inequality constraints are binding and in some cases they are not.

Consider the general inequality and equality constrained optimisation problem written in standard form:

\begin{align}
    \text{min.} \; & f(x) \\
    \text{s.t.} \; & h_i(x) = 0 \quad (\lambda_i) \quad \forall i \in \{1,2,...,m\}  \\
    & g_j(x) \leq 0 \quad (\mu_j) \quad \forall j \in \{1,2,...,n\}
\end{align}
There are $m$ equality constraints associated with Lagrange multipliers $\lambda_i$ and $n$ inequality constraints associated with Lagrange multipliers $\mu_j$.

:::{admonition} Standard Form
:class: note

In standard form, the constraints are written separately with a zero on the right-hand side. For equality constraints, we have "= 0". For inequality constraints, we have "$\leq$ 0" (not "$\geq$ 0"). We will write all problems in standard form first so it is easier to write the Lagrangian and KKT conditions.
:::

The Lagrangian is:
\begin{equation}
    \mathcal{L} = f(x) + \sum_{i=1}^m \lambda_i \cdot h_i(x) + \sum_{j=1}^{n} \mu_j \cdot g_j(x)
\end{equation}
The Lagrangian has three components: the original objective function, the equality constraints multiplied by their Lagrange multipliers, and the inequality constraints multiplied by their Lagrange multipliers.

### KKT Conditions
Then we derive the following set of equations that characterises the optimal solution. These are the KKT conditions.

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
