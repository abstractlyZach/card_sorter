from __future__ import annotations

from . import cards


class Collection(object):
    """A collection of Cards.

    Assumes its input is already sorted.
    """

    _cards: list[cards.Card]

    def __init__(self, cards_=None):
        if cards_ is None:
            cards_ = []
        self._cards = cards_

    def __str__(self):
        return "\n".join(str(card) for card in self._cards)

    def __eq__(self, other: Collection) -> bool:
        return self._cards == other._cards
