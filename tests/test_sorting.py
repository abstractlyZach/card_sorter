import pytest

from card_sorter import cards, collections, utils

sort_test_parameters = (
    "description, expected_smaller, expected_larger",
    [
        ("", "Isshin, Two Heavens as One", "Marneus Calgar"),
        ("", "Radha, Heir to Keld", "Svella, Ice Shaper"),
        (
            "Comma comes before letters or apostrophe",
            "Tamiyo, Collector of Tales",
            "Tamiyo's Safekeeping",
        ),
        ("Spaces come after letters", "Sunblade Samurai", "Sun Titan"),
        (
            "Apostrophe is ignored pt. 1",
            "You're Confronted By Robbers",
            "Your Temple Is Under Attack",
        ),
        (
            "Apostrophe is ignored pt. 2",
            "Your Temple Is Under Attack",
            "You've Been Caught Stealing",
        ),
        ("Dash is later than letters", "Windgrace Acolyte", "Wind-Scarred Crag"),
    ],
)


@pytest.mark.parametrize(*sort_test_parameters)
def test_sorting(description: str, expected_smaller: str, expected_larger: str):
    expected_smaller = cards.Card(expected_smaller)
    expected_larger = cards.Card(expected_larger)
    assert expected_smaller < expected_larger, description


def test_create_a_collection():
    collections.Collection(
        [cards.Card("Isshin"), cards.Card("Boros Charm"), cards.Card("Opt")]
    )


example_collection_txt1 = "Boros Charm\nIsshin\nOpt"
example_collection_txt2 = "Isshin\nMarneus Calgar\nTheoretical Duplication"

collection_params = [
    (
        [cards.Card("Boros Charm"), cards.Card("Isshin"), cards.Card("Opt")],
        example_collection_txt1,
    ),
    (
        [
            cards.Card("Isshin"),
            cards.Card("Marneus Calgar"),
            cards.Card("Theoretical Duplication"),
        ],
        example_collection_txt2,
    ),
]


@pytest.mark.parametrize("cards_, expected_collection_str", collection_params)
def test_print_collection(cards_, expected_collection_str: str):
    collection = collections.Collection(cards_)
    assert str(collection) == expected_collection_str


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
