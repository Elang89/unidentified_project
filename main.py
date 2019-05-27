from dotenv import load_dotenv
from flask_restplus import Api
from flask_injector import FlaskInjector
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
from os import getenv

from app.subscribers.controller import subscribers_controller
from instance.config import app_config


db = SQLAlchemy()


def create_app(config_name):
    """create_app sets up the application and 
    its configuration.

    Arguments:
        config_name {str} -- type of config to be used 
        for example 'development'

    Returns:
        Flask -- default flask app object. 
    """
    api = Api()
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("config.py")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(subscribers_controller)

    api.init_app(app)
    db.init_app(app)
    return app


if __name__ == "__main__":
    load_dotenv(verbose=True)
    config_name = getenv('FLASK_ENV')
    port = getenv('ENV_PORT')
    app = create_app(config_name)
    app.run(port=port)
