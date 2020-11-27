from flask import request, jsonify
from flask_restful import Resource
from datetime import date, datetime

from models.emergencyInsured import EmergencyInsuredModel
from models.emergencyPet import EmergencyPetModel
from models.provider import ProviderModel
from models.proposal import ProposalModel
from flask_jwt_simple import jwt_required, get_jwt
from utils import *

class EmergencyResource(Resource):
    
    def _list_emergency(self):
        
        emergencyPet = EmergencyPetModel.list_all()
        emergencyPetList = list(map(lambda emergency:{
            'id':emergency.id,
            'label':emergency.label,
            'call':emergency.call,
            'lat':emergency.latitude,
            'log':emergency.longitude,
            'status':emergency.status,
            'provider_name':select_provider_by_id(emergency.provider_id)['fantasy_name']
        },emergencyPet))
        

        emergencyInsured = EmergencyInsuredModel.list_all()
        emergencyInsuredList = list(map(lambda emergency:{
            'id':emergency.id,
            'label':emergency.label,
            'call':emergency.call,
            'lat':emergency.latitude,
            'log':emergency.longitude,
            'status':emergency.status,
            'provider_name':select_provider_by_id(emergency.provider_id)['fantasy_name']
        },emergencyInsured))


        return {
            'emergencyPet':emergencyPetList,
            'emergencyInsured':emergencyInsuredList
        } 
    
    def get(self):
        try:
            return self._list_emergency()
        except Exception as e:
            return f"{e}", 500

    def post(self):
        item = request.get_json() if request.get_json() else request.form
        
        try:
            if item:
                if item['call_type'].lower() == 'pet':
                    # emergency = select_emergency_proposal_by_policy(item["number_policy"])
                    # emergency = select_emergency_pet_by_proposal(item["number_proposal"])
                    # return update_emergency_pet(emergency["id"],item)
                    return insert_into_emergency_pet(item)
                    
                else:
                    
                    # emergency = select_emergency_insured_by_policy(item["number_policy"])
    
                    # return update_emergency_insured( emergency["id"],item)
                    return insert_into_emergency_insured(item)


                return 'edited', 200
            else:
                return 'unedited, invalid payload', 400
        except Exception as e:
            return f"{e}",500

class EmergencyDetailResource(Resource):
    # @jwt_required
    def put(self, id):
        item = request.get_json() if request.get_json() else request.form

        try:
            if item:
                if item['call_type'].lower() == 'pet':
                    
                    update_emergency_pet(id,item)
                    
                else:
                    update_emergency_insured(id,item)


                return 'edited', 200
            else:
                return 'unedited, invalid payload', 400
        except Exception as e:
            return f"{e}",500
    

    