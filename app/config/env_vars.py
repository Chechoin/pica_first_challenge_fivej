import os

from dotenv import load_dotenv

load_dotenv("./.env", override=True)

MYSQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_TCP_PORT = os.getenv("MYSQL_TCP_PORT")
MYSQL_HOST = os.getenv("MYSQL_HOST")
DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_TCP_PORT}/{MYSQL_DATABASE}"
