from fastapi import FastAPI,Depends

app = FastAPI()

# dependency connection function
def get_db():
    db = {'connection':'Mock_conection_db'} # ths is the line where we wite the db estalishement.but here we have ony dict
    try:
        yield db
    finally:
        db.close()

# endpoint
@app.get('/home')
def home(db=Depends(get_db)):
    return {'status':db['connection']}