import click

from modelling_energy_systems import lp


@click.command()
def run():
    lp.build_figures()


if __name__ == "__main__":
    run()
