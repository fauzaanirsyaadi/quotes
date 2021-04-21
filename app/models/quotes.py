from app import db 
from datetime import datetime

class quotes(db.Model):
    quotes_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    quotes_value = db.Column(db.String(250), nullable=False)
    
    def __repr__(self):
        return f'Quotes<{self.quotes_value}>'
        
