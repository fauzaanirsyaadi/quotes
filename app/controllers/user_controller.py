from flask import Flask, render_template, request, redirect, url_for, flash
from flask import jsonify, make_response
from ..models.user import Users
from app import db
import os
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine
from sqlalchemy.sql import text

connect_str = 'postgresql://postgres:admin@localhost:5432/quotes'
engine = create_engine(connect_str, echo=False)

class UserController:

  def get_users():
    response = jsonify([
        {
            'user_id': raw.user_id, 
            'users_name': raw.users_name, 
            'users_email' : raw.users_email,
            } for raw in Users.query.all()
    ]) 
    return response

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
  def get_users_by_offset_limit():#pagination
    offset = request.args.get("offset")
    limit = request.args.get("limit")
    
    all = []
    with engine.connect() as connection:
        qry = text("SELECT * FROM users OFFSET {}  LIMIT {}".format(offset, limit))
        result = connection.execute(qry)
        for item in result:
            all.append({
                'user_id': item[0],
                'users_name': item[1],
                'users_email' : item[2]
            })
    return {'data': all, 'total': len(list(all))}

  @staticmethod
  def search_user(users_name):
    all = []
    with engine.connect() as connection:
        qry = text("SELECT * FROM users WHERE users_name ILIKE'%{}%' ORDER BY name".format(users_name))
        result = connection.execute(qry)
        for item in result:
            all.append({
                'user_id': item[0],
                'users_name': item[1],
                'users_email' : item[2]
            })
    return jsonify(all)

  @staticmethod
  def sort_user_name():
    offset = request.args.get("offset")
    limit = request.args.get("limit")
    
    all = []
    with engine.connect() as connection:
        qry = text("SELECT * FROM users ORDER BY users_name OFFSET {} LIMIT {}".format(offset, limit))
        result = connection.execute(qry)
        for item in result:
            all.append({
                'user_id': item[0],
                'users_name': item[1],
                'users_email' : item[2]
            })
    return jsonify(all)

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
          str(os.environ.get("SECRET_KEY")), 
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
