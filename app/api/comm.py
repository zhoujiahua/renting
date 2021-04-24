#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from flask import request, jsonify
from . import api_comm
from app.forms.search import SearchForm


@api_comm.route("/api/comm/email")
def api_comm_email():
    return 'send email api'


@api_comm.route("/api/comm/category/<key>/<sort>")
def api_comm_category(key, sort):
    return jsonify({'key': key, 'sort': sort})


@api_comm.route("/api/comm/news")
def api_comm_news():
    page = request.args['page']
    limit = request.args['limit']
    return jsonify({'page': page, 'limit': limit})


@api_comm.route("/api/comm/search")
def api_comm_search():
    form = SearchForm(request.args)
    if form.validate():
        key = form.key.data.strip()
        page = form.page.data
        return jsonify({'key': key, 'page': page})
    else:
        return jsonify(form.errors)
