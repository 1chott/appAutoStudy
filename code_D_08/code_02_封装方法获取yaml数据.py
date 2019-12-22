# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 14:55
# @Author  : ChoCandy.T


def get_data(f_name, info):
    import yaml
    with open('./Data/{}.yaml'.format(f_name), 'r', encoding='utf-8')as f:
        data = yaml.load(f)
    data = list(data[info].values())
    return data


print(get_data(5, "login_success"))
