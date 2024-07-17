import click

from modelling_energy_systems import dispatch_lp


@click.command()
def run():
    dispatch_lp.build_figures()


if __name__ == "__main__":
    run()
