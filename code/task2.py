#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# way one
with open('ocr', 'r') as f:
    content = f.read()
    bytes = []  # 文档中有哪些字符串
    stat_dict = {}  # 每个字符串的个数 组成字典
    result = ''  # 最后的字符串拼接起来
    for s in content:
        bytes.append(s) if s not in bytes else ''
    for char in bytes:
        stat_dict[char] = 0
    for char in content:
        stat_dict[char] += 1
    for char in stat_dict:
        result += char if stat_dict[char] == 1 else ''
    print(result)

# way two
with open('ocr', 'r') as f:
    content = f.read()
    bytes = set(content)  # 用集合 可以迅速地找出构成元素  里面包含换行符
    stat_dict = {}  # 每个字符串的个数 组成字典
    for char in content:
        stat_dict[char] = stat_dict.get(char, 0) + 1
    stat_dict.pop('\n')  # 需要删除换行符
    avgOC = len(content)//len(stat_dict)  # 理解什么是 rare
    result = ''.join([c for c in stat_dict if stat_dict[c] < avgOC])
    print(result)

# way 3
with open('ocr', 'r') as f:
    content = f.read()
    bytes = set(content)  # 用集合 可以迅速地找出构成元素  里面包含换行符
    stat_dict = {}  # 每个字符串的个数 组成字典
    for char in bytes:  # 使用count 可以减少 循环次数
        stat_dict[char] = content.count(char)
    stat_dict.pop('\n')  # 需要删除换行符
    avgOC = len(content)//len(stat_dict)  # 理解什么是 rare
    result = ''.join([c for c in stat_dict if stat_dict[c] < avgOC])
    print(result)
