# Stochastic programming

(content:uncert-stochastic:introduction)=

## Ways to deal with parametric uncertainty

We can distinguish two broad kinds of uncertainty (recall the discussion of uncertainty in {numref}`content:sensitivity-analysis`): structural uncertainty and parametric uncertainty. **Structural uncertainty** pertains to uncertainty in the model's structure: we are not certain if the model is an appropriate representation of reality. For example, it could be oversimplified in a way that limits its usefulness for our intended application because we model nonlinear relations with linear equations. **Parametric uncertainty** stems from limited information on the parameters in the model: the numbers we feed into it. Assuming the structure of our model is broadly fine, we may still be uncertain about about the exact value of certain parameters to fill in, such as electricity demand, or wind power generation. We will only discuss this second type of uncertainty here.

```{figure} ../images/uncertainty-types.jpg
:name: fig:uncertainty_summary
:figwidth: 550px

Parametric uncertainty in the context of broader uncertainty. Based on a talk by David Spiegelhalter, "Uncertainty in Decision Models" (not available online).
```

We have already covered sensitivity analysis in {numref}`content:sensitivity-analysis`. In sensitivity analysis, we checked how the optimal solution changes as parameters in the problem formulation change (as discussed in {numref}`content:sensitivity-analysis`). An alterative to sensitivity analysis is robustness analysis: here, we take a solution (e.g. the optimal solution) and investigate how well it performs when parameters change. You can read more about this in {cite:p}`starreveld2024robustness`.

What about methods that allow us to incorporate uncertainty already when we formulate a model There are two widely-used approaches for doing that.

First, there is stochastic programming. In stochastic programming we explicitly model the fact that some parameters are uncertain, and we assume that we know the probabilities of certain outcomes for these parameters. We can set up several scenarios with known probabilities and formulate our problem such that all scenarios are considered, along with their probabilities, in solving the optimisation problem. As a result, stochastic programming can tell us what decisions to make based on our uncertainty quantification in the form of scenarios and their probabilities. Its usefulness depends heavily on how well these scenarios represent the uncertainties they represent.

Second, there is robust optimisation. Here also, we explicitly model the fact that some parameters are uncertain. There are different kinds of robust optimisation, but most commonly, problems are formulated so that the worst-case realisation of uncertain parameters is accounted for (and thus optimised for). This is very different from how stochastic programming deals with uncertainty: rather than optimising for a single (worst-case) outcome like robust optimisation, stochastic programming allows us to explicitly consider different uncertain outcomes -- if we can describe these uncertain outcomes as a set of scenarios with given probabilities (which, in practice, can be difficult or even impossible).

In addition to sensitivity analysis, we can also perform robustness analysis. Like sensitivity analysis, this is done after the model is solved.

The following table gives a high-level overview of all the methods mentioned so far:

|  | Stochastic programming | Robust optimisation | Sensitivity analysis | Robustness analysis |
| --- | --- | --- | --- | --- |
| When to do it | When formulating the model | When formulating the model | After we solve the model | After we solve the model |
| What you need | Explicit quantification of scenarios with their probability for uncertain variables | Specification of an uncertainty set for uncertain variables | A model and a set of scenarios | A model, a set of scenarios, and a fixed solution |
| What you get | Solution that includes the possibility for recourse---choosing one of several alternatives once we know more about the realisation of uncertain parameters | Solution that is feasible for any possible realisation of the uncertain parameters, and optimal for the worst case | Effect of changes in limited numbers of parameters on the optimal solution (e.g. by looking at shadow prices), but only for small perturbations around the optimal solution | Effect of changes in limited numbers of parameters on the feasibility of a fixed solution, but only for small perturbations in parameters |
| Where to read more | Below in this chapter | In a future version of this reader | {numref}`content:sensitivity-analysis` | {cite:p}`starreveld2024robustness` |

For the remainder of this chapter, we move on to stochastic programming.

## Stochastic programming example: demand response

In this example, we want to adjust demand to better match the fluctuating supply of renewable energy sources. A consumer performs a certain task that requires the use of electricity. The utility function $f_t(u_t)$ measures the benefit of consuming energy $u_t$ for the task during time period $t = 1, ..., T$.

### {{ labeled_circle_params }}

Consider four time periods ($T = 4$).

We know that the total consumption for the four time periods together must be between 6 and 8 kWh.

We also know the consumption cannot be higher than $U_{max}$ = 3 kWh for each time period $t$.

We also know the ramping limit (up or down) is $U_{ramp}$ = 1.5 kWh between any two time periods.

Now we introduce uncertainty with a stochastic process. Electricity price per time period is an uncertain parameter. We consider price uncertainty with scenarios, indexed by $\omega$. $\lambda$ is the set of possible realisations of the stochastic process, or prices. $\lambda_\omega$ is a vector representing one possible realisation of the stochastic process. (Note that in this example, stochastic process = uncertain model parameter = price uncertainty.) Each realisation $\lambda_\omega$ is associated with a probability $\pi_\omega$. In this example, we consider a discrete probability distribution consisting of two scenarios so the probabilities $\pi_1$ and $\pi_2$ add up to 1. The table below shows the scenarios we consider.

| Scenario | Probability | Price | Price | Price | Price |
| --- | --- | --- | --- | --- | --- |
| $\omega$ | $\pi_\omega$ | $\lambda_1$| $\lambda_{2\omega}$ | $\lambda_{3\omega}$ | $\lambda_{4\omega}$ |
| 1 | 0.5 | 120 | 105 | 154 | 84 |
| 2 | 0.5 | 120 | 45 | 66 | 36 |

So, we have two scenarios with 50\% probability each. Note that $\lambda_1 = 120$ in both scenarios.

### {{ labeled_circle_vars }}

We want to decide how much energy to consume $u_{t\omega}$ during time period $t = 1, ..., T$. Because we have two scenarios, and one certain time period, there are seven optimisation variables: $u_1, u_{21}, u_{31}, u_{41}, u_{22}, u_{32}, u_{42}$ (the consumption at $t=1$ and the scenario-dependent consumption at $t=2,3,4$).

### {{ labeled_circle_obj }}

Our objective is to maximise welfare (minimise costs minus benefits):

\begin{align}
    \min \left[ \lambda_1 u_1 - f_1(u_1) + \sum_{\omega=1}^\Omega \pi_\omega \times \sum_{t=2}^T (\lambda_{t\omega} u_{t\omega} - f_t(u_{t\omega}) ) \right]
\end{align}

This is the implementation of the objective function in Equation {eq}`eqn:stochastic_discrete`. The first part with $t=1$ represents the certain part because $\lambda_1 = 120$ always. We will use a utility function $f_t(u_t)$ which is a linear function of consumption $u_t$: $f_t(u_t) = 100 u_t$.

### {{ labeled_circle_constr }}

We have three practical constraints to consider.

First, the consumption per time period cannot be higher than $U_{max}$ = 3 kWh:

\begin{equation}
    U_{min} \leq u_t \leq U_{max}
\end{equation}

Second, the total consumption for the four periods together must be between 6 and 8 kWh.

Third, there is a ramping limit of 1.5 kWh between time periods.

### Full problem

In our example, we end up with the following optimisation problem:

* Variables: $u_1, u_{21}, u_{31}, u_{41}, u_{22}, u_{32}, u_{42}$
* Objective (to be minimised):
\begin{equation}
    \begin{split}
        J = &  (120-100)u_1 + 0.5\left[(105-100)u_{21} + (154-100)u_{31} + (84-100)u_{41}\right] \\
        & + 0.5\left[(45-100)u_{22} + (66-100)u_{32} + (36-100)u_{42}\right]
    \end{split}
\end{equation}
* Consumption per time period constraint:
\begin{equation}
    \begin{split}
        0 \leq u_1 \leq 3 & \\
        0 \leq u_{t\omega} \leq 3 & \hspace{20 pt} \omega=1,2, t=2,3,4 \\
    \end{split}
\end{equation}
* Total consumption constraint:
\begin{equation}
    \begin{split}
        u_1 + \sum_t u_{t\omega} \leq 8 & \hspace{20 pt} \omega=1,2, t=2,3,4 \\
        u_1 + \sum_t u_{t\omega} \geq 6 & \hspace{20 pt} \omega=1,2, t=2,3,4 \\
    \end{split}
\end{equation}
* Ramping limits constraint:
\begin{equation}
    \begin{split}
        u_1 - u_0 \leq 1.5 & \hspace{20 pt} \omega=1,2, u_0=0 \\
        u_{2\omega} - u_1 \leq 1.5 & \hspace{20 pt} \omega=1,2 \\
        u_{t\omega} - u_{(t-1)\omega} \leq 1.5 & \hspace{20 pt} \omega=1,2, t=3,4 \\
        u_0 - u_1 \leq 1.5 & \hspace{20 pt} \omega=1,2, u_0=0 \\
        u_1 - u_{2\omega} \leq 1.5 & \hspace{20 pt} \omega=1,2 \\
        u_{(t-1)\omega} - u_{t\omega} \leq 1.5 & \hspace{20 pt} \omega=1,2, t=3,4 \\
    \end{split}
\end{equation}

### Optimal solution

The optimal solution of our example is:
| Scenario | $u_1$ | $u_{2\omega}$ | $u_{3\omega}$ | $u_{4\omega}$ | Total |
| --- | --- | --- | --- | --- | --- |
| 1 | 0.25 | 1.75 | 1.25 | 2.75 | 6 |
| 2 | 0.25 | 1.75 | 3 | 3 | 8 |

```{figure} ../images/stochastic_programming_ex_soln.png
:name: fig:stochastic_programming_ex_soln
:figwidth: 450px

Optimal solution of energy consumption during each time period
```

We can think of our example as a two-stage stochastic programming problem. In the first stage (here and now), decisions $u$, not depending on the realisation of the uncertain parameters, are made. The parameters (price) in the first time period $t=1$ are certain so we can decide how much energy to consume now, $u_1$. Then, the outcome $\lambda_\omega$ of the random parameter vector $\lambda$ is realised. In the second stage (wait and see), the decisions $u_\omega$ are made according to $\lambda_\omega$. As the price in each time period is revealed, we adapt and decide how much energy to consume. This two-stage approach allows the decision-maker to adapt to the actual outcome of random events while still achieving the overall optimal outcome given the uncertainty.

## References

```{bibliography}
:filter: docname in docnames
```
