# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 9:06
# @Author  : ChoCandy.T
import pytest


class TestDemo:

    # (key, (value1, value2))
    @pytest.mark.parametrize("user", ["Tom", "Jerry"])
    def test_demo_1(self, user):
        print("=" * 40)
        print("测试数据user: ", user)

    # ((key1, key2), [(value1, value2), (value1, value2)])  # 需要一一对应
    @pytest.mark.parametrize(("user", "password"), [("Tom", "123456"), ("Jerry", "654321")])
    def test_demo_2(self, user, password):
        print("=" * 40)
        print("测试数据user: ", user)
        print("测试数据password: ", password)

    # 模拟json格式数据 (key, [{k1: v1, k2: v2}, {k1: v1, k2: v2}])  获取数据 v1/v2=key[k1/k2]
    @pytest.mark.parametrize("info", [{"user": "Tom", "password": "123456"}, {"user": "Jerry", "password": "654321"}])
    def test_demo_3(self, info):
        print("="*40)
        print("测试数据user: ", info["user"])
        print("测试数据password: ", info["password"])
