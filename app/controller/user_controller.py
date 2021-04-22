from flask import jsonify
from ..models.user import Users
from app import db

class UserController:

  @staticmethod
  def fetch_by_id(id):
    quote = Users()
    fetch_user = quote.query.filter_by(users_id=id).first()

    return jsonify({
      'users_id': fetch_user.users_id,
      'quotes_value': fetch_user.quotes_value
    }), 200

  @staticmethod
  def fetch_all():
    return jsonify([
      {
        'users_id': fetch_user.users_id,
        'quotes_value': fetch_user.quotes_value
      } for fetch_user in Users.query.all()
    ]), 200


  @staticmethod
  def create(data):
    if len(data['quotes_value']) < 4:
      return jsonify({
        'error': 'Bad Request',
        'message': 'quote must be contain minimum of 4 letters'
      }), 400

    quote = Users(quotes_value=data['quotes_value'])
    db.session.add(quote)
    db.session.commit()

    return jsonify({
      'users_id': quote.users_id, 
      'quotes_value': quote.quotes_value
    }), 200

  @staticmethod
  def update(data):
    quote = Users.query.filter_by(users_id=data['id']).first()
    if 'quotes_value' in data:
      quote.quotes_value=data['quotes_value']

    db.session.commit()
    return jsonify({
      'message': 'data has been updated',
      'users_id': quote.users_id,
      'quotes_value' : quote.quotes_value
    }), 200

  @staticmethod
  def delete(id):
    quote = Users.query.filter_by(users_id=id).first()
    db.session.delete(quote)
    db.session.commit()

    return jsonify({
      'message': 'data has been deleted'
    }), 200
