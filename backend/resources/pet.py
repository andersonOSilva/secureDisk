from flask import request, jsonify
from flask_jwt_simple import jwt_required, get_jwt
from flask_restful import Resource
from models.pet import PetModel
from models.user import UserModel
from datetime import date, datetime

class PetResource(Resource):
    
    def _list_pet(self):
        pet = PetModel.list_all()
        
        return list(map(lambda pet:{
            'id':pet.id,
            'name':pet.name,
            'species':pet.species,
            'breed':pet.breed,
            'size':pet.size,
            'weight':pet.weight,
            'status':pet.status,
            'insured_id':pet.insured_id

        },pet))
    
    def get(self):
        try:
            return self._list_pet()
        except Exception as e:
            return f"{e}", 500

    def post(self):
        item = request.get_json() if request.get_json() else request.form

        try:
            if item:
                model = PetModel()
                model.name = item['name'] 
                model.species = item['species'] 
                model.breed = item['breed'] 
                model.size = item['size'] 
                model.weight = item['weight'] 
                model.insured_id = item['insured_id']
                model.created_date = date.today()
                model.save()
                
                return 'created', 201
            else:
                return 'not created, invalid payload', 400
        except Exception as e:
            return f"{e}", 500

class PetDetailResource(Resource):

    def _get_pet(self, id_pet):
        
        pet = PetModel.get_by_id(id_pet)
        user = UserModel.get_by_id(pet.insured_id)
        owner = {
                'id': user.id,
                'email': user.email,
                'status': user.status,
                'type_user': user.type_user,
                'created_date': user.created_date.strftime("%d/%m/%Y"),
                'url_details': f'http://192.168.1.108:8080/api/user/{user.id}'
            }

        if pet is None:
            return {'message': 'Pet not found'}, 404

        return {
            'id':pet.id,
            'name':pet.name,
            'species':pet.species,
            'breed':pet.breed,
            'size':pet.size,
            'weight':pet.weight,
            'status':pet.status,
            'insured_id':pet.insured_id,
            'created_date':pet.created_date.strftime("%d/%m/%Y"),
            'owner_data':owner
        }
    
    # @jwt_required
    def get(self, id):
        try:
            # print(id)
            id_pet = id
            return self._get_pet(id_pet)
        except Exception as e:
            return f"{e}", 500
    
    # @jwt_required
    def put(self, id):
        item = request.get_json() if request.get_json() else request.form

        try:

            if item:
                model = PetModel.get_by_id(id)
                
                if 'name' in item:
                    model.name = item['name']
                if 'species' in item:
                    model.species = item['species']
                if 'breed' in item:
                    model.breed = item['breed']
                if 'size' in item:
                    model.size = item['size']
                if 'weight' in item:
                    model.weight = item['weight']
                if 'status' in item:
                    model.status = item['status']
                if 'status' in item:
                    model.status = item['status']
                
                model.save()

                return 'edited', 204
            else:
                return 'unedited, invalid payload', 400
        except Exception as e:
            return f"{e}",500
    
    def delete(self,id):
        try:
            pet = PetModel.get_by_id(id)
            pet.delete()
            return 'No Content', 204
        except Exception as e:
            return f"{e}", 500

    