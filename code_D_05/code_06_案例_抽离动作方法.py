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
desired_caps["appPackage"] = "com.baidu.homework"
# desired_caps["appActivity"] = ".activity.user.passport.ChoiceLoginModeActivity"   # adb 获取的启动名 初始化启动 但是不一样
desired_caps["appActivity"] = "com.baidu.homework.activity.init.InitActivity"   # aapt 获取的启动名 初始化启动
desired_caps["resetKeyboard"] = True    # 输入中文需要重置输入键盘
desired_caps["unicodeKeyboard"] = True  # 采用unicode码输入

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
time.sleep(5)
skip_feature = (By.XPATH, '//*[@text="跳过"]')
skip_btn = get_ele(skip_feature)

if skip_btn:
    execute_tap(skip_feature)

    student_feature = (By.XPATH, '//*[@text="学生"]')
    execute_tap(student_feature)

    grade_feature = (By.XPATH, '//*[@text="高一"]')
    execute_tap(grade_feature)

    sub_feature = (By.XPATH, '//*[@text="完成"]')
    execute_tap(sub_feature)
    time.sleep(4)

    main_feature = (By.CLASS_NAME, 'android.view.View')
    execute_tap(main_feature)
    time.sleep(2)
    execute_tap(main_feature)
    time.sleep(5)
else:
    print("不是第一次启动app")

# 关闭资源
driver.quit()
