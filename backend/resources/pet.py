from flask import request, jsonify
from flask_restful import Resource
from datetime import date, datetime
from flask_jwt_simple import jwt_required, get_jwt

from models.pet import PetModel
from models.proposal import ProposalModel
from models.user import UserModel
from utils import *

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

                insert_into_proposal(item['proposal'])
                proposal = ProposalModel.get_by_number(item['proposal']['number'])

                model = PetModel()
                model.name = item['name'] 
                model.species = item['species'] 
                model.breed = item['breed'] 
                model.size = item['size'] 
                model.weight = item['weight'] 
                model.insured_id = item['insured_id']
                model.proposal_id = proposal.id
                model.created_date = date.today()
                model.save()
                
                return 'created', 201
            else:
                proposal.delete()
                return 'not created, invalid payload', 400
        except Exception as e:
            return f"{e}", 500

class PetDetailResource(Resource):

    def _get_pet(self, id_pet):

        return select_pet_by_proposal_id(id_pet)
    
    # @jwt_required
    def get(self, id):
        try:
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
            proposal = ProposalModel.get_by_id(pet.proposal_id)
            
            proposal.delete()
            pet.delete()
            return 'No Content', 204
        except Exception as e:
            return f"{e}", 500

    