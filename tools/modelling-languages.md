# Modelling languages and frameworks

## Mathematical modelling languages

To make our life easier when working with mathematical models on a computer, we use mathematical modelling languages (also called algebraic modelling languages). Such languages allow us to write our problems in mathematical form.

Some well-known commercial languages are [AMPL](https://en.wikipedia.org/wiki/AMPL) and [GAMS](https://en.wikipedia.org/wiki/General_algebraic_modeling_system). They were designed from the ground up around mathematical problems,  which differentiates them from general-purpose programming languages. This kind of modelling language sits in between the mathematical problem as we would write it down by hand and the numerical algorithms that solve the problem ({numref}`fig-modelling-languages`).

```{figure} ../images/modelling-languages.png
:name: fig-modelling-languages
:figwidth: 400px

Modelling languages.
```

We are interested in open-source mathematical languages built inside existing general-purpose programming languages such as Python, which allow us to combine the benefits of a mathematical modelling language with the power of having access to everything else the programming language provides. Prominent examples include:

* [YALMIP](https://yalmip.github.io/) (in Matlab)
* [JuMP](https://jump.dev/) (in Julia)
* [Pyomo](https://pyomo.readthedocs.io/) (in Python)

In this reader, we will focus on Pyomo and Python. The next section, {ref}`content:pyomo-basics`, introduces the functionality of Pyomo. To install Python and Pyomo, see the [installation instructions in the appendix](../appendix/installing-python.md). For some pointers on learning the basics of Python, see the [Python basics section](../appendix/python-basics.md) in the appendix.

## Model frameworks

When you often deal with similar problem structures, it makes sense to introduce another layer of abstraction: a model framework ({numref}`fig-frameworks`). In the energy sector, for example, a mathematical model will typically deal with the supply of electricity by different power plants and the demand for electricity by different customers. So rather than writing the equations that deal with this - for example the  supply and demand balance - from scratch, we use a domain-specific tool that does this for us: a model framework that provides building blocks such as "power plants" and builds a mathematical problem based on how we as users configure these building blocks.

```{figure} ../images/frameworks.png
:name: fig-frameworks
:figwidth: 400px

Domain-specific modelling software: model frameworks.
```

In this reader we will use the [Calliope framework](https://www.callio.pe/) to build larger and more complex problems. Underneath, the same or at least similar mathematical constraints are used as those we built by hand in the early sections of this reader. However, you can use Calliope without writing any maths and without knowing any Python. This makes it suitable for experimentation and prototyping, as well as for building large and complex models.

<!-- FIXME: add refs to later sections --->
