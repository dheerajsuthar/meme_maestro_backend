from . import BaseModel
from peewee import CharField


class UserModel(BaseModel):
    name = CharField()
    password = CharField(null=False)
    email = CharField(unique=True, null=False)
