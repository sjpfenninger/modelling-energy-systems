# Economic dispatch as a linear optimisation problem

(content:lp:economic-dispatch)=
## Economic dispatch

We start by looking at a simple problem. We are a power company that owns two power plants. We know what demand for power is going to be in the next hour, and we need to decide how to operate our power plants to meet that demand while minimising our cost. To do so we decide which of our plants should be operating, and if they are operating, how much electricity they should be generating. The problem is illustrated in {numref}`fig-economic-dispatch`.

```{figure} ../images/economic-dispatch.jpg
:name: fig-economic-dispatch

An illustrative economic dispatch problem with two power plants.
```

We call this the economic dispatch (ED) problem. More generally, the problem is to distribute the total power demand among available power generators (also called "units" or "generating units") in a way that minimizes the total power generation cost. Each generating unit has different power generation costs based on how it generates power. What we usually consider in this kind of problem is the marginal cost, so, the cost of providing one additional unit of electricity. This implies that we do not consider the cost of building the power plant, only of operating it now that it exists.

For a gas-fired power plant, for example, the main contributor to the power cost is the cost of gas. These costs can vary significantly across different units, for instance, the power generation costs for a nuclear unit and a gas-fired unit will differ widely. In addition, renewable generators like a wind farm have no or very small marginal generation costs, since their main resource - wind in the case of a wind farm - is free. We will return to that issue later.

```{admonition} A note on terminology
:class: tip
In the context of "economic dispatch", you will frequently hear these terms:
* Unit commitment: This is a more general problem that we will return to later, which includes additional considerations, for example the fact that power plants can be turned on and off (but they might require time, or additional costs, to do so). Economic dispatch can be considered a sub-problem of unit commitment.
* Merit order: You will also hear "merit order" in the context of dispatch. This simply refers to the approach of ranking different generating units or sources of electricity based on their "merit". If we consider only costs, then the merit order is the solution to the economic dispatch problem.
```

(content:lp:optimisation)=
## Mathematical optimisation

To formulate a mathematical optimisation problem, we will generally need four components.

First, we have some {{ circle_1 }} **parameters**, known quantities that remain fixed. Second, we have the {{ circle_2 }} **decision variables**, the quantities we do not know and would like to find optimal values for.

In order to find optimal values for the variables, we need to know what we are looking for. That is where the {{ circle_3 }} **objective function** comes in: this is a function made up of our variables that we seek to either minimise or maximise. For example, if we want to minimise cost across all our power plants, our objective function would represent that cost by summing up each individual plant's cost.

Finally, we likely have some {{ circle_4 }} **constraints**. These are expressions that limit the values that our variables can take. For example, if we have a variable describing the power generation of a power plant, we would want to **constrain** that variable so that its maximum value is the rated power output of the power plant.

In summary, these are the four components of an optimisation problem - we will use this structure whenever we think through a problem formulation:

* {{ circle_1_params }}
* {{ circle_2_variables }}
* {{ circle_3_objective }}
* {{ circle_4_constraints }}

## Economic dispatch as an optimisation problem

Now that we've introduced economic dispatch ({numref}`content:lp:economic-dispatch`) and the basic concept of optimisation ({numref}`content:lp:optimisation`), we can formulate the economic dispatch problem from {numref}`fig-economic-dispatch` as a linear optimisation problem. "Linear optimisation" means that both our objective function and all of the constraints are linear, continuous functions.

We assume that we're looking at a one-hour time frame and ignore everything that happens before and after that hour.

```{admonition} "Programming"
:class: tip
Linear optimisation is often called "linear programming" and abbreviated to LP. "Programming" in this context does not mean "computer programming" in the modern sense but comes from the history of how these methods were developed in the United States during World War II, where "programming" referred to logistics scheduling in the military. We will use "programming" and "optimisation" interchangeably.
```

### {{ circle_1_params }}

We know the demand for the hour we are looking at, $P_{demand}$ = 500 MW.

We also know some things about our power plants (units). We know what their minimum and maximum power generation are. We will call that $P_{min,i}$ and $P_{max,i}$, for each unit $i$.

We also know how much it costs us to run our units for an hour. For now, we will assume that the cost is simply a function of the power output over the hour that we are considering. Thus, our per-unit cost is $C_i$, representing the unit $i$'s generating cost in €/MW.

The specifics of our two units are:

* Unit 1 is a coal-fired power plant: Cost is 3 EUR/MW, minimum output is 50 MW, maximum output 300 MW
* Unit 2 is a gas-fired power plant: Cost is 4 EUR/MW, minimum output 100 MW, and maximum output 400 MW

### {{ circle_2_variables }}

We want to decide how to operate our units, so our variables - the unknown quantities that we want to optimise - are the power generated in each unit $i$:

$P_i$

### {{ circle_3_objective }}

Our objective is to minimise our cost of generating power. Given the cost per unit, $C_i$, and the power generated in each unit, $P_i$, we can formulate the total cost as follows:

\begin{equation}
\label{eq:ed_cost}
C = \sum_{i=1}^{n} C_i * P_{i}
\end{equation}

### {{ circle_4_constraints }}

We have two practical constraints to consider.

First, our units must operate within their physical limits - their generated power must be between their minimum and maximum possible output:

\begin{equation}
\label{eq:ed_min}
P_{min,i} \leq P_{i} \leq P_{max,i}
\end{equation}

Second, the amount of electricity generated must exactly match the demand for electricity:

\begin{equation}
\label{eq:ed_balance}
\sum_{i=1}^{n} P_{i} = P_{demand}
\end{equation}

Note this implies that we ignore many practical matters, for example:

* We have perfect knowledge about everything, e.g. we know demand exactly.
* We ignore the fact that demand and supply are separated in space; i.e. there are no grid losses of electricity.

### Full problem

In our example, with two power plants, we end up with the following linear optimisation or linear programming (LP) problem:

* Variables: $P_1$ and $P_2$
* Objective (to be minimised): $C = C_1 * P_1 + C_2 * P_2 = 3P_1 + 4P_2$
* Demand balance constraint: $P_1 + P_2 = 500$
* Operational constraint for unit 1: $50 \leq P_1 \leq 300$
* Operational constraint for unit 2: $100 \leq P_2 \leq 400$

## Graphical solution

Since this is a two-dimensional problem, with our two decision variables $P_1$ and $P_2$, we can visualise the solution graphically. In principle, we are looking for a value for $P_1$ and $P_2$, so a point in the two-dimensional decision space seen in {numref}`fig-dispatchlp-decisionspace`.

```{figure} ../images-built/fig_dispatchlp_decisionspace.jpg
:name: fig-dispatchlp-decisionspace
:figwidth: 500px

The two-dimensional decision space.
```

First, we can draw in the operational constraints for both units. These constraints are **inequality constraints**: they state that a variable must be lesser or equal to, greater than or equal to, a specific value. This turns the decision space into a well-constrained area, as seen in {numref}`fig-dispatchlp-decisionspace-operationalconstraints`.

```{figure} ../images-built/fig_dispatchlp_decisionspace_operationalconstraints.jpg
:name: fig-dispatchlp-decisionspace-operationalconstraints
:figwidth: 500px

The two-dimensional decision space with the operational constraints for both units shown in red ($P_1$) and green ($P_2$).
```

Next, we need to consider the demand constraint. The demand constraint is an **equality constraint**. We want a linear combination of the supply variables to add up to exactly the known power demand for the hour, 500 MW. In combining the operational constraints from above with the demand constraint, we end up with the **feasible region** which in this case is just a line segment ({numref}`fig-dispatchlp-decisionspace-allconstraints`).

```{figure} ../images-built/fig_dispatchlp_decisionspace_allconstraints.jpg
:name: fig-dispatchlp-decisionspace-allconstraints
:figwidth: 500px

The two-dimensional decision space after the addition of the demand constraint. The feasible region is now a line segment (grey).
```

There are still an infinite number of feasible solutions to this problem ({numref}`fig-dispatchlp-decisionspace-allconstraints` highlights one possible feasible solution). Which solution is the optimal one?

## Contour lines

## Active constraints

## More reading
