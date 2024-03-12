from peewee import Model, CharField, TextField, DateField
from database.database import db

class Laudo(Model):
    codigo = CharField(max_length=5)
    tecnico = CharField()
    date = DateField()
    tipo = CharField()
    descricao = TextField()
    
    class Meta:
        database = db
