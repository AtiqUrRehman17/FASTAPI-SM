from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    id: int

@app.get("/user",response_model=User)
def get_user():
    return User(id=1,name='khan')