import pytest

from card_sorter import cards, utils

cards_to_add_next_to_each_other = utils.str_to_collection(
    """Oliphaunt
     Olivia, Crimson Bride
     Ollenbock Escort"""
)


@pytest.fixture
def small_collection():
    return utils.str_to_collection(
        """Okiba Salvage
        Omen of the Sea
        Oni-Cult Anvil
        Onward // Victory"""
    )


add_card_test_cases = [
    (cards.Card("Oliphaunt")),
    (cards.Card("One with Nothing")),
]


def collection_has_no_non_empty_packets(small_collection):
    assert len(small_collection.get_packets()) == 0


@pytest.mark.parametrize("new_card", add_card_test_cases)
def test_add_single_card_to_collection_shows_up_in_packet(small_collection, new_card):
    small_collection.insert(new_card)
    packets = small_collection.get_packets()
    assert len(packets) == 1
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


def test_add_multiple_cards_to_a_packet(small_collection):
    for card in cards_to_add_next_to_each_other:
        small_collection.insert(card)
    packets = small_collection.get_packets()
    assert len(packets) == 1
    my_packet = packets[0]
    assert my_packet.card_before == cards.Card("Okiba Salvage")
    assert my_packet.card_after == cards.Card("Omen of the Sea")
    assert len(my_packet) == len(cards_to_add_next_to_each_other)


def test_packet_printing(small_collection):
    small_collection.insert(add_card_test_cases[0])
    assert (
        str(small_collection)
        == """Okiba Salvage
\tOliphaunt
Omen of the Sea
Oni-Cult Anvil
Onward // Victory"""
    )


def test_packet_before_everything(small_collection):
    small_collection.insert(cards.Card("Alpha Authority"))
    my_packet = small_collection.get_packets()[0]
    assert my_packet.card_before == cards.Card("<null card>")
    assert my_packet.card_after == cards.Card("Okiba Salvage")


def test_packet_after_everything(small_collection):
    small_collection.insert(cards.Card("Zurgo Helmsmasher"))
    my_packet = small_collection.get_packets()[0]
    assert my_packet.card_before == cards.Card("Onward // Victory")
    assert my_packet.card_after == cards.Card("<null card>")
