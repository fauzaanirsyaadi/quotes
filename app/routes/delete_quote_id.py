from app import app, db
from ..models.quotes import quotes

@app.route('/delete_quote_id/<id>/', methods=['DELETE'])
def delete_quote_id(id):
    q = quotes.query.filter_by(quotes_id=id).all()
    db.session.delete(q)
    db.session.commit()
    return {
        'success': 'Data deleted successfully'
    }