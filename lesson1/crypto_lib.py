import hashlib

from passlib.context import CryptContext
pwd_context=CryptContext(schemes=['bcrypt'], deprecated='auto')
def encode_md5(value: str)-> str:
    value+="f"
    result = hashlib.md5(value.encode()).hexdigest()
    return result


def get_password_hash(password: str)->str:
    result=pwd_context.hash(password)
    return result
print(get_password_hash('1'))
def verify_password(password: str, hashed_password:str)-> bool:
    result= pwd_context.verify(password, hashed_password)
    return result
res= get_password_hash('1')
print(res)
h='$2b$12$yLpgG7amtCJqjzgWUqcRJ.NAp5eqzueGFTI5CcOVU.M0BgeOSVBCC'
print(verify_password('1',h))

