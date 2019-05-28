from peewee import MySQLDatabase
from meme_maestro_backend.config import config

config = config()
print(config['database.name'])
database = MySQLDatabase(config['database.name'],
                         user=config['database.user'],
                         password=config['database.password'],
                         host=config['database.host'])
if __name__ == '__main__':
    from .model import  *
    models = [UserModel]
    database.connect()
    database.create_tables([UserModel])