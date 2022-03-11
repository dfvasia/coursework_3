from flask import request
from flask_restx import Resource, Namespace

from app.dao.models.director import DirectorSchema
from app.tools.auth import login_required, admin_required
from container import director_service

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    @login_required
    def get(self):
        all_directors = director_service.get_all()

        return DirectorSchema(many=True).dump(all_directors), 200

    @admin_required
    def post(self):
        reg_json = request.json

        s = director_service.create(reg_json)
        s_t = f"/director/{s}"
        return "", 201, {'location': s_t}


@directors_ns.route('/<int:did>')
class DirectorsView(Resource):
    @login_required
    def get(self, did: int):
        director = director_service.get_one(did)

        return DirectorSchema().dump(director), 200

    @admin_required
    def put(self, did):
        reg_json = request.json
        reg_json["id"] = did

        director_service.get_update(reg_json)

        return "", 204

    @admin_required
    def patch(self, did):
        reg_json = request.json
        reg_json["id"] = did

        director_service.update_partial(reg_json)

        return "", 204

    @admin_required
    def delete(self, did: int):
        director_service.delete(did)

        return "", 204


