# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 9:06
# @Author  : ChoCandy.T


# 与unittest不同之处， 1. 测试类不需要继承任何父类  2.类级别的fixture方法命名不同
class TestDemo:

    def setup_class(self):
        print("我是类级别的初始化方法setup_class")

    def setup(self):
        print("我是方法级别的初始化方法setup")

    def teardown(self):
        print("我是方法级别的销毁方法teardown")

    def teardown_class(self):
        print("我是类级别的销毁方法teardown_class")

    def test_demo1(self):
        print("我是demo1单元测试")

    # pytest 用例失败自动重试， pip install pytest-rerunfailures
    # Terminal运行输入 pytest --reruns 次数
    def test_demo2(self):
        assert False
