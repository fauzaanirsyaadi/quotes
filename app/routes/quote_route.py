from flask import Blueprint, jsonify, request
from ..models.quotes import Quotes
from ..controllers.quote_controller import QuoteController
from ..utils.token_required import token_required
from app import limiter


quote = Blueprint('quote', __name__)

@quote.route('/fetch/<id>', methods=['GET'])
@token_required
def fetch_by_id(id):
  return QuoteController.fetch_by_id(id=id)


@quote.route('/fetch/all', methods=['GET'])
@token_required
def fetch_all():
  return QuoteController.fetch_all()


@quote.route('/fetch/qod', methods=['GET'])
@limiter.limit("5 per day")
def fetch_qod():
  return QuoteController.fetch_qod()


@quote.route('/create', methods=['POST'])
@token_required
def create():
  data = request.get_json()
  return QuoteController.create(data=data)


@quote.route('/update', methods=['PUT'])
@token_required
def update():
  data = request.get_json()
  return QuoteController.update(data=data)


@quote.route('/delete/<id>', methods=['DELETE'])
@token_required
def delete(id):
  return QuoteController.delete(id=id)

