from flask import request
from flask_jwt_simple import create_jwt
from flask_restful import Resource
from models.insured import InsuredModel
from os import environ
from datetime import date, datetime


class AuthenticationResource(Resource):

    def post(self):
        data = request.get_json()
        email = data['email'].strip()
        password = data['password']
        insured = InsuredModel.authenticate(email, password)

        if insured:

            access = create_jwt({
                'id_insured': insured.id,
                'email': insured.email,
                'first_name': insured.first_name,
                'last_name': insured.last_name,
                'cpf': insured.cpf,
                'tel': insured.tel,
                'cel': insured.cel,
                'status': insured.status
            })

            return {
                'id_insured': insured.id,
                'email': insured.email,
                'first_name': insured.first_name,
                'last_name': insured.last_name,
                'cpf': insured.cpf,
                'tel': insured.tel,
                'cel': insured.cel,
                'status': insured.status,
                'jwt': access
            }, 200
        else:
            return {'message': 'Invalid credentials'}, 400
