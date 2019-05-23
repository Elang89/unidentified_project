from injector import inject
from flask import Blueprint, request, jsonify
from pymongo import MongoClient


MIMETYPE = 'application/json'
subscribers_controller = Blueprint('subscribers', __name__, url_prefix='/subscribers')

@subscribers_controller.route('/add', methods=['POST'])
@inject
def add_subscriber(mongo_client: MongoClient):
    """create_subscriber receives a json with data
    to add a new subscriber.

    Returns:
        Response - an HttpResponse with a success or failure 
        code depending on the result of the add operation.
    """
    
    data = {'name': 'Wilson', 'age': 'something'}
    db = mongo_client.plpdb
    db.subscribers.insert(data)
    return jsonify(status="Ok", statusCode=200)
