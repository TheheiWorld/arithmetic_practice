#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/11/30 下午8:35

'''
直接选择排序：
在要排序的一组数中，
选出最小的一个数与第一个位置的数交换；
然后在剩下的数当中再找最小的与第二个位置的数交换，
如此循环到倒数第二个数和最后一个数比较为止。
'''

origin = [49, 38, 65, 97, 76, 13, 27, 49, 78, 34, 12, 64, 1, 8]

def sort(origin):
    l = origin.__len__()
    for index, num in enumerate(origin):
        min = num
        min_index = index

        for j in range(index + 1, l):
            if origin[j] < min:
                min = origin[j]
                min_index = j

        origin[min_index] = origin[index]
        origin[index] = min

sort(origin)
print(origin)
