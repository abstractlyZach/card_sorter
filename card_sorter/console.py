import click

from card_sorter import cards, utils


@click.command()
@click.argument("csv_filename")
@click.option("--show-collection/--no-show-collection", default=False)
def main(csv_filename: str, show_collection: bool):
    """The hypermodern Python project."""
    collection = utils.get_collection_from_csv(csv_filename)
    if show_collection:
        click.echo(collection)
        click.echo("=" * 20)
    if cards.is_ordered(collection, error=True):
        click.echo("sorted!")
    else:
        click.echo("not sorted :(")
