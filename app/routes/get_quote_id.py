from app import app
from flask import jsonify
from ..models.quotes import quotes

@app.route('/get_quote_id/')
def get_quote_id():

    return jsonify([
        {
            'quotes id': user.quotes_id, 
			'quotes value': user.quotes_value, 

            } for user in quotes.query.all()
    ])