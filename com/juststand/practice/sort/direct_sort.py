#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/11/28 下午8:56

'''
直接插入排序：
每步将一个待排序的记录，
按其顺序码大小插入到前面已经排序的字序列的合适位置（从后向前找到合适位置后），
直到全部插入排序完为止
'''

orgin = [49, 38, 65, 97, 76, 13, 27, 49, 78, 34, 12, 64, 1]

def sort(source):
    for index,num in enumerate(orgin):
        if index == 0:
            continue
        temp = num
        i = index - 1
        while i >= 0:
            if orgin[i] > temp:
                orgin[i + 1] = orgin[i]
            else:
                break
            i = i - 1
        orgin[i + 1] = temp
    print(orgin)


sort(orgin)