from employee import Employee

def test_give_default_raise():
    emp = Employee("John", "Lart", 50000)
    emp.give_raise()
    assert emp.annual_salary == 50000

def test_give_custom_raise():
    emp = Employee("John", "Lart", 50000)
    emp.give_raise(8000)
    assert emp.annual_salary == 58000
