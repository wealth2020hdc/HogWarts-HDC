# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
import pytest


def test_assume():
    print("登录操作")
    pytest.assume(1 == 2)
    print("搜索操作")
    pytest.assume(2 == 2)
    print("加购操作")
    pytest.assume(3 == 2)

