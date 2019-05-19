from flask import Flask, jsonify
from flask_restplus import Api

from instance.config import app_config
from app.subscribers.controller import subscribers_controller



def create_app(config_name):
    api = Api()
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.register_blueprint(subscribers_controller)

    api.init_app(app)
    return app
