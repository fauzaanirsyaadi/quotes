from app import db 
from datetime import datetime

class Quotes(db.Model):
    quotes_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    quotes_value = db.Column(db.String(1000), nullable=False, unique=True)
    
    def __repr__(self):
        return f'Quotes<{self.quotes_value}>'
        
