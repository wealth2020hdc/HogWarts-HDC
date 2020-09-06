# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
from typing import List

import pytest
import yaml


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    print(len(items))
    # 倒叙执行测试用例
    # items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)


# 命令行去添加一个参数
def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")

    mygroup.addoption("--env",
                      default='test',
                      dest='env',
                      help='set your run env')

    mygroup.addoption("--env1",
                      default='test',
                      dest='env1',
                      help='set your run env')


# @pytest.fixture(scope='session')
# def cmdoption(request):
#     myenv = request.config.getoption("--evn", default='test')
@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    print(myenv)
    if myenv == 'test':
        dataspath = 'data/test/data.yaml'

    if myenv == 'dev':
        dataspath = 'data/dev/data.yaml'

    with open(dataspath) as f:
        datas = yaml.safe_load(f)

    return myenv, datas


# 通过方法动态的生成测试用例
def pytest_generate_tests(metafunc: "Metafunc") -> None:
    if "param" in metafunc.fixturenames:
        metafunc.parametrize("param",
                             metafunc.module.mydatas,
                             ids=metafunc.module.myids,
                             scope='function')