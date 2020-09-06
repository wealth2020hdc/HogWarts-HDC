import pytest
import yaml


@pytest.fixture(autouse=True)
def cale_hint():
    print("开始计算")
    yield
    print("计算结束\n")


# 命令行去添加一个参数
def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")

    mygroup.addoption("--env",
                      default='test',
                      dest='env',
                      help='set your run env')


@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    print(myenv)
    if myenv == 'test':
        dataspath = 'data/test/data.yaml'

    if myenv == 'dev':
        dataspath = 'data/dev/data.yaml'

    if myenv == 'st':
        dataspath = 'data/st/data.yaml'

    with open(dataspath) as f:
        datas = yaml.safe_load(f)

    return myenv, datas
