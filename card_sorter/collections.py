from __future__ import annotations

import bisect

from . import cards


class CardGroup(object):
    """A collection of Cards.

    Assumes its input is already sorted.
    """

    _cards: list[cards.Card]

    def __init__(self, cards_: list[cards.Card] = None):
        if cards_ is None:
            cards_ = []
        # deduplicate the list
        seen = set()
        self._cards = []
        for i, card in enumerate(cards_):
            if card not in seen:
                self._cards.append(card)
                seen.add(card)

    def __str__(self):
        if not self._cards:
            return "<No cards>"
        return "\n".join(str(card) for card in self._cards)

    def __eq__(self, other: Collection) -> bool:
        return self._cards == other._cards

    def __iter__(self):
        for card in self._cards:
            yield card

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, key):
        return self._cards[key]

    def __contains__(self, item: cards.Card) -> bool:
        return item in self._cards


class Collection(CardGroup):
    """A collection of Cards and Packets.

    Assumes its input is already sorted.
    """

    _packets: list[Packet]

    def __init__(self, cards_=None):
        super().__init__(cards_)
        self._packets = [
            Packet(self._cards[i], self._cards[i + 1])
            for i in range(len(self._cards) - 1)
        ]

    def __str__(self):
        if not self._cards:
            return "<No cards>"
        lines = []
        for i in range(len(self._packets)):
            lines.append(str(self._cards[i]))
            if not self._packets[i].is_empty():
                lines.append("\t" + str(self._packets[i]))
        lines.append(str(self._cards[-1]))
        return "\n".join(lines)

    def insert(self, card_: cards.Card) -> None:
        # subtract 1 because packets are offset by 1 since they're in-betweens
        insert_index = bisect.bisect_left(self._cards, card_) - 1
        self._packets[insert_index].add(card_)

    def get_packets(self) -> list[Packet]:
        return [packet for packet in self._packets if not packet.is_empty()]


class Packet(CardGroup):
    _card_before: cards.Card
    _card_after: cards.Card

    def __init__(self, card_before: cards.Card, card_after: cards.Card, cards_=None):
        super().__init__(cards_)
        self._card_before = card_before
        self._card_after = card_after

    def __repr__(self):
        to_return = "Packet("
        num_cards_to_print = min(len(self._cards), 3)
        for i in range(num_cards_to_print):
            to_return += str(self._cards[i])
        to_return += ")"
        return to_return

    def add(self, card_: cards.Card) -> None:
        self._cards.append(card_)

    def sort(self):
        self._cards.sort()

    def is_empty(self) -> bool:
        return not self._cards

    @property
    def card_before(self) -> cards.Card:
        return self._card_before

    @property
    def card_after(self) -> cards.Card:
        return self._card_after
