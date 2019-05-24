from injector import inject, Module
from flask import Config
from flask_injector import request
from pymongo import MongoClient
from pymongo.database import Database


class MongoDatabaseModule(Module):
    """MongoDatabaseModule is an extended class 
    from Module from the injector package.
    It will be injected into controllers to
    gain access to a mongo database.
    Arguments:
        Module {Module} -- default injector Module class
    """

    def configure(self, binder):
        """configure is an implementation of the
        Module configure function. It is used to create 
        the binder to the Database that will be used for 
        injection. 
        Arguments:
            binder {Binder} -- injector Binder class
        """
        binder.bind(Database, to=self.create, scope=request)

    @inject
    def create(self, config: Config):
        """create is the method used to create
        the Database object to be injected.
        Arguments:
            config {Config} -- [description]
        """
        client = MongoClient(
            host=config['MONGO_HOSTNAME'],
            username=config['MONGO_USER'],
            password=config['MONGO_PASSWORD'],
            port=int(config['MONGO_PORT']),
            authSource=config['MONGO_DATABASE']
        )

        return client[config['MONGO_DATABASE']]
