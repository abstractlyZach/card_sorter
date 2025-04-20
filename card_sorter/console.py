import click

from card_sorter import cards, utils


@click.command()
@click.argument("csv_filename")
def main(csv_filename: str):
    """The hypermodern Python project."""
    collection = utils.get_collection_from_csv(csv_filename)
    # for card in collection:
    #     click.echo(card)
    if cards.is_ordered(collection, error=True):
        click.echo("sorted!")
    else:
        click.echo("not sorted :(")
