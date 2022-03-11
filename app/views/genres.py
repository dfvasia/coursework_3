
from flask import request, Response
from flask_restx import Resource, Namespace

from app.dao.models.genre import GenreSchema
from app.tools.auth import login_required, admin_required
from app.tools.jwt_token import JwtSchema
from container import genre_service

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    @login_required
    def get(self, token_data):
        all_genres = genre_service.get_all()
        return GenreSchema(many=True).dump(all_genres), 200

    @admin_required
    def post(self):
        reg_json = request.json
        s = genre_service.create(reg_json)
        s_t = f"/genres/{s}"
        return "", 201, {'location': s_t}


@genres_ns.route('/<int:gid>')
class GenresView(Resource):
    @login_required
    def get(self, gid: int):
        genre = genre_service.get_one(gid)

        return GenreSchema().dump(genre), 200

    @admin_required
    def put(self, gid):
        reg_json = request.json
        reg_json["id"] = gid

        genre_service.get_update(reg_json)

        return "", 204

    @admin_required
    def patch(self, gid):
        reg_json = request.json
        reg_json["id"] = gid

        genre_service.update_partial(reg_json)

        return "", 204

    @admin_required
    def delete(self, gid: int):
        genre_service.delete(gid)

        return "", 204
