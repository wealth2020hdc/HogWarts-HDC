import allure
import pytest
import yaml
import time
from selenium import webdriver


# 用例标识，可以与用例的管理地址相连
@allure.testcase("http//:www.githua.com")
# 功能模块划分
@allure.feature("百度搜索")
# 参数化
@pytest.mark.parametrize("test_data", yaml.safe_load(open("./data/baidu_data.yaml", encoding="UTF-8")),
                         ids=["search1", "search2", "search3", "search4"])
# @pytest.mark.parametrize("test_data", yaml.safe_load(open("./data/baidu_data.yaml", encoding="UTF-8")),
#                          ids=["search1", "search2"])
def test_steps_demo(test_data):
    with allure.step("打开百度网页"):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com/")
        driver.maximize_window()

    with allure.step(f"输入搜索内容:{test_data}"):
        driver.find_element_by_id("kw").send_keys(test_data)
        time.sleep(3)
        driver.find_element_by_id("su").click()
        time.sleep(5)

    with allure.step("保存图片"):
        driver.save_screenshot(f"./result_picture/{test_data}.png")
        allure.attach.file(f"./result_picture/{test_data}.png", attachment_type=allure.attachment_type.PNG)

    with allure.step("关闭浏览器"):
        driver.quit()






