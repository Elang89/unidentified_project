import os

from dotenv import load_dotenv
from app import create_app


if __name__ == '__main__':
    load_dotenv(verbose=True)
    config_name = os.getenv('APP_SETTINGS')
    port = os.getenv('ENV_PORT')
    app = create_app(config_name)
    app.run(port = port)
