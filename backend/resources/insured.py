from flask import request, jsonify
from flask_jwt_simple import jwt_required, get_jwt
from flask_restful import Resource
from models.insured import InsuredModel
from datetime import date, datetime


class InsuredResource(Resource):

    def _list_provider(self):
        providers = ProviderModel.list_all()

        return list(map(lambda provider: {
            'id': providers.id,
            'name': providers.first_name,
            'email': providers.email,
            'status': providers.status,
            'password': providers.password
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
                model.business_name = item['first_name']
                model.fantasy_name = item['last_name']
                model.email = item['email']
                model.cel = item['cel']
                model.tel = item['tel']
                model.cpf = item['cpf']
                model.status = item['status']
                # model.status = item['status'] if 'active' in item else True
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
            'first_name':provider.first_name,
            'last_name': provider.last_name,
            'cpf':provider.cpf,
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
                if 'first_name' in item:
                    model.first_name = item['first_name']
                if 'last_name' in item:
                    model.last_name = item['last_name']
                if 'email' in item:
                    model.email = item['email']
                if 'cpf' in item:
                    model.cpf = item['cpf']
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
