#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from flask import render_template
from . import web_admin


@web_admin.route('/admin')
def admin_index():
    return render_template('admin/admin.html')
