from sqlalchemy.exc import SQLAlchemyError
from datetime import date, datetime
import sqlite3

from models.pet import PetModel
from models.policy import PolicyModel
from models.insured import InsuredModel
from models.proposal import ProposalModel
from models.petSchedule import PetScheduleModel

from .policy import select_plan_policy_by_id 
from utils.policy import insert_into_policy

def insert_into_insured( item, user):
    try:
        
        if item:
            # cria a apolice no banco e busca seu id 
            insert_into_policy(item['policy'])
            policy = PolicyModel.get_by_number(item['policy']['number'])
            print(policy)

            insured = InsuredModel()
            insured.first_name = item['first_name']
            insured.last_name = item['last_name']
            insured.cel = item['cel']
            insured.tel = item['tel']
            insured.cpf = item['cpf']
            insured.password = item['password']
            insured.user_id = user.id
            insured.policy_id = policy.id
            insured.save()

            return {"succes":True,"message":'Insured created'}
        else:
            user.delete()
            policy.delete()
            return {"succes":False, "message":'Not created insured, invalid payload'}
    
    except Exception as e:
        user.delete()
        return {"succes":False, "message":f'{e} invalid payload','type_error':'insured/utils'}




def select_insured_by_user_id(user_id):
    try:
        insured = InsuredModel.get_by_user_id(user_id)
        insured_policy = PolicyModel.get_by_id(insured.policy_id)

        policy = {
            'id':insured_policy.id,
            'number':insured_policy.number,
            'status':insured_policy.status,
            'created_date':insured_policy.created_date.strftime("%d/%m/%Y"),
            'plan':select_plan_policy_by_id(insured_policy.plan_policy_id)
        }

        if insured is None:
            return {'success':False,'message': 'Insured not found'}
        else:
            return {
                'id': insured.id,
                'first_name':insured.first_name,
                'last_name': insured.last_name,
                'cpf':insured.cpf,
                'tel':insured.tel,
                'cel':insured.cel,
                'policy': policy

            }
            

    except Exception as e:
        return {"succes":False, "message":f'{e} invalid payload'}

def select_insured_by_policy_id(policy_id):
    try:
        insured = InsuredModel.get_by_policy_id(policy_id)

        if insured is None:
            return {'success':False,'message': 'Insured not found'}
        else:
            return {
                'id': insured.id,
                'first_name':insured.first_name,
                'last_name': insured.last_name,
                'cpf':insured.cpf,
                'tel':insured.tel,
                'cel':insured.cel
                
            }
            

    except Exception as e:
        return {"succes":False, "message":f'{e} invalid payload'}


# @jwt_required
def update_insured( item, user):

    try:
        if item:
            insured = InsuredModel.get_by_user_id(user.id)

            if 'first_name' in item:
                insured.first_name = item['first_name']
            if 'last_name' in item:
                insured.last_name = item['last_name']
            if 'email' in item:
                insured.email = item['email']
            if 'cpf' in item:
                insured.cpf = item['cpf']
            if 'tel' in item:
                insured.tel = item['tel']
            if 'cel' in item:
                insured.cel = item['cel']
            if 'status' in item:
                insured.status = item['status'] 
            if 'password' in item:
                insured.password = item['password']
            
            insured.save()
            return {"success":True,"message":'Insured edited'}
        else:
            user.delete()
            return {"success":False, "message":'Not edited insured, invalid payload'}
        
    
    except Exception as e:
        user.delete()
        return {"success":False, "message":f'{e} invalid payload','type_error':'insured/utils'}


def delete_insured( id):
    try:
        insured = InsuredModel.get_by_user_id(id)
        policy = PolicyModel.get_by_id(insured.policy_id)
        pet = PetModel.get_by_insured(insured.insured_id)
        proposal = ProposalModel.get_by_id(pet.proposal_id)
        pet_schedule = PetScheduleModel.get_by_pet(pet.id)
        
        if pet_schedule:
            pet_schedule.delete()
        
        proposal.delete()
        pet.delete()
        policy.delete()
        insured.delete()

        return {"success":True, "message":'insured deleted'}


    except Exception as e:
        return {"success":False, "message":f"{e}" }
