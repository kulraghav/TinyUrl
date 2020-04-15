import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
 
 
class Config(object):
   """
   Set Flask configuration vars from .env file
   """
 
   DB_HOST = os.getenv('DB_HOST')
   DB_USER = os.getenv('DB_USER')
   DB_PASSWORD = os.getenv('DB_PASSWORD')
   DB_NAME = os.getenv('DB_NAME')
 
   # Database
   SQLALCHEMY_DATABASE_URI = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
   SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
