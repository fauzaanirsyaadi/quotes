#ini adalah file pertama yang akan dibaca
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#quote
from app.routes.quote_route import quote
app.register_blueprint(quote, url_prefix='/quote')

#user
from app.routes.quote_route import quote
app.register_blueprint(quote, url_prefix='/quote')

#models
from .models.quotes import Quotes

if __name__=='__main__':
  app.run(debug=True)
