import blackjack

def test_count():
    user = [3,5]
    result = blackjack.count(user)
    assert result == 8