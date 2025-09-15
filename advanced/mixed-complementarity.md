
(content:mixed-complementarity)=

# Interactions between actors: Mixed Complementarity Problems

In this section we consider an approach to depict how relations between actors affect the outcome of the electricity markets which, in {numref}`content:milp`, we had considered as optimisation problems from the perspective of a market operator.

We will study electricity market situations as Nash and Nash-Cournot games. These games can be represented as a set of optimisation problems, describing the decision problems of each of the involved actors, that are linked together via a common coupling constraint. Based on that observation, we can formulate a Mixed Complementarity Problem (MCP) which is associated to these linked optimisation problems. The MCP is given by the set of KKT conditions of the decision problems of the involved agents and the coupling constraint. Before we continue, let's briefly revisit the KKT conditions.

## Revisiting the market clearing problem

In {numref}`content:milp:day-ahead-auction` we discussed the clearing of a day-ahead power market, from the perspective of a market operator, when the price-quantity pairs by the supply and demand agents are given. Using those price-quantity bids, the market operator clears the market in a way that maximizes social welfare.

The optimisation problem is considered under given price-quantity pairs of supply and demand agents, $(P_i^s, Q_i^s), (P_j^d, Q_j^d)$. This is exactly the same problem that we formulated with "bids" and "offers" in {numref}`content:milp:day-ahead-auction`, just with different notation. This optimisation problem can be formulated as :

```{math}
:label: market_clearing
\begin{align}
& \max \sum_{j \in J} P^d_j \cdot q^d_j - \sum_{i \in I} P^s_i \cdot q^s_i \tag{1} \\
& \text{s.t:}\\
& \sum_{j \in J} q^d_j - \sum_{i \in I} q^s_i = 0 \quad (\lambda)  \tag{2}\\
& 0 \leq q^s_i \leq Q^s_i \quad (\underline{μ_i}, \overline{μ_i}) \quad \forall i \in I \tag{3}\\
& 0 \leq q^d_j \leq Q^d_j \quad (\underline{ν_j}, \overline{ν_j}) \quad \forall j \in J \tag{4}\\
\end{align}
```

This market clearing problem allows for determining the demand served $q^d_j$ and supply cleared $q^s_i$ in the market. The market clearing price $\lambda$ is the dual variable associated with the supply-demand balance.

We can write the Karush Kuhn Tacker conditions for the market clearing problem of Eq. {eq}`market_clearing`, as:

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

### The market clearing problem from the perspective of the participants

Above we presented the clearing of the market as faced by the market operator, who aims to maximise social welfare. In the case of the market operator, the supply and demand bids are given, since they are submitted by the corresponding supply and demand agents. From the supply and demand agents perspective, the objective is different.

The **supply agents** want to maximise their profit, given the price the market clears at. We assume the electricity suppliers are price-taking, meaning they don't influence the market price. Since the firms do not influence the price and compete on both prices and quantities, the electricity market can be described as a Nash game, in the context of [game theory](https://en.wikipedia.org/wiki/Game_theory). The optimisation problem of each agents $i$ in Eq. {eq}`supply_side` reads:

```{math}
:label: supply_side
\begin{align}
& \max (λ - VC_i) \cdot q^s_i \tag{8} \\
& \text{s.t:}\\
& 0 \leq q^s_i \leq \overline{Q^s_i} \quad (\underline{\mu_i}, \overline{\mu_i}) \tag{9} \\
\end{align}
```

where :
\begin{align*}
& VC_i = \text{Variable Cost of generator } i \\
& \overline{Q^s_i} = \text{the maximum output of generator } i \\
\end{align*}

The KKT conditions of the problem in Eq. {eq}`supply_side` are the following :

```{math}
:label: KKT_supply
\begin{align}
& VC_i - λ - \underline{μ_i} + \overline{μ_i} =0 \tag{10a} \\
& 0 \leq q^s_i \leq \overline{Q^s_i} \quad (\underline{μ_i}, \overline{μ_i}) \tag{9} \\
& -\underline{μ_i} \cdot q^s_i = 0 \tag{10b} \\
& \overline{μ_i} \cdot (q^s_i - \overline{Q^s_i}) = 0 \tag{10c} \\
& \underline{μ_i}, \overline{μ_i} \geq 0 \tag{10d} \\
\end{align}
```

Similarly, the **demand agents** aim to maximize their utility, again considering the clearing price as given. The demand agents are also price-takers. The optimisation problem of each agent $i$ in Eq. {eq}`demand_side` reads:

```{math}
:label: demand_side
\begin{align}
& \max (WTP_j - λ) \cdot q^d_j \tag{11} \\
& \text{s.t:}\\
& 0 \leq q^d_j \leq \overline{Q^d_j} \quad (\underline{ν_j}, \overline{ν_j}) \tag{12} \\
\end{align}
```

where :
\begin{align*}
& WTP_j = \text{Willingness to pay of demand agent } j \\
& \overline{Q^s_i} = \text{the maximum consumption capacity of generator } j \\
\end{align*}

The KKT conditions of the problem in Eq. {eq}`demand_side` are :

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

Equations {eq}`supply_side` and {eq}`demand_side` presented the optimisation independently faced by each supply and demand agent. But as a basic principle, the total supply has to be equal to the total demand (Eq. (2) of the market clearing problem in {numref}`content:milp:day-ahead-auction`). This is the **linking constraint** bringing together the different optimisation problems.

```{math}
\begin{align}
& \sum_{j \in J} q^d_j - \sum_{i \in I} q^s_i = 0 \quad (\lambda)  \tag{2}\\
\end{align}
```

## A solution to market clearing through the KKT conditions

To arrive at the equilibrium of supply and demand, we have to **simultaneously** solve the supply-side problems {eq}`supply_side`, the demand-side problems {eq}`demand_side` and the linking constraint (2). Thus, we have to find an optimal solution for all optimisation problems at once. Equivalently, we can find a solution to all Karush Kuhn Tucker conditions at once. We can concatenate the KKT conditions of the three problems as:

```{math}
:label: MCP_KKT
\begin{align}
& VC_i - λ - \underline{μ_i} + \overline{μ_i} =0 \tag{10a} \\
& 0 \leq q^s_i \leq \overline{Q^s_i} \quad (\underline{μ_i}, \overline{μ_i}) \tag{9} \\
& -\underline{μ_i} \cdot q^s_i = 0 \tag{10b} \\
& \overline{μ_i} \cdot (q^s_i - \overline{Q^s_i}) = 0 \tag{10c} \\
& \underline{μ_i}, \overline{μ_i} \geq 0 \tag{10d} \\
& -WTP_j + λ - \underline{ν_j} + \overline{ν_j} = \tag{13a} \\
& 0 \leq q^d_j \leq \overline{Q^d_j} \quad (\underline{ν_j},  \overline{ν_j}) \tag{12}\\
& - \underline{ν_j} \cdot q^d_j = 0 \tag{} \tag{13b} \\
& \overline{ν_j} \cdot (q^d_j - \overline{Q^d_j}) = 0 \tag{13c} \\
& \underline{ν_j},  \overline{ν_j} \geq 0 \tag{13d} \\
& \sum_{j \in J} q^d_j - \sum_{i \in I} q^s_i = 0 \quad (\lambda)  \tag{2}\\
\end{align}
```

Comparing the KKTs of the concatenated (supply + demand + linking constraint) problem in Eq. {eq}`MCP_KKT` with those of the market clearing problem (market operator perspective) in Eq. {eq}`market_clearing`, we can deduce that there is **only** a difference in the following constraints:

\begin{align}
& VC_i - λ - \underline{μ_i} + \overline{μ_i} =0 \tag{10a} \\
& P^s_i - \lambda - \underline{\mu_i} + \overline{\mu_i} = 0 \quad \forall i \in I \tag{5b} \\
& -WTP_j + λ - \underline{ν_j} + \overline{ν_j} = \tag{13a} \\
& -P^d_j + \lambda - \underline{\nu_j} + \overline{\nu_j} = 0 \quad \forall j \in J \tag{5a}
\end{align}

However, we know that in competitive electricity markets generators bid their capacity at variable cost and demand agents at their willingness to pay. Hence, we can say $VC_i = P^s_i$ and $WTP_j = P^d_j$. Therefore, constraint (10a) is equal to constraint (5b) and (13a) to (5a). Through this observation, we can conclude that the KKTs of the concatenated dispatch problems (supply + demand+ linking constraint) are the same as those of the market clearing problem.

Since the two problems described by {eq}`MCP_KKT` and {eq}`market_clearing` have the same set of KKT conditions, the market clearing problem is identical to the dispatch optimisation problem faced by the supply and demand agents. Hence, a solution that satisfies the KKTs of the market clearing problem will also be a solution of the dispatch optimisation problem.

By concatenating the optimality conditions of the supply and demand agent dispatch problems and the linking constraint, we have formed a Mixed Complementarity Problem. Through the equivalence of the KKTs we have also proved that the market clearing problem is the **Equivalent Optimisation Problem (EOP)** of the Mixed Complementarity Problem ({eq}`MCP_KKT`).

```{warning} Every optimisation has an equivalent MCP, but not every MCP has an equivalent optimisation problem.
```

### Solving MCPs

There are three different approaches to solving the MCP and calculate the clearing price of the market:

* This MCP can be solved directly either with dedicated solvers such as [PATH](https://pages.cs.wisc.edu/~ferris/path.html) or as a feasibility problem (NLP or MILP) using optimisation. In simple cases, you can determine the equilibrium solution analytically by deriving best response functions (see {numref}`content:mixed-complementarity:nash-cournot-games`). Larger problems, however, are very challenging to solve directly as we are - by definition, due to the complementarity conditions - dealing with non-linear problems.
* Apply price-search algorithms and iterative methods. The general principle of such methods is as follows: we start by making an educated guess on what the equilibrium price $\lambda$ in the game is. We present this price to each of the agents in the game and solve their decision problems. Those solutions are optimal from their perspective, but may not ensure that demand and supply are matched (Eq. (2)). Based on the mismatch in demand and supply, we adjust the price $\lambda$ accordingly and repeat this process until we have found the equilibrium price $\lambda$. We will not cover these techniques here.
* For some MCPs, we can derive an equivalent optimisation problem (EOP) and solve it like we do other problems - using mathematical programming languages such as YALMIP or Pyomo and solvers such as Gurobi. This builds on the notion that if we can find an optimisation problem that is described by the same set of KKT conditions as the MCP, solutions to that optimisation problem will -- by definition -- also be solutions to the MCP.

## Use of an inverse demand function

We can formulate the MCP problem through the use of an inverse demand function. Instead of the price-quantity bids of the demand agents, w use a linear relationship between the price of electricity and the demanded quantity to represent the demand side of the market. The linear equation takes the form of :

```{math}
:label: linear demand
\begin{align}
λ = \overline{λ} - β \cdot \sum_{j \in J} q^d_j
\end{align}
```

From the market clearing constraint we know $\sum_{j \in J} q^d_j = \sum_{i \in I} q^s_i$. Hence, the inverse demand function can be rewritten as $λ = \overline{λ} - β \cdot \sum_{i \in I} q^s_i$. In this way, we have eliminated the second vector of decision variables $q^d_j$. The $\overline{λ}$ is the interceptor of the demand curve and signifies the maximum willingness to pay and you can see the graphic interpretation of the inverse curve in {numref}`fig-inverse-demand`. Taking all the above into account, the game can be finally reformulated as :

```{figure} ../images/inverse_demand_function.jpg
:name: fig-inverse-demand
Inverse demand function and supply curve, based on supply-side bid pairs.
```

```{math}
:label: game_inverse_demand
\begin{align}
    & \max \{(\lambda - VC_i) \cdot q^s_i \quad \forall i \in I \tag{8} \\
    & \text{s.t.} \quad 0 \leq q^s_i \leq \overline{Q^s_i} \quad (\underline{\mu_i}, \overline{\mu_i}) \} \tag{9} \\
    &\lambda = \overline{\lambda} - \beta \cdot \sum_{i \in I} q^s_i \tag{14} \\
\end{align}

```

The KKT conditions of the decision problems of the suppliers and the inverse demand function jointly make up the MCP of this Nash game. Note that the inverse demand function participates as-is in the MCP, but is not part of the optimisation problem (it is outside of the curly brackets). That is the case since we are studying a Nash game, and therefore, the suppliers do not consider the impact of their actions on the price.

```{math}
:label : MCP inverse demand
\begin{align}
& \{ VC_i - λ - \underline{μ_i} + \overline{μ_i} = 0 \tag{10a} \\
& 0 \leq q^s_i \leq \overline{Q^s_i} \quad (\underline{μ_i}, \overline{μ_i}) \tag{9} \\
& -\underline{μ_i} \cdot q^s_i = 0 \tag{10b} \\
& \overline{μ_i} \cdot (q^s_i - \overline{Q^s_i}) = 0 \tag{10c} \\
& \underline{μ_i}, \overline{μ_i} \geq 0 \tag{10d} \} \\
& λ = \overline{λ} - β \cdot \sum_{i \in I} q^s_i \tag{14} \\
\end{align}
```

With the MCP defined, we can now derive the Equivalent optimisation problem to determine the equilibrium solution to the game in Eq. {eq}`game_inverse_demand`. Remember here, that the KKT conditions of the EOP have to match the MCP in order for the EOP to provide a solution to the initial problem. To derive the EOP, we make use of the graphical interpretation of the problem show in {numref}`fig-inverse-demand`.

From the discussion above, we know that the Nash game between suppliers and consumers in perfectly competitive electricity markets will maximize social welfare in that market. Hence, we can formulate a candidate EOP which aims to maximize social welfare. Based on {numref}`fig-inverse-demand-area` and the fact that  social welfare is the area between the demand and supply curve, social welfare can be computed as :

$$
SW = (ABDE) - (ABC) - \text{Area of sketched polygon} = \overline{\lambda} \cdot \sum_{i} q^s_i - \frac{1}{2}\beta(\sum_{i} q^s_i)^2 - \sum_{i} VC_i \cdot q^s_i
$$

```{figure} ../images/area_inv_demand.jpg
:name: fig-inverse-demand-area
Areas to calculate social welfare from inverse demand and supply curves.
```

The EOP should furthermore consider the constraints of the suppliers, resulting in the following optimisation problem:

```{math}
:label: EOP_Nash
\begin{align}
& \max \overline{\lambda} \cdot \sum_{i} q^s_i - \frac{1}{2}\beta (\sum_{i} q^s_i)^2 - \sum_{i} VC_i \cdot q^s_i \tag{15} \\
& \text{s.t}\\
& 0 \leq q^s_i \leq Q^s_i \quad (\underline{μ_i}, \overline{μ_i}) \quad \forall i \in I \tag{3} \\
\end{align}
```

The equivalence of the MCP with the EOP can be demonstrated through the derivation of the KKTs for the EOP in Eq. {eq}`EOP_Nash`. Note that we now have an optimisation problem with quadratic terms in the objective. However, these problems are still convex, hence, KKT conditions are -- in all the cases that we consider -- necessary and sufficient conditions for optimality. This also means that we can use solver software that supports solving quadratic problems, like Gurobi and Cplex, to efficiently obtain solutions.

<!--
Let's assume a general optimisation problem, as seen below :

```{math}
\begin{align}
    &\min f(x) \\
    &\text{s.t:} \nonumber \\
    &h_i(x) = 0 \quad (λ_{i}) \quad \forall  i \in = 1, \dots, m \nonumber \\
    &g_j(x) \leq 0 \quad (μ_{i}) \quad \forall  j \in = 1, \dots, n \nonumber \\
\end{align}
```

The Lagrangian reads :

```{math}
:label: eqn:mcp-Lagrangian
\begin{equation}
    \mathcal{L} = f(x) + \sum_{i=1}^m \lambda_i \cdot h_i(x) + \sum_{j=1}^{n} \mu_j \cdot g_j(x)
\end{equation}
```

The KKT conditions of the problem are the following :

```{math}
:label: eqn:mcp-KKT
\begin{align}
    & \frac{\partial \mathcal{L}}{\partial x} = 0   \quad & (\text{Optimality conditions})\\
    & h_i(x) = 0 \quad \forall i \in  \{1,2,...,m\}  \quad &  (\text{Primal feasibility}) \\
    & g_j(x) \leq 0 \quad \forall j \in  \{1,2,...,n\}  \quad & (\text{Primal feasibility}) \\
    & \mu_j \cdot g_j(x) =  0 \quad \forall j \in  \{1,2,...,n\}  \quad & (\text{Complementary slackness conditions}) \\
    & \mu_j \geq 0 \quad \forall j \in  \{1,2,...,n\} & (\text{Dual feasibility})
\end{align}
```

For linear and convex quadratic optimisation problems, the KKT conditions are both sufficient and necessary conditions for optimality. In other words, any solution that satisfies these conditions is guaranteed to be an optimal solution to the optimisation problem. This system of equations is an example of a mixed complementarity problem (see box below). In the following paragraphs, we will examine how mixed complementarity problems (MCP) can help us solve market clearing problems from the perspective of market actors.

```{admonition} What is a mixed complementarity problem (MCP)?
The KKT conditions introduced in {numref}`content:duality-kkts:kkt-conditions` are a special case of a mixed complementarity problem (MCP). Below, we will use our existing knowledge of KKT conditions to formulate such problems - including by combining the KKT conditions from more than one optimisation problem into a single MCP.

You can find an extensive introduction to complementarity problems more generally, including formal mathematical definitions, and many applications to energy (markets), in {cite}`Gabriel_Conejo_Fuller_Hobbs_Ruiz_2013`.
```

## Nash games

We will first study a simple, single-time step market clearing problem. We start with the perspective of the market clearing operator, leveraging our knowledge of optimisation and electricity markets. Next, we move to the perspective of the individual market participants, assuming they compete in a Nash game. Based on the KKT conditions of both problems, we will be able to show that both formulations yield the same result. We conclude this section by introducing an alternative, condensed formulation using inverse demand functions, which prepares us for the Nash-Cournot games in the following section.

### The market clearing problem from the perspective of the market operator

Let's start with a simple market clearing problem. The market-clearing problem is relevant to a pool-like market. We start by formulating the market clearing problem  from the perspective of the market operator, which aims at maximizing social welfare.

### The market clearing problem from the perspective of the market participants and the resulting MCP

Now let's look at the issue from the perspective of the supply and demand agents participating in the electricity market. Contrary to what is presented up to now, supply and demand agents now have to decide on how much to generate or consume. So what is the optimisation problem faced by the suppliers (generators) and the demand agents (customers, retailers) that aim to maximize their profit or utility?

First, the generators want to maximize their profit considering the market clearing price as given

(recall that in Nash games, agents are assumed to be price-takers).

In that case, the market clearing price $λ$ is a parameter and not a decision variable in the optimisation problem of the individual market participants. Note that it will be a decision variable in the MCP describing the Nash game.

Secondly,, again by using the assumption that their actions do not influence the market price. Therefore, the optimisation problem faced by the demand-side agents is :

The two different optimisation problems are connected through a common linking or coupling constraint, requiring supply and demand quantities to match. That is Eq. (2) of the initial market clearing problem. To determine the equilibrium of the Nash game between demand and supply agents, we need to **simultaneously** s of Problem {eq}`market_clearing`.

By concatenating the KKTs of the individual problems (Eqs. {eq}`supply_side`, {eq}`demand_side`) along with the linking constraint, we obtain the mixed complementarity problem associated with this Nash game:

-->

(content:mixed-complementarity:nash-cournot-games)=

## Nash-Cournot games

Up to now, we have assumed a **perfectly competitive market**, meaning firms have zero market power and act as pure price-takers. This is demonstrated by the example in {numref}`content:appendix:game-theory`. This was a **Nash game**. Contrary, in Nash-Cournot games agents strategically anticipate how their own quantity decisions influence the price (and hence their profit or utility). Each agent takes the decisions of the other players as given, as in a Nash game. In this Section, we will describe how the optimisation problem changes, when agents anticipate the impact of their actions on price.

### A simple Nash-Cournot game

To simplify notation, we will make use of an inverse demand curve to simulate the demand side. To allow agents to strategically anticipate how their actions influence the price, the inverse demand curve (14, below) now **is part of the optimisation problem** (note the position of the curly bracket). The Nash-Cournot game is:

```{math}
:label: Nash_Cournot
\begin{align}
&\max \{(\lambda - VC_i) \cdot q^s_i \quad &\forall i \in I \tag{8} \\
& \text{s.t.} \quad 0 \leq q^s_i \leq \overline{Q^s_i} \quad (\underline{\mu_i}, \overline{\mu_i}) \tag{9} \\
&\lambda = \overline{\lambda} - \beta \cdot \sum_{i \in I} q^s_i \} \tag{14} \\
\end{align}
```

The MCP associated with the Nash-Cournot game in Eq. {eq}`Nash_Cournot` can be obtained by deriving the KKT conditions of the optimisation problems that make up the game:

```{math}
:label: KKT_Nash_Cournot
\begin{align}
& \{ -\overline{λ} + β \cdot \sum_{i \in I} q^s_i + β \cdot q^s_i + VC_i - \underline{μ_i} + \overline{μ_i} = 0 \tag{10a'} \\
& 0 \leq q^s_i \leq \overline{Q^s_i} \quad (\underline{μ_i}, \overline{μ_i}) \tag{9} \\
& -\underline{μ_i} \cdot q^s_i = 0 \tag{10b} \\
& \overline{μ_i} \cdot (q^s_i - \overline{Q^s_i}) = 0 \tag{10c} \\
& \underline{μ_i}, \overline{μ_i} \geq 0 \tag{10d} \}
\end{align}
```

To understand the derivation of (10a') in Eq. {eq}`KKT_Nash_Cournot`, we can say that the Lagrangian of {eq}`Nash_Cournot` is:

$$
\mathcal{L} = -(λ - VC_i) \cdot q^s_i - \underline{\mu_i}q^s_i + \overline{\mu_i}(q^s_i - \overline{Q^s_i})
$$

Substituting equation (14) from Eq. {eq}`Nash_Cournot`, which defines the inverse demand function, into the Lagrangian, yields:

$$
\mathcal{L} = -\overline{λ}q^s_i + β \cdot q^s_i \cdot \sum_{i} q_i^s + VC_i \cdot q_i^s - \underline{\mu_i}q^s_i + \overline{\mu_i}(q^s_i - \overline{Q^s_i})
$$

Finally, differentiating the Lagrangian with respect to $q^s_i$ yields (10a') in {eq}`KKT_Nash_Cournot`:

$$
\frac{\partial \mathcal{L}}{\partial q_i^s} = -\overline{\lambda} + \beta \cdot \sum_{i} q_i^s + \beta \cdot q^s_i + VC_i - \underline{\mu_i} + \overline{\mu_i}
$$

### Obtaining Nash-Cournot Equilibria via equivalent optimisation problems

Nash-Cournot games can be solved with similar methods to Nash games, by either:

* directly solving the MCP: analytically/graphically using best response functions or via dedicated solvers; <!--TODO: add reference to numerical example using best response functions -->
* through iterative price search algorithms;
* through the derivation of an equivalent optimisation problem, which can be solved through optimisation algorithms.

How can the EOP be obtained in the case of a Nash-Cournot game? As always, this entails finding an optimisation problem that has the same KKT conditions as the MCP {eq}`KKT_Nash_Cournot`. In contrast to the Nash game, we cannot leverage any knowledge related to the equilibrium solution: Nash-Cournot equilibria are *not* welfare-maximizing. Comparing the MCP of the Nash game and the Nash-Cournot game, however, shows that they are identical with the exception of Eq. (10a) and Eq. (10a').

```{math}
\begin{align}
& -\overline{λ} + β \cdot \sum_{i \in I} q^s_i + VC_i - \underline{μ_i} + \overline{μ_i} = 0 \tag{10a} \\
&  -\overline{λ} + β \cdot \sum_{i \in I} q^s_i + β \cdot q^s_i + VC_i - \underline{μ_i} + \overline{μ_i} = 0 \tag{10a'} \\
\end{align}
```

The optimality condition in the Nash-Cournot game has an extra term of the form $β \cdot q^s_i$. With this information, we can now *adjust* the objective of EOP of the Nash game to ensure this additional term shows up in the KKT conditions. We do this by integrating the term that differentiates Eq. (10a) and Eq. (10a') and adding it to the objective of the EOP of the Nash game.

The resulting EOP for the Nash-Cournot game with $i \in I$ participants reads:

```{math}
:label: EOP_Nash_Cournot
\begin{align}
& \max \overline{\lambda} \cdot \sum_{i} q^s_i - \frac{1}{2}\beta \sum_{i} \left(q^s_i\right)^2 - \frac{1}{2}\beta (\sum_{i} q^s_i)^2 - \sum_{i} VC_i \cdot q^s_i \tag{15'} \\
& \text{s.t}\\
& 0 \leq q^s_i \leq Q^s_i \quad (\underline{μ_i}, \overline{μ_i}) \quad \forall i \in I \tag{3} \\
\end{align}
```

Note that the objective function of this EOP is no longer a measure of social welfare, in contrast to the objective of the EOP of the Nash game. The problem contains quadratic terms in the objective but is still convex.

## Final remarks

With the introduction of the Mixed Complementarity Problems as a way to solve the Nash and Nash-Cournot games, we have introduced a paradigm shift in the way we study interactions between self-interested market participants. Up to now, we were considering the market only from the side of a central market operator that aims to clear the market. Now, with the techniques introduced in this section, we can study simple electricity markets as the interaction between different market actors. Specifically, through the Nash games, we can understand the participation of agents in a perfectly competitive market. To study how strategic behaviour and market power change market outcomes, we introduced the Nash-Cournot equilibrium.

For both Nash and Nash-Cournot games, we developed formulations of the game (i.e., the set of interrelated optimisation problems and the coupling constraint) and the corresponding mixed complementarity problem (i.e., the KKT conditions of the decision problems of the involved actors and the coupling constraint). We discussed how we can determine the equilibria in such games, focusing on equivalent optimisation problems. For the Nash game, we showed that the equivalent optimisation problem is a maximization of social welfare. We also obtained an equivalent optimisation problem for the Nash-Cournot game.

These games allow making relationships and interactions between market agents explicit. In complex cases, for which the formulation of an optimisation problem is non-trivial, MCPs offer a more intuitive way of formalizing problems.

## References

```{bibliography}
:filter: docname in docnames
```
