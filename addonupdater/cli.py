"""Enable CLI."""
import click


@click.command()
@click.option('--token', '-T', help='GitHub access_token.')
@click.option('--addon', '-A', help='Addon name.')
@click.option('--repo', '-R', default=None, help='Addon repo.')
@click.option('--test', is_flag=True, help="Test run, will not commit.")
@click.option('--verbose', is_flag=True, help="Print more stuff.")
def cli(token, addon, repo, test, verbose):
    """CLI for this package."""
    from addonupdater.updater import AddonUpdater
    updater = AddonUpdater(token, addon, repo, test, verbose)
    updater.update_addon()


cli()  # pylint: disable=E1120
