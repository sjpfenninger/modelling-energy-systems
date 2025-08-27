(content:appendix:game-theory)= 

# Basics of game theory

So far, we have considered the dispatch of power from the system perspective, i.e, how would a central planner dispatch the available power plants in the most cost-efficient way. This assumes that this central planner has full control of and information on these power plants.  Modern, liberalized electricity systems do not work in such a centralized manner, but are rather market-based, meaning that a large set of actors (e.g., producers, consumers) are involved. These actors act in a selfish manner to maximize their profits or utility.

## Prisoner's dillema

To model the behaviour of different actors in the market, we can use a mix of optimisation and game theory. Let's begin with one of the classic game theory examples, the Prisoner's Dilemma. Assume that two suspected bank robbers, Thelma and Louise, are captured by the police. They are separated and have the choice of whether or not to confess and implicate the other:

* if both confess, they both serve 10 years in jail;
* if one confesses and implicates the other and the other doesn’t, she goes free, the other serves 20 years;
* if none of them confess, they both serve 1 year.

The payoff matrix of the prisoner's dilemma can be seen in {numref}`fig-payoff-matrix`. Based on the payoff matrix, the optimal scenario is for neither Thelma nor Louise to confess, as this leads to less years in prison in total. This situation of the payoff matrix (1,1) is the Pareto-optimal outcome of the prisoner's dilemma.

On the contrary, the Nash equilibrium of the dilemma is when both Thelma and Louise confess, and each serves 10 years in prison. The presented example is a case of a "non-cooperative game" where Thelma and Louise selfishly try to maximize their own utility $Π_α$ by selecting a strategy $χ_α$. In such a non-cooperative game, each agent selects its strategy simultaneously and independently, assuming that the strategy of the other players $χ_{-α}$ is given. In a state of Nash equilibrium (denoted with $*$) none of the players has an incentive to deviate from the equilibrium strategy $χ_α^*$ as no alternative feasible strategy $χ_α \in Φ_α$ exists that leads to more utility. Formally, the Nash equilibrium condition reads:

$$ Π(χ_α*, χ_{-α}*) \geq (χ_α, χ_{-α}*) \quad \forall χ_α \in Φ_α , α \in A $$

:::{table} Payoff matrix of the prisoner's dilemma. Each table cell is composed of (number years Thelma serves in jail, number of years Louise serves in jail).
:width: 75%
:align: center
:name: fig-payoff-matrix
|                             | Thelma confesses | Thelma does not confess |
| --------------------------- | ---------------- | ----------------------- |
| **Louise confesses**        | (10, 10)         | (20, 0)                 |
| **Louise does not confess** | (0, 20)          | (1, 1)                  |
:::

Linking this back to our example, the case where both Thelma and Louise confess is the Nash equilibrium point since Thelma has no utility if she changes her strategy unilaterally. If she chooses to not confess, instead of 10 years in prison, she will receive 20 years while Thelma will be released. In other terms, her utility will be lower than the Nash-equilibrium point. In summary, in Nash games, each actor chooses the strategy with the highest payoff for themselves, assuming that the other actors have done the same at the same time  {cite}`Gabriel_Conejo_Fuller_Hobbs_Ruiz_2013`.

Such Nash games can be  used to describe perfectly competitive electricity markets, where the producers and consumers are price-takers. This means that the market actors do not anticipate how their own actions will influence the market price. In contrast, in Nash-Cournot games, each firm anticipates its impact on the market through the knowledge of the inversion function {cite}`ruiz2014tutorial`. More specifically, in a Nash-Cournot game, the firms compete on production quantity and anticipate the impact of their own actions on the commodity price.

```{admonition} Pareto optimal outcome
The Pareto optimal strategy, named after the economist Vilfredo Pareto, corresponds to the strategy where no alternative strategy exists that would benefit any of the actors. Every actor is as well off as they can be: it is the optimal solution for all actors jointly.
```
