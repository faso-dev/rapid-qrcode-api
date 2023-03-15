from app.users.models import User
from database import get_session
from utils import generate_access_code


class UserService:
    """
    User service class
    """

    @staticmethod
    def all() -> list[User]:
        """
        Get all users
        This method is used to get all users.

        :return: The list of users
        """
        return User.query.all()

    @staticmethod
    def create(data: dict) -> User:
        user = User(**data)
        user.access_code = generate_access_code()
        get_session().add(user)
        get_session().commit()

        return user

    @staticmethod
    def get_by_access_code(access_code: str) -> User | None:
        """
        Get user by access code
        This method is used to get a user by access code.

        :param access_code: The access code of the user
        :return: The user
        """
        return User.query.filter_by(access_code=access_code).first()

    @staticmethod
    def invalidate_access_code(user: User) -> User:
        """
        Invalidate access code
        This method is used to invalidate an access code.

        :param user: The user
        :return: The user
        """
        user.access_code = None
        get_session().commit()

        return user
