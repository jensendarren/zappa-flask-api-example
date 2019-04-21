from app import app, api, db
from app.errors import make_error
from flask import request
from flask_restful import Resource
from app.models import User, Post

class PingController(Resource):
    def get(self):
        return {'pong': 'Welcom to API Example App! This is the MESSAGE: ' + app.config['MESSAGE']}

class RegistrationsController(Resource):
    def post(self):
        payload = request.get_json()
        user = User.query.filter_by(username=payload['username']).first()
        if user is not None:
            return make_error(409, 42, 'Please use a different username.', 'retry')
        else:
            user = User(username=payload['username'])
            db.session.add(user)
            db.session.commit()
            return {'registration': payload}

class UsersController(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if user is None:
            return make_error(404, 42, 'User not found', 'retry')
        return {'username': user.username}

api.add_resource(PingController, '/ping')
api.add_resource(RegistrationsController, '/registration')
api.add_resource(UsersController, '/users/<int:user_id>')