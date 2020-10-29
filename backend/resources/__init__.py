from datetime import datetime, timedelta
from enum import IntEnum
from flask import current_app, jsonify
from flask_cors import CORS
from flask_jwt_simple import JWTManager, get_jwt
from flask_restful import Api
from functools import wraps
from werkzeug.exceptions import HTTPException
from os import environ


def initialize_resources(application):
    api = Api(application)
    jwt = JWTManager(application)
    # Caso a aplicação não esteja rodando local, tirar o origins abaixo
    if not environ.get('CORS_URL', None):
        CORS(application, supports_credentials=True, origins="*")
    else:
        # so usar na produção o comando abaixo
        CORS(application, resources={
             r"*": {"origins": environ.get('CORS_URL')}})

    # Endpoints
    from resources.user_password_recovery import UserPasswordRecoveryResource
    from resources.authentication import AuthenticationResource
    
    # from resources.provider import ProviderResource
    # from resources.insured import InsuredResource
    from resources.planProposal import PlanProposalResource
    from resources.collaborator import CollaboratorResource
    from resources.petSchedule import PetScheduleResource
    from resources.planPolicy import PlanPolicyResource
    from resources.emergencyInsured import EmergencyInsuredResource
    from resources.emergencyPet import EmergencyPetResource
    from resources.emergency import EmergencyResource
    from resources.proposal import ProposalResource
    from resources.provider import ProviderResource
    from resources.insured import InsuredResource
    from resources.policy import PolicyResource
    from resources.user import UserResource
    from resources.pet import PetResource
    
    # from resources.provider import ProviderDetailResource
    # from resources.insured import InsuredDetailResource
    from resources.emergencyInsured import EmergencyInsuredDetailResource
    from resources.emergencyPet import EmergencyPetDetailResource
    from resources.emergency import EmergencyDetailResource
    from resources.planProposal import PlanProposalDetailResource
    from resources.petSchedule import PetScheduleDetailResource
    from resources.planPolicy import PlanPolicyDetailResource
    from resources.proposal import ProposalDetailResource
    from resources.policy import PolicyDetailResource
    from resources.user import UserDetailResource
    from resources.pet import PetDetailResource

    api.add_resource(PetResource, '/api/pet')
    api.add_resource(UserResource, '/api/user')
    api.add_resource(PolicyResource, '/api/policy')
    api.add_resource(InsuredResource, '/api/insured')
    api.add_resource(ProposalResource, '/api/proposal')
    api.add_resource(ProviderResource, '/api/provider')
    api.add_resource(EmergencyResource, '/api/emergency')
    api.add_resource(PlanPolicyResource, '/api/planPolicy')
    api.add_resource(PetScheduleResource, '/api/petSchedule')
    api.add_resource(CollaboratorResource, '/api/collaborator')
    api.add_resource(PlanProposalResource, '/api/planProposal')
    api.add_resource(EmergencyInsuredResource, '/api/emergencyInsured')
    api.add_resource(EmergencyPetResource, '/api/emergencyPet')
    # api.add_resource(InsuredResource, '/api/insured')
    # api.add_resource(ProviderResource, '/api/provider')

    api.add_resource(PetDetailResource, '/api/pet/<int:id>')
    api.add_resource(UserDetailResource, '/api/user/<int:id>')
    api.add_resource(PolicyDetailResource, '/api/policy/<int:id>')
    api.add_resource(ProposalDetailResource, '/api/proposal/<int:id>')
    api.add_resource(PlanPolicyDetailResource, '/api/planPolicy/<int:id>')
    api.add_resource(PetScheduleDetailResource, '/api/petSchedule/<int:id>')
    api.add_resource(EmergencyDetailResource, '/api/emergency/<int:id>')
    api.add_resource(EmergencyPetDetailResource, '/api/emergencyPet/<int:id>')
    api.add_resource(PlanProposalDetailResource, '/api/planProposal/<int:id>')
    api.add_resource(EmergencyInsuredDetailResource, '/api/emergencyInsured/<int:id>')
    # api.add_resource(InsuredDetailResource, '/api/insured/<int:id>')
    # api.add_resource(ProviderDetailResource, '/api/provider/<int:id>')

    api.add_resource(UserPasswordRecoveryResource, '/api/user/recovery')
    api.add_resource(AuthenticationResource, '/api/login')


class HttpCode(IntEnum):
    Ok = 200
    BadRequest = 400
    Unauthorized = 401
    Forbidden = 403
    NotFound = 404
