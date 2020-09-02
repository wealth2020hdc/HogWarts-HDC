import pytest


def test_one():
    assert 3 == 1 + 2


@pytest.mark.flaky(reruns=5, reruns_delay=1)
def test_two():
    assert 5 == 1 * 3
