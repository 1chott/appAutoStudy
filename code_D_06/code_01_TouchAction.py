# -*- coding: utf-8 -*-
# @Time    : 2019/12/13 17:49
# @Author  : ChoCandy.T

# 导入python需要的webdriver库
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
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
desired_caps["resetKeyboard"] = True
desired_caps["unicodeKeyboard"] = True

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


# 封装获取分辨率方法
def get_resolution():
    resolution = driver.get_window_size()
    return resolution['width'], resolution['height']


# 封装向左滑屏动作方法可传入滑动次数
def sliding_screen(num_times):
    w, h = get_resolution()
    for i in range(num_times):
        driver.swipe(w*0.9, h*0.5, w*0.3, h*0.5)
        time.sleep(2)


# 获取WLAN按钮
wlan_feature = (By.XPATH, '//*[@text="WLAN"]')
wlan_ele = get_ele(wlan_feature)
# wlan 里面的 korman
korman_feature = (By.XPATH, '//*[@text="korman"]')

# 获取显示按钮
display_feature = (By.XPATH, '//*[@text="显示"]')
display_ele = get_ele(display_feature)

# 组合手势操作 3步
# 实例化action 动作对象
action = TouchAction(driver)
# 点击/轻敲操作， 可传入元素对象、坐标、次数 tap(element=None, x=None, y=None, count=1)
action.tap(wlan_ele).perform()
# action.tap(x=385, y=477)

# 长按操作
action.long_press(get_ele(korman_feature), duration=1000)

# # 按压操作
# action.press(display_ele)
# # 松手
# action.release()

# 执行动作
action.perform()

time.sleep(3)
# 关闭资源
driver.quit()