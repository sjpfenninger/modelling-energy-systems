import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from modelling_energy_systems import util
from modelling_energy_systems.util import SAVETO_KWARGS

from modelling_energy_systems.dispatch_lp import setup_fig_dispatchlp_decisionspace

sns.set_context("talk")


def build_figures():
    fig_sensitivitylp_changed_plantconstraint(
        "images-built/fig_sensitivitylp_changed_plantconstraint.jpg"
    )
    fig_sensitivitylp_changed_demandconstraint(
        "images-built/fig_sensitivitylp_changed_demandconstraint.jpg"
    )
    fig_sensitivitylp_changed_demandconstraint_infeasible(
        "images-built/fig_sensitivitylp_changed_demandconstraint_infeasible.jpg"
    )
    fig_sensitivitylp_shadowprice("images-built/fig_sensitivitylp_shadowprice.jpg")


def fig_sensitivitylp_changed_plantconstraint(save_to=None):
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

    p1 = util.find_intersection((0, 400), (-1, 500))

    # Old Feasible Region
    ax.axvline(x_min, color="r")
    ax.axvline(x_max, linestyle="--", dashes=[6, 7], color="r")
    util.plot_y_range(y_min, y_max, ax, color="g")
    util.plot_function(x, demand, ax, color="b")

    # Corner Point 1
    plt.annotate(
        r"$J = 1900$",
        p1,
        xytext=(30, 20),
        textcoords="offset points",
        fontsize=16,
        ha="center",
        va="center",
    )

    # New Upper Limit
    x_max_new = 200
    ax.axvline(x_max_new, color="r")

    # Line Segment
    x_p1, y_p1 = util.find_intersection((0, 400), (-1, 500))
    x_p2, y_p2 = util.find_intersection((float("inf"), x_max_new), (-1, 500))
    p1 = (x_p1, y_p1)
    p2 = (x_p2, y_p2)
    util.draw_line_segment(p1, p2, ax, color="grey")

    # Corner Point 2
    plt.annotate(
        r"$J = 3(200)+4(300) = 1800$",
        p2,
        xytext=(100, 30),
        textcoords="offset points",
        fontsize=16,
        ha="center",
        va="center",
        color="orange",
        bbox=dict(facecolor="white", edgecolor="black", boxstyle="round"),
    )
    ax.plot(p2[0], p2[1], "o", color="orange", markersize=10)

    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax


def fig_sensitivitylp_changed_demandconstraint(save_to=None):
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

    p1 = util.find_intersection((0, 400), (-1, 500))

    def new_demand(x):
        return 600 - x

    # Old Feasible Region
    util.plot_x_range(x_min, x_max, axis=None, color="r")
    util.plot_y_range(y_min, y_max, axis=None, color="g")
    util.plot_function(x, demand, ax, linestyle="--", dashes=[6, 7], color="b")

    # New Demand
    util.plot_function(x, new_demand, ax, color="b")

    # Line Segment
    x_p1, y_p1 = util.find_intersection((0, 400), (-1, 600))
    x_p2, y_p2 = util.find_intersection((float("inf"), 300), (-1, 600))
    p1 = (x_p1, y_p1)
    p2 = (x_p2, y_p2)
    util.draw_line_segment(p1, p2, ax, color="grey")

    # Optimum
    plt.annotate(
        r"$J = 3(300)+4(300) = 2100$",
        p2,
        xytext=(60, -30),
        textcoords="offset points",
        fontsize=16,
        ha="center",
        va="center",
        color="orange",
        bbox=dict(facecolor="white", edgecolor="black", boxstyle="round"),
    )
    ax.plot(p2[0], p2[1], "o", color="orange", markersize=10)

    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax


def fig_sensitivitylp_changed_demandconstraint_infeasible(save_to=None):
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

    def new_demand(x):
        return 800 - x

    # Old Feasible Region
    util.plot_x_range(x_min, x_max, axis=None, color="r")
    util.plot_y_range(y_min, y_max, axis=None, color="g")
    util.plot_function(x, demand, ax, linestyle="--", dashes=[6, 7], color="b")
    plt.fill_between(
        x,
        y_min * np.ones_like(x),
        y_max * np.ones_like(x),
        where=(x >= x_min) & (x <= x_max),
        color="red",
        alpha=0.5,
    )

    # New Demand
    util.plot_function(x, new_demand, ax, color="b")

    # Statement
    plt.text(
        (x_min + x_max) / 2,
        (y_min + y_max) / 2,
        "Decision \nSpace",
        ha="center",
        va="center",
    )
    plt.text(
        (x_min + x_max) / 2 + 80,
        (y_min + y_max) / 2 + 100,
        "Infeasible Problem: demand constraint does\nnot intersect rest of decision space",
        ha="center",
        va="center",
        fontsize=18,
        fontfamily="serif",
        color="red",
        bbox=dict(facecolor="white", edgecolor="black", boxstyle="round"),
    )

    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax


def fig_sensitivitylp_shadowprice(save_to=None):
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

    p1 = util.find_intersection((0, 400), (-1, 500))

    # Feasible Region
    util.plot_x_range(x_min, x_max, axis=None, color="r")
    util.plot_y_range(y_min, y_max, axis=None, color="g")
    util.plot_function(x, demand, ax, color="b")
    x_p1, y_p1 = util.find_intersection((0, 400), (-1, 500))
    x_p2, y_p2 = util.find_intersection((float("inf"), x_max), (-1, 500))
    p1 = (x_p1, y_p1)
    p2 = (x_p2, y_p2)
    util.draw_line_segment(p1, p2, ax, color="grey")

    # Corner Point 1
    plt.annotate(
        r"$J = 1900$",
        p1,
        xytext=(30, 20),
        textcoords="offset points",
        fontsize=16,
        ha="center",
        va="center",
    )

    # Corner Point 2
    plt.annotate(
        r"$J = 1700$",
        p2,
        xytext=(45, 20),
        textcoords="offset points",
        fontsize=16,
        ha="center",
        va="center",
        color="orange",
    )
    ax.plot(p2[0], p2[1], "o", color="orange", markersize=10)

    # Arrow
    p2 = (x_p2 + 0.7, y_p2)
    plt.annotate(
        "",
        p2,
        xytext=(0, 50),
        textcoords="offset points",
        arrowprops=dict(
            arrowstyle="<-", color="orange", linewidth=4, mutation_scale=20
        ),
    )

    # Statement
    plt.text(
        (x_min + x_max) / 2 + 100,
        (y_min + y_max) / 2 - 100,
        "Objective changed by +4 when\nincreasing demand by +1",
        ha="center",
        va="center",
        fontsize=18,
        fontfamily="serif",
        color="orange",
        bbox=dict(facecolor="white", edgecolor="black", boxstyle="round"),
    )

    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax
