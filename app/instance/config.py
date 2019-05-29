from os import getenv


def _create_connection_string(user, password, host, port, db):
    return 'postgresql://{user}:{password}@{host}:{port}/{db}'.format(
        user=user,
        password=password,
        host=host,
        port=port,
        db=db
    )


class Config(object):
    """Config object for app configuration
    Arguments:
        object {object} -- default python object type
    """

    DEBUG = True
    PG_HOSTNAME = getenv('PG_HOSTNAME')
    PG_USER = getenv('PG_USER')
    PG_PASSWORD = getenv('PG_PASSWORD')
    PG_PORT = getenv('PG_PORT')
    PG_DATABASE = getenv('PG_DATABASE')

    SQLALCHEMY_DATABASE_URI = _create_connection_string(
        user=PG_USER, password=PG_PASSWORD, host=PG_HOSTNAME, port=PG_PORT, db=PG_DATABASE)


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
