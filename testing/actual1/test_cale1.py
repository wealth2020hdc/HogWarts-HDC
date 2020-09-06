from pythoncode import cale
import pytest
import yaml


class TestCale:
    @classmethod
    def setup_class(cls):
        print("执行一次")
        cls.calculate = cale.Calculator()

    @pytest.mark.parametrize("a, b, c", yaml.safe_load(open("./data/data_add.yaml", encoding="UTF-8")),
                             ids=["int", "int2"])
    def test_add(self, a, b, c):
        assert c == self.calculate.add_cale(a, b)
