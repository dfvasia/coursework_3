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

    def get_by_name(self, username: str) -> Optional[User]:
        return self.dao.get_by_username(username)

    def create(self, username, password):
        return self.dao.create({"username": username, "password": password, "password_hash": get_password_hash(password), "role_id": 1
        })


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
