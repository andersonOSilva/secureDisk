from flask import request, jsonify
from flask_restful import Resource
from datetime import date, datetime
from flask_jwt_simple import jwt_required, get_jwt

from utils import *
    # insert_into_insured
    # insert_into_provider
    # insert_into_collaborator
    # select_insured_by_user_id
    # select_collaborator_by_user_id
    # select_provider_by_user_id
    # update_insured
    # update_collaborator
    # update_provider
    # delete_provider
    # delete_collaborator
    # delete_insured
    # validator
    # -encrypt
from models.user import UserModel


class UserResource(Resource):

    def _list_user(self):

        users = UserModel.list_all()


        return list(map(lambda user: {
            'id': user.id,
            'email': user.email,
            'status': user.status,
            'type_user': user.type_user,
            'created_date': user.created_date.strftime("%d/%m/%Y"),
            'url_details': f'http://192.168.1.108:8080/api/user/{user.id}'
            }, users))
    
    # @jwt_required
    def get(self):
        try:
            return self._list_user()
        except Exception as e:
            return f"{e}", 500

    def post(self):
        item = request.get_json() if request.get_json() else request.form

        try:
            if item:
                # valida os dados de inserção
                if not user_validate(item)['success']:
                    return user_validate(item), 400
                    
                # insere os itens de usuario
                user = UserModel()
                user.email = item['email']
                user.password = encrypt(item['password'])
                user.type_user = item['type_user']
                user.active = item['active'] if 'active' in item else True
                user.created_date = date.today()
                user.save()
                
                user_inserted = UserModel.get_by_email(item['email'])
                
                # checa o tipo de usuario
                if str(item["type_user"]) == "insured":
                    # insere as info do usuario na tabela de acordo com o tipo
                    response = insert_into_insured(item, user_inserted)
                elif str(item["type_user"]) == "provider":
                    # insere as info do usuario na tabela de acordo com o tipo
                    response = insert_into_provider(item, user_inserted)
                else:
                    # insere as info do usuario na tabela de acordo com o tipo
                    response = insert_into_collaborator(item, user_inserted)

                return response, 201
            else:
                return 'not created, invalid payload', 400
        except Exception as e:
            return f"{e}", 500


class UserDetailResource(Resource):
    
    def _get_user(self, id_user):
        user = UserModel.get_by_id(id_user)


        if user is None:
            return {'message': 'User not found'}, 404

        if user.type_user == "insured":
            response = select_insured_by_user_id(user)

        elif user.type_user == "provider":
            response = select_provider_by_user_id(user)
            
        else:
            response = select_collaborator_by_user_id(user)
            
        
        return {
            'id':user.id,
            'email':user.email,
            'status': user.status,
            'type_user': user.type_user,
            'created_date': user.created_date.strftime("%d/%m/%Y"),
            'data':response
            
        }

    @jwt_required
    def get(self, id):
        try:
            id_user = id
            return self._get_user(id_user)

        except Exception as e:
            return f"{e}", 500

    @jwt_required
    def put(self, id):
        item = request.get_json() if request.get_json() else request.form

        try:
            if item:
                
                if not user_update_validate(item)['success']:
                    return user_update_validate(item), 400

                user = UserModel.get_by_id(id)

                
                if 'email' in item:
                    user.email = item['email']
                if 'status' in item:
                    user.status = item['status']
                if 'password' in item:
                    user.password = encrypt(item['password'])

                user.save()

                if str(item["type_user"]) == "insured":
                    response = update_insured(item, user)
                elif str(item["type_user"]) == "provider":
                    response = update_provider(item, user)
                    
                else:
                    response = update_collaborator(item, user)
                    
                return response, 200
            else:
                return 'unedited, invalid payload', 400

        except Exception as e:
            return f"{e}", 500

    def delete(self, id):
        try:

            user = UserModel.get_by_id(id)
            if user:
                
                if user.type_user == "insured":
                    response = delete_insured(user.id)
                elif user.type_user == "provider":
                    response = delete_provider(user.id)
                    
                else:
                    response = delete_collaborator(user.id)
                    
                
                if response["success"]:
                    user.delete()
                else:
                    return 'User no deleted', 500
            else:
                return 'User not found', 404

            return 'No Content', 204

        except Exception as e:
            return f"{e}", 500
