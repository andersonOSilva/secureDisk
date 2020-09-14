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
    from resources.user import UserResource
    from resources.pet import PetResource
    
    # from resources.provider import ProviderDetailResource
    # from resources.insured import InsuredDetailResource
    from resources.user import UserDetailResource
    from resources.pet import PetDetailResource

    api.add_resource(PetResource, '/api/pet')
    api.add_resource(UserResource, '/api/user')
    # api.add_resource(InsuredResource, '/api/insured')
    # api.add_resource(ProviderResource, '/api/provider')

    api.add_resource(PetDetailResource, '/api/pet/<int:id>')
    api.add_resource(UserDetailResource, '/api/user/<int:id>')
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
