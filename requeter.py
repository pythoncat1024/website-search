#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @name   : requeter.py
# @author : cat
# @date   : 2017/8/16.
# 用于网络请求，获取网页数据。 --> parser.parser(content) -->

import requests

# url = 'http://www.baidu.com'  # utf-8
url = 'https://www.t66y.com/index.php'  # gbk
params = {'encoding': 'utf-8'}
r = requests.get(url)
r.encoding = 'gbk'


def url_text(url, charset='gbk'):
    r = requests.get(url)
    print("origin encodeing = ", r.encoding)
    r.encoding = charset
    return r.url, r.text


if __name__ == '__main__':
    print('origin url = ', r.url)
    print(url_text(url))
    # print(r.text)  # ok

    pass
