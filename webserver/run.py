from flask import Flask
import os, sys

sys.path.append('..')
import config

if __name__ == '__main__':
    #HOST = os.environ.get('SERVER_HOST', 'localhost')
    app = Flask(__name__)
    app.run(host = config.WEB_HOST, port = config.WEB_PORT, debug=True)
    app.jinja_env.globals['STATIC_URL'] = config.STATIC_URL

from . import views
