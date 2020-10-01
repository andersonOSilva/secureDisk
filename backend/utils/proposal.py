from datetime import date, datetime
from sqlalchemy.exc import SQLAlchemyError

from models.planProposal import PlanProposalModel
from models.proposal import ProposalModel

def insert_into_proposal(item):
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

