from flask import request, jsonify
from flask_restful import Resource
from datetime import date, datetime
from flask_jwt_simple import jwt_required, get_jwt

from models.planProposal import PlanProposalModel


class PlanProposalResource(Resource):
    
    def _list_plan_proposal(self):
        plan = PlanProposalModel.list_all()
        return list(map(lambda plan:{
            'id':plan.id,
            'name':plan.name,
            'status':plan.status
            

        },plan))
    
    def get(self):
        try:
            return self._list_plan_proposal()
        except Exception as e:
            return f"{e}", 500

    def post(self):
        item = request.get_json() if request.get_json() else request.form

        try:
            if item:
                model = PlanProposalModel()
                model.name = item['name'] 
                model.desc = item['desc'] 
                model.created_date = date.today()
                model.save()
                
                return 'created', 201
            else:
                return 'not created, invalid payload', 400
        except Exception as e:
            return f"{e}", 500

class PlanProposalDetailResource(Resource):

    def _get_plan_proposal(self, id_plan):
        
        plan = PlanProposalModel.get_by_id(id_plan)

        if plan is None:
            return {'message': 'Plan not found'}, 404

        return {
            'id':plan.id,
            'name':plan.name,
            'desc':plan.desc,
            'status':plan.status,
            'created_date':plan.created_date.strftime("%d/%m/%Y")
        }
    
    # @jwt_required
    def get(self, id):
        try:
            id_plan = id
            return self._get_plan_proposal(id_plan)
        except Exception as e:
            return f"{e}", 500
    
    # @jwt_required
    def put(self, id):
        item = request.get_json() if request.get_json() else request.form

        try:

            if item:
                model = PlanProposalModel.get_by_id(id)
                
                if 'name' in item:
                    model.name = item['name']
                if 'desc' in item:
                    model.desc = item['desc']
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
            plan = PlanProposalModel.get_by_id(id)
            plan.delete()
            return 'No Content', 204
        except Exception as e:
            return f"{e}", 500

    