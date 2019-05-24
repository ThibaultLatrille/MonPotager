from flask import Flask, g
import sys
import psycopg2

sys.path.append('../..')
import config

app = Flask(__name__)
app.jinja_env.globals['STATIC_URL'] = config.STATIC_URL


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'db'):
        g.pg = psycopg2.connect("dbname='"+config.DB_NAME+"' user='"+config.DB_USER+"' host='"+config.DB_HOST+"' password='"+config.DB_PASSWORD+"'")
        g.db = g.pg.cursor()
    return g.db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'pg'):
        g.pg.close()

from . import views
