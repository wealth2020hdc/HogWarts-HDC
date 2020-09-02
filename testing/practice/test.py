# --*-HogWarts-HDC-*--
# --*-UTF-8-*--

# with open("./steps/step.yaml") as f:
#     steps = yaml.safe_load(f)
# return list(steps)
import yaml

with open("./steps/step.yaml") as f:
    print(f)
    steps = yaml.safe_load(f)
    print(steps)