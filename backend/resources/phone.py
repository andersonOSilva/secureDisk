from flask import request, jsonify
from flask_restful import Resource
from datetime import date, datetime
from flask_jwt_simple import jwt_required, get_jwt

from models.phone import PhoneModel
from utils import *

class PhoneResource(Resource):
    
    def _list_phone(self):
        phone = PhoneModel.list_all()
        return list(map(lambda phone:{
            'id':phone.id,
            'phone':phone.phone,
            'webphone':phone.webphone,
            'branch_line':phone.branch_line,
            'status':phone.status,
            'owner':select_user_by_id(phone.user_id)
        },phone))
    
    def get(self):
        try:
            return self._list_phone()
        except Exception as e:
            return f"{e}", 500

    def post(self):
        item = request.get_json() if request.get_json() else request.form

        try:
            if item:
                model = PhoneModel()
                model.phone = item['phone'] 
                model.webphone = item['webphone'] 
                model.branch_line = item['branch_line'] 
                model.status = item['status'] 
                model.user_id = item['user_id'] 
                model.created_date = date.today()
                model.save()
                
                return 'created', 201
            else:
                return 'not created, invalid payload', 400
        except Exception as e:
            return f"{e}", 500

class PhoneDetailResource(Resource):

    def _get_phone(self, id_phone):
        
        phone = PhoneModel.get_by_id(id_phone)

        if phone is None:
            return {'message': 'Phone not found'}, 404

        return {
            'id':phone.id,
            'phone':phone.phone,
            'webphone':phone.webphone,
            'branch_line':phone.branch_line,    
            'status':phone.status,
            'user_id':select_user_detail_by_id(phone.user_id),
            'created_date':phone.created_date.strftime("%d/%m/%Y")
        }
    
    # @jwt_required
    def get(self, id):
        try:
            id_phone = id
            return self._get_phone(id_phone)
        except Exception as e:
            return f"{e}", 500
    
    # @jwt_required
    def put(self, id):
        item = request.get_json() if request.get_json() else request.form

        try:

            if item:
                model = PhoneModel.get_by_id(id)
                if 'phone' in item:
                    model.phone = item['phone']
                if 'webphone' in item:
                    model.webphone = item['webphone']
                if 'branch_line' in item:
                    model.branch_line = item['branch_line']
                if 'status' in item:
                    model.status = item['status']
                if 'user_id' in item:
                    model.user_id = item['user_id']
                
                model.save()

                return 'edited', 200
            else:
                return 'unedited, invalid payload', 400
        except Exception as e:
            return f"{e}",500
    
    def delete(self,id):
        try:
            phone = PhoneModel.get_by_id(id)
            phone.delete()
            return 'No Content', 204
        except Exception as e:
            return f"{e}", 500

    