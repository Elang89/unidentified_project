import os


class Config(object):
    """Config object for app configuration
    Arguments:
        object {object} -- default python object type
    """
    DEBUG = False
    SECRET = os.getenv('SECRET')
    MONGO_DATABASE_URI = os.getenv('DATABASE_URL')


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
    MONGO_DATABASE_URI = 'postgresql://localhost/test_db'
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
