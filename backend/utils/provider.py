import sqlite3
from datetime import date, datetime
from sqlalchemy.exc import SQLAlchemyError

from models.provider import ProviderModel

def insert_into_provider( item, user):
    try:
        if item:
            provider = ProviderModel()
            provider.business_name = item['business_name']
            provider.fantasy_name = item['fantasy_name']
            provider.type_provider = item['type_provider']
            provider.cnpj = item['cnpj']
            provider.address = item['address']
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


def select_provider_by_id(id):
    try:
        provider = ProviderModel.get_by_id(id)
        
        if provider is None:
            return {'success':False,'message': 'Provider not found'}
        else:
            return {
                'id': provider.id,
                'business_name':provider.business_name,
                'fantasy_name': provider.fantasy_name,
                'cnpj':provider.cnpj,
                'tel':provider.tel,
                'address':provider.address,
                'type_provider':provider.type_provider
            }
            return {"succes":True,"message":'Provider found'}

    except Exception as e:
        return {"succes":False, "message":f'{e} invalid payload'}

def select_provider_by_user_id( user_id):
    try:
        provider = ProviderModel.get_by_user_id(user_id)

        if provider is None:
            return {'success':False,'message': 'Provider not found'}
        else:
            return {
                'id': provider.id,
                'business_name':provider.business_name,
                'fantasy_name': provider.fantasy_name,
                'cnpj':provider.cnpj,
                'tel':provider.tel,
                'address':provider.address,
                'type_provider':provider.type_provider,
                
            }
            return {"succes":True,"message":'Provider found'}

    except Exception as e:
        return {"succes":False, "message":f'{e} invalid payload'}


# @jwt_required
def update_provider( item, user):
    print(item)
    try:
        if item:
            provider = ProviderModel.get_by_user_id(user.id)

            if 'business_name' in item:
                provider.business_name = item['business_name']
            if 'fantasy_name' in item:
                provider.fantasy_name = item['fantasy_name']
            if 'type_provider' in item:
                provider.type_provider = item['type_provider']
            if 'cnpj' in item:
                provider.cnpj = item['cnpj']
            if 'tel' in item:
                provider.tel = item['tel']
            if 'cel' in item:
                provider.cel = item['cel']
            if 'address' in item:
                provider.address = item['address']
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
