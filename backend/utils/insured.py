from models.insured import InsuredModel
from datetime import date, datetime
from sqlalchemy.exc import SQLAlchemyError
import sqlite3

def insert_into_insured( item, user):
    try:
        if item:
            
            insured = InsuredModel()
            insured.first_name = item['first_name']
            insured.last_name = item['last_name']
            insured.cel = item['cel']
            insured.tel = item['tel']
            insured.cpf = item['cpf']
            insured.password = item['password']
            insured.user_id = user.id
            insured.save()

            return {"succes":True,"message":'Insured created'}
        else:
            user.delete()
            return {"succes":False, "message":'Not created insured, invalid payload'}
    
    except Exception as e:
        user.delete()
        return {"succes":False, "message":f'{e} invalid payload','type_error':'insured/utils'}




def select_insured_by_user_id( user):
    try:
        insured = InsuredModel.get_by_user_id(user.id)

        if insured is None:
            return {'success':False,'message': 'Insured not found'}
        else:
            return {
                'id': insured.id,
                'first_name':insured.first_name,
                'last_name': insured.last_name,
                'cpf':insured.cpf,
                'tel':insured.tel,
                'cel':insured.cel
            }
            

    except Exception as e:
        return {"succes":False, "message":f'{e} invalid payload'}


# @jwt_required
def update_insured( item, user):

    try:
        if item:
            insured = InsuredModel.get_by_user_id(user.id)

            if 'first_name' in item:
                insured.first_name = item['first_name']
            if 'last_name' in item:
                insured.last_name = item['last_name']
            if 'email' in item:
                insured.email = item['email']
            if 'cpf' in item:
                insured.cpf = item['cpf']
            if 'tel' in item:
                insured.tel = item['tel']
            if 'cel' in item:
                insured.cel = item['cel']
            if 'status' in item:
                insured.status = item['status'] 
            if 'password' in item:
                insured.password = item['password']
            
            insured.save()
            return {"success":True,"message":'Insured edited'}
        else:
            user.delete()
            return {"success":False, "message":'Not edited insured, invalid payload'}
        
    
    except Exception as e:
        user.delete()
        return {"success":False, "message":f'{e} invalid payload','type_error':'insured/utils'}


def delete_insured( id):
    try:
        insured = InsuredModel.get_by_user_id(id)
        insured.delete()

        return {"success":True, "message":'insured deleted'}


    except Exception as e:
        return {"success":False, "message":f"{e}" }
