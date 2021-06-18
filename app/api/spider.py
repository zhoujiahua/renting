#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
from flask import jsonify
from . import api_spider
from uuid import uuid4
import requests


@api_spider.route("/api/spider/splist")
def api_spider_splist():
    try:
        ids = uuid4()
        url = "https://xa.58.com/chuzu/?PGTID=%s&ClickID=2" % ids
        r = requests.get(url)
        r.encoding = "utf-8"
        html = r.text
        # bs = BeautifulSoup(html, "html.parser")

        if r.status_code == 200:
            return jsonify({
                "id": ids,
                "success": True,
                "result": html
            }), 200

        return None
    except Exception as e:
        print(e)
