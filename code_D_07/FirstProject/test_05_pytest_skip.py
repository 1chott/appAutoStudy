# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 11:28
# @Author  : ChoCandy.T


import pytest


# 跳过范围包括 模块 类 方法
# 跳过方法和类 直接加装饰器 @pytest.mark.skip() 无条件跳过 或者@pytest.mark.skipif(条件) 有条件跳过bool类型
# 跳过模块 pytestmark = pytest.mark.skip()   必须使用pytestmark 变量接收

pytestmark = pytest.mark.skip()


class TestDemo:
    @pytest.mark.skip()
    def test_demo_01(self):
        print('我是demo_01')

    def test_demo_02(self):
        print('我是demo_02')


@pytest.mark.skip()
class TestDemo2:
    def test_demo_03(self):
        print('我是demo_03')

    def test_demo_04(self):
        print('我是demo_04')