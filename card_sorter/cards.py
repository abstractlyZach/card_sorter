# Allows for forward references. e.g. reference Card in Card's annotations
# https://peps.python.org/pep-0563/#enabling-the-future-behavior-in-python-3-7
from __future__ import annotations

from card_sorter.collections import CardGroup

INVISIBLE_CHARS = ",- '"


def is_ordered(cards: CardGroup, error=False):
    for index in range(len(cards) - 1):
        if cards[index] > cards[index + 1]:
            if error:
                raise AssertionError(
                    f"{cards[index]} does not come before {cards[index + 1]}"
                )
            return False
    return True


def archidekt_name_comparator(name1: str, name2: str) -> int:
    """Recursively compare names using Archidekt's alphabetical ordering.

    - Returns negative if name1 should come first in alphabetical order.
    - Returns 0 if the names are the same.
    - Returns positive otherwise.
    """
    name1, name2 = name1.lower(), name2.lower()
    zero_len_status = _handle_zero_len_names(name1, name2)
    if zero_len_status != 2:
        return zero_len_status

    recursion_status = recurse_if_needed(name1, name2)
    if recursion_status != 2:
        return recursion_status

    first_char1, first_char2 = name1[0], name2[0]

    # default comparison
    if first_char1 < first_char2:
        return -1
    else:
        return 1


def _handle_zero_len_names(name1: str, name2: str) -> int:
    if len(name1) == 0 and len(name2) == 0:
        return 0
    elif len(name1) == 0:
        return -1
    elif len(name2) == 0:
        return 1
    return 2


def recurse_if_needed(name1: str, name2: str) -> int:
    first_char1, first_char2 = name1[0], name2[0]
    if first_char1 in INVISIBLE_CHARS:
        return archidekt_name_comparator(name1[1:], name2[:])
    if first_char2 in INVISIBLE_CHARS:
        return archidekt_name_comparator(name1[:], name2[1:])
    if first_char1 == first_char2:
        return archidekt_name_comparator(name1[1:], name2[1:])
    return 2


class Card:
    def __init__(self, name: str):
        self._name: str = name

    @property
    def name(self):
        return self._name

    def __eq__(self, other: Card):
        return self.name == other.name

    def __lt__(self, other: Card):
        return archidekt_name_comparator(self.name, other.name) < 0

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'Card("{self._name}")'
