from fastapi import FastAPI, Header, HTTPException,Depends
import os
from pydantic_settings import BaseSettings

app = FastAPI()

class Settings(BaseSettings):
    API_KEY: str


    class Config:
        env_file = ".env"


settings = Settings()

def get_api_key(api_key: str = Header(...)):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return api_key

@app.get("/secure-data")
def read_secure_data(api_key: str = Depends(get_api_key)):
    return {"message": "This is secure data accessible only with a valid API key."}