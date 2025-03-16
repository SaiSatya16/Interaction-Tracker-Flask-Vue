from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from models.user import User
import datetime

class SignupApi(Resource):
    def post(self):
        body = request.get_json()
        username = body.get('username')
        email = body.get('email')
        password = body.get('password')
        
        if User.find_by_email(email):
            return {'message': 'Email already exists'}, 400
        
        User.add_user(username, email, password)
        return {'message': 'User created successfully'}, 201

class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        email = body.get('email')
        password = body.get('password')
        
        user = User.find_by_email(email)
        
        if not user or not User.check_password(user, password):
            return {'message': 'Invalid credentials'}, 401
        
        expires = datetime.timedelta(days=1)
        access_token = create_access_token(
            identity=str(user['_id']),
            expires_delta=expires
        )
        
        return {'token': access_token}, 200
