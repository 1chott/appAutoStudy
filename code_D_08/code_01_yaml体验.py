# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 10:11
# @Author  : ChoCandy.T


import yaml

with open("./Data/1.yaml", "r", encoding="UTF-8") as f:
    data_1 = yaml.load(f)

with open("./Data/2.yaml", "r", encoding="UTF-8") as f:
    data_2 = yaml.load(f)

with open("./Data/3.yaml", "r", encoding="UTF-8") as f:
    data_3 = yaml.load(f)

print(data_1)
print(data_2)
print(data_3)
