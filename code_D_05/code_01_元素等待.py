# -*- coding: utf-8 -*-
# @Time    : 2019/12/13 17:49
# @Author  : ChoCandy.T

# 导入python需要的webdriver库
from appium import webdriver
from selenium.webdriver.common.by import By

# 定义一个空字典存放具体的配置参数
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = dict()

# 书写具体的参数
desired_caps["platformName"] = "android"
desired_caps["platformVersion"] = "5.1.1"
desired_caps["deviceName"] = "emulator-5554"
desired_caps["appPackage"] = "com.android.settings"
desired_caps["appActivity"] = ".Settings"

# 实例化driver对象, 打开 设置页面（设置app）
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# 显式等待 (driver对象， 等待时间， 多久查询一次)
wait = WebDriverWait(driver, 5, 1)
# 显示等待 wait.until(self, method, message='')
obj = wait.until(lambda x: x.find_element(By.XPATH, "//*[@text='蓝牙']"))
print(obj)

# 隐式等待
# driver.implicitly_wait(3)

# 强制等待
# import time
# time.sleep(3)

# 关闭资源
driver.quit()
