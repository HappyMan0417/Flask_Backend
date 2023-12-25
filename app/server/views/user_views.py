from flask import jsonify, Blueprint, request
from server.models.user_models import get_data, create_data, update_data_by_id, delete_data_by_id
example_blueprint = Blueprint('example', __name__)

@example_blueprint.route('/getdata', methods=['GET'])
def handle_get():
    
    records = get_data()
    results = [
        {
            "id": record.id,
            "name": record.username,
            "password": record.password
        } for record in records]

    return {"count": len(results), "records": results}
@example_blueprint.route('/createdata', methods=['POST'])
def create():
    content = request.json
    # your creation logic goes here...
    create_data(content)

    return {"message": "Successfully created!"}, 201

@example_blueprint.route('/updatedata/<userid>', methods=['PUT'])
def update_data(userid):

    content = request.json
    # your creation logic goes here...

    print(content)
    result = update_data_by_id(userid, content)

    if result is None:  # if update_data returns None, user was not found
        return {"error": "User not found", "code": 404}, 404
    else:
        return {"message": "Successfully updated!", "user": str(result), "code": 200}, 200  # Ensure your User model has a __str__ method

@example_blueprint.route('/deletedata/<int:userid>', methods=['DELETE'])
def delete_data(userid):
    result = delete_data_by_id(userid)
    if result is None:  # if delete_data returns None, user was not found
        return {"error": "User not found"}, 404
    else:
        return {"message": "Successfully deleted!"}, 200

