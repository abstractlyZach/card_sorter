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


@pytest.fixture
def removed_packets():
    return [
        utils.str_to_collection(
            """
Bane's Contingency
Bane's Contingency
Bane's Contingency
Bane's Contingency
Bane's Contingency
        """
        ),
        utils.str_to_collection(
            """
Banishment
Basilisk Gate
Battle Brawler
Bearer of Memory
Beckoning Will-o'-Wisp
        """
        ),
        utils.str_to_collection("""Boon of Boseiju"""),
        utils.str_to_collection(
            """
Candlekeep Inspiration
Candlekeep Sage
Carefree Swinemaster
Careful Cultivation"""
        ),
        utils.str_to_collection(
            """
Commander's Sphere
Command Tower
Cone of Cold
Contact Other Plane
Coronation of Chaos
Corrosive Ooze
Crackling Doom"""
        ),
    ]


@pytest.fixture
def big_collection():
    return utils.str_to_collection(
        """
Bane's Invoker
Banishing Slash
Befriending the Moths // Imperial Moth
Behold the Unspeakable // Vision of the Unspeakable
Benalish Honor Guard
Bishop of Rebirth
Blade of the Oni
Blink of an Eye
Bloodfell Caves
Blood Pact
Blossoming Sands
Bludgeon Brawl
Blunt the Assault
Blur
Bonecaller Cleric
Borderland Marauder
Braids's Frightful Return
Brave the Sands
Breath Weapon
Bronze Cudgels
Brute Suit
Burnished Hart
Bygone Bishop
Caligo Skin-Witch
Campfire
Carnelian Orb of Dragonkind
Cast Down
Cavalry Pegasus
Chain Devil
Champion of the Flame
Charcoal Diamond
Chardalyn Dragon
Circle of the Land Druid
Citadel Gate
Clawing Torment
Cloak of the Bat
Cloakwood Hermit
Cloakwood Swarmkeeper
Clockwork Fox
Cloudkill
Cloudreader Sphinx
Coiling Stalker
Cold-Water Snapper
Colossal Badger // Dig Deep
Commander Liara Portyr
Crib Swap
Crush Contraband
Crystal Dragon // Rob the Hoard
Curator's Ward
Daring Archaeologist
Dark Bargain
Dark Ritual
"""
    )
