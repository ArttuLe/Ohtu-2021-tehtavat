from entities.user import User
import re
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if len(username) < 3:
            raise UserInputError("Username too short")

        if re.match("^[a-z]+$", username) is None:
            raise UserInputError("Username must contain only letters")

        if len(password) < 8:
            raise UserInputError("Password too short")
        
        if password_confirmation != password:
            raise UserInputError("Wrong confirmation password")

        if re.match("^[a-z]+$", password) is not None:
            raise UserInputError("Password must contain numbers and letters")

        if self._user_repository.find_by_username(username) is not None:
            raise UserInputError("Username already taken")
        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa


user_service = UserService()
