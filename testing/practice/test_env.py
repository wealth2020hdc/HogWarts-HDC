# --*-HogWarts-HDC-*--
# --*-UTF-8-*--


# 测试用例通过fixture方法的传入，获取测试数据 / 开发数据
def test_case(cmdoption):
    print("测试环境验证")
    print(cmdoption)
    env, datas = cmdoption
    print(f'环境：{env}, 数据：{datas}')
    ip = datas['env']['ip']
    port = datas['env']['port']
    url = 'http://'+ip+':'+str(port)
    print(url)

