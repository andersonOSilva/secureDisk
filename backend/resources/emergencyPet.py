from flask import request, jsonify
from flask_restful import Resource
from datetime import date, datetime

from models.emergency import EmergencyModel
from models.provider import ProviderModel
from models.proposal import ProposalModel
from flask_jwt_simple import jwt_required, get_jwt
from utils import *

class EmergencyPetDetailResource(Resource):

    def _get_emergency(self, id_emergency):
        emergency = EmergencyPetModel.get_by_id(id_emergency)
        pet_pacient = select_pet_by_proposal_id(emergency.proposal_id)

        if emergency is None:
            return {'message': 'Plan not found'}, 404

        return {
            'id':emergency.id,
            'label':emergency.label,
            'call':emergency.call,
            'lat':emergency.latitude,
            'log':emergency.longitude,
            'provider_name':select_provider_by_id(emergency.provider_id),
            'pacient':pet_pacient
        }
    
    # @jwt_required
    def get(self, id):
        try:
            return self._get_emergency(id)
        except Exception as e:
            return f"{e}", 500
    
    def delete(self,id):
        try:
            emergency = EmergencyPetModel.get_by_id(id)
            emergency.delete()
            return 'No Content', 204
        except Exception as e:
            return f"{e}", 500

    