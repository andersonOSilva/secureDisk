from flask import request, jsonify
from flask_jwt_simple import jwt_required, get_jwt
from flask_restful import Resource
from models.provider import ProviderModel
from datetime import date, datetime


class ProviderResource(Resource):

    def _list_provider(self):
        providers = ProviderModel.list_all()

        return list(map(lambda provider: {
            'id': providers.id,
            'name': providers.fantasy_name,
            'email': providers.email,
            'status': providers.status
        }, providers))

    # @jwt_required
    def get(self):
        try:
            return self._list_provider()
        except Exception as e:
            return f"{e}", 500

    def post(self):
        item = request.get_json() if request.get_json() else request.form

        try:
            if item:
                model = ProviderModel()
                model.business_name = item['business_name']
                model.fantasy_name = item['fantasy_name']
                model.email = item['email']
                model.cel = item['cel']
                model.tel = item['tel']
                model.cnpj = item['cnpj']
                model.password = item['password']
                model.created_date = date.today()
                model.save()

                return 'created', 201
            else:
                return 'not created, invalid payload', 400
        except Exception as e:
            return f"{e}", 500


class ProviderDetailResource(Resource):

    def _get_provider(self, id_provider):
        provider = ProviderModel.get_by_id(id_provider)

        if provider is None:
            return {'message': 'Provider not found'}, 404

        return {
            'id': provider.id,
            'business_name':provider.business_name,
            'fantasy_name': provider.fantasy_name,
            'cnpj':provider.cnpj,
            'tel':provider.tel,
            'cel':provider.cel,
            'email':provider.email,
            'status':provider.status,
            'created_date':provider.created_date
        }

    @jwt_required
    def get(self, id):
        try:
            id_provider = id
            return self._get_provider(id_provider)

        except Exception as e:
            return f"{e}", 500

    # @jwt_required
    def put(self, id):
        item = request.get_json() if request.get_json() else request.form

        try:
            if item:
                model = ProviderModel.get_by_id(id)
                if 'business_name' in item:
                    model.business_name = item['business_name']
                if 'fantasy_name' in item:
                    model.fantasy_name = item['fantasy_name']
                if 'email' in item:
                    model.email = item['email']
                if 'cnpj' in item:
                    model.cnpj = item['cnpj']
                if 'tel' in item:
                    model.tel = item['tel']
                if 'cel' in item:
                    model.cel = item['cel']
                if 'status' in item:
                    model.status = item['status']
                    # model.status = item['status'] if 'active' in item else True
                if 'password' in item:
                    model.password = item['password']
                model.save()

                return 'edited', 204
            else:
                return 'unedited, invalid payload', 400

        except Exception as e:
            return f"{e}", 500

    def delete(self, id):
        try:
            provider = ProviderModel.get_by_id(id)
            provider.delete()
            return 'No Content', 204

        except Exception as e:
            return f"{e}", 500
