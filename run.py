import sys
sys.path.append('..')
import config
from webserver import app

if __name__ == '__main__':
    app.run(host = config.WEB_HOST, port = config.WEB_PORT, threaded = True, debug=True)

