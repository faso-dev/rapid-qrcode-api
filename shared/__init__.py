from flask_marshmallow import Marshmallow
from marshmallow import ValidationError

ma = Marshmallow()
BaseSchema = ma.Schema


def validate_request_data(schema, request_data, partial=False):
    try:
        data = schema.load(request_data, partial=partial)
        return None, data
    except ValidationError as err:
        return {
            'success': False,
            'violations': err.messages,
            'message': 'Les données de la requête ne sont pas valides'
        }, None
