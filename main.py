import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_restplus import Api
from flask_pymongo import PyMongo

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


if __name__ == '__main__':
    load_dotenv(verbose=True)
    config_name = os.getenv('APP_SETTINGS')
    port = os.getenv('ENV_PORT')
    app = create_app(config_name)
    app.run(port = port)
