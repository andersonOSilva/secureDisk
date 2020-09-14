from models.provider import ProviderModel
from datetime import date, datetime
from sqlalchemy.exc import SQLAlchemyError
import sqlite3

def insert_into_provider( item, user):
    try:
        if item:
            provider = ProviderModel()
            provider.business_name = item['business_name']
            provider.fantasy_name = item['fantasy_name']
            provider.cnpj = item['cnpj']
            provider.tel = item['tel']
            provider.cel = item['cel']
            # provider.password = item['password']
            provider.user_id = user.id
            provider.save()

            return {"succes":True,"message":'Provider created'}
        else:
            user.delete()
            return {"succes":False, "message":'Not created provider, invalid payload'}
    
    except Exception as e:
        user.delete()
        return {"succes":False, "message":f'{e} invalid payload','type_error':'provider/utils'}




def select_provider_by_user_id( user):
    try:
        provider = ProviderModel.get_by_user_id(user.id)

        if provider is None:
            return {'success':False,'message': 'Provider not found'}
        else:
            return {
                'id': provider.id,
                'business_name':provider.business_name,
                'fantasy_name': provider.fantasy_name,
                'cnpj':provider.cnpj,
                'tel':provider.tel,
                'cel':provider.cel
            }
            return {"succes":True,"message":'Provider created'}

    except Exception as e:
        return {"succes":False, "message":f'{e} invalid payload'}


# @jwt_required
def update_provider( item, user):

    try:
        if item:
            provider = ProviderModel.get_by_user_id(user.id)

            if 'business_name' in item:
                provider.business_name = item['business_name']
            if 'fantasy_name' in item:
                provider.fantasy_name = item['fantasy_name']
            if 'cnpj' in item:
                provider.cnpj = item['cnpj']
            if 'tel' in item:
                provider.tel = item['tel']
            if 'cel' in item:
                provider.cel = item['cel']
            if 'status' in item:
                provider.status = item['status'] 
            if 'password' in item:
                provider.password = item['password']
            
            provider.save()
            return {"success":True,"message":'Provider edited'}
        else:
            user.delete()
            return {"success":False, "message":'Not edited provider, invalid payload'}
        
    
    except Exception as e:
        user.delete()
        return {"success":False, "message":f'{e} invalid payload','type_error':'provider/utils'}


def delete_provider( id):
    try:
        provider = ProviderModel.get_by_user_id(id)
        provider.delete()

        return {"success":True, "message":'provider deleted'}


    except Exception as e:
        return {"success":False, "message":f"{e}" }
