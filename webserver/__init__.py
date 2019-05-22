from flask import Flask
import sys

sys.path.append('../..')
import config

app = Flask(__name__)
app.jinja_env.globals['STATIC_URL'] = config.STATIC_URL

from . import views
