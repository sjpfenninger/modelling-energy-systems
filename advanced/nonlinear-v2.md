(content:nonlinear)=

# Non Linear Programming

In this chapter, we will extend the optimization problems to regions, where the objective function and/or at least one of the constraints are non-linear functions. First, we will analyze how the Classic Economic Dispatch problems turns from a linear to a non-linear optimization problem. Secondly, we will demonstrate how an non-linear program can be solved through the optimality conditions, when no constraints are present. Then we will extend this approach to some constrained non-linear problems. Finally, we will delve into some computational methods, such as the gradient descend, that can be utilized for more complex problems, where an analytical solution is not possible. 

## The Classic Economic Dispatch revisited
As indicated in Chapter **(reference to reader Chapter)** the Classic Economic Dispatch problem relates to how to optimally schedule production, to minimize system-wide operation cost. In other words, how to distribute power generation, to meet system demand, across a range of powerplants with different operating costs.

Up to now, we have only considered powerplants with a linear structure cost. This means that the $Marginal Cost = constant$. But in reality the assumption of a constant marginal cost, and therefore a linear total cost structure is not realistic. For a real powerplant the marginal cost is dependent on the amount of power produced, so $MC = f(P_{G_i})$. But what are the sources of non-linearity ? 

* **Efficiency curve:** A powerplant, whether it is a gas turbine for gas-fired plants or a steam turbine for coal and nuclear plants, does not have a constant efficiency across the span of its operational range. An example efficiency curve can be seen in figure {numref}`gas_turb_eff_curve`. Therefore, if the efficiency is a function of the power generated, the cost of fuel per unit of power produced is also affected. 

* **Operation & Maintenance:** The operational & maintenance expenses of a powerplant are also a function of the power produced, again introducing non-linearities to the system. For example, the tear of the components is a function of the loading of the powerplant.

Taking all the above into account it is evident that the Classic Economic Dispatch is transformed into a non-linear problem, where the cost curve of each generator is often described by a convex, quadratic function, of the form $C_i(P_{G_i}) =  α + βP_{G_i} + γP_{G_i}^2$. An example of the cost curve can be seen in figure {numref}`cost_curve`.

```{admonition} Definiton of Marginal Cost (MC)
Marginal Cost (MC) is defined as the measure of change in cost, caused by a unitary change in output. Mathematically it is inherently linked with the derivative : 

$$
MC = \frac{d C_i(P_{G_i})} {d P_{G_i}}
$$
```

```{figure} gas_turb_eff_curve.jpeg
:name: gas_turb_eff_curve

An example curve of efficiency plotted against the load on a aeroderivative gas turbine, taken from <https://www.wartsila.com/energy/learn-more/technology-comparison-engines-vs-aeros/part-load-efficiency>.
```

```{figure} cost_curve.jpg
:name: cost_curve
An example of the convex, quadratic cost function of a generator, as a function of the power generated. 
```
All in all, Classic Economic Dispatch seen in Chapter **ref chapter** is now transformed to the following non-linear form. Specifically, if the cost function is quadratic $C_i(P_{G_i}) =  α + βP_{G_i} + γP_{G_i}^2$, the problem falls under the category of Quadratic Programming, a special case of Non-Linear Programming, . 

```{math}
:label: CED_nlp
\begin{align}
& \min C(P_G) = \sum_{i=1}^{n} C_i(P_{G_i}) \\
& \text{subject to} \\
& \sum_{i=1}^{n} P_{G_i} = P^\text{total}_D \\
& P^\text{min}_{G_i} \leq P_{G_i} \leq P^\text{max}_{G_i}
\end{align}
```
## Solving an NLP without constraints
In its more general form an NLP is described as : 

```{math}
\begin{align}
& \min \{ f(x) : \text{s.t. } \quad g_i(x) \geq 0, \quad i \in I, \quad h_j(x) = 0, \quad j \in E, \quad x \in \mathbb{R}^n \} \\
& \text{where:} \\
& f \in C^2(\mathbb{R}^n \to \mathbb{R}) \quad \text{(smooth (non)linear function)} \\
& g_i \in C^2(\mathbb{R}^n \to \mathbb{R}) \quad \text{(smooth (non)linear inequality constraints)} \\
& h_j \in C^2(\mathbb{R}^n \to \mathbb{R}) \quad \text{(smooth (non)linear equality constraints)}
\end{align}
```
```{warning}
The notation $f \in C^2(\mathbb{R}^n \to \mathbb{R})$ means that the function f is twice and continously differentiable, so the first and second derivatives exist $ x \in R^n $.
```
But how can we solve the Non-Linear Optimization problem in case of convex functions ? Let's start by building some mathematical background. Assuming that function $f$ is twice differentiable and that $x^*$ is the presumed extremum, either minimum or maximum, the Taylor expansion of the function around $x^*$  ignoring third order terms and higher is presented in equation {eq}`Taylor`. To generalize the case for a multivariable optimization problem, the vector x is defined as $(x_1, x_2, \dots, x_n)^T$. 


```{math}
:label: Taylor
\begin{equation}
f(x) = f(x^*) + \nabla^T f(x^*)(x-x^*) + \frac{1}{2} (x-x^*)^T \nabla^2 f(x^*) (x-x^*) + O_3(x-x^*) 
\end{equation}
```
Defining the Hessian matrix $H$ of the function $f$ with respect to the vector $x$ as :

```{math}
:label: Hessian

H(\mathbf{x}) = 
\begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \dots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \dots & \frac{\partial^2 f}{\partial x_2 \partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \dots & \frac{\partial^2 f}{\partial x_n^2}
\end{bmatrix}

```
Finally, the gradient of $f$ is defined as : 
```{math}
:label: gradient
\begin{equation}
\nabla f(\mathbf{x}) = \left( \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \dots, \frac{\partial f}{\partial x_n} \right)
\end{equation}
```
Considering the definitions of {eq}`Hessian` and {eq}`gradient`, equation {eq}`Taylor` can be re-written as : 

```{math}
:label: Taylor_Hessian
\begin{equation}
f(x) = f(x^*) + \nabla^T f(x^*)(x-x^*) + \frac{1}{2}(x-x*)^TH(x)(x-x^*)
\end{equation}
```
From single dimensional calculus we know that for $x^*$ to be a stationary point, $f'(x^*) =0 $ must hold true. For a multivariable function such as the one used in our general NLP the condition to check whether $x^*$ is a **stationary point** is can be seen in {eq}`stationary point`. The difference between the three types of stationary points can be visualized in {numref}`Stationary point` 

```{math}
:label: stationary point 
\begin{equation}
\nabla f(\mathbf{x}) = \left( \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \dots, \frac{\partial f}{\partial x_n} \right) = 0 
\end{equation}
```
```{figure} 14.7.3.png
:name: Stationary point

An example of the three different types of stationary points, (a) are local minima, (b) are local maxima and (c) is a saddle point. Taken from <https://math.libretexts.org/Bookshelves/Calculus/Map%3A_University_Calculus_%28Hass_et_al%29/13%3A_Partial_Derivatives/13.7%3A_Extreme_Values_and_Saddle_Points> 
```

The condition described in {eq}`stationary point` is a necessary condition for $x^*$ to be an extremum. Let us now derive the **sufficient** condition so that $x^*$ is a minimum, either local or global. By plugging the necessary condition {eq}`stationary point` in {eq}`Taylor_Hessian` we get :

```{math}
:label: Taylor_Hessian_sufficient
\begin{equation}
f(x) = f(x^*) + \frac{1}{2}(x-x*)^TH(x)(x-x^*)
\end{equation}
```
For $x^*$ to be a **local minimum** of $f$, $ f(x) \geq f(x*) \quad \forall x \in \mathbb{R}^n \ \text{with} \ \|x - x^*\| < \epsilon $, where $\epsilon$ is an arbitrary tolerance value defined. If  $ f(x) > f(x*) \quad \forall x \neq x^* $, then $x^*$ is a **global minimum** point. Therefore for $f(x) \geq f(x^*)$ to hold true based on {eq}`Taylor_Hessian_sufficient`, the sufficient condition for optimality is :

$$
(x-x*)^TH(x*)(x-x*) \geq 0 
$$

In other words, the term $(x-x*)^TH(x)(x-x*)$ establishes the character of the stationary point, whether it is a minimum, maximum or saddle point. In practice, to determine the character of the stationary point $x*$ we need to check if the Hessian matrix $H(x*)$ is positive-definite, positive-semidefinite, negative-definite, negative-semidefinite, or indefinite, through the **eigenvalues of the matrix**. To calculate the eigenvalues of the matrix we have to solve the equation $det(H(x) - λ\mathbb{I}) = 0$. All in all, depending on the shape of the objective function $f$ and the eigenvalues of the Hessian matrix we can characterize it according to the following table : 

| f(x) is          | H(f(x*)) is        | Eigenvalues λ of H(f(x*)) are | Stationary point is              |
|----------------------|------------------------|--------------------------------------|----------------------------------|
| Strictly convex       | positive-definite       | all \(>0\)                           | minimum                          |
| Convex                | positive-semidefinite   | all \(\geq 0\)                       | minimum (may be more than one)   |
| Concave               | negative-semidefinite   | all \(\leq 0\)                       | maximum (may be more than one)   |
| Strictly concave      | negative-definite       | all \(<0\)                           | maximum (may be more than one)   |
|                       | indefinite              | some positive, some negative         | saddle point                     |

To sum up the process of identifying whether a stationary point corresponds to a maximum, minimum or a saddle point, the following algorithm has to be followed :

1.  Evaluate the gradient $\nabla f$ to identify the stationary points $x*$ of the objective function. 
2. Calculate the Hessian matrix $H(f(x))$. 
3. Calculate the eigenvalues of the Hessian matrix.
4. Evaluate each stationary point, based on the eigenvalues of the Hessian and the table above. 

Finally, an example where we can practice the above mentioned process to identify whether a function has a maximum or a minimum. Assume that we want to check whether the function $f(x_1, x_2) = 2x_1^2 - 3x_1x_2 + 2x_2^2$. As seen in figure {numref}`function_surface`, the function is convex. First, we will calculate the gradient and identify the stationary points, i.e the points where $\nabla f = 0$ :

$$
\nabla f(x) = [4x_1 - 3x_2, -3x_1 + 4x_2] = 0
$$

$$
\rightarrow (x_1, x_2) = (0,0)
$$

The Hessian matrix of $f$ is :

$$
H(x) = \begin{bmatrix} 
4 & -3 \\ 
-3 & 4 
\end{bmatrix}
$$

Then the eigenvalues are calculated as : 

$$
det(H(x)-λ\mathbb{I}) = \begin{bmatrix} 
4-λ & -3 \\
-3 & 4-λ 
\end{bmatrix}
$$

$$
(4-λ)^2 - (-3)^2 = 0 \rightarrow (λ_1, λ_2) = (1, 7)
$$

Since both eigenvalues are positive and the function $f$ is a convex, then according to the table the point $(x_1, x_2) = (0, 0)$ is a minimum. 

```{figure} function_surface.jpg
:name: function_surface

Surface plot of $f(x_1, x_2) = 2x_1^2 - 3x_1x_2 + 2x_2^2$
```
To conclude, in this chapter we have seen how we can identify possible extremum points in **non-linear functions** **without constraints** through the calculation of the gradient, the Hessian matrix and finally the eigenvalues of the Hessian. According to the sign of the eigenvalues we identified whether a corresponding stationary point is an extremum or a saddle point. In that way, we can approach unconstrained Non-Linear Programs of convex functions.

## Solving an NLP with constraints
Looking back to the problem where we started, the Classical Economic Dispatch with non-linear cost functions {eq}`CED_nlp`, we see that this is an NLP **with constraints**. Therefore, the methodology described in the previous chapter cannot be directly applied to it. In this chapter, we will present a methodology to solve NLP problems, while respecting the stated constraints. 

### NLP with one equality constraint
The first case we will examine is a Non-Linear program, with one equality constraint that is non-linear. In its general form, with a decision variable vector $(x_1, x_2, \dots, x_n)^T $ the problem can be stated as :

$$
\min f(x) \\
\text {s.t} h(x) = 0 \\
$$

We start by introducing a new function, the **Lagrangian** defined as : 

```{math}
:label: Lagrangian
\begin{align}
&L(x, λ) = f(x) + λh(x) \\
&\text{where} \quad λ \quad \text{is the Lagrangian multiplier} \\
\end{align}
```
To find the minimum $x^*$ the gradient of the Lagrangian has to be $\nabla L(x^*, λ^*) = 0 $ in other words, the **necessary conditions** at the minimum are :

```{math}
:label: Necessary cond Langrange
\begin{align}
&\frac{\partial L(x, λ)}{\partial x} \bigg|_{x = x^*} = 0 \\
&\frac{\partial L(x, λ)}{\partial λ} \bigg|_{λ = λ^*} = 0 \\
&h(x*) = 0 \\
\end{align}
```
The above can be generalized for a cases with $n$ equality constraints, but in that case the Lagrange multiplier $λ$ will not be a single variable, rather a vector $λ =(λ_1, λ_2, \dots, λ_n)^T $.

Assume that we want to apply the Lagrangian to the following problem, which has a linear objective function, but a quadratic constraint : 

```{math}
\begin{align}
\min f(x_1, x_2) = x_1 + x_2 \\
\text{s.t} \quad h(x) = x_1^2 + x_2^2 - 1 = 0 
\end{align}
```
First, we derive the Lagrangian function : 
```{math}
:label: Lagrange example
\begin{equation}
L(x, λ) = f(x) + λh(x) = x_1 + x_2 + λ(x_1^2 + x_2^2 - 1)
\end{equation}
```
Secondly, we calculate the partial derivates of the Lagrangian from {eq}`Lagrange example` :

```{math}
:label: Pd Lagrange
\begin{align}
\frac{\partial L(x, λ)}{\partial x_1} = 0 \Rightarrow 1+2λx_1 = 0 \\
\frac{\partial L(x, λ)}{\partial x_2} = 0 \Rightarrow 1+2λx_2 = 0 \\
\frac{\partial L(x, λ)}{\partial λ} = 0 \Rightarrow x_1^2 + x_2^2 -1 = 0 \\
\end{align}
```
The above is a 3x3 system of equations which can be trivially solved, arriving to a solution of $x_1^*, x_2^* = \pm (1/\sqrt2)$, with the plus sign corresponding to the maximum and the negative to the minimum. 

Except from aiding to the search of an extremum, the Lagrangian multipliers utilized have another crucial role. They proved provide useful information of the right-hand side change of the active constraint. Specifically, the optimal value of  Lagrange multiplier $λ^*$ is the change in optimal value of the objective function due to the relaxation of an active constraint. 

Now let us revisit the initial Classic Economic Dispatch problem {eq}`CED_nlp` and solve it, while respecting the equality condition, which maintains the system balance. The Lagrangian of the problem reads : 

```{math}
:label: Lagrange NLP equality 
\begin{equation}
L(P_{G_i}, λ) = \sum_{i=1}^{n} C_i(P_{G_i}) - λ \cdot (\sum_{i=1}^{n}(P_{G_i})- P_D)
\end{equation}
```
Then considering the optimality conditions defined in {eq}`Necessary cond Langrange` we obtain : 

```{math}
:label: Optimality conditions CED
\begin{align}
& \frac{\partial L}{\partial P_{G_i}} = MC(P_{G_i}) - λ = 0 \\
& \text{where :} \quad MC(P_{G_i}) \quad \text{is the Marginal Cost of unit i} \\
& \frac{\partial L}{\partial λ} = \sum_{i=1}^{n}(P_{G_i}) + P_D = 0
\end{align}
```
From equation {eq}`Optimality conditions CED` and the necessary optimality conditions we have a key takeaways; For the system to operate at its minimal cost, **all  generators must operate at the same Marginal Cost** $λ = MC(P_{G_i})$. In that case, the Lagrange multiplier is also the **market clearing price** and presents the system wide marginal cost. This means that if the active constraint changes by +1 unit of power, the system-wide price will change by +λ. 


```{warning} Marginal Cost (MC) and Incremental Cost are the same. 
```

### Economic Dispatch with demand utility function
A consideration while clearing the market is not only to minimize the system cost, but to maximize the social welfare, i.e the utility that both consumers and producers get from the market. Therefore, we will introduce the **utility function** of a consumer, which represents the satisfaction experienced by the consumer of a good. Fundamentally, as the rate of commodity acquisition increases, the marginal utility decreases. In broader terms, it means that the more someone consumes the less extra utility one gets, by an extra unit of consumption. Therefore, the marginal utility function of a consumer $P_{D_j}$ has a negative slope and has often the form $MU(P_{D_j}) = a -bP_{D_j}$. Therefore, consumers will tend to consume up to the point where the marginal utility is equal to the marginal cost. Intuitively this makes sense, since after that point the satisfaction or utility gained is lower than the extra cost of purchasing the commodity. This  is known as the **marginal decision rule** and is extremely useful for identifying equilibria between production and consumption. To bridge with Chapter **MCP** the utility function of the consumers is essentially the inverse demand function, described in the previous Chapter of the reader. In this case, we have developed the tools to use a non-linear utility function as : 

$$
U_j(P_{D_j})  =(α - βP_{D_j})P_{D_j} = αP_{D_j} - βP_{D_j}^2 \quad α,β > 0 : constant 
$$

or

$$
U_j(P_{D_j})  =(α + βP_{D_j})P_{D_j} = αP_{D_j} + βP_{D_j}^2 \quad α>0 \quad β<0 : constant 
$$

The marginal utility is $MU(P_{D_j}) = α-2βP_{D_j}$ or $ MU(P_{D_j}) = α+2βP_{D_j}$ respectively. 

Considering the definition of the utility functions and the general consideration that market shall maximize the social welfare, we can define a new market-clearing problem with elastic demand, in the context on Non-Linear utility functions. The objective function and constraints can be seen below : 

```{math}
:label: SW maximization 
\begin{align}
& \max SW(P_G, P_D) = \sum_{j=1}^{m} U_j(P_{D_j}) - \sum_{i=1}^{n} U_i(P_{G_i}) \\ 
& \text{subject to} \quad \sum_{j=1}^{m}P_{D_j} = \sum_{i=1}^{n}P_{G_i} \\
\end{align}
```
Despite the different formulation, the NLP presented in {eq}`SW maximization` has still only one active constraint and n+m decision variables, therefore it can be solved through the application of the Lagrangian function in the following manner : 

```{math}
:label: SW Lagrangian
\begin{align}
& L(P_{G_i},P_{D_j}, λ) = \sum_{j=1}^{m} U_j(P_{D_j}) - \sum_{i=1}^{n} U_i(P_{G_i}) - λ(\sum_{j=1}^{m}P_{D_j} - \sum_{i=1}^{n}P_{G_i}) \\ 
& \frac{\partial L}{\partial P_{D_j}} = MU_j(P_{D_j}) - λ = 0 \quad \text{for} j =  1, 2, \dots, m \\
& \frac{\partial L}{\partial P_{G_i}} = MC_i(P_{G_i}) + λ = 0\quad \text{for} i =  1, 2, \dots, n \\
& \frac{\partial L}{\partial λ} = sum_{j=1}^{m}P_{D_j} - \sum_{i=1}^{n}P_{G_i} = 0 \\
\end{align}
```
After deriving the optimality conditions through the Lagrangian we arrive at a system of m+n linear equations with m+n unknows, which can trivially be solved. By closer examination of the optimality conditions, we see that **all generating units** must operate at **identical marginal cost** and **all demand agents** at   **identical marginal utility**. As both are equal to the Lagrangian multiplier it means that the system marginal cost equals the system marginal utility , satisfying the **marginal decision rule**. 

### NLP with inequality constraints
In case that the Economic Dispatch problem involves inequality constraints, such as minimum and maximum generation limits, the Lagrangian cannot help us identify the extreme points. In that case, the first-order necessary conditions are the Karush Kuhn Tacker (KKT) conditions discussed in Chapter **ref Chapter**.  For a general problem with only inequality constraints, n decision variables and m inequality constraints, in the form of :

$$
\min f(x) \\
\text{s.t} \quad g_j(x) \leq 0 \quad \forall j \in J
$$

The Karush Kuhn Tacker conditions read: 

```{math}
:label: KKT NLP
\begin{align}
& \nabla f + \sum_{j=1}^{m} μ_j\nabla g_j(x) = 0 \tag{Optimality} \\
& g_j(x) \leq 0 \quad \text{for} \quad j = 1, 2, \dots, m  \tag{Feasibility} \\
& μ_j g_j(x) = 0 \quad \text{for} \quad j = 1, 2, \dots, m  \tag{Complementary slackness} \\
& μ_j \geq 0 \quad \text{for} \quad j = 1, 2, \dots, m  \tag{Non-negativity} \\
\end{align}
```
```{warning}
$μ_j$ are called the KKT multipliers and are analogous to the Lagrangian multipliers. 
```
Through solving the set of equations, it may be possible to arrive to an optimal solution for a Non Linear Program which includes inequality constraints. 

## Algorithms for solving NLPs
In case of NLPs with multiple decision variables and inequality constraint, the analytical solution of the problem through the application of the Karush Kuhn Tacker problem can be tedious or even not possible. Therefore, a set of numerical tools has been developed to solve NLPs. In the context of this course, we will focus on one of the most commonly used and powerful tools, the gradient descend method.  

Overall, the algorithms used for numerical optimization can be divided in the three following categories, based on the order of the method. 
1. **Zero-order methods**, which only use function values. They are most popular when the gradient and Hessian are difficult to get. For example in cases where the objective function is not explicitly defined. An example of this method is the Nelder-Mead or downhill simplex method.  
2. **First-order methods**, which use the first derivative of the function. Such a method is the steepest or gradient descent. These methods are very popular nowadays as they are well suited for large datasets and machine learning. 
3. **Second-order methods**, which utilize the second-derivative of the objective function. Such methodologies are used in cases where high accuracy is needed. A popular example of a second order numerical method is the Newton, which can be utilized to approximate functions and locate the root of the function derivative, as used in the optimality conditions. 

### Gradient descent method 
In the context of this reader, the method of focus will be the gradient descent, due to its large application range. In broad terms, applying the gradient descent is like a blindfolded man trying to descent a hill, while taking the least steps as possible. As one goes down the hill, he would first choose to make big strides in the direction where the slope is the steepest. While he approaches the valley and the lowest point, the steps will get smaller and smaller, in order to avoid overshooting the target (minimum). This is roughly the working of the gradient or steepest descent. 

In mathematical terms, the algorithm of the gradient descent can be applied to an unconstrainted minimization problem :

$$
\min f(x) \quad x \in \mathbb{R^n}
$$

If we don't have any further information, we seek a stationary point of $f$ where $\nabla f(x^*) = 0$. If we start our method at an arbitrary point $x^k$, we define the search direction vector as $d^k = - \nabla f(x^k)$. Then the next iteration point for the gradient descent search is :

$$
x^{k+1} = x^k -a^k\nabla f(x^k) = x^k -a^kd^k
$$

Where $a^k$ is the step size of the iterative process. The step size shall be chosen appropriately, as a too large step might lead to overshooting the minimum value and a too small might lead to very small convergence of the method. Additionally, the step size can be kept fixed during the iteration processes, or can be adjusted throughout. A logical strategy to optimize the convergence is too decrease the step size, as we move towards the minimum. In general, the gradient descent has the property of global convergence, so it will converge regardless of the initial conditions and with a rate of $O(1/k)$. The gradient descent algorithm will be terminated when the computed gradient at a point $x^k$, $\nabla f(x(k))$ is smaller than a defined tolerance value $ε$ or $\left\|\nabla f(x(k))\right\| \leq \epsilon$. 

One of the main issues of the gradient descent is that for non convex functions where possibly multiple minima and maxima exist, the gradient descent algorithm can be trapped in a local extremum point, as seen in figure {numref}`gradient_descent`. This "trapping" can be caused by the initial conditions or the learning rate used. To counter this, a good strategy is to choose different initializations and step size (learning rate) of the algorithm to see, what extrema it calculates once terminating. 

```{figure} gradient_descent.png
:name: gradient_descent

Gradient descent algorithm with multiple min/max points 
 ```