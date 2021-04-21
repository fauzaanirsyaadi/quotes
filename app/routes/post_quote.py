from app import app
from flask import jsonify, request
from ..models.quotes import quotes
from app import db

@app.route('/post_quote/', methods=['POST'])
def post_quote():
	data = request.get_json()
	if len(data['quotes_value']) < 4:
		return jsonify({
			'error': 'Bad Request',
			'message': 'quote must be contain minimum of 4 letters'
		}), 400
	u = quotes(
			quotes_value=data['quotes_value'], 
		)
	db.session.add(u)
	db.session.commit()
	return {
        'quotes_id': u.quotes_id, 'quotes value': u.quotes_value
    }, 201
 