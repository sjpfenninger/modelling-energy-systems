(content:appendix:duality-conversion-summary)=

# Duality: conversion summary

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
