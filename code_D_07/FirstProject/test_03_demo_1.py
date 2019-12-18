# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 10:27
# @Author  : ChoCandy.T


import pytest
import time
from selenium.webdriver.common.by import By

import Base


class TestDemoSettings:
    def setup(self):
        self.driver = Base.get_diver()
        self.action = Base.BaseAction(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.run(order=10)  # 测试用例执行顺序排序
    @pytest.mark.parametrize("info", [{"key": "蓝牙"}, {"key": "WLAN"}])
    def test_demo_1(self, info):
        # 测试用例 打开设置， 点击搜索按钮， 搜索框输入内容
        # 搜索按钮、 搜索框
        search_btn = (By.ID, 'com.android.settings:id/search')
        search_input = (By.ID, 'android:id/search_src_text')

        # 点击搜索按钮
        self.action.execute_tap(search_btn)
        # 搜索框输入内容
        self.action.execute_input(search_input, info["key"])
        time.sleep(2)
