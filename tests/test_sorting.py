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
def test_comparing_two_cards(
    description: str, expected_smaller: str, expected_larger: str
):
    expected_smaller = cards.Card(expected_smaller)
    expected_larger = cards.Card(expected_larger)
    assert expected_smaller < expected_larger, description


def test_create_a_collection():
    collections.Collection(
        [cards.Card("Isshin"), cards.Card("Boros Charm"), cards.Card("Opt")]
    )


def test_collection_sorted():
    collection = utils.get_collection_from_card_names(
        [
            "Adventurous Impulse",
            "Agent of the Shadow Thieves",
            "Akroan Hoplite",
            "Alaundo the Seer",
            "Alexi's Cloak",
        ]
    )
    assert cards.is_ordered(collection)


def test_collection_not_sorted():
    collection = utils.get_collection_from_card_names(
        [
            "Agent of the Shadow Thieves",
            "Adventurous Impulse",
            "Akroan Hoplite",
            "Alaundo the Seer",
            "Alexi's Cloak",
        ]
    )
    assert not cards.is_ordered(collection)


def test_same_cards_are_sorted():
    collection = utils.get_collection_from_card_names(
        [
            "Agent of the Shadow Thieves",
            "Agent of the Shadow Thieves",
            "Agent of the Shadow Thieves",
            "Agent of the Shadow Thieves",
        ]
    )
    assert cards.is_ordered(collection)
