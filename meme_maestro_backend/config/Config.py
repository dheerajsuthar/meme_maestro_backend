from configparser import ConfigParser
from pathlib import Path

# TODO: find better solution for project base path
CONFIG_PATH = Path(__file__).parent / 'app.ini'
CONFIG_ENV = 'development'


def config():
    config = ConfigParser()
    config.read(CONFIG_PATH)
    return config[CONFIG_ENV]
