from flask import request, jsonify
from flask_jwt_simple import jwt_required, get_jwt
from flask_restful import Resource
from models.pet import PetModel
from models.proposal import ProposalModel
from models.user import UserModel
from datetime import date, datetime
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
        
        pet = PetModel.get_by_id(id_pet)
        pet_proposal = ProposalModel.get_by_id(pet.proposal_id)
        
        user = UserModel.get_by_id(pet.insured_id)
        
        proposal = {
            'number':pet_proposal.number,
            'plan': select_plan_proposal_by_id(pet_proposal.plan_proposal_id)
        }
        
        owner = {
                'id': user.id,
                'email': user.email,
                'status': user.status,
                'type_user': user.type_user,
                'created_date': user.created_date.strftime("%d/%m/%Y"),
                'url_details': f'http://127.0.0.1:8080/api/user/{user.id}'
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
            'proposal':proposal,
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
            proposal = ProposalModel.get_by_id(pet.proposal_id)
            
            proposal.delete()
            pet.delete()
            return 'No Content', 204
        except Exception as e:
            return f"{e}", 500

    