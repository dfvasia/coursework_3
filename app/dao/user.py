from typing import Optional

import sqlalchemy.exc

from app.dao.models.user import User

from exceptions import IncorrectData, DuplicateError


# CRUD
class UserDAO:
    def __init__(self, session):
        self.session = session
        self._roles = {'user', 'admin'}

    def db_update(self, user):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user.id

    def get_by_username(self, username: str) -> Optional[User]:
        return self.session.query(User).filter(User.username == username).one_or_none()

    def update_role(self, username: str, role: str):
        if role not in self._roles:
            raise IncorrectData
        user = self.get_by_username(username)
        user.role = role
        return self.db_update(user)

    def update_password(self, username: str, password_hash: str):
        user = self.get_by_username(username)
        user.password = password_hash
        return self.db_update(user)

    def get_one(self, uid) -> Optional['User']:
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def create(self, data):
        try:
            print(data)
            user = User(**data)
            return self.db_update(user)
        except sqlalchemy.exc.IntegrityError:
            raise DuplicateError

    def delete(self, uid):
        user = self.get_one(uid)
        self.db_update(user)
