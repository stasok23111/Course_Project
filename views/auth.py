from flask import request, abort
from flask_restx import Namespace, Resource
from implemented import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class AuthRegisterView(Resource):
    def post(self):
        req_json = request.json
        new_user = user_service.create(req_json)
        return new_user, 201


@auth_ns.route('/login/')
class AuthLoginView(Resource):
    def post(self):
        req_json = request.json
        email = req_json.get("email")
        password = req_json.get("password")
        try:
            tokens = auth_service.generate_tokens(email, password)
            return tokens, 201

        except Exception as e:
            abort(401)

    def put(self):
        req_json = request.json
        refresh_token = req_json.get("refresh_token")
        try:
            tokens = auth_service.get_new_tokens(refresh_token)
            return tokens, 201

        except Exception as e:
            abort(401), e