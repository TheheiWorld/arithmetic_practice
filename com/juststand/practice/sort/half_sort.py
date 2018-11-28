#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/11/28 下午9:36

'''
二分法插入：
二分法插入排序的思想和直接插入一样，
只是找合适的插入位置的方式不同，
这里是按二分法找到合适的位置，
可以减少比较的次数
'''

orgin = [49, 38, 65, 97, 76, 13, 27, 49, 78, 34, 12, 64, 1]
def sort(origin):
    for index, num in enumerate(orgin):
        temp = num
        left = 0
        right = index - 1
        mid = 0

        while left <= right:
            mid = int((left + right)/2)
            if temp < orgin[mid]:
                right = mid - 1
            else:
                left = mid + 1

        for i in range(index - 1, left - 1 , -1):
            orgin[i + 1] = orgin[i]

        if left != index:
            orgin[left] = temp

sort(orgin)
print(orgin)