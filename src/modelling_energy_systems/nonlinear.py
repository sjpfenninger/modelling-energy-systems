import numpy as np
from matplotlib import pyplot as plt

from modelling_energy_systems.util import SAVETO_KWARGS

def build_figures():
    fig_countour_plots("images-built/fig_contour_plots.jpg")


def fig_countour_plots():
    fig, ax = plt.subplots(figsize=(8, 4))


    ax.grid(True)
    return fig, ax


def fig_countour_plots(save_to):
    # Create a grid of points
    x = np.linspace(-1, 1, 400)
    y = np.linspace(-1, 1, 400)
    X, Y = np.meshgrid(x, y)

    # 1. Quadratic function with a saddle point at (0,0), f(x, y) = x^2 - y^2 (example of saddle function)
    Z1 = X*Y + 2.2

    # 2. Parabolic function: f(x, y) = (x+1)^2 + (y-1)^2 (translated parabola)
    Z2 = (X - 1)**2 + (Y + 1)**2

    # 3. Linear function: f(x, y) = 2x + y
    Z3 = 2 * X + Y

    # 4. Parabolic function: f(x, y) = x^2 + y^2 (circle-like shape)
    Z4 = X**2 + Y**2

    # Create 2x2 subplot
    fig, axes = plt.subplots(2, 2, figsize=(10, 8), sharex=True, sharey=True, constrained_layout=True, subplot_kw = {'aspect':1})

    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    # Plot each function in a subplot
    ax = axes[0, 0]
    contour1 = ax.contourf(X, Y, Z1, cmap='coolwarm')
    fig.colorbar(contour1, ax=ax)

    ax = axes[0, 1]
    contour2 = ax.contourf(X, Y, Z2, cmap='coolwarm')
    fig.colorbar(contour2, ax=ax)

    ax = axes[1, 0]
    contour3 = ax.contourf(X, Y, Z3, cmap='coolwarm')
    fig.colorbar(contour3, ax=ax)

    ax = axes[1, 1]
    contour4 = ax.contourf(X, Y, Z4, cmap='coolwarm')
    fig.colorbar(contour4, ax=ax)

    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax
