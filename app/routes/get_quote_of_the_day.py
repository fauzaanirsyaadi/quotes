from app import app
from flask import jsonify
from ..models.quotes import quotes

@app.route('/get_quote/')
def get_quote():

    return jsonify([
        {
            'quotes id': user.quotes_id, 
			'quotes value': user.quotes_value

            } for user in quotes.query.all()
    ])

# SELECT < column_name > FROM < table_name >
# ORDER BY RAND()
# select.order_by(func.random())