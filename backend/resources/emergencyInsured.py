from flask import request, jsonify
from flask_restful import Resource
from datetime import date, datetime

from models.emergency import EmergencyModel
from models.provider import ProviderModel
from models.policy import PolicyModel
from flask_jwt_simple import jwt_required, get_jwt
from utils import *

class EmergencyInsuredDetailResource(Resource):

    def _get_emergency(self, id_emergency):
        emergency = EmergencyInsuredModel.get_by_id(id_emergency)
        insured = InsuredModel.get_by_id(emergency.policy_id)
        pacient = select_insured_by_user_id(insured.user_id)
        if emergency is None:
            return {'message': 'Plan not found'}, 404

        return {
            'id':emergency.id,
            'label':emergency.label,
            'call':emergency.call,
            'lat':emergency.latitude,
            'log':emergency.longitude,
            'provider':select_provider_by_id(emergency.provider_id),
            'pacient':pacient
        }
    
    # @jwt_required
    def get(self, id):
        try:
            return self._get_emergency(id)
        except Exception as e:
            return f"{e}", 500
    
    def delete(self,id):
        try:
            emergency = EmergencyInsuredModel.get_by_id(id)
            emergency.delete()
            return 'No Content', 204
        except Exception as e:
            return f"{e}", 500

    