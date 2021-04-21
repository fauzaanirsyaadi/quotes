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
from app.routes import delete_quote_id
from app.routes import get_quote_id
from app.routes import get_quote_of_the_day
from app.routes import get_quote
from app.routes import post_quote
from app.routes import put_quote_id

#models
from .models.quotes import quotes
