from nearest import nearest_square 
from nearest import email_validator

def test_nearest_square():
    assert(nearest_square(5)==4)

def test_email_validator():
    assert(test_email_validator(ob@code.edu) == True)
def test_email_validator():
    assert(test_email_validator(jj@code) == True)