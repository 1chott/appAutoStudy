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
def sliding_screen(num_times):
    w, h = get_resolution()
    for i in range(num_times):
        driver.swipe(w*0.9, h*0.5, w*0.3, h*0.5)
        time.sleep(2)


# 需求， 打开设置页面，点击安全，点击屏幕锁屏方式， 点击图案， 绘制一个手势
# 获取WLAN按钮
wlan_feature = (By.XPATH, '//*[@text="WLAN"]')
wlan_ele = get_ele(wlan_feature)

# 获取存储按钮
storage_feature = (By.XPATH, '//*[@text="存储"]')
storage_ele = get_ele(storage_feature)

# 安全按钮
security_feature = (By.XPATH, '//*[@text="安全"]')

# 设置页面往上滑， 以显示安全按钮
driver.drag_and_drop(storage_ele, wlan_ele)
time.sleep(2)

# 点击安全按钮
execute_tap(security_feature)

# 点击屏幕锁定方式
lock_method_feature = (By.XPATH, '//*[@text="屏幕锁定方式"]')
lock_method_ele = get_ele(lock_method_feature)

execute_tap(lock_method_ele)

# 点击图案按钮
pattern_feature = (By.XPATH, '//*[@text="图案"]')
execute_tap(pattern_feature)

# 绘制锁屏手势 Z
time.sleep(1)
action2 = TouchAction(driver)
# 先按下一个地方  wait(300) 300ms 一般为人眼可见现象速度
action2.press(x=116, y=421).wait(300).perform()
# 画Z
action2.move_to(x=610, y=425).wait(300).move_to(x=123, y=902).wait(300).move_to(x=610, y=902).wait(300).perform()

time.sleep(2)

# 关闭资源
driver.quit()
