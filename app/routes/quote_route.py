from flask import Blueprint, jsonify, request
from ..models.quotes import Quotes
from ..controller.quote_controller import QuoteController


quote = Blueprint('quote', __name__)

@quote.route('/fetch/<id>', methods=['GET'])
def fetch_by_id(id):
  return QuoteController.fetch_by_id(id=id)


@quote.route('/fetch/all', methods=['GET'])
def fetch_all():
  return QuoteController.fetch_all()


@quote.route('/fetch/qod', methods=['GET'])
def fetch_qod():
  return QuoteController.fetch_qod()


@quote.route('/create', methods=['POST'])
def create():
  data = request.get_json()
  return QuoteController.create(data=data)


@quote.route('/update', methods=['PUT'])
def update():
  data = request.get_json()
  return QuoteController.update(data=data)


@quote.route('/delete/<id>', methods=['DELETE'])
def delete(id):
  return QuoteController.delete(id=id)
