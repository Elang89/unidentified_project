from flask import Config
from flask_injector import request
from injector import inject, Module
from pymongo import MongoClient

class MongoClientModule(Module):
    """MongoClientModule is a class that extends Module from
    inject. It is used to create a MongoClient
    
    Arguments:
        Module {Module} -- injector Module class
    """
    
    def configure(self, binder):
        binder.bind(MongoClient,
            to=self.create, 
            scope=request)
    @inject
    def create(self, config: Config):
        return MongoClient(config['MONGO_URI'])