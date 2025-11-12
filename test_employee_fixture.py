import pytest

from employee import Employee 

@pytest.fixture
def employee():
    return Employee('Alice', 'Brown', 70000)

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 75000

def test_give_custom_raise(employee):
    employee.give_raise(15000)
    assert employee.annual_salary == 85000