# -*- coding: utf-8 -*-
# @Time    : 2019/12/13 17:49
# @Author  : ChoCandy.T

# 导入python需要的webdriver库
import time

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# 定义一个空字典存放具体的配置参数
desired_caps = dict()

# 书写具体的参数
desired_caps["platformName"] = "android"
desired_caps["platformVersion"] = "5.1.1"
desired_caps["deviceName"] = "emulator-5554"
desired_caps["appPackage"] = "com.android.settings"
desired_caps["appActivity"] = ".Settings"

# 实例化driver对象, 打开 设置页面（设置app）
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


# 封装查找元素方法，使用try防止报错
def get_ele(driver_obj, feature):
    wait = WebDriverWait(driver_obj, 5, 1)
    try:
        ele = wait.until(lambda x: x.find_element(*feature))
    except Exception as e:
        print(e, feature)
        return None
    else:
        return ele


search_btn = (By.ID, 'com.android.settings:id/search')
search_input = (By.XPATH, '//*[@text="搜索…"]')
search_back_btn = (By.CLASS_NAME, 'android.widget.ImageButton')

# 查找搜索按钮， 点击
search_btn = get_ele(driver, search_btn)
search_btn.click()

# 查找搜索输入框， 查找搜索返回按钮
search_input = get_ele(driver, search_input)
search_back_btn = get_ele(driver, search_back_btn)

# 搜索框输入 11  等待3s 清空输入框内容  # 占时无法输入中文，需要添加其他配置
search_input.send_keys("blue")
time.sleep(3)
search_input.clear()
time.sleep(3)

# 点击返回按钮
search_back_btn.click()
time.sleep(3)

# 关闭资源
driver.quit()
