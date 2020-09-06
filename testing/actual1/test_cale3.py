# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
from pythoncode.cale import Calculator
from testing.actual1.get_datas import get_datas
import pytest
import allure


@allure.feature("计算器测试")
class TestCale(object):
    datas = get_datas()

    @classmethod
    def setup_class(cls):
        cls.cale = Calculator()

    @allure.story("加法测试")
    @pytest.mark.parametrize('a, b, c', datas["add_datas"], ids=datas["add_mgids"])
    @pytest.mark.first
    @pytest.mark.dependency(name='add')
    def test_add(self, a, b, c):
        print("第一个执行")
        try:
            assert c == self.cale.add_cale(a, b)
        except Exception as f:
            print(f)
            return False

    @allure.story("减法测试")
    @pytest.mark.parametrize('a, b, c', datas["sub_datas"], ids=datas["sub_mgids"])
    @pytest.mark.second
    @pytest.mark.dependency(name='sub', depends=["add"])
    def test_sub(self, a, b, c):
        print("第二个执行")
        try:
            assert c == self.cale.sub_cale(a, b)
        except Exception as f:
            print(f)
            return False

    @allure.story("乘法测试")
    @pytest.mark.parametrize('a, b, c', datas["mul_datas"], ids=datas["mul_mgids"])
    @pytest.mark.third
    @pytest.mark.dependency(name='mul')
    def check_mul(self, a, b, c):
        print("第三个执行")
        try:
            assert c == self.cale.mul_cale(a, b)
        except Exception as f:
            print(f)
            assert False

    @allure.story("除法测试")
    @pytest.mark.parametrize('a, b, c', datas["div_datas"], ids=datas["div_mgids"])
    @pytest.mark.last
    @pytest.mark.dependency(name='div', depends=["mul"])
    def check_div(self, a, b, c):
        print("最后执行")
        try:
            assert c == self.cale.div_cale(a, b)
        except Exception as f:
            print(f)
            assert False
