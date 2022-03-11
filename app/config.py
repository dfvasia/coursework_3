class Config(object):
    DEBUG = True
    SECRET = 't=ab2sw=$hlYLTu7HL73'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ACCESS_TOKEN_EXPIRATION = 10  # minutes
    REFRESH_TOKEN_EXPIRATION = 30  # days
    PWD_SALT = '9aKOpRedO2hov*cr9*U!'.encode('utf-8')
    PWD_ITERATIONS = 100_000
