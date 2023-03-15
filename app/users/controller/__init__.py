from flask import Blueprint, jsonify, request

from app.users.schemas import UserSchema
from app.users.services import UserService
from shared import validate_request_data

user_api = Blueprint('user_api', __name__, url_prefix='/api/v1/users')


@user_api.route('', methods=['POST'])
def create_user():
    violations, data = validate_request_data(UserSchema(), request.json)

    if violations:
        return jsonify(violations), 422

    return jsonify({
        'item': UserService.create(data).to_json()
    }), 201
