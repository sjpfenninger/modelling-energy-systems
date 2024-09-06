# Duality: additional examples

## Maximisation problem

The primal problem is given by:

$$\text{Max. } J(\mathbf{x}) = x_1 + 4x_2$$

subject to:

\begin{align}
    x_1 + 2x_2 \leq 5 \\
    2x_1 + x_2 = 4 \\
    x_1 - x_2 \geq 1 \\
    x_1, x_2 \geq 0 \\
\end{align}

Note that the constraint $x_1 - x_2 \geq 1$ is the same as $-x_1 + x_2 \leq -1$.

Since there are three primal constraints (one equality and two inequalities), there are three dual variables for the problem. We will call them $\lambda_1$, $\mu_1$, and $\mu_2$ (again, we could use whatever variable names we want).

The dual problem is:

$$\text{Min. } F(\lambda, \mu) = 5\mu_1 + 4\lambda_1 - \mu_2$$

subject to:
\begin{align}
    \mu_1 + 2\lambda_1 - \mu_2 \geq 1 \\
    2\mu_1 + \lambda_1 + \mu_2 \geq 4 \\
    \mu_1, \mu_2 \geq 0 \\
\end{align}
The variable $\lambda_1$ is unrestricted in sign (free).

The solution to the primal problem is:

$$x_1^{*} = 1.666667$$

$$x_2^{*} = 0.666667$$

$$J(\mathbf{x}^{*}) = 4.33333$$

The active constraints are $2x_1 + x_2 = 4$ and $-x_1 + x_2 = -1$.

The shadow prices (Lagrange multipliers) for these active constraints are: $\lambda_1 = 1.666667$ and $\mu_2 = 2.333333$.

The solution to the dual problem is:

$$\mu_1 = 0$$

$$\mu_2 = 2.333333$$

$$\lambda_1 = 1.666667$$

$$F(\mathbf{\lambda^{*}}, \mathbf{\mu^{*}}) = 4.333333$$


Conclusions:

* The optimum value of the primal and the dual objective function is equal to 4.333333.
* The optimal values of the decision variables of the dual problem are equal to the Lagrange multipliers of the primal problem.
* Likewise, the shadow prices (Lagrange multipliers) of the dual problem are equal to the solution of the primal problem.

## Illustrative example of the perspective switch in duality (lunch ingredients)

An illustrative small example of the relationship between primal and
dual linear programs will show that these two problems arise from two
different perspectives on the same application. As an example, we
introduce a diet problem.

Johanna is deciding what to purchase for lunch. She has two choices:

1.  Soup, which costs 2.80€ per portion,

2.  Salad with fresh vegetables, which costs 3.20€ per portion.

In this lunchroom, it is possible to purchase a fraction of an item if
the client wishes. Also, the farmer can sell a fraction of a vegetable
to the owner of the lunchroom.

The soup ingredients are: onion, carrot, and tomato. The ingredients for
the salad are onion, carrot, and apple. The amount of the ingredients is
specified in recipes presented in the table below:

| Ingredient | Soup ($x_1$) | Salad ($x_2$) |
| --- | --- | --- |
| Onion | 1 | 0.5 |
| Carrot | 2.5 | 3 |
| Tomato | 2 | 0 |
| Apple | 0 | 1 |
| Cost | 2.80 | 3.20 |


Johanna's dietary requirements:
-   Onion: 0.5
-   Carrot: 4
-   Tomato: 1.5
-   Apple: 1.5

Johanna wants to minimise the lunch cost by finding the least expensive
combination of soup and fresh salad that meets her requirements, whereby
she needs at least 0.5 onion, 4 carrots, 1.5 tomatoes, and 1.5 apples for lunch.

This decision problem can be formulated as an LP problem as follows:

$$\text{Min. } 2.80x_1 + 3.20x_2$$

subject to:

\begin{align}
    x_1 + 0.5x_2 \geq 0.5 \\
    2.5x_1 + 3x_2 \geq 4 \\
    2x_1 \geq 1.5 \\
    x_2 \geq 1.5 \\
    x_1, x_2 \geq 0 \\
\end{align}

By applying the linear programming method to this problem, we can find
easily that the unique solution is $x_1 = 0.75$ and $x_2 = 1.5$, i.e. it
means $3/4$ portion soup and $1.5$ portion salad.

The value of the cost function for the optimal solution is
$2.80 \times 0.75 + 3.20 \times 1 = 6.90$.

There are 2 active constraints: $2x_1 \geq 1.5$ and $x_2 \geq 1.5$.

The shadow price is 1.40 for the active constraint $2x_1 \geq 1.5$, i.e.,
the cost will be 8.30 if the wish would be to eat at least 2.5 tomatoes.

The shadow price is 3.20 for the active constraint $x_2 \geq 1.5$, i.e.,
the cost will be 10.10 if the wish would be to eat at least 2.5 apples.

Let us have a look at this problem from the perspective of the farmer
who supplies the lunchroom with vegetables. The owner of the lunchroom
needs to buy at least 0.5 onion, 4 carrots, 1.5 tomatoes, and 1.5
apples.

The farmer wants to maximise his revenues. His decision problem is: How
can I set the prices per onion, carrot, tomato, and apple so that the
lunchroom owner will buy them from me, and my revenue is maximised?

The lunchroom owner will buy vegetables only if the total cost of soup
is below 2.80€ and for the salad, below 3.20€.

These restrictions impose the following constraints on the prices
$\mu_1, \mu_2, \mu_3, \mu_4$ for onions, carrots, tomatoes, and apples:

$$1 \mu_1 + 2.5 \mu_2 + 2 \mu_3 + 0 \mu_4 \leq 2.80$$

$$0.5 \mu_1 + 3 \mu_2 + 0 \mu_3 + 1 \mu_4 \leq 3.20$$

Clearly, all the prices for all these vegetables should be non-negative.

The revenue of the farmer is
$(0.5 \mu_1 + 4 \mu_2 + 1.5 \mu_3 + 1.5 \mu_4)$ and it should be
maximised. This gives us the following dual problem:

$$\text{Max. } F(\mu) = 0.5 \mu_1 + 4 \mu_2 + 1.5 \mu_3 + 1.5 \mu_4$$

subject to:
\begin{align}
    1 \mu_1 + 2.5 \mu_2 + 2 \mu_3 \leq 2.80 \\
    0.5 \mu_1 + 3 \mu_2 + \mu_4 \leq 3.20 \\
    \mu_1, \mu_2, \mu_3, \mu_4 \geq 0 \\
\end{align}

By applying the linear programming method to this dual problem, we can
find easily that the unique solution is
$\mu_1 = 0, \mu_2 = 0, \mu_3 = 1.40, \mu_4 = 3.20$.

It may seem strange that the farmer charges nothing for onion
($\mu_1 = 0$) and carrot ($\mu_2 = 0$). He charges 1.40€ per tomato and
3.20€ per apple. It is better for him to give onions and carrots for
free and charge as much as possible for tomatoes and apples.
