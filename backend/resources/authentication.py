from flask_jwt_simple import create_jwt
from datetime import date, datetime
from flask_restful import Resource
from flask import request
from os import environ

from models.user import UserModel
from models.insured import InsuredModel
from models.provider import ProviderModel
from models.collaborator import CollaboratorModel
from utils import *
class AuthenticationResource(Resource):

    def post(self):
        data = request.get_json()
        email = data['email'].strip()
        password = encrypt(data['password'])
        user = UserModel.authenticate(email, password)

        if user:
            if user.type_user == 'insured':
                user_data = InsuredModel.get_by_user_id(user.id)
                user_data_json = {
                                    'id': user_data.id,
                                    'first_name':user_data.first_name,
                                    'last_name': user_data.last_name,
                                    'cpf':user_data.cpf,
                                    'tel':user_data.tel,
                                    'cel':user_data.cel
                                }
            elif user.type_user == 'provider':
                user_data = ProviderModel.get_by_user_id(user.id)
                user_data_json = {
                                    'id': user_data.id,
                                    'business_name':user_data.business_name,
                                    'fantasy_name': user_data.fantasy_name,
                                    'cnpj':user_data.cnpj,
                                    'tel':user_data.tel,
                                    'cel':user_data.cel
                                }

            else:
                user_data = CollaboratorModel.get_by_user_id(user.id)
                user_data_json ={
                                    'id': user_data.id,
                                    'first_name':user_data.first_name,
                                    'last_name': user_data.last_name,
                                    'cpf':user_data.cpf,
                                    'tel':user_data.tel,
                                    'cel':user_data.cel
                                }

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
                'created_date':user.created_date.strftime("%d/%m/%Y"),
                'jwt': access,
                'user_data':user_data_json

                }, 200
        else:
            return {'message': 'Invalid credentials'}, 400
