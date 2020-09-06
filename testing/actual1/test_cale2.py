# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
from pythoncode.cale import Calculator
import pytest
import yaml
import allure

with open('./data/data_cale.yaml') as f:
    datas = yaml.safe_load(f)
    add_datas = datas["add"].values()
    add_mgids = datas["add"].keys()
    sub_datas = datas["sub"].values()
    sub_mgids = datas["sub"].keys()
    mul_datas = datas["mul"].values()
    mul_mgids = datas["mul"].keys()
    div_datas = datas["div"].values()
    div_mgids = datas["div"].keys()


@allure.feature("计算器测试")
class TestCale(object):
    @classmethod
    def setup_class(cls):
        cls.cale = Calculator()

    @allure.story("加法测试")
    @pytest.mark.parametrize('a, b, c', add_datas, ids=add_mgids)
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
    @pytest.mark.parametrize('a, b, c', sub_datas, ids=sub_mgids)
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
    @pytest.mark.parametrize('a, b, c', mul_datas, ids=mul_mgids)
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
    @pytest.mark.parametrize('a, b, c', div_datas, ids=div_mgids)
    @pytest.mark.last
    @pytest.mark.dependency(name='div', depends=["mul"])
    def check_div(self, a, b, c):
        print("最后执行")
        try:
            assert c == self.cale.div_cale(a, b)
        except Exception as f:
            print(f)
            assert False
