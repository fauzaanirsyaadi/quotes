#ini adalah file pertama yang akan dibaca
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'super secret string' 

limiter = Limiter(
  app,
  key_func=get_remote_address,
  default_limits=["200 per day", "50 per hour"]
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.routes.quote_route import quote
app.register_blueprint(quote, url_prefix='/quote')

from app.routes.user_route import user
app.register_blueprint(user, url_prefix='/user')

# models
from .models.quotes import Quotes
from .models.user import Users

if __name__=='__main__':
  app.run(debug=True)
