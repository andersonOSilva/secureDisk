from flask_jwt_simple import create_jwt
from datetime import date, datetime
from flask_restful import Resource
from flask import request
from os import environ

from models.user import UserModel
from models.insured import InsuredModel
from models.provider import ProviderModel
from models.collaborator import CollaboratorModel

class AuthenticationResource(Resource):

    def post(self):
        data = request.get_json()
        email = data['email'].strip()
        password = data['password']
        user = UserModel.authenticate(email, password)

        if user:
            if user.type_user == 'insured':
                user_data = InsuredModel.get_by_user_id(user.id)

            elif user.type_user == 'provider':
                user_data = ProviderModel.get_by_user_id(user.id)

            else:
                user_data = CollaboratorModel.get_by_user_id(user.id)

            access = create_jwt({
                'id_insured': user.id,
                'email': user.email,
                'status': user.status,
                'type_user':user.type_user
            })

            return {
                'id_insured': user.id,
                'email': user.email,
                'status': user.status,
                'type_user':user.type_user,
                'created_date':user.created_date,
                'jwt': access,
                'user_data':user_data
            }, 200
        else:
            return {'message': 'Invalid credentials'}, 400
