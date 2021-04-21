from app import app
from flask import jsonify
from ..models.quotes import quotes

@app.route('/get_quote/')
def get_quote():

    return jsonify([
        {
            'quotes id': s.quotes_id, 
			'quotes value': s.quotes_value

            } for s in quotes.query.all()
    ])