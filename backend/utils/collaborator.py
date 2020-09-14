from models.collaborator import CollaboratorModel
from datetime import date, datetime
from sqlalchemy.exc import SQLAlchemyError
import sqlite3

def insert_into_collaborator( item, user):
    try:
        if item:
            
            collaborator = CollaboratorModel()
            collaborator.first_name = item['first_name']
            collaborator.last_name = item['last_name']
            collaborator.cel = item['cel']
            collaborator.tel = item['tel']
            collaborator.cpf = item['cpf']
            collaborator.password = item['password']
            collaborator.user_id = user.id
            collaborator.save()

            return {"succes":True,"message":'Collaborator created'}
        else:
            user.delete()
            return {"succes":False, "message":'Not created collaborator, invalid payload'}
    
    except Exception as e:
        user.delete()
        return {"succes":False, "message":f'{e} invalid payload','type_error':'collaborator/utils'}




def select_collaborator_by_user_id( user):
    try:
        collaborator = CollaboratorModel.get_by_user_id(user.id)

        if collaborator is None:
            return {'success':False,'message': 'Collaborator not found'}
        else:
            return {
                'id': collaborator.id,
                'first_name':collaborator.first_name,
                'last_name': collaborator.last_name,
                'cpf':collaborator.cpf,
                'tel':collaborator.tel,
                'cel':collaborator.cel
            }

    except Exception as e:
        return {"succes":False, "message":f'{e} inssvalid payload'}


# @jwt_required
def update_collaborator( item, user):

    try:
        if item:
            collaborator = CollaboratorModel.get_by_user_id(user.id)

            if 'first_name' in item:
                collaborator.first_name = item['first_name']
            if 'last_name' in item:
                collaborator.last_name = item['last_name']
            if 'email' in item:
                collaborator.email = item['email']
            if 'cpf' in item:
                collaborator.cpf = item['cpf']
            if 'tel' in item:
                collaborator.tel = item['tel']
            if 'cel' in item:
                collaborator.cel = item['cel']
            if 'status' in item:
                collaborator.status = item['status'] 
            if 'password' in item:
                collaborator.password = item['password']
            
            collaborator.save()
            return {"success":True,"message":'Collaborator edited'}
        else:
            user.delete()
            return {"success":False, "message":'Not edited collaborator, invalid payload'}
        
    
    except Exception as e:
        user.delete()
        return {"success":False, "message":f'{e} invalid payload','type_error':'collaborator/utils'}


def delete_collaborator( id):
    try:
        collaborator = CollaboratorModel.get_by_user_id(id)
        collaborator.delete()

        return {"success":True, "message":'collaborator deleted'}


    except Exception as e:
        return {"success":False, "message":f"{e}" }
