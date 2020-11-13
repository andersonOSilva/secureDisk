import sqlite3
from datetime import date, datetime
from sqlalchemy.exc import SQLAlchemyError

from models.phone import PhoneModel

def insert_into_phone(item,user_inserted):
    try:    
        model = PhoneModel()
        model.phone = item['phone'] 
        model.webphone = item['webphone'] 
        model.branch_line = item['branch_line'] 
        model.status = item['status'] 
        model.user_id = user_inserted.id 
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
    phone = PhoneModel.get_by_user_id(id)
    
    if phone is None:
        return {'message': 'Phone not found'}, 404

    return list(map(lambda phone:{
            'id':phone.id,
            'phone':phone.phone,
            'webphone':phone.webphone,
            'branch_line':phone.branch_line,
            'status':phone.status,
            # 'owner':select_user_by_id(phone.user_id)
        },phone))
    
def update_phone( item, user):

    try:
        if item:
            phone = PhoneModel.get_by_phone(item['phone_original']['phone'])

            if 'phone' in item['phone_edited']:
                phone.phone = item['phone_edited']['phone']
            if 'webphone' in item['phone_edited']:
                phone.webphone = item['phone_edited']['webphone']
            if 'branch_line' in item['phone_edited']:
                phone.branch_line = item['phone_edited']['branch_line']
            if 'status' in item['phone_edited']:
                phone.status = item['phone_edited']['status']
            if 'user_id' in item['phone_edited']:
                phone.user_id = item['phone_edited']['user_id']
            
            phone.save()
            return {"success":True,"message":'Phone edited'}
        else:
            return {"success":False, "message":'Not edited phone, invalid payload'}
        
    
    except Exception as e:
        return {"success":False, "message":f'{e} invalid payload','type_error':'phone/utils'}
