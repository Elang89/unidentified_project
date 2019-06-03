from injector import inject
from flask import request, jsonify, Blueprint



MIMETYPE = 'application/json'
subscribers_controller = Blueprint('subscribers', __name__, url_prefix='/subscribers')

@subscribers_controller.route('/add', methods=['POST'])
def add_subscriber():
    """create_subscriber receives a json with data
    to add a new subscriber.

    Returns:
        Response - an HttpResponse with a success or failure 
        code depending on the result of the add operation.
    """
    raise NotImplementedError


@subscribers_controller.route('/', methods=['GET'])
def get_subscribers():
    return jsonify(status_code=200, status='Ok', test='works')

