from flask import request, jsonify
from flask_jwt_simple import jwt_required, get_jwt
from flask_restful import Resource
from models.petSchedule import PetScheduleModel
from models.provider import ProviderModel
from models.proposal import ProposalModel
from datetime import date, datetime
from utils import *
class PetScheduleResource(Resource):
    
    def _list_pet_schedule(self):
        
        petSchedule = PetScheduleModel.list_all()
        
        return list(map(lambda petSchedule:{
            'id':petSchedule.id,
            'name':petSchedule.name,
            'pet_name':select_pet_by_proposal_id(petSchedule.proposal_id)['pet']['name'],
            'date':petSchedule.date,
            'time':petSchedule.time,
            'provider_name':select_provider_by_id(petSchedule.provider_id)['fantasy_name']
            
        },petSchedule))
    
    def get(self):
        try:
            return self._list_pet_schedule()
        except Exception as e:
            return f"{e}", 500

    def post(self):
        item = request.get_json() if request.get_json() else request.form

        try:
            if item:
                model = PetScheduleModel()
                model.name = item['name']
                model.email = item['email']
                model.date = item['date']
                model.time = item['time']
                model.provider_id = item['provider_id']
                model.proposal_id = item['proposal_id']
                model.created_date = date.today()
                model.save()
                
                return 'created', 201
            else:
                return 'not created, invalid payload', 400
        except Exception as e:
            return f"{e}", 500

class PetScheduleDetailResource(Resource):

    def _get_pet_schedule(self, id_pet_schedule):
        pet_schedule = PetScheduleModel.get_by_id(id_pet_schedule)
        provider = ProviderModel.get_by_id(pet_schedule.provider_id)
        
        pacient = select_pet_by_proposal_id(pet_schedule.proposal_id)
        provider_associated = {
            'id':provider.id,
            'fantasy_name':provider.fantasy_name,
            'provider_details':f'http://127.0.0.1:8080/api/user/{provider.user_id}'
            
        }

        if pet_schedule is None:
            return {'message': 'Plan not found'}, 404

        return {
            'id':pet_schedule.id,
            'name':pet_schedule.name,
            'date':pet_schedule.date,
            'time':pet_schedule.time,
            'email':pet_schedule.email,
            'status':pet_schedule.status,
            'created_date':pet_schedule.created_date.strftime("%d/%m/%Y"),
            'provider':provider_associated,
            'pacient':pacient
        }
    
    # @jwt_required
    def get(self, id):
        try:
            return self._get_pet_schedule(id)
        except Exception as e:
            return f"{e}", 500
    
    # @jwt_required
    def put(self, id):
        item = request.get_json() if request.get_json() else request.form

        try:

            if item:
                
                model = PetScheduleModel.get_by_id(id)
                
                if 'name' in item:
                    model.name = item['name']
                if 'date' in item:
                    model.date = item['date']
                if 'time' in item:
                    model.time = item['time']
                if 'email' in item:
                    model.email = item['email']
                if 'provider_id' in item:
                    model.provider_id = item['provider_id']
                if 'status' in item:
                    model.status = item['status']
                
                model.save()

                return 'edited', 200
            else:
                return 'unedited, invalid payload', 400
        except Exception as e:
            return f"{e}",500
    
    def delete(self,id):
        try:
            pet_schedule = PetScheduleModel.get_by_id(id)
            pet_schedule.delete()
            return 'No Content', 204
        except Exception as e:
            return f"{e}", 500

    