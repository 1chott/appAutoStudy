# -*- coding: utf-8 -*-
# @Time    : 2019/12/13 17:49
# @Author  : ChoCandy.T

# 导入python需要的webdriver库
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
        print(e)
        return None
    else:
        return ele


# 蓝牙按钮
bluetooth = (By.XPATH, "//*[@text='蓝牙']")

# 定位到的蓝牙按钮
blue_t_ele = get_ele(driver, bluetooth)

# 后期封装元素操作方法，先判断元素是否存在
if blue_t_ele:
    print('找到蓝牙按钮')
else:
    print('蓝牙按钮不存在')

# 关闭资源
driver.quit()
