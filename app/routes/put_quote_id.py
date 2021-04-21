from app import app, db
from ..models.quotes import quotes
from flask import request, jsonify

@app.route('/put_quote_id/<id>/',methods=['PUT'])
def put_quote_id(id):
    data = request.get_json()
    q = quotes.query.filter_by(quotes_id=id).all()
    if 'quotes_value' in data:
        q.quotes_value=data['quotes_value']
    db.session.commit()    
    return jsonify({
        'Success': 'data has been updated',
        'quotes_value' : q.quotes_value
    })
