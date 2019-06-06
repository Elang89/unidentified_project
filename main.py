
#!/usr/bin/env python

from dotenv import load_dotenv
from flask_injector import FlaskInjector
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, Blueprint, Flask
from os import getenv

from app.subscribers.model import Subscriber
from app.subscribers.controller import subscribers_controller
from instance.config import app_config

load_dotenv(verbose=True)
config_name = getenv('FLASK_ENV')
port = getenv('ENV_PORT')
application = Flask(__name__, instance_relative_config=True)
application.config.from_object(app_config[config_name])
application.config.from_pyfile('config.py')
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(application)


@application.route('/', methods=['GET'])
def root():
    return jsonify(test='works')


application.register_blueprint(subscribers_controller)


if __name__ == '__main__':
    application.run(port=port, host='0.0.0.0')
