from flask import request, jsonify
from flask_jwt_simple import jwt_required, get_jwt
from flask_restful import Resource
from models.policy import PolicyModel
from datetime import date, datetime

from utils import *
    # insert_into_insured
    # insert_into_provider
    # insert_into_collaborator
    # select_insured_by_user_id
    # select_collaborator_by_user_id
    # select_provider_by_user_id
    # update_insured
    # update_collaborator
    # update_provider
    # delete_provider
    # delete_collaborator
    # delete_insured
    # validator
    # -encrypt

class PolicyResource(Resource):
    
    def _list_policy(self):
        policy = PolicyModel.list_all()
        print(policy)
        return list(map(lambda policy:{
            'id':policy.id,
            'number':policy.number,
            'status':policy.status
            

        },policy))
    
    def get(self):
        try:
            return self._list_policy()
        except Exception as e:
            return f"{e}", 500

    def post(self):
        item = request.get_json() if request.get_json() else request.form

        try:
            if item:
                model = PolicyModel()
                model.number = item['number'] 
                model.plan_policy_id = item['plan_policy_id'] 
                model.created_date = date.today()
                model.save()
                
                return 'created', 201
            else:
                return 'not created, invalid payload', 400
        except Exception as e:
            return f"{e}", 500

class PolicyDetailResource(Resource):

    def _get_policy(self, id):
        
        policy = PolicyModel.get_by_id(id)
        
        if policy is None:
            return {'message': 'Policy not found'}, 404

        return {
            'id':policy.id,
            'number':policy.number,
            'status':policy.status,
            'created_date':policy.created_date.strftime("%d/%m/%Y"),
            'owner':select_insured_by_policy_id(id),
            'plan_policy':select_plan_policy_by_id(policy.plan_policy_id)
        }
    
    # @jwt_required
    def get(self, id):
        try:
            # print(id)
            id = id
            return self._get_policy(id)
        except Exception as e:
            return f"{e}", 500
    
    # @jwt_required
    def put(self, id):
        item = request.get_json() if request.get_json() else request.form

        try:

            if item:
                model = PolicyModel.get_by_id(id)
                
                if 'number' in item:
                    model.number = item['number']
                if 'plan_policy_id' in item:
                    model.plan_policy_id = item['plan_policy_id']
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
            policy = PolicyModel.get_by_id(id)
            policy.delete()
            return 'No Content', 204
        except Exception as e:
            return f"{e}", 500

    