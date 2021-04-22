from flask import Blueprint, jsonify, request
from ..models.user import Users
from ..controller.user_controller import UserController

quote = Blueprint('quote', __name__)

@quote.route('/fetch/<id>', methods=['GET'])
def fetch_by_id(id):
  return UserController.fetch_by_id(id=id)


@quote.route('/fetch/all', methods=['GET'])
def fetch_all():
  return UserController.fetch_all()


@quote.route('/create', methods=['POST'])
def create():
  data = request.get_json()
  return UserController.create(data=data)


@quote.route('/update', methods=['PUT'])
def update():
  data = request.get_json()
  return UserController.update(data=data)


@quote.route('/delete/<id>', methods=['DELETE'])
def delete(id):
  return UserController.delete(id=id)
