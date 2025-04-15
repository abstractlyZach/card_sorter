import pytest
from card_sorter import cards

sort_test_parameters = (
    "description,expected_smaller, expected_larger",
    [
        ("", "Isshin, Two Heavens as One", "Marneus Calgar"),
        ("", "Radha, Heir to Keld", "Svella, Ice Shaper"),
        (
            "Comma comes before apostrophe",
            "Tamiyo, Collector of Tales",
            "Tamiyo's Safekeeping",
        ),
        ("Spaces come after letters", "Sunblade Samurai", "Sun Titan"),
    ],
)


@pytest.mark.parametrize(*sort_test_parameters)
def test_sorting(description: str, expected_smaller: str, expected_larger: str):
    expected_smaller = cards.Card(expected_smaller)
    expected_larger = cards.Card(expected_larger)
    assert expected_smaller < expected_larger, description
