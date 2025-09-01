# Python basics

This is a very quick introduction to Python. It is not meant to be comprehensive, but rather a quick overview of the most important concepts that we will use when operating Pyomo or Calliope in other chapters. If you already have basic Python skills, you can skip this.

## Where and what to learn

For our purposes you can get away with using Python in a basic way, like a scientific calculator.

However, learning some basic Python, like minimal use of control statements (especially `for` loops) will make some steps quicker and easier to do.

There are many online resources to learn Python. Some examples are listed below - check out different options and see what works best for you.

* **LearnPython**. The website [LearnPython.org](https://www.learnpython.org/) provides a free, interactive introduction to Python.
* **QuantEcon: Python Programming for Economics and Finance**. The website [QuantEcon: Python Programming for Economics and Finance](https://python-programming.quantecon.org/intro.html) teaches you Python by giving you information, examples, and possibilities to try for yourself. In particular, their chapters "1. About Python" through "6. OOP I: Introduction to Object Oriented Programming" (leaving out chapter 7, which goes into more detail on object-oriented programming); then, all chapters from 8 onwards which give an overview of Python's most important scientific packages.
* **Software Carpentry**. The [Plotting and Programming in Python](https://swcarpentry.github.io/python-novice-gapminder/) lesson from Software Carpentry is a good hands-on tutorial.
* **YouTube videos**: On YouTube there are many videos that teach Python. Try this [playlist: "Python Programming Beginner Tutorials"](https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7).

## Jupyter notebooks

Some of the chapters in this reader are **Jupyter notebooks**. These are executable documents that combine elements of a written document with (Python) code and the results of that code (e.g. text or images).

If you are unfamiliar with Jupyter, I recommend watching this 25 minute YouTube video to get an overview of how these notebooks work: [Jupyter Notebook Complete Beginner Guide 2023 - From Jupyter to Jupyterlab, Google Colab and Kaggle!](https://www.youtube.com/watch?v=5pf0_bpNbkw).


## Common issues and points to remember

Python:

* Use `**` for exponent, not `^`: e.g. `2**2` for $2^2$.

* Careful: whitespace has meaning in Python - it is used to structure the code into separate logical blocks. For example, to delineate what code is inside an if-block (in this example y only becomes 2 if x > 1, whereas z = 3 is outside the if-block and always executed):
```
if x > 1:
    y = 2
z = 3
```

Jupyter notebooks:

* Jupyter notebooks consists of cells. Some cells contain text. Others contain code. Cells with code can be executed: while your cursor is inside the cell, press `Shift + Return`.

* Notebook cells in a notebook all run in the same Python interpreter. For example, assign 1 to a variable: `x = 1`. If you execute this in a notebook cell, all other notebook cells now have access to the variable `x`.

* Within the notebook environment, just executing a command will show you the results: writing `1 + 1` in a cell and executing that cell will print `2`. Writing `x` in a cell will print `1` (if the variable x was previously assigned as above).
