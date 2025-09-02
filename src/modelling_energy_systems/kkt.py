import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from modelling_energy_systems.util import SAVETO_KWARGS

sns.set_context("talk")

MIN_COORD = 0
MAX_COORD = 500
P_D = 500


def build_figures():
    fig_kkt_contours("images-built/fig_kkt_contours.jpg")
    fig_kkt_contours_constraints("images-built/fig_kkt_contours_constraints.jpg")
    fig_kkt_limited_constraints("images-built/fig_kkt_limited_constraints.jpg")


def _basic_fig_kkt_contours():
    fig, ax = plt.subplots(figsize=(8, 8))

    ax.set_xlim(MIN_COORD, MAX_COORD)
    ax.set_ylim(MIN_COORD, MAX_COORD)
    ax.set_aspect("equal", "box")
    ax.set_xlabel("$\\mathbf{P_{G1}}$", fontsize=18)
    ax.set_ylabel("$\\mathbf{P_{G2}}$", fontsize=18)
    ax.grid(False)

    # Remove x and y tick labels
    ax.tick_params(axis="both", which="both", labelbottom=False, labelleft=False)

    return fig, ax


def setup_fig_kkt_contours():

    fig, ax = _basic_fig_kkt_contours()

    g1 = np.linspace(MIN_COORD, MAX_COORD, 300)
    g2 = np.linspace(MIN_COORD, MAX_COORD, 300)
    G1, G2 = np.meshgrid(g1, g2)
    Z = G1**2 + G2**2

    ax.contour(G1, G2, Z, levels=8, colors="red")

    line_g1 = np.array([MIN_COORD, MAX_COORD])
    line_g2 = P_D - line_g1
    ax.plot(line_g1, line_g2, color="blue", linewidth=2)
    ax.text(255, 255, r"$P_D - {P}_{G1} - {P}_{G2} = 0$", color="blue", fontsize=18)

    p = np.array([350, 150])

    grad_f = np.array([3, 3])
    grad_h = np.array([-1, -1])

    u_f = grad_f / np.linalg.norm(grad_f)
    u_h = grad_h / np.linalg.norm(grad_h)

    scale = 50

    return fig, ax, p, u_f, u_h, scale


def fig_kkt_contours(save_to=None):
    fig, ax, p, u_f, u_h, scale = setup_fig_kkt_contours()

    ax.plot(p[0], p[1], "o", color="blue", markersize=10)

    ax.arrow(
        p[0],
        p[1],
        u_f[0] * scale,
        u_f[1] * scale,
        color="red",
        head_width=10,
        length_includes_head=True,
    )

    ax.text(
        p[0] + u_f[0] * scale * 1.1,
        p[1] + u_f[1] * scale * 1.1,
        r"$\nabla f(x)$",
        color="red",
        fontsize=16,
    )

    ax.arrow(
        p[0],
        p[1],
        u_h[0] * scale,
        u_h[1] * scale,
        color="blue",
        head_width=10,
        length_includes_head=True,
    )
    ax.text(
        p[0] + u_h[0] * scale * 1.3,
        p[1] + u_h[1] * scale * 1.3,
        r"$\nabla h(x)$",
        color="blue",
        fontsize=16,
    )

    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax


def fig_kkt_contours_constraints(save_to=None):
    fig, ax, p, u_f, u_h, scale = setup_fig_kkt_contours()

    x = np.linspace(MIN_COORD, MAX_COORD, 100)
    x_min = 0
    x_max = 400
    y_min = 00
    y_max = 400

    # Shade the rectangular region defined by x_min, x_max, y_min, y_max
    xs = [x_min, x_max, x_max, x_min]
    ys = [y_min, y_min, y_max, y_max]
    ax.fill(xs, ys, color="grey", alpha=0.3)

    # Points
    ax.plot(400, P_D - 400, "o", color="blue", markersize=10)

    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax


def fig_kkt_limited_constraints(save_to=None):
    fig, ax, p, u_f, u_h, scale = setup_fig_kkt_contours()

    x = np.linspace(MIN_COORD, MAX_COORD, 100)
    x_min = 0
    x_max = 350
    y_min = 0
    y_max = 350

    # Shade the rectangular region defined by x_min, x_max, y_min, y_max
    xs = [x_min, x_max, x_max, x_min]
    ys = [y_min, y_min, y_max, y_max]
    ax.fill(xs, ys, color="grey", alpha=0.3)

    # Points
    p1 = 400
    p2 = 350
    textoffset = 10
    ax.plot(p1, P_D - p1, "o", color="blue", alpha=0.3, markersize=10)
    ax.text(
        p1 - textoffset,
        P_D - p1 - textoffset,
        "Previous optimal solution",
        horizontalalignment="right",
    )
    ax.plot(p2, P_D - p2, "o", color="blue", markersize=10)
    ax.text(
        p2 - textoffset,
        P_D - p2 - textoffset,
        "New optimal solution",
        horizontalalignment="right",
    )

    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax


if __name__ == "__main__":
    build_figures()
