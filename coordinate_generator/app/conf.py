import os
from .common import CustomJSONEncoder

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "secrete_key"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@db:5432/postgres')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTFUL_JSON = {'cls': CustomJSONEncoder}


class ProductionConfig(Config):
    DEBUG = False
    # SECRET_KEY = os.environ['API_SECRET_KEY']


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
