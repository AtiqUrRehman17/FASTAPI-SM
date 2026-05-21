from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_elegibale_pass():
    payload = {
        'income':60000,
        'age' : 22,
        'emplyement_status' : 'Employeed'
    }
    response = client.post('/loan_ligibility',json=payload)
    assert response.status_code == 200
    assert response.json() == {'eligiale':True}


def test_eligiable_fail():
    payload = {
        'income':45000,
        'age':18,
        'emplyement_status':'UnEmployeed'
    }
    client.post('/loan_ligibility',json=payload)
    response = client.post('/loan_ligibility',json=payload)
    assert response.status_code == 200
    assert response.json() == {'eligiale':False}