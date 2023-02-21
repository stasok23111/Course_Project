from flask import request
from flask_restx import Resource, Namespace
from dao.model.user import UserScheme
from implemented import user_service
from helpers.decorators import auth_required

user_ns = Namespace('user')


@user_ns.route('/')
class UserView(Resource):

    @auth_required
    def get(self, email):

        user = user_service.get_by_email(email)
        result = UserScheme().dump(user)
        return result, 200

    @auth_required
    def patch(self, email):
        req_json = request.json
        req_json["email"] = email
        user_service.update(req_json)
        return "", 204


@user_ns.route('/password/')
class UserPasswordView(Resource):
    @auth_required
    def put(self, email):
        data = request.json
        data['email'] = email
        user_service.update_password(data)
        return "", 204