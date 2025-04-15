from card_sorter import cards

def test_sorting():
    first = cards.Card('Isshin, Two Heavens as One')
    second = cards.Card('Marneus Calgar')
    assert first < second

def test_sorting_2():
    first = cards.Card('Svella, Ice Shaper')
    second = cards.Card('Radha, Heir to Keld')
    assert second < first
