import hashlib
from .pet import *
from .email import *
from .policy import *
from .proposal import *
from .insured import *
from .provider import *
from .validator import *
from .collaborator import *
from .emergency import *

def encrypt(password):
    password += "çopademacaco"
    sha_signature = \
        hashlib.sha256(password.encode()).hexdigest()
    return sha_signature
 

