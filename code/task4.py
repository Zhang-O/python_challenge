#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request as ur
import re, time, socket, urllib.error

timeout = 20
socket.setdefaulttimeout(timeout)

baseUrl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
URL = []
ddd = '12345'
i = 1
def openUrl(num):
    try:
        with ur.urlopen(baseUrl+num) as f:
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
    except UnicodeDecodeError as e:
        print('-----UnicodeDecodeError url:', num)
    except urllib.error.URLError as e:
        print("-----urlError url:", num)
    except socket.timeout as e:
        # openUrl(num)
        print("-----socket timout:", num)


while openUrl(ddd):
    time.sleep(10)
    print('第%s次链接'%(i,))
    i += 1


# 爬的过程中 有一些小 手段 ，需要 调整 手段，具体的是到 结束的页面去看提示
# 爬的过程中 经常会出新 timeout 错误 ，可以写一个处理错误的函数，也可以把 后面的结果作为起点赋值给ddd
# 最后的答案是 peak.html







