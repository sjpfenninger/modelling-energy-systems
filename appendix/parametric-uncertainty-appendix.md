# Additional material on parametric uncertainty

There is much uncertainty surrounding future developments in technology, economics, and policy. For example, think of the uncertainty involved in forecasting natural gas prices and the impact a global pandemic or regional war can have on prices. It is important to account for uncertainty in modelling in order to make predictions of the future. We already discussed one way to address uncertainty in {numref}`content:uncert:stochastic-programming`: stochastic programming. This appendix gives a brief overview of other aspects of uncertainty in energy system optimisation models, including: characterising (or quantifying) uncertainty, analysing uncertainty (sensitivity analysis and robustness analysis), and two additional approaches to optimisation under uncertainty (robust optimisation and modelling to generate alternatives).

## Optimisation problem with parametric uncertainty
Recall from {numref}`content:uncert:optimisation-problem` the optimisation problem we aim to solve:
```{math}
:label: eqn:optimisation
\begin{align}
    \begin{split}
        \min_{\mathbf{x}}&~f(\mathbf{x}, \mathbf{z}) \\
        \text{s.t.}&~\mathbf{x} \in \mathcal{X}(\mathbf{z}) \\
    \end{split}
\end{align}
```

where $\mathbf{z}$ are the uncertain input parameters. $f(\mathbf{x},\mathbf{z})$ is the objective function with decision variables $\mathbf{x}$ which belong to the feasible region $\mathcal{X}(\mathbf{z})$ (constraints). Now the objective function is a function of the uncertain parameters $\mathbf{z}$ and the decision variables must belong to a feasible region that also depends on $\mathbf{z}$.

## Static vs. adaptive problem settings
In a static problem setting, the decisions $\mathbf{x}$ are made before the uncertain parameters $\mathbf{z}$ are observed. The decisions cannot be changed after the uncertain parameters are revealed. This leads to a single-stage optimisation problem. In the generation expansion planning example in {numref}`content:uncert:gen-exp-example`, the decisions of how much capacity investment to make in each generator have to be made before the uncertain parameters of demand, capacity factors, fixed costs, and variable costs are known. Once the uncertain parameters are revealed, the investment decision cannot be adjusted.

In contrast, an adaptive setting involves multiple stages of decisions. First, decisions $\mathbf{x}_0$ are made, then uncertain parameters $\mathbf{z}_1$ are observed. Then, the decision maker adapts to $\mathbf{z}_1$ and makes decisions $\mathbf{x}_1$. $\mathbf{z}_2$ are observed, $\mathbf{x}_2$ are decided, and so forth. Optimisation problems with more than two stages are very difficult to manage {cite:p}`dantzig1961solution` and are outside the scope of this course.

```{figure} ../images/static_opt_timeline.jpg
:name: fig:static
:figwidth: 350 px

Static problem setting {cite:p}`starreveld2024robustness`
```

```{figure} ../images/multistage_kstage_timeline.jpg
:name: fig:adaptive
:figwidth: 600 px

Adaptive problem setting {cite:p}`starreveld2024robustness`
```

## Uncertainty characterisation
Characterising uncertainty is an important, but tricky, process. The aim is to quantify the uncertainty surrounding the input parameters $\mathbf{z}$. We would like to know what range of values an uncertain parameter is in.

There is no general best practice for quantifying uncertainty. It depends on the specific situation and can be "more of an art than a science." Uncertainty can be quantified based on historic data, external models, expert opinion, and/or subjective assumptions. Nevertheless, uncertainty characterisation can have a great impact on results, so it is a process not to be overlooked.

Exogenous uncertainty is outside our control whereas endogenous uncertainty can be affected by our decisions. The latter is generally more difficult to deal with {cite:p}`nohadani2018optimization`. An example of exogenous uncertainty is the weather, where for example wind speed or cloud coverage are outside our control. An example of endogenous uncertainty is global temperature. Our behavior in how much carbon dioxide we emit has an impact on the global temperature.

Uncertainty can also change over time. Here, we will consider three types shown in {numref}`fig:unc_time`. Type I, the investment type, concerns a decision (investment) made at one time, so only the uncertainty in the parameter at that time matters. In Type II, the range of uncertainty remains constant over time. Lastly, the type we generally face is Type III, which deals with increasing uncertainty over time.

```{figure} ../images/Moret2017_characterization_Fig5.jpg
:name: fig:unc_time
:figwidth: 500px

Uncertainty over time {cite:p}`moret2017strategic`
```

## Analysis of uncertainty
We will now turn to analysing the potential impact of uncertain input parameters. Analysing uncertainty means properly describing and understanding the impact of model parameter variations on the model prediction. Due to an uncertain parameter, the outcome of a model can be desirable in one scenario and completely undesirable in another scenario, depending on the value of the uncertain parameter. Analysing uncertainty is an essential part of assessing any model. In particular, we will focus on sensitivity analysis and robustness analysis.

### Sensitivity analysis
**Sensitivity analysis** analyses the sensitivity of a model under variation in input parameters {cite:p}`saltelli2004sensitivity`. In {numref}`content:sensitivity-analysis` we already discussed sensitivity analysis in the specific context of the economic dispatch example. In sensitivity analysis, we change the value of the uncertain input parameters $\mathbf{z}$ and want to know 1) How does the optimal solution change? and 2) What is the optimal objective value?

It is assumed that the solution is fully flexible and able to adapt to changes in the model inputs. The solution is able to adapt with perfect foresight, so the uncertain parameters $\mathbf{z}$ are observed, then the decision is made ({numref}`fig:sensitivity`).

```{figure} ../images/SA_timeline.jpg
:name: fig:sensitivity
:figwidth: 400 px

Sensitivity analysis timeline {cite:p}`starreveld2024robustness`
```

Recall the optimisation problem in Equation {eq}`eqn:optimisation`. We input a set of scenarios, $S = \{ \mathbf{z}^1, ...,\mathbf{z}^N \}$, and evaluate the sensitivity of the model with respect to each scenario in $S$. For each scenario $i$, we determine the optimal solution $\mathbf{x}^*$ by re-solving the optimisation problem. Once we have the solution, we evaluate the objective function value $f(\mathbf{x}^*, \mathbf{z}^i)$. This algorithm can be described as follows:
```{prf:algorithm} Sensitivity Analysis
:label: sensitivity-analysis-algorithm

**Input** Set of scenarios $\mathcal{S} = \left\{\mathbf{z}^{1}, \ldots, \mathbf{z}^{N}\right\}$

**Output** Evaluation of sensitivity of model w.r.t. each scenario in $\mathcal{S}$

**for** scenario $i \in \{1, \dotsc, N\}$ **do**\
     1: Determine optimal solution $\mathbf{x}^*$ by solving $\min\limits_{\mathbf{x}}\{f(\mathbf{x}, \mathbf{z}^{i})~|~\mathbf{x} \in \mathcal{X}(\mathbf{z}^{i}) \}$ \
     2: Evaluate objective value by computing $f(\mathbf{x}^*, \mathbf{z}^{i})$
```

### Robustness analysis
In **robustness analysis**, we analyse the robustness of a _fixed_ solution under variation in the input parameters {cite:p}`Hertog_BenTal_Brekelmans_Roos_2021`. This situation is shown in {numref}`fig:robustness` where the decision $\mathbf{x}$ is made, then the uncertain parameters $\mathbf{z}$ are revealed (and the decision cannot be changed). We change the value of the uncertain input parameters and want to know 1) Is the solution feasible? and 2) What is the optimal objective value?

```{figure} ../images/static_opt_timeline.jpg
:name: fig:robustness
:figwidth: 400 px

Robustness analysis timeline {cite:p}`starreveld2024robustness`
```

Again, we consider a set of scenarios, $S = \{ \mathbf{z}^1, ...,\mathbf{z}^N \}$. Now we evaluate the robustness of a fixed solution $\bar{\mathbf{x}}$ with respect to each input scenario. For each scenario $i$, we first evaluate the feasibility by determining if the solution $\bar{\mathbf{x}}$ is in the feasible region $\mathcal{X}(\mathbf{z}^i)$. Then we compute the objective function value $f(\bar{\mathbf{x}}, \mathbf{z}^i)$. The algorithm is written as follows:
```{prf:algorithm} Robustness Analysis
:label: robustness-analysis-algorithm

**Input** Set of scenarios $\mathcal{S} = \left\{\mathbf{z}^{1}, \ldots, \mathbf{z}^{N}\right\}$, Given a solution $\bar{\mathbf{x}}$

**Output** Evaluation of robustness of $\bar{\mathbf{x}}$ w.r.t. each scenario in $\mathcal{S}$

**for** scenario $i \in \{1, \dotsc, N\}$ **do**\
    1: Evaluate feasibility by determining whether $\bar{\mathbf{x}} \in \mathcal{X}(\mathbf{z}^{i})$ \
    2: Evaluate objective value by computing $f(\bar{\mathbf{x}}, \mathbf{z}^{i})$
```

Note that unlike in sensitivity analysis, in robustness analysis, the model does not need to be re-solved for each scenario (because we consider a fixed solution). Only simple function evaluations are involved, so there is less computational effort than there is for sensitivity analysis.

### Local vs. global analysis
In local analysis, we evaluate how small perturbations in an input parameter affect the output of interest {cite:p}`trucano2006calibration`. Only one parameter, or a certain limited number of parameters, is altered at a time. By contrast, in global analysis, all the input parameters are varied simultaneously and they are varied over the whole domain of possible parameter values {cite:p}`Zhou2008`. There is a big difference in computational effort between local and global analysis when dealing with a large number of uncertain parameters.

## Optimisation under uncertainty
It is important to assess uncertainty in energy system optimisation models. In {numref}`content:uncert:stochastic-programming` we already discussed stochastic programming. Two additional approaches we will now discuss are robust optimisation and modelling to generate alternatives.

### Robust optimisation {cite:p}`Bertsimas_Hertog_2022`
Consider the optimisation problem
\begin{align}
    \begin{split}
        \min_{\mathbf{x}}&~f_0(\mathbf{x}, \mathbf{z}) \\
        \text{s.t.}&~f_1(\mathbf{x}, \mathbf{z}) \leq 0 \\
        &~~~~~\vdots \\
        &~f_m(\mathbf{x}, \mathbf{z}) \leq 0 \\
    \end{split}
\end{align}
again with decision variables $\mathbf{x}$ and uncertain parameters $\mathbf{z}$. There are $m$ constraints.

Now we reformulate the problem by moving the uncertainty to the constraints ("epigraph form"). $\theta$ is a deterministic objective function.
\begin{align}
    \begin{split}
        \min_{\mathbf{x},\theta}&~\theta \\
        \text{s.t.}&~f_0(\mathbf{x}, \mathbf{z}) \leq \theta \\
        &~f_1(\mathbf{x}, \mathbf{z}) \leq 0 \\
        &~~~~~\vdots \\
        &~f_m(\mathbf{x}, \mathbf{z}) \leq 0 \\
    \end{split}
\end{align}
Then we merge the multiple constraints into a single constraint:
\begin{align}
    \begin{split}
        \min_{\mathbf{x},\theta}&~\theta \\
        \text{s.t.}&~\underbrace{\max\{f_0(\mathbf{x}, \mathbf{z})-\theta, \max_{i=1,\dotsc,m} f_i(\mathbf{x}, \mathbf{z})\}}_{g(\mathbf{x}, \mathbf{z})} \leq 0 \\
    \end{split}
\end{align}
In "standard form", we write this as:
\begin{align}
    \begin{split}
        \min_{\mathbf{x}}&~f(\mathbf{x}) \\
        \text{s.t.}&~g(\mathbf{x}, \mathbf{z}) \leq 0 \\
    \end{split}
\end{align}
Note that there is no uncertainty in the objective function $f(\mathbf{x})$ (it is not a function of $\mathbf{z}$) and there is a single constraint $g(\mathbf{x}, \mathbf{z}) \leq 0$. Any problem can be rewritten in this "standard form", which is a deterministic optimisation problem.

Now we assume the uncertain parameters $\mathbf{z}$ are contained within some geometric "uncertainty set" $\mathcal{U}$. An example of an uncertainty set is shown in {numref}`fig:uncertainty_set`. The modeler can choose how large or small to make $\mathcal{U}$.

```{figure} ../images/uncertainty_set.png
:name: fig:uncertainty_set
:figwidth: 450px

Example geometric uncertainty set $\mathcal{U}$ {cite:p}`cheramin2021uncertaintyset`
```

Then we write the problem as:
\begin{align}
    \begin{split}
        \min_{\mathbf{x}}&~f(\mathbf{x}) \\
        \text{s.t.}&~g(\mathbf{x}, \mathbf{z}) \leq 0, ~~\forall \mathbf{z} \in \mathcal{U} \\
    \end{split}
\end{align}
The constraints must hold for all possible realisations of $\mathbf{z} \in \mathcal{U}$. We also optimise with respect to the worst-case of $\mathbf{z} \in \mathcal{U}$ because if the constraint holds for the worst-case $\mathbf{z}$ then it will hold for all other $\mathbf{z} \in \mathcal{U}$. Note that $\forall \mathbf{z} \in \mathcal{U}$ may imply an infinite number of constraints.

To solve the robust optimisation problem, we consider the reformulation approach and the adversarial approach.

#### Reformulation approach
The idea behind the **reformulation approach** is to solve the robust optimisation problem by creating a deterministic and finite equivalent, called a "robust counterpart". Depending on the shape of the uncertainty set, we can write a corresponding robust counterpart {cite:p}`Bertsimas_Hertog_2022`.

There are two important notes to make in the reformulation. The first is that $g(\mathbf{x}, \mathbf{z}) \leq 0, ~\forall \mathbf{z} \in \mathcal{U}$ is true if and only if $\max\limits_{\mathbf{z} \in \mathcal{U}}  g(\mathbf{x}, \mathbf{z}) \leq 0$. That is, if the constraint holds for the $\mathbf{z}$ that maximises $g$, then it holds for all other $\mathbf{z} \in \mathcal{U}$. Thus, we no longer have the issue of potentially an infinite number of constraints. Secondly, we can use duality to rewrite $\max\limits_{\mathbf{z} \in \mathcal{U}} \dots$ as $\min\limits_{\mathbf{y} \in \mathcal{Y}} \dots$. $\mathbf{y}$ are the dual variables. Now instead of a $\min\limits_{\mathbf{x}} \max\limits_{\mathbf{z}}$ problem, we have a $\min\limits_{\mathbf{x}} \min\limits_{\mathbf{y}}$ problem, which we can combine into a single $\min\limits_{\mathbf{x}, \mathbf{y}}$ problem.

#### Adversarial approach
The idea behind the **adversarial approach** is to solve the robust optimisation problem by viewing it as a game between the decision maker $\mathbf{x}$ and an "adversary" $\mathbf{z}$. The game is played as follows:
1. The decision maker makes the first move by optimising the problem for the nominal scenario $\mathbf{z}_{0}$ to obtain an initial solution $\mathbf{x}_0$ \
    $\begin{align}
        \min\limits_{\mathbf{x}}&~f(\mathbf{x}) \\
        \text{s.t.}&~g(\mathbf{x}, \mathbf{z}_{0}) \leq 0 ~\\
    \end{align}
    \bigg \rbrace \Rightarrow \mathbf{x}_0 $
2. The adversary searches for the worst possible counter to $\mathbf{x}_0$ by maximising $g$ given $\mathbf{x}_0$ to obtain a counter $\mathbf{z}_1$ \
    $\begin{align}
        \max\limits_{\mathbf{z}}&~g(\mathbf{x}_0, \mathbf{z})~ \\
        \text{s.t.}&~\mathbf{z} \in \mathcal{U}~~\\
    \end{align}
    \bigg \rbrace \Rightarrow \mathbf{z}_1  $ \
    Since the decision maker is trying to get $g \leq 0$, the adversary maximises $g$ to find the worst-case scenario. \
    $\ast$ If the adversary finds a counter $\mathbf{z}_1$ such that $g(\mathbf{x}_0, \mathbf{z}_1) > 0$, we continue by finding a new optimal solution (Step 3). If $g(\mathbf{x}_0, \mathbf{z}_1) > 0$ that means the constraint is violated so we have to continue looking for a solution. Otherwise, if $g(\mathbf{x}_0, \mathbf{z}_1) \leq 0$, then $\mathbf{x}_0$ is a solution to the robust optimisation problem so the game stops.
3.  The decision maker reacts to the adversary's counter $\mathbf{z}_1$ by looking for a new solution $\mathbf{x}_1$ \
    $\begin{align}
        \min\limits_{\mathbf{x}}&~f(\mathbf{x}) \\
        \text{s.t.}&~g(\mathbf{x}, \mathbf{z}_{0}) \leq 0, ~\\
        &~g(\mathbf{x}, \mathbf{z}_{1}) \leq 0, ~\\
    \end{align}
    \Biggr \rbrace \Rightarrow \mathbf{x}_1  $ \
    Now, there are two constraints, considering both $\mathbf{z}_0$ and $\mathbf{z}_1$.
4.  The adversary searches for the worst possible counter $\mathbf{z}_2$ to $\mathbf{x}_1$ \
    $\begin{align}
        \max\limits_{\mathbf{z}}&~g(\mathbf{x}_1, \mathbf{z})~ \\
        \text{s.t.}&~\mathbf{z} \in \mathcal{U}~~\\
    \end{align}
    \bigg \rbrace \Rightarrow \mathbf{z}_2  $ \
    $\ast$ If the adversary finds a counter $\mathbf{z}_2$ such that $g(\mathbf{x}_1, \mathbf{z}_2) > 0$, we continue by finding a new optimal solution. Otherwise, if $g(\mathbf{x}_1, \mathbf{z}_2) \leq 0$, then $\mathbf{x}_1$ is a solution to the robust optimisation problem so the game stops.
5.  The game continues with the decision maker reacting to the adversary's counter to obtain a new solution, then the adversary finding a worst possible counter, and so on. We continue until the adversary cannot find a counter that violates the constraint.

The following table summarises the pros and cons of the reformulation approach and adversarial approach. The best approach depends on the situation {cite:p}`bertsimas2016reformulation`.
| **Reformulation approach** {cite:p}`ben1998robust` | **Adversarial approach** {cite:p}`mutapcic2009cutting` |
| --- | --- |
| + Single problem to solve | -- Iteratively solve multiple problems |
| -- Requires deriving robust counterpart | + Simple to implement |
| -- Problem size increased at start | + Problem size increases incrementally |
| -- More difficult when uncertainty set is non-convex | -- May require many iterations before convergence |

#### Limitations of robust optimisation
Robust optimisation relies on the assumption that the uncertain parameters $\mathbf{z}$ are contained within some uncertainty set $\mathcal{U}$. However, it is not always clear how to choose an appropriate shape and size of $\mathcal{U}$. This affects our ability to solve a robust optimisation problem. Additionally, our ability to solve a robust optimisation problem depends on the function $g$ and the uncertainty set $\mathcal{U}$. If $g$ is non-concave in $\mathbf{z}$, then exact reformulations of the problem are known for only certain combinations of $g$ and $\mathcal{U}$. Lastly, when solving robust optimisation problems in practice, it may involve an unacceptably large increase in the number of variables and constraints, making the problem difficult to solve even though it is theoretically tractable.

:::{admonition} Difference in key assumption between stochastic programming and robust optimisation
:class: important

The key assumption in stochastic programming is that the uncertain parameters are characterised by a known probability distribution.
The key assumption in robust opimisation is that the uncertain parameters are contained in some uncertainty set.

:::

#### Distributionally robust optimisation
The idea behind **distributionally robust optimisation** is to combine stochastic programming and robust optimisation {cite:p}`Bertsimas_Hertog_2022` {cite:p}`delage2010distributionally`. Recall the stochastic programming problem in Equation {eq}`eqn:stochastic` (repeated below):
\begin{align}
    \begin{split}
        \min_{\mathbf{x}}&~\mathbb{E}_{\mathbb{P}} \left[ f(\mathbf{x}, \tilde{\mathbf{z}}) \right] \\
        \text{s.t.}&~\mathbb{P} \left( g(\mathbf{x}, \tilde{\mathbf{z}}) \leq 0 \right) \geq 1-\epsilon \\
    \end{split}
\end{align}
$\mathbb{P}$ is the probability distribution of $\tilde{\mathbf{z}}$, which is often unknown. Thus, we assume $\mathbb{P}$ is contained within some "ambiguity set" $\mathcal{P}$. Think of $\mathcal{P}$ as a sort of equivalent to the uncertainty set $\mathcal{U}$ except for probability distributions.

```{figure} ../images/DRO_ambiguity_set.png
:name: fig:ambiguity_set
:figwidth: 300px

An ambiguity set $\mathcal{P}$ of probability distributions. The probability distribution $\mathbb{P}$ of $\tilde{\mathbf{z}}$ takes on one of these distributions, but we are uncertain as to which. {cite:p}`shen2020ambiguityset`
```

So we formulate a distributionally robust optimisation problem:
\begin{align}
    \begin{split}
        \min_{\mathbf{x}} \max_{\mathbb{P} \in \mathcal{P}}&~\mathbb{E}_{\mathbb{P}} \left[ f(\mathbf{x}, \tilde{\mathbf{z}}) \right] \\
        \text{s.t.}&~\mathbb{P} \left( g(\mathbf{x}, \tilde{\mathbf{z}}) \leq 0 \right) \geq 1-\epsilon,~~\forall \mathbb{P} \in \mathcal{P} \\
    \end{split}
\end{align}
We optimise with respect to the worst-case distribution $\mathbb{P} \in \mathcal{P}$. It turns out that distributionally robust optimisation can in many cases be solved more efficiently than stochastic programming.

### Modelling to generate alternatives {cite:p}`brill1982modeling` {cite:p}`lombardi2020policy`
Real world problems are quite complex. They may not be captured realistically in a mathematical model. So instead of fixating on a single optimal solution, we can explore multiple near-optimal solutions. For example, we can make multiple scenarios for a carbon-neutral energy system {cite:p}`pickering2022diversity`. It is also helpful to provide policymakers with diverse solution options like a set of energy transition pathways.

{numref}`fig:MGA` shows the concept of exploring the near-optimal solution space. The gray area depicts the feasible space of solutions. The red x represents the single optimal solution $\mathbf{x}^*$ with corresponding optimal objective value $f(\mathbf{x}^*)$. The green area represents the solution space if we allow an $\epsilon \%$ increase in the objective value. We see that there are many similar solutions between $\underline{\mathbf{x}}^\epsilon$ and $\bar{\mathbf{x}}^\epsilon$ which are near-optimal.

```{figure} ../images/near_optimal_space.png
:name: fig:MGA

Exploring the near-optimal solution space in modelling to generate alternatives {cite:p}`neumann2021near`
```

There are a number of limitations of modelling to generate alternatives. Firstly, it does not deal with parametric uncertainty, but it does address structural uncertainty. Therefore, it is a good idea to pair it with robustness analysis. Secondly, for large-scale problems, there is a large number of possible search directions. Therefore, we may only be able to explore a limited part of the near-optimal solution space. Thirdly, it can be difficult to determine which alternatives are most desirable and to measure how diverse the set of alternatives is. The ultimate objective of the problem can be unclear or subjective.

## Summary
The table below compares the ways to deal with parametric uncertainty which were discussed in this chapter:
|  | Stochastic programming | Robust optimisation | Sensitivity analysis | Robustness analysis |
| --- | --- | --- | --- | --- |
| When do we do it | When formulating the model | When formulating the model | After we solve the model | After we solve the model |
| What do we need | Explicit quantification of scenarios with their probability for uncertain variables | Specification of an uncertainty set for uncertain variables | A model and a set of scenarios | A model, a set of scenarios, and a fixed solution |
| What do we get | Solution that includes the possibility for recourse---choosing one of several alternatives once we know more about the realisation of uncertain parameters | Solution that is feasible for any possible realisation of the uncertain parameters, and optimal for the worst case | Effect of changes in limited numbers of parameters on the optimal solution (e.g. by looking at shadow prices), but only for small perturbations around the optimal solution | Effect of changes in limited numbers of parameters on the feasibility of a fixed solution, but only for small perturbations in parameters |


## References

```{bibliography}
:filter: docname in docnames
```