from app import app
from flask import jsonify
from ..models.quotes import quotes

@app.route('/get_quote_id/<id>')
def get_quote_id(id):
    quote = quotes.query.filter_by(quotes_id=id).first_or_404()
    return{
        'quotes id': quote.quotes_id, 
        'quotes value': quote.quotes_value, 

        }