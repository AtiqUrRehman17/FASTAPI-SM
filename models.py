from pydantic import BaseModel

class Employee(BaseModel):
    id : int
    name : str
    deparment:str
    age : int


