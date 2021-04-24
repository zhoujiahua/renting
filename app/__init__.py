#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask
from flask_cors import CORS
from app.models.user import db


def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    CORS(app, supports_credentials=True)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    db.init_app(app)
    db.create_all(app=app)

    return app


def register_blueprint(app):
    # Web Main view
    from app.web.main.main import web_main
    app.register_blueprint(web_main)

    # Web Admin view
    from app.web.admin.admin import web_admin
    app.register_blueprint(web_admin)

    # Api register
    from app.api.user import api_user
    from app.api.comm import api_comm
    app.register_blueprint(api_user)
    app.register_blueprint(api_comm)
