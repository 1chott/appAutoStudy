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
    action = TouchAction(driver)
    # 如果feature是元组类型 这调用获取元素的方法， 否则就是元素对象
    if isinstance(feature, tuple):
        ele = get_ele(feature)
    else:
        ele = feature
    # 点击操作
    action.tap(ele).perform()


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
def sliding_screen_left(num_times):
    w, h = get_resolution()
    for i in range(num_times):
        driver.swipe(w*0.9, h*0.5, w*0.3, h*0.5)
        time.sleep(2)


# 封装向上滑屏动作方法可传入滑动次数，慢速滑动不会有惯性
def sliding_screen_top(num_times, speed):
    w, h = get_resolution()
    for i in range(num_times):
        driver.swipe(w*0.5, h*0.9, w*0.5, h*0.1, speed)
        time.sleep(0.5)


# 封装递归查找元素方法
slide_times = 0     # 全局变量控制滑动次数，防止元素不存在无限滑屏（防止无递归出口）


# 封装递归查找元素方法
def get_ele_recursion(feature, pages):
    global slide_times  # 获取全局变量
    ele = get_ele(feature)
    if ele:     # 递归出口一： 查找到元素
        slide_times = 0    # 递归出口记得恢复全局变量的值
        return ele
    elif slide_times >= pages:      # 递归出口二： 滑屏超过X次后提示找不到元素，退出递归
        slide_times = 0     # 递归出口记得恢复全局变量的值
        print("滑动{}页找不到该元素{}".format(pages, feature))
        return None
    else:
        sliding_screen_top(1, 4000)
        slide_times += 1       # 递归条件之二
        return get_ele_recursion(feature, pages)


# 获取 关于平板电脑按钮
ipad_feature = (By.XPATH, '//*[@text="关于平板电脑aaa"]')
ipad_ele = get_ele_recursion(ipad_feature, 5)

execute_tap(ipad_ele)

# 关闭资源
driver.quit()
