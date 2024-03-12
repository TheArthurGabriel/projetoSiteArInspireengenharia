import os
from peewee import PostgresqlDatabase
from dotenv import load_dotenv

load_dotenv()

# db = SqliteDatabase('laudos.db')
db = PostgresqlDatabase('postgresql://postgres:jVprGyEDnUEaZDqszKoUCCnvQJfSgJDl@postgres.railway.internal:5432/railway')