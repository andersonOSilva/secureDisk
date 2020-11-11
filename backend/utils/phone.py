import sqlite3
from datetime import date, datetime
from sqlalchemy.exc import SQLAlchemyError

from models.phone import PhoneModel

def insert_into_phone(item):
    try:    
        model = PhoneModel()
        model.phone = item['phone'] 
        model.webphone = item['webphone'] 
        model.branch_line = item['branch_line'] 
        model.status = item['status'] 
        model.user_id = item['user_id'] 
        model.created_date = date.today()
        model.save()

        return 201, 'created'
    except Exception as e:
        
        return {"succes":False, "message":f'{e} invalid payload','type_error':'phone/utils'}

def select_phone_by_id(id):
    phone = PhoneModel.get_by_id(id)
    
    if phone is None:
        return {'message': 'Phone not found'}, 404

    return {
        'id':phone.id,
        'phone':phone.phone,
        'webphone':phone.webphone,
        'branch_line':phone.branch_line,    
        'status':phone.status,
        'user_id':phone.user_id,
        'created_date':phone.created_date.strftime("%d/%m/%Y")
    }

def select_phone_by_user_id(id):
    phone = PhoneModel.get_by_id_user(id)
    
    if phone is None:
        return {'message': 'Phone not found'}, 404

    return {
        'id':phone.id,
        'phone':phone.phone,
        'webphone':phone.webphone,
        'branch_line':phone.branch_line,    
        'status':phone.status,
        'user_id':phone.user_id,
        'created_date':phone.created_date.strftime("%d/%m/%Y")
    }

