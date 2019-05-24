
from os import getenv


class Config(object):
    """Config object for app configuration
    Arguments:
        object {object} -- default python object type
    """
    DEBUG = False
    MONGO_HOSTNAME = getenv('MONGO_HOSTNAME')
    MONGO_USER = getenv('MONGO_USER')
    MONGO_PASSWORD = getenv('MONGO_PASSWORD')
    MONGO_PORT = getenv('MONGO_PORT')
    MONGO_DATABASE = getenv('MONGO_DATABASE')


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
