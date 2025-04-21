import pytest

from card_sorter import cards, utils


@pytest.fixture
def small_collection():
    return utils.get_collection_from_card_names(
        [
            "Okiba Salvage",
            "Omen of the Sea",
            "Oni-Cult Anvil",
            "Onward // Victory",
        ]
    )


add_card_test_cases = [
    (cards.Card("Oliphaunt")),
    (cards.Card("One with Nothing")),
]


@pytest.mark.parametrize("new_card", add_card_test_cases)
def test_add_single_card_to_collection_shows_up_in_packet(small_collection, new_card):
    small_collection.insert(new_card)
    packets = small_collection.get_packets()
    assert new_card in packets[0]


ordering_test_cases = [
    (
        cards.Card("Oliphaunt"),
        cards.Card("Okiba Salvage"),
        cards.Card("Omen of the Sea"),
    ),
    (
        cards.Card("One with Nothing"),
        cards.Card("Omen of the Sea"),
        cards.Card("Oni-Cult Anvil"),
    ),
]


@pytest.mark.parametrize(
    "new_card, expected_card_before, expected_card_after", ordering_test_cases
)
def test_add_single_card_to_collection_packet_has_right_ordering(
    small_collection, new_card, expected_card_before, expected_card_after
):
    small_collection.insert(new_card)
    packets = small_collection.get_packets()
    my_packet = packets[0]
    assert my_packet.card_before == expected_card_before
    assert my_packet.card_after == expected_card_after


# do the same, but check the packet left and right card
