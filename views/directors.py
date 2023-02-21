from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):

        page = request.args.get('page')
        directors = director_service.get_all(page)
        return DirectorSchema(many=True).dump(directors), 200

    def post(self):
        req_json = request.json
        ent = director_service.create(req_json)
        return "", 201, {"location": f"/directors/{ent.id}"}


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        return DirectorSchema().dump(director), 200

    def put(self, did):
        req_json = request.json
        req_json["id"] = did
        director_service.update(req_json)
        return "", 204

    def patch(self, did):
        req_json = request.json
        req_json["id"] = did
        director_service.partially_update(req_json)
        return "", 204

    def delete(self, did):
        director_service.delete(did)
        return "", 204
