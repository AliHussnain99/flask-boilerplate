import logging
import os

from core.settings import app
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(app.root_path, 'env', 'local', '.env'))


def get_env_variable(key):
    try:
        value = os.environ[key]
        if value.lower() == 'true':
            return True
        elif value.lower() == 'false':
            return False
        else:
            try:
                return int(value)
            except ValueError:
                return value
    except KeyError:
        app.logger.error(f"ENVIRONMENT VARIABLE: {key} is not set. Please set the environment in the env file.")
        raise KeyError(key)


def get_db_url():
    db_engine = get_env_variable('DATABASE_ENGINE')
    db_name = get_env_variable('DATABASE_NAME')
    db_user = get_env_variable('DATABASE_USER')
    db_password = get_env_variable('DATABASE_PASSWORD')
    db_host = get_env_variable('DATABASE_HOST')
    db_port = get_env_variable('DATABASE_PORT')
    app.logger.info(f"{db_engine}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
    return f"{db_engine}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"


def initiate_logging(app):
    # LOGGING CONFIGURATIONS ON THE BASIS OF ENV
    app.logger.setLevel(logging.DEBUG if get_env_variable('FLASK_DEBUG') else logging.INFO)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(formatter)
    app.logger.addHandler(stream_handler)
