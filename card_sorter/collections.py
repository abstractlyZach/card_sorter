from __future__ import annotations

from . import cards


class CardGroup(object):
    """A collection of Cards.

    Assumes its input is already sorted.
    """

    _cards: list[cards.Card]

    def __init__(self, cards_=None):
        if cards_ is None:
            cards_ = []
        self._cards = cards_

    def __str__(self):
        if not self._cards:
            return "<No cards>"
        return "\n".join(str(card) for card in self._cards)

    def __eq__(self, other: Collection) -> bool:
        return self._cards == other._cards


class Collection(CardGroup):
    """A collection of Cards and Packets.

    Assumes its input is already sorted.
    """

    _packets: list[Packet]

    def __init__(self, cards_=None):
        super().__init__(cards_)
        self._packets = [Packet() for _ in range(len(self._cards) - 1)]

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


class Packet(CardGroup):
    def sort(self):
        self._cards.sort()

    def is_empty(self) -> bool:
        return not self._cards
