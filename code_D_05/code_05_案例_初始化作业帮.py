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
# desired_caps["appActivity"] = ".activity.user.passport.ChoiceLoginModeActivity"
desired_caps["appActivity"] = "com.baidu.homework.activity.init.InitActivity"
desired_caps["resetKeyboard"] = True    # 输入中文需要重置输入键盘
desired_caps["unicodeKeyboard"] = True  # 采用unicode码输入

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


time.sleep(5)
skip_feature = (By.XPATH, '//*[@text="跳过"]')
get_ele(driver, skip_feature).click()

student_feature = (By.XPATH, '//*[@text="学生"]')
get_ele(driver, student_feature).click()

grade_feature = (By.XPATH, '//*[@text="高一"]')
get_ele(driver, grade_feature).click()

sub_feature = (By.XPATH, '//*[@text="完成"]')
get_ele(driver, sub_feature).click()
time.sleep(4)

main_feature = (By.CLASS_NAME, 'android.view.View')
get_ele(driver, main_feature).click()
time.sleep(2)
get_ele(driver, main_feature).click()
time.sleep(5)

# 关闭资源
driver.quit()
