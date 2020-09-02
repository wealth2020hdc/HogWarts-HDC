# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
import pytest
import yaml

from pythoncode.cale import Calculator

cale = Calculator()


def get_steps():
    with open("./steps/step.yaml") as f:
        steps = yaml.safe_load(f)
    return list(steps)


def steps(a, b, result):
    steps1 = get_steps()
    # print(type(steps1))
    # print(steps1)
    for step in steps1:
        # print(step)
        if "add_cale" == step:
            print("add_cale")
            assert result == cale.add_cale(a, b)
        elif "add_cale1" == step:
            print("add_cale1")
            assert result == cale.add_cale1(a, b)
        elif "add_cale2" == step:
            print("add_cale2")
            assert result == cale.add_cale1(a, b)


@pytest.mark.parametrize("a, b, result", yaml.safe_load(open("./data/cale.yaml"))["add"].values(),
                         ids=yaml.safe_load(open("./data/cale.yaml"))["add"].keys())
def test_add(a, b, result):
    print("参数化")
    steps(a, b, result)
    print("参数化")