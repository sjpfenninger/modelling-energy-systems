import matplotlib.pyplot as plt
import seaborn as sns

from modelling_energy_systems.util import SAVETO_KWARGS

sns.set_context("talk")


def build_figures():
    fig_market_supply("images-built/fig_market_supply.jpg")
    fig_market_demand("images-built/fig_market_demand.jpg")
    fig_market_clearing("images-built/fig_market_clearing.jpg")
    fig_markets_acceptedbids("images-built/fig_markets_acceptedbids.jpg")


def fig_market():
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_xlim(0, 80)
    ax.set_ylim(0, 21)
    ax.set_xlabel("Power [MW]", fontsize=16)
    ax.set_ylabel("Price [EUR/MWh]", fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    ax.grid(True)
    return fig, ax


def fig_market_supply(save_to):
    fig, ax = fig_market()

    power_values = [5, 12, 13, 8, 8, 9, 10, 10, 5]
    price_values = [1, 3, 3.5, 4.5, 5, 6, 8, 9, 10]
    total_power = 0

    for i, p in enumerate(price_values):
        ax.axhline(
            y=p, xmin=total_power / 80, xmax=(total_power + power_values[i]) / 80
        )
        total_power += power_values[i]
        if i < len(price_values) - 1:
            ax.axvline(
                x=total_power, ymin=price_values[i] / 21, ymax=price_values[i + 1] / 21
            )
            ax.axvline(x=total_power, ymin=0, ymax=price_values[i] / 21, linestyle="--")

    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax


def fig_market_demand(save_to):
    fig, ax = fig_market()

    power_values = [8, 7, 4, 5, 4, 5, 3, 3]
    price_values = [20, 18, 16, 15, 11, 7, 4, 3]
    total_power = 0

    for i, p in enumerate(price_values):
        ax.axhline(
            y=p,
            xmin=total_power / 80,
            xmax=(total_power + power_values[i]) / 80,
            color="r",
        )
        total_power += power_values[i]
        if i < len(price_values) - 1:
            ax.axvline(
                x=total_power,
                ymax=price_values[i] / 21,
                ymin=price_values[i + 1] / 21,
                color="r",
            )
            ax.axvline(
                x=total_power,
                ymin=0,
                ymax=price_values[i] / 21,
                linestyle="--",
                color="r",
            )
        else:
            ax.axvline(x=total_power, ymin=0, ymax=price_values[i] / 21, color="r")

    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax


def fig_market_clearing(save_to):
    fig, ax = fig_market()

    # Supply
    power_values = [5, 12, 13, 8, 8, 9, 10, 10, 5]
    price_values = [1, 3, 3.5, 4.5, 5, 6, 8, 9, 10]
    total_power = 0

    for i, p in enumerate(price_values):
        ax.axhline(
            y=p, xmin=total_power / 80, xmax=(total_power + power_values[i]) / 80
        )
        total_power += power_values[i]
        if i < len(price_values) - 1:
            ax.axvline(
                x=total_power, ymin=price_values[i] / 21, ymax=price_values[i + 1] / 21
            )

    # Demand
    power_values = [8, 7, 4, 5, 4, 5, 3, 3]
    price_values = [20, 18, 16, 15, 11, 7, 4, 3]
    total_power = 0

    for i, p in enumerate(price_values):
        ax.axhline(
            y=p,
            xmin=total_power / 80,
            xmax=(total_power + power_values[i]) / 80,
            color="r",
        )
        total_power += power_values[i]
        if i < len(price_values) - 1:
            ax.axvline(
                x=total_power,
                ymax=price_values[i] / 21,
                ymin=price_values[i + 1] / 21,
                color="r",
            )
        else:
            ax.axvline(x=total_power, ymin=0, ymax=price_values[i] / 21, color="r")

    # Intersection
    ax.axhline(y=4.5, xmin=0, xmax=33 / 80, color="k", linestyle="--")
    ax.axvline(x=33, ymin=0, ymax=4.5 / 21, color="k", linestyle="--")

    # Annotations
    plt.text(
        15,
        5.75,
        "Clearing Price:\n4.5 EUR/MWh",
        ha="center",
        va="center",
        fontsize=13,
        fontfamily="serif",
        color="k",
        bbox=dict(facecolor="white", edgecolor="black", boxstyle="round"),
    )
    plt.text(
        49,
        1.75,
        "Scheduled Generation\nor Demand: 33 MW",
        ha="center",
        va="center",
        fontsize=13,
        fontfamily="serif",
        color="k",
        bbox=dict(facecolor="white", edgecolor="black", boxstyle="round"),
    )

    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax


def fig_markets_acceptedbids(save_to):
    fig, ax = fig_market()

    # Supply
    power_values = [5, 12, 13, 8, 8, 9, 10, 10, 5]
    price_values = [1, 3, 3.5, 4.5, 5, 6, 8, 9, 10]
    total_power = 0

    for i, p in enumerate(price_values):
        ax.axhline(
            y=p, xmin=total_power / 80, xmax=(total_power + power_values[i]) / 80
        )
        total_power += power_values[i]
        if i < len(price_values) - 1:
            ax.axvline(
                x=total_power, ymin=price_values[i] / 21, ymax=price_values[i + 1] / 21
            )

    # Demand
    power_values = [8, 7, 4, 5, 4, 5, 3, 3]
    price_values = [20, 18, 16, 15, 11, 7, 4, 3]
    total_power = 0

    for i, p in enumerate(price_values):
        ax.axhline(
            y=p,
            xmin=total_power / 80,
            xmax=(total_power + power_values[i]) / 80,
            color="r",
        )
        total_power += power_values[i]
        if i < len(price_values) - 1:
            ax.axvline(
                x=total_power,
                ymax=price_values[i] / 21,
                ymin=price_values[i + 1] / 21,
                color="r",
            )
        else:
            ax.axvline(x=total_power, ymin=0, ymax=price_values[i] / 21, color="r")

    # Intersection
    ax.axhline(y=4.5, xmin=0, xmax=33 / 80, color="k")

    # Shadings
    plt.fill_between([0, 30], [0, 0], [4.5, 4.5], color="blue", alpha=0.5)
    plt.fill_between([30, 33], [0, 0], [4.5, 4.5], color="yellow", alpha=0.5)
    plt.text(
        15,
        4.5 / 2,
        "Unit 1",
        ha="center",
        va="center",
        fontsize=16,
        fontfamily="serif",
        color="k",
    )
    plt.text(
        31.5,
        4.5 / 2,
        "2",
        ha="center",
        va="center",
        fontsize=16,
        fontfamily="serif",
        color="k",
    )

    if save_to:
        plt.savefig(save_to, **SAVETO_KWARGS)
    else:
        return fig, ax
