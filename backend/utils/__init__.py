from .insured import *
from .collaborator import *
from .provider import *
from .validator import *
from .email import *
import hashlib

def encrypt(password):
    password += "çopademacaco"
    sha_signature = \
        hashlib.sha256(password.encode()).hexdigest()
    return sha_signature
 

