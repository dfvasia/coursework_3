from flask import request
from flask_restx import Resource, Namespace

from app.dao.models.movie import MovieSchema, Movie
from app.tools.auth import login_required, admin_required
from container import movie_service

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    @login_required
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        if director_id is not None or genre_id is not None:
            temp_dict = {'director_id': director_id, 'genre_id': genre_id}
            movie = movie_service.found_film(temp_dict)
            return MovieSchema(many=True).dump(movie), 200
        all_movies = movie_service.get_all()
        return MovieSchema(many=True).dump(all_movies), 200

    @admin_required
    def post(self):
        reg_json = request.json

        s = movie_service.create(reg_json)
        s_t = f"/director/{s}"
        return "", 201, {'location': s_t}


@movies_ns.route('/<int:mid>')
class MoviesView(Resource):
    @login_required
    def get(self, mid: int):
        movie = movie_service.get_one(mid)

        return MovieSchema().dump(movie), 200

    @admin_required
    def put(self, mid):
        reg_json = request.json
        reg_json["id"] = mid

        movie_service.get_update(reg_json)

        return "", 204

    @admin_required
    def patch(self, mid):
        reg_json = request.json
        reg_json["id"] = mid

        movie_service.get_update_partial(reg_json)

        return "", 204

    @admin_required
    def delete(self, mid: int):
        movie_service.delete(mid)

        return "", 204
