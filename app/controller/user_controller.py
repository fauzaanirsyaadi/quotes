from flask import jsonify
from ..models.user import Users
from app import db

class UserController:

  @staticmethod
  def user_by_id(id):
    quote = Users()
    fetch_user = quote.query.filter_by(users_id=id).first()

    return jsonify({
      'users_id': fetch_user.users_id,
      'users_name': fetch_user.users_name,
      'users_email': fetch_user.users_email,
      'users_password': fetch_user.users_password,
    }), 200

  @staticmethod
  def user_all():
    return jsonify([
      {
      'users_id': fetch_user.users_id,
      'users_name': fetch_user.users_name,
      'users_email': fetch_user.users_email,
      'users_password': fetch_user.users_password
      } for fetch_user in Users.query.all()
    ]), 200


  @staticmethod
  def signup(data):
    if len(data['user_name']) < 4:
      return jsonify({
        'error': 'Bad Request',
        'message': 'quote must be contain minimum of 4 letters'
      }), 400

    quote = Users(
      user_name=data['user_name'],
      users_email= data['users_email'],
      users_password= data['users_password']
      )

    db.session.add(quote)
    db.session.commit()

    return jsonify({
      'users_id': quote.users_id, 
      'users_name': quote.users_name,
      'users_email': quote.users_email,
      'users_password': quote.users_password
    }), 200


  @staticmethod
  def update(data):
    quote = Users.query.filter_by(users_id=data['id']).first()
    if 'quotes_value' in data:
      quote.user_name=data['user_name'],
      quote.users_email= data['users_email'],
      quote.users_password= data['users_password']

    db.session.commit()
    return jsonify({
      'message': 'data has been updated',
      'users_id': quote.users_id,
      'users_name': quote.users_name,
      'users_email': quote.users_email,
      'users_password': quote.users_password
    }), 200

  @staticmethod
  def delete(id):
    quote = Users.query.filter_by(users_id=id).first()
    db.session.delete(quote)
    db.session.commit()

    return jsonify({
      'message': 'data has been deleted'
    }), 200
