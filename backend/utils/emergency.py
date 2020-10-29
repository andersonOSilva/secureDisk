from datetime import date, datetime
from sqlalchemy.exc import SQLAlchemyError
from utils import select_pet_by_proposal_id, select_plan_policy_by_id, select_plan_proposal_by_id

from models.planPolicy import PlanPolicyModel
from models.emergencyInsured import EmergencyInsuredModel
from models.emergencyPet import EmergencyPetModel
from models.provider import ProviderModel
from models.proposal import ProposalModel
from models.policy import PolicyModel
from models.pet import PetModel
from models.insured import InsuredModel



def insert_into_emergency_insured(item):
    try:
        if item:
            model = EmergencyInsuredModel()
            
            model.call = item['call']
            model.call_type = item['call_type']
            model.label = item['label']
            model.longitude = item['log']
            model.latitude = item['lat']
            model.collab_id = item['collab_id']
            model.provider_id = item['provider_id']
            model.policy_id = item['policy_id'] 
            
            model.created_date = date.today()
            
            model.save()
            
            return 'created', 201
        else:
            return 'not created, invalid payload', 400
    except Exception as e:
        return f"{e}", 500

def insert_into_emergency_pet(item):
    print('insert_pet')
    try:
        if item:
            print('insert_pet_if')
            model = EmergencyPetModel()
            model.call = item['call']
            model.call_type = item['call_type']
            model.label = item['label']
            model.longitude = item['log']
            model.latitude = item['lat']
            model.collab_id = item['collab_id']
            model.provider_id = item['provider_id']
            model.proposal_id = item['proposal_id'] 
            
            model.save()
            
            return 'created', 201
        else:
            return 'not created, invalid payload', 400
    except Exception as e:
        return f"{e}", 500

def select_emergency_pet_by_id(id_emergency):
    emergency = EmergencyPetModel.get_by_id(id_emergency)
    provider = ProviderModel.get_by_id(emergency.provider_id)
    
    provider_associated = {
        'id':provider.id,
        'fantasy_name':provider.fantasy_name,
        'tel':provider.tel,
        'cel':provider.cel,
        'provider_details':f'http://127.0.0.1:8080/api/user/{provider.user_id}'
        
    }

    return {
            'id':emergency.id,
            'name':emergency.name,
            'date':emergency.date,
            'time':emergency.time,
            'email':emergency.email,
            'status':emergency.status,
            'created_date':emergency.created_date.strftime("%d/%m/%Y"),
            'provider':provider_associated,
            'pet_pacient':select_pet_by_proposal_id(emergency.proposal_id)
            
        }
        
def select_emergency_insured_by_policy(policy_number):
    policy = PolicyModel.get_by_number(policy_number)
    emergency = EmergencyInsuredModel.get_by_policy(policy.id)
    
    insured = InsuredModel.get_by_policy_id(emergency.policy_id)
    if emergency.provider_id != 0:
        
        provider = ProviderModel.get_by_id(emergency.provider_id)
        provider_associated = {
        'id':provider.id,
        'fantasy_name':provider.fantasy_name,
        'tel':provider.tel,
        'cel':provider.cel,
        'provider_details':f'http://127.0.0.1:8080/api/user/{provider.user_id}'
        
        }
    else:
        provider_associated = ''

    
    
    insured_pacient = {
                'id': insured.id,
                'first_name':insured.first_name,
                'last_name': insured.last_name,
                'cpf':insured.cpf,
                'tel':insured.tel,
                'cel':insured.cel,
                'policy':{
                    'id':policy.id,
                    'number':policy.number,
                    'status':policy.status,
                    'created_date':policy.created_date.strftime("%d/%m/%Y"),
                    'plan':select_plan_policy_by_id(policy.plan_policy_id)
                }

            }

    return {
            'id':emergency.id,
            'label':emergency.label,
            'call_type':emergency.call_type,
            'call':emergency.call,
            'latitude':emergency.latitude,
            'longitude':emergency.longitude,
            'created_date':emergency.created_date.strftime("%d/%m/%Y"),
            'provider':provider_associated,
            'insured_pacient':insured_pacient
        }

def select_emergency_pet_by_proposal(proposal_number):
    proposal = ProposalModel.get_by_number(proposal_number)
    emergency = EmergencyPetModel.get_by_proposal(proposal.id)
    print(proposal.id)
    print(emergency.id)
    pet = PetModel.get_by_proposal(emergency.proposal_id)
    print(pet)
    
    if emergency.provider_id != 0:

        provider = ProviderModel.get_by_id(emergency.provider_id)
        provider_associated = {
        'id':provider.id,
        'fantasy_name':provider.fantasy_name,
        'tel':provider.tel,
        'cel':provider.cel,
        'provider_details':f'http://127.0.0.1:8080/api/user/{provider.user_id}'
        
        }
    else:
        provider_associated = ''

    
    
    insured_pacient = {
                'id':pet.id,
                'name':pet.name,
                'species':pet.species,
                'breed':pet.breed,
                'size':pet.size,
                'weight':pet.weight,
                'proposal':{
                    'id':proposal.id,
                    'number':proposal.number,
                    'status':proposal.status,
                    'created_date':proposal.created_date.strftime("%d/%m/%Y"),
                    'plan':select_plan_proposal_by_id(proposal.plan_proposal_id)
                }

            }

    return {
            'id':emergency.id,
            'label':emergency.label,
            'call_type':emergency.call_type,
            'call':emergency.call,
            'latitude':emergency.latitude,
            'longitude':emergency.longitude,
            'created_date':emergency.created_date.strftime("%d/%m/%Y"),
            'provider':provider_associated,
            'insured_pacient':insured_pacient
        }

def select_emergency_insured_by_id(id_emergency):
    emergency = EmergencyInsuredModel.get_by_id(id_emergency)
    provider = ProviderModel.get_by_id(emergency.provider_id)
    insured = InsuredModel.get_by_proposal(emergency.policy_id)
    policy = PolicyModel.get_by_id(emergency.policy_id)
    
    
    insured_pacient = {
                'id': insured.id,
                'first_name':insured.first_name,
                'last_name': insured.last_name,
                'cpf':insured.cpf,
                'tel':insured.tel,
                'cel':insured.cel,
                'policy':{
                    'id':policy.id,
                    'number':policy.number,
                    'status':policy.status,
                    'created_date':policy.created_date.strftime("%d/%m/%Y"),
                    'plan':select_plan_policy_by_id(policy.plan_policy_id)
                }

            }
    provider_associated = {
        'id':provider.id,
        'fantasy_name':provider.fantasy_name,
        'tel':provider.tel,
        'cel':provider.cel,
        'provider_details':f'http://127.0.0.1:8080/api/user/{provider.user_id}'
        
    }

    return {
            'id':emergency.id,
            'name':emergency.name,
            'date':emergency.date,
            'time':emergency.time,
            'email':emergency.email,
            'status':emergency.status,
            'created_date':emergency.created_date.strftime("%d/%m/%Y"),
            'provider':provider_associated,
            'insured_pacient':insured_pacient
        }

def update_emergency_pet(id,item):
    try:
        model = EmergencyPetModel.get_by_id(id)
        
        if 'call_type' in item:
            
            model.call_type = item['call_type']

        if 'call' in item:
            
            model.call = item['call']

        if 'label' in item:
            
            model.label = item['label']

        if 'latitude' in item:
            
            model.latitude = item['latitude']

        if 'longitude' in item:
            
            model.longitude = item['longitude']

        if 'policy_id' in item:
            
            model.policy_id = item['policy_id']

        if 'provider_id' in item:
            
            model.provider_id = item['provider_id']

        if 'collab_id' in item:
            
            model.collab_id = item['collab_id']

        if 'status' in item:
            
            model.status = item['status']

        model.save()

        return {"success":True,"message":'emergency updated'}

    except Exception as e:
        return {"success":False,"message":'fail update'}

def update_emergency_insured(id,item):
    try:
        model = EmergencyInsuredModel.get_by_id(id)

        if 'call_type' in item:
            
            model.call_type = item['call_type']

        if 'call' in item:
            
            model.call = item['call']

        if 'label' in item:
            
            model.label = item['label']

        if 'latitude' in item:
            
            model.latitude = item['latitude']

        if 'longitude' in item:
            
            model.longitude = item['longitude']

        if 'policy_id' in item:
            
            model.policy_id = item['policy_id']

        if 'provider_id' in item:
            
            model.provider_id = item['provider_id']

        if 'collab_id' in item:
            
            model.collab_id = item['collab_id']

        if 'status' in item:

            model.status = item['status']

        model.save()

        return {"success":True,"message":'emergency updated'}

    except Exception as e:
        return {"success":False,"message":'fail update'}