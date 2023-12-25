from flask import jsonify, Blueprint, request
from app.models.user_models import get_data, create_data
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