import matplotlib.pyplot as plt
import seaborn as sns

from modelling_energy_systems.util import SAVETO_KWARGS

sns.set_context("talk")


def build_figures():
    fig_stochastic("images-built/fig_stochastic.jpg")
    fig_stochastic_with_no_uncert("images-built/fig_stochastic_with_no_uncert.jpg")


def fig_stochastic(save_to):
    fig, ax = plt.subplots(figsize=(8, 4))

    x = range(1, 5)
    y1 = [0.25, 1.75, 1.25, 2.75]
    y2 = [0.25, 1.75, 3, 3]

    plt.plot(x, y1, label="Scenario 1 (high price)", color="blue")
    plt.plot(x, y2, label="Scenario 2 (low price)", color="green")

    plt.xlabel("Time period")
    plt.ylabel("Consumption (kWh)")
    plt.legend()

    ax.set_xticks([1, 2, 3, 4])
    ax.set_yticks([0, 0.5, 1, 1.5, 2, 2.5, 3])

    # plt.gca().yaxis.grid(
    #     True, linestyle="-", which="major", color="grey", linewidth=0.5
    # )

    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax


def fig_stochastic_with_no_uncert(save_to):
    fig, ax = plt.subplots(figsize=(8, 4))

    x = range(1, 5)
    y1 = [0.25, 1.75, 1.25, 2.75]
    y2 = [0.25, 1.75, 3, 3]
    y3 = [1, 2.5, 1.5, 3]

    plt.plot(x, y1, label="Scenario 1 (high price)", color="blue")
    plt.plot(x, y2, label="Scenario 2 (low price)", color="green")
    plt.plot(x, y3, label="No uncertainty", color="orange")

    plt.xlabel("Time period")
    plt.ylabel("Consumption (kWh)")
    plt.legend()

    ax.set_xticks([1, 2, 3, 4])
    ax.set_yticks([0, 0.5, 1, 1.5, 2, 2.5, 3])

    # plt.gca().yaxis.grid(
    #     True, linestyle="-", which="major", color="grey", linewidth=0.5
    # )

    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax
