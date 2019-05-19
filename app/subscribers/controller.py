from flask import Blueprint, Response, request, jsonify

MIMETYPE = 'application/json'
subscribers_controller = Blueprint('subscribers', __name__, url_prefix='/subscribers')

@subscribers_controller.route('/add', methods=['POST'])
def add_subscriber():
    """create_subscriber receives a json with data
    to add a new subscriber.

    Returns:
        [Response] - an HttpResponse with a success or failure 
        code depending on the result of the add operation.
    """

    data = request.get_json()
    print(data)
    return jsonify(status="Ok", statusCode=200)