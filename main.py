
#!/usr/bin/env python

from dotenv import load_dotenv
from flask_injector import FlaskInjector
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, Blueprint, Flask
from os import getenv

from app.subscribers.model import Subscriber
from app.subscribers.controller import subscribers_controller
from instance.config import app_config

main_blueprint = Blueprint('api', __name__, url_prefix='/api/')

def create_app(config_name):
    """create_app sets up the application and 
    its configuration.
    
    Arguments:
        config_name {str} -- type of config to be used 
        for example 'development'
    
    Returns:
        Flask -- default flask app object. 
    """

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    SQLAlchemy(app)

    @app.route('/', methods=['GET'])
    def root():
        return jsonify(test='works')

    app.register_blueprint(subscribers_controller)


    return app


if __name__ == '__main__':
    load_dotenv(verbose=True)
    config_name = getenv('FLASK_ENV')
    port = getenv('ENV_PORT')
    app = create_app(config_name)
    app.run(port=port, host='0.0.0.0')

