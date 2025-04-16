# Allows for forward references. e.g. reference Card in Card's annotations
# https://peps.python.org/pep-0563/#enabling-the-future-behavior-in-python-3-7
from __future__ import annotations

SPECIAL_ORDERING = ",'"


def archidekt_name_comparator(name1: str, name2: str) -> int:
    """Recursively compare names using Archidekt's alphabetical ordering.

    - Returns negative if name1 should come first in alphabetical order.
    - Returns 0 if the names are the same.
    - Returns positive otherwise.
    """
    if len(name1) == 0 and len(name2) == 0:
        return 0
    elif len(name1) == 0:
        return -1
    elif len(name2) == 0:
        return 1

    first_char1, first_char2 = name1[0], name2[0]
    if first_char1 == first_char2:
        return archidekt_name_comparator(name1[1:], name2[1:])

    # different chars
    if first_char1 in SPECIAL_ORDERING and first_char2 in SPECIAL_ORDERING:
        name1_char_index = SPECIAL_ORDERING.index(first_char1)
        name2_char_index = SPECIAL_ORDERING.index(first_char2)
        if name1_char_index < name2_char_index:
            return -1
        else:
            return 1

    # Archidekt deprioritizes spaces
    if first_char1 == " ":
        return 1
    elif first_char2 == " ":
        return -1

    # default comparison
    if first_char1 < first_char2:
        return -1
    else:
        return 1


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
