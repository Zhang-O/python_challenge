#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request as ur
import re, time



baseUrl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
URL = []
ddd = '12345'
i = 1
def openUrl(num):
    with ur.urlopen(baseUrl+num,timeout= 100) as f:
        data = f.read()
        if re.search(r'(\d+)', data.decode('utf-8')):
            nothing = re.search(r'(\d+)', data.decode('utf-8')).group(0)
            URL.append(nothing)
            global ddd
            ddd = nothing
            print(ddd)
            return True
        else:
            print('结束')
            return False

while openUrl(ddd):
    time.sleep(1)
    print('第%s次链接'%(i,))
    i += 1


# 爬的过程中 有一些小 手段 ，需要 调整 手段，具体的是到 结束的页面去看提示
# 最后的答案是 peak.html







