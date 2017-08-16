#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @name   : parser.py
# @author : cat
# @date   : 2017/8/16.
from bs4 import BeautifulSoup
import requeter

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

init_url, html_doc = requeter.url_text(requeter.url)


def root_url(init_url=init_url):
    init_url = str(init_url)
    index = init_url.rfind("/")
    return init_url[:index + 1]


if __name__ == '__main__':
    rp = root_url()
    print('origin url = ', rp)
    soup = BeautifulSoup(html_doc, "html.parser")
    tags = soup.find_all('tr', class_="tr3 f_one")
    print("len = ", len(tags))
    for tr in tags:
        # print(tr.th.h2)
        sub_link = tr.th.h2.a.get('href')
        # print(sub_link)
        link = rp + sub_link
        # print(link)
        print(tr.th.h2.text, link, sep=" : ", end="\n" * 2)

        # print(soup.prettify())
