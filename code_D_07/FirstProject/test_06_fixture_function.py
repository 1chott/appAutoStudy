# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 12:13
# @Author  : ChoCandy.T


import pytest


# 将login()设置为工厂函数  autouse=False 默认值 设为 True的时候调用的时候就不需要手动传
@pytest.fixture(autouse=True)
def login():
    print('1111')
    

class TestDemo:
    # 调用工厂函数 将方法当参数传入
    def test_demo_01(self, login):
        print("2222")
        
    def test_demo_02(self):
        print("3333")
