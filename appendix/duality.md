# More on duality

(content:appendix:duality-conversion-summary)=

## Duality: conversion summary

This is a summary of the recommended approach to convert a primal problem into its dual problem.

First, you convert the primal problem to a standard form:

* Minimisation.
* All constraints of the form $ax \leq b$.
* All variables with bound $\geq 0 $.

Second, you convert the standard-form primal problem into the dual problem, as illustrated in {numref}`fig:generic_primal_dual_conversion` and written out in the bullet point list below:

```{figure} ../images/primal_dual.jpg
:name: fig:generic_primal_dual_conversion

Illustration of the conversion from standard form primal problem to dual problem.
```

* The primal objective function coefficients, $c_n$, are the dual constraint parameters.
* The primal constraint parameters, $b_m$, are the dual objective function coefficients.
* The primal constraints in $\leq$ form lead to dual variables $y_m \leq 0$.
* The primal constraints in $=$ form lead to dual variables $y_m$ which are unconstrained / free.
* The primal variables $x_n \geq 0$ lead to dual constraints of $\leq$ form.
* The constraint coefficient $a_{mn}$ corresponds to the m-th constraint and n-th variable in the primal problem. It corresponds to the n-th constraint and m-th variable in the dual problem.

(content:appendix:duality-example)=

## Lunch ingredients: an illustrative example of the perspective switch in duality

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
