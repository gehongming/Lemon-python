#__author__="G"
#date: 2019/6/29
# -*- coding: utf-8 -*-
# Name: conftest
# Author: 简
# Time: 2019/6/20

from selenium import webdriver
import pytest
import os


from work_pytest.PageObjects.ketangpai_login_page import LoginPage
from work_pytest.TestDatas import common_datas as cd
from work_pytest.TestDatas import work_datas as ld
from work_pytest.common import contants



# 删除指定目录下的文件
def remove_files_in_dir(dir):
    files = os.listdir(dir)
    for item in files:
        c_path = os.path.join(dir,item)
        if os.path.isdir(c_path):
            remove_files_in_dir(c_path)
        else:
            os.remove(c_path)

# session级别的
@pytest.fixture(scope="session",autouse=True)
def session_action():
    print("===== 会话开始，测试用例开始执行=====")
    # 清除测试报告、截图目录
    remove_files_in_dir(contants.allure_dir)
    remove_files_in_dir(contants.screenshot_dir)
    yield
    print("===== 会话结束，测试用例全部执行完成！=====")

@pytest.fixture(scope="function")
def open_url():
    # 前置
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(cd.base_url)
    LoginPage(driver).login(ld.login_data["phone"],ld.login_data["pwd"])
    yield driver  # yield之前代码是前置，之后的代码就是后置。
    # 后置
    driver.quit()





# 在测试用例中使用fixture
# @pytest.mark.usefixtures("函数名称")
# @pytest.fixture(scope="class")
# def login_web(open_url):
#     # 登陆操作
#     LoginPage(open_url).login(cd.user,cd.passwd)
#     yield open_url



# work_1前置=打开浏览器+访问+登录
# work_1后置=关闭浏览器
# work_2前置=打开浏览器+访问+登录
# work_2后置=关闭浏览器
# work_2前置=打开浏览器+访问+登录
# work_2后置=关闭浏览器