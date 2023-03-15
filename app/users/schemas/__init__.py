from marshmallow import fields

from shared import BaseSchema


class UserSchema(BaseSchema):
    """
    User schema class
    """

    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.String(required=True)

    class Meta:
        """
        Meta class
        """

        strict = True
        fields = ('first_name', 'last_name', 'email')


class AccessCodeSchema(BaseSchema):
    """
    Access code schema class
    """

    access_code = fields.String(required=True)

    class Meta:
        """
        Meta class
        """

        strict = True
        fields = ('access_code',)
