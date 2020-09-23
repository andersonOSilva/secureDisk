from datetime import date, datetime
from models.proposal import ProposalModel
from models.pet import PetModel
from sqlalchemy.exc import SQLAlchemyError
from utils.proposal import insert_into_proposal
import sqlite3

def select_pet_by_proposal_id(proposal_id):
    try:
        pet = PetModel.get_by_proposal(proposal_id)

        if pet is None:
            return {'success':False,'message': 'Insured not found'}
        else:
            return {
            'id':pet.id,
            'name':pet.name,
            'species':pet.species,
            'breed':pet.breed,
            'size':pet.size,
            'weight':pet.weight,
            'status':pet.status,
            'insured_id':pet.insured_id,
            'created_date':pet.created_date.strftime("%d/%m/%Y")
        }
            

    except Exception as e:
        return {"succes":False, "message":f'{e} invalid payload'}
