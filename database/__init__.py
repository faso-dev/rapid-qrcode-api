from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    """
    Base model for all models.
    """
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)
    
    def to_json(self):
        """
        Convert the model to a json object.

        :return: The model as a json object.
        """
        raise NotImplementedError('You must implement the to_json method')


def get_session():
    """
    Get the current database session.

    :return: The current database session.
    """
    return db.session


def get_engine():
    """
    Get the current database engine.

    :return: The current database engine.
    """
    return db.engine


def get_metadata():
    """
    Get the current database metadata.

    :return: The current database metadata.
    """
    return db.metadata
