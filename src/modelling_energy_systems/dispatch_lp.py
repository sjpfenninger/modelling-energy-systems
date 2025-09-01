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
    fig_dispatchlp_modifieddemand("images-built/fig_dispatchlp_modifieddemand.jpg")
    fig_dispatchlp_modifieddemand_contourlines(
        "images-built/fig_dispatchlp_modifieddemand_contourlines.jpg"
    )


def setup_fig_dispatchlp_decisionspace(min_coord, max_coord):
    MIN_COORD = min_coord
    MAX_COORD = max_coord

    fig, ax = plt.subplots(figsize=(8, 8))

    ax.set_xlim(MIN_COORD, MAX_COORD)
    ax.set_ylim(MIN_COORD, MAX_COORD)
    ax.set_xlabel("$\\mathbf{P_{G1}}$: Power from coal power plant [MW]")
    ax.set_ylabel("$\\mathbf{P_{G2}}$: Power from gas power plant [MW]")
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
    p1 = util.find_intersection((0, 400), (-1, 500))
    p2 = util.find_intersection((float("inf"), 300), (-1, 500))
    util.draw_line_segment(p1, p2, ax, color="grey")

    # Corner Point 1
    plt.annotate(
        "$J = 3(100)+4(400) = 1900$",
        p1,
        xytext=(120, 30),
        textcoords="offset points",
        ha="center",
        va="center",
        bbox=dict(boxstyle="round,pad=0.5", fc="white", alpha=1),
    )

    # Corner Point 2
    plt.annotate(
        "Optimal solution\n$J = 3(300)+4(200) = 1700$",
        p2,
        xytext=(10, -40),
        textcoords="offset points",
        ha="center",
        va="center",
        bbox=dict(boxstyle="round,pad=0.5", fc="white", alpha=1),
    )

    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax


def fig_dispatchlp_contourlines(save_to=None):
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
    p1 = util.find_intersection((0, 400), (-1, 500))
    p2 = util.find_intersection((float("inf"), 300), (-1, 500))
    util.draw_line_segment(p1, p2, ax, color="grey")

    # Optimum
    ax.plot(p2[0], p2[1], "o", color="orange", markersize=10)

    # Objective
    def obj(x):
        return (1700 - 3 * x) / 4

    def obj_val(x, y):
        return 3 * x + 4 * y

    # Level Curves
    p1_arrow, p2_arrow = util.repeat_line(
        x, obj, obj_val, ax, 3, 30, color="k", linestyle="--"
    )

    # Arrows
    ax.text(
        p1_arrow[0],
        p1_arrow[1] + 15,
        "$J$ increasing",
        bbox=dict(facecolor="white", edgecolor="black", boxstyle="round"),
    )
    ax.text(
        p2_arrow[0],
        p2_arrow[1] - 15,
        "$J$ decreasing",
        bbox=dict(facecolor="white", edgecolor="black", boxstyle="round"),
    )

    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax


def fig_dispatchlp_contourlines_parallel(save_to=None):
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
    p1 = util.find_intersection((0, 400), (-1, 500))
    p2 = util.find_intersection((float("inf"), 300), (-1, 500))
    util.draw_line_segment(p1, p2, ax, color="orange")

    # Optimum
    ax.plot(p2[0], p2[1], "o", color="orange", markersize=10)

    # Objective
    def obj(x):
        return (2000 - 4 * x) / 4

    def obj_val(x, y):
        return 4 * x + 4 * y

    # Level Curves
    p1_arrow, p2_arrow = util.repeat_line(
        x, obj, obj_val, ax, 3, 30, labels=False, color="k", linestyle="--"
    )

    # Arrow Text
    ax.text(
        p1_arrow[0],
        p1_arrow[1] + 15,
        "$J$ increasing",
        bbox=dict(facecolor="white", edgecolor="black", boxstyle="round"),
    )
    ax.text(
        p2_arrow[0],
        p2_arrow[1] - 15,
        "$J$ decreasing",
        bbox=dict(facecolor="white", edgecolor="black", boxstyle="round"),
    )

    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax


def fig_dispatchlp_activeconstraints(save_to=None):
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
    lower_x_range, upper_x_range = util.plot_x_range(x_min, x_max, ax, color="k")
    lower_y_range, upper_y_range = util.plot_y_range(y_min, y_max, ax, color="k")
    demand_line = util.plot_function(x, demand, ax, color="b")

    # Line Segment
    p1 = util.find_intersection((0, 400), (-1, 500))
    p2 = util.find_intersection((float("inf"), 300), (-1, 500))

    # Corner Point 2
    plt.annotate(
        r"$J = 1700$",
        p2,
        xytext=(40, 20),
        textcoords="offset points",
        fontsize=16,
        ha="center",
        va="center",
        color="orange",
    )
    ax.plot(p2[0], p2[1], "o", color="orange", markersize=10)

    # Active Constraints
    upper_x_range.set_color("red")
    upper_x_range.set_linewidth(3)
    demand_line.set_color("red")
    demand_line.set_linewidth(3)

    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax


def fig_dispatchlp_modifieddemand(save_to=None):
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

    p_int1 = util.find_intersection((0, y_max), (-1, 500))
    p_int2 = util.find_intersection((0, y_max), (float("inf"), x_min))
    p_int3 = util.find_intersection((0, y_min), (float("inf"), x_min))
    p_int4 = util.find_intersection((0, y_min), (float("inf"), x_max))
    p_int5 = util.find_intersection((float("inf"), x_max), (-1, 500))

    plt.fill_between(
        x,
        y_min * np.ones_like(x),
        y_max * np.ones_like(x),
        where=(x >= x_min) & (x <= p_int1[0] + 2),
        color="gray",
        alpha=0.5,
    )
    plt.fill_between(
        x,
        y_min * np.ones_like(x),
        demand(x),
        where=(x >= p_int1[0]) & (x <= x_max),
        color="gray",
        alpha=0.5,
    )
    plt.text(
        (x_min + x_max) / 2 - 10,
        (y_min + demand((x_min + x_max) / 2)) / 2,
        "Feasible Region",
        ha="center",
        va="center",
    )

    # Corner Points
    ax.plot(p_int1[0], p_int1[1], "o", color="grey", markersize=10)
    ax.plot(p_int2[0], p_int2[1], "o", color="grey", markersize=10)
    ax.plot(p_int3[0], p_int3[1], "o", color="orange", markersize=10)
    ax.plot(p_int4[0], p_int4[1], "o", color="grey", markersize=10)
    ax.plot(p_int5[0], p_int5[1], "o", color="grey", markersize=10)

    plt.annotate(
        r"$J = 3(50) + 4(100) = 550$",
        p_int3,
        xytext=(110, -25),
        textcoords="offset points",
        fontsize=16,
        ha="center",
        va="center",
        color="orange",
        bbox=dict(boxstyle="round,pad=0.5", fc="white", alpha=1),
    )

    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax


def fig_dispatchlp_modifieddemand_contourlines(save_to=None):
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

    p_int1 = util.find_intersection((0, y_max), (-1, 500))
    p_int2 = util.find_intersection((0, y_max), (float("inf"), x_min))
    p_int3 = util.find_intersection((0, y_min), (float("inf"), x_min))
    p_int4 = util.find_intersection((0, y_min), (float("inf"), x_max))
    p_int5 = util.find_intersection((float("inf"), x_max), (-1, 500))

    plt.fill_between(
        x,
        y_min * np.ones_like(x),
        y_max * np.ones_like(x),
        where=(x >= x_min) & (x <= p_int1[0] + 2),
        color="gray",
        alpha=0.5,
    )
    plt.fill_between(
        x,
        y_min * np.ones_like(x),
        demand(x),
        where=(x >= p_int1[0]) & (x <= x_max),
        color="gray",
        alpha=0.5,
    )

    # Corner Points
    ax.plot(p_int1[0], p_int1[1], "o", color="grey", markersize=10)
    ax.plot(p_int2[0], p_int2[1], "o", color="grey", markersize=10)
    ax.plot(p_int3[0], p_int3[1], "o", color="orange", markersize=10)
    ax.plot(p_int4[0], p_int4[1], "o", color="grey", markersize=10)
    ax.plot(p_int5[0], p_int5[1], "o", color="grey", markersize=10)

    plt.annotate(
        r"$J = 550$",
        p_int3,
        xytext=(40, -25),
        textcoords="offset points",
        fontsize=16,
        ha="center",
        va="center",
        color="orange",
        bbox=dict(boxstyle="round,pad=0.5", fc="white", alpha=1),
    )

    # Level Curves
    def obj(x):
        return (550 - 3 * x) / 4

    def obj_val(x, y):
        return 3 * x + 4 * y

    p1_arrow, p2_arrow = util.repeat_line(
        x, obj, obj_val, ax, 6, 60, labels=False, color="k", linestyle="--"
    )

    # Arrow Text
    ax.text(
        p1_arrow[0],
        p1_arrow[1] + 15,
        "$J$ increasing",
        bbox=dict(facecolor="white", edgecolor="black", boxstyle="round"),
    )

    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax
