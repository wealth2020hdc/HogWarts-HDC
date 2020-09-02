# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
import pytest


@pytest.mark.dependency()
# pytest标记预期会失败的测试xfail
@pytest.mark.xfail(reason="deliberate fail")
def test_a():
    print("a")
    assert False


@pytest.mark.dependency()
def test_b():
    print("a")
    assert True


# 依赖a,如果a用例成功，则c会被执行
# 依赖a,如果a用例失败，则c不会被执行，跳过c用例
# depends=[],列表中加入依赖的测试名称
@pytest.mark.dependency(depends=["test_a"])
def test_c():
    print("a")
    assert True


@pytest.mark.dependency(depends=["test_b"])
def test_d():
    print("a")
    assert True


@pytest.mark.dependency(depends=["test_c", "test_b"])
def test_e():
    print("a")
    assert True
