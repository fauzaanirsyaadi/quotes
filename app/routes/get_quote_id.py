import uuid
from app import app
from ..models.quotes import quotes


@app.route('/get_quote_id/<id>')
def get_quote_id(id):
    q = quotes.query.filter_by(quotes_id=id).all()
    return{
        'quotes_id': q.quotes_id, 
        'quotes_value': q.quotes_value
    }