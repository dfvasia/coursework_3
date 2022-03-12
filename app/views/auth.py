from flask import request
from flask_restx import Resource, Namespace, abort
from marshmallow import Schema, fields, ValidationError
import app.tools.jwt_token as jwt


from container import user_service
from exceptions import DuplicateError

auth_ns = Namespace('auth')


class LoginValidator(Schema):
    # username = fields.Str(required=True)
    # surname = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        """Create token"""
        try:
            validated_data = LoginValidator().load(request.json)
            user = user_service.get_by_user_email(validated_data['email'])
            if not user:
                abort(404)
            token_data = jwt.JwtSchema().load({'user_id': user.id, 'role': user.role_id})
            a = jwt.JwtToken(token_data).get_tokens()
            b = user_service.write_refresh_token(user.email, a["refresh_token"])
            print(b)
            return a, 201

        except ValidationError as e:
            print(e)
            abort(400)

    def put(self):
        """Update token"""
        try:
            r_token = request.json.get('refresh_token')
            data = jwt.JwtToken.decode_token(r_token)
            if not data:
                abort(404)
            token_data = jwt.JwtSchema().load({'user_id': data['user_id'], 'role': data['role']})
            return jwt.JwtToken(token_data).get_tokens(), 201
        except ValidationError as e:
            print(str(e))
            abort(400)
