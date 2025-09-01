# Dealing with uncertainty

We can distinguish two broad kinds of uncertainty (recall the discussion of uncertainty in {numref}`content:sensitivity-analysis`): structural uncertainty and parametric uncertainty. **Structural uncertainty** pertains to uncertainty in the model's structure: we are not certain if the model is an appropriate representation of reality. For example, it could be oversimplified in a way that limits its usefulness for our intended application because we model nonlinear relations with linear equations. **Parametric uncertainty** stems from limited information on the parameters in the model: the numbers we feed into it. Assuming the structure of our model is broadly fine, we may still be uncertain about the exact value of particular parameters to fill in, such as electricity demand or wind power generation. We will only discuss this second type of uncertainty here.

```{figure} ../images/uncertainty-types.jpg
:name: fig:uncertainty_summary
:figwidth: 550px

Parametric and structural uncertainty. Based on a talk by David Spiegelhalter, "Uncertainty in Decision Models" (not available online).
```

(content:uncert-parametric)=

## Parametric uncertainty

We have already covered one method to deal with parametric uncertainty in {numref}`content:sensitivity-analysis`: sensitivity analysis. We checked how the optimal solution changes as parameters in the problem formulation change.

An alternative to sensitivity analysis is robustness analysis: here, we take a solution (e.g. the optimal solution) and investigate how well it performs when parameters change. Like sensitivity analysis, this is done after the model is solved.

What about methods that allow us to incorporate uncertainty already when we formulate a model? There are two widely-used approaches for doing that.

First, there is stochastic programming. In stochastic programming, we explicitly model the fact that some parameters are uncertain, and we assume that we know the probabilities of specific outcomes for these parameters. We can set up several scenarios with known probabilities and formulate our problem such that all scenarios are considered, along with their probabilities, in solving the optimisation problem. As a result, stochastic programming can tell us what decisions to make based on our uncertainty quantification in the form of scenarios and their probabilities. Its usefulness depends heavily on how well these scenarios represent the uncertainties they represent.

Second, there is robust optimisation. Here also, we explicitly model the fact that some parameters are uncertain. There are different kinds of robust optimisation, but most commonly, problems are formulated so that the worst-case realisation of uncertain parameters is accounted for (and thus optimised for). At the same time, robust optimisation ensures that the solution is feasible for all possible realisations of the uncertain parameters. So we have a solution that is guaranteed to work, based on our assessment of the uncertainty in parameters, and works best in their worst-case realisation.

Robust optimisation is very different from how stochastic programming deals with uncertainty: rather than optimising for a single (worst-case) outcome, stochastic programming allows us to explicitly consider different uncertain outcomes---if we can describe these uncertain outcomes as a set of scenarios with given probabilities (which, in practice, can be difficult or even impossible).

:::{admonition} The key difference between stochastic programming and robust optimisation
:class: important

* The key assumption in stochastic programming is that the uncertain parameters are characterised by a known probability distribution.
* The key assumption in robust optimisation is that the uncertain parameters are contained in a known uncertainty set, without knowledge about the distribution of values within this set. However, it is not always clear how to choose an appropriate shape and size for this uncertainty set and depending on how it is defined, the problem can become very difficult to solve (see the appendix section on {ref}`content:uncert-robust`).

:::

No matter how we deal with parametric uncertainty, _characterising_ the uncertainty in the parameters is an important and tricky process. For example, how can we know what range of values an uncertain parameter might be in? Unfortunately, there is no general best practice for quantifying uncertainty. It depends on the specific situation and can be as much an art as science. Uncertainty can be quantified for example based on historic data, external models, expert opinion, and/or subjective assumptions.

We will devote specific attention to stochastic programming in the [next chapter](stochastic-programming.md). Before we move on to that, and following the overview table of parametric uncertainty methods below, the remainder of this section will briefly discuss how to deal with structural uncertainty.

(parametric-uncertainty-methods-table)=
:::{table} Overview of parametric uncertainty methods
|  | Stochastic programming | Robust optimisation | Sensitivity analysis | Robustness analysis |
| --- | --- | --- | --- | --- |
| When to do it | When formulating the model | When formulating the model | After we solve the model | After we solve the model |
| What you need | Explicit quantification of scenarios with their probability for uncertain variables | Specification of an uncertainty set for uncertain variables | Access to shadow prices, or a set of scenarios for parameter values to test | A model solution to test under different scenarios |
| What you get | Solution that includes the possibility for recourse---choosing one of several alternatives once we know more about the realisation of uncertain parameters | Solution that is feasible for any possible realisation of the uncertain parameters, and optimal for the worst case | Effect of changes in limited numbers of parameters on the optimal solution (e.g. by looking at shadow prices), but only for small perturbations around the optimal solution | Effect of changes in limited numbers of parameters on the feasibility of a fixed solution, but only for small perturbations in parameters |
| Where to read more | Section on {ref}`content:uncert-stochastic` | Appendix section on {ref}`content:uncert-robust` | Section on {ref}`content:sensitivity-analysis` | {cite:p}`starreveld.etal_robustness_2024` and example in {ref}`content:uncert-stochastic:comparison-without-uncert` |
:::

## Structural uncertainty

What if we also consider the possibility that our model itself is flawed, besides the fact that the values of our parameters are uncertain?

For example, we formulate a cost-minimisation problem, but in reality, we are willing to accept solutions that are not perfectly cost-minimal if they provide important secondary benefits. Thus looking for cost-minimal model solutions may be a structurally "wrong" thing to do.

One approach to deal with this is called "modelling to generate alternatives" or MGA. MGA methods explore the feasible space of a model (typically near the optimal solution) to generate alternative solutions that may be considerably different from the optimal solution in important respects.

A typical MGA approach works in two steps. First, we solve the model as usual, finding the optimal solution (for example, the solution with minimal cost). In a second step we replace the objective function with a different objective. This could be anything, and we will design the objective based on what kinds of solutions we are interested in - for example, solutions that minimise or maximise only certain specific decision variables. At the same time, we introduce the optimal value of the objective function from the first step as an additional constraint with a certain slack: for example, we add the constraint that the cost can be 10% higher than the minimal cost from step one. By solving this new model, we find alternative near-optimal solutions.

There are many recent examples of MGA use in the energy field, for example, the study "Diversity of options to eliminate fossil fuels and reach carbon neutrality across the entire European energy system" {cite:p}`pickering.etal_diversity_2022`.

Note that MGA methods do not by themselves address parametric uncertainty, but they can be combined with approaches that do so (for example, sensitivity analysis).

## References

```{bibliography}
:filter: docname in docnames
```
