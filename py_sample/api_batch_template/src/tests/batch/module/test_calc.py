from batch.module import plus


def test_plus_integer():
    result = plus(1, 2)
    assert result == 3
