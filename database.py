import os
import pymongo

class DB(object):
    """Database class for application
    
    Arguments:
        object {object} -- Default python object.
    """

    URI = 'mongodb://{user}:{password}@{host}:{port}'.format(
        user=os.getenv('MONGO_DATABASE_USER'),
        password=os.getenv('MONGO_DATABASE_PASSWORD'),
        host=os.getenv('MONGO_DATABASE_HOST'),
        port=os.getenv('MONGO_DATABASE_PORT'))

    @staticmethod
    def init(database):
        """init receives a database parameter
        as a string and initializes a new database.

        Arguments:
            database {string} -- the database name to initialize
        """
        client = pymongo.MongoClient(DB.URI)
        DB.DATABASE = client[database]

    @staticmethod
    def insert(collection, data):
        """insert inserts an object in to the
        database.
        
        Arguments:
            collection {Collection} -- mongodb collection object.
            data {dict} -- dictionary with mongo query.
        """
        DB.DATABASE[collection].insert(data)
    
    @staticmethod
    def find_one(collection, query):
        """find_one retrieves one object
        from the database based on the 
        query sent.
        
        Arguments:
            collection {Collection} -- mongodb collection object.
            query {dict} -- dictionary with mongo query.
        Returns:
            dict - mongodb document result.
        """
        return DB.DATABASE[collection].find_one(query)

    @staticmethod
    def find(collection, limit=50, query={}):
        """find retrieves all objects corresponding to 
        a mongodb query. 
        
        Returns:
            Cursor -- mongodb Cursor object.
        """
        return DB.DATABASE[collection].find(filter = query, limit = limit)
