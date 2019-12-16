# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 16:05
# @Author  : ChoCandy.T


from appium import webdriver


class DriverUtils:
    # 手机配置参数
    descried_caps = dict()

    def __init__(self):
        # 书写具体的参数
        self.descried_caps["platformName"] = "android"
        self.descried_caps["platformVersion"] = "5.1.1"
        self.descried_caps["deviceName"] = "emulator-5554"
        self.descried_caps["appPackage"] = "com.android.settings"
        self.descried_caps["appActivity"] = ".Settings"
        self.descried_caps["resetKeyboard"] = True
        self.descried_caps["unicodeKeyboard"] = True
        self.driver = None

    @classmethod
    def get_driver(cls):
        if not cls.driver:
            # 实例化driver对象, 打开 设置页面（设置app）
            cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cls.descried_caps)
