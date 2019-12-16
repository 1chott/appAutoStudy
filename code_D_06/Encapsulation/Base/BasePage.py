# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 16:24
# @Author  : ChoCandy.T
from Encapsulation.Base.Driver import DriverUtils
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self):
        self.driver = DriverUtils.get_driver()
        self.slide_times = 0

    # 封装查找元素方法，使用try防止报错
    def get_ele(self, feature):
        wait = WebDriverWait(self.driver, 5, 1)
        try:
            ele = wait.until(lambda x: x.find_element(*feature))
        except Exception as e:
            print(e, feature)
            return None
        else:
            return ele

    # 封装方法， 传父类和子类的feature
    def get_ele_by_father(self, father_feature, son_feature):
        father_ele = self.get_ele(father_feature)
        wait = WebDriverWait(father_ele, 5, 1)
        try:
            ele = wait.until(lambda x: x.find_element(*son_feature))
        except Exception as e:
            print(e, son_feature)
            return None
        else:
            return ele

    # 封装递归查找元素方法
    def get_ele_recursion(self, feature, pages):
        ele = self.get_ele(feature)
        if ele:  # 递归出口一： 查找到元素
            slide_times = 0  # 递归出口记得恢复全局变量的值
            return ele
        elif self.slide_times >= pages:  # 递归出口二： 滑屏超过X次后提示找不到元素，退出递归
            slide_times = 0  # 递归出口记得恢复全局变量的值
            print("滑动{}页找不到该元素{}".format(pages, feature))
            return None
        else:
            self.sliding_screen_top(1, 4000)    # TODO BaseHandler 导入
            self.slide_times += 1  # 递归条件之二
            return self.get_ele_recursion(feature, pages)
