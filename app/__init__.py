#ini adalah file pertama yang akan dibaca
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#routes
from app.routes import index

#models
from .models.quotes import quotes
