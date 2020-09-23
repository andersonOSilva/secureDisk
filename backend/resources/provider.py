from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_simple import jwt_required, get_jwt

from models.provider import ProviderModel


class ProviderResource(Resource):

    def _list_provider(self):

        provider = ProviderModel.list_all()

        return list(map(lambda provider: {
            'id': provider.id,
            'business_name':provider.business_name,
            'fantasy_name': provider.fantasy_name,
            'cnpj':provider.cnpj,
            'tel':provider.tel,
            'cel':provider.cel,
            'url_details': f'http://127.0.0.1:8080/api/user/{provider.user_id}'
            }, provider))
    
    
    def get(self):
        try:
            return self._list_provider()
        except Exception as e:
            return f"{e}", 500

    