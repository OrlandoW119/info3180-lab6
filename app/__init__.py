from flask import Flask
from flask,sqlalchemy import sqlalchemy
from .config import config


app= Flask(__name__)
db=SQLAlchemy(app)


app.config.from_object(Config)
from app import views