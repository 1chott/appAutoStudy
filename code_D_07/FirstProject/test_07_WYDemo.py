# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 15:12
# @Author  : ChoCandy.T


# 导包
# 创建一个手机驱动 和里面工作
import time
import pytest

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


import Base


class TestDemo:
    def setup(self):
        # 手机驱动
        self.driver = Base.get_diver()
        # 执行操作
        self.action = Base.BaseAction(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_tap_top(self):
        # 点击操作  要先获取元素信息
        box_feature = By.ID, "com.netease.newsreader.activity:id/fo"
        top_feature = By.XPATH, "//*[@text='置顶']"
        top_obj = self.action.get_ele_ancestry(box_feature,top_feature)
        
        self.action.execute_tap(top_obj)
        
        black_feature = By.ID, "com.netease.newsreader.activity:id/aq4"
        time.sleep(2)
        self.action.execute_tap(black_feature)

    @pytest.mark.parametrize("info", [{"user": "111@163.com", "password": "123456"}, {"user": "222@163.com", "password": "123456"}])
    def test_login(self, info):
        # 点击我 登录
        tab_feature = By.ID, "android:id/tabs"
        me_feature = By.XPATH, "//*[@text='我']"
        me_obj = self.action.get_ele_ancestry(tab_feature,me_feature)
        self.action.execute_tap(me_obj)
        
        # 点击登录按钮
        btn_feature = By.ID, "com.netease.newsreader.activity:id/a7a"
        self.action.execute_tap(btn_feature)
        
        # 输入账号
        val_feature = By.ID, "com.netease.newsreader.activity:id/ph"
        pwd_feature = By.ID, "com.netease.newsreader.activity:id/pn"
        
        # 最近点击登录按钮
        login_feature = By.ID, "com.netease.newsreader.activity:id/pp"
        
        self.action.execute_input(val_feature, info["user"])
        time.sleep(2)
        action2 = TouchAction(self.driver)
        action2.tap(x=600, y=100).perform()
        self.action.execute_input(pwd_feature, info["password"])
        time.sleep(2)
        action2.tap(x=600, y=100).perform()
        self.action.execute_tap(login_feature)




