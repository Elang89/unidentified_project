import os


class Config(object):
    """Config object for app configuration
    Arguments:
        object {object} -- default python object type
    """
    APPLICATION_ROOT = '/api/v1'
    DEBUG = False
    MONGO_URI = 'mongodb://{user}:{password}@{host}:{port}'.format(
        user = os.getenv('MONGO_DATABASE_USER'), 
        password = os.getenv('MONGO_DATABASE_PASSWORD'),
        host = os.getenv('MONGO_DATABASE_HOST'), 
        port = os.getenv('MONGO_DATABASE_PORT'))


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
    MONGO_URI = ''
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
