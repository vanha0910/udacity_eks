import logging
import os

# from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# load_dotenv()

db_username = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]
db_host = os.environ.get("DB_HOST", "127.0.0.1")
db_port = os.environ.get("DB_PORT", "5432")
db_name = os.environ.get("DB_NAME", "postgres")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

db = SQLAlchemy(app)

app.logger.setLevel(logging.DEBUG)
