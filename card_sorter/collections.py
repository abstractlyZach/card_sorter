from . import cards


class Collection(object):
    """A collection of Cards.

    Assumes its input is already sorted.
    """

    _cards: list[cards.Card]

    def __init__(self, cards: list[cards.Card] = []):
        self._cards = cards

    def __str__(self):
        return "\n".join(str(card) for card in self._cards)
