# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 17:56
# @Author  : ChoCandy.T


# 快排    array数组  (传入数据需要是数字列表)
def quick_sort(array):
    # 递归出口  如果传入的数组列表 长度=1，返回列表
    if len(array) <= 1:
        return array

    # 获取列表第一个元素
    item = array[0]
    # 遍历剩余元素 与 item 比大小 所以遍历范围定为 array[1::] (去掉了下标为0的元素)
    # 这里用的列表推导式写，也可以用for循环嵌套if语句
    smaller = [i for i in array[1::] if i <= item]  # 比item小或等于的放入 samller列表
    bigger = [i for i in array[1::] if i > item]     # 比item大的放入 bigger 列表
    # 将smaller列表和[item]和bigger进行列表拼接组成排好序的列表
    return quick_sort(smaller) + [item] + quick_sort(bigger)


# # 快排    array数组  (传入数据需要是数字列表)
# def quick_sort(array):
#     # 递归出口  如果传入的数组列表 长度=1，返回列表
#     if len(array) <= 1:
#         return array
#
#     # 用来比较的默认元素
#     item = array[0]
#     smaller = []    # 比 item 小和等于的数存放的列表
#     bigger = []     # 比 item 大的数存放的列表
#     for i in array[1::]:    # 遍历剩余元素
#         if i <= item:       # 比 item 小和等于的数存放到smaller列表
#             smaller.append(i)
#         else:               # 比 item 大的数存放到bigger列表
#             bigger.append(i)
#
#     # smaller、bigger 列表也需要排序
#     return quick_sort(smaller) + [item] + quick_sort(bigger)


# item 要查找的数，  array 有序数组(已经排好序的数组)
def binary_search(item, array):
    mini_index = 0  # 获取最小值的下标
    max_index = len(array) - 1  # 获取最大值的下标
    while mini_index <= max_index:
        mid_index = (mini_index + max_index) // 2   # 整个列表的中间元素的下标
        guess = array[mid_index]    # 中间那个元素 猜数字 从中间那个元素开始对比猜
        if item < guess:    # 目标数字比 猜测数字小 （也就是说目标数值在列表的左半边）
            max_index = mid_index - 1   # 将最大值的下标改为 中间值左边元素的下标
        elif item > guess:  # 目标数字比 猜测数字大 （也就是说目标数值在列表的右半边）
            mini_index = mid_index + 1  # 将最小值的下标改为 中间值右边元素的下标
        elif item == guess:     # 猜对的时候 直接返回下标
            return mid_index
        else:       # 不存在返回 None
            return None


if __name__ == '__main__':
    # 生成测试数据
    num_list = []
    import random
    for j in range(30):
        num_list.append(random.randint(0, 60))

    # 打印源数据和排序后数据
    print(num_list)     # [62, 8, 13, 66, 37, 36, 3, 88, 46, 67, 44, 97, 36, 3, 41]
    a_array = quick_sort(num_list)     # [3, 3, 8, 13, 36, 36, 37, 41, 44, 46, 62, 66, 67, 88, 97]
    print(a_array)

    a_array = list(set(a_array))
    a_item = random.randint(0, 60)
    print(a_item)
    print(binary_search(a_item, a_array))
