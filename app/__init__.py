from flask import Flask
from flask.ext import sqlalchemy

app = Flask(__name__)
app.config.from_object('config')
db = sqlalchemy.SQLALchemy(app)

from app import views, models
