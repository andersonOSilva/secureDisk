def user_validate(request):
    if 'email' not in request or not isinstance(request['email'], str):
        return {'success': False, 'message':'email'}
    if 'password' not in request or not isinstance(request['password'], str):
        return {'success': False, 'message':'password'}
    if 'type_user' not in request or not isinstance(request['type_user'], str):
        return {'success': False, 'message':'type_user'}

    if request['type_user'] == "insured":
        response = insured_validate(request)
    elif request['type_user'] == "provider":
       response = provider_validate(request)
    else:
        response = collaborator_validate(request)
    
    return response

def insured_validate(request):

    if 'first_name' not in request or not isinstance(request['first_name'], str):
        return {'success': False, 'message':'firs_name'}
    
    if 'last_name' not in request or not isinstance(request['last_name'], str):
        return {'success': False, 'message':'last_name'}
    
    if 'cpf' not in request or not isinstance(request['cpf'], str) or len(request['cpf']) > 14:
        return {'success': False, 'message':'cpf'}
        
    
    return {'success':True}

def provider_validate(request):

    if 'business_name' not in request or not isinstance(request['business_name'], str):
        return {'success': False, 'message':'business_name'}
    if 'fantasy_name' not in request or not isinstance(request['fantasy_name'], str):
        return {'success': False, 'message':'fantasy_name'}
    if 'cnpj' not in request or not isinstance(request['cnpj'], str) or len(request['cnpj']) > 19:
        return {'success': False, 'message':'cnpj'}
    
    return {'success':True}


def collaborator_validate(request):

    if 'first_name' not in request or not isinstance(request['first_name'], str):
        return {'success': False, 'message':'first_name'}

    if 'last_name' not in request or not isinstance(request['last_name'], str):
        return {'success': False, 'message':'last_name'}

    if 'cpf' not in request or not isinstance(request['cpf'], str) or len(request['cpf']) > 14:
        return {'success': False, 'message':'cpf'}
    
    return {'success':True}

def user_update_validate(request):
    if 'email' in request and not isinstance(request['email'], str):
        return {'success': False, 'message':'email'}
    if 'password' in request and not isinstance(request['password'], str):
        return {'success': False, 'message':'password'}
    if 'type_user' in request and not isinstance(request['type_user'], str):
        return {'success': False, 'message':'type_user'}

    if request['type_user'] == "insured":
        response = insured_update_validate(request)
    elif request['type_user'] == "provider":
       response = provider_update_validate(request)
    else:
        response = collaborator_update_validate(request)
    
    return response

def insured_update_validate(request):

    if 'first_name' in request and not isinstance(request['first_name'], str):
        return {'success': False, 'message':'firs_name'}
    
    if 'last_name' in request and not isinstance(request['last_name'], str):
        return {'success': False, 'message':'last_name'}
    
    if 'cpf' in request and not isinstance(request['cpf'], str) or 'cpf' in request and len(request['cpf']) > 14:
        return {'success': False, 'message':'cpf'}
        
    
    return {'success':True}

def provider_update_validate(request):

    if 'business_name' in request and not isinstance(request['business_name'], str):
        return {'success': False, 'message':'business_name'}
    if 'fantasy_name' in request and not isinstance(request['fantasy_name'], str):
        return {'success': False, 'message':'fantasy_name'}
    if 'cnpj' in request and not isinstance(request['cnpj'], str) or len(request['cnpj']) > 19:
        return {'success': False, 'message':'cnpj'}
    
    return {'success':True}


def collaborator_update_validate(request):

    if 'first_name' in request and not isinstance(request['first_name'], str):
        return {'success': False, 'message':'first_name'}

    if 'last_name' in request and not isinstance(request['last_name'], str):
        return {'success': False, 'message':'last_name'}

    if 'cpf' in request and not isinstance(request['cpf'], str) or 'cpf' in request and len(request['cpf']) > 14:
        return {'success': False, 'message':'cpf'}
    
    return {'success':True}

