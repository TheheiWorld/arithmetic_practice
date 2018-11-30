#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author : juststand
# create_date : 2018/11/29 下午5:39

'''
希尔排序
'''

origin = [49, 38, 65, 97, 76, 13, 27, 49, 78, 34, 12, 64, 1]

def sort(origin):
    l = origin.__len__()
    d = l
    while True:
        d = int(d/2)
        for x in range(0, d):
            for i in range(x + d, l):
                temp = origin[i]
                j = i - d
                while j >= 0 and origin[j] > temp:
                    origin[j + d] = origin[j]
                    j = j - d
                else:
                    origin[j + d] = temp

        if d == 1:
            break

sort(origin)
print(origin)

