from flask import jsonify
from ..models.quotes import Quotes
import random
from app import db

class QuoteController:

  @staticmethod
  def fetch_by_id(id):
    quote = Quotes()
    fetch_quote = quote.query.filter_by(quotes_id=id).first()

    return jsonify({
      'quotes_id': fetch_quote.quotes_id,
      'quotes_value': fetch_quote.quotes_value
    }), 200

  @staticmethod
  def fetch_all():
    return jsonify([
      {
        'quotes_id': fetch_quote.quotes_id,
        'quotes_value': fetch_quote.quotes_value
      } for fetch_quote in Quotes.query.all()
    ]), 200

  @staticmethod
  def fetch_qod():
    fetch_quotes = Quotes.query.all()
    count_quotes = len(fetch_quotes)
    qod = fetch_quotes[random.randint(0, count_quotes-1)]
    return jsonify({
      'quotes_id': qod.quotes_id,
      'quotes_value': qod.quotes_value
    }), 200

  @staticmethod
  def create(data):
    if len(data['quotes_value']) < 4:
      return jsonify({
        'error': 'Bad Request',
        'message': 'quote must be contain minimum of 4 letters'
      }), 400

    quote = Quotes(quotes_value=data['quotes_value'])
    db.session.add(quote)
    db.session.commit()

    return jsonify({
      'quotes_id': quote.quotes_id, 
      'quotes_value': quote.quotes_value
    }), 200

  @staticmethod
  def update(data):
    quote = Quotes.query.filter_by(quotes_id=data['id']).first()
    if 'quotes_value' in data:
      quote.quotes_value=data['quotes_value']

    db.session.commit()
    return jsonify({
      'message': 'data has been updated',
      'quotes_id': quote.quotes_id,
      'quotes_value' : quote.quotes_value
    }), 200

  @staticmethod
  def delete(id):
    quote = Quotes.query.filter_by(quotes_id=id).first()
    db.session.delete(quote)
    db.session.commit()

    return jsonify({
      'message': 'data has been deleted'
    }), 200
