from datetime import datetime, timedelta,timezone
from authlib.jose import JoseError,jwt
from fastapi import HTTPException

# define the constants
SECRET_KEY = 'secret_key'
ALGORITHEM = 'HS256'
ACCESS_TOKEN_EXPIRY_MINUTES = 30

# LETS CREATE FUNCTIONS
def create_token(data:dict):
    header = {'algo':ALGORITHEM}
    expire = datetime.now(timezone.utc) + timedelta(ACCESS_TOKEN_EXPIRY_MINUTES)
    payload = data.copy()
    payload.update({'exp':expire})
    jwt.encode(header,payload,SECRET_KEY).decode('utf-8') # creating a token

# verifying the token
def verify_token(token:str):
    try:
        claims = jwt.decode(token,SECRET_KEY)
        claims.validate()
        username = claims.get('sub')
        if username is None:
            raise HTTPException(status_code=401, detail='token missing')
        return username
    except JoseError:
        raise HTTPException(status_code=401,detail='Could not validate Credentials')