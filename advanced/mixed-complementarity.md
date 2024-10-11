(content:mixed-complementarity)=

# Mixed complementarity problems

Before delving deeper into how the complex relations between the actors affect the outcome of the electricity/commodities markets, it is first necessary to set a solid foundation. First, we will discuss some basic concepts in game theory, such as Pareto efficiency and Nash and Nash-Cournot games. Secondly, we will briefly describe the fundamentals of Mixed Complementarity before we discover their relevance to study energy markets.

## Game theory basics

So far, we have considered the dispatch of power from the system perspective, i.e, how would a central planner dispatch the available power plants in the most cost-efficient way. This assumes that this central planner has full control of and information on these power plants.  Modern, liberalized electricity systems do not work in such a centralized manner, but are rather market-based, meaning that a large set of actors (e.g., producers, consumers) are involved. These actors act in a selfish manner to maximize their profits or utility.

To model the behavior of different actors in the market, it is necessary to employ a mix of optimization and game theory. Let's begin with one of the classic game theory examples, the Prisoner's Dilemma. Assume that two suspected bank robbers, Thelma & Louise, are captured by the police. They are separated and have the choice of whether or not to confess and implicate the other:

* if both confess, they both serve 10 years in jail;
* if one confesses and implicates the other and the other doesn’t, she goes free, the other serves 20 years;
* if none of them confess, they both serve 1 year.

The payoff matrix of the prisoner's dilemma can be seen in {numref}`fig-payoff-matrix`. Based on the payoff matrix, the optimal scenario is for neither Thelma nor Louise to confess, as this leads to less years in prison in total. This situation of the payoff matrix (1,1) is the Pareto-optimal outcome of the prisoner's dilemma.

On the contrary, the Nash equilibrium of the dilemma is when both Thelma and Louise confess, and each serves 10 years in prison. The presented example is a case of a "non-cooperative game" where Thelma and Louise selfishly try to maximize their own utility $Π_α$ by selecting a strategy $χ_α$. In such a non-cooperative game, each agent selects its strategy simultaneously & independently, assuming that the strategy of the other players $χ_{-α}$ is given. In a state of Nash equilibrium (denoted with $*$) none of the players has an incentive to deviate from the equilibrium strategy $χ_α^*$ as no alternative feasible strategy $χ_α \in Φ_α$ exists that leads to more utility. Formally, the Nash equilibrium condition reads:

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

Such Nash games can be  used to describe perfectly competitive electricity markets, where the producers and consumers are price-takers. This means that the market actors do anticipate how their own actions will influence the market price. In contrast, in Nash-Cournot games, each firm anticipates its impact on the market through the knowledge of the inversion function {cite}`ruiz2014tutorial`. More specifically, in a Nash-Cournot game, the firms compete on production quantity and anticipate the impact of their own actions on the commodity price.

```{admonition} Pareto Optimal Outcome
The Pareto optimal strategy, named after the economist Vilfredo Pareto, corresponds to a strategy, where no alternative one exists, that benefits all actors. Therefore, it is the optimal solution for all actors jointly.
```

## Basics of mixed complementarity problems

Let's assume a general optimization problem, as seen below :

\begin{align}
    &\min_{x} \ f(x) \\
    &\text{subject to:} \nonumber \\
    &h_i(x) = 0 \quad (λ_{i}) \quad \forall  i \in = 1, \dots, m \nonumber \\
    &g_j(x) \leq 0 \quad (μ_{i}) \quad \forall  j \in = 1, \dots, p \nonumber \\
\end{align}

The Lagrangian reads :

:label: eqn:Lagrangian
\begin{equation}
    \mathcal{L} = f(x) + \sum_{i=1}^m \lambda_i \cdot h_i(x) + \sum_{j=1}^{n} \mu_j \cdot g_j(x)
\end{equation}

The KKT conditions of the problem are the following :

:label: eqn:KKT
\begin{align}
    & \frac{\partial \mathcal{L}}{\partial x} = 0   \quad & (\text{Optimality conditions})\\
    & \frac{\partial \mathcal{L}}{\partial \lambda_i} = h_i(x) = 0 \quad \forall i \in  \{1,2,...,m\}  \quad &  (\text{Primal feasibility}) \\
    & g_j(x) \leq 0 \quad \forall j \in  \{1,2,...,n\}  \quad & (\text{Primal feasibility}) \\
    & \mu_j \cdot g_j(x) =  0 \quad \forall j \in  \{1,2,...,n\}  \quad & (\text{Complementary slackness conditions}) \\
    & \mu_j \geq 0 \quad \forall j \in  \{1,2,...,n\} & (\text{Dual feasibility})
\end{align}

The set of KKTs described in equation {eq}`eqn:KKT` are an instance of a Mixed Complementarity Problem. Because for linear and convex quadratic (non-linear) optimization problems, the KKT pose both a sufficient and necessary condition for optimality, the solution of the MCP satisfies the KKTs of the original problem and therefore is a solution. In the following paragraphs, we will examine how MCPs can help us solve market clearing problems from the perspective of market actors.

```{note}
According to {cite}`Gabriel_Conejo_Fuller_Hobbs_Ruiz_2013` a Non Linear Complementarity problem is defined as : If we have a function $F$ the pure Non Linear complementarity problem $NCP(F)$ is to find a $x \in R^n$ such that for all $i$:

$$
1. \quad F_i(x) \geq 0 \\
2. \quad x_i \geq 0 \\
3. \quad x_i \cdot F_i(x) = 0
$$

The Mixed Complementarity problem is a **generalization** of the NCP, as it allows for variables with both upper and lower limits
```

## Application of mixed complementarity problems in electricity markets

Let's start with a simple market clearing problem. The market-clearing problem is relevant to pool-like market. In such a pool,  the market operator has to clear the auction and decide on a market price along with quantities from each producer. Once again, the market clearing problem is from the side of the pool/system operator, which aims at maximizing social welfare. The optimization problem is considered under given price-quantity pairs of supply and demand agents, $(P_i^s, Q_i^s), (P_j^d, Q_j^d)$. The optimization problem is formulated as :

```{math}
:label: market_clearing
\begin{align}
& \max \sum_{j \in J} P^d_j \cdot q^d_j - \sum_{i \in I} P^s_i \cdot q^s_i \tag{1} \\
& \text{subject to:}\\
& \sum_{j \in J} q^d_j - \sum_{i \in I} q^s_i = 0 \quad (\lambda)  \tag{2}\\
& 0 \leq q^s_i \leq Q^s_i \quad (\underline{μ_i}, \overline{μ_i}) \quad \forall i \in I \tag{3}\\
& 0 \leq q^d_j \leq Q^d_j \quad (\underline{ν_j}, \overline{ν_j}) \quad \forall j \in J \tag{4}\\
\end{align}
```

The KKT conditions of the market-clearing problem {eq}`market_clearing` are :

```{math}
:label: KKT_market_clearing
\begin{align}
& \sum_{j \in J} q^d_j - \sum_{i \in I} q^s_i = 0 \quad (\lambda)  \tag{2} \\
& 0 \leq q^s_i \leq Q^s_i \quad (\underline{\mu_i}, \overline{\mu_i}) \quad \forall i \in I \tag{3} \\
& 0 \leq q^d_j \leq Q^d_j \quad (\underline{\nu_j}, \overline{\nu_j}) \quad \forall j \in J \tag{4} \\
& -P_j^d + \lambda - \underline{\nu_j} + \overline{\nu_j} = 0 \quad \forall j \in J \tag{5a} \\
& P_i^s - \lambda - \underline{\mu_i} + \overline{\mu_i} = 0 \quad \forall i \in I \tag{5b} \\
& -\underline{\nu_j} q_j^d = 0 \quad \forall j \in J \tag{6a} \\
& \overline{\nu_j} \cdot (q_j^d - \overline{Q_j^d}) = 0 \quad \forall j \in J \tag{6b} \\
& -\underline{\mu_i} q_i^s = 0 \quad \forall i \in I \tag{6c} \\
& \overline{\mu_i} \cdot (q_i^s - \overline{Q_i^s}) = 0 \quad \forall i \in I \tag{6d} \\
& \underline{\mu_i}, \overline{\mu_i} \geq 0 \quad \forall i \in I \tag{7a} \\
& \underline{\nu_j}, \overline{\nu_j} \geq 0 \quad \forall j \in J \tag{7b} \\
\end{align}
```

Now let's look at the issue from the side of the supply and demand agents participating in the electricity market, offering price-quantity pairs. These, contrary to what presented up to now, have to be decided by each participant. So what is the optimization problem faced by the suppliers (generators) and the demand agents (customers, retailers) ?

First, the generators wants to maximize their profit given the market clearing price. As we are discussing the problem in the context of a perfectly competitive market, there is enough supply that the actions of individual do not influence the market price. Therefore, bridging with the previous chapter, supply and demand agents compete in a Nash game. In that case, the market clearing price $λ$ is a parameter and not a decision variable in the optimization problem. The supply-side optimization problem is {eq}`supply_side` :

```{math}
:label: supply_side
\begin{align}
& \max (λ - VC_i) \cdot q^s_i \tag{8} \\
& \text{subject to:}\\
& 0 \leq q^s_i \leq \overline{Q^s_i} \quad (\underline{\mu_i}, \overline{\mu_i}) \tag{9} \\
\end{align}
```
where :
\begin{align*}
& VC_i = \text{Variable Cost of generator } i \\
& \overline{Q^s_i} = \text{the maximum output of generator } i \\
\end{align*}

The KKT conditions of the problem {eq}`supply_side` are the following :

```{math}
:label: KKT_supply
\begin{align}
& VC_i - λ - \underline{μ_i} + \overline{μ_i} =0 \tag{10a} \\
& 0 \leq q^s_i \leq \overline{Q^s_i} \quad (\underline{μ_i}, \overline{μ_i}) \tag{9} \\
& -\underline{μ_i} \cdot q^s_i = 0 \tag{10b} \\
& -\overline{μ_i} \cdot (q^s_i - \overline{Q^s_i}) = 0 \tag{10c} \\
& \underline{μ_i}, \overline{μ_i} \geq 0 \tag{10d} \\
\end{align}
```
Secondly, the demand agents aim to maximize their utility, again by using the assumption that their actions do not influence the market price. Therefore, the optimization problem faced by the demand-side agents is :

```{math}
:label: demand_side
\begin{align}
& \max (WTP_j - λ) \cdot q^d_j \tag{11} \\
& \text{subject to:}\\
& 0 \leq q^d_j \leq \overline{Q^d_j} \quad (\underline{ν_j}, \overline{ν_j}) \tag{12} \\
\end{align}
```
where :
\begin{align*}
& WTP_j = \text{Willingness to pay of demand agent } j \\
& \overline{Q^s_i} = \text{the maximum consumption capacity of generator } j \\
\end{align*}

The KKT conditions of the problem {eq}`demand_side` are :

```{math}
:label: KKT_demand
\begin{align}
& -WTP_j + λ - \underline{ν_j} + \overline{ν_j} = \tag{13a} \\
& 0 \leq q^d_j \leq \overline{Q^d_j} \quad (\underline{ν_j},  \overline{ν_j}) \tag{12}\\
& - \underline{ν_j} \cdot q^d_j = 0 \tag{} \tag{13b} \\
& \overline{ν_j} \cdot (q^d_j - \overline{Q^d_j}) = 0 \tag{13c} \\
& \underline{ν_j},  \overline{ν_j} \geq 0 \tag{13d} \\
\end{align}
```
The two different optimization problems are connected through a common linking constraint, requiring supply and demand quantities to match. That is constraint (2) of the initial market clearing problem. To arrive at the equilibrium of the Nash game between demand and supply agents we need to **simultaneously** solve the supply-side problem {eq}`supply_side`, the demand-side problem {eq}`demand_side` and the linking constraint (2) of problem {eq}`market_clearing`.

There are several ways to solve the new optimization problem. We can follow one of the three methods :
* Concatenate the optimality conditions from the KKTs of the individual problems ({eq}`supply_side`, {eq}`demand_side`) along with the linking constraint to form a Mixed Complimentarity Problem. We will later show, why by concentating the constraints we arrive at the MCP. Then the MCP can be solved either with dedicated solvers such as PATH or as a feasibility problem( NLP, MIPL, optimization problems).
* Apply price-search algorithms and iterative methods, to find a solution that satisfies all costraints.
* Derive an equivalent optimization problem (EOP) and solve it using optimization solvers, such as yalmip used during the course.

But now let's prove why concatenating the KKT conditions of problems ({eq}`supply_side`, {eq}`demand_side`) along with the linking constrait formulates an MCP.

```{math}
:label: MCP_KKT
\begin{align}
& VC_i - λ - \underline{μ_i} + \overline{μ_i} =0 \tag{10a} \\
& 0 \leq q^s_i \leq \overline{Q^s_i} \quad (\underline{μ_i}, \overline{μ_i}) \tag{9} \\
& -\underline{μ_i} \cdot q^s_i = 0 \tag{10b} \\
& -\overline{μ_i} \cdot (q^s_i - \overline{Q^s_i}) = 0 \tag{10c} \\
& \underline{μ_i}, \overline{μ_i} \geq 0 \tag{10d} \\
& -WTP_j + λ - \underline{ν_j} + \overline{ν_j} = \tag{13a} \\
& 0 \leq q^d_j \leq \overline{Q^d_j} \quad (\underline{ν_j},  \overline{ν_j}) \tag{12}\\
& - \underline{ν_j} \cdot q^d_j = 0 \tag{} \tag{13b} \\
& \overline{ν_j} \cdot (q^d_j - \overline{Q^d_j}) = 0 \tag{13c} \\
& \underline{ν_j},  \overline{ν_j} \geq 0 \tag{13d} \\
& \sum_{j \in J} q^d_j - \sum_{i \in I} q^s_i = 0 \quad (\lambda)  \tag{2}\\
\end{align}
```
Comparing the KKTs of the **concatenated problem {eq}`MCP_KKT`** with those of the **market-clearing problem {eq}`market_clearing`**, we can deduce that there is a difference in the following constraints :

\begin{align}
& VC_i - λ - \underline{μ_i} + \overline{μ_i} =0 \tag{10a} \\
& P^s_i - \lambda - \underline{\mu_i} + \overline{\mu_i} = 0 \quad \forall i \in I \tag{5b} \\
& -WTP_j + λ - \underline{ν_j} + \overline{ν_j} = \tag{13a} \\
& -P^d_j + \lambda - \underline{\nu_j} + \overline{\nu_j} = 0 \quad \forall j \in J \tag{5a}
\end{align}

But since we know that in electricity markets suppliers bid their capacity at variable cost and demand agents at their willigness to pay, we can conclude $VC_i = P^s_i$ and $WTP_j = P^d_j$. Therefore, constraint (10a) is equal to constraint (5b) and (13a) to (5a). Through this observation, we can conclude that the KKTs of the MCP (supply-side + demand-size + linking constraint) are the same as the market-clearing problem. The main implication of this, is that a solution that satisfies the KKTs of the market-clearing problem will also be a solution of the MCP. Bring in mind that these are both convex optimization problems. Therefore, we have proved that the market-clearing problem is the **Equivalent Optimization Problem (EOP)** of the MCP.

```{warning} Every optimization has an equivalent MCP, but not every MCP has an equivalent optimization problem.
```
### An alternative formulation of the market clearing problem
Another formulation of the Nash game between demand and supply agents can be presented through the use of an inverse demand function. In that case, instead of having demand bid-pairs, a linear relationship between the price of electricity and the demanded quantity is in place. The linear equation takes the form of :

```{math}
:label: linear demand
\begin{align}
$ λ = \overline{λ} - β \cdot \sum_{j \in J} q^d_j
\end{align}
```

But since from the linking constraint we know $\sum_{j \in J} q^d_j = \sum_{i \in I} q^s_i$ the inverse demand function can be rewritten as $λ = \overline{λ} - β \cdot \sum_{i \in I} q^s_i$. In this way we have eliminated the second vector of decision variables $q^d_j$.The $\overline{λ}$ is the interceptor of the demand curve and signifies the maximum willingness to pay and you can see the graphic interpretation of the inverse curve in {numref}`fig-inverse-demand`. Taking all the above into account , the game can be finally reformulated as :


```{figure} ../images/inverse_demand_function.jpg
:name: fig-inverse-demand
Inverse demand function and supply curve, based on supply-side bid pairs.
```

```{math}
:label : game inverse demand
\begin{align}
& \{\max (λ-VC_i) \cdot q^s_i \tag{8} \\
& \text{s.t} 0 \leq q^s_i \leq \overline{Q^s_i} \quad (\underline{μ_i}, \overline{μ_i}) \} \tag{9}\\
& λ = \overline{λ} - β \cdot \sum_{i \in I} q^s_i \tag{14} \\
\end{align}
```
Calculating the KKT conditions of the game yields the MCP. Note that the inverse demand function participates as-is in the MCP, but is not part of the optimization problem (it is outside of the curly brackets). That is the case since we are participating in a Nash game, and therefore the suppliers do not consider their actions impact on price !

```{math}
:label : MCP inverse demand
\begin{align}
& \{ VC_i - λ - \underline{μ_i} + \overline{μ_i} = 0 \tag{10a} \\
& 0 \leq q^s_i \leq \overline{Q^s_i} \quad (\underline{μ_i}, \overline{μ_i}) \tag{9} \\
& -\underline{μ_i} \cdot q^s_i = 0 \tag{10b} \\
& -\overline{μ_i} \cdot (q^s_i - \overline{Q^s_i}) = 0 \tag{10c} \\
& \underline{μ_i}, \overline{μ_i} \geq 0 \tag{10d} \} \\
& λ = \overline{λ} - β \cdot \sum_{i \in I} \tag{14} \\
\end{align}
```
With the MCP defined, we can now derive the Equivalent Optimization problem  to solve the initital game {eq}`game inverse demand`. Remember here, that the KKT conditions of the EOP and the MCP have to be the same in order for the EOP to provide a solution to the initial problem. To derive the EOP we make use of the graphical interpretation of the problem show in {numref}`fig-inverse-demand`. Remember here, that the we proved that the Nash game is equivalent to the market-clearing problem faced by the market operator. Leveraging this, we can **derive the EOP to maximize the Social Welfare**. Based on {numref}`fig-inverse-demand-area` and the fact that the social welfare is the area under the supply and the demand curves we can say that :

$$
SW = (ABDE) - (ABC) - \text{Area of sketched polygon} = \overline{\lambda} \cdot \sum_{i} q^s_i - \frac{1}{2}\beta \sum_{i} \left(q^s_i\right)^2 - \sum_{i} VC_i \cdot q^s_i
$$

```{figure} ../images/area_inv_demand.jpg
:name: fig-inverse-demand-area
Areas to calculate social welfare from inverse demand and supply curves.
```

Therefore the EOP is formulated as :

```{math}
:label: EOP_Nash
\begin{align}
& \max \overline{\lambda} \cdot \sum_{i} q^s_i - \frac{1}{2}\beta \sum_{i} \left(q^s_i\right)^2 - \sum_{i} VC_i \cdot q^s_i \tag{15} \\
& \text{s.t}\\
& 0 \leq q^s_i \leq Q^s_i \quad (\underline{μ_i}, \overline{μ_i}) \quad \forall i \in I \tag{3} \\
\end{align}
```
Finally, the equivalence of the MCP with the EOP can be demonstrated through the derivation of the KKTs for the EOP {eq}`EOP_Nash`.

### Nash-Cournot games

Up to now, we have assumed a perfectly competitive market, meaning firms have zero market power and act as pure price-takers. This is only a theoretical artefact, as firms always have some market power. To model such interactions, a Nash-Cournot game can be implemented, where each agent assumes that the impact of the other players decision on the price is given. Therefore, he acts on the the residual demand. Again, we will make use of an inverse demand curve to simulate the demand-side bids. Now that the impact of the other players decision is part of the optimization problem of a single agent, the inverse curve **is part of the optimization problem**. The Nash-Cournot game is present below :

```{math}
:label: Nash_Cournot
\begin{align}
& \{ \max (λ-VC_i) \cdot q^s_i \tag{8} \\
& \text{s.t} 0 \leq q^s_i \leq \overline{Q^s_i} \quad (\underline{μ_i}, \overline{μ_i}) \ \tag{9}\\
&  λ = \overline{λ} - β \cdot \sum_{i \in I} \tag{14} \} \\
\end{align}
```

```{warning} In the Nash-Cournot game the inverse demand function is now an integral part of the optimization problem.
```

Now to better understand how to solve a Nash-Cournot game, we will walk through a numerical example. Let us assume two market participants that compete a la Cournot. The demand is elastic and described by and inverse demand function with $\overline{λ}= 100 \text{€} / MWh,  β=5\text{€} / MWh^2 $. The variable cost of supplier 1 is $10 \text{€}/ MWh$ and of supplier 2 $30 \text{€} / MWh$. There are no maximum generation constraints for any of the suppliers. The Nash-Cournot game now reads :

```{math}
:label: nash_cournot_example
\begin{align}
& \{ \max  (100 - 5 \cdot (q^s_1 + q^s_2) - 10) \cdot q^s_1  \\
& \text{subject to} \quad q^s_1 \geq 0 \quad (\underline{μ_1}) \} \\
& \max \{ (110 - 5 \cdot (q^s_1 + q^s_2) - 30) \cdot q^s_2 \} \\
& \{ \text{subject to} \quad q^s_2 \geq 0 \quad (\underline{μ_2}) \}
\end{align}
```

When there is competition between two agents, an easy way to find the equilibrium point is through a graphical solution, as illustrated in {eq}`Nash_Cournot`. To obtain the graphical solution, we solve the problem for supplier 1, by derivating the objective function w.r.t $q^s_1$ and then setting the derivate $\frac{\partial obj}{\partial q^s_1} = 0 $. In that way we obtain the best response function of supplier 1, which describes how supplier 1 shall act based on the actions of supplier 2. Then we perform the same process for supplier 2 by setting the derivative $\frac{\partial obj}{\partial q^s_2} = 0 $ and obtaining the best response function of supplier 2. Finally, by plotting both we can obtain from the intersection point the equilibrium quantities.

```{figure} ../images/nash_cournot.jpg
:name:fig-nash_cournot
Graphical solution of numerical example {eq}`nash_cournot_example`.
```
Overall, the Nash-Cournot games can be solved with similar methods to Nash games, by either:

* concatenating the optimality conditions and linking constraints to form an MCP, which can be solved graphically or through variable algorithms
* through iterative price search algorithms
* through the derivation of an Equivalent Optimization Problem, which can be solved through optimization algorithms

How can the EOP be obtained in the case of a la Cournot competition ? As always, let us start through deriving the KKT conditions for a generalized Nash-Cournot game {eq}`Nash_Cournot`:

```{math}
:label: KKT Nash Cournot
\begin{align}
& \{ -\overline{λ} + β \cdot \sum_{i \in I} q^s_i + β \cdot q^s_i + VC_i - \underline{μ_i} + \overline{μ_i} = 0 \tag{10a'} \\
& 0 \leq q^s_i \leq \overline{Q^s_i} \quad (\underline{μ_i}, \overline{μ_i}) \tag{9} \\
& -\underline{μ_i} \cdot q^s_i = 0 \tag{10b} \\
& -\overline{μ_i} \cdot (q^s_i - \overline{Q^s_i}) = 0 \tag{10c} \\
& \underline{μ_i}, \overline{μ_i} \geq 0 \tag{10d} \}
\end{align}
```

Now comparing the Lagrangian between the Nash game (10a) and Nash-Cournot game (10a') we see the following difference. The Nash-Cournot game has an extra term of $β \cdot q^s_i$. Again, leveraging our knowledge of the derivation of EOP for the Nash game, we can obtain the EOP for the Nash-Cournot game, by adjusting for that extra term in the KKT conditions. The EOP for a Nash-Cournot game with $i \in I$ participants can be seen in {eq}`EOP_Nash_Cournot`.

```{math}
\begin{align}
& -\overline{λ} + β \cdot \sum_{i \in I} q^s_i + VC_i - \underline{μ_i} + \overline{μ_i} = 0 \tag{10a} \\
&  -\overline{λ} + β \cdot \sum_{i \in I} q^s_i + β \cdot q^s_i + VC_i - \underline{μ_i} + \overline{μ_i} = 0 \tag{10a'} \\
\end{align}
```

```{math}
:label: EOP_Nash_Cournot
\begin{align}
& \max \overline{\lambda} \cdot \sum_{i} q^s_i - \frac{1}{2}\beta \sum_{i} \left(q^s_i\right)^2 - \frac{1}{2}\beta \sum_{i} (q^s_i)^2 - \sum_{i} VC_i \cdot q^s_i \tag{15'} \\
& \text{s.t}\\
& 0 \leq q^s_i \leq Q^s_i \quad (\underline{μ_i}, \overline{μ_i}) \quad \forall i \in I \tag{3} \\
\end{align}
```

Finally, some remarks on the Equivalent Optimization Problem of the Nash-Cournot game with the inverse demand function. Firstly, the objective function of the does not compute some direct measure of the Social Welfare expected by clearing the market, in comparison to the Nash game. The objective function of the EOP is a mere artefact constructed to solve the Nash-Cournot game. Secondly, despite the non-linear terms (squared) of the EOP, we are still in the convex optimization region and therefore can obtain a solution to the problem through the KKTs.

## Remarks

With the introduction of the Mixed Complementarity problems as a way to solve the Nash and Nash-Cournot games, we have introduced a paradigm shift in the way we study the market interactions. Up to now, we were considering the market only from the side of a pool operator that aims to clear the market. Now, with the new tools available we can model the market clearing along with the interactions between different market actors. Specifically, through the Nash equilibrium we can model the participation of agents in a perfectly competitive market, where they have zero market power. Moreover, to formulate a problem that better describes modern market, we introduced the Nash-Cournot equilibrium. In a Nash-Cournot game, the actors have market-power and try to optimally set their actions, considering the actions of the other actors as granted.

For both Nash and Nash-Cournot games, we demonstrated how through the formulation of a Mixed Complementarity Problem, which has equivalence of the KKT conditions, and then solve an Equivalent Optimization Problem, to find the equilibrium solution. For the Nash game, we showed that the Equivalent Optimization Problem is the maximization of the social welfare, as exactly in the market clearing problem. Finally, we also extracted the Equivalent Optimization Problem for the Nash-Cournot game, based on comparing the Nash-Cournot with the Nash game KKTs. All in all, through the use of equilibrium problems we can make relationships and interactions between market agents explicit, and have a more intuitive way of formalizing problem. Through the tools of MCP and EOP we can solve these equilibrium problems!


## References

```{bibliography}
:filter: docname in docnames
```
