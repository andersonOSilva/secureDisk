from flask import request, jsonify
from flask_restful import Resource
from datetime import date, datetime
from flask_jwt_simple import jwt_required, get_jwt

from models.proposal import ProposalModel
from utils import *


class ProposalResource(Resource):
    
    def _list_proposal(self):
        proposal = ProposalModel.list_all()
        return list(map(lambda proposal:{
            'id':proposal.id,
            'number':proposal.number,
            'status':proposal.status
            

        },proposal))
    
    def get(self):
        try:
            return self._list_proposal()
        except Exception as e:
            return f"{e}", 500

    def post(self):
        item = request.get_json() if request.get_json() else request.form

        try:
            if item:
                model = ProposalModel()
                model.number = item['number'] 
                model.plan_proposal_id = item['plan_proposal_id'] 
                model.created_date = date.today()
                model.save()
                
                return 'created', 201
            else:
                return 'not created, invalid payload', 400
        except Exception as e:
            return f"{e}", 500

class ProposalDetailResource(Resource):

    def _get_proposal(self, id):
        
        proposal = ProposalModel.get_by_id(id)

        if proposal is None:
            return {'message': 'Proposal not found'}, 404

        return {
            'id':proposal.id,
            'number':proposal.number,
            'status':proposal.status,
            'created_date':proposal.created_date.strftime("%d/%m/%Y"),
            'pet':select_pet_by_proposal_id(id)['pet'],
            'plan_proposal':select_pet_by_proposal_id(id)['proposal_details']['plan_proposal']
        }
    
    # @jwt_required
    def get(self, id):
        try:
            id = id
            return self._get_proposal(id)
        except Exception as e:
            return f"{e}", 500
    
    # @jwt_required
    def put(self, id):
        item = request.get_json() if request.get_json() else request.form

        try:

            if item:
                model = ProposalModel.get_by_id(id)
                
                if 'number' in item:
                    model.number = item['number']
                if 'plan_proposal_id' in item:
                    model.plan_proposal_id = item['plan_proposal_id']
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
            proposal = ProposalModel.get_by_id(id)
            proposal.delete()
            return 'No Content', 204
        except Exception as e:
            return f"{e}", 500

    