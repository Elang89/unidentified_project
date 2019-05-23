from os import getenv

class Config(object):
    """Config object for app configuration
    Arguments:
        object {object} -- default python object type
    """
    MONGO_URI = 'mongodb://{user}:{password}@{host}:{port}/?authSource=admin'.format(
        user=getenv('MONGO_DATABASE_USER'),
        password=getenv('MONGO_DATABASE_PASSWORD'),
        host=getenv('MONGO_DATABASE_HOST'),
        port=getenv('MONGO_DATABASE_PORT'))
    DEBUG = False


class DevelopmentConfig(Config):
    """Development config settings
    
    Arguments:
        Config {Config} -- default config object from 
        which class inherits.
    """
    DEBUG = True


class TestingConfig(Config):
    """Testing config settings
    
    Arguments:
        Config {Config} -- default config object from
        which class inherits.
    """
    TESTING = True
    DEBUG = True


class StagingConfig(Config):
    """Staging config settings
    
    Arguments:
        Config {Config} -- default config object from
        which class inherits.
    """
    DEBUG = True


class ProductionConfig(Config):
    """Production config settings
    
    Arguments:
        Config {Config} -- default config object from 
        which class inherits.
    """
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
