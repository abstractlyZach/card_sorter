from . import cards, collections


def get_collection_from_txt(filename: str) -> collections.Collection:
    return collections.Collection(get_cards_from_txt(filename))


def get_collection_from_card_names(card_names: list[str]) -> collections.Collection:
    return collections.Collection([cards.Card(name) for name in card_names])


def get_cards_from_txt(filename: str) -> list[cards.Card]:
    return [cards.Card(name) for name in read_card_names_from_txt(filename)]


def read_card_names_from_txt(filename: str) -> list[str]:
    names = []
    with open(filename) as infile:
        for line in infile:
            names.append(line.strip())
    return names
