from dotenv import load_dotenv
from flask_restplus import Api
from flask_injector import FlaskInjector
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
from os import getenv

from app.subscribers.controller import subscribers_controller
from app.subscribers.model import Subscriber
from instance.config import app_config


load_dotenv(verbose=True)
config_name = getenv('FLASK_ENV')
port = getenv('ENV_PORT')

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config[config_name])
app.config.from_pyfile("config.py")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(subscribers_controller)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
