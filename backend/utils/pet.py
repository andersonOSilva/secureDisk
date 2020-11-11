import sqlite3
from datetime import date, datetime
from sqlalchemy.exc import SQLAlchemyError
from utils.proposal import insert_into_proposal

from models.proposal import ProposalModel
from models.pet import PetModel
from models.planProposal import PlanProposalModel
from models.insured import InsuredModel

def select_pet_by_proposal_id(proposal_id):
    try:
        pet = PetModel.get_by_proposal(proposal_id)
        proposal = ProposalModel.get_by_id(proposal_id)
        plan = PlanProposalModel.get_by_id(proposal.plan_proposal_id)
        insured = InsuredModel.get_by_id(pet.insured_id)

        if pet is None:
            return {'success':False,'message': 'Insured not found'}
        else:
            return {
                'pet':{
                    'id':pet.id,
                    'name':pet.name,
                    'species':pet.species,
                    'breed':pet.breed,
                    'size':pet.size,
                    'weight':pet.weight
                },
                'proposal_details':{
                    'id':proposal.id,
                    'number':proposal.number,
                    'status':proposal.status,
                    'created_date':proposal.created_date.strftime("%d/%m/%Y"),
                    'plan_proposal':{
                        'id':plan.id,
                        'name':plan.name,
                        'desc':plan.desc,
                        'status':plan.status,
                        'created_date':plan.created_date.strftime("%d/%m/%Y")
                    }
                },
                'owner':{
                    'name':f'{insured.first_name} {insured.last_name}',

                    'details':f'http://127.0.0.1:8080/api/user/{insured.user_id}'
                    }
                
            }
            

    except Exception as e:
        return {"succes":False, "message":f'{e} invalid payload'}


