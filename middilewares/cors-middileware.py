from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    all_origins = [
        'http://frontend.com','http://my-app.com'
    ],
    allow_credentials = True,
    allow_methods = ['GET','POST','PUT','DELETE'],
    allow_headers = ['*']
    )