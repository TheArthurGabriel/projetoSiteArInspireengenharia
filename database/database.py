import os
from peewee import PostgresqlDatabase
from dotenv import load_dotenv

load_dotenv()

# db = SqliteDatabase('laudos.db')
db = PostgresqlDatabase(os.getenv('DATABASE_URI', ''))