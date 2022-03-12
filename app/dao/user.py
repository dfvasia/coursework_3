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

    def get_by_user_email(self, email: str) -> Optional[User]:
        return self.session.query(User).filter(User.email == email).one_or_none()

    def update_role(self, email: str, role: str):
        if role not in self._roles:
            raise IncorrectData
        user = self.get_by_user_email(email)
        user.role = role
        return self.db_update(user)

    def write_refresh_token(self, email: str, refresh_token: str):
        user = self.get_by_user_email(email)
        user.refresh_token = refresh_token
        return self.db_update(user)

    def update_password(self, email: str, password_hash: str):
        user = self.get_by_user_email(email)
        user.password = password_hash
        return self.db_update(user)

    def get_one(self, uid) -> Optional[User]:
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def create(self, data):
        try:
            user = User(**data)
            return self.db_update(user)
        except sqlalchemy.exc.IntegrityError:
            raise DuplicateError

    def delete(self, uid):
        user = self.get_one(uid)
        self.db_update(user)
