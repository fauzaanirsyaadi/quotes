from flask import jsonify
from ..models.user import Users
from app import db

class UserController:

  @staticmethod
  def user_by_id(id):
    user = Users()
    fetch_user = user.query.filter_by(users_id=id).first()

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
        'message': 'user must be contain minimum of 4 letters'
      }), 400

    user = Users(
      user_name=data['user_name'],
      users_email= data['users_email'],
      users_password= data['users_password']
      )

    db.session.add(user)
    db.session.commit()

    return jsonify({
      'users_id': user.users_id, 
      'users_name': user.users_name,
      'users_email': user.users_email,
      'users_password': user.users_password
    }), 200


  @staticmethod
  def update(data):
    user = Users.query.filter_by(users_id=data['id']).first()
    if 'quotes_value' in data:
      user.user_name=data['user_name'],
      user.users_email= data['users_email'],
      user.users_password= data['users_password']

    db.session.commit()
    return jsonify({
      'message': 'data has been updated',
      'users_id': user.users_id,
      'users_name': user.users_name,
      'users_email': user.users_email,
      'users_password': user.users_password
    }), 200

  @staticmethod
  def delete(id):
    user = Users.query.filter_by(users_id=id).first()
    db.session.delete(user)
    db.session.commit()

    return jsonify({
      'message': 'data has been deleted'
    }), 200
