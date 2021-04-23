from flask import request, jsonify
from ..models.user import Users
from app import db
import os
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class UserController:
  
  @staticmethod
  def fetch_by_id(id):
    user = Users()
    fetch_user = user.query.filter_by(users_id=id).first()

    return jsonify({
      'users_id': fetch_user.users_id,
      'users_name': fetch_user.users_name,
      'users_email': fetch_user.users_email,
    }), 200


  @staticmethod
  def login(auth):
    if not auth or not auth['email'] or not auth['password']:
      return jsonify({
        'message': 'Credentials not complete',
      }), 400

    user = Users.query.filter_by(users_email=auth['email']).first()

    if user:
      if check_password_hash(user.users_password, auth['password']):
        token = jwt.encode({
            'users_id': user.users_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24 * 7)
          }, 
          os.environ.get("SECRET_KEY"), 
          algorithm="HS256"
        )
        return jsonify({
          'users_id': user.users_id,
          'token': token
        })

    return jsonify({
      'message': 'Wrong credentials',
    }), 401


  @staticmethod
  def signup(data):
    user = Users(
      users_name=data['users_name'],
      users_email= data['users_email'],
      users_password= generate_password_hash(data['users_password'], method='sha256')
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
      'message': 'You have registered successfully',
      'users_name': user.users_name,
      'users_email': user.users_email
    }), 200


  @staticmethod
  def update(data):
    user = Users.query.filter_by(users_id=data['users_id']).first()
    if user:
      user.users_name = data['users_name'],
      user.users_email = data['users_email']
      
    if 'users_password' in data:
      user.users_password = data['users_password']

    db.session.commit()

    return jsonify({
      'message': 'data has been updated',
      'users_id': user.users_id,
      'users_name': user.users_name,
      'users_email': user.users_email
    }), 200


  @staticmethod
  def delete(id):
    user = Users.query.filter_by(users_id=id).first()
    db.session.delete(user)
    db.session.commit()

    return jsonify({
      'message': 'data has been deleted'
    }), 200
