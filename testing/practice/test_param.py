# --*-HogWarts-HDC-*--
# --*-UTF-8-*--


# datas = [(1, 2, 3), (4, 5, 6)]
# myids = ["整数", "int"]
import yaml

with open('data/a.yaml') as f:
    datas = yaml.safe_load(f)
    myids = datas.keys()
    mydatas = datas.values()


def test_param(param):
    print(f'param:{param}')
    print("动态生成测试用例")
