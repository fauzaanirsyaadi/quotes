#ini adalah file pertama yang akan dibaca
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import flask_login

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'super secret string' 
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.routes.quote_route import quote
app.register_blueprint(quote, url_prefix='/quote')

#models
from .models.quotes import Quotes

if __name__=='__main__':
  app.run(debug=True)
