#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=app.config['PORT'], debug=app.config['DEBUG'], threaded=True)
