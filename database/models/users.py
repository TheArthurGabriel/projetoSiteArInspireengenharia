from peewee import Model, CharField, TextField, DateField
from database.database import db

class Users(Model):
    nome = CharField(unique=True)
    senha=CharField()
    
    class Meta:
        database = db
