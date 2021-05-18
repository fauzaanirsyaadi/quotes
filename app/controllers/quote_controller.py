from flask import Flask, render_template, request, redirect, url_for, flash
from flask import jsonify, make_response
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from ..models.quotes import Quotes
import random
from app import db

connect_str = 'postgresql://postgres:admin@localhost:5432/quote'
engine = create_engine(connect_str, echo=False)

class QuoteController:

  @staticmethod
  def index():
    return render_template('index.html')

  @staticmethod
  def fetch_by_id(id):
    response = make_response()

    quote = Quotes()
    fetch_quote = quote.query.filter_by(quotes_id=id).first()

    response = jsonify({
      'quotes_id': fetch_quote.quotes_id,
      'quotes_value': fetch_quote.quotes_value
    }), 200

    return response

  @staticmethod
  def fetch_all():
    response = make_response()
    quotes = Quotes.query.all()

    response = jsonify([
        {
            'quotes_id': row.quotes_id, 
            'quotes_value': row.quotes_value, 
            } for row in quotes
    ]) 

    return response

  @staticmethod
  def fetch_qod():
    response = make_response()

    fetch_quotes = Quotes.query.all()
    count_quotes = len(fetch_quotes)
    qod = fetch_quotes[random.randint(0, count_quotes-1)]
    response = jsonify({
      'quotes_id': qod.quotes_id,
      'quotes_value': qod.quotes_value
    }), 200

    return response

  @staticmethod
  def get_quotes_by_offset_limit():
    offset = request.args.get("offset")
    limit = request.args.get("limit")
    
    all = []
    with engine.connect() as connection:
        qry = text("SELECT * FROM Quotes OFFSET {}  LIMIT {}".format(offset, limit))
        result = connection.execute(qry)
        for item in result:
            all.append({
                'quotes_id': item[0],
                'quotes_value': item[1]
            })
    return {'data': all, 'total': len(list(all))}

  @staticmethod
  def search_quote(quotes_value):
    all = []
    with engine.connect() as connection:
        qry = text("SELECT * FROM Quotes WHERE quotes_value ILIKE'%{}%' ORDER BY name".format(name))
        result = connection.execute(qry)
        for item in result:
            all.append({
                'quotes_id': item[0],
                'quotes_value': item[1]
            })
    return jsonify(all)

  @staticmethod
  def sort_quotes_value():
    offset = request.args.get("offset")
    limit = request.args.get("limit")
    
    all = []
    with engine.connect() as connection:
        qry = text("SELECT * FROM Quotes ORDER BY quotes_value OFFSET {} LIMIT {}".format(offset, limit))
        result = connection.execute(qry)
        for item in result:
            all.append({
                'quotes_id': item[0],
                'quotes_value': item[1]
            })
    return jsonify(all)

  @staticmethod
  def create():
    data = request.get_json()

    quote = Quotes(quotes_value=data['quotes_value'])
    db.session.add(quote)
    db.session.commit()

    return jsonify({
      'quotes_id': quote.quotes_id, 
      'quotes_value': quote.quotes_value
    }), 201

  @staticmethod
  def update(id):
    data = request.get_json()

    quote = Quotes.query.filter_by(quotes_id=id).first()
    if 'quotes_value' in data:
      quote.quotes_value=data['quotes_value']

    db.session.commit()
    return jsonify({
      'message': 'data has been updated',
      'quotes_id': quote.quotes_id,
      'quotes_value' : quote.quotes_value
    }), 201

  @staticmethod
  def delete(id):
    quote = Quotes.query.filter_by(quotes_id=id).first()
    db.session.delete(quote)
    db.session.commit()

    return jsonify({
      'message': 'data has been deleted'
    }), 200
