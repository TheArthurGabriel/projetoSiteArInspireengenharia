import os
from peewee import PostgresqlDatabase
from dotenv import load_dotenv

load_dotenv()

db = PostgresqlDatabase('postgresql://ajxnzfay:hcCy9Gm6VkTGkL5-F3O65WW_4UQ159ie@kesavan.db.elephantsql.com/ajxnzfay')