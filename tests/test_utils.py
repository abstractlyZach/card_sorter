from card_sorter import cards, utils

DATA_FILENAME = "tests/data/favorite_cards.txt"
CARD_NAMES = [
    "Isshin, Two Heavens as One",
    "Mardu Siegebreaker",
    "Marneus Calgar",
    "Phelia, Exuberant Shepherd",
    "Seeing Double",
]


def test_importing_card_names():
    card_names = utils.read_card_names_from_txt(DATA_FILENAME)
    assert card_names == CARD_NAMES


def test_importing_cards():
    test_cards = utils.get_cards_from_txt(DATA_FILENAME)
    assert test_cards == [cards.Card(name) for name in CARD_NAMES]


def test_importing_cards_to_collection():
    collection = utils.get_collection_from_txt(DATA_FILENAME)
    assert collection == utils.get_collection_from_card_names(CARD_NAMES)
