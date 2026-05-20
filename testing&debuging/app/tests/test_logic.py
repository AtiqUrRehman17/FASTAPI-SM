import pytest
from ..logic import is_eligible_for_loan

def test_eligibale_user():
    assert is_eligible_for_loan(60000,25,'Employeed') == True

def test_underage_user():
    assert is_eligible_for_loan(55000,19,'Employeed') == False


def test_low_income():
    assert is_eligible_for_loan(5000,29,'Employeed') == False 

def test_unemployed_user():
    assert is_eligible_for_loan(55000,22,'UnEmployeed') == False

def test_boundry_case():
    assert is_eligible_for_loan(50000,21,'Employeed') == True