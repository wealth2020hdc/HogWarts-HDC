# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
def test_case(cmdoption):
    print("测试环境验证")
    print(cmdoption)
    env, datas = cmdoption
    ip = datas["env"]["ip"]
    port = datas["env"]["port"]
    username = datas["env"]["username"]
    password = datas["env"]["password"]
    print(f'环境：{env}')
    print(f'http://{ip}:{port}')
    print(f'用户：{username}')
    print(f'密码：{password}')
