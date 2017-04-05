#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

# way one
with open('task4.txt', 'r',closefd=True) as f:
    # content = f.read()
    # print(f.read())   #打印结果为 空   ，因为 第二次read  会在第一次read 的结束处 开始
    # regExp = re.search(r'[^A-Z]+([A-Z]{3})([a-z]{1})([A-Z]{3})[^A-Z]+',content)
    # print(regExp.groups())
    str_arr = f.readlines()
    result = []
    for i in str_arr:
        regExp = re.search(r'[^A-Z]+([A-Z]{3})([a-z]{1})([A-Z]{3})[^A-Z]+', i)
        result.append(regExp.group(2)) if regExp else ''
    print(''.join(result))

# way two
with open('task4.txt', 'r',closefd=True) as f:
    content = f.read()
    # 生成一个list ，元素为group
    regExp = re.findall(r'[^A-Z]+[A-Z]{3}([a-z]{1})[A-Z]{3}[^A-Z]+', content)
    print(''.join(regExp))
