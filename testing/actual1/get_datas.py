# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
import yaml


def get_datas():
    datas_dict = {}
    with open('./data/data_cale.yaml') as f:
        datas = yaml.safe_load(f)
        datas_dict["add_datas"] = datas["add"].values()
        datas_dict["add_mgids"] = datas["add"].keys()
        datas_dict["sub_datas"] = datas["sub"].values()
        datas_dict["sub_mgids"] = datas["sub"].keys()
        datas_dict["mul_datas"] = datas["mul"].values()
        datas_dict["mul_mgids"] = datas["mul"].keys()
        datas_dict["div_datas"] = datas["div"].values()
        datas_dict["div_mgids"] = datas["div"].keys()
    return datas_dict
