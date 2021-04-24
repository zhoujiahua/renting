#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import render_template
from bs4 import BeautifulSoup
from . import web_main
import requests


@web_main.route('/')
def main_index():
    url = 'https://xa.58.com/chuzu/'
    res = requests.get(url)
    res.encoding = 'utf-8'
    # print(res.status_code)
    html = res.content
    text = res.text
    # print(html, text)
    bs = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    house_list = bs.select('.house-list .house-cell')
    pager_wrap = bs.select('#pager_wrap .pager>a')
    house_list_len = len(house_list)
    pager_wrap_len = len(pager_wrap)
    print(house_list_len, pager_wrap[pager_wrap_len - 2])
    return render_template('main/index.html')
