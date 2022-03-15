import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    SECRET = 't=ab2sw=$hlYLTu7HL73'

    JSON_AS_ASCII = False

    ITEMS_PER_PAGE = 12

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ACCESS_TOKEN_EXPIRATION = 10  # minutes
    REFRESH_TOKEN_EXPIRATION = 30  # days

    PWD_HASP_SALT = '9aKOpRedO2hov*cr9*U!'.encode('utf-8')
    PWD_HASP_ITERATIONS = 100_000


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(BASEDIR), 'movies.db')
