from flask import Blueprint, jsonify, request

from app.users.services import UserService
from app.users.schemas import AccessCodeSchema
from shared import validate_request_data

qrcode_api = Blueprint('qrcode_api', __name__, url_prefix='/api/v1/qrcodes')


@qrcode_api.route('', methods=['POST'])
def check_qrcode():
    violations, data = validate_request_data(AccessCodeSchema(), request.json)

    if violations:
        return jsonify(violations), 422

    item = UserService.get_by_access_code(data['access_code'])

    if not item:
        return jsonify({
            'code': 'not_found',
            'message': 'User not found'
        }), 404

    return jsonify({
        'item': item.to_json()
    }), 200
