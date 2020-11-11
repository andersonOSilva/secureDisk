from models.user import UserModel
from models.insured import InsuredModel
from models.provider import ProviderModel
from models.collaborator import CollaboratorModel

from .insured import select_insured_by_user_id
from .provider import select_provider_by_user_id
from .collaborator import select_collaborator_by_user_id
def select_user_by_id(id):

    user = UserModel.get_by_id(id)

    return{
        'id':user.id,
        'email':user.email,
        'status': user.status,
        'type_user': user.type_user
    }

def select_user_detail_by_id(id):
    try:
        user = UserModel.get_by_id(id)
        if user:
            if user.type_user == 'insured':
                return select_insured_by_user_id(id)
            if user.type_user == 'provider':
                return select_provider_by_user_id(id)
                
            if user.type_user == 'collaborator':
                return select_collaborator_by_user_id(id)
        else:
            return 'user not found'
    except Exception as e:
        return e
        

    