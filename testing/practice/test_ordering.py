# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
import pytest


# @pytest.mark.run(order=4)
@pytest.mark.last
def test_one():
    print("one")
    assert 1 == 2 / 2


# @pytest.mark.run(order=3)
@pytest.mark.third
def test_two():
    print("two")
    assert 3 == 1 + 2


# @pytest.mark.run(order=2)
@pytest.mark.second
def test_three():
    print("three")
    assert 3 == 1 + 2


# @pytest.mark.run(order=1)
@pytest.mark.first
def test_four():
    print("four")
    assert 3 == 1 + 2
