# app.py

from flask import Flask
from flask_restx import Api

from app.config import Config
from app.database import db
from app.views.director import directors_ns
from app.views.genres import genres_ns
from app.views.movies import movies_ns
from app.views.user import user_ns  # users_ns
from app.views.auth import auth_ns


# def create_app(config: Config) -> Flask:
#     application = Flask(__name__)
#     application.config.from_object(config)
#     application.app_context().push()
#
#     return application


# def configure_app(application: Flask):
    # db.init_app(application)
    # api = Api(app)
    # api.add_namespace(movies_ns)
    # api.add_namespace(genres_ns)
    # api.add_namespace(directors_ns)
    # api.add_namespace(user_ns)
    # # api.add_namespace(users_ns)
    # api.add_namespace(auth_ns)


# if __name__ == '__main__':
# app_config = Config()
# app = create_app(app_config)
# configure_app(app)
# app.run()

from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from app.config import DevelopmentConfig
from app.database import db
from app.views.auth import auth_ns
from app.views.director import directors_ns
from app.views.genres import genres_ns
from app.views.movies import movies_ns
from app.views.user import user_ns

api = Api(
    authorizations={
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorizations'},
    title='Flask Course Project 3',
    doc='/docs'
)

# Нужно для работы с фронтендом
cors = CORS()


def create_app(config: [DevelopmentConfig]) -> Flask:
    try:
        # Создание Flask
        application = Flask(__name__)
        application.config.from_object(config)

        cors.init_app(application)
        db.init_app(application)
        api.init_app(application)

        # Регистрация эндпоинтов
        api.add_namespace(movies_ns)
        api.add_namespace(genres_ns)
        api.add_namespace(directors_ns)
        api.add_namespace(user_ns)

        # api.add_namespace(users_ns)
        api.add_namespace(auth_ns)

        return application
    except ImportError as e:
        print(e)
