# -*- coding: utf-8 -*-
# @Time    : 2019/12/13 17:49
# @Author  : ChoCandy.T

# 导入python需要的webdriver库
from appium import webdriver
from selenium.webdriver.common.by import By

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

# 点击设置界面的 搜索按钮
# driver.find_element_by_id("com.android.settings:id/search").click()
search_btn = (By.ID, 'com.android.settings:id/search')
driver.find_element(*search_btn).click()

# 点击搜索功能的 返回按钮
# driver.find_element_by_class_name("android.widget.ImageButton").click()
back_btn = (By.CLASS_NAME, 'android.widget.ImageButton')
driver.find_element(*back_btn).click()

# 点击设置页面的 WLAN按钮
# driver.find_element_by_xpath("//*[@text='WLAN']").click()
wlan_btn = (By.XPATH, "//*[@text='WLAN']")
driver.find_element(*wlan_btn).click()

# 关闭资源
driver.quit()
