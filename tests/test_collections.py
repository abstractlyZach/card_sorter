import pytest

from card_sorter import cards, collections

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


def test_no_duplicates(test_collection):
    assert len(test_collection) == 5
