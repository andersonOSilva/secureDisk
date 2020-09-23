from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_simple import jwt_required, get_jwt

from models.insured import InsuredModel


class InsuredResource(Resource):

    def _list_insured(self):

        insured = InsuredModel.list_all()

                
        return list(map(lambda insured: {
            'id': insured.id,
            'first_name':insured.first_name,
            'last_name': insured.last_name,
            'cpf':insured.cpf,
            'tel':insured.tel,
            'cel':insured.cel,
            'url_details': f'http://127.0.0.1:8080/api/user/{insured.user_id}'
            }, insured))
    
    
    def get(self):
        try:
            return self._list_insured()
        except Exception as e:
            return f"{e}", 500

    