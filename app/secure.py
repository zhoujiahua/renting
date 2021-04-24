#!/usr/bin/python3
# -*- coding: UTF-8 -*-

config = {
    "MYSQL": "mysql",
    "CYMSQL": "cymysql",
    "ACCOUNT": "topy",
    "PASSWORD": "123456",
    "ADDRESS": "192.168.0.5",
    "PORT": 3306,
    "DATABASENAME": "topy"
}

# SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://topy:123456@10.150.253.30:3306/topy'
# SQLALCHEMY_DATABASE_URI = '{MYSQL}+{CYMSQL}://{ACCOUNT}:{PASSWORD}@{ADDRESS}:{PORT}/{DATABASENAME}'.format(**config)

# 为True时，flask-sqlalchemy会跟踪对象的修改
SQLALCHEMY_TRACK_MODIFICATIONS = True
