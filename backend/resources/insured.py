from flask import request, jsonify
from flask_jwt_simple import jwt_required, get_jwt
from flask_restful import Resource
from models.insured import InsuredModel
from datetime import date, datetime


class InsuredResource(Resource):

    def _list_insured(self):
        insured = InsuredModel.list_all()

        return list(map(lambda insured: {
            'id': insured.id,
            'name': insured.first_name,
            'email': insured.email,
            'status': insured.status
        }, insured))

    # @jwt_required
    def get(self):
        try:
            return self._list_insured()
        except Exception as e:
            return f"{e}", 500

    def post(self):
        item = request.get_json() if request.get_json() else request.form

        try:
            if item:
                model = InsuredModel()
                model.first_name = item['first_name']
                model.last_name = item['last_name']
                model.email = item['email']
                model.cel = item['cel']
                model.tel = item['tel']
                model.cpf = item['cpf']
                model.password = item['password']
                model.created_date = date.today()
                model.save()

                return 'created', 201
            else:
                return 'not created, invalid payload', 400
        except Exception as e:
            return f"{e}", 500


class InsuredDetailResource(Resource):

    def _get_insured(self, id_insured):
        insured = InsuredModel.get_by_id(id_insured)

        if insured is None:
            return {'message': 'Insured not found'}, 404
        created_date = insured.created_date.strftime("%d/%m/%Y")
         
        return {
            'id': insured.id,
            'first_name':insured.first_name,
            'last_name': insured.last_name,
            'cpf':insured.cpf,
            'tel':insured.tel,
            'cel':insured.cel,
            'email':insured.email,
            'status':insured.status,
            'created_date': created_date
        }

    @jwt_required
    def get(self, id):
        try:
            id_insured = id
            return self._get_insured(id_insured)

        except Exception as e:
            return f"{e}", 500

    # @jwt_required
    def put(self, id):
        item = request.get_json() if request.get_json() else request.form

        try:
            if item:
                model = InsuredModel.get_by_id(id)
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
            insured = InsuredModel.get_by_id(id)
            insured.delete()
            return 'No Content', 204

        except Exception as e:
            return f"{e}", 500
