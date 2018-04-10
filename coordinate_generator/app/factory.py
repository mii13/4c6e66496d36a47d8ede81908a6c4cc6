import os
from flask import Flask
from flask_restful import Api
from .resources import CoordinatesResource
from .extensions import db


config = {
    "dev": "app.conf.DevelopmentConfig",
    "testing": "app.conf.TestingConfig",
    "default": "app.conf.Config",
    "stage": "app.conf.StagingConfig",
    "prod": "app.conf.ProductionConfig"
}


def create_app():
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    db.app = app

    api = Api(app)
    api.add_resource(CoordinatesResource, '/coordinates', endpoint='coordinates')

    return app
