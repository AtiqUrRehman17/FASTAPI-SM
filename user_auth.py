from fastapi import FastAPI,Depends,Form,HTTPException,status
from fastapi.security import OAuth2PasswordBearer # used for user authentication

app = FastAPI()
oauth_schem = OAuth2PasswordBearer(tokenUrl='token')

# endpoints
@app.post('/token')
def login(username : str = Form(...), password:str = Form(...)):
    if username == 'john' and password == 'pass123':
        return {'access_token':'valid_token','token_type':'bearer'}
    raise HTTPException(status_code=400,detail='Invalid crdentials')

def decode_token(token:str):
    if token == 'valid_token':
        return {'name':'john'}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='invalid authentication credentils')



def get_currnt_user(token : str = Depends(oauth_schem)):
    return decode_token(token)



@app.get('/profile')
def get_profile(user:str = Depends(get_currnt_user)):
    return {'user':user['name']}

    