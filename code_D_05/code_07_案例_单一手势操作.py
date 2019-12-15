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
def get_ele(feature):
    wait = WebDriverWait(driver, 5, 1)
    try:
        ele = wait.until(lambda x: x.find_element(*feature))
    except Exception as e:
        print(e, feature)
        return None
    else:
        return ele


# 封装点击操作， 可传入元素特征或元素对象
def execute_tap(feature):
    # 如果feature是元组类型 这调用获取元素的方法， 否则就是元素对象
    if isinstance(feature, tuple):
        ele = get_ele(feature)
    else:
        ele = feature
    ele.click()


# 封装输入操作， 可传入元素特征或元素对象
def execute_input(feature, text):
    if isinstance(feature, tuple):
        ele = get_ele(feature)
    else:
        ele = feature
    ele.clear()
    ele.send_keys(text)


# 业务流程
# 滑屏
driver.swipe(230, 1180, 230, 280, 3000)
time.sleep(3)
# 获取屏幕分辨率， 通过分辨率设置滑屏坐标
resolution = driver.get_window_size()
print(resolution)
driver.swipe(resolution["width"]*0.5, resolution["height"]*0.1,resolution["width"]*0.5, resolution["height"]*0.9, 4000)

# scroll 滑屏
# driver.scroll(开始元素， 结束元素)  ios 系统使用

# 关闭资源
driver.quit()
