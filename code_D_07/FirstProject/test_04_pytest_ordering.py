# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 11:01
# @Author  : ChoCandy.T


import pytest


class TestDemo:
    # 测试用例执行顺序排序 值小排前
    @pytest.mark.run(order=4)
    def test_demo_01(self):
        print('我是demo_01')

    @pytest.mark.run(order=2)
    def test_demo_02(self):
        print('我是demo_02')

    @pytest.mark.run(order=3)
    def test_demo_03(self):
        print('我是demo_03')

    @pytest.mark.run(order=1)
    def test_demo_04(self):
        print('我是demo_04')
