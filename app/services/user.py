from typing import Optional

from app.dao.models.user import User
from app.dao.user import UserDAO
from app.tools.security import get_password_hash


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    # def get_all(self):
    #     return self.dao.get_all()

    def get_by_user_email(self, email: str) -> Optional[User]:
        return self.dao.get_by_user_email(email)

    def create(self, **user):
        return self.dao.create({"username": user["username"], "surname": user["surname"], "email": user["email"], "password_hash": get_password_hash(user["password"]), "role_id": 1})

    def write_refresh_token(self, email: str, refresh_token: str) -> Optional[User]:
        return self.dao.write_refresh_token(email, refresh_token)
        # return self.dao.get_by_user_email(username)

    # def get_update(self, data):
    #     uid = data.get("id")
    #     user = self.get_one(uid)
    #
    #     user.name = data.get("name")
    #
    #     self.dao.db_update(user)
    #
    # def update_partial(self, data):
    #     uid = data.get("id")
    #     user = self.get_one(uid)
    #
    #     if "name" in data:
    #         user.name = data.get("name")
    #     self.dao.db_update(user)
    #
    # def delete(self, uid):
    #     self.dao.delete(uid)
