from marshmallow import Schema, fields

from app.database import db


class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True)
    name_role = db.Column(db.String, unique=True)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    surname = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)
    role_id = db.Column(db.String, db.ForeignKey("group.id"))
    role = db.relationship("Group")
    refresh_token = db.Column(db.String)


class Fgu(db.Model):
    __tablename__ = 'fgu'
    __table_args__ = (db.PrimaryKeyConstraint('id_user', 'id_genre'),)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    id_genre = db.Column(db.Integer, db.ForeignKey('genre.id'))
    genre = db.relationship('Genre')


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    surname = fields.Str()
    email = fields.Str()
    password_hash = fields.Str(load_only=True)
    role = fields.Str()
    role_id = fields.Int()
    refresh_token = fields.Str()


class GroupSchema(Schema):
    id = fields.Int()
    name_role = fields.Str()
