from database import BaseModel, db


class User(BaseModel):
    """
    User model
    """

    __tablename__ = 'users'

    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    access_code = db.Column(db.String(10), nullable=True, unique=True, default=None)

    def __repr__(self):
        return '<User %r>' % self.id

    def to_json(self):
        """
        Convert the model to a json object.

        :return: The model as a json object.
        """
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'access_code': self.access_code,
            'created_at': self.created_at,
        }
