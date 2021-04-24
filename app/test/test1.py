#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask, current_app

app = Flask(__name__)

# ============================================
# 应用上下文 对象 Flask
# 请求上下文 对象 Request
# Flask AppContext
# Request RequestContext
# ============================================

# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# ctx.pop()

# with
# 实现上下文协议的对象使用with
# 上下文管理器
# __enter__ __exit__
# 上下文表达式必须要返回一个上下文管理器

with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']

# 1.连接数据库
# 2.sql
# 3.释放资源

# 文件读写
# try:
#     f = open(r'D:\t.txt')
# finally:
#     f.close()
