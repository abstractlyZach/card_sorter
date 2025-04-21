import csv
from collections.abc import Iterable

from . import cards, collections


def get_collection_from_txt(filename: str) -> collections.Collection:
    return collections.Collection(get_cards_from_txt(filename))


def get_collection_from_card_names(card_names: Iterable[str]) -> collections.Collection:
    return collections.Collection([cards.Card(name) for name in card_names])


def get_cards_from_txt(filename: str) -> list[cards.Card]:
    return [cards.Card(name) for name in read_card_names_from_txt(filename)]


def read_card_names_from_txt(filename: str) -> list[str]:
    names = []
    with open(filename) as infile:
        for line in infile.readlines():
            names.append(line.strip())
    return names


def read_card_names_from_csv(filename: str) -> list[str]:
    names = []
    with open(filename) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",", quotechar='"')
        # assuming only 1 item in the row
        for row in spamreader:
            names.append(row[0])
    return names


def get_collection_from_csv(filename: str) -> collections.Collection:
    return get_collection_from_card_names(read_card_names_from_csv(filename))


def str_to_collection(cards_: str) -> collections.Collection:
    """Creates a collection from newline-separated cards names."""
    return get_collection_from_card_names(line.strip() for line in cards_.splitlines())
