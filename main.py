import os

from dotenv import load_dotenv
from flask import Flask
from flask_restplus import Api

from instance.config import app_config

def create_app(config_name): 
    api = Api()
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    api.init_app(app)

    return app


if __name__ == '__main__':
    load_dotenv(verbose=True)
    config_name = os.getenv('APP_SETTINGS')

    app = create_app(config_name)
    app.run(debug=True)
