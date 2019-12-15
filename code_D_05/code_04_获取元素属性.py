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


# 定位更多按钮
more_feature = (By.XPATH, '//*[@text="更多"]')
more_btn = get_ele(driver, more_feature)

# 获取各种属性 多数uiautomatorviewer 里面显示的都能获取到
print("name:", more_btn.get_attribute("name"))   # 获取text， 如果text为空， 获取content-desc
print("classname: ", more_btn.get_attribute("className"))
print("resourceid ", more_btn.get_attribute("resourceId"))

# 关闭资源
driver.quit()
