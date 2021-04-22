from flask import request, jsonify
import jwt
from ..models.user import Users
import os
from functools import wraps


def token_required(f):
  @wraps(f)
  def decorator(*args, **kwargs):
    token = None
    if 'x-access-token' in request.headers:
        token = request.headers['x-access-token']

    if not token:
        return jsonify({'message': 'a valid token is missing'})

    try:
        data = jwt.decode(token, os.environ.get("SECRET_KEY"), algorithms=["HS256"])
        current_user = Users.query.filter_by(users_id=data['users_id']).first()
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'token is invalid'})

    return f(*args, **kwargs)
  return decorator