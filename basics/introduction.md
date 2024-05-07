# Introduction

In this course, we'll progressively explore how modelling techniques, particularly optimisation methods, can effectively address decision-making challenges in energy and power systems. These techniques have broad applications across various sectors, including industry and supply chain management.

Alongside the modelling methods, we will explore issues relevant to both current and future power system operations and design. Topics range from economic dispatch and unit commitment to making planning and operational decisions in electricity and heat systems, as well as optimal charging strategies for electric vehicles.

Our departure point and initial emphasis will be on linear optimisation methods - the first two rows in {numref}`table-optimisation-problem-types` below. While recognizing that real-world scenarios often involve non-linearities, linear optimisation offers the advantage of speed and efficiency in solving problems. This makes it a practical choice for constructing large-scale models.

(table-optimisation-problem-types)=
:::{table} Types of optimisation problems
:widths: auto
:align: center
| Objective function | Constraints |Binary variables? | Type of problem |
| ------------------ | ----------- | ---------------- | --------------- |
| Linear             | Linear      |     No           | LP (Linear Programming) |
| Linear             | Linear      |     Yes          | MILP (Mixed Integer Linear Programming) |
| Non-linear         | Linear      |     No           | NLP (Non-Linear Programming) |
| Non-linear         | Linear      |     Yes          | MINLP (Mixed Integer Non-Linear Programming) |
| Non-linear         | Non-linear  |     No           | NLPN (Non-Linear Programming with Non-linear constraints) |
| Non-linear         | Non-linear  |     Yes          | MINLPN (Mixed Integer Non-Linear Programming with Non-linear constraints) |
:::
