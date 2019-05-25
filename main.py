from dotenv import load_dotenv
from flask_restplus import Api
from flask_injector import FlaskInjector
from flask import Flask, jsonify
from os import getenv

from app.providers import MongoDatabaseModule
from app.subscribers.controller import subscribers_controller
from instance.config import app_config



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
    app.config.from_pyfile('config.py')
    default_injector_modules = dict(mongo_client = MongoDatabaseModule())
        
    app.register_blueprint(subscribers_controller)
    
    FlaskInjector(app = app, modules = default_injector_modules.values())

    api.init_app(app)
    return app


if __name__ == '__main__':
    load_dotenv(verbose=True)
    config_name = getenv('APP_SETTINGS')
    port = getenv('ENV_PORT')
    app = create_app(config_name)
    app.run(port=port)

