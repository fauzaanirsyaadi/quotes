from flask import Blueprint, jsonify, request
from ..models.user import Users
from ..controllers.user_controller import UserController
from ..utils.token_required import token_required

user = Blueprint('user', __name__)


@user.route('/login', methods=['POST'])
def login():
  auth = request.get_json()
  return UserController.login(auth=auth)


@user.route('/signup', methods=['POST'])
def signup():
  data = request.get_json()
  return UserController.signup(data=data)


@user.route('/fetch/<id>', methods=['GET'])
@token_required
def fetch_by_id(id):
  return UserController.fetch_by_id(id=id)


@user.route('/update', methods=['PUT'])
@token_required
def update():
  data = request.get_json()
  return UserController.update(data=data)


@user.route('/delete/<id>', methods=['DELETE'])
@token_required
def delete(id):
  return UserController.delete(id=id)

  