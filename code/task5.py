#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle

print(pickle.format_version)
print(pickle.compatible_formats)

# 这个 题目有点晕忽忽的  ，一是对 pickle这个模块用的比较少 ，平时还是json 比较多
# 二是 对结果的呈现形式 没有自己试过
with open('banner.p','rb') as f:
    content = pickle.load(f)
    # print(content)
    for i in content:
        print(i)
    for line in content:
        # way one
        print(''.join(map(lambda pair: pair[0]*pair[1], line)))
        # way two
        line_str = [ char*num for char, num in line]
        print(''.join(line_str))