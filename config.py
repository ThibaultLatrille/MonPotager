import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ['SECRET_KEY_BASE'] if 'SECRET_KEY_BASE' in os.environ else 'dev_key'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] if 'DATABASE_URL' in os.environ else 'sqlite:///' + os.path.join(basedir, 'app.db')


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
