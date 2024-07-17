import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from modelling_energy_systems import util
from modelling_energy_systems.util import SAVETO_KWARGS

sns.set_context("talk")


def build_figures():
    fig_dispatchlp_decisionspace("images-built/fig_dispatchlp_decisionspace.jpg")
    fig_dispatchlp_decisionspace_operationalconstraints(
        "images-built/fig_dispatchlp_decisionspace_operationalconstraints.jpg"
    )
    fig_dispatchlp_decisionspace_allconstraints(
        "images-built/fig_dispatchlp_decisionspace_allconstraints.jpg"
    )
    fig_dispatchlp_optimalsolution("images-built/fig_dispatchlp_optimalsolution.jpg")
    fig_dispatchlp_contourlines("images-built/fig_dispatchlp_contourlines.jpg")
    fig_dispatchlp_contourlines_parallel(
        "images-built/fig_dispatchlp_contourlines_parallel.jpg"
    )
    fig_dispatchlp_activeconstraints(
        "images-built/fig_dispatchlp_activeconstraints.jpg"
    )


def setup_fig_dispatchlp_decisionspace(min_coord, max_coord):
    MIN_COORD = min_coord
    MAX_COORD = max_coord

    fig, ax = plt.subplots(figsize=(8, 8))

    ax.set_xlim(MIN_COORD, MAX_COORD)
    ax.set_ylim(MIN_COORD, MAX_COORD)
    ax.set_xlabel("$\\mathbf{P_1}$: Power from coal power plant [MW]")
    ax.set_ylabel("$\\mathbf{P_2}$: Power from gas power plant [MW]")
    ax.grid(True)
    return fig, ax


def fig_dispatchlp_decisionspace(save_to=None):
    MIN_COORD = 0
    MAX_COORD = 500
    fig, ax = setup_fig_dispatchlp_decisionspace(MIN_COORD, MAX_COORD)

    x = np.linspace(MIN_COORD, MAX_COORD, 100)
    plt.fill_between(
        x,
        MIN_COORD * np.ones_like(x),
        MAX_COORD * np.ones_like(x),
        color="gray",
        alpha=0.5,
    )
    plt.text(
        (MAX_COORD - MIN_COORD) / 2,
        (MAX_COORD - MIN_COORD) / 2,
        "Decision Space",
        ha="center",
        va="center",
    )
    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax


def fig_dispatchlp_decisionspace_operationalconstraints(save_to=None):
    MIN_COORD = 0
    MAX_COORD = 500
    fig, ax = setup_fig_dispatchlp_decisionspace(MIN_COORD, MAX_COORD)

    x = np.linspace(MIN_COORD, MAX_COORD, 100)
    x_min = 50
    x_max = 300
    y_min = 100
    y_max = 400

    util.plot_x_range(x_min, x_max, ax, color="r")
    util.plot_y_range(y_min, y_max, ax, color="g")

    plt.fill_between(
        x,
        y_min * np.ones_like(x),
        y_max * np.ones_like(x),
        where=(x >= x_min) & (x <= x_max),
        color="gray",
        alpha=0.5,
    )
    plt.text(
        (x_min + x_max) / 2,
        (y_min + y_max) / 2,
        "Decision \nSpace",
        ha="center",
        va="center",
    )
    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax


def fig_dispatchlp_decisionspace_allconstraints(save_to=None):
    MIN_COORD = 0
    MAX_COORD = 500
    fig, ax = setup_fig_dispatchlp_decisionspace(MIN_COORD, MAX_COORD)

    x = np.linspace(MIN_COORD, MAX_COORD, 100)
    x_min = 50
    x_max = 300
    y_min = 100
    y_max = 400

    # Demand constraint
    def demand(x):
        return 500 - x

    # Feasible Region
    util.plot_x_range(x_min, x_max, ax, color="r")
    util.plot_y_range(y_min, y_max, ax, color="g")
    util.plot_function(x, demand, ax, color="b")

    # Line Segment
    x_p1, y_p1 = util.find_intersection((0, 400), (-1, 500))
    x_p2, y_p2 = util.find_intersection((float("inf"), 300), (-1, 500))
    p1 = (x_p1, y_p1)
    p2 = (x_p2, y_p2)
    util.draw_line_segment(p1, p2, ax, color="grey")

    # Feasible Solution
    ax.plot(250, 250, "o", color="k", markersize=10)
    plt.annotate(
        "One possible\nfeasible\nsolution",
        xy=(250, 250),
        xytext=(350, 310),
        ha="left",
        va="bottom",
        xycoords="data",
        arrowprops=dict(
            facecolor="black",
            linewidth=0.5,
            headwidth=10,
            headlength=10,
            mutation_scale=10,
            shrink=0.1,
        ),
    )

    # Decision space label
    plt.text(
        (x_min + x_max) / 2,
        (y_min + y_max) / 2,
        "Decision \nSpace",
        ha="center",
        va="center",
        color="grey",
    )

    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax


def fig_dispatchlp_optimalsolution(save_to=None):
    pass


def fig_dispatchlp_contourlines(save_to=None):
    pass


def fig_dispatchlp_contourlines_parallel(save_to=None):
    pass


def fig_dispatchlp_activeconstraints(save_to=None):
    pass
