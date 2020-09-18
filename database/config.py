from settings import *
import os

database_username = os.getenv('DATABASE_USER')
database_password = os.getenv('DATABASE_PASSWORD')
database_server = os.getenv('DATABASE_SERVER')
database_name = os.getenv('DATABASE_NAME')
url_connection = f"mysql://{database_username}:{database_password}@{database_server}/{database_name}"