import pytest

from card_sorter import utils


@pytest.fixture
def small_collection():
    return utils.str_to_collection(
        """Okiba Salvage
        Omen of the Sea
        Oni-Cult Anvil
        Onward // Victory"""
    )


@pytest.fixture
def test_collection():
    return utils.str_to_collection(
        """Sentinel of the Pearl Trident
        Seraphic Greatsword
        Seraphic Greatsword
        Seven-Tail Mentor
        Shakedown Heavy
        Shield of the Realm"""
    )
