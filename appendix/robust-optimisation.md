(content:uncert-robust)=

# Robust optimisation

```{admonition} Robust optimisation
This section is based on {cite:p}`Bertsimas_Hertog_2022`.
```

Consider the optimisation problem

\begin{align}
    \begin{split}
        \min_{\mathbf{x}}&~f_0(\mathbf{x}, \mathbf{z}) \\
        \text{s.t.}&~f_1(\mathbf{x}, \mathbf{z}) \leq 0 \\
        &~~~~~\vdots \\
        &~f_m(\mathbf{x}, \mathbf{z}) \leq 0 \\
    \end{split}
\end{align}

with decision variables $\mathbf{x}$ and uncertain parameters $\mathbf{z}$. There are $m$ constraints.

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

In [standard form](content:lp:standard-form), we write this as:

\begin{align}
    \begin{split}
        \min_{\mathbf{x}}&~f(\mathbf{x}) \\
        \text{s.t.}&~g(\mathbf{x}, \mathbf{z}) \leq 0 \\
    \end{split}
\end{align}

Note that there is no uncertainty in the objective function $f(\mathbf{x})$ (it is not a function of $\mathbf{z}$) and there is a single constraint $g(\mathbf{x}, \mathbf{z}) \leq 0$.

Now we assume the uncertain parameters $\mathbf{z}$ are contained within some geometric "uncertainty set" $\mathcal{U}$. An example of an uncertainty set is shown in {numref}`fig:uncertainty_set`. The modeler can choose how large or small to make $\mathcal{U}$.

```{figure} ../images/uncertainty_set.png
:name: fig:uncertainty_set
:figwidth: 450px

Example geometric uncertainty set $\mathcal{U}$ for two uncertain parameters $z_1, z_2$ (adapted from {cite:p}`cheramin2021uncertaintyset`)
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

## Reformulation approach

The idea behind the **reformulation approach** is to solve the robust optimisation problem by creating a deterministic and finite equivalent, called a "robust counterpart". Depending on the shape of the uncertainty set, we can write a corresponding robust counterpart {cite:p}`Bertsimas_Hertog_2022`.

There are two important notes to make in the reformulation. The first is that $g(\mathbf{x}, \mathbf{z}) \leq 0, ~\forall \mathbf{z} \in \mathcal{U}$ is true if and only if $\max\limits_{\mathbf{z} \in \mathcal{U}}  g(\mathbf{x}, \mathbf{z}) \leq 0$. That is, if the constraint holds for the $\mathbf{z}$ that maximises $g$, then it holds for all other $\mathbf{z} \in \mathcal{U}$. Thus, we no longer have the issue of potentially an infinite number of constraints. Secondly, we can use duality to rewrite $\max\limits_{\mathbf{z} \in \mathcal{U}} \dots$ as $\min\limits_{\mathbf{y} \in \mathcal{Y}} \dots$. $\mathbf{y}$ are the dual variables. Now instead of a $\min\limits_{\mathbf{x}} \max\limits_{\mathbf{z}}$ problem, we have a $\min\limits_{\mathbf{x}} \min\limits_{\mathbf{y}}$ problem, which we can combine into a single $\min\limits_{\mathbf{x}, \mathbf{y}}$ problem.

## Adversarial approach

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

## Limitations of robust optimisation

Robust optimisation relies on the assumption that the uncertain parameters $\mathbf{z}$ are contained within some uncertainty set $\mathcal{U}$. However, it is not always clear how to choose an appropriate shape and size of $\mathcal{U}$. This affects our ability to solve a robust optimisation problem. Additionally, our ability to solve a robust optimisation problem depends on the function $g$ and the uncertainty set $\mathcal{U}$. If $g$ is non-concave in $\mathbf{z}$, then exact reformulations of the problem are known for only certain combinations of $g$ and $\mathcal{U}$. Lastly, when solving robust optimisation problems in practice, it may involve an unacceptably large increase in the number of variables and constraints, making the problem difficult to solve even though it is theoretically tractable.

## Distributionally robust optimisation

The idea behind **distributionally robust optimisation** is to combine stochastic programming and robust optimisation {cite:p}`Bertsimas_Hertog_2022` {cite:p}`delage2010distributionally`.

We have a stochastic programming problem with decision variables $\mathbf{x}$ and uncertain parameters $\mathbf{z}$:

\begin{align}
    \begin{split}
        \min_{\mathbf{x}}&~\mathbb{E}_{\mathbb{P}} \left[ f(\mathbf{x}, \tilde{\mathbf{z}}) \right] \\
        \text{s.t.}&~\mathbb{P} \left( g(\mathbf{x}, \tilde{\mathbf{z}}) \leq 0 \right) \geq 1-\epsilon \\
    \end{split}
\end{align}

$\mathbb{P}$ is the probability distribution of $\tilde{\mathbf{z}}$, which is often unknown. Thus, we can assume that $\mathbb{P}$ is contained within some "ambiguity set" $\mathcal{P}$. Think of $\mathcal{P}$ as a sort of equivalent to the uncertainty set $\mathcal{U}$ except for probability distributions.

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

## Software to solve robust optimisation problems

Software to solve robust optimisation problems is not as advanced as for other problem types. An example is [romodel](https://github.com/cog-imperial/romodel), which extends Pyomo's capabilities to describe robust optimisation and includes some algorithms to solve these problems.

## References

```{bibliography}
:filter: docname in docnames
```
