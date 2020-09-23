from models.policy import PolicyModel
from datetime import date, datetime
from sqlalchemy.exc import SQLAlchemyError
from models.planPolicy import PlanPolicyModel

def insert_into_policy(item):
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


# tras os detalhes do plano da apolice
def select_plan_policy_by_id(id_plan):
    plan = PlanPolicyModel.get_by_id(id_plan)

    if plan is None:
        return {'message': 'Plan not found'}, 404

    return {
        'id':plan.id,
        'name':plan.name,
        'desc':plan.desc,
        'status':plan.status,
        'created_date':plan.created_date.strftime("%d/%m/%Y")
    }