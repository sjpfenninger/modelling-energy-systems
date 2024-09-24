import click

from modelling_energy_systems import dispatch_lp, lp_sensitivity, markets_milp


@click.command()
def run():
    dispatch_lp.build_figures()
    lp_sensitivity.build_figures()


if __name__ == "__main__":
    run()
