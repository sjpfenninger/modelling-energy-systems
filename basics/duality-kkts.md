# Duality and KKTs

## Duality

... more to be added ...

:::{admonition} Strong and weak duality
:class: note

Weak duality means that the solution to any primal minimisation problem is always greater than or equal to the solution of the corresponding dual (maximisation) problem. Under certain conditions - and this includes the condition that we are dealing with linear optimisation - we also see strong duality, which means that the solution of the primal problem is **equal to** the solution of the dual problem. We only deal with the linear case here, where strong duality always applies, so we do not consider this distinction further.
:::

<!-- We have already discussed duality in linear programming problems. In this course, we focus on convex optimisation problems. Recall that for any primal problem, there exists a corresponding dual problem. For the optimal solution of the problem, the primal objective and dual objective are the same. This is called strong duality. The optimal values of the primal decision variables are the shadow prices, or Lagrange multipliers, of the dual problem, and vice versa. We also learned how to convert a primal problem into a dual problem using tables or by rewriting the primal problem in standard form for which the dual problem is known. -->

## Karush-Kuhn-Tucker (KKT) conditions

### Unconstrained optimisation

Let's go back to basic optimisation (high school mathematics). Whenever you had to optimise (minimise or maximise) a function, you were doing unconstrained optimisation. To determine the maximum or minimum of a certain function, we should take the derivative of that function w.r.t. the decision variable $x$ and equate it to zero (necessary condition for optimality). Then we take the second order derivative to see if it is a minimum or maximum (sufficient condition). If there are multiple variables, we take partial derivatives.

\begin{align}
    \min f(x) & \rightarrow & \frac{\partial f(x)}{\partial x} =  0 \quad \text{(necessary condition)} \\
    & & \frac{\partial^2 f(x)}{\partial x^2} > 0 \quad \text{(sufficient condition)} \\
    \max f(x) & \rightarrow & \frac{\partial f(x)}{\partial x} =  0 \quad \text{(necessary condition)} \\
    & & \frac{\partial^2 f(x)}{\partial x^2} < 0 \quad \text{(sufficient condition)} \\
\end{align}

A point that satisfies the necessary condition for optimality ($\frac{\partial f(x)}{\partial x} =  0$) is called a stationary point. For convex optimisation problems, we never use the sufficient condition because any stationary point will be a minimum.

### Economic dispatch example Part I: unconstrained optimisation and equality constrained optimisation

In energy systems, unfortunately we do not deal with many unconstrained optimisation problems---usually there are at least a few constraints. Consider the example of economic dispatch that we have studied. We will build up the complexity of the problem throughout this document to illustrate how we can use duality and KKT conditions to solve such problems and interpret their solutions.

Consider two generators $G_1$ and $G_2$ with cost structures $C_1(g_1) = a_1 + b_1 \cdot g_1^2$ and $C_2(g_2) = a_2 + b_2 \cdot g_2^2$. Note that the cost functions are quadratic _not_ linear. This is quite typical in power systems. So we have a quadratic programming problem, but it is still a convex programming problem. Therefore, the techniques we use here also apply to linear programming problems. We need to dispatch the generators to meet a load $L$ at minimal cost. We will ignore the capacity constraints of the generators for now. Thus, we have the following optimisation problem:

\begin{align}
    & \text{min.} \quad a_1 + b_1 \cdot g_1^2+ a_2 + b_2 \cdot g_2^2 \\
    & \text{s.t.} \quad g_1 + g_2 = L
\end{align}

If we do not consider the equality constraint $g_1 + g_2 = L$ then the optimal solution to this problem (what minimises operating cost of the system) is $g_1^* = 0$, $g_2^*=0$, i.e. not run the generators at all. You can easily confirm this with the necessary condition for optimality: take the derivative of the objective function w.r.t. $g_1$ and $g_2$, equate those expressions to zero, and solve for $g_1$ and $g_2$. This is the unconstrained optimisation previously discussed.

To deal with the constraint in our optimisation problem, we introduce the Lagrangian. The Lagrangian elevates the constraint to the objective function.

\begin{equation}
    \mathcal{L} = (a_1 + b_1 \cdot g_1^2+ a_2 + b_2 \cdot g_2^2) + \lambda \cdot (L - g_1 - g_2)
\end{equation}

The first part of the Lagrangian is the original objective function. Then we add the constraint multiplied by a Lagrange multiplier $\lambda$. We want to find an optimal value of $\lambda$ that coordinates the decision of $g_1$ and $g_2$ to ensure that the constraint $L = g_1^* + g_2^*$ is met at minimum cost.

To do this, we draw on our knowledge of unconstrained optimisation, since now we have a single function, the Lagrangian, to minimise. Thus, we take the first derivative of the Lagrangian w.r.t. $g_1$ and $g_2$ and $\lambda$:

\begin{align}
    & \frac{\partial \mathcal{L}}{\partial g_1} = 2 \cdot b_1 \cdot g_1 - \lambda = 0  \\
    & \frac{\partial \mathcal{L}}{\partial g_2} = 2 \cdot b_2 \cdot g_2 - \lambda = 0  \\
    & \frac{\partial \mathcal{L}}{\partial \lambda} = L - g_1 - g_2 = 0
\end{align}

Notice that now we have three equations and three unknowns. So, we can solve for $g_1$, $g_2$, and $\lambda$, which gives the optimal solution to the original optimisation problem.

### Equality constrained optimisation

Now we will generalise the Lagrangian to any equality constrained optimisation problem. Consider the following minimisation problem with equality constraints $h_i(x)$:
\begin{align}
    \text{min.} \; & f(x) \\
    \text{s.t.} \; & h_i(x) = 0 \quad (\lambda_i) \quad \forall i \in \{1,2,...,m\}
\end{align}
The equality constraints are written in standard form (as introduced in {numref}`content:lp:economic-dispatch`), so we have "= 0" on the right-hand side. There are $m$ equality constraints. We associate a Lagrange multiplier $\lambda_i$ to each constraint.

The Lagrangian is then:
\begin{equation}
    \mathcal{L} = f(x) + \sum_{i=1}^m \lambda_i \cdot h_i(x)
\end{equation}

We can find the optimal solution ($x^*, \lambda_i^*$) to the original optimisation problem by taking the derivative of the Lagrangian w.r.t. the decision variables $x$ and w.r.t. the Lagrange multipliers $\lambda_i$. Notice that taking $\frac{\partial \mathcal{L}}{\partial \lambda_i} = 0$ recovers the equality constraints $h_i(x) = 0$.

\begin{align}
    & \frac{\partial \mathcal{L}}{\partial x} = 0 \\
    & \frac{\partial \mathcal{L}}{\partial \lambda_i} = h_i(x) = 0 \quad \forall i \in  \{1,2,...,m\}
\end{align}

#### Graphical interpretation

The equality constrained optmisation problem also has a graphical interpretation. {numref}`fig:KKT_eqconst_graphical` shows the graphical interpretation of our economic dispatch example.

```{figure} ../images/KKT_eqconst_graphical.png
:name: fig:KKT_eqconst_graphical
:figwidth: 400 px

Graphical representation of the equality constrained economic dispatch problem
```

$g_1$ and $g_2$ are on the axes. The red contour lines are constant values of the objective function, or total operating cost. The total operating cost increases as $g_1$ and $g_2$ increase. The blue line is the equality constraint. The green dot is the optimal solution. At this point, the gradient of the objective function $\nabla f(x)$ (red arrow) is 1) perpendicular to the constraint and 2) parallel to the gradient of the constraint $\nabla h(x)$ (blue arrow). This can be expressed as:
\begin{equation}
    \nabla f(x) + \lambda \cdot \nabla h(x) = 0
\end{equation}

### Economic dispatch example Part II: inequality and equality constrained optimisation

In energy systems, we not only have equality constraints, but also inequality constraints. For example, returning to the economic dispatch example, the generators have capacity constraints $\overline{G_1}$ and $\overline{G_2}$ and cannot run at negative output (lower bound of zero). The optimisation problem becomes:

\begin{align}
    \text{min.} \; & a_1 + b_1 \cdot g_1^2+ a_2 + b_2 \cdot g_2^2 \\
    \text{s.t.} \; & g_1 + g_2 = L  \\
    & 0 \leq g_1 \leq \overline{G_1}  \\
    & 0 \leq g_2 \leq \overline{G_2}
\end{align}

To solve the problem with equality and inequality constraints, we extend our graphical interpretation. The grey area in {numref}`fig:KKT_eqconst_ineqconst_graphical` is the feasible region because it represents the feasible range of output of $g_1$ and $g_2$. The set of feasible solutions---the values of $g_1$ and $g_2$ that satisfy both the equality and inequality constraints---lie on the blue line within the grey area.

```{figure} ../images/KKT_eqconst_ineqconst_graphical.png
:name: fig:KKT_eqconst_ineqconst_graphical
:figwidth: 400 px

Graphical representation of the equality and inequality constrained economic dispatch problem
```

The optimal solution needs to be part of the feasible solution set. In this case, we see that the optimal solution (green dot) is indeed in the feasible area. Thus the inequality constraints $0 \leq g_1 \leq \overline{G_1}$ and $0 \leq g_2 \leq \overline{G_2}$ actually do not play a role in this particular example.

However, this is not always the case. What if the capacity limits on $g_1$ and $g_2$ do play a role? Then we want to figure out which inequality constraints are active. We can replace these constraints with equality constraints. Then we have an equality constrained optimisation problem which we know how to solve.

### Inequality and equality constrained optimisation

For most problems, we do not know which constraints will be active/binding. Luckily, we can use a set of optimality conditions called Karush-Kuhn-Tucker (KKT) conditions to reflect the fact that in some cases inequality constraints are binding and in some cases they are not.

Consider the general inequality and equality constrained optimisation problem written in standard form:

\begin{align}
    \text{min.} \; & f(x) \\
    \text{s.t.} \; & h_i(x) = 0 \quad (\lambda_i) \quad \forall i \in \{1,2,...,m\}  \\
    & g_j(x) \leq 0 \quad (\mu_j) \quad \forall j \in \{1,2,...,n\}
\end{align}
There are $m$ equality constraints associated with Lagrange multipliers $\lambda_i$ and $n$ inequality constraints associated with Lagrange multipliers $\mu_j$.

The Lagrangian is:
```{math}
:label: eqn:Lagrangian
\begin{equation}
    \mathcal{L} = f(x) + \sum_{i=1}^m \lambda_i \cdot h_i(x) + \sum_{j=1}^{n} \mu_j \cdot g_j(x)
\end{equation}
```
To formulate the Lagrangian, we followed the same logic as before: elevate the equality _and_ inequality constraints to the Lagrangian. The Lagrangian has three components: the original objective function, the equality constraints multiplied by their Lagrange multipliers, and the inequality constraints multiplied by their Lagrange multipliers.

Then we derive the following set of equations that characterises the optimal solution. These are the KKT conditions.

```{math}
:label: eqn:KKT
\begin{align}
    & \frac{\partial \mathcal{L}}{\partial x} = 0   \quad & (\text{Optimality conditions})\\
    & \frac{\partial \mathcal{L}}{\partial \lambda_i} = h_i(x) = 0 \quad \forall i \in  \{1,2,...,m\}  \quad &  (\text{Primal feasibility}) \\
    & g_j(x) \leq 0 \quad \forall j \in  \{1,2,...,n\}  \quad & (\text{Primal feasibility}) \\
    & \mu_j \cdot g_j(x) =  0 \quad \forall j \in  \{1,2,...,n\}  \quad & (\text{Complementary slackness conditions}) \\
    & \mu_j \geq 0 \quad \forall j \in  \{1,2,...,n\} & (\text{Dual feasibility})
\end{align}
```

Let's look at each of these equations in a little more detail. We have:
1. Derivative of Lagrangian w.r.t. decision variables $x$ equal to zero $\rightarrow$ optimality conditions
2. Derivative of Lagrangian w.r.t. Lagrange multipliers $\lambda_i$ (equality constraints) $\rightarrow$ primal feasibility (solution is feasible with respect to the primal constraints)
3. Derivative of Lagrangian w.r.t. Lagrange multipliers $\mu_j$ (inequality constraints) $\rightarrow$ primal feasibility
4. The multiplication of a Lagrange multiplier with its associated inequality constraint is zero $\rightarrow$ complementary slackness conditions (indicates that in some cases the inequality constraints might not be binding)
5. Lagrange multipliers $\mu_j$ need to be positive or zero $\rightarrow$ dual feasibility

Let's look more carefully at the interpretation of the complementary slackness conditions---the last two constraints in Equation {eq}`eqn:KKT`:

\begin{align}
    & \mu_j \cdot g_j(x) =  0 \quad \forall j \in  \{1,2,...,n\}  \\
    & \mu_j \geq 0 \quad \forall j \in  \{1,2,...,n\}
\end{align}

If a constraint is binding, we can replace the inequality sign with an equality sign, so we have $g_j(x) = 0$. Then, the Lagrange multiplier $\mu_j$ may take on any non-zero value ($\mu_j \geq 0$). Since $g_j(x) = 0$ in this case, the constraint $\mu_j \cdot g_j(x) = 0$ will be satisfied no matter the value of $\mu_j$. On the other hand, if the constraint is non-binding ($g_j(x) < 0$), the Lagrange multiplier will equal zero ($\mu_j = 0$). Otherwise the constraint $\mu_j \cdot g_j(x) = 0$ would be violated. This shows that an inequality constraint can only affect the optimal solution if it is binding. Note that these constraints are non-linear.

Now we want to find a solution to the set of equations (values for $x$, $\lambda_i$, and $\mu_j$). For most, but not all, convex problems, these conditions are sufficient and necessary conditions for optimality, so the obtained solution would be an optimal solution.

Note that sometimes KKT conditions are written in condensed form:
\begin{align}
    & \nabla f(x) + \sum_{i=1}^m \lambda_i \cdot \nabla h_i(x) + \sum_{j=1}^{n} \mu_j \cdot \nabla g_j(x) = 0  \\
    & \mu_j \cdot g_j(x) =  0 \quad \forall j \in  \{1,2,...,n\}  \\
    & \mu_j \geq 0 \quad \forall j \in  \{1,2,...,n\}
\end{align}

### Economic dispatch example Part III: KKT conditions

Let's revisit the economic dispatch example and apply KKT conditions. In standard form, the constraints are written separately with a zero on the right-hand sign and "=" or "$\leq$" signs:
\begin{align}
    \text{min.} \; & a_1 + b_1 \cdot g_1^2+ a_2 + b_2 \cdot g_2^2 &  \\
    \text{s.t.} \; & g_1 + g_2 - L = 0 \quad &(\lambda) \\
    &  - g_1 \leq 0 \quad &(\mu_1) \\
    &  g_1 - \overline{G_1} \leq 0 \quad &(\mu_2) \\
    &  - g_2 \leq 0 \quad &(\mu_3)  \\
    &  g_2 - \overline{G_2} \leq 0 \quad &(\mu_4)
\end{align}

This makes it easy to write the Lagrangian following Equation {eq}`eqn:Lagrangian`:
\begin{align}
    \mathcal{L} = & a_1 + b_1 \cdot g_1^2+ a_2 + b_2 \cdot g_2^2 + \lambda \cdot ( g_1 + g_2 - L ) \\
    & + \mu_1 \cdot ( - g_1) + \mu_2 \cdot ( g_1 - \overline{G_1})  \\
    & + \mu_3 \cdot ( - g_2 ) + \mu_4 \cdot ( g_2 - \overline{G_2})
\end{align}

Then we derive the KKT conditions:
\begin{align}
    & \frac{\partial \mathcal{L}}{\partial g_1} = 2 \cdot b_1 \cdot g_1 + \lambda - \mu_1 + \mu_2 = 0 \quad & (\text{Optimality conditions}) \\
    & \frac{\partial \mathcal{L}}{\partial g_2} = 2 \cdot b_2 \cdot g_2 + \lambda - \mu_3 + \mu_4 = 0 \quad & (\text{Optimality conditions}) \\
    & \frac{\partial \mathcal{L}}{\partial \lambda} = g_1 + g_2 - L = 0 \quad &  (\text{Primal feasibility (equality constraint)}) \\
    &  - g_1 \leq 0 \quad & (\text{Primal feasibility (inequality constraint}) \\
    &  g_1 - \overline{G_1} \leq 0  \quad & (\text{Primal feasibility (inequality constraint}) \\
    &  - g_2 \leq 0  \quad & (\text{Primal feasibility (inequality constraint}) \\
    &  g_2 - \overline{G_2} \quad & (\text{Primal feasibility (inequality constraint}) \\
    & \mu_1 \cdot ( - g_1) = 0  \quad & (\text{Complementary slackness conditions}) \\
    & \mu_2 \cdot ( g_1 - \overline{G_1}) = 0 \quad & (\text{Complementary slackness conditions}) \\
    & \mu_3 \cdot ( - g_2 )  = 0 \quad & (\text{Complementary slackness conditions}) \\
    & \mu_4 \cdot ( g_2 - \overline{G_2}) = 0 \quad & (\text{Complementary slackness conditions}) \\
    & \mu_1, \mu_2, \mu_3, \mu_4 \geq 0 \quad & (\text{Dual feasibility})
\end{align}

Clearly, this is a large set of equations. This problem is not trivial to solve because the complementary slackness constraints are non-linear. For simple cases addressed in this course, we can solve the problem by using trial-and-error: "What if a certain constraint $g_j(x)$ is binding? Does that lead to a feasible solution? Is the solution optimal?" In this example, there are four inequality constraints so in theory there are 16 ($=2^4$) possible combinations. However, some combinations are not possible, for example if $g_1 = 0$, then $g_1 \neq \overline{G_1}$. By trying different combinations of constraints, we come up with candidate solutions, then assess whether they are optimal or not.

Let's look at the problem graphically (see {numref}`fig:KKT_g2const_graphical`). We assume that the feasible range of values for $g_2$ reduces so the original optimal solution (green dot) is no longer in the feasible set. By looking at the graph and reasoning, we can suppose that the upper capacity limit of $g_2$ will be binding. So, we will test the solution in which $g_1$ is producing somewhere in its operating range $0 < g_1 < \overline{G_1}$ (the inequality constraints are non-binding) and $g_2$ is operating at maximum capacity $g_2 = \overline{G_2}$. The solution still needs to satisfy the equality constraint (be on the blue line).

```{figure} ../images/KKT_g2const_graphical.png
:name: fig:KKT_g2const_graphical
:figwidth: 400 px

Graphical representation of the economic dispatch problem with reduced feasible range for $g_2$
```

Given this test solution, we know that $\mu_1$, $\mu_2$, $\mu_3$ $= 0$ and $\mu_4 \neq 0$. This simplifies the set of KKT conditions to:
\begin{align}
    & \frac{\partial \mathcal{L}}{\partial g_1} = 2 \cdot b_1 \cdot g_1 + \lambda  = 0  \\
    & \frac{\partial \mathcal{L}}{\partial g_2} = 2 \cdot b_2 \cdot g_2 + \lambda + \mu_4 = 0  \\
    & \frac{\partial \mathcal{L}}{\partial \lambda} = g_1 + g_2 - L = 0  \\
    &  - g_1 < 0  \\
    &  g_1 - \overline{G_1} < 0   \\
    & g_2 = \overline{G_2} \\
    & \mu_1, \mu_2, \mu_3 = 0  \\
    & \mu_4 \geq 0
\end{align}

The only unknown variables are $g_1$, $\lambda$, and $\mu_4$, which we can solve for. If we can find a solution, it is optimal. We can also ask ourselves "Does the solution make sense? Is there an alternative set of binding inequality constraints that would yield a better solution?" to check that indeed we have found the optimal solution. The new solution---orange dot in {numref}`fig:KKT_g2const_graphical`---satisfies the constraints but comes at a higher total operating cost than before.

### Duality and KKT conditions

Lastly, we will discuss the relationship between duality and KKT conditions. We know that for every primal problem, there exists a dual problem, but how do we formulate the dual problem?

Recall the general formulation of a primal problem:
\begin{align}
    \text{min.} \; & f(x)  \\
    \text{s.t.} \; & h_i(x) = 0 \quad (\lambda_i) \quad \forall i \in \{1,2,...,m\}  \\
    & g_j(x) \leq 0 \quad (\mu_j) \quad \forall j \in \{1,2,...,n\}
\end{align}

The Lagrangian is:
\begin{equation}
    \mathcal{L}(x,\lambda,\mu) = f(x) + \sum_{i=1}^m \lambda_i \cdot h_i(x) + \sum_{j=1}^{n} \mu_j \cdot g_j(x)
\end{equation}

The Lagrangian dual function, or dual function, is the minimum of the Lagrangian:
\begin{equation}
    \mathcal{D}(\lambda,\mu)  = \text{inf}_{x} \{\mathcal{L}(x,\lambda,\mu)\} = \text{inf}_{x} \{ f(x) + \sum_{i=1}^m \lambda_i \cdot h_i(x) + \sum_{j=1}^{n} \mu_j \cdot g_j(x) \}
\end{equation}
with "inf" a generalisation of the "min" operator.

The dual function defines a lower bound on the optimal value of the primal problem $p^*$: $\mathcal{D}(\lambda,\mu) \leq p^*$ for any $\mu \geq 0$ and any $\lambda$. We want to find the best possible lower bound of the primal problem, which means maximising the lower bound:
```{math}
:label: eqn:dual
\begin{align}
    \text{max.} \; & \mathcal{D}(\lambda,\mu)  \\
    \text{s.t.} \; & \mu_j \geq 0 \quad \forall j \in \{1,2,...,n\}
\end{align}
```
This is the dual problem. We denote the optimal value of this problem as $d^*$.

As mentioned at the beginning, strong duality is when the optimal value of the primal equals the optimal value of the dual. In our new terminology, this is written as $d^* = p^*$. Strong duality can be used to show that a solution that satisfies the KKT conditions must be an optimal solution to the primal and dual problems. Meaning, the KKT conditions are necessary and sufficient conditions for optimality. Weak duality is when $d^* \leq p^*$. This holds even for non-convex problems. $p^* - d^*$ is referred to as the duality gap.

In practice, we do not start from the general expression in Equation {eq}`eqn:dual` to derive the dual problem. Instead, we write the primal problem in standard form, for which we know the relation between the dual and the primal problem, or we use tables.

## Further reading

For more background on duality and to dive deeper into the mathematics, we suggest reading Chapter 5 of {cite:t}`boyd.vandenberghe_convex_2004` which is [freely available online](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf).

## References

```{bibliography}
:filter: docname in docnames
```
