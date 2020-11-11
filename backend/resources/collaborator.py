from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_simple import jwt_required, get_jwt

from models.collaborator import CollaboratorModel


class CollaboratorResource(Resource):

    def _list_collaborator(self):

        collaborator = CollaboratorModel.list_all()

                
        return list(map(lambda collaborator: {
            'id': collaborator.id,
            'first_name':collaborator.first_name,
            'last_name': collaborator.last_name,
            'registration':collaborator.registration,
            'url_details': f'http://127.0.0.1:8080/api/user/{collaborator.user_id}'
            }, collaborator))
    
    
    def get(self):
        try:
            return self._list_collaborator()
        except Exception as e:
            return f"{e}", 500

    