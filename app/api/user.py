#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from . import api_user


@api_user.route("/api/user/login")
def api_user_login():
    return 'user login api'


@api_user.route("/api/user/register")
def api_user_register():
    return 'user register api'
